#!/usr/bin/env python3
"""Validate the {curly} SDG keywords in a drafted sentence against the INTI list.

Catches the failure mode that matters: a keyword that looks plausible but is not
actually on INTI's list, which would fail their check.

Usage:
    python3 check_sdg.py "Reducing feed cost supports {food security} ..."
    python3 check_sdg.py draft_sentence.txt
    python3 check_sdg.py manuscript.docx          # scans every paragraph
    python3 check_sdg.py --min-goals 2 "..."      # require 2 distinct goals

Exit codes: 0 all keywords valid, 1 unknown keyword found, 2 nothing to check.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

DEFAULT_JSON = Path(__file__).resolve().parent.parent / "resources" / "sdg_keywords.json"

# Matches {anything} that is not itself a brace -- our keywords never nest.
KEYWORD_RE = re.compile(r"\{([^{}]+)\}")


def load_terms(json_path: Path) -> dict[str, tuple[int, str]]:
    """Map normalised keyword -> (goal number, canonical spelling)."""
    if not json_path.is_file():
        sys.exit(f"Keyword data not found: {json_path}\nRun extract_sdg.py first.")
    data = json.loads(json_path.read_text(encoding="utf-8"))
    table: dict[str, tuple[int, str]] = {}
    for goal in data["goals"]:
        for term in goal["terms"]:
            table[norm(term)] = (goal["number"], term)
    return table


def norm(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def resolve(keyword: str, table: dict[str, tuple[int, str]]) -> tuple[str, object]:
    """Look up a keyword. Returns (status, detail).

    status is one of: exact | case | wildcard | not_found
    """
    raw = keyword.strip()
    key = norm(raw)
    if key in table:
        return "exact", table[key]

    # Case-insensitive rescue (e.g. 'Food Security' for 'food security').
    for stored, (number, canonical) in table.items():
        if stored == key:
            return "case", (number, canonical)

    # INTI stem markers: 'coast*' should also match 'coastal management'.
    bare = key.rstrip("*").strip()
    if bare and len(bare) >= 4:
        hits = {stored: val for stored, val in table.items() if stored.startswith(bare)}
        if len(hits) == 1:
            return "wildcard", next(iter(hits.values()))
        if hits:
            return "ambiguous", sorted(hits)

    return "not_found", None


def extract_text(source: str) -> str:
    """Return file contents if `source` names a readable file, else treat it as literal text.

    Guards against OSError: a long sentence passed on the command line is not a
    valid filename, and must fall through to being treated as text.
    """
    try:
        path = Path(source)
        if not path.is_file():
            return source
        if path.suffix.lower() == ".docx":
            try:
                import docx  # type: ignore
            except ImportError:
                sys.exit("python-docx is required to read .docx:  pip install python-docx")
            document = docx.Document(str(path))
            return "\n".join(p.text for p in document.paragraphs)
        return path.read_text(encoding="utf-8", errors="replace")
    except (OSError, ValueError):
        return source


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("source", help="sentence text, a .txt file, or a .docx to scan")
    parser.add_argument("--keywords-json", default=str(DEFAULT_JSON))
    parser.add_argument("--min-goals", type=int, default=0, help="fail unless this many distinct goals are cited")
    args = parser.parse_args()

    table = load_terms(Path(args.keywords_json))
    text = extract_text(args.source)
    found = KEYWORD_RE.findall(text)

    if not found:
        print("No {curly} keywords found in the input.")
        print("INTI keywords must be written inside curly braces, e.g. {food security}.")
        sys.exit(2)

    goals_hit: dict[int, list[str]] = {}
    problems: list[str] = []
    notes: list[str] = []

    for raw in found:
        status, detail = resolve(raw, table)
        if status == "exact":
            number, canonical = detail  # type: ignore[misc]
            goals_hit.setdefault(number, []).append(canonical)
        elif status == "case":
            number, canonical = detail  # type: ignore[misc]
            goals_hit.setdefault(number, []).append(canonical)
            notes.append(f"  case/wording fixed: '{raw}' -> '{canonical}'")
        elif status == "wildcard":
            number, canonical = detail  # type: ignore[misc]
            goals_hit.setdefault(number, []).append(canonical)
            notes.append(f"  stem-matched: '{raw}' -> '{canonical}'")
        elif status == "ambiguous":
            notes.append(f"  ambiguous, not an exact list entry: '{raw}'")
            problems.append(f"'{raw}' is not a literal INTI keyword (it may expand to several)")
        else:
            problems.append(f"'{raw}' is NOT on the INTI list")

    print(f"Checked {len(found)} keyword(s) against the INTI list.\n")
    for number in sorted(goals_hit):
        unique = sorted(set(goals_hit[number]))
        print(f"  SDG {number:<2} {len(unique)} keyword(s): {', '.join('{' + k + '}' for k in unique)}")

    if notes:
        print("\nNotes:")
        for note in notes:
            print(note)

    if problems:
        print("\nPROBLEMS:")
        for problem in sorted(set(problems)):
            print(f"  ! {problem}")
        print("\nFix each keyword so it matches resources/sdg_keywords.md exactly.")
        sys.exit(1)

    if args.min_goals and len(goals_hit) < args.min_goals:
        print(f"\nFAIL: only {len(goals_hit)} distinct goal(s) cited, need {args.min_goals}.")
        sys.exit(1)

    print(f"\nOK - {len(found)} keyword(s) valid across {len(goals_hit)} goal(s).")


if __name__ == "__main__":
    main()