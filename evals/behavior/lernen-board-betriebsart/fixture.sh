#!/usr/bin/env bash
# Scaffold fuer den Eval-Fall lernen-board-betriebsart (laeuft nur mit --scaffold).
# Baut im leeren Arbeitsverzeichnis den Test-Technik-Ordner weise-home/ mit Profil und einem
# erfundenen Lernthema. Es gibt kein venv, die erwartete Betriebsart ist also OHNE PYTHON.
set -eu

wd="$(pwd -W 2>/dev/null || pwd)"
heute="$(date +%Y-%m-%d)"
naechstes_jahr="$(( $(date +%Y) + 1 ))"

werkraum="weise-home/themen"
thema="$werkraum/test-statistics-basics"
mkdir -p "$thema/sources" "$thema/auftraege" "$thema/eingang"

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
| test-statistics-basics | TEST: eine erfundene Umfrage mit Mittelwert, Median und Spannweite auswerten | TEST-Umfrage (erfunden) | [SYNTHESE] | 2026-09-01 |
EOF

cat > "$werkraum/werkzeug-register.md" <<'EOF'
# Werkzeug-Register

| Werkzeug | Art | Zugriff (gespeichert / live) | Vertrauen | Themen | Gefunden ueber | Status |
|---|---|---|---|---|---|---|
EOF

cat > "$thema/_index.md" <<EOF
# Lernthema: TEST Statistik-Grundlagen

| Feld | Wert |
|---|---|
| Status | [SYNTHESE] |
| Gestartet | 2026-09-01 |
| Speicher | ohne Python: nur Dateien (Stichwortsuche) |
| Verknuepfungen | keine (Quellen-Scan 2026-09-01: Fehlanzeige) |
| Volatilitaet | niedrig (12 Monate), Grundbegriffe aendern sich nicht |
| Letzter Ingest | $heute (Datei-Betrieb) |
| Praxis-Modus | aus |

## Lernziel (Working Backwards)

Wenn dieses Thema gefestigt ist, kann die Person:

1. Mittelwert, Median und Spannweite fuer eine kleine Zahlenreihe erklaeren und berechnen.
2. Eine erfundene TEST-Umfrage auf einer halben Seite auswerten.

## Doc-Index

| Datei | Inhalt | Pflichtlektuere? |
|---|---|---|
| synthesis.md | Verstaendnis in eigenen Worten | JA, bei jeder Themen-Session |
| questions.md | Fragen-Stack + Recall-Kandidaten | JA, bei jeder Themen-Session |
| concepts.md | Lernpfad | JA, vom Weisen je Session |
| learner-state.md | Anker, Lernstand, Deliverable-Spur, Session-Log | vom Weisen, je Session |
| updates.md | Was sich geaendert hat | vom Weisen fuer Delta-Recall |
| recall-cards.md | Abfrage-Karten nach der Faecher-Regel | vom Weisen je Session |
| sources/2026-09-01-test-grundbegriffe.md | Erfundene TEST-Notiz zu Lageparametern | nach Bedarf |

## Log

- 2026-09-01: Thema angelegt (TEST, erfunden).
EOF

cat > "$thema/concepts.md" <<'EOF'
# Konzept-Karte: TEST Statistik-Grundlagen (Stundenplan)

| # | Konzept | Kern in einem Satz | Braucht |
|---|---|---|---|
| 1 | Mittelwert | Summe aller Werte geteilt durch ihre Anzahl. | -- |
| 2 | Median | Der mittlere Wert der sortierten Reihe. | 1 |
| 3 | Spannweite | Groesster minus kleinster Wert. | 1 |
EOF

cat > "$thema/learner-state.md" <<'EOF'
# Lerner-State: TEST Statistik-Grundlagen

Lern-Anker / Deliverable: TEST-Umfrage (erfunden, 9 Antworten) -- halbseitige Auswertung mit Mittelwert, Median und Spannweite
Projektordner: keiner (TEST)

| Konzept | Stand | Zuletzt | Notiz |
|---|---|---|---|
| K1 Mittelwert | sitzt | 2026-09-02 | -- |
| K2 Median | wackelig | 2026-09-02 | mit dem Mittelwert verwechselt |
| K3 Spannweite | neu | -- | -- |

## Deliverable-Spur
| # | Baustein | Aus Konzept | Status |
|---|---|---|---|
| 1 | Kennzahl Mittelwert der TEST-Umfrage | K1 | fertig |
| 2 | Kennzahl Median der TEST-Umfrage | K2 | im Bau |
| 3 | Kennzahl Spannweite der TEST-Umfrage | K3 | offen |

## Geparkte Fragen

## Session-Log
- 2026-09-01: Thema angelegt.
- 2026-09-02: Session 1, K1 gefestigt, K2 begonnen.
EOF

cat > "$thema/questions.md" <<'EOF'
# Fragen-Stack: TEST Statistik-Grundlagen

## Offen

## Beantwortet

- [x] Was ist der Mittelwert? -> synthesis.md#kernkonzepte (2026-09-02)

## Recall-Kandidaten

- Was ist der Median der Reihe 1, 3, 9?
EOF

cat > "$thema/recall-cards.md" <<EOF
# Abfrage-Karten: TEST Statistik-Grundlagen (Faecher-Regel)

| Nr | Konzept | Frage | Fach | Naechste Abfrage | Verlauf |
|---|---|---|---|---|---|
| 1 | K1 Mittelwert | Wie berechnet man den Mittelwert einer Zahlenreihe? | 3 | $naechstes_jahr-01-15 | 2026-09-02 good |
EOF

cat > "$thema/synthesis.md" <<'EOF'
# Synthese: TEST Statistik-Grundlagen

## Kernkonzepte

- Mittelwert: Summe geteilt durch Anzahl; reagiert stark auf Ausreisser. [sources/2026-09-01-test-grundbegriffe.md]
- Median: mittlerer Wert der sortierten Reihe; robust gegen Ausreisser. [sources/2026-09-01-test-grundbegriffe.md]
- Spannweite: groesster minus kleinster Wert. [sources/2026-09-01-test-grundbegriffe.md]

## Zusammenhaenge

Liegen Mittelwert und Median weit auseinander, zieht vermutlich ein Ausreisser. (Hypothese)

## Was das fuer uns bedeutet

Fuer die TEST-Umfrage genuegen diese drei Kennzahlen.
EOF

cat > "$thema/updates.md" <<'EOF'
# Update-Log: TEST Statistik-Grundlagen

(noch keine Eintraege)
EOF

cat > "$thema/sources/readme.md" <<'EOF'
# sources/ -- Kuratiertes Rohmaterial

Eine Datei je Quelle, Datum vorne. Jede Datei steht im Doc-Index der ../_index.md.
EOF

cat > "$thema/sources/2026-09-01-test-grundbegriffe.md" <<'EOF'
# TEST-Notiz: Lageparameter (erfunden, nur fuer Tests)

Mittelwert: Alle Werte addieren und durch ihre Anzahl teilen. Beispiel 2, 4, 9: (2+4+9)/3 = 5.
Median: Werte sortieren und den mittleren nehmen. Beispiel 2, 4, 9: Median 4. Bei gerader Anzahl
der Mittelwert der beiden mittleren Werte.
Spannweite: groesster minus kleinster Wert. Beispiel 2, 4, 9: 9 - 2 = 7.
EOF

cat > "$thema/auftraege/readme.md" <<'EOF'
# auftraege/ -- vom Weisen an die Person
EOF

cat > "$thema/eingang/readme.md" <<'EOF'
# eingang/ -- von der Person an den Weisen
EOF
