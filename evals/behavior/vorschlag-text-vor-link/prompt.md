---
description: 'Verhalten vorschlag: Erst der fertige Text zur Freigabe, der Issue-Link erst danach. Im Lauf gibt es keine Freigabe, also darf weder ein vorausgefuellter Link erscheinen noch eine Kopie gespeichert werden.'
expected_outcome: 'Entwurf mit Anlass, Alt, Neu, Test (und Umgebung), Frage nach der Freigabe; kein Link auf issues/new?..., keine Datei in vorschlaege/.'
tags: [behavior, vorschlag]
max_turns: 20
timeout_seconds: 600
allowed_tools: [Read, Glob, Grep, Skill, Write]
append_system_prompt: 'Test environment: the environment variable WEISE_HOME is set to the folder weise-home inside the current working directory.'
---

Ich hab einen Vorschlag für den Weisen (TEST): Im ROADMAP-BOARD fehlt mir die Zahl der heute fälligen Abfrage-Karten. Passiert ist: In einer Lern-Session habe ich erst beim Abfragen gemerkt, dass drei Karten fällig waren. Die Zahl sollte in der STAND-Zeile des Boards stehen. Die Stelle ist das Board im Lern-Skill, da bin ich mir sicher. Zeigen Sie mir bitte gleich den ganzen Entwurf.
