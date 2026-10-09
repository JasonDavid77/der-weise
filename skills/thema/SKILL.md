---
name: thema
description: >
  Legt ein neues Lernthema an oder aktualisiert ein bestehendes: Werkraum aus
  der Vorlage, Lernziel zuerst (Working Backwards), Recherche erst besprechen
  (Prompts fuer das Recherche-Werkzeug der Person oder eigene Websuche),
  sources, Synthese-Pflicht, Fragen-Stack, Speicher-Ingest (nur mit Python),
  Abfrage-Karten, ANLAGE-BERICHT als Pflicht-Abschluss. Unterricht und Pruefung
  uebernimmt der Skill lernen. Nutze diesen Skill, wenn die Person sagt:
  "neues Lernthema", "Neues Lernthema: X", "ich will X lernen", "Thema lernen",
  "Einarbeitung starten", "Thema aktualisieren", "new learning topic",
  "I want to learn X", oder wenn ein bestehendes Thema im Werkraum
  weiterbearbeitet oder aktualisiert wird.
argument-hint: "[thema]"
---

# Thema -- Lernthema anlegen + Kreislauf fahren

Vor dem ersten Datenzugriff `${CLAUDE_PLUGIN_ROOT}/references/daten.md` lesen.

Alle Schritte sind Pflicht. Anrede aus dem Profil (Feld `anrede`), Ton wie in
`${CLAUDE_PLUGIN_ROOT}/skills/lernen/persona.md`.

**Wo was liegt:** Werkraum = Pfad im Feld `werkraum` von
`<WEISE_HOME>\config.json` (ein Ordner je Thema, dazu `_themen.md` und
`werkzeug-register.md`). Fehlt `config.json`: `<WEISE_HOME>\themen`
(Datenregeln 1 und 4). Vorlage fuer neue Themen: `${CLAUDE_SKILL_DIR}/template`.
Ordner im Thema: `auftraege/` und `eingang/` (alte Namen: Datenregel 7).

**Betriebsart pruefen, nie annehmen** (Datenregel 5, wie im Skill `lernen`):
Existiert `<WEISE_HOME>\venv\Scripts\python.exe`, laeuft alles **VOLL** mit
Speicher und den Befehlen unten. Sonst **OHNE PYTHON**: Das Wissen liegt nur als
Dateien im Werkraum, jeder Speicher-Schritt entfaellt, Abfrage-Karten stehen in
`recall-cards.md` (Faecher-Regel,
`${CLAUDE_PLUGIN_ROOT}/skills/lernen/references/karten.md`). Befehle (nur VOLL,
PowerShell):

```
$py = "<WEISE_HOME>\venv\Scripts\python.exe"; $s = "<WEISE_HOME>\scripts"
& $py "$s\learn-store.py" --thema <name> [--register]    # in den Speicher legen
& $py "$s\learn-recall.py" --thema <name> --add "<frage>" # Abfrage-Karte anlegen
```

Gerade doppelte Anfuehrungszeichen gehoeren nie in den Text eines Arguments
(PowerShell zerteilt ihn sonst); fuer woertliche Oberflaechentexte „…“ nutzen.

**Session-Fahrplan zuerst (IMMER):** Jede thema-Session (A, B oder E) beginnt
mit einem kleinen Kasten, der zeigt, was jetzt passiert und wo der Input der
Person gebraucht wird -- erst dann geht es los. Vorlage (echt befuellen):

```
THEMA: <thema> -- <Anlage | Arbeits-Session | Update>
+---------------------------------------------------+
| 1 <schritt>                       (ICH)           |
| 2 <schritt>                       (SIE: <input>)  |
| 3 ...                                             |
| Ende: Speicher -> ANLAGE-BERICHT                  |
+---------------------------------------------------+
```

## A. Neues Thema anlegen (nur mit Bestaetigung der Person)

1. **Name klaeren:** kebab-case, Englisch (Ausnahme: Eigennamen). Vorschlagen,
   die Person bestaetigt. Vorher kurz pruefen, ob ein installiertes Wissenspaket
   zum Thema passt: `${CLAUDE_PLUGIN_ROOT}/skills/paket/SKILL.md` als Datei lesen,
   Abschnitt 1, Schritte 2 bis 5. Passt eines: `/weise:paket` anbieten, der Stoff
   liegt dort schon vor (Datenregel 11). Nichts gefunden: still weiter.
2. **Lernziel zuerst (Working Backwards):** "Was wollen Sie KOENNEN, wenn das
   Thema gefestigt ist?" -- 1-3 Punkte von der Person. Dabei auch fragen: "Gibt es
   einen konkreten Fall / ein Projekt dafuer?" -> Anker vor-erfassen:
   `learner-state.md` aus der Vorlage fuellen (Zeilen "Lern-Anker" und
   "Projektordner"). Das Projekt muss dafuer NICHT fertig durchdacht sein: Der
   Weise zieht Lernpfad und Deliverable-Spur nach, wenn es waechst
   (Projekt-Nachzug). Ohne bestaetigtes Lernziel wird NICHT angelegt.
2b. **Praxis-Modus abfragen:** "Geht es um ein Werkzeug, das Sie bedienen lernen
   wollen -- soll der Weise je Konzept einen kleinen Fall, Uebungsdokumente und
   einen Klickweg zum Mitmachen bauen?" Antwort als Kopfzeile
   `Praxis-Modus | an` bzw. `aus` ins `_index.md`. Im Zweifel **aus**.
   Bei jedem **Werkzeug-Thema** (egal ob Praxis-Modus an oder aus) gehoert die
   Bedienkarte `ui-observed.md` (aus der Vorlage) von Anfang an dazu: Dort haelt
   der Weise fest, wie die Oberflaeche in dieser Umgebung wirklich aussieht.
3. **Struktur:** `${CLAUDE_SKILL_DIR}/template` nach `<werkraum>/<thema>/`
   kopieren, Platzhalter fuellen (_index.md: Thema, Lernziel, Datum, Status
   [SAMMELN]). `ui-observed.md` nur bei reinen Wissensthemen (kein bedienbares
   Werkzeug) weglassen. `recall-cards.md` nur im Betrieb OHNE PYTHON behalten
   (VOLL legt `learn-recall.py` die `recall-cards.json` an).
3b. **Ausloeser-Quellen zuerst:** "Was hat das Thema angestossen -- ein Artikel,
   ein Gespraech, ein Dokument?" Die Ausloeser-Quellen der Person einsammeln, als
   Text nach `sources/` kuratieren + Doc-Index-Zeile. Initial-Sweep (A.5) und
   Quellen-Scan (A.6) laufen danach durch diese Quellen informiert.
4. **Registrieren:** Zeile in `<werkraum>/_themen.md`.
5. **Initial-Sweep: erst den Bedarf besprechen, dann Recherche (Standard).**
   Wie recherchiert wird, sagt das Profil-Feld `recherche`: `werkzeug` = Prompts
   fuer das Recherche-Werkzeug der Person, `websuche` = der Weise sucht selbst.
   Fehlt das Feld: einmal fragen und in `<WEISE_HOME>\config.json` speichern
   (zusammenfuehrend: lesen, nur dieses Feld setzen, Rest erhalten).
   (1) Erst lesen: die Ausloeser-Quellen aus A.3b und die Unterlagen zum
   Anker-Projekt, vollstaendig. Liegt etwas noch bei der Person, wartet dieser
   Schritt.
   (2) Mit der Person sprechen: Was braucht das Projekt, was ist schon bekannt,
   wo sind die Luecken? Ein Gespraech, kein fertiger Prompt.
   (3) Daraus eine **Themenliste**: je Thema ein Satz, was wir wissen muessen und
   wofuer (welches Lernziel, welcher Baustein). Die Person gibt sie frei, streicht
   oder ergaenzt.
   (4) Erst nach der Freigabe, je Thema: bei `werkzeug` ein eigener, kurzer
   Prompt als nummerierte Datei `auftraege/R<n>-YYYY-MM-DD-<kurz>.md`, mit
   Zeile in der Uebersicht `auftraege/readme.md`; uebergeben wird der Ordner mit
   kurzer Anleitung, der Prompt steht NICHT noch einmal im Gespraech. Alles
   dazu in `${CLAUDE_SKILL_DIR}/references/recherche.md`. Bei `websuche` eine eigene Suche.
   Alternative: ohne Sweep starten. Bei `werkzeug` eine eigene Websuche nur, wenn
   die Person es fuer dieses Thema ausdruecklich sagt. Ergebnisse landen als
   datierte Textdateien in `sources/`.
6. **Quellen-Scan (Pflicht -- Werkzeuge WIRKLICH aufrufen, nicht aus dem Kopf):**
   - verbundene MCP-Server und Werkzeuge dieser Sitzung auflisten
   - vorhandene Konnektor- oder Register-Suche aufrufen -- Ergebnis notieren, auch
     wenn leer
   - Fach-Datenbanken und offizielle Dokumentationen: bei `werkzeug` als
     Suchhinweis in die Prompts aus A.5 (eigene Websuche nur auf Ansage der
     Person), bei `websuche` in die eigene Suche aus A.5
   Jeder Eintrag traegt **wie gefunden** (Werkzeugliste / Suche / Recherche /
   Erinnerung -- "aus Erinnerung" ausdruecklich so markieren). Treffer UND
   Fehlanzeige (mit Methode + Datum) ins `werkzeug-register.md` MIT Routing-Spalten
   (Art, Zugriff gespeichert/live, Vertrauen) UND in die Verknuepfungen-Zeile der
   Themen-`_index.md`. Routing-Regel: Volatiles (Rechtsprechung, Preise, laufende
   Aenderungen) NIE speichern, immer live abfragen.
   **Verbinden gehoert dazu:** Kandidaten mit klarem Nutzen nicht nur notieren,
   sondern in einem Satz pitchen (von wem + was es bringt); die Person entscheidet.
7. **Speicher-Ingest (VOLL: Pflicht, sobald Inhalt da ist):**
   `learn-store.py --thema <name> --register`. Legt die Abschnitte EINMAL mit
   Etikett thema=<name> in den Speicher (die Themen-Sicht ist der Filter darauf)
   + legt das Register ab. Der Bericht nennt den laengsten Abschnitt und
   "abgeschnitten: 0" -- steht dort etwas anderes, STOP und melden.
   OHNE PYTHON entfaellt dieser Schritt; im Deckblatt steht bei "Letzter
   Ingest" dann das Datum, an dem zuletzt Stoff dazukam, mit dem Zusatz
   "(Datei-Betrieb)" -- der Frische-Check des Weisen rechnet mit diesem Datum.
7b. **Curriculum-Induktion (Pflicht, sobald der erste Stoff da ist; VOLL nach dem ersten Ingest):** Aus synthesis +
   sources eine `concepts.md` erzeugen (Lernpfad: Konzepte in Lernreihenfolge, je
   1 Kern-Satz + Voraussetzungen) und in questions.md einen **Pruefkatalog**
   anlegen (Frage / Erwartet / typische Irrtuemer -- mindestens fuer die
   Kern-Konzepte). Bei Werkzeug-Themen pruefen die Fragen die Mechanik des
   Werkzeugs, nicht den Fachstoff des Ankers. Abfrage-Karten anlegen (VOLL:
   `learn-recall.py --thema <name> --add "<frage>"`; OHNE PYTHON: Zeilen in
   `recall-cards.md`, Fach 1, faellig morgen). Der Lernpfad ist ein Start,
   kein Vertrag: Der Weise erweitert ihn, wenn das Projekt waechst.
7c. **Konsistenz-End-Check (Pflicht):** Bevor der Bericht rausgeht, Zahlen und
   Status im `_index.md` und in `_themen.md` GEGEN die Dateien pruefen:
   Konzept-Zahl = Zeilen in concepts.md; Quellen-Zahl = Dateien in sources/
   (ohne `readme.md`; ein Wissenspaket unter `sources/paket/` zaehlt als eine Quelle);
   Status stimmt ueberall ueberein.
8. **ANLAGE-BERICHT (Pflicht-Abschluss, Format s. Abschnitt D)** -- belegt auch den
   Quellen-Scan: ueber welche Werkzeuge, Treffer/Fehlanzeige.

## B. Themen-Session (bestehendes Thema weiterbearbeiten)

1. `_index.md` + `questions.md` + `synthesis.md` lesen (vollstaendig).
2. **Recall zuerst:** 2-3 faellige Karten bzw. Recall-Kandidaten abfragen, BEVOR
   neuer Stoff kommt -- vorher pruefen, ob sie noch zum Stand passen. Jede
   gestellte Karte in der Kartendatei des Themas fortschreiben
   (`${CLAUDE_PLUGIN_ROOT}/skills/lernen/references/karten.md`). (Volle
   Lern-Sessions fuehrt der Weise.)
3. **Eingang:** `eingang/` (alte Namen: Datenregel 7) pruefen. Ergebnisse von
   Recherche-Auftraegen laufen nach `${CLAUDE_SKILL_DIR}/references/recherche.md`,
   Abschnitt 3 (zuordnen, ablegen, sofort in die Synthese, Uebersicht
   fortschreiben). Alles andere -> kuratieren nach
   `sources/` (sauber benannt, datiert) -> Zeile im Doc-Index der `_index.md`.
   PDFs, Word-Dateien und Mitschnitte VOR dem Ingest in .md/.txt ueberfuehren --
   learn-store.py nimmt nur .md/.txt und warnt laut bei uebersprungenen Dateien.
   Hat der Eingang Update-Charakter -> Teil E fahren.
4. **Synthese-Pflicht:** Neues Material in `synthesis.md` einarbeiten (eigene
   Worte, Quellen-Verweise). Eine Session ohne Synthese-Update ist keine
   Lern-Session.
5. **Ingest-Pflicht:** Hat sich `synthesis.md` oder `sources/` geaendert -> VOLL:
   `learn-store.py --thema <name>` (neue Register-Zeile -> zusaetzlich
   `--register`). In beiden Betriebsarten danach "Letzter Ingest" im Deckblatt
   auf heute setzen (OHNE PYTHON mit "(Datei-Betrieb)").
6. **Fragen-Stack pflegen:** Neues -> Offen; Beantwortetes -> Haken + Verweis;
   Gefestigtes -> Recall-Kandidaten bzw. Karte.
7. Status im `_index.md` und in `_themen.md` aktuell halten.
8. Bericht (Abschnitt D) ausgeben, wenn neuer Stoff dazukam.

## C. Festigen (ab Status [FESTIGEN])

1. Gefestigtes ist durch den laufenden Ingest bereits im Speicher -- kein
   separater Weg.
2. Recall-Kandidaten und Karten ergaenzen; Pruef-Sessions ueber den Weisen.
3. **Ziel-Check** gegen das Lernziel in `_index.md`: erreicht -> [GEFESTIGT],
   Luecken -> als offene Fragen zurueck in den Stack.

## D. ANLAGE-BERICHT (Pflicht-Format)

Nach Anlage (A) und nach jeder Session mit neuem Stoff (B) ausgeben -- VOLL die
Zahlen aus dem SPEICHER-BERICHT von learn-store.py uebernehmen, OHNE PYTHON bei
2. und 3. "entfaellt (Datei-Betrieb)":

```
ANLAGE-BERICHT <thema> -- YYYY-MM-DD
1. Werkraum:    <werkraum>/<thema>/ -- N Dateien (was neu ist)
2. Speicher:    thema=<name> -- N Abschnitte (ersetzt), laengster <t> Token, abgeschnitten 0
3. Gesamt:      Sammlung "wissen" -- M Abschnitte
4. Verknuepft:  <je Werkzeug EIN Satz: von wem + was es dem Thema bringt;
                Status verbunden/Kandidat; Register gespeichert: ja/nein>
5. Lernziel:    <1 Zeile> | Status: [TAG]
6. Naechster Schritt: <1 Zeile>
```

## E. Update-Session (volatile Themen aktuell halten)

Trigger: Frische-Pitch des Weisen mit GO der Person -- oder die Person direkt
("Update <thema>", "Thema aktualisieren").

1. **Recherche:** wie A.5 -- Bedarf besprechen, Themenliste von der Person
   freigeben lassen, dann je Thema: bei `werkzeug` ein nummerierter Auftrag nach
   `auftraege/` (eigene Websuche nur auf ausdrueckliche Ansage der Person),
   Ergebnis -> `eingang/`; bei `websuche` eine eigene Suche. Auftrag,
   Uebergabe und Ruecklauf nach `${CLAUDE_SKILL_DIR}/references/recherche.md`;
   die Quelle liegt danach datiert in `sources/`, mit Doc-Index-Zeile.
2. **Delta-Diff:** Neues gegen `synthesis.md` halten; jede Aussage klassifizieren:
   bestaetigt / ergaenzt / UEBERHOLT.
3. **Deltas sichern:** je ueberholter Aussage ein Eintrag in `updates.md`
   (Alt WORTGENAU zitieren, Neu, Quelle, Datum, Delta-Recall-Checkbox offen).
   Betroffene Abfrage-Karten anpassen, bevor sie wieder gestellt werden.
4. **Synthese umschreiben:** `synthesis.md` traegt danach NUR den Ist-Stand.
5. **Quellen-Hygiene als EIN Sammel-Vorschlag an die Person:** (a) ganz ueberholte
   Quellen -> nach `sources/_archive/` verschieben (wird nicht gespeichert);
   (b) teil-ueberholte redigieren: Passage durch `[ueberholt YYYY-MM-DD ->
   updates.md]` ersetzen. Faustregel: mehr als ein Drittel ueberholt oder
   Kernthese gekippt -> ganz archivieren. EIN GO der Person, dann ausfuehren.
   Ausnahme `sources/paket/` (Datenregel 11): dort nichts archivieren oder
   redigieren; Ueberholtes steht nur in `updates.md`, das naechste Paket bringt
   den neuen Stand.
6. **Neu speichern** (A.7, nur VOLL) raeumt veraltete Abschnitte automatisch ab; "Letzter
   Ingest" im Deckblatt in beiden Betriebsarten auf heute setzen. **UPDATE-BERICHT** = ANLAGE-BERICHT + 1
   Zeile: "N Aussagen ueberholt -> updates.md | M Quellen archiviert/redigiert".
   Kam der Trigger vom Weisen -> zurueck zur Lern-Session.

## Regeln

- Nie freihaendig anlegen -- immer Vorlage + Bestaetigung der Person.
- **Keine vertraulichen Inhalte in Werkraum oder Speicher** (Datenregel 10).
  Hierher gehoeren Lernmaterial, Anleitungen, eigene Notizen und erfundene
  Uebungsfaelle. Vertrauliche Akten, Mandats- oder Kundendaten bleiben in ihren
  eigenen Systemen; hier steht hoechstens ein Verweis. Im Zweifel fragen, bevor
  etwas nach `sources/` kommt.
- **4-Ziele-Gesetz (VOLL):** Neues Wissen geht IMMER in Werkraum + Themen-Sicht +
  Gesamtbestand + Werkzeug-Register. Themen-Sicht und Gesamtbestand sind EIN
  Schreibvorgang (Sammlung "wissen", Etikett thema=<name>). OHNE PYTHON: Werkraum
  + Werkzeug-Register.
- **Umstieg auf VOLL:** Kommt Python dazu (Einrichtung mit `/weise:einrichten`),
  jedes Thema einmal mit `learn-store.py --thema <name>` speichern. Karten aus
  `recall-cards.md` bleiben die Kartendatei des Themas, auch in VOLL
  (`${CLAUDE_PLUGIN_ROOT}/skills/lernen/references/karten.md`), es geht also
  keine verloren; ihre Uebernahme in die FSRS-Karten ist ein eigener Schritt
  (per /weise:vorschlag melden).
- **Aktualitaets-Gesetz:** Gespeicherte Dateien tragen NUR den aktuellen Stand --
  Deltas -> updates.md, ganz Ueberholtes -> sources/_archive/ (beides nicht
  gespeichert); Archiv-Moves nur per GO in einer Update-Session (Teil E).
- Boxen-Richtung ist fix: `auftraege/` = der Weise -> die Person, `eingang/` =
  die Person -> der Weise (alte Namen: Datenregel 7).
- Themen nie loeschen: [RUHT] setzen.
- Unterricht und Wissens-Pruefung macht der Weise (Skill `lernen`), nicht dieser
  Skill. Das laufende Thema darf der Weise im Projekt-Nachzug erweitern; neue
  Themen legt nur dieser Skill an.
