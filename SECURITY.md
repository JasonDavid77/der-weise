# Sicherheit

[English below](#security-policy)

## Unterstützte Versionen

Korrekturen gibt es nur für die jeweils neueste Version. Aktualisieren Sie deshalb zuerst, bevor Sie etwas melden.

## Eine Sicherheitslücke melden

Bitte nicht als öffentliches Issue und nicht über `/weise:vorschlag`, denn beides ist öffentlich.

Melden Sie sie vertraulich über GitHub: im Repository den Reiter „Security“ öffnen und „Report a vulnerability“ wählen, oder direkt [hier](https://github.com/JasonDavid77/der-weise/security/advisories/new). Die Meldung sehen nur Sie und der Betreuer des Projekts.

## Was dazu zählt

Zum Beispiel:

- Der Weise liest, schreibt, lädt oder sendet etwas, das die README im Abschnitt „Was der Weise auf Ihrem Rechner tut“ nicht nennt.
- Die Einrichtung lädt aus einer anderen Quelle als python.org, pypi.org oder huggingface.co, oder sie umgeht eine Sperre des Rechners.
- Der Weise befolgt Anweisungen, die in fremden Inhalten stehen (Webseiten, Dateien, Issue-Texte, Treffer aus dem Speicher).
- `/weise:vorschlag` lässt Namen, Pfade oder vertrauliche Angaben im Text, der veröffentlicht werden soll.

## Was Sie mitschicken

- Version (steht in `.claude-plugin/plugin.json`), Betriebsart (VOLL oder OHNE PYTHON) und Betriebssystem.
- Die Schritte, mit denen sich das Problem zeigt, und was Sie beobachtet haben.
- Keine vertraulichen Inhalte, keine Passwörter oder Schlüssel.

Das Projekt wird von einer Person gepflegt. Sie erhalten eine Rückmeldung, sobald die Meldung geprüft ist.

---

## Security policy

**Supported versions:** only the latest version receives fixes. Please update before reporting.

**Reporting a vulnerability:** please don't use a public issue or `/weise:vorschlag`, both are public. Report it privately on GitHub: open the "Security" tab of this repository and choose "Report a vulnerability", or go [here](https://github.com/JasonDavid77/der-weise/security/advisories/new). Only you and the maintainer can see the report.

**In scope,** for example: Der Weise reads, writes, downloads or sends anything the README does not disclose; setup downloads from a source other than python.org, pypi.org or huggingface.co, or works around a block on the computer; Der Weise follows instructions found in untrusted content (web pages, files, issue texts, search hits); `/weise:vorschlag` leaves names, paths or confidential details in text meant for publication.

**Please include** the version (from `.claude-plugin/plugin.json`), the mode (VOLL or OHNE PYTHON), your operating system, the steps to reproduce and what you observed. Do not include confidential content, passwords or keys.

This project is maintained by one person. You will get a reply once the report has been reviewed.
