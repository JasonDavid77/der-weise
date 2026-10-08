# Evals für den Weisen

Testsuite für `claude plugin eval` (Claude Code ab v2.1.269, Doku:
https://code.claude.com/docs/en/plugin-evals). Jeder Lauf ist ein echter Modellaufruf auf Ihrem Konto.

## Aufbau

| Ordner | Fälle | Prüft |
|---|---|---|
| `trigger/` | 18 | `lernen`, `thema` und `vorschlag` springen an: je Skill drei Sätze auf Deutsch, drei auf Englisch |
| `no-trigger/` | 10 | `einrichten` und `paket` springen nie von selbst an (je 2 Fälle); bei 6 fremden Anfragen springt kein Skill des Weisen an, darunter Beinahe-Treffer |
| `behavior/` | 3 | `lernen-board-betriebsart`: das Board zeigt die Betriebsart; `thema-themenliste-vor-prompts`: erst die Themenliste zur Freigabe, dann Recherche-Prompts; `vorschlag-text-vor-link`: erst der Text zur Freigabe, dann Link oder Senden (ohne Shell-Werkzeug nur der Weg über den Browser) |

Alle Themen und Vorschläge sind erfunden und tragen "TEST". Es gibt nur kostenlose Prüfer
(`regex`, `tool_used`), kein Richter-Modell.

## Testumgebung

Jeder Fall setzt per `append_system_prompt` `WEISE_HOME` auf den Ordner `weise-home` im
Arbeitsverzeichnis des Laufs; der echte Technik-Ordner bleibt unberührt. Die Fälle mit dem Tag
`scaffold` bauen dort mit `fixture.sh` (Bash, unter Windows Git Bash) ein Profil und einen
TEST-Werkraum. Ohne `venv` ist die erwartete Betriebsart OHNE PYTHON.

## Starten (im Plugin-Ordner)

```
claude plugin eval . --tag trigger no-trigger
claude plugin eval . --tag behavior --scaffold --allow-tools Write Edit
claude plugin eval . --scaffold --allow-tools Write Edit
claude plugin eval . --case lernen-board-betriebsart --scaffold --runs 1 --ablation none
```

- Ohne `--scaffold` fehlt der TEST-Werkraum; die Fälle mit dem Tag `scaffold` scheitern dann.
- Ohne `--allow-tools Write` legt `thema` nichts an, und die Prüfungen "keine Datei vor der
  Freigabe" bestehen ohne Aussage.
- `Bash` oder `PowerShell` nicht freigeben: Unter nativem Windows fehlt die Sandbox, solche Läufe
  werden abgewiesen.
- Umfang der ganzen Suite: 31 Fälle, je 3 Läufe mit und 3 ohne Plugin, also 186 Läufe. Mit
  `-j 4` laufen vier gleichzeitig.

## Ergebnisse lesen

- Auslösetests haben nur den Prüfer `tool_used: Skill`; ohne Plugin steht dort immer 0, `Δ` zeigt
  also die Auslöserate.
- `no-trigger/` prüft mit `min: 0`, `max: 0` und `arm: both`; dort ist `Δ` erwartungsgemäß 0.
- In `behavior/` ist `skill-fired` im Vergleich mit und ohne Plugin nur Anzeige; gezählt werden
  die übrigen Prüfer (mit `--ablation none` zählt er mit).
- Jeder Lauf schreibt nach `evals/results/`; der Ordner gehört nicht ins Repo.
