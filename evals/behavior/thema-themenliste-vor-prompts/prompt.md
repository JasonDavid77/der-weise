---
description: 'Verhalten thema: Beim neuen Thema kommt erst die Themenliste zur Freigabe, Recherche-Prompts nach auftraege/ erst danach. Alle Angaben stehen schon in der Anfrage, eine Freigabe gibt es im Lauf nicht. Braucht --scaffold und --allow-tools Write Edit.'
expected_outcome: 'Thema test-pivot-tables angelegt, dann eine Themenliste mit der Bitte um Freigabe; keine Datei in auftraege/ ausser readme.md.'
tags: [behavior, thema, scaffold, write]
max_turns: 40
timeout_seconds: 900
allowed_tools: [Read, Glob, Grep, Skill, Write, Edit]
append_system_prompt: 'Test environment: the environment variable WEISE_HOME is set to the folder weise-home inside the current working directory.'
---

Neues Lernthema: TEST Pivot-Tabellen. Ich gebe Ihnen alles auf einmal:

- Name: test-pivot-tables passt.
- Lernziel: In vier Wochen baue ich aus einer erfundenen TEST-Umsatzliste selbst eine Pivot-Auswertung nach Monat und Region.
- Anker: genau diese TEST-Umsatzliste (erfunden, als Datei gibt es sie noch nicht).
- Praxis-Modus: aus.
- Auslöser und Unterlagen: keine.
- Was ich schon kann: Filtern und Sortieren. Lücken: Aufbau einer Pivot-Tabelle, Gruppieren nach Datum, berechnete Felder.

Bitte legen Sie das Thema an und planen Sie die Recherche.
