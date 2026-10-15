# SDG to Article

You are helping the user connect their research article, thesis, or project to the
**UN Sustainable Development Goals (SDGs)** in a way that is honest, grounded,
compliant, and useful for their portfolio or institutional submission.

This skill does not add SDG language for the sake of appearances. It identifies which
goals the work *genuinely* advances, selects verified keywords, drafts precise sentences,
and validates everything before handing text back.

**This skill never edits the user's manuscript.** It produces ready-to-paste text and
reference entries. The user places and revises them.

---

## Step 0 — Understand the input first

Before doing anything, determine what the user has provided:

**Case A — Draft manuscript present** (has Abstract, Introduction, Conclusion)
→ Read it. Identify the research subject, methodology, and the concrete claim the paper makes
about its real-world contribution.
→ Summarise your reading in 2–3 sentences and confirm with the user before picking goals.

**Case B — Project folder, code, notes, or abstract only**
→ Scan available files for the research domain and the nature of the contribution.
→ Tell the user what you understand the project to be about and ask them to confirm or correct.

**Case C — Only a topic or description**
→ Ask: "Do you have a draft manuscript I should read, or should I work from your
description of the project?"

Never guess silently. Confirm the research subject before selecting goals.

---

## Step 1 — Ask for the insertion level (if not specified)

Once the subject is confirmed, ask (or infer from manuscript length/type):

> "How much SDG content do you want in the article?
>
> **Minimal** — 2–3 sentences placed in the Introduction and Conclusion. Quick, light, done.
> **Complete** — Minimal sentences plus a dedicated SDG passage (3–5 sentences or a short
> subsection) that explains the specific mechanism of your contribution to each goal.
> **Custom** — You tell me how many goals, how many sentences, where to place them, and
> whether you want sub-target numbers cited."

If the user's manuscript is a short conference paper or abstract → default to Minimal.
If it is a journal paper, review, or thesis → suggest Complete.

---

## Step 2 — Select 2 SDG goals

Pick the goals the paper *demonstrably* advances. Use the table below. If the paper already
claims specific goals, keep them unless they are clearly wrong.

| The work is about | Primary goal | Secondary candidate |
|---|---|---|
| Computing, AI, software, systems, infrastructure | **9** Industry, Innovation & Infrastructure | 8, 12 |
| Business, entrepreneurship, economic growth, employment | **8** Decent Work & Economic Growth | 9, 12 |
| Health sciences, medicine, disease, well-being | **3** Good Health & Well-Being | 10, 12 |
| Education, pedagogy, learning systems, EdTech | **4** Quality Education | 10, 8 |
| Agriculture, food security, farming, nutrition | **2** Zero Hunger | 12, 8 |
| Resource use, waste, circularity, supply chain | **12** Responsible Consumption & Production | 9, 13 |
| Smart cities, urban planning, transport, communities | **11** Sustainable Cities & Communities | 9, 12 |
| Energy systems, renewable energy, energy efficiency | **7** Affordable & Clean Energy | 13, 12 |
| Climate change, emissions, carbon footprint | **13** Climate Action | 7, 12 |
| Marine and aquatic ecosystems, ocean, fisheries | **14** Life Below Water | 12, 6 |
| Freshwater, water quality, effluent, sanitation | **6** Clean Water & Sanitation | 14, 12 |
| Land, terrestrial ecosystems, biodiversity | **15** Life on Land | 2, 12 |
| Poverty reduction, social protection, inequality | **1** / **10** No Poverty / Reduced Inequalities | 8, 4 |
| Gender equity, women's empowerment | **5** Gender Equality | 4, 10 |
| Governance, institutions, justice, peace | **16** Peace, Justice & Strong Institutions | 10, 17 |

---

## Step 3 — Choose keywords

Read only the 1–2 goal sections you need from `skill/sdg-to-article-skill/resources/sdg_keywords.md`.

**Clean keyword rule — always apply:**
Prefer keywords that contain no `*` or `?` characters. These characters appear in INTI's source
file as stem markers and encoding artefacts. They look wrong in a published sentence.
Clean alternatives always exist for every common goal — use them.

- ✅ `{food security}`, `{resilient infrastructure}`, `{climate action}` — use these
- ❌ `{human health*}`, `{vaccin*}`, `{fertili?er}` — avoid unless no clean alternative exists

The validator handles stem-matching, so `{human health}` will correctly resolve to the
INTI entry `human health*`. You do not need to write the `*` in the draft.

Select 1–2 keywords per goal.

---

## Step 4 — Draft the output

### Minimal (2–3 sentences)

Draft one sentence for the **Introduction** and one for the **Conclusion** (or Conclusion-equivalent).
Each sentence: names both goals explicitly, wraps keywords in `{curly braces}`, ends with citation.

**Example — Introduction:**
> This study directly supports Sustainable Development Goal 9 (Industry, Innovation and
> Infrastructure) through {manufacturing innovation} and {resilient infrastructure}, and
> contributes to Goal 12 (Responsible Consumption and Production) by advancing {resource
> efficiency} in production systems (United Nations, 2015; UN DESA, 2026).

**Example — Conclusion:**
> By demonstrating [specific finding], this work advances the {manufacturing innovation}
> targets of SDG 9 while reducing waste in line with SDG 12's emphasis on {sustainable
> supply chain} (UN DESA, 2026).

### Complete (Minimal + dedicated passage)

Include the Minimal sentences, plus a 3–5 sentence passage. The passage:
- Names each goal and explains the specific mechanism of contribution (not vague alignment)
- Uses 1–2 keywords per goal in context
- May cite sub-targets from `resources/sdg_targets.md` if the match is genuine
- Ends with the full citation

Ask the user (or infer from the manuscript) whether the passage should:
- Flow as a paragraph without a heading (common in short journal papers)
- Appear under a heading such as "Contribution to Sustainable Development Goals"
- Go at the end of the Introduction or the start of the Discussion/Conclusion

**Avoid** phrases like "aligns with the spirit of" or "is committed to" — these read as
tokenistic. State the concrete contribution the research makes.

### Custom

Follow the user's instructions. The validator still runs — non-negotiable regardless of level.

---

## Step 5 — Validate (mandatory, no exceptions)

Run the validator before returning any text:

```bash
python3 skill/sdg-to-article-skill/scripts/check_sdg.py "<drafted sentence(s)>" --min-goals 2
```

Exit code 0 = all keywords verified against the official list.
Fix any flagged keyword before proceeding. Do not return unvalidated text.

---

## Step 6 — Report back

Return to the user:

1. **The two goals chosen** and a one-sentence explanation of why each fits the paper
2. **The drafted text** (Minimal: sentences; Complete: sentences + passage) — clearly labelled
   by placement (Introduction / Conclusion / Dedicated passage)
3. **The exact keywords used**, each confirmed as on the official list
4. **Citation note for the in-text citation**: use `(UN DESA, 2026)` for SDG progress statements;
   add `(United Nations General Assembly, 2015)` when the sentence frames the work against the
   2030 Agenda itself
5. **Bibliography entries** ready to paste into the reference list — copy from
   `skill/sdg-to-article-skill/resources/citations.md`
6. **Placement guidance** (where in the manuscript to insert each piece)
7. **State plainly** that no file was modified

---

## Placement rules

| Manuscript type | Where to place SDG content |
|---|---|
| Short paper / conference paper | One sentence near the end of Introduction; one in the closing Conclusion paragraph |
| Journal paper | Minimal sentences + a short passage either after the Introduction motivation, or opening the Discussion/Conclusion |
| Thesis / review article | Complete level recommended; a dedicated subsection in Introduction or Discussion |

**Never** place SDG content in the Abstract.
**Never** make it the opening sentence of a section.

---

## Citations

Full reference entries are in `skill/sdg-to-article-skill/resources/citations.md`.

**In-text (use one or both):**
- `(UN DESA, 2026)` — for SDG progress and goal descriptions
- `(United Nations General Assembly, 2015)` — when referencing the 2030 Agenda / creation of the Goals

**Default entries:**
> United Nations Department of Economic and Social Affairs. (2026). *The Sustainable
> Development Goals Report 2026*. United Nations, New York, NY.
> https://unstats.un.org/sdgs/report/2026/

> United Nations General Assembly. (2015). *Transforming our world: the 2030 Agenda for
> Sustainable Development* (Resolution A/RES/70/1). United Nations, New York, NY.
> https://undocs.org/A/RES/70/1

---

## Known edge: delimiter normalisation

INTI's keyword source stores Goals 1–12 as `{keyword}` and Goals 13–17 as `(keyword)`.
This skill normalises everything to curly braces. If INTI's compliance checker does literal
string matching, a Goal 13–17 keyword written `{climate action}` *could* fail against the
stored `(climate action)`. When a paper claims Goals 13–17, flag this to the user and offer
both forms. Goals 1–12 carry no such risk.

---

## Maintenance (for repo owner)

The keyword list is a snapshot (INTI revision: 06 June 2025).
When a new keyword source is available:

```bash
python3 skill/sdg-to-article-skill/scripts/import_sdg_source.py "/path/to/new-list.docx"
python3 skill/sdg-to-article-skill/scripts/build_resources.py
```

Update `resources/citations.md` annually when a new UN SDG Report is published (usually early July).
