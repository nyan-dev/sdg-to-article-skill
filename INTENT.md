# Why I Built This, and How to Use It

*A reference and rationale guide for INTI researchers and students.*

This document is not a technical spec — `README.md` covers that. This one
records the **reasoning** behind the tool, the **workflow** to follow,
and the **judgement calls** made along the way.

Written: October 2026

---

## 1. The reason it exists

INTI International University requires every published paper to demonstrate
contribution to the UN Sustainable Development Goals. Concretely, per paper:

- cite **2 SDG goals**
- use keywords **from INTI's own official keyword list**
- add a short statement (1-2 sentences) tying the work to those goals
- support it with a citation

INTI supplies that keyword list as a `.docx`: one Word table, 17 rows, each cell
containing a few hundred keywords jammed into a single comma-separated blob.
Goals 1-12 store terms as `{keyword}`, Goals 13-17 as `(keyword)` — inconsistently,
with no explanation anywhere.

That file is genuinely painful to work with:

- **A machine can't read it reliably.** `.docx` is a zipped binary. Many AI tools
  and scripts simply skip it or silently return nothing.
- **It is 1,634 keywords.** You need maybe four of them. There is no way to
  quickly see "which ones suit my specific topic or paper?"
- **Goals 14 and 15 are machine-generated noise.** Goal 14's 294 keywords are
  really 7 prefixes × 42 concepts (`marine|ocean|oceans|sea|seas|coast*|mangrove`
  × `fisheries|pollution|coral bleaching|…`). Written out flat, that is 294 lines
  that tell you nothing.
- **Every paper needs the same UN citation**, and I'd been re-finding and
  re-verifying it repeatedly.

So the intent: **turn an unusable Word file into plain text an AI can read, make
the right keyword easy to find, and enforce correctness before anything reaches a
manuscript.**

---

## 2. What I decided, and why

Four judgement calls I want to remember, because they were not obvious:

**Plain text only.** The `.docx` is not shipped. The canonical data file is
`sdg_keywords.csv` — 1,634 rows, RFC-4180, readable by any AI, script, or
spreadsheet. Markdown and JSON are *derived* from it. I found and removed the
docx because shipping a binary that some tools cannot parse defeats the purpose.

**Normalise everything to curly braces.** INTI is inconsistent — `{keyword}` for
Goals 1-12, `(keyword)` for 13-17. I chose to always write `{keyword}`, because
that is the form the user confirms by default, and consistency means only one
format to remember. *Known risk recorded in `SKILL.md`: if INTI's checker does
literal matching including delimiters, a Goal 13-17 keyword written
`{marine and fisheries}` may not match their stored `(marine and fisheries)`.
Still unresolved — worth one question to the research office.*

**One fixed citation, not a fresh search each time.** I searched for and verified
a UN publication for 2026:

> United Nations Department of Economic and Social Affairs. (2026). *The
> Sustainable Development Goals Report 2026*. United Nations, New York, NY.
> https://unstats.un.org/sdgs/report/2026/

Published 7 July 2026, ISBN 9789211547351 — verified against UN iLibrary and
DESA Publications, not written from memory. Paired with UNGA Resolution 70/1
(2015), which is the instrument that actually created the 17 Goals and never goes
stale. Together these cover every paper without re-researching.

**Validate, don't trust.** `skill/inti-sdg/scripts/check_sdg.py` fails on any
keyword not literally on INTI's list. This matters more than it sounds: a keyword
can look completely plausible and still not be on the list, which is a silent
compliance failure. I would rather be told "this one isn't valid" than discover
it at submission.

---

## 3. How I use it day to day

### Setup, once per machine

```bash
cd /mnt/d/academics/inti-sdg-skill
./install.sh
```

Symlinks `skill/inti-sdg` into `~/.config/opencode/skills/`, so the skill is
available in **every** project folder — Thesis, Paper 1, Paper 2, anything
opened in future. Edits to the repo take effect immediately; no reinstall needed.
(Use `./install.sh --copy` if the repo ever sits across a filesystem boundary.)

No dependencies. Python 3 standard library only. No network access at runtime.

### The normal case

Open the paper's folder and just ask. No flags, no paths:

> Add INTI SDG statements to `manuscript.docx`

or

> Which SDG goals should this paper cite?

The skill will:

1. Read the manuscript to work out subject matter and the concrete
   sustainability claim
2. Pick 2 goals using a lookup table (e.g., computing/tech → **SDG 9**; health → **SDG 3**;
   business/growth → **SDG 8**; agriculture/food → **SDG 2**; resource efficiency → **SDG 12**)
3. Choose 1-2 keywords per goal from `sdg_keywords.md`
4. Draft 1-2 sentences with keywords in curly braces
5. **Run the validator** and refuse to proceed if any keyword is invalid
6. Report back: goals chosen and why, the sentence, the exact keywords, the
   references to add, and a suggested insertion point

**It never edits the manuscript.** I paste the text myself. That was a deliberate
choice — a tool that silently rewrites an academic manuscript is a tool I would
not trust, and I would not use.

### My own manual path

Sometimes I don't want the skill at all. I open the CSV directly:

```bash
cd /mnt/d/academics/inti-sdg-skill/skill/inti-sdg/resources

# list every keyword for SDG 2
python3 -c "import csv; L=open('sdg_keywords.csv').read().splitlines(); \
print('\n'.join(r['keyword'] for r in csv.DictReader(L[next(n for n,l in enumerate(L) if not l.startswith('#')):]) \
if r['goal_number']=='2'))"
```

Then I write the sentence myself and verify it:

```bash
python3 ../scripts/check_sdg.py "my sentence with {food security} here" --min-goals 2
```

This is a quick, direct way to test and verify keywords for your draft.

### Checking a finished manuscript

```bash
python3 scripts/check_sdg.py path/to/manuscript.docx
```

Exit 2 with "No `{curly}` keywords found" means the paper has zero INTI keywords —
the most common failure when checking an unannotated draft.

---

## 4. The steps, condensed

For any paper, the process is the same five steps:

| # | Step | Rule |
|---|---|---|
| 1 | Identify the paper's real subject | Pick goals the work *demonstrably* supports, not ones that merely sound good |
| 2 | Choose at least 2 goals | Select goals directly relevant to the paper's domain |
| 3 | Pick 1-2 keywords per goal | Verbatim from the list. Keep `*` stem markers. Keep `?` encoding artifacts. Never invent or reword |
| 4 | Write 1-2 sentences + citation | `(UN DESA, 2026)`, plus `(United Nations General Assembly, 2015)` when framing against the 2030 Agenda |
| 5 | Validate before pasting | `check_sdg.py --min-goals 2`. Do not skip this |

**Placement.** Short paper or conference paper → one sentence at the end of the
Introduction, or the closing Conclusion paragraph. Review or long journal paper →
a short 3-5 sentence paragraph in the Introduction, or a closing Discussion
paragraph. **Never** in the Abstract. **Never** as the opening sentence.

**Avoid** "aligns with the spirit of" / "is committed to" — tokenistic, and
reviewers notice. State the concrete contribution.

---

## 5. Worked example

Subject: Sustainable agricultural and production systems.

Goals chosen: **SDG 2 (Zero Hunger)** and **SDG 12 (Responsible Consumption and
Production)** — which also happens to match what the manuscript claimed.

**Sentence A** (Introduction/Conclusions, SDG 2):

> By optimizing feed inputs while meeting nutritional requirements, the
> formulation directly advances Sustainable Development Goal 2 (Zero Hunger) by
> strengthening {food security} and {agricultural productivity} (United Nations,
> 2015; UN DESA, 2026).

**Sentence B** (last section, SDG 12):

> Equally, by directing finite resources to their highest-value use, the same
> approach supports Sustainable Development Goal 12 (Responsible Consumption and
> Production) through {sustainable food consumption} and {sustainable supply
> chain}, reducing environmental footprints without compromising output quality
> (UN DESA, 2026).

Validated: 4 keywords, 2 goals, all literal entries on INTI's list.

### A trap I nearly fell into

My first instinct was `{resource efficiency}` for SDG 12. It reads perfectly for
that goal — but it appears under **both SDG 8 and SDG 12** in INTI's list. Using
it would have credited the wrong goal. The validator flagged it as ambiguous.

**Lesson: always run the check. The keywords that feel most obviously right are
the most likely to be the ones I haven't verified.**

### Manuscript adjustments to keep in mind

- Delete any redundant or vague SDG clauses buried mid-paragraph in the conclusions
- Add reference entries (UN DESA 2026 and UNGA 70/1) to your bibliography

---

## 6. Keeping it current

**I edited the CSV by hand** → rebuild the derived files:

```bash
cd skill/inti-sdg && python3 scripts/build_resources.py
```

**INTI published a new revision** → import once, then rebuild:

```bash
pip install python-docx
python3 scripts/import_inti_docx.py "/path/to/new INTI list.docx"
python3 scripts/build_resources.py
```

The importer backs up the old CSV first, and is the *only* part of the skill that
touches a `.docx`. Delete the file afterwards — nothing else needs it.

**A newer annual UN report is out** (usually early July) → update the year in
`resources/citations.md`.

---

## 7. What this tool does not do

Being clear about the limits, so I don't over-trust it:

- **It does not edit manuscripts.** By design.
- **It does not know INTI's compliance checker.** The curly-vs-paren risk for
  Goals 13-17 is unresolved and only INTI can settle it.
- **It does not judge whether my SDG claim is honest.** It checks that keywords
  exist on the list, not that my paper genuinely advances that goal. That
  judgement stays mine, and I should not let the tool pick goals for me just
  because they match keywords.
- **Sub-targets are optional.** `sdg_targets.md` has all 169 official UN targets,
  but I should only cite one when the claim actually matches its wording.
- **The keyword list is a snapshot**, stamped 06 June 2025. If INTI revises it,
  the tool is wrong until re-imported.

---

## 8. If I only remember one thing

**Run `check_sdg.py` before pasting anything into a manuscript.**

The most likely way this whole exercise goes wrong is not a malformed file or a
missing goal — it is a keyword that looks authoritative, reads naturally in the
sentence, and quietly isn't on INTI's list. That failure is invisible in
review and fatal at submission. The validator exists to catch exactly that, and
it takes one second to run.