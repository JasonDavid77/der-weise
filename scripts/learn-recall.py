"""
learn-recall.py -- Abfrage-Karten je Lernthema mit echter Vergessenskurve (FSRS).

Die Karten liegen als Datei in <werkraum>/<thema>/recall-cards.json (wird nie
in den Speicher gelegt). Der Weise holt beim Sitzungsstart die faelligen Karten
(--due) und meldet nach jeder Antwort die Bewertung zurueck (--review).

Aufruf (PowerShell):
  & "<WEISE_HOME>\\venv\\Scripts\\python.exe" "<WEISE_HOME>\\scripts\\learn-recall.py" --thema <name> --due
  ... learn-recall.py --thema <name> --add "Frage ..."
  ... learn-recall.py --thema <name> --review <id> --rating good
  ... learn-recall.py --thema <name> --list

Bewertungen: again (vergessen) | hard (schwer) | good (sass) | easy (locker)
"sitzt" im learner-state = Abrufwahrscheinlichkeit R > 0.9 UND Stabilitaet S >= 7 Tage.
"""

import os
import sys
import json
import tempfile
import argparse
from pathlib import Path
from datetime import datetime, timezone

import weise_config as cfg

try:
    from fsrs import Scheduler, Card, Rating
except ImportError:
    raise SystemExit("[fehler] Paket fsrs fehlt -- Installation wiederholen (/weise:einrichten).")

RATINGS = {"again": Rating.Again, "hard": Rating.Hard,
           "good": Rating.Good, "easy": Rating.Easy}


def cards_path(thema: str) -> Path:
    return cfg.werkraum() / thema / "recall-cards.json"


def load(thema: str) -> list:
    p = cards_path(thema)
    return json.loads(p.read_text(encoding="utf-8-sig")) if p.is_file() else []


def save(thema: str, items: list) -> None:
    """Atomar: ein Absturz kann die Karten nie halb geschrieben hinterlassen."""
    p = cards_path(thema)
    fd, tmp = tempfile.mkstemp(dir=str(p.parent), suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(items, f, ensure_ascii=False, indent=1)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, str(p))
    finally:
        if os.path.exists(tmp):
            try:
                os.remove(tmp)
            except OSError:
                pass


def fmt(card: Card, scheduler: Scheduler) -> str:
    r = scheduler.get_card_retrievability(card)
    stab = card.stability if card.stability is not None else 0.0
    return f"R={float(r):.2f} S={stab:.1f}d faellig={card.due.strftime('%Y-%m-%d')}"


def main() -> int:
    parser = argparse.ArgumentParser(description="Abfrage-Karten (FSRS) je Lernthema")
    parser.add_argument("--thema", required=True)
    parser.add_argument("--due", action="store_true", help="faellige Karten zeigen")
    parser.add_argument("--list", action="store_true", help="alle Karten zeigen")
    parser.add_argument("--add", type=str, help="neue Karte (Frage)")
    parser.add_argument("--review", type=int, help="Karten-Nummer bewerten")
    parser.add_argument("--rating", choices=list(RATINGS), help="Bewertung zu --review")
    args = parser.parse_args()

    if not (cfg.werkraum() / args.thema).is_dir():
        print(f"[fehler] Thema nicht gefunden: {cfg.werkraum() / args.thema}")
        return 1

    scheduler = Scheduler()   # FSRS-Standardwerte, Ziel-Abrufquote 0.9
    items = load(args.thema)

    if args.add:
        new_id = max((it["id"] for it in items), default=0) + 1
        items.append({"id": new_id, "question": args.add.strip(),
                      "card": Card().to_dict(), "history": []})
        save(args.thema, items)
        print(f"Karte #{new_id} angelegt (sofort faellig): {args.add.strip()[:80]}")
        return 0

    if args.review is not None:
        if not args.rating:
            print("[fehler] --review braucht --rating again|hard|good|easy")
            return 1
        for it in items:
            if it["id"] == args.review:
                card, _log = scheduler.review_card(Card.from_dict(it["card"]), RATINGS[args.rating])
                it["card"] = card.to_dict()
                it["history"].append({"date": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M"),
                                      "rating": args.rating})
                save(args.thema, items)
                print(f"Karte #{it['id']} bewertet ({args.rating}): {fmt(card, scheduler)}")
                return 0
        print(f"[fehler] Karte #{args.review} nicht gefunden")
        return 1

    if args.due or args.list:
        now = datetime.now(timezone.utc)
        shown = 0
        for it in items:
            card = Card.from_dict(it["card"])
            if args.due and card.due > now:
                continue
            tag = "FAELLIG" if card.due <= now else "ok     "
            print(f"  {tag} #{it['id']:>2} | {fmt(card, scheduler)} | {it['question'][:90]}")
            shown += 1
        if shown == 0:
            print("  Keine faelligen Karten." if args.due else "  Keine Karten vorhanden.")
        return 0

    parser.error("eine Aktion angeben: --due | --list | --add | --review")
    return 1


if __name__ == "__main__":
    sys.exit(main())
