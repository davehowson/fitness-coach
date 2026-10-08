# Workout app adapters

Each supported app lives in `apps/<app>/` and exposes the same three jobs to the coach:

| Job | Hevy command (`python3 apps/hevy/hevy.py …`) | Private output (gitignored) |
|---|---|---|
| **Catalog**: which exercises the app accepts, including the user's custom ones | `sync-catalog` | `my-data/<app>/catalog.json` |
| **History**: what the user actually did | `sync-history`, then `summary` | `my-data/<app>/history.json`, `summary.json` |
| **Publish**: write the plan into the app | `publish-routine plan.json` (dry-run unless `--apply`) | – |

Supported apps: **Hevy** (`apps/hevy/API.md` has the API contract and its limits).

Rules for every adapter:
- Credentials come from environment variables, never from files in this repo.
- Enable the guard once per clone: `git config core.hooksPath .githooks` (CI also runs `scripts/check-no-private-paths.sh --tree`).
- Everything fetched from the user's account goes under `my-data/` (gitignored). Nothing personal in tracked files.
- Writes are dry-run by default and validated against the cached catalog before anything is sent.
- Stdlib-only Python so it runs anywhere without installs.

To add an app: create `apps/<app>/` with an API notes file and a CLI offering the same subcommands, add a row above, and
extend `.claude/skills/app-sync/SKILL.md`.
