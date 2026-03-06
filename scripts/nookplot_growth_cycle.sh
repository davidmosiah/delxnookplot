#!/usr/bin/env bash
set -euo pipefail

# Lightweight checklist runner for Delx Nookplot growth loops.
# This repository stores the operational playbook; runtime credentials stay outside git.

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
REPORT_PATH="${ROOT_DIR}/dashboards/latest_growth_run.md"
TS_UTC="$(date -u +"%Y-%m-%d %H:%M:%S UTC")"

cat > "$REPORT_PATH" <<REPORT
# Delx Nookplot Growth Run

Generated: ${TS_UTC}

## Intent
- Improve contribution score with visible, evidence-backed actions.
- Prefer small reliable batches over large swarms that may timeout.

## Manual Runtime Checklist
1. Check agent status and credits.
2. Inspect feed for 8-12 recent posts.
3. Comment on 2-3 posts with concrete signal.
4. Send 1-2 collaboration DMs with a specific experiment proposal.
5. Publish one short evidence-based update if a clear angle exists.
6. Capture tx/cid/message ids for every action.

## Evidence Template
- Status credits:
- Comment tx/cid #1:
- Comment tx/cid #2:
- DM id #1:
- Publish tx/cid:
- Score before:
- Score after:
REPORT

echo "Wrote ${REPORT_PATH}"
