# Projektpfad: die Karte bleibt ganz, gelernt wird, was das Projekt braucht

Ausgelagert aus `../SKILL.md` (Abschnitt 2, "Projektpfad"). Lesen in der Vorbereitung jeder
Lern-Session; der Skill `thema` liest diese Datei fuer den ersten Projektpfad (A.7b).
`${CLAUDE_PLUGIN_ROOT}` = Plugin-Ordner, also der Ordner ueber `skills/`.

## Grundsatz

`concepts.md` ist die **Karte** des ganzen Themas, kein Pflichtweg. Ein **Projekt** ist das
Zielobjekt, an dem gelernt und gebaut wird (bisher "Anker"). Der **Projektpfad** sind die Konzepte
der Karte, die dieses Projekt braucht, in Bau-Reihenfolge. Alle uebrigen Konzepte sind **frei**:
Sie kommen nicht von selbst dran, nur auf Wunsch der Person, dann als Uebung mit Ansage
(SKILL.md Abschnitt 5). Ein Thema kann nacheinander mehrere Projekte tragen; hoechstens eines ist
aktiv.

**Lesart fuer den ganzen Skill:** Hat das Thema ein aktives Projekt, meint "Lernpfad" und
"naechstes offenes Konzept" den Projektpfad, "Deliverable-Spur" die Tabelle Projektpfad in der
`projekt.md` des aktiven Projekts, "Anker" das aktive Projekt und "Kern-Konzepte" die Konzepte auf
dem Pfad.

## Wo was steht (je Angabe genau EIN Ort)

| Angabe | Ort |
|---|---|
| Karte (alle Konzepte) | `concepts.md` |
| Lernstand je Konzept (neu / wackelig / sitzt / Uebung), "Gelernt in" | `learner-state.md`; "sitzt" ergibt sich nur aus den Karten (`karten.md`) |
| Aktives Projekt | `learner-state.md`, Zeile "Aktives Projekt:" (Werte unten); die Zeile "Lern-Anker / Deliverable:" nennt dasselbe Projekt |
| Bau-Stand je Baustein, Projektstatus, Ablage | `projekte/<name>/projekt.md` |

Der Bau-Stand sagt nichts ueber den Lernstand: Ein Baustein kann fertig sein, waehrend das Konzept
"wackelig" ist (etwa nach dem Tempo-Modus).

**Zeile "Aktives Projekt:" in `learner-state.md`** (bestimmt, was die Vorbereitung tut):

| Wert | Bedeutung | Was die Session tut |
|---|---|---|
| `<name>` | Pfad bestaetigt, `projekt.md` liegt vor | Board mit Projektpfad, Konzept-Takt entlang des Pfads. Steht das Projekt schon auf "fertig": Board, Recall, dann die Frage vom Projektende |
| `<name> (Pfad offen)` | Projekt genannt, Pfad noch nicht bestaetigt | PLAN still vorbereiten; REVIEW ist das Erste nach dem Sessionkopf; nach dem Ja Board und Recall wie sonst |
| `keines (zuletzt <name>, weiterlernen)` | Projekt fertig, die Person lernt frei weiter | Board ohne Projektpfad (ZIEL = Lernziel, rechts `-- Uebung --`), Recall, dann waehlt die Person aus der Karte (Uebung mit Ansage); der Weise schlaegt kein Konzept von sich aus vor |
| `keines (zuletzt <name>, Schluss)` | Projekt fertig, keine neuen Konzepte | Board ohne Projektpfad, faellige Karten, kein neues Konzept; einmal der Ziel-Check gegen das Lernziel (Skill `thema` Teil C), Ergebnis ins Session-Log |
| `keines` | Thema ohne Projekt ("kein Anker") | Karte der Reihe nach, jede Praxis als Uebung, Board ohne Projektpfad |
| Zeile fehlt | Thema aus der Zeit vor dem Projektpfad | alter Ablauf; einmaliger Vorschlag, siehe unten |

Die Zeile "Projektpfad: nein (YYYY-MM-DD)" oder "Projektpfad: vorgeschlagen (YYYY-MM-DD)" heisst:
kein Projektpfad, und der Weise schlaegt von sich aus keinen mehr vor. Die Zeile steht unter
"Projektordner:". Die Person kann jederzeit "Projektpfad anlegen" sagen (dann laeuft der Ja-Zweig
unten) oder "Neues Projekt zu <thema>".

## `projekte/<name>/projekt.md`

`<name>`: kebab-case, zwei bis vier Woerter; der Weise schlaegt ihn vor (nach der Frage zu
Vertraulichem, s.u.), die Person bestaetigt ihn mit dem Pfad. Gibt es den Ordner schon, `-2`
anhaengen.

```
# Projekt: <name>

Deliverable: <Ziel-Artefakt in einer Zeile>
Ablage: <Pfad des Projekts bei der Person | dieser Ordner | bei der Person, ohne Pfad>
Status: laeuft | fertig YYYY-MM-DD | ruht YYYY-MM-DD
Gestartet: YYYY-MM-DD

## Projektpfad
| Nr | Konzept | Baustein | Bau-Stand |
|---|---|---|---|
| 1 | K2 <konzept> | <Baustein> | offen / im Bau / fertig / schon gekonnt / entfaellt YYYY-MM-DD |

## Log
- YYYY-MM-DD: Projektpfad bestaetigt (<n> Konzepte, <k> frei).
```

**Bau-Stand:** "im Bau", sobald der Takt des Konzepts beginnt; "fertig", wenn die Person den
Baustein in Stufe 5 gebaut hat und das Ergebnis in der Ablage liegt (bei "dieser Ordner": als Datei
in `projekte/<name>/`). In die Tabelle kommen nur diese Werte; der Lernstand steht nie hier.
`projekte/` wird nicht gespeichert und nicht durchsucht. Uebungsdokumente gehoeren weiter nach
`uebungen/<konzept>/`, ein Ordner je Thema, unabhaengig vom Projekt.

**Vertrauliches (Datenregel 10):** Als Erstes, noch bevor Name und Pfad gezeigt werden, einmal
fragen, ob das Projekt ein echter Fall mit vertraulichen Inhalten ist (hat der Skill `thema` das
schon geklaert, nicht noch einmal). Wenn ja, gilt fuer den ganzen Werkraum:
- Projektname, Deliverable-Zeile, die Zeile "Lern-Anker", die Spalte "Anker (Projekt)" in
  `_themen.md` und die Namen der Bausteine sind neutral: kein Mandant, kein Kunde, keine Person,
  kein Aktenzeichen, keine Einzelheit des Falls.
- Die Ablage ist der eigene Ort der Person; `projekt.md` nennt nur den Pfad. Gibt es keinen eigenen
  Ort, steht "bei der Person, ohne Pfad", und im Werkraum entsteht aus dem Bau keine Datei.
- Antworten der Person zum Fall (SKILL.md Abschnitt 6) bleiben im Gespraech oder am Ort der
  Person; nach `questions.md` kommt nur die neutrale Frage mit "beantwortet YYYY-MM-DD".

## Der Zyklus je Projekt

1. **PLAN.** Aus Lernziel und Deliverable die Konzepte der Karte markieren, die das Projekt
   braucht, in Bau-Reihenfolge; Voraussetzungen ("Braucht") kommen mit auf den Pfad. Je Konzept
   ein Baustein.
2. **REVIEW.** Den Pfad zeigen (Projektname, je Konzept der Baustein), daneben die Zahl der freien
   Konzepte, und fragen: "Fehlt etwas, kann etwas weg?" Ohne Bestaetigung kein Start. Erst nach
   dem Ja `projekt.md` schreiben, in `learner-state.md` die Zeile "Aktives Projekt: <name>" setzen
   (ohne Zusatz), fehlt im Doc-Index der `_index.md` die Zeile `projekte/`, sie ergaenzen, und das
   Board in der Form mit Projekt zeigen.
   Will die Person keinen Ausschnitt, sondern alles der Reihe nach: Dann enthaelt der Pfad alle
   Konzepte der Karte (Log: "Pfad = ganze Karte, Wunsch der Person"); sonst alles wie oben. Kommt
   keine Antwort oder will die Person sofort bauen (Tempo-Modus): Die Frage bleibt die eine Frage
   vor dem ersten Bauschritt; ohne Antwort endet die Session ohne neuen Stoff.
3. **OPTIMIEREN.** Vermutet die Person oder der Weise, dass ein Pfad-Konzept schon gekonnt ist:
   EINE kurze Pruef-Frage. Sitzt die Antwort: Bau-Stand "schon gekonnt", Lernstand "wackelig",
   "Gelernt in" = "schon gekonnt". Hat das Konzept keine Karte, eine anlegen; eine vorhandene
   bleibt, wie sie ist. "sitzt" entsteht nie aus einer einzelnen Antwort. Doppeltes faellt aus dem
   Pfad. Kommt das Konzept auf dem Pfad an die Reihe, entfallen die Stufen 1 bis 3: ein Satz Kern
   mit Herkunfts-Zeile, dann die Anwendung (Stufe 4 und 5). Das ist die einzige Ausnahme von
   "Erklaeren startet bei Null"; stockt die Person in der Anwendung, zurueck zu Stufe 1.
4. **AUSFUEHREN.** Der Konzept-Takt laeuft nur entlang des Pfads, je Konzept ein Baustein.
   Freie Konzepte werden nicht angeboten. Ist der letzte Baustein fertig (oder entfallen): Status
   "fertig YYYY-MM-DD", dann der Zweitfall nach "Far-Transfer" und die Frage: "Weiterlernen (freie
   Konzepte als Uebung), ein neues Projekt, oder hier aufhoeren?"
   - **Weiterlernen:** "Aktives Projekt: keines (zuletzt <name>, weiterlernen)". Die Person waehlt
     aus der Karte, jedes Konzept laeuft als Uebung mit Ansage.
   - **Neues Projekt:** siehe unten.
   - **Aufhoeren:** "Aktives Projekt: keines (zuletzt <name>, Schluss)". Keine neuen Konzepte; die
     faelligen Karten kommen weiter, und der Ziel-Check gegen das Lernziel laeuft nach Skill
     `thema` Teil C.
   Bleibt die Frage ohne Antwort, steht weiter "Aktives Projekt: <name>" bei Status "fertig"; die
   naechste Session stellt nach dem Recall zuerst diese Frage.

## Der Pfad aendert sich

Projekt-Nachzug (SKILL.md Abschnitt 4): Ein neues Konzept kommt auf die Karte UND als Zeile auf den
Pfad. Ein freies Konzept, das das Projekt jetzt doch braucht (auch: im Tempo-Modus beruehrt), kommt
als Zeile auf den Pfad. Ein Konzept, das das Projekt nicht mehr braucht: Bau-Stand "entfaellt
YYYY-MM-DD", es ist wieder frei. Jede Aenderung als Zeile ins Log der `projekt.md`.

## Erster Pfad, neues Projekt, Themen aus der Zeit davor

- **Erster Pfad:** Der Skill `thema` schlaegt ihn nach der Karte vor (PLAN und REVIEW). Steht in
  `learner-state.md` noch "(Pfad offen)", holt der Weise das zu Beginn der Lern-Session nach.
- **Neues Projekt zum Thema** ("Neues Projekt zu <thema>: <was>", oder die Person nennt am
  Projektende ein neues). Gibt es das Thema nicht: an den Skill `thema` verweisen. Sonst, nach dem
  Recall und vor dem Board: PLAN und REVIEW auf derselben Karte. Konzepte mit Lernstand ungleich
  "neu" stehen normal im neuen Pfad; im REVIEW und im Board zeigt der Weise sie als "gelernt in
  <projekt>, <stand>" (aus `learner-state.md`), und sie laufen nur ueber die Anwendung (ein Satz
  Kern, der einen notierten Irrtum aufgreift, dann Stufe 4 und 5; stockt die Person, zurueck zu
  Stufe 1). Lernstand und "Gelernt in" bleiben dabei, wie sie sind; nur "Zuletzt" wird
  fortgeschrieben. Erst nach dem Ja:
  das bisherige Projekt bekommt Status "fertig" (alle Bausteine fertig oder entfallen) oder sonst
  "ruht"; die neue `projekt.md` entsteht; in `learner-state.md` werden "Lern-Anker / Deliverable:",
  "Aktives Projekt:" und "Projektordner:" auf das neue Projekt gesetzt, in `_themen.md` die Spalte
  "Anker (Projekt)"; eine Log-Zeile in `_index.md`. Ohne Ja bleibt alles beim bisherigen Projekt.
  Hat das Thema noch gar keinen Projektpfad (Zeile fehlt oder "keines"), laeuft stattdessen der
  Ja-Zweig unten, bei "keines" ohne alte Spur.
- **Themen aus der Zeit vor dem Projektpfad** (`learner-state.md` nennt einen Lern-Anker, hat
  aber weder die Zeile "Aktives Projekt:" noch eine Zeile "Projektpfad:"): Die Session laeuft wie
  bisher (Board ohne Projektpfad, Deliverable-Spur in `learner-state.md`). Einmal, NACH dem Board,
  in einem Satz und nie im Tempo-Modus vorschlagen: "Ich kann daraus den Projektpfad fuer <Anker>
  machen: Sie sehen dann nur noch, was das Projekt braucht. Soll ich?" Gleich danach
  "Projektpfad: vorgeschlagen (YYYY-MM-DD)" eintragen. Die Session laeuft so oder so weiter.
  - **Ja:** fertige und laufende Bausteine der alten Spur uebernehmen; fuer die offenen PLAN und
    REVIEW (die alte Spur fuehrte jedes Konzept, sie ist kein Pfad). Der Bau-Stand der
    uebernommenen Bausteine bleibt, wie er war; "Ablage" = die bisherige Zeile "Projektordner:",
    sonst "dieser Ordner"; "Gestartet" = heute. Nach dem Ja wie im REVIEW oben; dazu in
    `learner-state.md`: die Zeile "Projektpfad: vorgeschlagen" entfernen, die Spalte "Gelernt in"
    ergaenzen (einmalig der Projektname bei allen Konzepten mit Lernstand ungleich "neu"), und
    unter der Ueberschrift "## Deliverable-Spur" nach einer Leerzeile der Satz "Stand YYYY-MM-DD,
    wird nicht mehr gepflegt: weiter in projekte/<name>/projekt.md", danach wieder eine Leerzeile.
    In `_themen.md` die Spalte "Anker (Projekt)" auf den Projektnamen setzen. Die alte Tabelle,
    Lernstand und Karten bleiben unveraendert. Ab jetzt gilt das Thema als Thema mit Projektpfad.
  - **Nein:** "Projektpfad: nein (YYYY-MM-DD)" statt "vorgeschlagen"; alter Ablauf, altes Board.
  Themen ohne Anker bekommen keinen Vorschlag.

## Karten

Eine Karte wird nur gestellt, wenn ihr Konzept gelehrt ist: Karten zu Konzepten mit Lernstand
"neu" ruhen (Stand-Pruefung 1c), egal ob auf dem Pfad oder frei. Hat ein Konzept nach Stufe 5 noch
keine Karte, legt der Weise eine an (Frage aus dem Pruefkatalog in `questions.md` oder eine eigene
zur Mechanik; Fach 1, faellig morgen, bzw. `learn-recall.py --add`). So kann jedes gelehrte Konzept
"sitzen".

## Die Karte auf Zuruf

Sagt die Person "Karte" (oder "ganze Karte", "show the map"): alle Konzepte aus `concepts.md` in
einer Tabelle, je Zeile Lernstand, "Gelernt in" und ob das Konzept auf dem aktuellen Pfad steht
oder frei ist. Danach zurueck in die Session.
