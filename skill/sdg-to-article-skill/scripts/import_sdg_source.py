#!/usr/bin/env python3
"""Import a keyword source .docx and convert it into the canonical CSV.

You normally do NOT need this. The skill ships a plain-text CSV that any AI can
read, and that CSV is the source of truth. Run this only when a new keyword list
revision is published and you want to refresh the whole skill.

Currently supports: .docx format only.
Planned for a future version: CSV and plain-text formats.

    pip install python-docx
    python3 import_sdg_source.py "/path/to/new-keywords.docx"

Reads :  the .docx path given on the command line
Writes: resources/sdg_keywords.csv   (overwritten — review with git diff!)
Then  : python3 build_resources.py

The old CSV is backed up to resources/sdg_keywords.csv.bak before overwriting.
"""

from __future__ import annotations

import argparse
import csv
import re
import shutil
import sys
from datetime import date
from pathlib import Path

try:
    import docx  # type: ignore
except ImportError:
    sys.exit("python-docx is required for this step:  pip install python-docx")

HERE = Path(__file__).resolve().parent
CSV_PATH = HERE.parent / "resources" / "sdg_keywords.csv"

# Curly first, so a round bracket nested inside a curly keyword survives.
TERM_RE = re.compile(r"\{([^{}]*)\}|\(([^()]*)\)")

OFFICIAL_TITLES = {
    1: "End poverty in all its forms everywhere",
    2: "End hunger, achieve food security and improved nutrition and promote sustainable agriculture",
    3: "Ensure healthy lives and promote well-being for all at all ages",
    4: "Ensure inclusive and equitable quality education and promote lifelong learning opportunities for all",
    5: "Achieve gender equality and empower all women and girls",
    6: "Ensure availability and sustainable management of water and sanitation for all",
    7: "Ensure access to affordable, reliable, sustainable and modern energy for all",
    8: "Promote sustained, inclusive and sustainable economic growth, full and productive employment and decent work for all",
    9: "Build resilient infrastructure, promote inclusive and sustainable industrialization and foster innovation",
    10: "Reduce inequality within and among countries",
    11: "Make cities and human settlements inclusive, safe, resilient and sustainable",
    12: "Ensure sustainable consumption and production patterns",
    13: "Take urgent action to combat climate change and its impacts",
    14: "Conserve and sustainably use the oceans, seas and marine resources for sustainable development",
    15: "Protect, restore and promote sustainable use of terrestrial ecosystems",
    16: "Promote peaceful and inclusive societies for sustainable development, provide access to justice for all and build effective, accountable and inclusive institutions at all levels",
    17: "Strengthen implementation, revitalize the Global Partnership and enhance the means of implementation for sustainable development",
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("docx_path", help="the newly revised INTI keyword .docx")
    args = parser.parse_args()

    src = Path(args.docx_path)
    if not src.is_file():
        sys.exit(f"Not found: {src}")

    document = docx.Document(str(src))
    if not document.tables:
        sys.exit(f"No tables found in {src}")

    table = document.tables[0]
    revision = next((p.text.strip() for p in document.paragraphs if p.text.strip()), "not stated")

    parsed: list[tuple[int, str, str, str, str]] = []
    for index, row in enumerate(table.rows[1:], start=1):
        name = row.cells[0].text.strip()
        blob = row.cells[1].text.strip()
        for match in TERM_RE.finditer(blob):
            curly, paren = match.group(1), match.group(2)
            keyword = (curly if curly is not None else paren).strip()
            if not keyword:
                continue
            parsed.append(
                (index, name, OFFICIAL_TITLES.get(index, name), keyword,
                 "curly" if curly is not None else "paren")
            )

    if not parsed:
        sys.exit(f"No {{keyword}} / (keyword) terms parsed from {src}")

    if CSV_PATH.is_file():
        backup = CSV_PATH.with_suffix(".csv.bak")
        shutil.copy2(CSV_PATH, backup)
        print(f"Backed up existing CSV -> {backup.name}")

    CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
    with CSV_PATH.open("w", encoding="utf-8", newline="") as fh:
        fh.write("# INTI SDG keyword list - canonical flat table\n")
        fh.write(f"# source_file: {src.name}\n")
        fh.write(f"# source_revision: {revision}\n")
        fh.write(f"# generated: {date.today().isoformat()}\n")
        fh.write(f"# {len(parsed)} terms across {len({r[0] for r in parsed})} goals\n")
        fh.write("#\n")
        fh.write("# source_delimiter records how INTI stores the term in their file:\n")
        fh.write("#   curly = {keyword} (Goals 1-12) | paren = (keyword) (Goals 13-17)\n")
        fh.write("# THIS SKILL ALWAYS WRITES CURLY BRACES regardless of source_delimiter.\n")
        csv.writer(fh).writerow(["goal_number", "goal_name", "official_title", "keyword", "source_delimiter"])
        csv.writer(fh).writerows(parsed)

    print(f"Imported {len(parsed)} terms from '{revision}'")
    print(f"Wrote {CSV_PATH}")
    print("\nNext: python3 build_resources.py")


if __name__ == "__main__":
    main()