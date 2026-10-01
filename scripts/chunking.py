"""
chunking.py -- Text in Abschnitte teilen, die vollstaendig ins Fenster des
Sprachmodells passen.

Hintergrund: Das Modell liest hoechstens 128 Token je Abschnitt und schneidet
den Rest stillschweigend ab. Mit 1000-Zeichen-Abschnitten fiel so gut die
Haelfte jedes Abschnitts aus der Suche (gemessen 2026-09-09). Hier gilt:
  1. chunk_text(): Absaetze, ueberlange Absaetze an Satzgrenzen, notfalls an
     Wortgrenzen geteilt; zu Abschnitten bis CHUNK_SIZE Zeichen zusammengelegt,
     mit CHUNK_OVERLAP Zeichen Ueberlappung.
  2. fit_to_model(): jeder Abschnitt wird mit dem echten Tokenizer gezaehlt und
     so lange halbiert, bis er hoechstens TOKEN_LIMIT Token hat.
"""

import re

from weise_config import CHUNK_SIZE, CHUNK_OVERLAP, TOKEN_LIMIT, EMBEDDING_MODEL

_SENTENCE_END = re.compile(r"(?<=[.!?:;])\s+")


def _split_long(para: str, size: int) -> list[str]:
    """Absatz laenger als size: an Satzgrenzen, notfalls an Wortgrenzen teilen."""
    pieces, buf = [], ""
    for sentence in _SENTENCE_END.split(para):
        while len(sentence) > size:
            if buf:
                pieces.append(buf)
                buf = ""
            cut = sentence.rfind(" ", 0, size)
            cut = cut if cut > size // 2 else size
            pieces.append(sentence[:cut].strip())
            sentence = sentence[cut:].strip()
        if buf and len(buf) + 1 + len(sentence) > size:
            pieces.append(buf)
            buf = sentence
        else:
            buf = f"{buf} {sentence}".strip()
    if buf:
        pieces.append(buf)
    return [p for p in pieces if p]


def chunk_text(text: str, size: int = CHUNK_SIZE, overlap: int = CHUNK_OVERLAP) -> list[str]:
    pieces = []
    for para in re.split(r"\n\s*\n+", text):
        para = para.strip()
        if not para:
            continue
        pieces.extend([para] if len(para) <= size else _split_long(para, size))

    chunks, cur = [], ""
    for piece in pieces:
        if cur and len(cur) + 2 + len(piece) > size:
            chunks.append(cur)
            tail = cur[-overlap:] if overlap else ""
            space = tail.find(" ")
            if 0 <= space < len(tail) - 1:
                tail = tail[space + 1:]          # Ueberlappung am Wortanfang
            cur = f"{tail}\n\n{piece}" if tail else piece
            if len(cur) > size:
                cur = piece                      # passt nicht: ohne Ueberlappung
        else:
            cur = f"{cur}\n\n{piece}" if cur else piece
    if cur.strip():
        chunks.append(cur)
    return chunks


_tokenizer = None


def token_count(text: str) -> int:
    global _tokenizer
    if _tokenizer is None:
        from transformers import AutoTokenizer
        _tokenizer = AutoTokenizer.from_pretrained(EMBEDDING_MODEL)
    return len(_tokenizer(text, add_special_tokens=False)["input_ids"])


def fit_to_model(chunks: list[str], limit: int = TOKEN_LIMIT) -> list[tuple[str, int]]:
    """Gibt [(abschnitt, token)] zurueck; jeder Abschnitt hat <= limit Token.
    Zu lange Abschnitte werden an der Wortgrenze nahe der Mitte halbiert."""
    out, stack = [], list(reversed(chunks))
    while stack:
        chunk = stack.pop()
        n = token_count(chunk)
        if n <= limit:
            out.append((chunk, n))
            continue
        mid = len(chunk) // 2
        cut = chunk.rfind(" ", 0, mid)
        if cut <= 0:
            cut = mid
        left, right = chunk[:cut].strip(), chunk[cut:].strip()
        stack.append(right)
        stack.append(left)
    return [(c, n) for c, n in out if c]
