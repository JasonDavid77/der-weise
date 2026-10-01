"""
query.py -- im Speicher des Weisen suchen (semantische Suche).

Aufruf (PowerShell):
  & "<WEISE_HOME>\\venv\\Scripts\\python.exe" "<WEISE_HOME>\\scripts\\query.py" "<frage>" --thema <name>
  ... query.py "<frage>" --thema excel-*      # alle Themen, die mit excel- beginnen
  ... query.py "<frage>" --alle               # ganzer Bestand ("Weiser: almighty")
  ... query.py "<frage>" --thema <name> --n 8
"""

import argparse

import weise_config as cfg


def resolve_topics(spec: str):
    """'name' -> 'name'; 'praefix*' -> Liste aller Themen mit diesem Praefix."""
    if not spec.endswith("*"):
        return spec
    prefix = spec[:-1]
    root = cfg.werkraum()
    names = sorted(d.name for d in root.iterdir()
                   if d.is_dir() and d.name.startswith(prefix) and not d.name.startswith("_"))
    if not names:
        raise SystemExit(f"Kein Lernthema beginnt mit '{prefix}' in {root}")
    print(f"Praefix-Sicht '{prefix}*': {', '.join(names)}")
    return names


def main() -> None:
    parser = argparse.ArgumentParser(description="Im Speicher des Weisen suchen")
    parser.add_argument("frage")
    scope = parser.add_mutually_exclusive_group(required=True)
    scope.add_argument("--thema", help="Themen-Sicht (Name oder praefix*)")
    scope.add_argument("--alle", action="store_true", help="ganzer Bestand, ohne Filter")
    parser.add_argument("--n", type=int, default=5, choices=range(1, 51), metavar="N",
                        help="Anzahl Treffer, 1-50 (Standard 5)")
    args = parser.parse_args()

    client = cfg.client()
    try:
        col = client.get_collection(name=cfg.COLLECTION_NAME,
                                    embedding_function=cfg.embedding_function())
    except Exception:
        raise SystemExit("Der Speicher ist noch leer. Erst learn-store.py --thema <name> ausfuehren.")

    where, label = None, "ganzer Bestand"
    if args.thema:
        topics = resolve_topics(args.thema)
        where = {"thema": topics} if isinstance(topics, str) else {"thema": {"$in": topics}}
        label = f"thema={args.thema}"

    res = col.query(query_texts=[args.frage], n_results=args.n, where=where)
    docs, metas, dists = res["documents"][0], res["metadatas"][0], res["distances"][0]
    print(f'Frage: "{args.frage}"')
    print(f"Treffer: {len(docs)} ({label}, Speicher gesamt {col.count()} Abschnitte)\n")
    if not docs:
        print("Keine Treffer. Ist das Thema schon gespeichert (learn-store.py --thema <name>)?")
    for i, (doc, meta, dist) in enumerate(zip(docs, metas, dists), 1):
        stand = f" | Stand {meta['stand']}" if meta.get("stand") else ""
        print(f"--- Treffer {i} | Aehnlichkeit {1 - dist:.3f} | {meta.get('source_file', '?')}{stand} ---")
        print(doc)
        print()


if __name__ == "__main__":
    main()
