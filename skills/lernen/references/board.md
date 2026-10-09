# ROADMAP-BOARD (Muster)

Ausgelagert aus `../SKILL.md` (Stufe 0). Das Board kommt am Sessionstart, nach jeder abgeschlossenen
Etappe (= ein Konzept ist durch Stufe 5) und sobald ein Projektpfad bestaetigt ist, echt befuellt
aus den faelligen Karten, `concepts.md`, `learner-state.md` und der `projekt.md` des aktiven
Projekts. **Die WISSEN-Zeile ist PFLICHT**: Betriebsart und Modus sind nie Interpretationssache.
`<n> Dateien` (OHNE PYTHON) = `synthesis.md` plus die Dateien in `sources/` ohne `readme.md` und
ohne `_archive`.

## Mit aktivem Projekt (Standard)

```
+----------------------------------------------------------------------+
| WISSEN: thema=<name>, <VOLL (<n> Abschnitte) | OHNE PYTHON (<n> Dateien)> |
|         Modus: <NORMAL|TEMPO>                                        |
| PROJEKT: <projekt>  --  ZIEL: <Deliverable in 1 Zeile>               |
|          Karte gesamt: <m>/<n> sitzen                                |
+----------------------------------------------------------------------+
| PROJEKTPFAD (<p>)                 | BAUSTEINE                        |
| [x] K2 <konzept>      sitzt       | [x] <Baustein 1>                 |
| [~] K5 <konzept>  <==  laeuft     | [~] <Baustein 2>                 |
| [ ] K7 <konzept>      offen       | [ ] <Baustein 3>                 |
| [ ] K9 <konzept>  NEU 2026-..     | [ ] <neuer Baustein>             |
+----------------------------------------------------------------------+
| STAND: Pfad <a>/<p> gelernt | Bausteine <x>/<p> | Geparkt: <g>       |
|        zuletzt: <K> | naechstes: <K>                                 |
| Frei (nicht im Projekt): <k> Konzepte  (zeigen mit "Karte")          |
| NEU IM PFAD: <K9 name, kam mit <Anlass>>  (nur wenn es das gibt)     |
+----------------------------------------------------------------------+
```

Die freien Konzepte stehen nur als Zahl im Board. "Pfad <a>/<p> gelernt" zaehlt die Pfad-Konzepte
mit Lernstand ungleich "neu". Im zweiten Projekt eines Themas steht bei schon Gelerntem, solange
sein Baustein nicht fertig ist, statt des Stands `gelernt in <projekt>, <stand>`: als
`[ ] K4 <konzept>  gelernt in ...`, und wenn es an der Reihe ist als `[~] K4 <konzept>  <==
gelernt in ...` (das Board darf dafuer breiter werden).

## Ohne Projektpfad

Gilt, solange `learner-state.md` kein aktives Projekt mit bestaetigtem Pfad nennt: Themen ohne
Anker, "Aktives Projekt: keines ...", Themen aus der Zeit vor dem Projektpfad (auch mit
"Projektpfad: nein" oder "vorgeschlagen").

```
+----------------------------------------------------------------------+
| WISSEN: thema=<name>, <VOLL (<n> Abschnitte) | OHNE PYTHON (<n> Dateien)> |
|         Modus: <NORMAL|TEMPO>                                        |
| TITEL:  <Thema>  --  ZIEL: <Deliverable in 1 Zeile>                  |
+----------------------------------------------------------------------+
| LERNPFAD                          | DELIVERABLE-SPUR                 |
| [x] K1 <konzept>      sitzt       | [x] <Baustein 1>                 |
| [~] K2 <konzept>  <==  laeuft     | [~] <Baustein 2>                 |
| [ ] K3 <konzept>      offen       | [ ] -- Uebung --                 |
| [ ] K9 <konzept>  NEU 2026-..     | [ ] <neuer Baustein>             |
+----------------------------------------------------------------------+
| STAND: <m>/<n> Konzepte sitzen | Deliverable <x>/<n> | Geparkt: <p>  |
|        zuletzt: <K> | naechstes: <K>                                 |
| NEU IM LERNPFAD: <K9 name, kam mit <Anlass>>  (nur wenn es das gibt) |
+----------------------------------------------------------------------+
```

## Legende (beide Formen)

Linke Spalte: `[x]` sitzt | `[~]` mit `<==` = laeuft (in der ersten Session das naechste Konzept) |
`[~]` ohne `<==` = wackelig (gelehrt, sitzt noch nicht) | `[ ]` offen | `NEU <Datum>` = per
Projekt-Nachzug aufgenommen. `<==` steht an genau EINEM Konzept: dem, das gerade laeuft, sonst
dem, das als naechstes drankommt; ist der Pfad fertig, an keinem.
Rechte Spalte: `[x]` fertig | `[~]` im Bau | `[ ]` offen | `[ ] schon gekonnt` = Baustein noch zu
bauen, Erklaerung entfaellt | `[-]` entfaellt | `-- Uebung --` = Konzept ohne Baustein (SKILL.md
Abschnitt 5).
Im almighty-Modus lautet die WISSEN-Zeile:
`WISSEN: ganzer Bestand, <VOLL (<N> Abschnitte) | OHNE PYTHON (<N> Dateien)> | Modus: ALMIGHTY`.
