"""
learn-store.py -- Wissen eines Lernthemas in den Speicher legen (Ingest).

Ein Befehl, vier Ziele:
  1. Werkraum         <werkraum>/<thema>/   (die Dateien selbst, Quelle der Wahrheit)
  2. Themen-Sicht     Filter thema=<name>   }  EIN Schreibvorgang in die
  3. Gesamtbestand    ohne Filter           }  Sammlung "wissen" (Etikett: thema)
  4. Werkzeug-Register  <werkraum>/werkzeug-register.md  (--register)

Aufruf (PowerShell):
  & "<WEISE_HOME>\\venv\\Scripts\\python.exe" "<WEISE_HOME>\\scripts\\learn-store.py" --thema <name>
  ... learn-store.py --register
  ... learn-store.py --thema <name> --register

Ingestiert je Thema: synthesis.md + sources/ (*.md, *.txt, rekursiv).
Ausgeschlossen: _index.md, concepts.md, questions.md, learner-state.md,
updates.md, ui-observed.md (liest der Weise direkt als Datei), auftraege/,
eingang/, uebungen/ (Arbeitsmaterial), sources/_archive/ (Ueberholtes:
der Speicher kennt nur den aktuellen Stand).
Idempotent: die Abschnitte des Themas werden vollstaendig ersetzt.
"""

import os
import re
import json
import time
import hashlib
import tempfile
import argparse
from pathlib import Path

import weise_config as cfg
from chunking import chunk_text, fit_to_model

INGEST_FILES = ("synthesis.md",)
INGEST_DIRS = ("sources",)
EXCLUDE_NAMES = {"readme.md", "_index.md", "claude.md"}
ARCHIVE_DIR = "_archive"
REGISTER_CATEGORY = "learn-register"
BATCH = 1000


def collect_topic_files(topic_dir: Path) -> tuple[list[Path], list[Path]]:
    """(ingestierbar, uebersprungen). Uebersprungen = alles in sources/, das
    kein .md/.txt ist -- muss erst in Text ueberfuehrt werden, sonst fehlt es
    still im Speicher."""
    files = [topic_dir / n for n in INGEST_FILES if (topic_dir / n).is_file()]
    skipped = []
    for sub in INGEST_DIRS:
        d = topic_dir / sub
        if not d.is_dir():
            continue
        for p in sorted(d.rglob("*")):
            if not p.is_file() or p.name.lower() in EXCLUDE_NAMES:
                continue
            if any(part.lower() == ARCHIVE_DIR for part in p.relative_to(d).parts):
                continue
            (files if p.suffix.lower() in (".md", ".txt") else skipped).append(p)
    return files, skipped


def build_chunks(files: list[Path], thema: str, root: Path):
    ids, docs, metas, longest = [], [], [], 0
    for f in files:
        text = f.read_text(encoding="utf-8-sig", errors="replace")
        rel_root = str(f.relative_to(root)).replace("\\", "/")
        rel_topic = str(f.relative_to(root / thema)).replace("\\", "/")
        stand = re.match(r"^(\d{4}-\d{2}-\d{2})", f.name)
        pieces = fit_to_model(chunk_text(text))
        for i, (chunk, n_tok) in enumerate(pieces):
            ids.append(f"learn:{thema}:{rel_topic}:{i:04d}")
            docs.append(chunk)
            meta = {"source_file": rel_root, "thema": thema, "category": "learn",
                    "chunk_index": i, "tokens": n_tok}
            if stand:
                meta["stand"] = stand.group(1)
            metas.append(meta)
            longest = max(longest, n_tok)
        print(f"  {rel_topic}: {len(pieces)} Abschnitte")
    return ids, docs, metas, longest


def upsert_batched(col, ids, docs, metas) -> None:
    for i in range(0, len(ids), BATCH):
        col.upsert(ids=ids[i:i + BATCH], documents=docs[i:i + BATCH],
                   metadatas=metas[i:i + BATCH])


def collection(client, emb_fn):
    return client.get_or_create_collection(name=cfg.COLLECTION_NAME,
                                           embedding_function=emb_fn,
                                           metadata={"hnsw:space": "cosine"})


def ingest_topic(client, emb_fn, thema: str, root: Path):
    topic_dir = root / thema
    if not topic_dir.is_dir():
        raise SystemExit(f"[fehler] Thema nicht gefunden: {topic_dir}")
    files, skipped = collect_topic_files(topic_dir)
    for p in skipped:
        print(f"[WARNUNG] UEBERSPRUNGEN (kein .md/.txt): {p.relative_to(topic_dir)}"
              f" -- erst in Text ueberfuehren, sonst fehlt dieses Wissen im Speicher.")
    if not files:
        raise SystemExit(f"[fehler] Nichts zu speichern in {topic_dir} (synthesis.md und sources/ leer)")

    print(f"Abschnitte fuer thema={thema} bilden ...")
    ids, docs, metas, longest = build_chunks(files, thema, root)
    if not ids:
        raise SystemExit("[fehler] 0 Abschnitte erzeugt (Dateien leer?) -- Abbruch vor jedem Loeschen.")

    col = collection(client, emb_fn)
    try:
        col.delete(where={"$and": [{"category": "learn"}, {"thema": thema}]})
    except Exception as e:
        raise SystemExit(f"[fehler] Alte Abschnitte von {thema} liessen sich nicht loeschen: {e}")
    upsert_batched(col, ids, docs, metas)
    return files, len(ids), longest


def ingest_register(client, emb_fn, root: Path) -> int:
    reg = root / cfg.REGISTER_NAME
    if not reg.is_file():
        raise SystemExit(f"[fehler] Register fehlt: {reg}")
    pieces = fit_to_model(chunk_text(reg.read_text(encoding="utf-8-sig", errors="replace")))
    if not pieces:
        raise SystemExit("[fehler] Register leer -- Abbruch vor jedem Loeschen.")
    col = collection(client, emb_fn)
    try:
        col.delete(where={"category": REGISTER_CATEGORY})
    except Exception as e:
        raise SystemExit(f"[fehler] Register liess sich nicht ersetzen: {e}")
    upsert_batched(col,
                   [f"learn-register:{i:04d}" for i in range(len(pieces))],
                   [c for c, _ in pieces],
                   [{"source_file": cfg.REGISTER_NAME, "category": REGISTER_CATEGORY,
                     "chunk_index": i, "tokens": n} for i, (_, n) in enumerate(pieces)])
    return len(pieces)


def write_json_atomic(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=str(path.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=1)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, str(path))
    finally:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except OSError:
                pass


def update_manifest(thema, files, n_chunks, longest, n_register, root: Path) -> None:
    manifest = {}
    if cfg.MANIFEST_PATH.is_file():
        try:
            manifest = json.loads(cfg.MANIFEST_PATH.read_text(encoding="utf-8"))
        except Exception:
            print("[hinweis] manifest.json unlesbar -- wird neu aufgebaut")
    today = time.strftime("%Y-%m-%d")
    chunking = f"{cfg.CHUNK_SIZE}/{cfg.CHUNK_OVERLAP} Zeichen, max {cfg.TOKEN_LIMIT} Token"
    if thema:
        manifest[thema] = {
            "datum": today, "abschnitte": n_chunks, "laengster_abschnitt_token": longest,
            "modell": cfg.EMBEDDING_MODEL, "chunking": chunking,
            "dateien": {str(f.relative_to(root)).replace("\\", "/"):
                        hashlib.sha256(f.read_bytes()).hexdigest()[:16] for f in files},
        }
    if n_register:
        manifest["_register"] = {"datum": today, "abschnitte": n_register}
    write_json_atomic(cfg.MANIFEST_PATH, manifest)


def main() -> None:
    parser = argparse.ArgumentParser(description="Lernthema in den Speicher legen")
    parser.add_argument("--thema", help="Ordnername des Themas im Werkraum")
    parser.add_argument("--register", action="store_true",
                        help="werkzeug-register.md in den Speicher legen")
    args = parser.parse_args()
    if not args.thema and not args.register:
        parser.error("--thema und/oder --register angeben")
    if args.thema and not cfg.topic_name_ok(args.thema):
        parser.error(f"--thema '{args.thema}': nur Kleinbuchstaben, Ziffern, Bindestriche")

    root = cfg.werkraum()
    start = time.time()
    client, emb_fn = cfg.client(), cfg.embedding_function()
    files, n_topic, longest, n_register = [], 0, 0, 0
    if args.thema:
        files, n_topic, longest = ingest_topic(client, emb_fn, args.thema, root)
    if args.register:
        n_register = ingest_register(client, emb_fn, root)
    update_manifest(args.thema, files, n_topic, longest, n_register, root)

    total = client.get_collection(cfg.COLLECTION_NAME).count()
    print(f"\n--- SPEICHER-BERICHT ({time.time() - start:.1f}s) ---")
    if args.thema:
        print(f"Werkraum:  {root / args.thema} -- {len(files)} Dateien")
        print(f"Thema:     thema={args.thema} -- {n_topic} Abschnitte (ersetzt)")
        print(f"Laengster Abschnitt: {longest} Token (Grenze {cfg.TOKEN_LIMIT}) -- abgeschnitten: 0")
    if args.register:
        print(f"Register:  {cfg.REGISTER_NAME} -- {n_register} Abschnitte")
    print(f"Gesamt:    Sammlung '{cfg.COLLECTION_NAME}' -- {total} Abschnitte")


if __name__ == "__main__":
    main()
