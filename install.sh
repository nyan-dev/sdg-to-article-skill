#!/usr/bin/env bash
# Install the sdg-to-article skill into AI tool skill directories.
#
#   ./install.sh          symlink (default; edits to the repo take effect live)
#   ./install.sh --copy   copy instead of symlink (use if the repo sits on a
#                         different filesystem, e.g. WSL/Windows boundary)
#
# Installs into whichever of these directories exist on this machine:
#   opencode   → ~/.config/opencode/skills/sdg-to-article/
#   AGY        → ~/.config/antigravity/skills/sdg-to-article/
#   Claude     → ~/.claude/skills/sdg-to-article/
#
# Re-run after cloning on a new machine, or after pulling if you used --copy.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_SRC="$REPO_DIR/skill/sdg-to-article-skill"
SKILL_NAME="sdg-to-article"

MODE="symlink"
[[ "${1:-}" == "--copy" ]] && MODE="copy"

if [[ ! -f "$SKILL_SRC/SKILL.md" ]]; then
  echo "error: $SKILL_SRC/SKILL.md not found. Run this from inside the repo." >&2
  exit 1
fi

# ── Tool directories ──────────────────────────────────────────────────────────

declare -A TOOL_DIRS=(
  ["opencode"]="$HOME/.config/opencode/skills"
  ["AGY"]="$HOME/.config/antigravity/skills"
  ["Claude"]="$HOME/.claude/skills"
)

INSTALLED=0

for TOOL in "${!TOOL_DIRS[@]}"; do
  BASE="${TOOL_DIRS[$TOOL]}"
  DEST="$BASE/$SKILL_NAME"

  # Only install into directories that exist (tool is present on this machine)
  if [[ ! -d "$BASE" ]]; then
    echo "  $TOOL  skill dir not found ($BASE) — skipping"
    continue
  fi

  # Remove any existing install
  if [[ -e "$DEST" || -L "$DEST" ]]; then
    echo "  $TOOL  replacing existing install at $DEST"
    rm -rf "$DEST"
  fi

  if [[ "$MODE" == "symlink" ]]; then
    ln -s "$SKILL_SRC" "$DEST"
    echo "  $TOOL  symlinked → $DEST"
  else
    cp -r "$SKILL_SRC" "$DEST"
    echo "  $TOOL  copied   → $DEST"
  fi

  INSTALLED=$((INSTALLED + 1))
done

echo ""

if [[ $INSTALLED -eq 0 ]]; then
  echo "No supported AI tool directories found on this machine."
  echo "You can still use the skill by referencing SKILL.md directly:"
  echo "  - Paste its contents into your AI tool's system prompt"
  echo "  - Or copy SKILL.md into your project as SKILL.md / CLAUDE.md"
  exit 0
fi

# ── Self-test ─────────────────────────────────────────────────────────────────
# Uses the source directly (tool installs may be symlinks pointing here).

if python3 "$SKILL_SRC/scripts/check_sdg.py" \
     "Test {food security} and {resource efficiency}." >/dev/null 2>&1; then
  echo "Validation check passed — skill is working."
else
  echo "warning: check_sdg.py self-test failed." >&2
  echo "  Confirm python3 is on PATH and resources/sdg_keywords.csv exists." >&2
  exit 1
fi

cat <<'EOF'

Done. The skill is available in every project folder.

Try it with:
  "Add SDG statements to manuscript.docx"
  "Which SDG goals should this paper cite?"

To use without installing, paste SKILL.md into your AI tool's system prompt.
EOF