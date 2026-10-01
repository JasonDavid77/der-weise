# Befehle (nur VOLL)

Ausgelagert aus `../SKILL.md` (Abschnitt "Technik und Betriebsart"). Aufrufform und
Fehlerregel nach Datenregel 5 in `${CLAUDE_PLUGIN_ROOT}/references/daten.md`.
`${CLAUDE_PLUGIN_ROOT}` = Plugin-Ordner, also der Ordner ueber `skills/`, aus dem diese Datei
gelesen wurde (in dieser Datei setzt Claude Code den Pfad nicht selbst ein).

Befehle (nur VOLL; PowerShell; `<name>` = Ordnername des Themas; fuer
`<WEISE_HOME>` den echten Pfad nach Datenregel 1 einsetzen):

```
$w = "<WEISE_HOME>"; $py = "$w\venv\Scripts\python.exe"; $s = "$w\scripts"
& $py "$s\query.py" "<frage>" --thema <name>          # Themen-Sicht
& $py "$s\query.py" "<frage>" --alle                  # almighty
& $py "$s\learn-recall.py" --thema <name> --due       # faellige Karten
& $py "$s\learn-recall.py" --thema <name> --review <id> --rating again|hard|good|easy
& $py "$s\learn-recall.py" --thema <name> --add "<frage>"
& $py "$s\learn-store.py" --thema <name>              # Thema neu in den Speicher legen
& $py "$s\self-check.py"                              # Selbsttest, wenn etwas hakt
```

**Anfuehrungszeichen:** Windows PowerShell reicht gerade doppelte
Anfuehrungszeichen INNERHALB eines Arguments nicht sauber an Python weiter. In
Fragen und Karten fuer woertliche Oberflaechentexte deshalb typografische
Zeichen nutzen: `--add 'Wo steht „Neue Spalte“?'` -- nie `"` im Text.

Scheitert ein Skript: Meldung woertlich zeigen, `self-check.py` laufen lassen,
nicht raten, und fuer diese Session OHNE PYTHON weiterarbeiten. Ausnahme:
`query.py` meldet "Der Speicher ist noch leer" -- das ist kein Fehler, sondern
heisst: Thema erst speichern (STOP wie in `../SKILL.md` Abschnitt 0).
