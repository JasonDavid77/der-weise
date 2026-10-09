# Changelog

Der Weise, von Jason Lau-Christen. Versionen nach dem Schema Hauptversion.Neuerung.Korrektur.

## 5.0.0 (Projektpfad, 09.10.2026)

- **Projektpfad zuerst:** Der Weise lehrt nicht mehr jedes Konzept eines Themas der Reihe nach. Die Konzeptliste ist jetzt die Karte des ganzen Themas. Gelernt wird entlang des Projektpfads: nur die Konzepte, die Ihr Projekt braucht, in der Reihenfolge des Baus.
- **Abgestimmt, bevor es losgeht:** Der Weise schlägt den Pfad vor, nennt die Zahl der übrigen Konzepte und fragt „Fehlt etwas, kann etwas weg?“. Ohne Ihr Ja beginnt kein Unterricht. Was Sie schon können, prüft er mit einer Frage und geht dann direkt in die Anwendung.
- **Das Board zeigt nur den Pfad:** links der Projektpfad, rechts die Bausteine, darunter die freien Konzepte als Zahl. Das Wort „Karte“ zeigt die ganze Karte mit Lernstand.
- **Mehrere Projekte je Thema:** „Neues Projekt zu <Thema>: …“ startet ein weiteres Projekt auf derselben Karte. Jedes Projekt hat einen eigenen Ordner `projekte/<name>/` mit Pfad, Bausteinen und Bau-Stand. Schon Gelerntes erscheint dort als „gelernt in <Projekt>“ und läuft nur noch über die Anwendung. Übungsdokumente bleiben in einem Ordner je Thema.
- **Projektende:** Ist der letzte Baustein fertig, fragt der Weise, ob Sie freie Konzepte als Übung weiterlernen, ein neues Projekt beginnen oder aufhören wollen.
- **Abfrage-Karten:** Neue Themen bekommen Karten nur für Konzepte auf dem Pfad. Eine Karte wird erst gestellt, wenn ihr Konzept gelehrt ist; bis dahin ruht sie. Fehlt einem gelehrten Konzept die Karte, legt der Weise sie an.
- **Laufende Themen:** Der Weise schlägt einmal vor, aus dem bisherigen Projekt einen Projektpfad zu machen. Ohne Ihr Ja bleibt der Ablauf, wie er war. Lernstand und Karten bleiben in jedem Fall erhalten. Themen ohne Projekt laufen wie bisher.
- **Vertrauliche Fälle:** Ist Ihr Projekt ein echter Fall, fragt der Weise danach. Dann bleiben Projektname und Bausteine im Themenordner neutral, und was Sie bauen, liegt nur an Ihrem eigenen Ort.

### Woran Sie es merken

- Bei einem neuen Lernthema mit Projekt zeigt der Weise, sobald der erste Stoff da ist, die Karte und dann den Projektpfad mit der Frage „Fehlt etwas, kann etwas weg?“.
- Im Board steht bei Themen mit Projektpfad PROJEKTPFAD statt LERNPFAD und die Zeile „Frei (nicht im Projekt): … Konzepte“.
- Neue Themen haben im Themenordner den Ordner `projekte`.
- Bei einem Thema von früher kommt nach dem Board einmal die Frage, ob der Weise daraus einen Projektpfad machen soll.

## 4.3.0 (08.10.2026)

- **Alle Pakete sehen und wählen:** `/weise:paket` zeigt immer eine Liste, auch bei nur einem Paket: installierte Pakete, Pakete aus Ihren bekannten Katalogen und Pakete aus Ordnern, je mit Zustand (eingespielt, bereit, nicht geladen). Danach wartet der Weise auf Ihre Wahl.
- **Einspielen ohne Installation:** Liegt ein Paket im Repo seines Katalogs, reicht es, den Katalog hinzuzufügen. Der Weise liest und prüft es dort.
- **Kennzeichen im Katalog:** Wissenspakete tragen im Katalog-Eintrag `"category": "weise-paket"`.
- **Privater Katalog scheitert an der Anmeldung:** Der Weise prüft den Zugang und nennt den einen Befehl, mit dem Sie sich in Ihrem eigenen Fenster anmelden. Er meldet nie selbst an und fasst keine Schlüssel an.
- **Deutlicher im Befehl:** Der Ordner hinter `/weise:paket` ist als „optional“ gekennzeichnet.

Beruht auf zwei Dateien von Claude Code, deren Aufbau nicht dokumentiert ist (`installed_plugins.json`, `known_marketplaces.json`). Fehlen sie, zeigt der Weise, was er auf den übrigen Wegen findet.

### Woran Sie es merken

- `/weise:paket` beginnt mit einer Liste und einer Frage, auch wenn nur ein Paket da ist.
- Pakete aus einem hinzugefügten Katalog stehen als „bereit“ in der Liste, ohne dass Sie sie installiert haben.

## 4.2.0 (08.10.2026)

- **Recherche-Aufträge mit Nummer:** Jeder Auftrag heißt `R<n>-<Datum>-<Thema>.md`. Die Nummer läuft über das ganze Thema fort, das Datum zeigt den Stand.
- **Übergabe als Ordner statt als Text:** Der Weise wiederholt die Prompts nicht mehr im Gespräch. Er nennt Ordner und Dateien, öffnet den Ordner im Dateimanager und gibt eine kurze Anleitung.
- **Übersicht:** `auftraege/readme.md` führt je Auftrag Thema, Zweck, Datum, Ergebnis und Stand (offen, zurück, eingearbeitet).
- **Rücklauf unter der Nummer:** Ihr Ergebnis legen Sie als `R<n>` in den Ordner `eingang`, am besten als Markdown oder Text. Zu Beginn der nächsten Session ordnet der Weise es zu, legt es als Quelle ab und arbeitet es sofort in die Synthese ein, mit Verweis auf die Nummer. Überholtes wandert in die Änderungsliste.
- **Recherche-Ergebnisse im Überblick:** Die Synthese hat einen Abschnitt mit einer Zeile je Auftrag.

### Woran Sie es merken

- Nach der Freigabe der Themenliste öffnet sich der Ordner mit `R1-…`, `R2-…`; im Gespräch steht nur die Anleitung.
- Liegt `R2.md` im Eingang, sagt der Weise das zu Beginn der Session und arbeitet es ein; in der Übersicht steht R2 danach auf „eingearbeitet“.

## 4.1.1 (08.10.2026)

- **Vorschläge ohne doppeltes Prüfen:** Ihre Freigabe im Gespräch ist der letzte Schritt. Ist die GitHub-Kommandozeile `gh` angemeldet, sendet der Weise den Vorschlag direkt und nennt den Link; vorher nennt er das Konto, unter dem das Issue erscheint. Sonst öffnet er das ausgefüllte Formular, und es bleibt ein Klick. „Nur speichern“ gibt es weiterhin.
- **Stand in der gespeicherten Kopie:** Jeder Vorschlag trägt, ob er gespeichert, im Browser geöffnet oder eingereicht ist.
- **Warnung bei altem Paketmaterial:** Ist ein Wissenspaket beim Einspielen über seiner eigenen Frist, sagt der Weise das vor dem Kopieren in einem eigenen Satz und im Bericht. Im Deckblatt steht „Frist bis <Datum>“.
- **Eine Fristregel für alles:** hoch = 28 Tage, mittel = 3 Monate, niedrig = 12 Monate; der Weise rechnet sie aus, statt zu schätzen.

### Woran Sie es merken

- Bei `/weise:vorschlag` fragt der Weise nach dem Text, ob er direkt senden, das Formular öffnen oder nur speichern soll.
- Bei `/weise:paket` mit älterem Material kommt vor dem Kopieren der Satz „Achtung: Das Material ist vom …“.

## 4.1.0 (Wissenspakete, 01.10.2026)

- **Neuer Befehl `/weise:paket`:** spielt ein Wissenspaket als Lernthema ein. Ein Wissenspaket ist ein eigenes Plugin mit fertigem Lernmaterial, ohne Lernziel und ohne Lernstand. Der Weise prüft jede Datei per Prüfsumme, fragt nach Ihrem Lernziel und legt das Thema an, bei VOLL auch im Speicher.
- **Updates von Paketen** tauschen nur das Paketmaterial im Ordner `sources/paket/` und legen den alten Stand ins Archiv. Dateien, die Sie dort selbst geändert haben, kopiert der Weise vorher in den Eingang des Themas.
- **Pakete als Ordner:** Liegt ein Paket als Git-Klon vor, geht `/weise:paket <ordner>`; Klone gehören nach `%USERPROFILE%\weise\pakete\`.
- **Frische-Check:** Bei Themen aus einem Paket zählt das Datum des Materials (Zeile „Paketstand“), und der Weise weist zuerst auf ein neueres Paket hin.
- **Neues Lernthema:** Passt ein installiertes Paket zum Thema, bietet der Weise `/weise:paket` an.
- **README:** Klickweg der Desktop-App im Schnellstart, Abschnitt „Wissenspakete“.

### Woran Sie es merken

- Es gibt den Befehl `/weise:paket`.
- Bei „Neues Lernthema: …“ fragt der Weise nach, wenn ein passendes Paket installiert ist.
- Themen aus einem Paket haben im Deckblatt die Zeile „Paketstand“ und den Ordner `sources/paket/`.

## 4.0.0 (erste öffentliche Version, 01.10.2026)

Der Weise wird ein Plugin für Claude Code, das jede Person für sich einrichtet.

- **Installation aus dem Katalog** `jason-lau-christen` statt Kopieren von Dateien; Updates laufen über Claude Code.
- **Vier Skills:** `lernen` (früher `weise`) und `thema` (früher `learn`), neu dazu `einrichten` und `vorschlag`.
- **Für jede Person einstellbar:** Name der Persona, Anrede, eigener Name, Weg für Recherchen und Ordner der Lernthemen stehen im Profil `config.json`. Standard: „Der Weise“, Anrede „Sie“. Das Profil wird immer zusammengeführt, nie überschrieben.
- **Zauberer und Totems:** Der Sessionkopf trägt im Standard 🧙, und bedeutungstragende Zeichen zeigen den Schritt (📖 Lerneinheit, ❓ Frage, 🛠️ Bauanleitung, 🔁 Abfrage-Karte und weitere). Abschaltbar; hat Ihr Agent eigene Zeichen, gelten diese.
- **Name vom eigenen Agenten:** Hat Ihr Agent schon einen Namen, schlägt `/weise:einrichten` ihn vor („Max der Weise“), ebenso dessen Anrede.
- **Recherche nach Wahl:** Der Weise schreibt Aufträge für Ihr eigenes Recherche-Werkzeug oder sucht selbst im Internet, in beiden Fällen erst nach Freigabe der Themenliste.
- **Neue Ordnernamen im Thema:** `auftraege/` (vom Weisen an Sie) und `eingang/` (von Ihnen). Ältere Themen behalten ihre bisherigen Ordner.
- **Sprache:** Der Weise antwortet in der Sprache, in der Sie schreiben.
- **Vorschläge per Befehl:** `/weise:vorschlag` formt einen Vorschlag (Anlass, alter und neuer Absatz, Test), entfernt Namen, Pfade und vertrauliche Angaben und öffnet nach Ihrer Freigabe ein vorausgefülltes Issue.
- **Technik:** Der Technik-Ordner ist fest `%USERPROFILE%\weise` (oder `WEISE_HOME`), nie der Plugin-Ordner. Die Installation kopiert keine Skills mehr, führt `config.json` zusammen und hält die Version in `version.txt` fest.
- **Umstieg:** Ältere Kopien unter `%USERPROFILE%\.claude\skills` verschiebt `/weise:einrichten` nach Zustimmung in die Sicherung.
- **Lern-Skill kürzer:** Die Regeln zu Wissen und Abfrage-Karten liegen in eigenen Dateien, Inhalt unverändert.
- **Neue Dokumentation:** README auf Deutsch und Englisch, Hilfe mit Fehlerbildern, Sicherheitsrichtlinie, MIT-Lizenz.

### Woran Sie es merken

- Nach der Installation gibt es `/weise:einrichten`, `/weise:thema`, `/weise:lernen` und `/weise:vorschlag`.
- Der Sessionkopf trägt den Namen, den Sie beim Einrichten gewählt haben, im Standard mit 🧙.
- Neue Themen haben die Ordner `auftraege/` und `eingang/`.
- Schreiben Sie auf Englisch, antwortet der Weise auf Englisch.
- Ist nach einem Update die Technik älter als das Plugin, sagt der Weise das in einem Satz und verweist auf `/weise:einrichten`.

---

## Vorgeschichte (nicht öffentlich erschienen)

### 3.2

- **Recherche erst besprechen:** Vor jeder Recherche liest der Weise die Unterlagen, bespricht den Bedarf und legt eine Themenliste zur Freigabe vor; erst danach entsteht je Thema ein kurzer Auftrag.
- Woran Sie es merken: Beim neuen Thema kommen zuerst ein Gespräch und eine Themenliste, kein fertiger Rechercheauftrag.

### 3.1: läuft auch ohne Python

Anlass: Auf einem Testrechner stoppte ein Schutzprogramm den Python-Installer.

- **Zwei Betriebsarten, automatisch erkannt:** VOLL und OHNE PYTHON. Ohne Python sucht der Weise nach Stichworten auf Deutsch und Englisch und plant Wiederholungen mit einer Fächer-Regel.
- **Kein Kartenverlust beim Umstieg:** Je Thema gilt genau eine Kartendatei.
- **Stichwortsuche nur im aufbereiteten Stoff** (`synthesis.md`, `sources/`), Suchwörter mit und ohne Umlaut.
- **Recherchen** laufen über ein externes Werkzeug der Person, eigene Websuche nur auf ausdrückliche Ansage.
- **Installation** prüft nach winget selbst, ob Python wirklich da ist, und bricht sonst mit einem klaren Hinweis ab.
- Woran Sie es merken: Das Board zeigt „OHNE PYTHON“; Quellenzeilen tragen „(Stichwortsuche)“; Karten stehen in `recall-cards.md`.

### 3.0

- **Der Lernpfad wächst mit dem Projekt:** Neue Stationen führen am Ende eines Blocks zu neuen Konzepten (Board: „NEU IM LERNPFAD“).
- **Tempo-Modus:** Unter Zeitdruck wird gebaut, das Lernen läuft mit (Lernzeile je Schritt, Fragen-Parkplatz, kurze Bilanz).
- **Übung mit Ansage,** wenn das Projekt ein Konzept nicht braucht; Sie entscheiden: jetzt, später, überspringen.
- **Beim Werkzeug-Lernen ein Schritt auf einmal:** Lerneinheit, eine Frage, Bauanleitung, echte Beschriftungen.
- **Vorher den Stand prüfen:** Abfrage-Karten werden vor dem Abfragen gegen den Ist-Stand geprüft; die Bedienkarte `ui-observed.md` gehört zu jedem Werkzeug-Thema.
- **Am echten Ziel bleiben:** Offene Fragen zum Projekt kommen zuerst, der Übungsfall zeigt die Stärke des Werkzeugs.
- **Der Speicher liest ganze Abschnitte:** Abschnitte von 400 Zeichen, jeder mit dem echten Tokenizer geprüft; abgeschnitten wird nichts mehr.
- **Technik:** eigene Python-Umgebung mit festen Paketversionen, Telemetrie aus, nach dem Modell-Download offline, Selbsttest `self-check.py`.

Frühere Fassungen waren interne Vorläufer.
