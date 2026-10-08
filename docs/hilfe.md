# Hilfe: wenn etwas klemmt

Diese Seite sammelt die bekannten Fehlerbilder, für beide Betriebsarten: **VOLL** (mit Python und Speicher) und **Stichwortsuche** (im Board: OHNE PYTHON).

Pfade: `%USERPROFILE%\weise` ist der Technik-Ordner. Haben Sie die Umgebungsvariable `WEISE_HOME` gesetzt, gilt stattdessen deren Ordner.

## Zuerst: Einrichtung prüfen

Rufen Sie `/weise:einrichten` auf. Der Weise zeigt Ihr Profil und die Betriebsart. Bei VOLL lässt er außerdem den Selbsttest laufen und zeigt dessen Ausgabe wörtlich. Am Ende steht „Selbsttest bestanden“ oder eine Liste mit OK, HINWEIS und FEHLER.

Grundregel bei jedem Fehler: **Nichts umgehen.** Stoppt ein Schutzprogramm oder eine Richtlinie Ihrer IT etwas, bleibt der Weise bei der Stichwortsuche. Alles Didaktische funktioniert dort genauso.

## Fehlerbilder

### Installation, Katalog und Start (beide Betriebsarten)

| Sie sehen … | Wahrscheinliche Ursache | Was Sie tun |
|---|---|---|
| Der Katalog lässt sich nicht hinzufügen, Meldung mit „git“ | Git fehlt auf dem Rechner | In PowerShell `git --version` prüfen. Fehlt Git: von [git-scm.com](https://git-scm.com) installieren oder die IT fragen. Ein GitHub-Konto ist nicht nötig. |
| `/plugin` meldet „isn't available in this environment“ | Der Befehl öffnet ein Menü, das diese Umgebung nicht zeigt | Die Form mit Angaben nutzen: `/plugin install weise --marketplace JasonDavid77/claude-plugins` |
| Die Befehle `/weise:…` erscheinen nicht | Die Sitzung lief schon vor der Installation | Neue Sitzung starten oder `/reload-plugins` eingeben |
| Der Weise erscheint doppelt, oder es gibt zusätzlich Skills „weise“ oder „learn“ | Ältere Kopien liegen unter `%USERPROFILE%\.claude\skills` | `/weise:einrichten` aufrufen; es verschiebt die alten Kopien nach Ihrer Zustimmung in die Sicherung. Danach neue Sitzung. |
| Der Weise weist auf `/weise:einrichten` hin | Profil `config.json` fehlt noch oder ist unvollständig | `/weise:einrichten` aufrufen. Bis dahin arbeitet der Weise mit Standardwerten. |
| „Die Technik ist älter als das Plugin“ | Das Plugin wurde aktualisiert, die Technik noch nicht | Einmal `/weise:einrichten` aufrufen |
| Rückfragen bei jedem Lesen im Themenordner | Der Themenordner liegt außerhalb Ihres Arbeitsordners | In `/weise:einrichten` die angebotene Freigabe annehmen; sie wirkt ab der nächsten Sitzung |
| Das Board zeigt „OHNE PYTHON“, obwohl VOLL eingerichtet ist | Die Python-Umgebung fehlt unter `%USERPROFILE%\weise\venv`, oder `WEISE_HOME` zeigt woandershin | `/weise:einrichten` aufrufen |
| Ein Skript meldet mitten in der Sitzung einen Fehler | Speicher, Modell oder Paket nicht in Ordnung | Der Weise zeigt die Meldung wörtlich und macht für diese Sitzung mit der Stichwortsuche weiter. Danach `/weise:einrichten` aufrufen. |

### Wissenspakete (`/weise:paket`)

| Sie sehen … | Wahrscheinliche Ursache | Was Sie tun |
|---|---|---|
| „Kein Wissenspaket gefunden“ | Das Paket ist nicht installiert, oder die Sitzung lief schon vor der Installation | Paket über seinen Katalog installieren, neue Sitzung. Liegt das Paket als Ordner vor: `/weise:paket <ordner>` |
| Ein privater Katalog lässt sich nicht hinzufügen („Repository not found“, Anmeldefehler) | Claude Code kann beim Laden nicht nach der Anmeldung fragen, oder Git hat eine alte Anmeldung gespeichert | Das Repo einmal selbst klonen (`git clone <url>`); Git fragt dann nach der Anmeldung und speichert sie. Ist eine alte Anmeldung gespeichert, diese vorher in der Windows-Anmeldeinformationsverwaltung entfernen. Danach den Katalog erneut hinzufügen, oder `/weise:paket <klon-ordner>` |
| „abweichend“ oder „fehlt“ bei der Prüfung | Datei beschädigt, unvollständig geladen oder verändert | Nichts kopieren lassen. Paket neu installieren bzw. den Klon neu holen, dann wieder `/weise:paket` |
| „fehlt“ bei vielen Dateien mit langen Namen, obwohl sie da sind | Der Pfad ist länger als 260 Zeichen, das liest Windows PowerShell nicht | Einen kürzeren Themenordner wählen (`/weise:einrichten`) oder den Klon in einen kürzeren Ordner legen |
| Fast alle Dateien „abweichend“, gleich nach Installation oder Klon | Git hat beim Herunterladen die Zeilenenden umgestellt; dem Paket-Repo fehlt die Datei `.gitattributes` mit `* -text` | Den Herausgeber des Pakets darauf hinweisen (Format: [wissenspaket.md](wissenspaket.md)). Nichts umstellen lassen, bis das Paket korrigiert ist |
| „Den Themenordner gibt es schon“ | Ein Thema mit diesem Namen liegt im Themenordner, ohne dieses Paket | Der Weise überschreibt nichts. Wählen Sie einen anderen Namen oder spielen Sie das Paket in das bestehende Thema ein (nur wenn dort noch kein anderes Paket liegt) |
| „Kein reines Wissenspaket“ | Das Paket bringt Befehle, Hooks oder einen Server mit | Der Weise spielt nur Daten ein. Prüfen Sie, woher das Paket stammt |

### Vorschläge (`/weise:vorschlag`)

| Sie sehen … | Wahrscheinliche Ursache | Was Sie tun |
|---|---|---|
| Der Weise bietet „Direkt senden“ nicht an | Die GitHub-Kommandozeile `gh` fehlt oder ist bei github.com nicht angemeldet | Den Weg über den Browser nehmen. Der Weise richtet keine Anmeldung ein |
| Das direkte Senden scheitert (403, SSO, Zeitüberschreitung) | Das angemeldete Konto darf dort kein Issue anlegen, oder die Verbindung brach ab | Der Weise zeigt die Meldung, prüft, ob das Issue trotzdem angelegt wurde, und bietet sonst den Browser an |
| Als Konto wird ein Firmenkonto genannt | `gh` ist mit dem Arbeitskonto angemeldet | „Im Browser senden“ wählen und dort mit dem gewünschten Konto absenden |

### Einrichtung VOLL (Windows)

| Sie sehen … | Wahrscheinliche Ursache | Was Sie tun |
|---|---|---|
| „Die Ausführung von Skripts ist auf diesem System deaktiviert“ | Richtlinie des Rechners | Der Weise startet die Einrichtung nur für diesen einen Aufruf mit einer Ausnahme. Erscheint die Meldung trotzdem, gilt eine Richtlinie Ihrer IT: nichts umgehen, bei der Stichwortsuche bleiben, die IT fragen. |
| „Der Technik-Ordner liegt zu tief“ oder pip: `No such file or directory` mit Hinweis auf „Long Path“ | Windows begrenzt Pfade auf 260 Zeichen | Einen kürzeren Technik-Ordner wählen: Umgebungsvariable `WEISE_HOME` für Ihr Konto setzen (zum Beispiel `C:\weise`), neue Sitzung, dann `/weise:einrichten` |
| winget-Fehler, danach Download von python.org | winget fehlt oder ist gesperrt | Nichts, die Einrichtung nimmt den zweiten Weg |
| „Python-Installer endete mit Code …“, „darf nicht starten“ oder „winget meldet Erfolg, aber Python fehlt“ | Ein Schutzprogramm oder eine Richtlinie blockiert die Installation | Nichts umgehen. Der Weise arbeitet mit der Stichwortsuche. Die Freigabe von Python bei der IT anfragen. |
| `SSL: CERTIFICATE_VERIFY_FAILED` bei pip | Die Firewall prüft verschlüsselte Verbindungen | Nichts umgehen. Die Meldung wörtlich an Ihre IT geben, bis dahin Stichwortsuche. |
| `ProxyError` oder Zeitüberschreitung bei pip | Proxy oder Verbindung bricht große Downloads ab | `/weise:einrichten` erneut aufrufen, die Einrichtung setzt fort. Bleibt es, die IT fragen. |
| Der Modell-Download scheitert (huggingface.co) | Der Download-Server ist gesperrt | Die IT um Freigabe von huggingface.co bitten. Oder den Ordner `modelle` von einem Rechner kopieren, auf dem die Einrichtung durchlief, nach `%USERPROFILE%\weise\modelle\`. |
| Eine Datei wird vom Virenschutz zurückgehalten | Schutzprogramm des Rechners | Nichts umgehen. Die Meldung wörtlich an Ihre IT geben. |

### Meldungen des Selbsttests und der Skripte (VOLL)

| Sie sehen … | Wahrscheinliche Ursache | Was Sie tun |
|---|---|---|
| „Sprachmodell fehlt“ | Der Modell-Download lief nicht durch | `/weise:einrichten` erneut aufrufen; geladen wird nur, was fehlt |
| „Paket … fehlt“ | Die Paket-Installation ist unvollständig | `/weise:einrichten` erneut aufrufen |
| „Werkraum … bzw. config.json fehlt noch“ | Die Einrichtung ist noch nicht abgeschlossen | `/weise:einrichten` aufrufen |
| „Speicher nicht beschreibbar“ | Der Ordner ist gesperrt oder wird synchronisiert | Technik-Ordner und Themenordner nicht in OneDrive oder einen anderen synchronisierten Ordner legen; Schreibrechte prüfen |
| „Der Speicher ist noch leer“ | Das Thema wurde noch nicht gespeichert | Den Weisen bitten, das Thema zu speichern (`learn-store.py --thema <name>`) |
| „You are sending unauthenticated requests to the HF Hub“ | Hinweis beim Modell-Download | Harmlos: Das Modell ist frei und braucht keinen Schlüssel |

## Von Hand prüfen

**VOLL**, in PowerShell:

```
& "$env:USERPROFILE\weise\venv\Scripts\python.exe" --version
& "$env:USERPROFILE\weise\venv\Scripts\python.exe" -m pip check
& "$env:USERPROFILE\weise\venv\Scripts\python.exe" "$env:USERPROFILE\weise\scripts\self-check.py"
```

Erwartet: `Python 3.12.x`, dann „No broken requirements found.“, dann „Selbsttest bestanden“. Der Selbsttest arbeitet in einem Wegwerf-Ordner; Ihre Themen und Ihr Speicher bleiben unberührt.

**Stichwortsuche:** Es genügt, dass `%USERPROFILE%\weise\config.json` lesbar ist und der Themenordner mit `_themen.md` existiert.

## Neues Fehlerbild?

Melden Sie es mit `/weise:vorschlag` und geben Sie die Meldung wörtlich an. Der Weise entfernt vor dem Absenden Namen, Pfade und vertrauliche Angaben und zeigt Ihnen den Text zur Freigabe. Sicherheitslücken bitte nach [SECURITY.md](../SECURITY.md) melden, nicht als Issue.
