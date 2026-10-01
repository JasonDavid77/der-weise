# learner-state.md (liegt im Themen-Ordner)

Ausgelagert aus `../SKILL.md` (Abschnitt 8). Gilt in jeder Lern-Session.
`${CLAUDE_PLUGIN_ROOT}` = Plugin-Ordner, also der Ordner ueber `skills/`, aus dem diese Datei
gelesen wurde (in dieser Datei setzt Claude Code den Pfad nicht selbst ein).

```
# Lerner-State: <thema>

Lern-Anker / Deliverable: <konkretes Zielobjekt> -- <Ziel-Artefakt in 1 Zeile>
Projektordner: <Pfad zur Ablage des Projekts, falls es einen gibt>

| Konzept | Stand | Zuletzt | Notiz |
|---|---|---|---|
| <konzept> | neu / wackelig / sitzt / Uebung | YYYY-MM-DD | <1 Zeile> |

## Deliverable-Spur
| # | Baustein | Aus Konzept | Status |
|---|---|---|---|
| 1 | <Baustein> | K<x> | offen / im Bau / fertig / Uebung / entfaellt <Datum> |

## Geparkte Fragen
- [ ] <Frage> (K<x>, geparkt YYYY-MM-DD)

## Session-Log
- YYYY-MM-DD: <1 Zeile: was geprueft, was haengt, welcher Baustein gewachsen,
  Modus NORMAL/TEMPO, Nachzug ja/nein>
```

Wird nicht gespeichert -- der Weise liest es als Datei. **"sitzt" haengt an der
Kartendatei, die das Thema nutzt (s.u.):** mit `recall-cards.json` = FSRS-
Abrufwahrscheinlichkeit > 0.9 bei Stabilitaet >= 7 Tagen (`learn-recall.py
--list` zeigt beides); mit `recall-cards.md` = alle Karten des Konzepts in Fach 4
oder 5 und ihre letzte Bewertung good oder easy. Der Weise SETZT "sitzt" NIE nach
Gefuehl. Deliverable-Status setzt er direkt, mit genau den Werten der Tabelle (=
Board-Marker `[ ]` / `[~]` / `[x]` / `-- Uebung --`). Kalibrierungs-Notizen in die
Notiz-Spalte.

**Welche Kartendatei gilt (je Thema genau EINE, in beiden Betriebsarten):**
- Liegt `recall-cards.md` vor, ist SIE die Kartendatei -- auch in VOLL, bis ihre
  Uebernahme nach FSRS erledigt ist (eigener Schritt, per /weise:vorschlag melden). So
  geht beim Umstieg auf VOLL keine Karte verloren.
- Liegt nur `recall-cards.json` vor: VOLL nutzt sie ueber `learn-recall.py`.
  OHNE PYTHON wird sie beim ersten Recall einmal nach `recall-cards.md`
  uebernommen (Fach 2, "Naechste Abfrage" = Datum aus `card.due`, UTC, Konzept
  aus der Frage erschliessen) und bleibt danach unveraendert liegen; ab dann gilt
  die md-Datei.
- Jede gestellte Karte wird in IHRER Kartendatei fortgeschrieben, auch beim
  Interleaving (Karte eines anderen Themas) und im Recall des Skills `thema`.

**`recall-cards.md`** im Themen-Ordner (Vorlage
`${CLAUDE_PLUGIN_ROOT}/skills/thema/template/recall-cards.md`), eine Zeile je
Karte:

```
| Nr | Konzept | Frage | Fach | Naechste Abfrage | Verlauf |
|---|---|---|---|---|---|
| 1 | K3 | <Frage> | 1 | YYYY-MM-DD | YYYY-MM-DD good; ... |
```

**Faecher-Regel:** Abstand je Fach: 1 = 1 Tag, 2 = 3 Tage, 3 = 7 Tage,
4 = 16 Tage, 5 = 35 Tage. Nach der Antwort: again -> Fach 1 | hard -> Fach
bleibt | good -> Fach + 1 | easy -> Fach + 2 (hoechstens 5). "Naechste Abfrage"
= heute + Abstand des neuen Fachs; im Verlauf Datum und Bewertung anhaengen.
Faellig ist, was "Naechste Abfrage" heute oder frueher hat.
