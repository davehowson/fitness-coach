---
name: app-sync
description: Pull the exercise catalog and training history from the user's workout app (currently Hevy only) into the private, gitignored my-data/ folder, so the workout-coach skill can build plans from exercises the app actually supports and from what the user really did. Run before workout-coach whenever the user logs workouts in a supported app, and again after a plan to publish it. Use when the user mentions Hevy, wants routines created in an app, or wants their workout history considered.
---

# App Sync

Runs **before** `workout-coach` (pre-flight) and **after** it (publish). Supported app: **Hevy**. Contract and limits: `apps/hevy/API.md`. Adapter layout: `apps/README.md`. Paths are relative to the repo root.

## Privacy (hard rules)
- Everything fetched goes to `my-data/<app>/`. Confirm `git check-ignore my-data/` succeeds before the first sync; if not, add `my-data/` to `.gitignore` first.
- The catalog contains the user's custom exercises and the history is their training log. Never copy either into tracked files, commit messages or examples. Never `git add` anything under `my-data/` or `my-plans/`.
- The API key lives only in the `HEVY_API_KEY` environment variable. Never write it to a file or echo it.

## Pre-flight (before workout-coach)

1. Ask which app they log in (only Hevy is supported; if another, say so and continue without sync).
2. Check access: `python3 apps/hevy/hevy.py check`. If `HEVY_API_KEY` is missing, tell the user: Hevy **Pro** is required, create a key at https://hevy.com/settings?developer and export it as `HEVY_API_KEY`. Do not ask them to paste the key into chat. If they cannot, continue without sync and say plans won't be app-compatible.
3. **Catalog** (needed to build any plan): if `my-data/hevy/catalog.json` is missing, or the user added custom exercises since, run `python3 apps/hevy/hevy.py sync-catalog`. Otherwise reuse the cache (check `fetched_at`; refresh if the user says they changed exercises).
4. **History** (skip if the user has no logged workouts or opts out): `python3 apps/hevy/hevy.py sync-history` (first run is a full pull at 10 workouts per call; later runs are incremental), then `python3 apps/hevy/hevy.py summary --weeks 12`.
5. Hand over to `workout-coach` with two things in mind: `my-data/hevy/catalog.json` is the **only** allowed exercise pool, and `my-data/hevy/summary.json` is the **historical baseline** (frequency, session length, weekly sets per muscle, last top set and best e1RM per exercise).

## Publish (after the user approves a plan)

1. `workout-coach` writes a routines file `my-plans/<slug>-<date>.routines.json` (schema below).
2. Dry run first: `python3 apps/hevy/hevy.py publish-routine my-plans/<file>.routines.json`. It validates every exercise against the catalog and every set against the exercise type, and refuses to duplicate an existing routine title.
3. Show the user what will be created (routine names, exercise counts, folder). **Hevy has no delete**: creates are permanent, so get a clear yes, then re-run with `--apply`. Use `--update` only when the user wants to overwrite a same-named routine.
4. Never create custom exercises silently. If something is missing, first swap to a same-pattern exercise that exists in the catalog (`python3 apps/hevy/hevy.py resolve "<name>"` lists the closest). Only if nothing fits, propose `create-exercise` (dry-run by default; permanent, cannot be edited) and wait for approval.

### Routines file schema
```json
{ "folder": "Block 1 (optional, created if missing)",
  "routines": [ { "title": "Upper A", "notes": "optional",
    "exercises": [ { "exercise": "Bench Press (Barbell)",
        "rest_seconds": 120, "notes": "Last time: 80 kg x 8", "superset_id": null,
        "sets": [ { "type": "warmup", "reps": 10, "weight_kg": 40 },
                  { "type": "normal", "reps": [6, 8], "weight_kg": 80 } ] } ] } ] }
```
- `exercise` must equal a catalog title exactly (or give `template_id`). Weights are **kg**.
- `reps` is an int or `[low, high]` (becomes Hevy's rep range). Timed exercises use `duration_seconds` instead.
- `type`: `warmup | normal | failure | dropset`. Leave `weight_kg` null when there is no history to anchor a load.

## Failure handling
- 401: bad key or not Pro. 403 on create: account's routine/custom-exercise limit reached; report it, don't retry. 400 on list: page size too large (client already caps). 429/5xx on reads are retried automatically; creates are never auto-retried after a 5xx (check the app for a duplicate before re-running).
- The API is unofficial-stability ("may change"). If a response shape surprises you, compare with `apps/hevy/API.md` and tell the user rather than guessing.
