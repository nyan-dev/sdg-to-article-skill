#!/usr/bin/env python3
"""Build the readable/structured SDG resources from the canonical CSV.

Standard library only. No python-docx, no network. Run this after editing
resources/sdg_keywords.csv.

    python3 build_resources.py

Reads :  resources/sdg_keywords.csv
Writes: resources/sdg_keywords.md     (grouped, cross-products collapsed)
        resources/sdg_keywords.json   (same structure the validator consumes)
"""

from __future__ import annotations

import csv
import json
import re
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESOURCES = HERE.parent / "resources"
CSV_PATH = RESOURCES / "sdg_keywords.csv"

# Only attempt cross-product collapse on a large, uniform block. A short list
# that merely happens to contain " and " must not be rewritten into product form.
COLLAPSE_MIN_TERMS = 40
COLLAPSE_MIN_COVERAGE = 0.95

MOJIBAKE_HINTS = ("?",)


def read_csv(path: Path) -> tuple[dict[str, str], list[dict]]:
    """Return (metadata from # comment lines, data rows)."""
    if not path.is_file():
        sys.exit(f"Canonical keyword CSV not found: {path}")

    meta: dict[str, str] = {}
    lines = path.read_text(encoding="utf-8").splitlines()

    body_start = 0
    for i, line in enumerate(lines):
        if not line.startswith("#"):
            body_start = i
            break
        stripped = line.lstrip("#").strip()
        if ":" in stripped:
            key, _, value = stripped.partition(":")
            meta[key.strip()] = value.strip()
    else:
        body_start = len(lines)

    reader = csv.DictReader(lines[body_start:])
    rows = [r for r in reader if r and r.get("keyword")]
    if not rows:
        sys.exit(f"No keyword rows parsed from {path}")
    return meta, rows


def try_collapse(keywords: list[str]) -> dict | None:
    """Detect a generated prefix x concept product, as used by Goals 14 and 15."""
    if len(keywords) < COLLAPSE_MIN_TERMS:
        return None
    if any(" and " not in k for k in keywords):
        return None

    pairs = [tuple(k.split(" and ", 1)) for k in keywords]
    pairs = [(p.strip(), c.strip()) for p, c in pairs]

    prefixes = sorted({p for p, _ in pairs})
    concepts = sorted({c for _, c in pairs})
    in_product = {(p, c) for p in prefixes for c in concepts}
    hits = sum(1 for pair in pairs if pair in in_product)
    coverage = hits / len(pairs)
    if coverage < COLLAPSE_MIN_COVERAGE:
        return None

    stragglers = sorted({f"{p} and {c}" for p, c in pairs if (p, c) not in in_product})
    return {
        "prefixes": prefixes,
        "concepts": concepts,
        "stragglers": stragglers,
        "coverage": round(coverage, 4),
        "combinations": len(prefixes) * len(concepts),
        "listed": len(pairs),
    }


def build(meta: dict[str, str], rows: list[dict]) -> list[dict]:
    order: list[int] = []
    grouped: dict[int, dict] = {}

    for row in rows:
        number = int(row["goal_number"])
        if number not in grouped:
            order.append(number)
            grouped[number] = {
                "number": number,
                "name": row["goal_name"].strip(),
                "official": (row.get("official_title") or row["goal_name"]).strip(),
                "delims": set(),
                "terms": [],
            }
        grouped[number]["delims"].add(row["source_delimiter"].strip())
        grouped[number]["terms"].append(row["keyword"].strip())

    goals = []
    for number in sorted(order):
        goal = grouped[number]
        keywords = goal["terms"]
        goals.append(
            {
                "number": number,
                "name": goal["name"],
                "official": goal["official"],
                "source_delimiters": sorted(goal["delims"]),
                "term_count": len(keywords),
                "terms": keywords,
                "collapse": try_collapse(keywords),
                "mojibake": [k for k in keywords if any(h in k for h in MOJIBAKE_HINTS)],
            }
        )
    return goals


def render_markdown(goals: list[dict], meta: dict[str, str]) -> str:
    total = sum(g["term_count"] for g in goals)
    out: list[str] = []
    out.append("# INTI SDG Keywords")
    out.append("")
    out.append(f"**Source:** INTI International University - {meta.get('source_file', 'official keyword list')}  ")
    out.append(f"**INTI revision:** {meta.get('source_revision', 'unknown')}  ")
    out.append(f"**Canonical data:** `sdg_keywords.csv` ({total} terms, {len(goals)} goals)  ")
    out.append(f"**Rebuilt:** {date.today().isoformat()}")
    out.append("")
    out.append("## How to use these")
    out.append("")
    out.append("Write every keyword wrapped in **curly braces**, regardless of goal:")
    out.append("`{food security}`, `{resource efficiency}`.")
    out.append("")
    out.append("The INTI source file is internally inconsistent - Goals 1-12 store")
    out.append("keywords as `{keyword}` but Goals 13-17 store them as `(keyword)`.")
    out.append("This skill normalises everything to curly braces. See SKILL.md for the")
    out.append("rationale and the residual risk if INTI's checker is doing exact")
    out.append("matching against the original delimiters.")
    out.append("")
    out.append("**Copy keywords verbatim.**")
    out.append("")
    out.append("- A trailing `*` is an INTI stem marker (`coast*` covers coastal). Keep it.")
    out.append("- A `?` inside a word (`fertili?er`, `democrati?ation`) is lost encoding in")
    out.append("  INTI's own file. Reproduce as-is rather than correcting it.")
    out.append("- Do not invent, pluralise, reword, or translate a keyword.")
    out.append("")
    out.append("---")
    out.append("")

    for goal in goals:
        out.append(f"## SDG {goal['number']} - {goal['name']}")
        out.append("")
        out.append(f"**Official title:** {goal['official']}  ")
        out.append(
            f"**Keywords:** {goal['term_count']} "
            f"(INTI stores as {'/'.join(goal['source_delimiters'])}; write as curly)"
        )
        out.append("")

        collapse = goal["collapse"]
        if collapse:
            out.append(
                f"> Generated cross-product: {collapse['listed']} listed terms = "
                f"{len(collapse['prefixes'])} prefixes x {len(collapse['concepts'])} concepts "
                f"({collapse['coverage']:.0%} coverage). A valid keyword is any prefix "
                f"+ `and` + any concept."
            )
            out.append("")
            out.append(f"**Prefixes:** {' | '.join(collapse['prefixes'])}")
            out.append("")
            out.append(f"**Concepts:** {' | '.join(collapse['concepts'])}")
            out.append("")
            if collapse["stragglers"]:
                out.append(f"**Stragglers** not in the product ({len(collapse['stragglers'])}):")
                out.append("")
                for item in collapse["stragglers"]:
                    out.append(f"- `{{{item}}}`")
                out.append("")
        else:
            out.append("```")
            out.append(", ".join("{" + k + "}" for k in goal["terms"]))
            out.append("```")
            out.append("")

        if goal["mojibake"]:
            items = ", ".join("`" + m + "`" for m in goal["mojibake"])
            out.append(f"> Contains `?` where an accented character was lost. Reproduce as-is: {items}")
            out.append("")

        out.append("---")
        out.append("")

    return "\n".join(out)


def main() -> None:
    meta, rows = read_csv(CSV_PATH)
    goals = build(meta, rows)

    total = sum(g["term_count"] for g in goals)
    md_path = RESOURCES / "sdg_keywords.md"
    md_path.write_text(render_markdown(goals, meta), encoding="utf-8")

    json_path = RESOURCES / "sdg_keywords.json"
    json_path.write_text(
        json.dumps(
            {
                "source_file": meta.get("source_file", ""),
                "source_revision": meta.get("source_revision", ""),
                "extracted": date.today().isoformat(),
                "total_terms": total,
                "goals": goals,
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )

    collapsed = [g["number"] for g in goals if g["collapse"]]
    print(f"Built from {CSV_PATH.name}: {len(goals)} goals / {total} terms")
    print(f"Cross-product collapsed: {collapsed or 'none'}")
    print(f"Wrote {md_path}")
    print(f"Wrote {json_path}")


if __name__ == "__main__":
    main()