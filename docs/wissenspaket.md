# Wissenspaket: Format 1

Ein Wissenspaket ist fertiges Lernmaterial für den Weisen (ab 4.1.0). Es ist ein eigenes Claude-Code-Plugin, das nur Daten enthält. `/weise:paket` prüft es und legt daraus ein Lernthema an. Lernziel, Lernstand, Synthese und Abfrage-Karten gehören nicht ins Paket, sie entstehen bei der Person, die es einspielt.

## Aufbau

```
<paket>/
  .claude-plugin/plugin.json   Name (Vorschlag: weise-<thema>), version, description, author
  weise-paket.json             Manifest (siehe unten)
  sources/                     das Material: nur .md und .txt, Unterordner erlaubt
  sources/readme.md            Inhaltsverzeichnis (Kapitel, Titel, Datei)
  README.md                    für Menschen: Inhalt, Stand, Herkunft, Nutzungshinweis
```

Keine Befehle, keine Hooks, kein Server: Hat ein Paket `skills/`, `commands/`, `agents/`, `hooks/` oder `.mcp.json`, spielt der Weise es nicht ein.

`sources/readme.md` wird nicht in den Speicher gelegt und nicht durchsucht. Der Weise liest es als Landkarte, um den Lernpfad zum Ziel der Person zu bauen.

## Manifest `weise-paket.json`

UTF-8 ohne BOM.

| Feld | Inhalt |
|---|---|
| `format` | `1` |
| `paket` | Name des Pakets, gleich dem Plugin-Namen |
| `thema` | Vorschlag für den Ordnernamen des Themas (kebab-case) |
| `titel` | lesbarer Titel |
| `version` | gleich `version` in plugin.json; bei jeder Änderung des Materials erhöhen |
| `stand` | Datum des Materials, `JJJJ-MM-TT` |
| `sprache` | Sprache des Materials, etwa `en` oder `de` |
| `volatilitaet` | `hoch (4 Wochen)`, `mittel (3 Monate)` oder `niedrig (12 Monate)`, dazu ein Satz warum |
| `quelle` | woher das Material stammt |
| `hinweis` | Nutzungshinweis (etwa Lizenz), wird der Person vor dem Einspielen gezeigt |
| `anzahl` | Zahl der Einträge in `dateien` |
| `dateien` | Liste mit `{ "pfad": "<relativ zu sources/, mit />", "sha256": "<64 Zeichen, klein>" }`, einschließlich `readme.md` |

## Zeilenenden (Pflicht)

Git für Windows stellt beim Herunterladen standardmäßig die Zeilenenden um. Dann stimmt keine Prüfsumme mehr. Jedes Repo, das Wissenspakete ausliefert, braucht deshalb vor dem ersten Commit eine Datei `.gitattributes` mit dieser Zeile:

```
* -text
```

Die Prüfsummen werden über die Dateien so berechnet, wie sie im Commit liegen.

## Ausliefern

Ein Paket steht wie jedes Plugin in einem Katalog (`.claude-plugin/marketplace.json`). Für Lizenzmaterial gehört der Katalog in ein privates Repo; wer es nutzen will, braucht Lesezugriff, und die Anmeldung muss in Git gespeichert sein, bevor Claude Code den Katalog lädt. Ein Paket funktioniert auch ohne Katalog als Ordner: `/weise:paket <ordner>`.
