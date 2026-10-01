"""
weise_config.py -- gemeinsame Einstellungen fuer alle Skripte des Weisen.

Einzige Quelle fuer Pfade, Modell und Abschnittsgroessen. Liegt in
<WEISE_HOME>/scripts/. WEISE_HOME ist der Technik-Ordner: Umgebungsvariable
WEISE_HOME, sonst %USERPROFILE%\\weise (macOS/Linux: ~/weise). Nie aus dem
Ort dieses Skripts abgeleitet.

Layout:
  <WEISE_HOME>/venv/         Python-Umgebung
  <WEISE_HOME>/scripts/      diese Skripte
  <WEISE_HOME>/speicher/     Wissensspeicher (ChromaDB) + manifest.json
  <WEISE_HOME>/modelle/      Sprachmodell (Hugging-Face-Cache)
  <WEISE_HOME>/config.json   Profil, darin {"werkraum": "<Ordner der Lernthemen>"}

Muss in jedem Skript VOR chromadb / sentence_transformers importiert werden,
weil hier die Umgebungsvariablen fuer Telemetrie und Offline-Betrieb gesetzt
werden.
"""

import os
import sys
import json
from pathlib import Path

WEISE_HOME = Path(os.environ.get("WEISE_HOME") or Path.home() / "weise")
CONFIG_PATH = WEISE_HOME / "config.json"
CHROMA_PATH = WEISE_HOME / "speicher"
MODEL_DIR = WEISE_HOME / "modelle"
MANIFEST_PATH = CHROMA_PATH / "manifest.json"

COLLECTION_NAME = "wissen"
EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
REGISTER_NAME = "werkzeug-register.md"   # liegt im Werkraum-Root

# Abschnittsgroessen. Das Modell liest hoechstens 128 Token je Abschnitt, zwei
# davon sind Steuerzeichen. 400 Zeichen deutscher Text sind rund 110 Token.
# chunking.fit_to_model() prueft zusaetzlich jeden Abschnitt mit dem echten
# Tokenizer und teilt weiter, bis er passt: kein Abschnitt wird abgeschnitten.
CHUNK_SIZE = 400
CHUNK_OVERLAP = 80
TOKEN_LIMIT = 126

# Datenschutz: keine Telemetrie. Nach dem ersten Laden arbeitet das Modell nur
# noch lokal (Offline-Schalter), ausser download-model.py setzt WEISE_ONLINE=1.
os.environ.setdefault("HF_HOME", str(MODEL_DIR))
os.environ["ANONYMIZED_TELEMETRY"] = "False"
os.environ["HF_HUB_DISABLE_TELEMETRY"] = "1"
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")


def model_cached() -> bool:
    """True, wenn das Modell im Cache liegt (Ordner snapshots nicht leer)."""
    snap = (Path(os.environ["HF_HOME"]) / "hub"
            / ("models--" + EMBEDDING_MODEL.replace("/", "--")) / "snapshots")
    return snap.is_dir() and any(snap.iterdir())


if os.environ.get("WEISE_ONLINE") != "1" and model_cached():
    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    os.environ.setdefault("HF_HUB_DISABLE_PROGRESS_BARS", "1")   # Ladebalken nur beim Download
    os.environ.setdefault("TRANSFORMERS_VERBOSITY", "error")

try:
    sys.stdout.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass


def load_config() -> dict:
    if CONFIG_PATH.is_file():
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8-sig"))
    return {}


def werkraum() -> Path:
    """Ordner mit den Lernthemen. Reihenfolge: WEISE_WERKRAUM, config.json,
    Standard <WEISE_HOME>/themen."""
    env = os.environ.get("WEISE_WERKRAUM")
    if env:
        return Path(env)
    cfg = load_config().get("werkraum")
    if cfg:
        return Path(os.path.expandvars(cfg))
    return WEISE_HOME / "themen"


def client():
    """ChromaDB-Client auf den lokalen Speicher, Telemetrie aus."""
    import chromadb
    from chromadb.config import Settings
    return chromadb.PersistentClient(path=str(CHROMA_PATH),
                                     settings=Settings(anonymized_telemetry=False))


def embedding_function():
    from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction
    return SentenceTransformerEmbeddingFunction(model_name=EMBEDDING_MODEL)


def topic_name_ok(name: str) -> bool:
    import re
    return re.fullmatch(r"[a-z0-9][a-z0-9-]*", name) is not None
