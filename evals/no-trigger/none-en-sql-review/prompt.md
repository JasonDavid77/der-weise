---
description: 'Kein Weise-Skill darf anspringen (en), allgemeine Code-Pruefung.'
tags: [no-trigger, none, en]
max_turns: 15
allowed_tools: [Read, Glob, Grep, Skill]
append_system_prompt: 'Test environment: the environment variable WEISE_HOME is set to the folder weise-home inside the current working directory.'
---

Review this SQL query for performance: SELECT * FROM orders WHERE YEAR(created_at) = 2025;
