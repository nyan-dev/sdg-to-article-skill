# Changelog

All notable changes to sdg-to-article-skill are documented here.

---

## [1.0.0] — October 2026

### Initial release

**Keyword data**
- Source: INTI International University — *SDG Goals Keywords as of 060625.docx*
- Revision: 06 June 2025
- Coverage: 17 goals, 1,634 terms
- Goals 14 and 15 cross-products collapsed to prefix × concept grids in the
  markdown resource (7 × 42 and 4 × 72 respectively)

**Citations bundled**
- UN DESA. (2026). *The Sustainable Development Goals Report 2026*. United Nations.
  ISBN 9789211547351. Published 7 July 2026.
- United Nations General Assembly. (2015). *Transforming our world: the 2030 Agenda
  for Sustainable Development* (A/RES/70/1).

**Features**
- Three insertion levels: Minimal, Complete, Custom
- Input detection: manuscript, project folder, or description
- Clean keyword rule: stem-form (`*`) and encoding-artefact (`?`) keywords
  excluded from drafted text; validator handles stem-matching transparently
- Universal platform support: works with any AI tool via root `SKILL.md`;
  `install.sh` targets opencode, AGY (Antigravity), and Claude Code
- Keyword validator (`check_sdg.py`) — exit codes 0 / 1 / 2
- Resource builder (`build_resources.py`) — CSV → md + json, stdlib only
- Keyword importer (`import_sdg_source.py`) — `.docx` format; CSV/txt planned

---

## Upcoming

- `import_sdg_source.py`: support for CSV and plain-text keyword source formats
- Additional tool install paths as AI coding tools stabilise their skill directories
