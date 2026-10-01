# Evidence -- Fundament des Weisen (v2-Kern, v3-Ergaenzungen unten)

> Warum der Skill so gebaut ist. Pro Prinzip: Kern -- Beleg -- Umsetzung im Skill.
> Substanz (Stand 2026-06-14). Aenderungen am Modell -> hier nachziehen.

## Lern-Mechanik (das Geruest)

- **Expertise-Reversal-Effekt** -- Fuehrung, die fuer Anfaenger hilft, schadet Fortgeschrittenen (und umgekehrt); Stuetze muss mit Koennen sinken. *(Kalyuga 2003; Kalyuga 2007)* -> **Fading laeuft ueber die ANWENDUNG (Stufe 2->4), NICHT ueber die Erklaer-Tiefe.** Stufe pro Konzept am learner-state-Stand kalibriert.
- **Worked-Example-Effekt** -- ein durchgerechnetes Beispiel schlaegt fruehes Selbstloesen, solange Schema fehlt. *(Sweller 1985ff; Sweller/van Merrienboer/Paas 1998)* -> Stufe 1: EIN worked example laut vorgedacht, am Build verankert, vor jeder eigenen Aufgabe.
- **Minimal-Guidance scheitert** -- entdeckendes/ungefuehrtes Lernen ist fuer Neulinge unterlegen; Anfaenger brauchen explizite Fuehrung. *(Kirschner/Sweller/Clark 2006)* -> Erklaeren startet IMMER bei Null; kein "lass ihn selbst draufkommen" am Anfang einer Etappe.
- **Guidance-Fading via Completion** -- Worked Example -> Completion-Problem (Luecken) -> freie Aufgabe ist der saubere Uebergang. *(Renkl/Atkinson 2000; Renkl/Atkinson 2003)* -> Stufe 2 = EINE Luecke, Stufe 3 = mehr Luecken, Stufe 4 = frei am Zielobjekt.

## Tutoring-Interaktion (der Takt)

- **Kontingentes Scaffolding** -- Hilfe steigt bei Stocken, sinkt bei Erfolg; nie stecken lassen. *(Wood/Bruner/Ross 1976)* -> **Kontingenz-Notbremse: bei Fehler EINE Stufe ZURUECK zu mehr Fuehrung, nie "haerter fragen".**
- **EMT-Eskalationsleiter** -- Expectation-Misconception-Tailored: Pump -> Hint -> Prompt -> Assertion. *(Graesser, AutoTutor; Nye/Graesser/Hu 2014)* -> exakte Leiter der Notbremse; Assertion (Weise loest selbst) ist letzter Schritt, nicht erster.
- **5-Schritt-Tutoring-Frame** -- Frage -> Antwort -> kurzes Feedback -> gemeinsam ausbauen -> Verstaendnis pruefen. *(Graesser & Person 1994)* -> Frame jeder iterativen Schleife; Schleifen werfen NIE aus der Etappe.
- **Productive Failure** -- erst probieren (auch scheitern), dann Instruktion; wirkt nur MIT Vorbedingungen, Effekt moderat. *(Kapur 2008ff; Sinha & Kapur 2021, d=0.36)* -> Mikrodosis NUR ab Stand "wackelig", mit zwingender Aufloesung; Default bleibt erklaeren-zuerst.

## Architektur (Lernen + Bauen = eine Bewegung)

- **Backward Design** -- vom Ziel-Deliverable rueckwaerts planen, jedes Konzept zahlt auf ein Koennen ein. *(Wiggins & McTighe 2005)* -> Deliverable aus `_index.md`-Lernziel + `concepts.md` abgeleitet (K -> Baustein); mit dem Lern-Anker zu EINEM Konzept verschmolzen.
- **4C/ID Whole-Task** -- ganze, sinnvolle Aufgaben statt isolierter Teilfertigkeiten; Komplexitaet wachsen lassen. *(van Merrienboer 1997; van Merrienboer/Kirschner 2018)* -> Roadmap-Board mit Deliverable-Spur; Boss-Fight (Stufe 4) = haertester realistischer Gegenspieler am echten Zielobjekt.

## Grenzen / Gegencheck

- **Nicht ueberkorrigieren:** Von Null erklaeren bleibt OK -- kurz, am Build verankert, relevant; Fading kommt aus der Anwendung, nicht aus duenner Erklaerung *(Design-Entscheidung 2026-06-14, vereinbar mit Expertise-Reversal)*.
- **Retrieval/Spacing** ist FSRS-Sache (learn-recall); der Weise erfindet kein eigenes Wiederhol-System und setzt "sitzt" nie nach Gefuehl. Einzige Ausnahme (v3.1): Kann FSRS nicht laufen (kein Python), gilt die Faecher-Regel nach Leitner als festgelegter Ersatz *(Leitner 1972, "So lernt man lernen": Karteikasten mit wachsenden Abstaenden)*.
- **LLM-Failure-Modes:** Gegen Sycophancy -- falsche Lerner-Antworten NICHT bestaetigen. Gegen Halluzination -- in der Assertion-Stufe quellengebunden bleiben (Herkunfts-Zeile), nicht frei fabulieren.
- **Triage gegen Turn-Ermuedung:** Kern-Konzepte volle Kette (Stufe 0-5); Neben-Begriffe nur Kurzform (Sofort-Definition + 1 Beispiel).

---
Substanz-Mechaniken (FSRS/Recall, Container-Doktrin, Quellen-Treue, Curriculum) blieben unveraendert -- Integritaets-Inventar 2026-06-14.

## v3-Ergaenzungen (2026-09-28) -- aus der Nutzung gelernt

Anlass: Nutzungserfahrung mit zwei Werkzeug-Themen unter echtem Zeitdruck. Befund
damals: In beiden Themen kippten die Lern-Sessions in reine Bau-Sessions (in einem
Thema zwei Wochen ohne Lern-Eintrag, im anderen eine Woche ohne Recall), der
Lernpfad blieb stehen, waehrend das Projekt wuchs.

- **Just-in-time-Information im Ganzaufgaben-Lernen** -- prozedurale Information
  wirkt am besten genau in dem Moment, in dem sie bei der Aufgabe gebraucht wird;
  stuetzende Information davor. *(van Merrienboer & Kirschner, Ten Steps to Complex
  Learning, 2018)* -> **Tempo-Modus: Lernzeile an jedem Bauschritt** ("Warum so" +
  Quelle), statt das Lernen bis nach dem Bau aufzuschieben.
- **Testing- und Spacing-Effekt** -- Abruf wirkt auch (und oft besser) mit
  Verzoegerung; verteiltes Ueben schlaegt geballtes. *(Roediger & Karpicke 2006;
  Cepeda et al. 2006)* -> **Fragen-Parkplatz:** eine aufgeschobene Pruef-Frage
  verliert ihren Nutzen nicht; sie kommt in der naechsten Wartezeit oder als
  Abfrage-Karte in die naechste Session.
- **Segmentierung und Vorstrukturierung** -- Lernende profitieren, wenn komplexer
  Stoff in selbst getaktete Abschnitte zerlegt wird und ein Ueberblick vorab die
  Einordnung traegt. *(Mayer 2009, Segmenting Principle; Ausubel 1960, Advance
  Organizer)* -> **Werkzeug-Form:** ein Schritt auf einmal, Gesamtweg mit Marker
  ueber jedem Block.
- **Teilaufgaben-Uebung neben der Ganzaufgabe** -- wiederkehrende Fertigkeiten, die
  die Ganzaufgabe nicht abdeckt, werden gezielt gesondert geuebt. *(van Merrienboer
  & Kirschner 2018, Part-Task Practice)* -> **Uebung mit Ansage** fuer Konzepte,
  die das Projekt nicht braucht -- mit Praxisteil, und mit Grund angesagt.
- **Adaptive Aufgabenfolge** -- die Abfolge der Lernaufgaben wird laufend an
  Lernstand und Aufgabe angepasst, nicht einmal fest geplant. *(van Merrienboer &
  Kirschner 2018, dynamische Aufgabenauswahl)* -> **Projekt-Nachzug:** der
  Lernpfad waechst mit dem Projekt; Backward Design bleibt der Rahmen, der Anker
  darf sich entwickeln.
- **Veraltete Praemissen** (LLM- und Material-Failure-Mode, eigener Befund) --
  Karten, die einen ueberholten Stand abfragen, kalibrieren in die falsche
  Richtung; Karten ueber Fachstoff statt Werkzeug-Mechanik pruefen das Falsche.
  -> **Stand-Pruefung vor jedem Recall** (1c).
- **Uebungsfall passend zum Werkzeug** (eigener Befund) -- ein Fall, an dem das
  Werkzeug scheitert, lehrt nicht, wie es funktioniert; ein vorab verratener Befund
  nimmt den Lernmoment. -> Uebungsfall zeigt die Staerke, Grenze danach, Befund nie
  vorab (Stufe 3b).
