---
name: einrichten
description: Richtet den Weisen auf diesem Rechner ein oder aendert die Einrichtung. Fragt das Profil ab (Name der Persona, Anrede, Name der Person, Recherche-Weg, Werkraum), schreibt es nach config.json, legt die Ordner an, sichert alte Skill-Kopien, prueft die Betriebsart und bietet die volle Fassung mit Python (Bedeutungssuche, FSRS-Karten) an. Nur per Befehl /weise:einrichten.
disable-model-invocation: true
---

# Einrichten: den Weisen auf diesem Rechner einrichten

Vor dem ersten Datenzugriff `${CLAUDE_PLUGIN_ROOT}/references/daten.md` lesen.

Gefahrlos wiederholbar: Jeder Schritt prueft zuerst, was schon da ist, fragt nur Fehlendes ab und
aendert nichts ohne Zustimmung. Windows zuerst. Auf macOS und Linux laeuft der Weise nur OHNE
PYTHON: das zu Beginn in einem Satz sagen und Schritt 6 auslassen. Befehle unten: PowerShell
(macOS/Linux sinngemaess mit `mkdir -p`, `cp -n`, `mv`).

## 1. Stand lesen

1. `<WEISE_HOME>` bestimmen (Datenregel 1), `<WEISE_HOME>\config.json` lesen (Datenregel 3).
   Fehlt sie: erste Einrichtung.
2. Still pruefen, ohne etwas zu aendern: Werkraum vorhanden (Datenregel 4)? Betriebsart
   (Datenregel 5)? Technik aktuell (Datenregel 6)? Alte Kopien (Schritt 5)?
3. Der Person in zwei Saetzen sagen, was passiert: sechs kurze Fragen, Ordner anlegen, auf Wunsch
   die volle Fassung mit Python (die dauert laenger, alles andere geht schnell).
4. Gibt es schon ein Profil: kurz zeigen (je Feld eine Zeile) und fragen, ob etwas geaendert
   werden soll. Nur Fehlendes oder zu Aenderndes fragen.

## 2. Profil abfragen

Erst im Chat nach dem Namen der Person fragen (freie Eingabe, "ohne Namen" ist erlaubt). Die
uebrigen fuenf Fragen mit dem Auswahl-Werkzeug der Sitzung in einem Fenster, sonst nummeriert im
Chat. Vorhandene Werte als Vorschlag zeigen.

**Eigener Agent zuerst** (daten.md, Abschnitt "Profil"): Vor dem Fragen in den geladenen
Anweisungen der Person nachsehen, ob ihr Agent schon einen Namen, eine Anrede oder eigene
Zeichen- und Emoji-Regeln hat. Dann diese als ersten Vorschlag zeigen, mit einem Satz, woher er
kommt ("Ihr Agent heisst Max, deshalb schlage ich 'Max der Weise' vor").

| Frage | Auswahl | Feld |
|---|---|---|
| Wie heissen Sie? | freie Eingabe oder ohne Namen (leer) | `nutzer` |
| Wie soll der Weise heissen? | "<Name des Agenten> der Weise" (falls vorhanden), "Der Weise" oder eigener Name | `persona` |
| Wie soll er Sie ansprechen? | Anrede des Agenten (falls vorhanden), Sie, du | `anrede` |
| Mit Zeichen und Totems? | 🧙 und die Totems des Weisen (Standard), die Zeichen Ihres Agenten (falls vorhanden), ohne | `zeichen`, `totems` |
| Wie soll recherchiert werden? | werkzeug / websuche (je ein Satz, unten) | `recherche` |
| Wo sollen die Lernthemen liegen? | `<WEISE_HOME>\themen` (Standard) oder anderer Ordner | `werkraum` |

- **Zeichen und Totems:** Standard `zeichen` "🧙", `totems` true. "Die Zeichen Ihres Agenten":
  `zeichen` nach dessen Regeln, `totems` false. "Ohne": `zeichen` leer, `totems` false.

- **werkzeug:** "Fuer jedes Recherche-Thema schreibe ich einen fertigen Auftrag (Prompt) nach
  `auftraege/`, mit Nummer (R1, R2, ...). Sie geben ihn in Ihr eigenes Recherche-Werkzeug und legen
  das Ergebnis unter derselben Nummer nach `eingang/`."
- **websuche:** "Ich suche selbst im Netz, nachdem Sie die Liste der Recherche-Themen freigegeben
  haben."
- **Werkraum:** voller Pfad; nicht in OneDrive oder einen anderen synchronisierten Ordner. Ein
  Werkraum aus einer frueheren Fassung bleibt, wie er ist.
- Nennt die Person von sich aus ein anderes Zeichen, dieses als `zeichen` eintragen.

## 3. Ordner anlegen

```
$h = "<WEISE_HOME>"; $w = "<werkraum>"
New-Item -ItemType Directory -Force -Path $h, $w, "$h\sicherung", "$h\vorschlaege" | Out-Null
foreach ($f in "_themen.md", "werkzeug-register.md") {
  if (-not (Test-Path "$w\$f")) { Copy-Item "${CLAUDE_PLUGIN_ROOT}/setup/$f" "$w\$f" } }
```

Vorhandene Dateien nie ueberschreiben.

## 4. Profil speichern

`config.json` zusammenfuehrend schreiben (daten.md, Abschnitt "Profil"): lesen, nur `format` (1),
`nutzer`, `persona`, `anrede`, `zeichen`, `totems`, `recherche` und `werkraum` setzen, alles
Uebrige erhalten.
Zuruecklesen; Erfolg erst melden, wenn die neuen Werte dort stehen. Scheitert das Schreiben:
Meldung woertlich zeigen, nicht so tun, als waere gespeichert.

## 5. Alte Kopien (Umstieg von einer frueheren Fassung)

Liegt `%USERPROFILE%\.claude\skills\weise\SKILL.md` oder `%USERPROFILE%\.claude\skills\learn\SKILL.md`
vor (macOS/Linux: `~/.claude/skills/...`):
1. Erklaeren: "Hier liegt noch eine fruehere Fassung des Weisen als eigener Skill. Sie wuerde neben
   dem Plugin mitgeladen; dann antworten zwei Fassungen auf dieselben Saetze."
2. Fragen, ob sie in die Sicherung soll. Die Lernthemen bleiben unberuehrt.
3. Nach Zustimmung verschieben, nie loeschen (Ziel schon vorhanden: `-HHMM` anhaengen):
   `Move-Item "$env:USERPROFILE\.claude\skills\<name>" "<WEISE_HOME>\sicherung\<name>-<JJJJ-MM-TT>"`
   Liegt `<WEISE_HOME>` auf einem anderen Laufwerk als das Benutzerprofil (Move-Item verschiebt
   Ordner nicht ueber Laufwerke hinweg): erst `Copy-Item -Recurse` in die Sicherung, pruefen, dass
   dort `SKILL.md` liegt, erst dann das Original mit `Remove-Item -Recurse` entfernen. Ohne
   geglueckte Kopie nichts entfernen.
4. Im Abschluss um eine neue Sitzung bitten (erst dann laedt nur noch das Plugin).

Ohne Zustimmung: nichts verschieben, auf die Doppelung hinweisen.

## 6. Betriebsart (nur Windows)

**venv vorhanden (VOLL):** Selbsttest laufen lassen, Ausgabe woertlich zeigen:
`& "<WEISE_HOME>\venv\Scripts\python.exe" "<WEISE_HOME>\scripts\self-check.py"`
Ziel: "Selbsttest bestanden". Meldet er FEHLER oder ist die Technik aelter als das Plugin
(Datenregel 6): die Installation unten erneut anbieten (gefahrlos wiederholbar, Reparatur und
Update in einem).

**venv fehlt:** VOLL anbieten, mit allen Angaben, zum Beispiel:
> "Der Weise laeuft schon jetzt, mit Stichwortsuche in Ihren Themen-Dateien. Die volle Fassung
> sucht nach Bedeutung statt nach Stichwoertern und plant die Abfrage-Karten genauer (FSRS).
> Dafuer: rund 1,5 GB Download, 2,5 GB Platz, 10 bis 30 Minuten. Quellen: python.org (ueber
> winget), pypi.org, huggingface.co. Keine Adminrechte noetig; Python kommt nur fuer Ihren Benutzer
> dazu und aendert kein anderes Python. winget nimmt dabei die Nutzungsbedingungen der Paketquelle
> an. Danach arbeiten die Skripte offline. Soll ich installieren?"

- **Ablehnen:** OHNE PYTHON, fertig. Spaeter jederzeit mit /weise:einrichten.
- **Zustimmung:** als Hintergrundbefehl starten (dauert laenger, als ein einzelner Befehl darf):
  `powershell -NoProfile -ExecutionPolicy Bypass -File "${CLAUDE_PLUGIN_ROOT}/setup/install.ps1" -WeiseHome "<WEISE_HOME>"`
  `-ExecutionPolicy Bypass` gilt nur fuer diesen Aufruf und aendert keine Einstellung des Rechners.
  Waehrenddessen mit Schritt 7 weitermachen. Die letzte Zeile muss "Fertig. Der Weise ist
  eingerichtet." lauten, davor "Selbsttest bestanden". Sonst: Meldung woertlich zeigen, in den
  Fehlerbildern unten nachsehen, OHNE PYTHON bleiben.
- **Schutzprogramm stoppt den Installer** (Virenschutz, Richtlinie): nichts umgehen, auch keinen
  anderen Weg zu Python suchen. OHNE PYTHON bleiben und anbieten, die IT mit der woertlichen Meldung
  um Freigabe zu bitten.
- **Nach geglueckter Installation mit vorhandenen Themen:** jedes Thema einmal speichern
  (`learn-store.py --thema <name>`, Aufruf wie Datenregel 5). Vorhandene `recall-cards.md` bleiben
  die Kartendatei ihres Themas; es geht keine Karte verloren.

**OHNE PYTHON, oder wenn etwas hakt:** Handpruefung, je Punkt OK / HINWEIS / FEHLER: `config.json`
lesbar und gueltiges JSON, Werkraum mit `_themen.md` vorhanden, keine alte Kopie (Schritt 5).
Meldungen woertlich zeigen, nicht raten.

## 7. Lesen ohne Rueckfrage (Angebot)

Sonst fragt Claude bei Dateien ausserhalb des Projektordners nach. Angebot: `<WEISE_HOME>` (und den
Werkraum, falls er ausserhalb liegt) in `%USERPROFILE%\.claude\settings.json` unter
`permissions.additionalDirectories` eintragen.
1. Datei lesen; fehlt sie, mit `{}` beginnen. Ist sie kein gueltiges JSON: nichts schreiben, das
   sagen.
2. Die Aenderung vorher zeigen (nur den betroffenen Ausschnitt) und Zustimmung holen.
3. Zusammenfuehren: alle uebrigen Einstellungen und vorhandene Eintraege erhalten, nichts doppelt.
4. Zuruecklesen. Wirkt spaetestens ab der naechsten Sitzung.

Ohne Zustimmung: Hinweis, dass beim Lesen im Werkraum Rueckfragen kommen koennen.

## 8. Abschluss (hoechstens fuenf Zeilen)

```
Profil:       <zeichen> <persona>, Anrede <Sie|du>, <nutzer | ohne Namen>, Totems <an|aus>, Recherche <werkzeug|websuche>
Betriebsart:  <VOLL (Selbsttest bestanden) | OHNE PYTHON | VOLL wird installiert, ich melde mich>
Werkraum:     <pfad> (<n> Themen)
Erster Schritt: "Neues Lernthema: <Thema>"  (gibt es schon Themen: "Lern-Session <thema>")
<nur wenn noetig: Bitte eine neue Sitzung starten (alte Kopie gesichert / Einstellungen geaendert).>
```

Laeuft die Installation noch: nach ihrem Ende das Ergebnis in einer Zeile nachreichen.

## Fehlerbilder (Installation und Selbsttest)

| Sie sehen ... | Wahrscheinliche Ursache | Tun |
|---|---|---|
| "Die Ausfuehrung von Skripts ist auf diesem System deaktiviert" | Richtlinie | Aufruf genau wie in Schritt 6 (mit `-ExecutionPolicy Bypass`); bleibt es: OHNE PYTHON, IT fragen |
| "Der Technik-Ordner liegt zu tief" oder pip: `No such file or directory` mit Hinweis auf "Long Path" | Windows-Pfadgrenze 260 Zeichen | kuerzeren Ort als `WEISE_HOME` waehlen (Benutzer-Umgebungsvariable), neue Sitzung, erneut einrichten |
| winget-Fehler, danach Download von python.org | winget fehlt oder ist gesperrt | nichts, das Skript nimmt den zweiten Weg |
| "Python-Installer endete mit Code ...", "darf nicht starten" oder "winget meldet Erfolg, aber Python fehlt" | Installation blockiert (Richtlinie, Virenschutz) | Nichts umgehen. OHNE PYTHON bleiben; Freigabe bei der IT anfragen |
| `SSL: CERTIFICATE_VERIFY_FAILED` bei pip | Die Firewall prueft verschluesselte Verbindungen | Meldung woertlich an die IT; nichts umgehen |
| `ProxyError` / Zeitueberschreitung bei pip | Proxy oder Verbindung bricht grosse Downloads ab | Installation erneut starten (setzt fort); bleibt es, Meldung an die IT |
| Modell-Download scheitert (huggingface.co / Speicher-CDN) | Download-Server gesperrt | Freigabe bei der IT anfragen; liegt das Modell schon in `<WEISE_HOME>\modelle\` (auch von Hand entpackt), prueft `download-model.py` nur |
| "You are sending unauthenticated requests to the HF Hub" | harmlose Warnung | nichts; das Modell ist frei und braucht keinen Schluessel |
| Selbsttest: "Sprachmodell fehlt" | Modell-Download lief nicht durch | `download-model.py` ausfuehren (Aufruf wie Datenregel 5) |
| Selbsttest: "Paket ... fehlt" | Paket-Installation unvollstaendig | Installation erneut starten |
| `query.py`: "Der Speicher ist noch leer" | Thema noch nicht gespeichert | `learn-store.py --thema <name>` |
| Die Skills des Weisen erscheinen nicht | Sitzung lief schon vor der Installation des Plugins | neue Sitzung starten oder `/reload-plugins` |
| Eine Datei wird vom Virenschutz zurueckgehalten | Schutzprogramm der Umgebung | Meldung woertlich an die IT; nichts umgehen |

Neue Fehlerbilder bitte per /weise:vorschlag melden (Meldung woertlich).

## Regeln

- Nichts umgehen: keine Sperre, keinen Virenschutz, keine Richtlinie.
- Nie loeschen, nur nach `<WEISE_HOME>\sicherung\` verschieben.
- `config.json` und `settings.json` immer zusammenfuehren, nie ueberschreiben.
- Nichts in den Plugin-Ordner schreiben (Datenregel 2).
- Aenderungen ausserhalb von `<WEISE_HOME>` (alte Kopien, `settings.json`, Installation) nur mit
  Zustimmung.
- Erfolg erst melden, wenn er geprueft ist (Zuruecklesen, Selbsttest).
