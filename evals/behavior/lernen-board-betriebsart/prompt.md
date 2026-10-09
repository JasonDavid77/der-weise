---
description: 'Verhalten lernen: Am Sessionstart steht das ROADMAP-BOARD mit der Betriebsart. Der Test-Technik-Ordner hat kein venv, also muss dort OHNE PYTHON stehen, nicht VOLL. Braucht --scaffold.'
expected_outcome: 'Sessionkopf, danach das ROADMAP-BOARD (das Testthema ist aus der Zeit vor dem Projektpfad: LERNPFAD neben DELIVERABLE-SPUR) mit der Zeile "WISSEN: thema=test-statistics-basics, OHNE PYTHON (<n> Dateien)".'
tags: [behavior, lernen, scaffold]
max_turns: 30
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill]
append_system_prompt: 'Test environment: the environment variable WEISE_HOME is set to the folder weise-home inside the current working directory.'
---

Lern-Session bitte: test-statistics-basics. Machen wir da weiter, wo wir aufgehört haben.
