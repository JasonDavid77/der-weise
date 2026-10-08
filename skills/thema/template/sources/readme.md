# sources/ -- Kuratiertes Rohmaterial

Finale Texte, Mitschriften, Berichte -- die Quelle der Wahrheit des Themas. Nur
der Weise legt hier ab (aus eingang/ oder der eigenen Suche kuratiert, sauber benannt, mit Datum vorne:
`YYYY-MM-DD-<slug>.md`; Ergebnisse eines Recherche-Auftrags mit dessen Nummer:
`YYYY-MM-DD-r<n>-<slug>.md`). Jede Datei = Zeile im Doc-Index der `../_index.md` (ein Wissenspaket
unter `paket/` = eine Zeile; diesen Ordner aendert nur `/weise:paket`).

**Nach jeder Aenderung hier (nur mit Python):** `learn-store.py --thema <name>` ausfuehren, sonst
fehlt das Neue in der Suche. Ohne Python findet die Stichwortsuche neue Dateien sofort. Nur .md/.txt werden durchsucht -- PDFs, Word-Dateien
und Mitschnitte erst in Text ueberfuehren. Ueberholtes kommt nach `_archive/`
(wird nicht gespeichert).
