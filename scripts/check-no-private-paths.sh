#!/usr/bin/env bash
# Fails if private paths (my-data/, my-plans/) are tracked or staged.
# Usage: check-no-private-paths.sh           -> checks the index (pre-commit)
#        check-no-private-paths.sh --tree    -> checks all tracked files (CI)
set -eu
if [ "${1:-}" = "--tree" ]; then files=$(git ls-files); else files=$(git diff --cached --name-only); fi
bad=$(printf '%s\n' "$files" | grep -E '^(my-data|my-plans)/' || true)
if [ -n "$bad" ]; then
  echo "error: private paths must never be committed:" >&2
  printf '  %s\n' $bad >&2
  echo "Unstage with: git rm --cached <path>" >&2
  exit 1
fi
