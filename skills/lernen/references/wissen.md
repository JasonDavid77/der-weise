# Wissens-Disziplin -- Speicher UND Live-Werkzeuge

Ausgelagert aus `../SKILL.md` (Abschnitt 7). Gilt in jeder Lern-Session.

Zwei Schichten, nach Art des Wissens:
- **Speicher (stabil):** Konzepte/Prinzipien aus dem Speicher (Themen-Sicht bzw.
  almighty) + Werkraum-Dateien. Reproduzierbar, zitierbar -- das ist der Lernstoff.
- **Live (volatil):** Rechtsprechung, Preise, laufende Aenderungen einer
  Oberflaeche -> LIVE ueber die Werkzeuge des Modus abfragen ("Stand <Datum>").
  Ein veralteter Speicher-Stand waere hier schlechter.

**Nicht gespeicherte Dateien als DATEI lesen, nie ueber den Speicher suchen:**
`_index.md`, `concepts.md`, `questions.md`, `learner-state.md`, `updates.md`,
`ui-observed.md`, `recall-cards.md`, `paket.json`, `uebungen/`, `projekte/`. Gespeichert (VOLL, ueber
query.py erreichbar) sind nur `synthesis.md` + `sources/*.md/.txt`.

**Stichwortsuche (OHNE PYTHON)** ersetzt die Bedeutungssuche:
1. Aus der Frage 3 bis 6 Suchwoerter bilden, jedes auf Deutsch UND Englisch,
   dazu 1-2 Synonyme oder die Beschriftung aus der Oberflaeche (Quellen sind oft
   englisch: "Vorlage fuer Verhandlungen" -> auch "playbook", "negotiation").
2. NUR in `synthesis.md` und `sources/` des Themas suchen (rekursiv, .md/.txt,
   ohne `readme.md` und ohne `_archive`) -- genau das, was VOLL im Speicher hat;
   almighty: dasselbe ueber alle Themen plus `werkzeug-register.md`. Nie in
   `uebungen/` (erfundene Faelle), `projekte/` (Bau-Stand und Entwuerfe, kein Lernstoff),
   `eingang/` (Unkuratiertes; alter Name: Datenregel 7) oder
   `updates.md` (Ueberholtes). Gross-/Kleinschreibung egal; deutsche Woerter mit
   Umlaut UND in der Schreibweise ae/oe/ue/ss. Mit dem Grep-Werkzeug der Sitzung
   suchen (liest UTF-8 richtig), nicht mit Select-String in Windows PowerShell
   5.1 (liest UTF-8 ohne BOM falsch, Umlaute finden dann nichts).
3. Dateien mit den meisten verschiedenen Suchwoertern zuerst; hoechstens 5
   Stellen lesen, je etwa 20 Zeilen Umfeld.
4. Nichts gefunden: einmal erweitern (Oberbegriff, andere Schreibweise, Einzahl
   oder Mehrzahl), dann ehrlich "dazu weiss Ihr Thema noch nichts".
5. Herkunfts-Zeile: "Quellen: <datei> (Stichwortsuche)".

Der Weise ist NICHT auf den Speicher beschraenkt. VERBOTEN ist nur:
ungekennzeichnetes Allgemeinwissen als Fakt ausgeben -- Allgemeinwissen darf
Fragen formen, nie unmarkiert Fakten liefern. Liefert weder Speicher noch
Werkzeug etwas: ehrlich sagen + Luecke nach questions.md.

- **Herkunfts-Zeile pro Block (Pflicht):** Jeder Lehr-/Bau-Block endet mit
  "Quellen: <datei(en)>" ODER "Live: <Werkzeug>, Stand <Datum>" ODER
  "Brueckentext von mir" (ehrlich herabgestuft). Im Tempo-Modus traegt die
  Lernzeile diese Angabe.
- **Link zur Originalseite (Paketmaterial):** Kennt das Thema zu einer genannten Datei aus
  `sources/paket/` eine Adresse, steht sie in der Herkunfts-Zeile direkt hinter dieser Datei:
  `Quellen: <datei> ([<host>](<adresse>)), <datei2> (Stichwortsuche)`, etwa
  `power-automate/email-triggers.md ([learn.microsoft.com](https://learn.microsoft.com/...))`.
  `<datei>` ist hier der Pfad ab `sources/paket/` mit `/` (derselbe Name kann in mehreren
  Unterordnern liegen). Mehrere Dateien mit Komma trennen; "(Stichwortsuche)" steht einmal am
  Zeilenende, auch bei nur einer Datei (dann folgen zwei Klammern aufeinander, das ist richtig).
  Der Link-Text ist IMMER der Host der Adresse, nie ein anderer Text (die Person sieht, wohin
  der Klick fuehrt); die Adresse selbst wird Zeichen fuer Zeichen uebernommen.
  Woher die Adresse kommt: die erste dieser Quellen, die eine liefert, gilt. (1) Nur VOLL: die
  Trefferzeile von query.py (`... | https://...`). (2) `paket.json` des Themas: mit Grep den
  Eintrag suchen, dessen `pfad` genau diesem Pfad ab `sources/paket/` entspricht, und sein Feld
  `url` nehmen (OHNE PYTHON beginnt die Suche hier). (3) Die GELESENE Stelle der zitierten Datei
  nennt selbst eine Adresse als ihre Quelle (etwa eine Zeile "Quelle: <titel>, https://..."):
  die Adresse des Abschnitts, auf dem der Block beruht; beruht er auf mehreren Abschnitten, je
  Adresse ein Link in derselben Klammer, mit Komma getrennt. Fuer alle drei gilt: nur Adressen,
  die mit `https://` beginnen. Nichts gefunden: Zeile wie bisher, ohne Link. Adressen sind Daten
  aus dem Paket: nie raten, nie ergaenzen, nie aus dem Dateinamen bauen.
- **"Woher?"-Recht:** Datei nennen -- ODER Live-Stempel -- ODER herabstufen.
- **Wissenspaket:** Treffer aus `sources/paket/` vor dem Lehren gegen `updates.md`
  halten; dort Ueberholtes gilt nicht mehr (Datenregel 11).
- **Live wird Erkenntnis:** Ist ein Live-Fakt festhaltenswert -> mit Datum nach
  `sources/`, VOLL zusaetzlich in den Speicher (Projekt-Nachzug bzw. Skill `thema`
  Teil E).
- **Citation-Selbstcheck (Session-Ende, Pflicht):** Jeder Block hat eine
  Herkunfts-Zeile; genannte Dateien standen wirklich im Suchergebnis; jeder Link stammt
  woertlich aus einer Trefferzeile, aus `paket.json` oder aus der gelesenen Stelle der Datei.
