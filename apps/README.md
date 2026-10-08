# Workout app adapters

Each supported app lives in `apps/<app>/` and exposes the same three jobs to the coach:

| Job | Hevy command (`python3 apps/hevy/hevy.py …`) | Private output (gitignored) |
|---|---|---|
| **Catalog**: which exercises the app accepts, including the user's custom ones | `sync-catalog` | `my-data/<app>/catalog.json` |
| **History**: what the user actually did | `sync-history`, then `summary` | `my-data/<app>/history.json`, `summary.json` |
| **Publish**: write the plan into the app | `list-routines`, then `publish-routine plan.json --folder NAME` (dry-run; `--apply --approve CODE` only after the user says yes) | – |

Supported apps: **Hevy** (`apps/hevy/API.md` has the API contract and its limits).

Rules for every adapter:
- Credentials come from environment variables, never from files in this repo.
- Enable the guard once per clone: `git config core.hooksPath .githooks` (CI also runs `scripts/check-no-private-paths.sh --tree`).
- Everything fetched from the user's account goes under `my-data/` (gitignored). Nothing personal in tracked files.
- Writes are dry-run by default and validated against the cached catalog before anything is sent. Applying needs the approval code from the preview, which is only valid for that exact content and destination.
- Never write to a user's app without their explicit approval. Present the workouts, ask where they should go (folders matter), ask about existing items, ask for changes, then ask for a yes.
- Stdlib-only Python so it runs anywhere without installs.

To add an app: create `apps/<app>/` with an API notes file and a CLI offering the same subcommands, add a row above, and
extend `.claude/skills/app-sync/SKILL.md`.
