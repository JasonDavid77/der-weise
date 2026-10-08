# Der Weise: learning on the job

**Deutsch** | [English](README.en.md)

Der Weise ist ein Lernpartner für Claude Code, der Ihnen ein Werkzeug oder ein Fachgebiet beibringt, während Sie damit an einem echten Projekt arbeiten. Er erklärt jedes Konzept von Grund auf, wendet es sofort auf Ihr Projekt an und festigt das Gelernte mit Abfrage-Karten. Gedacht ist er für Menschen ohne Technikwissen, zum Beispiel Juristinnen und Juristen, die KI-Werkzeuge in ihre Arbeit holen.

Der Weise arbeitet in der Claude-Desktop-App im Reiter „Code“ oder in Claude Code im Terminal, nicht im normalen Chat.

## Schnellstart

**In der Claude-Desktop-App per Klick:** unten links auf Ihr Profil, dann **Einstellungen**, im Fenster unter **Anweisungen** auf **Plugins**. Dort das Repo `JasonDavid77/claude-plugins` angeben, dann beim Weisen auf das Plus-Zeichen. Weiter mit Schritt 3.

**Oder per Befehl** (Desktop-App im Reiter „Code“ oder Terminal):

1. Katalog hinzufügen. Geben Sie im Eingabefeld von Claude Code ein:

   ```
   /plugin marketplace add JasonDavid77/claude-plugins
   ```

2. Den Weisen installieren:

   ```
   /plugin install weise@jason-lau-christen
   ```

   Beides in einem Schritt geht auch: `/plugin install weise --marketplace JasonDavid77/claude-plugins`

3. Eine neue Sitzung starten (oder `/reload-plugins` eingeben) und den Weisen einrichten:

   ```
   /weise:einrichten
   ```

   Der Weise fragt im Gespräch nach seinem Namen, nach der Anrede (Sie oder du), nach Zeichen und Totems, nach Ihrem Namen, nach Ihrem Weg für Recherchen und nach dem Ordner für Ihre Lernthemen. Hat Ihr eigener Agent schon einen Namen, schlägt er diesen vor: Aus „Max“ wird „Max der Weise“. Danach schlägt er den ersten Schritt vor, etwa „Neues Lernthema: …“.

## Die fünf Skills

| Befehl | Was er tut |
|---|---|
| `/weise:einrichten` | Richtet den Weisen im Gespräch ein und bietet die volle Suche an; startet nur, wenn Sie den Befehl eingeben. |
| `/weise:thema` | Legt ein neues Lernthema an oder aktualisiert ein bestehendes, beginnend mit Ihrem Lernziel. |
| `/weise:lernen` | Führt eine Lern-Session: erst fällige Abfrage-Karten, dann das nächste Konzept, erklärt und gleich an Ihrem Projekt gebaut. |
| `/weise:vorschlag` | Macht aus Ihrem Verbesserungswunsch einen Vorschlag und reicht ihn nach Ihrer Freigabe als öffentliches Issue ein. |
| `/weise:paket` | Spielt ein Wissenspaket als Lernthema ein oder aktualisiert es (siehe unten); startet nur, wenn Sie den Befehl eingeben. |

Sie müssen die Befehle nicht auswendig kennen. Sätze wie „Neues Lernthema: …“, „Lern-Session“, „lernen wir weiter“ oder „frag mich ab“ genügen.

## Wissenspakete

Ein Wissenspaket ist fertiges Lernmaterial zu einem Thema, zum Beispiel die Anleitungen eines Werkzeugs als Text. Es ist ein eigenes kleines Plugin ohne Befehle und enthält nur Daten: die Texte und eine Liste mit einer Prüfsumme je Datei. Lernziel, Lernstand und Abfrage-Karten enthält es nicht, die entstehen bei Ihnen. Bringt ein Paket doch Befehle, Hooks oder einen Server mit, spielt der Weise es nicht ein. Installieren Sie Pakete nur aus Katalogen, denen Sie vertrauen. Wie ein Paket aufgebaut ist, steht in [docs/wissenspaket.md](docs/wissenspaket.md).

1. Paket installieren wie jedes Plugin, über den Katalog, in dem es steht.
2. `/weise:paket` aufrufen. Der Weise findet die installierten Pakete, prüft jede Datei, fragt nach Ihrem Lernziel und legt das Thema in Ihrem Themenordner an, bei VOLL auch im Speicher. Liegt ein Paket als Ordner vor (etwa als Git-Klon), geben Sie den Ordner an: `/weise:paket <ordner>`.
3. Kommt eine neue Paketversion, rufen Sie `/weise:paket` wieder auf. Der Weise tauscht nur das Paketmaterial im Ordner `sources/paket/` und legt den alten Stand ins Archiv. Ihr Lernziel, Ihre Notizen, Ihre Karten und Ihre eigenen Quellen bleiben.

Pakete aus einem privaten Katalog brauchen Lesezugriff auf dessen Repo. Claude Code kann beim Laden nicht nach einem Passwort fragen; die Anmeldung muss vorher in Git gespeichert sein (am einfachsten: das Repo einmal selbst klonen).

## Ein Beispiel

So hat der Weise uns selbst durch einen echten Bau in Microsoft Power Automate geführt: erst die Lehre, dann der Bauschritt im Werkzeug. Das Gespräch unten ist nachgestellt und gekürzt, Thema und Inhalte sind Testdaten.

> **Sie:** Neues Lernthema: TEST-Anfragen per Formular
>
> **Der Weise:** Gern. Zuerst das Ziel: Was soll am Ende laufen?
>
> **Sie:** Wer unser Formular ausfüllt, soll automatisch in einer Liste landen und eine Bestätigung per Mail bekommen.
>
> **Der Weise:** Dann ist das unser Ziel. Was wissen Sie schon über Power Automate, und wo hakt es? Danach lege ich Ihnen eine Themenliste für die Recherche zur Freigabe vor.

Einige Tage später, mitten im Bau:

> **Sie:** Lernen wir weiter.

```
🧙 Der Weise: TEST-Anfragen per Formular
| WISSEN: thema=test-anfragen, VOLL (180 Abschnitte) | Modus: NORMAL |
| LERNPFAD                           | DELIVERABLE-SPUR             |
| [x] K1 Auslöser              sitzt | [x] Formular steht           |
| [~] K2 Antwortdetails  <==   läuft | [~] Ablauf holt die Antwort  |
Formular > [Ablauf] > Liste > Mail
```

> **Der Weise:** 📖 K2, von Null: Der Auslöser meldet nur, *dass* jemand das Formular abgeschickt hat, und liefert eine Nummer dieser Antwort. Die Antworten selbst holt erst ein zweiter Schritt, „Antwortdetails abrufen“. Im Alltag: Die Klingel sagt Ihnen, dass Post da ist. Den Brief müssen Sie noch aus dem Kasten holen.
>
> ❓ Eine Frage, bevor wir bauen: Was stünde in der Liste, wenn wir diesen zweiten Schritt weglassen?
>
> **Sie:** Nur die Nummer, nicht die Antworten.
>
> **Der Weise:** ✅ Genau. 🛠️ Bauanleitung, ein Schritt:
> 1. Unter dem Auslöser „Wenn eine neue Antwort übermittelt wird“ auf **Aktion hinzufügen**.
> 2. In der Suche `Antwortdetails abrufen` eingeben und die Aktion von **Microsoft Forms** wählen.
> 3. **Formular-ID:** dasselbe Formular wie im Auslöser. **Antwort-ID:** aus dem dynamischen Inhalt die **Antwort-ID** des Auslösers.
> 4. **Speichern**, dann sagen Sie mir, was Sie sehen.
>
> *Quellen: sources/forms-ausloeser.md, Bedienkarte ui-observed.md*

So läuft jedes Werkzeug-Thema: erst die Idee von Null, dann eine Frage, dann ein einzelner Bauschritt mit den echten Beschriftungen. Was Sie gelernt haben, kommt als Abfrage-Karte wieder.

## Zwei Betriebsarten

Der Weise erkennt selbst, welche Betriebsart läuft. Das Board zeigt sie in der ersten Zeile.

- **VOLL** (empfohlen, Windows): mit einer eigenen Python-Umgebung und einem lokalen Speicher, der nach Bedeutung sucht. Eine deutsche Frage findet so auch eine englische Anleitung. Wiederholungen der Abfrage-Karten plant ein erprobtes Verfahren (FSRS). Einrichtung über `/weise:einrichten`, einmalig rund 1,5 GB Download.
- **Stichwortsuche** (im Board: OHNE PYTHON): ohne jede Installation. Der Weise sucht nach Stichworten auf Deutsch und Englisch in Ihren Themendateien, Wiederholungen plant eine einfache Fächer-Regel. Alles andere ist gleich. Diese Betriebsart gilt automatisch, wenn Python fehlt oder gesperrt ist.

Wechseln Sie später auf VOLL, rufen Sie `/weise:einrichten` erneut auf. Ihre Themen und Abfrage-Karten bleiben erhalten.

## Voraussetzungen

- **Claude Code:** die Claude-Desktop-App mit dem Reiter „Code“ oder Claude Code im Terminal.
- **Git:** Claude Code lädt den Katalog über Git. Prüfen Sie in PowerShell mit `git --version`. Fehlt Git, installieren Sie es von [git-scm.com](https://git-scm.com) oder fragen Sie Ihre IT. Ein GitHub-Konto brauchen Sie dafür nicht.
- **Zusätzlich für VOLL:** Windows (64 Bit), rund 2,5 GB freier Platz, einmal Internet für rund 1,5 GB Download und 10 bis 30 Minuten. Adminrechte sind nicht nötig.

**Grenzen:** Getestet ist der Weise unter Windows. Auf macOS und Linux ist nur die Stichwortsuche vorgesehen, und sie ist dort noch nicht getestet. Einen Installationsweg ohne Git gibt es derzeit nicht.

## Was der Weise auf Ihrem Rechner tut

- **Ihre Daten bleiben lokal** in einem Ordner: `%USERPROFILE%\weise` (änderbar über die Umgebungsvariable `WEISE_HOME`). Darin liegen Ihre Lernthemen (`themen\`, oder der Ordner, den Sie beim Einrichten wählen), Ihr Profil (`config.json`), Sicherungen und die Entwürfe Ihrer Vorschläge; bei VOLL zusätzlich Python-Umgebung, Speicher und Sprachmodell. In den Plugin-Ordner schreibt der Weise nichts, weil Claude Code ihn bei jedem Update ersetzt.
- **Downloads nur einmal und nur nach Ihrer Zustimmung** (VOLL): Python 3.12 von python.org (über winget, falls vorhanden), rund 95 Python-Pakete in festen Versionen von pypi.org und ein Sprachmodell (paraphrase-multilingual-MiniLM-L12-v2, rund 0,5 GB) von huggingface.co. Danach sucht der Weise offline.
- **Telemetrie ist aus:** Die Pakete senden keine Nutzungsdaten.
- **Keine Hooks, kein MCP-Server, kein Hintergrunddienst.** Der Weise läuft nur, wenn Sie ihn aufrufen, per Befehl oder mit einem Satz wie „Lern-Session“.
- **Claude-Einstellungen ändert er nur nach Rückfrage:** `/weise:einrichten` bietet an, den Ordner `%USERPROFILE%\weise` (und Ihren Themenordner, falls er woanders liegt) als zusätzlichen Arbeitsordner in `%USERPROFILE%\.claude\settings.json` einzutragen, damit der Weise dort ohne Rückfragen lesen kann. Die Änderung sehen Sie vorher. Findet er ältere Kopien des Weisen unter `%USERPROFILE%\.claude\skills`, verschiebt er sie nach Ihrer Zustimmung in die Sicherung. Gelöscht wird nichts.
- **Websuche nur, wenn Sie das wählen:** Mit der Einstellung „websuche“ sucht der Weise selbst im Internet, und zwar erst, wenn Sie die Themenliste freigegeben haben. Mit „werkzeug“ schreibt er Rechercheaufträge für Ihr eigenes Recherche-Werkzeug und sucht nur dann selbst, wenn Sie ihn ausdrücklich darum bitten.
- **Wissenspakete liest er nur:** `/weise:paket` liest die Liste Ihrer installierten Plugins (`%USERPROFILE%\.claude\plugins\installed_plugins.json`, ersatzweise den Plugin-Ordner) und die Ordner der Wissenspakete, prüft die Dateien per PowerShell und kopiert sie in Ihren Themenordner. Bei „Neues Lernthema“ sieht `/weise:thema` an denselben Stellen nach, ob ein passendes Paket installiert ist. In die Plugin-Ordner schreibt der Weise nichts.
- **Vorschläge nur nach Ihrer Freigabe:** `/weise:vorschlag` entfernt Namen, Pfade und vertrauliche Angaben, zeigt Ihnen den fertigen Text und fragt, wie er eingereicht werden soll. Ist auf Ihrem Rechner die GitHub-Kommandozeile `gh` angemeldet, kann der Weise den Vorschlag nach Ihrer Freigabe direkt senden; er nennt vorher das Konto, unter dem das Issue erscheint, und fragt dafür einmal bei github.com den Kontonamen ab. Sonst öffnet er das ausgefüllte Formular im Browser, und Sie klicken selbst auf Absenden. Sie können auch nur speichern. Ein Konto oder eine Anmeldung richtet der Weise nie ein. Issues auf GitHub sind öffentlich.
- **Das Gespräch selbst** verarbeitet Claude wie in jeder Claude-Code-Sitzung, einschließlich der Dateien, die der Weise dafür liest. Legen Sie deshalb keine vertraulichen Inhalte in Ihre Lernthemen, also keine Akten, Mandats- oder Kundendaten. Der Weise arbeitet mit Lernmaterial, Anleitungen und erfundenen Übungsfällen.

## Updates

Claude Code aktualisiert Kataloge von Dritten standardmäßig nicht von selbst. So schalten Sie das für diesen Katalog einmal ein: `/plugin` eingeben, „Marketplaces“ wählen, dann `jason-lau-christen`, dann „Enable auto-update“. Neue Versionen kommen danach beim Start von Claude Code.

Von Hand: `/plugin` eingeben, unter „Installed“ den Weisen wählen, „Update now“, danach eine neue Sitzung starten. In der Desktop-App finden Sie Ihre Plugins außerdem über das Plus-Zeichen (+) unter „Plugins“.

Ist nach einem Update die Technik älter als das Plugin, sagt der Weise das in einem Satz. Rufen Sie dann einmal `/weise:einrichten` auf.

Was sich geändert hat, steht im [CHANGELOG](CHANGELOG.md).

## Deinstallation

```
/plugin uninstall weise@jason-lau-christen
/plugin marketplace remove jason-lau-christen
```

Wissenspakete sind eigene Plugins und bleiben dabei installiert. Entfernen mit `/plugin uninstall <paket>@<katalog>`; die eingespielten Themen bleiben im Themenordner.

**Ihre Daten bleiben dabei erhalten.** Lernthemen, Profil und Technik liegen in `%USERPROFILE%\weise` (bzw. in Ihrem gewählten Themenordner), und dort löscht Claude Code nichts. Wenn Sie alles entfernen möchten:

1. Lernthemen sichern, falls Sie sie behalten wollen.
2. Den Ordner `%USERPROFILE%\weise` löschen (und einen eigenen Themenordner, falls Sie einen gewählt haben).
3. Nur bei VOLL: Python 3.12 über die Windows-Einstellungen unter „Apps“ entfernen, falls die Einrichtung es installiert hat und Sie es sonst nicht nutzen.
4. Falls Sie beim Einrichten der Freigabe zugestimmt haben: die Einträge des Weisen unter `additionalDirectories` in `%USERPROFILE%\.claude\settings.json` entfernen.

## Hilfe und Vorschläge

- **Wenn etwas klemmt:** [docs/hilfe.md](docs/hilfe.md) listet die bekannten Fehlerbilder. `/weise:einrichten` zeigt jederzeit Ihr Profil und prüft die Technik.
- **Vorschläge und Fehler:** mit `/weise:vorschlag` oder direkt als [Issue](https://github.com/JasonDavid77/der-weise/issues). Für ein Issue brauchen Sie ein kostenloses GitHub-Konto. Der Weise legt jeden Vorschlag zusätzlich unter `%USERPROFILE%\weise\vorschlaege\` ab; dort bleibt er gespeichert, mit dem Stand (gespeichert, im Browser geöffnet oder eingereicht mit Link).
- **Ohne GitHub-Konto:** Schicken Sie die gespeicherte Datei über [LinkedIn](https://www.linkedin.com/in/jason-lau-christen-81bbb3240).
- **Mitarbeit:** Pull Requests bitte erst nach Absprache in einem Issue.
- **Sicherheitslücken** bitte nicht als Issue melden, sondern wie in [SECURITY.md](SECURITY.md) beschrieben.

## Lizenz

[MIT](LICENSE), Copyright (c) 2026 Jason Lau-Christen.
