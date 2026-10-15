# sdg-to-article Skill Package

This subfolder contains the self-contained skill package and validation scripts for the **sdg-to-article** tool.

## Contents

- **`SKILL.md`**: Agent instruction file with YAML frontmatter for tool discovery (opencode, Antigravity, Claude Code, etc.)
- **`resources/`**: Plain-text data resources:
  - `sdg_keywords.csv`: Canonical flat table (1,634 rows across 17 goals)
  - `sdg_keywords.md`: Human- and LLM-readable keyword reference
  - `sdg_keywords.json`: Structured dictionary consumed by `check_sdg.py`
  - `sdg_targets.md`: 169 official UN SDG sub-targets
  - `citations.md`: Verified, ready-to-paste reference entries
- **`scripts/`**:
  - `check_sdg.py`: Zero-dependency Python validator that inspects text or manuscripts for `{curly}` keywords
  - `build_resources.py`: Rebuilds the derived `.md` and `.json` files from `sdg_keywords.csv`
  - `import_sdg_source.py`: One-off utility to ingest future keyword `.docx` updates

## Quick Validation

```bash
# Validate a drafted sentence directly:
python3 scripts/check_sdg.py "This study advances {resilient infrastructure} and {resource efficiency}." --min-goals 2

# Scan a manuscript file (.docx or .txt):
python3 scripts/check_sdg.py path/to/manuscript.docx --min-goals 2
```

See the root [`README.md`](../../README.md) for full documentation, installation instructions, and workflow guidance.