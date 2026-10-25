#!/bin/sh
# Manual sync from a local chinaeasymode checkout (normally the GitHub Action in that repo does this).
# Reads visa.json from origin/main, never from the working tree, so unmerged edits are not published.
# Usage: scripts/sync-local.sh ../chinaeasymode
set -e
SITE=${1:?path to chinaeasymode checkout}
cd "$(dirname "$0")/.."
git -C "$SITE" fetch -q origin main
git -C "$SITE" show origin/main:src/data/visa.json > upstream/visa.json
SOURCE_COMMIT=$(git -C "$SITE" rev-parse origin/main) python3 scripts/build.py
git status --short
