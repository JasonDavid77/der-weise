"""
self-check.py -- Selbsttest des Weisen: Umgebung pruefen und einmal den ganzen
Weg echt durchlaufen (speichern, suchen, Abfrage-Karten).

Der Durchlauf arbeitet in einem Wegwerf-Ordner mit einem Probe-Thema. Der echte
Speicher und die echten Lernthemen werden NICHT beruehrt.

Aufruf (PowerShell):
  & "<WEISE_HOME>\\venv\\Scripts\\python.exe" "<WEISE_HOME>\\scripts\\self-check.py"

Ergebnis: je Punkt OK / HINWEIS / FEHLER, am Ende "Selbsttest bestanden" oder
nicht. Rueckgabewert 0 = bestanden, 1 = mindestens ein FEHLER.
"""

import os
import re
import sys
import shutil
import tempfile
import subprocess
import importlib.metadata as md
from pathlib import Path

import weise_config as cfg

EXPECTED = {"chromadb": "1.5.9", "sentence-transformers": "5.5.1",
            "torch": "2.12.1", "fsrs": "6.3.1"}
SCRIPTS = Path(__file__).resolve().parent

PROBE_SYNTHESIS = """# Synthese: Probe

## Tempo-Modus

Im Tempo-Modus wird unter Zeitdruck gebaut. Die Pruef-Frage kommt nicht mitten
im Bau, sondern wird sichtbar auf einen Parkplatz gestellt und in der naechsten
Wartezeit gestellt, zum Beispiel waehrend ein Testlauf rechnet.

## Lernpfad

Der Lernpfad waechst mit dem Projekt. Kommt eine neue Station dazu, nimmt der
Weise den fehlenden Lernschritt in den Lernpfad auf und zeigt es im Board.
"""

# Ein einziger sehr langer Absatz ohne Leerzeile: prueft, dass ueberlange
# Absaetze geteilt werden und kein Abschnitt das Modellfenster ueberschreitet.
PROBE_LONG = ("Dieser Absatz ist absichtlich sehr lang und hat keine Leerzeile, "
              "damit der Selbsttest sieht, ob lange Texte sauber geteilt werden. ") * 30

RESULTS = []


def mark(status: str, text: str) -> None:
    RESULTS.append(status)
    print(f"[{status:7}] {text}")


def run(args: list[str], env: dict) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, *args], env=env, capture_output=True,
                          text=True, encoding="utf-8", errors="replace", timeout=900)


def check_environment() -> None:
    v = sys.version_info
    if (v.major, v.minor) == (3, 12):
        mark("OK", f"Python {v.major}.{v.minor}.{v.micro}")
    else:
        mark("HINWEIS", f"Python {v.major}.{v.minor}.{v.micro} (getestet ist 3.12)")

    for pkg, want in EXPECTED.items():
        try:
            have = md.version(pkg)
        except md.PackageNotFoundError:
            mark("FEHLER", f"Paket {pkg} fehlt -- Installation wiederholen (/weise:einrichten)")
            continue
        if have.split("+")[0] == want:
            mark("OK", f"Paket {pkg} {have}")
        else:
            mark("HINWEIS", f"Paket {pkg} {have} (erwartet {want})")

    if cfg.model_cached():
        mark("OK", f"Sprachmodell liegt lokal ({os.environ['HF_HOME']})")
    else:
        mark("FEHLER", "Sprachmodell fehlt -- download-model.py ausfuehren (oder /weise:einrichten)")

    offline = os.environ.get("HF_HUB_OFFLINE") == "1"
    mark("OK" if offline else "HINWEIS",
         "Offline-Betrieb aktiv" if offline else "Offline-Betrieb erst nach dem Modell-Download aktiv")
    mark("OK" if os.environ.get("ANONYMIZED_TELEMETRY") == "False" else "FEHLER",
         "Telemetrie aus")

    root = cfg.werkraum()
    if cfg.CONFIG_PATH.is_file() and root.is_dir():
        mark("OK", f"Werkraum {root}")
    else:
        mark("HINWEIS", f"Werkraum {root} bzw. config.json fehlt noch (/weise:einrichten)")

    try:
        cfg.CHROMA_PATH.mkdir(parents=True, exist_ok=True)
        probe = cfg.CHROMA_PATH / ".schreibprobe"
        probe.write_text("ok", encoding="utf-8")
        probe.unlink()
        mark("OK", f"Speicher beschreibbar ({cfg.CHROMA_PATH})")
    except OSError as e:
        mark("FEHLER", f"Speicher nicht beschreibbar: {e}")


def check_roundtrip() -> None:
    if not cfg.model_cached():
        mark("FEHLER", "Durchlauf uebersprungen: ohne Modell kein Test")
        return
    tmp = Path(tempfile.mkdtemp(prefix="weise-selbsttest-"))
    try:
        topic = tmp / "themen" / "probe"
        (topic / "sources").mkdir(parents=True)
        (topic / "synthesis.md").write_text(PROBE_SYNTHESIS, encoding="utf-8")
        (topic / "sources" / "2026-01-01-langer-absatz.md").write_text(PROBE_LONG, encoding="utf-8")
        (tmp / "themen" / cfg.REGISTER_NAME).write_text(
            "# Werkzeug-Register\n\n| Werkzeug | Art | Zugriff |\n|---|---|---|\n"
            "| Probe-Werkzeug | Test | lokal |\n", encoding="utf-8")
        env = dict(os.environ, WEISE_HOME=str(tmp), WEISE_WERKRAUM=str(tmp / "themen"))

        r = run([str(SCRIPTS / "learn-store.py"), "--thema", "probe", "--register"], env)
        longest = re.search(r"Laengster Abschnitt: (\d+) Token", r.stdout)
        long_parts = re.search(r"2026-01-01-langer-absatz\.md: (\d+) Abschnitte", r.stdout)
        if r.returncode == 0 and longest and int(longest.group(1)) <= cfg.TOKEN_LIMIT:
            mark("OK", f"Speichern: laengster Abschnitt {longest.group(1)} Token, nichts abgeschnitten")
        else:
            mark("FEHLER", f"Speichern gescheitert:\n{r.stdout[-800:]}{r.stderr[-800:]}")
            return
        if long_parts and int(long_parts.group(1)) > 1:
            mark("OK", f"Langer Absatz in {long_parts.group(1)} Abschnitte geteilt")
        else:
            mark("FEHLER", "Langer Absatz wurde nicht geteilt")

        r = run([str(SCRIPTS / "query.py"), "Was passiert mit der Pruef-Frage, wenn es eilig ist?",
                 "--thema", "probe", "--n", "1"], env)
        if r.returncode == 0 and "Parkplatz" in r.stdout:
            mark("OK", "Suche im Thema findet den richtigen Abschnitt")
        else:
            mark("FEHLER", f"Suche im Thema:\n{r.stdout[-800:]}{r.stderr[-800:]}")

        r = run([str(SCRIPTS / "query.py"), "Probe-Werkzeug", "--alle", "--n", "3"], env)
        if r.returncode == 0 and "Probe-Werkzeug" in r.stdout:
            mark("OK", "Suche im ganzen Bestand findet auch das Register")
        else:
            mark("FEHLER", f"Suche im ganzen Bestand:\n{r.stdout[-800:]}{r.stderr[-800:]}")

        recall = str(SCRIPTS / "learn-recall.py")
        steps = [
            (["--thema", "probe", "--add", "Wohin kommt die Pruef-Frage im Tempo-Modus?"], "Karte #1 angelegt"),
            (["--thema", "probe", "--due"], "FAELLIG #"),
            (["--thema", "probe", "--review", "1", "--rating", "good"], "bewertet (good)"),
            (["--thema", "probe", "--list"], "ok      #"),
        ]
        for args, expect in steps:
            r = run([recall, *args], env)
            if r.returncode != 0 or expect not in r.stdout:
                mark("FEHLER", f"Abfrage-Karten ({args[2]}):\n{r.stdout[-600:]}{r.stderr[-600:]}")
                break
        else:
            mark("OK", "Abfrage-Karten: anlegen, faellig, bewerten, auflisten")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main() -> int:
    print(f"Selbsttest des Weisen -- WEISE_HOME={cfg.WEISE_HOME}\n")
    check_environment()
    check_roundtrip()
    fails = RESULTS.count("FEHLER")
    print()
    if fails:
        print(f"Selbsttest NICHT bestanden: {fails} Fehler. Fehlerbilder: /weise:einrichten oder "
              "https://github.com/JasonDavid77/der-weise/blob/main/docs/hilfe.md")
        return 1
    print(f"Selbsttest bestanden ({RESULTS.count('OK')} OK, {RESULTS.count('HINWEIS')} Hinweise).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
