#!/opt/local/bin/bash
# Watch what the ai-contribution-policies bundle depends on, twice a week, unattended. ADR-0013.
#
# The Knowledge/ bundle sweep proves the bundles are well-formed and flags records past
# `stale_after` — it moved there with the bundles on 2026-09-20 (ADR-0014). Neither that nor a hook
# can notice that a policy changed before its record expires — which is how the Rust, Fedora and
# Asahi Linux records were all wrong on 2026-09-14 with every gate green. This runs the two
# checks that can, and always raises a notification, including when nothing changed: a scheduled
# check that is silent on success cannot be told apart from one that stopped running.
#
# It edits nothing and pushes nothing. A reported change is a reason to re-read a primary source
# in a session, the same way every other change to a record is made.
#
# Exits non-zero only when a check could not do its job. Changes are findings, not failures.

set -uo pipefail

SCRIPTS="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"   # <bundle>/scripts
BUNDLE="$(cd "$SCRIPTS/.." && pwd)/knowledge"
WORKSPACE="$(cd "$SCRIPTS/../../workspace/scripts" && pwd)"   # Knowledge: owns the schedule
# Git-ignored, beside the bundle's other OKF caches (Knowledge ADR-0004). It lived under
# ~/Library/Application Support until 2026-11-01.
STATE="${SOURCE_WATCH_STATE:-$(cd "$SCRIPTS/.." && pwd)/.okf/cache/source-watch}"

notify() {
    # The message goes in as an argument, never spliced into AppleScript source.
    /usr/bin/osascript - "$1" >/dev/null 2>&1 <<'OSA'
on run argv
    display notification (item 1 of argv) with title "Bundle source watch"
end run
OSA
}

fail() {
    echo "watch-sources: $1" >&2
    notify "Did not run: $1"
    exit 1
}

[ -f "$BUNDLE/index.md" ] || fail "no bundle at $BUNDLE"
for tool in python3 curl gh; do
    command -v "$tool" >/dev/null 2>&1 || fail "$tool not on PATH"
done
# Pull-request state is the signal that would have caught the Rust record. Without gh that check
# degrades to nothing, so refuse to run rather than report a partial clean result.
gh auth status >/dev/null 2>&1 || fail "gh is not authenticated"

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

echo "=== source watch, $(date -u +%Y-%m-%dT%H:%M:%SZ) ==="
rc=0
python3 "$SCRIPTS/check-upstream-list.py" \
    --bundle "$BUNDLE" --state "$STATE/upstream-list.json" --summary-file "$tmp/upstream" || rc=1
echo
# This job's own installation, before anything it is meant to check. run-gates.sh used to assert  # <!-- historical-filename: retired 2026-09-20 with the bundle sweep, ADR-0014 -->
# this and was retired with the bundles (ADR-0014), leaving nothing running `--check` in this
# workspace — so it moves here, to the only scheduled job left. A schedule that checks nothing is
# the failure this portfolio keeps re-learning; it was found again on 2026-09-20 when an orphaned
# agent stayed loaded, pointing at a deleted script, while `--check` reported OK.
"$WORKSPACE/install-launchd.sh" --check || fail "launchd installation has drifted"

python3 "$SCRIPTS/check-primary-drift.py" \
    --state-dir "$STATE/primary" --summary-file "$tmp/primary" "$BUNDLE" || rc=1

primary="$(cat "$tmp/primary" 2>/dev/null || echo 'primary-source check failed')"
upstream="$(cat "$tmp/upstream" 2>/dev/null || echo 'upstream list check failed')"
msg="$primary; $upstream"
[ "$rc" -eq 0 ] || msg="ERROR — $msg"
echo
echo "summary: $msg"
notify "$msg"
exit "$rc"
