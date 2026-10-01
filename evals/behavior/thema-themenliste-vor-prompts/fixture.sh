#!/usr/bin/env bash
# Scaffold fuer den Eval-Fall thema-themenliste-vor-prompts (laeuft nur mit --scaffold).
# Baut im leeren Arbeitsverzeichnis den Test-Technik-Ordner weise-home/ mit vollstaendigem Profil
# (Recherche-Weg "werkzeug") und einem leeren Werkraum. Kein venv: Betriebsart OHNE PYTHON.
set -eu

wd="$(pwd -W 2>/dev/null || pwd)"

werkraum="weise-home/themen"
mkdir -p "$werkraum"

cat > weise-home/config.json <<EOF
{
  "format": 1,
  "werkraum": "$wd/weise-home/themen",
  "persona": "Der Weise",
  "anrede": "Sie",
  "nutzer": "TEST-Person",
  "zeichen": "",
  "recherche": "werkzeug"
}
EOF

cat > "$werkraum/_themen.md" <<'EOF'
# Lernthemen (Werkraum des Weisen)

| Thema | Lernziel in einer Zeile | Anker (Projekt) | Status | Gestartet |
|---|---|---|---|---|
EOF

cat > "$werkraum/werkzeug-register.md" <<'EOF'
# Werkzeug-Register

| Werkzeug | Art | Zugriff (gespeichert / live) | Vertrauen | Themen | Gefunden ueber | Status |
|---|---|---|---|---|---|---|
EOF
