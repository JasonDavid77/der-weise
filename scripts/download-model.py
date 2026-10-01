"""
download-model.py -- das Sprachmodell einmalig in <WEISE_HOME>/modelle laden.

Einziges Skript, das ins Netz geht (huggingface.co), und nur dann, wenn das
Modell noch fehlt. Liegt es schon da (geladen oder von Hand nach
<WEISE_HOME>/modelle entpackt), wird offline nur geprueft. Erzwungenes
Neuladen: vorher $env:WEISE_ONLINE = "1" setzen.

Aufruf (PowerShell):
  & "<WEISE_HOME>\\venv\\Scripts\\python.exe" "<WEISE_HOME>\\scripts\\download-model.py"
"""

import os

import weise_config as cfg  # setzt Offline-Betrieb, wenn das Modell schon da ist


def folder_size_mb(path) -> float:
    total = 0
    for root, _dirs, files in os.walk(path):
        for name in files:
            try:
                total += os.path.getsize(os.path.join(root, name))
            except OSError:
                pass
    return total / 1024 / 1024


def main() -> None:
    print(f"Modell:  {cfg.EMBEDDING_MODEL}")
    print(f"Ziel:    {os.environ['HF_HOME']}")
    if os.environ.get("HF_HUB_OFFLINE") == "1":
        print("Modell liegt schon lokal -- nur Pruefung, kein Download.")
    else:
        print("Modell fehlt -- Download von huggingface.co (rund 0,5 GB) ...")
    from sentence_transformers import SentenceTransformer
    from transformers import AutoTokenizer
    model = SentenceTransformer(cfg.EMBEDDING_MODEL)
    AutoTokenizer.from_pretrained(cfg.EMBEDDING_MODEL)
    vec = model.encode(["Probe: Der Weise lernt lokal."])
    print(f"Probe:   Vektor mit {vec.shape[1]} Werten berechnet")
    print(f"Fenster: {model.max_seq_length} Token je Abschnitt")
    model_dir = os.path.join(os.environ["HF_HOME"], "hub",
                             "models--" + cfg.EMBEDDING_MODEL.replace("/", "--"))
    print(f"Groesse: {folder_size_mb(model_dir):.0f} MB ({model_dir})")
    print("OK: Modell liegt lokal. Alle anderen Skripte laufen ab jetzt offline.")


if __name__ == "__main__":
    main()
