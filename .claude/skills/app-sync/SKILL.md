---
name: app-sync
description: Pull the exercise catalog and training history from the user's workout app (currently Hevy only) into the private, gitignored my-data/ folder, so the workout-coach skill can build plans from exercises the app actually supports and from what the user really did. Run before workout-coach whenever the user logs workouts in a supported app, and again after a plan to publish it. Use when the user mentions Hevy, wants routines created in an app, or wants their workout history considered.
---

# App Sync

Runs **before** `workout-coach` (pre-flight) and **after** it (publish, only with the user's approval). Supported app: **Hevy**. Contract and limits: `apps/hevy/API.md`. Adapter layout: `apps/README.md`. Paths are relative to the repo root.

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

## Publish (hard rule: never write to the app without the user's explicit approval)

Every write to Hevy (routines, folders, custom exercises) is permanent: Hevy has no delete. **Never write because a plan was approved, because the user said "build it", or because a permission mode allows it.** The user must see the exact workouts and say yes to them. The CLI enforces this (dry run by default; `--apply` also needs `--approve <code>` printed by the preview, and the code changes whenever the content or destination changes). Never pass `--approve` on the user's behalf or before they have answered.

Steps, in order. Do not skip or reorder:

1. `workout-coach` writes `my-plans/<slug>-<date>.routines.json` (schema below). No `folder` field: the destination is chosen with the user.
2. **Look at what is already in the account:** `python3 apps/hevy/hevy.py list-routines` (read-only). Tell the user what exists: folders, and routines sitting in "My Routines".
3. **Ask where to put the new routines** (use AskUserQuestion). Options: an existing folder (name them), a new folder (suggest a name such as the plan name), or "My Routines" with no folder. Never default silently: users keep their data in folders.
4. **If routines already exist, ask what to do with them** (AskUserQuestion): leave them alone; or archive/separate them. The API cannot delete, archive or move routines (`PUT` replaces contents and its folder behaviour is undocumented), so do not try. If the user wants them tidied, tell them to move them into an "Archive" folder in the Hevy app themselves (long-press the routine, then Move), and recommend putting the new plan in its own folder so nothing mixes. Wait for them before continuing if they choose that.
5. **Dry run:** `python3 apps/hevy/hevy.py publish-routine my-plans/<file>.routines.json --folder "<name>"` (or `--root`). It validates every exercise against the catalog and every set against the exercise type, refuses to duplicate an existing routine title, and prints a full preview and an approval code.
6. **Present the workouts to the user in plain, readable form** (do not just paste raw output): a table per routine with exercise, sets x reps, load, rest, supersets, and notes; where they will be created (folder, new or existing); what already exists there; and the permanence warning (no delete). Lead with the destination.
7. **Ask if they want any changes** before anything is written: exercises, loads, rep ranges, session length, folder, names. If they want changes, edit the routines file, re-run the dry run, present again, and ask again. Loop until they have no more changes.
8. **Ask for a clear, explicit yes to publish exactly this** ("Create these 3 routines in folder X?"). Silence, "looks good" about the plan content, or approval of an earlier version is not a yes to the write.
9. Only then run the same command with `--apply --approve <code>`. If the code is rejected, something changed: go back to step 5.
10. `--update` (overwrite a same-named routine) is a separate decision: name the routine it would replace, state that the old contents are lost, and get a separate yes.
11. Never create custom exercises silently. If something is missing, first swap to a same-pattern exercise in the catalog (`python3 apps/hevy/hevy.py resolve "<name>"`). Only if nothing fits, propose `create-exercise` (dry run; permanent and uneditable), show the user, and get a yes before `--apply --approve <code>`.

### Routines file schema
```json
{ "routines": [ { "title": "Upper A", "notes": "optional",
    "exercises": [ { "exercise": "Bench Press (Barbell)",
        "rest_seconds": 120, "notes": "Last time: 80 kg x 8", "superset_id": null,
        "sets": [ { "type": "warmup", "reps": 10, "weight_kg": 40 },
                  { "type": "normal", "reps": [6, 8], "weight_kg": 80 } ] } ] } ] }
```
- The destination folder is **not** in this file; it is chosen with the user at publish time (`--folder`/`--root`).
- `exercise` must equal a catalog title exactly (or give `template_id`). Weights are **kg**.
- `reps` is an int or `[low, high]` (becomes Hevy's rep range). Timed exercises use `duration_seconds` instead.
- `type`: `warmup | normal | failure | dropset`. Leave `weight_kg` null when there is no history to anchor a load.

## Failure handling
- 401: bad key or not Pro. 403 on create: account's routine/custom-exercise limit reached; report it, don't retry. 400 on list: page size too large (client already caps). 429/5xx on reads are retried automatically; creates are never auto-retried after a 5xx (check the app for a duplicate before re-running).
- The API is unofficial-stability ("may change"). If a response shape surprises you, compare with `apps/hevy/API.md` and tell the user rather than guessing.
