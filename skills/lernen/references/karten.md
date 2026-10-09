# learner-state.md (liegt im Themen-Ordner)

Ausgelagert aus `../SKILL.md` (Abschnitt 8). Gilt in jeder Lern-Session.
`${CLAUDE_PLUGIN_ROOT}` = Plugin-Ordner, also der Ordner ueber `skills/`, aus dem diese Datei
gelesen wurde (in dieser Datei setzt Claude Code den Pfad nicht selbst ein).

```
# Lerner-State: <thema>

Lern-Anker / Deliverable: <konkretes Zielobjekt> -- <Ziel-Artefakt in 1 Zeile>
Aktives Projekt: <name> | <name> (Pfad offen) | keines ...   (Werte: projektpfad.md)
Projektordner: <Pfad zur Ablage des Projekts, falls es einen gibt>

| Konzept | Stand | Zuletzt | Gelernt in | Notiz |
|---|---|---|---|---|
| <konzept> | neu / wackelig / sitzt / Uebung | YYYY-MM-DD | <projekt> / Uebung / schon gekonnt / -- | <1 Zeile> |

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
Gefuehl. Kalibrierungs-Notizen in die Notiz-Spalte.

**Projekt und Bau-Stand** (`projektpfad.md`): Die Zeile "Aktives Projekt:" nennt das eine
aktive Projekt des Themas; ihre Werte und was sie ausloesen, stehen dort in der Tabelle. Die
Bausteine und ihr Bau-Stand stehen in `projekte/<name>/projekt.md`, nicht hier; den Bau-Stand
setzt der Weise direkt, mit genau den Werten der Tabelle dort. "Gelernt in" nennt das Projekt,
in dem das Konzept zuerst durch Stufe 5 lief (oder "Uebung", "schon gekonnt"); gesetzt wird es in
Stufe 5 (einmalig auch beim Umstellen eines aelteren Themas, `projektpfad.md`) und danach nicht
mehr geaendert. Laeuft ein schon gelerntes Konzept in einem spaeteren Projekt nur ueber die
Anwendung, wird allein "Zuletzt" fortgeschrieben.

**Themen ohne die Zeile "Aktives Projekt:"** (aus der Zeit vor dem Projektpfad) haben hier einen
Abschnitt `## Deliverable-Spur` (`| # | Baustein | Aus Konzept | Status |`, Status offen / im Bau /
fertig / Uebung / entfaellt <Datum>, das sind die Board-Marker `[ ]` / `[~]` / `[x]` /
`-- Uebung --`) und keine Spalte "Gelernt in". Solange das Thema keinen Projektpfad hat, pflegt
der Weise den Bau-Stand dort weiter. Bekommt es einen (`projektpfad.md`, "Ja"), kommt die Spalte
dazu, und der Bau-Stand steht ab dann nur noch in `projekt.md`; die alte Tabelle bleibt als
Stand von damals stehen.

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
