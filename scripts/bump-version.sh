#!/usr/bin/env bash
#
# Bump the Marketing Growth Suite version across all three version files in
# lockstep. `.claude-plugin/marketplace.json` (plugins[].version) is the single
# source of truth for the module version; this script keeps plugin.json and
# skills/module.yaml synchronized to it.
#
# It does NOT commit or tag. Review the diff, commit, and push to `main`; the
# release-tag GitHub Actions workflow then creates and pushes the matching
# annotated `v<semver>` tag automatically.
#
# Usage:
#   scripts/bump-version.sh <new-semver>      e.g. scripts/bump-version.sh 2.1.0
#
set -euo pipefail

NEW_VERSION="${1:-}"

if [[ -z "$NEW_VERSION" ]]; then
  echo "Usage: scripts/bump-version.sh <new-semver>   (e.g. 2.1.0)" >&2
  exit 2
fi

if [[ ! "$NEW_VERSION" =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
  echo "Error: '$NEW_VERSION' is not a valid semver (expected MAJOR.MINOR.PATCH, e.g. 2.1.0)." >&2
  exit 2
fi

if ! command -v jq >/dev/null 2>&1; then
  echo "Error: jq is required but not installed." >&2
  exit 1
fi

# Resolve repo root so the script works from any directory.
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MARKETPLACE="$REPO_ROOT/.claude-plugin/marketplace.json"
PLUGIN="$REPO_ROOT/.claude-plugin/plugin.json"
MODULE_YAML="$REPO_ROOT/skills/module.yaml"

for f in "$MARKETPLACE" "$PLUGIN" "$MODULE_YAML"; do
  if [[ ! -f "$f" ]]; then
    echo "Error: expected file not found: $f" >&2
    exit 1
  fi
done

OLD_VERSION="$(jq -r '.plugins[0].version' "$MARKETPLACE")"

# marketplace.json — source of truth.
tmp="$(mktemp)"
jq --arg v "$NEW_VERSION" '.plugins[0].version = $v' "$MARKETPLACE" > "$tmp"
mv "$tmp" "$MARKETPLACE"

# plugin.json — native Claude Code plugin manifest.
tmp="$(mktemp)"
jq --arg v "$NEW_VERSION" '.version = $v' "$PLUGIN" > "$tmp"
mv "$tmp" "$PLUGIN"

# skills/module.yaml — BMAD module manifest. Only the module_version line changes.
sed -i -E "s/^module_version: .*/module_version: $NEW_VERSION/" "$MODULE_YAML"

# Sanity check: confirm all three now agree.
mv_v="$(jq -r '.plugins[0].version' "$MARKETPLACE")"
pl_v="$(jq -r '.version' "$PLUGIN")"
my_v="$(sed -nE 's/^module_version: (.*)$/\1/p' "$MODULE_YAML")"

if [[ "$mv_v" != "$NEW_VERSION" || "$pl_v" != "$NEW_VERSION" || "$my_v" != "$NEW_VERSION" ]]; then
  echo "Error: version sync failed (marketplace=$mv_v plugin=$pl_v module=$my_v)." >&2
  exit 1
fi

echo "Bumped version: ${OLD_VERSION} -> ${NEW_VERSION}"
echo "  - .claude-plugin/marketplace.json (plugins[0].version)"
echo "  - .claude-plugin/plugin.json (version)"
echo "  - skills/module.yaml (module_version)"
echo
echo "Next steps:"
echo "  git add .claude-plugin/marketplace.json .claude-plugin/plugin.json skills/module.yaml"
echo "  git commit -m \"Release v${NEW_VERSION}\""
echo "  git push origin main"
echo
echo "On push to main, the release-tag workflow creates and pushes annotated tag v${NEW_VERSION}."
