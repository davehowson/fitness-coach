# Fitness Coach

An evidence-based workout coach for [Claude Code](https://claude.com/claude-code). It builds a training plan from a research wiki instead of from memory, and can read your history from, and publish routines to, the [Hevy](https://www.hevyapp.com) app.

- **A wiki to plan from.** `wiki/` holds the numbers: sets, reps, RIR, rest, splits, progression, deloads, conditioning, hybrid training. Each rule carries an evidence grade, so you can see what is firm and what is coaching convention.
- **Skills that run the process.** `workout-coach` takes you from intake to plan to refinement. `app-sync` connects Hevy.
- **Your data stays private.** Plans, exercise catalogs and training history go to gitignored folders, and guards stop them from being committed.
- **Nothing is written to your app without your yes.** You see the exact workouts first and choose the destination folder.

## How it works

```
 ┌─────────────┐   catalog + history    ┌───────────────┐   plan   ┌───────────────┐
 │  Hevy app   │ ─────────────────────▶ │ workout-coach │ ───────▶ │   my-plans/   │
 │ (your data) │   (app-sync, read)     │  (uses wiki/) │          │ plan + JSON   │
 └─────────────┘                        └───────────────┘          └───────┬───────┘
        ▲                                                                  │
        │            preview, your changes, your explicit yes             │
        └──────────────────────  app-sync publish  ◀───────────────────────┘
```

1. **Sync (optional).** `app-sync` pulls your exercise catalog (including custom exercises) and training history into `my-data/`. The catalog becomes the only exercise pool, so every routine can be created in the app.
2. **Intake.** The coach asks about health screen, goal, days and minutes per week, equipment, injuries and experience. Red flags (chest pain, known cardiac or metabolic disease, and so on) stop the plan and point you to clearance. It never assumes the health screen is "none".
3. **Plan.** It decides in a fixed order: goal, week, weekly sets per muscle, sessions, progression. It then scores the plan against a 14-item quality checklist and fixes any failures before showing it.
4. **Refine.** You give feedback and the coach changes the minimum needed, keeping weekly volume in range.
5. **Publish (optional).** Routines go to Hevy only after you approve them. See [Safety rules](#safety-rules).

## Quick start

You need [Claude Code](https://claude.com/claude-code) and Python 3 (standard library only). Hevy is optional but needs a **Hevy Pro** account for API access.

```bash
git clone <this repo> && cd fitness-coach
git config core.hooksPath .githooks        # enable the private-path guard

# optional, for Hevy: create a key at https://hevy.com/settings?developer
export HEVY_API_KEY=...                    # never written to disk by this repo

claude                                     # then ask: "build me a workout plan"
```

Claude Code picks up the skills in `.claude/skills/` on its own. Ask for a plan, or mention Hevy to sync first.

If you keep the key in a local `.env`, load it into your shell yourself (`set -a; . ./.env; set +a`). The CLI only reads the environment variable. `.env` is gitignored.

## Skills

| Skill | Use it to |
|---|---|
| `workout-coach` | Create, adjust or review a plan. Gathers a profile, builds from the wiki, presents session cards, progression, deload and substitutions, and iterates on feedback. |
| `app-sync` | Pull the Hevy catalog and history before planning, and publish approved routines afterwards. |

## Hevy CLI

`apps/hevy/hevy.py` is a standard-library Python CLI. The `api-key` header only ever goes to `https://api.hevyapp.com`.

| Command | What it does | Writes to Hevy? |
|---|---|---|
| `check` | Verify the key and show the account | No |
| `sync-catalog` | Cache all exercises, including custom ones, to `my-data/hevy/catalog.json` | No |
| `sync-history [--full]` | Cache workouts (full pull first, incremental after) | No |
| `summary [--weeks 12]` | Frequency, session length, weekly sets per muscle, last top set and best e1RM per exercise | No |
| `resolve "<name>"` | Find the closest catalog exercise for a name | No |
| `list-routines` | Show your folders and existing routines | No |
| `publish-routine plan.json (--folder NAME \| --root)` | Validate and **preview** routines; `--apply --approve CODE` to create them | Only with approval |
| `create-exercise ...` | Preview a custom exercise; `--apply --approve CODE` to create it | Only with approval |

Run commands as `python3 apps/hevy/hevy.py <command>`. The API contract and its limits are in [`apps/hevy/API.md`](apps/hevy/API.md).

## Safety rules

**Nothing is written to your workout app without your explicit approval.** Hevy has no delete, so a create is permanent. The agent follows these steps, and the CLI enforces the key ones:

1. Run `list-routines` and show what already exists.
2. Ask which folder the new routines go in (an existing folder, a new one, or no folder). There is no silent default.
3. Ask what to do with existing routines: leave them, or move them to an Archive folder yourself in the app. The API cannot delete, archive or move routines.
4. Run a dry run. It validates every exercise against your catalog and every set against its exercise type.
5. Show you the workouts in readable form: exercises, sets, reps, loads, rest, supersets, notes and destination.
6. Ask whether you want any changes. Loop until you have none.
7. Ask for a clear yes to exactly that content, then run `--apply --approve <code>`. The code is printed by the preview and changes whenever the workouts or destination change, so approving one version can never publish another.

Overwriting a routine with the same name (`--update`) is a separate decision with its own yes.

## Privacy

This repo is meant to be public, so personal data never enters tracked files.

| Path | Holds | Tracked? |
|---|---|---|
| `my-plans/` | Your living profile (`profile.md`), plans and generated routines files | No (gitignored) |
| `my-data/` | Hevy catalog (including your custom exercises), training history, summary | No (gitignored) |
| `.env` | Optional local API key | No (gitignored) |

- `HEVY_API_KEY` is read from the environment and never written to disk.
- A pre-commit hook (`.githooks/pre-commit`) and a CI job (`.github/workflows/private-paths.yml`) fail if anything under `my-plans/` or `my-data/` is staged or tracked. Enable the hook once per clone with `git config core.hooksPath .githooks`.
- Nothing in `my-plans/` or `my-data/` should be copied into the wiki, research notes, skills, commit messages or examples.

## Repository layout

```
.claude/skills/      workout-coach and app-sync skill definitions
wiki/                the reference the coach plans from (start at wiki/README.md and wiki/00-workflow.md)
research/            how the wiki was built: briefs, raw findings, canonical defaults, verification log
apps/                app adapters (apps/hevy/hevy.py, apps/hevy/API.md, apps/README.md)
scripts/             check-no-private-paths.sh
.githooks/           pre-commit guard
.github/workflows/   CI check for private paths
my-plans/            (gitignored) your plans
my-data/             (gitignored) your app data
```

## The wiki

Start at [`wiki/README.md`](wiki/README.md). The procedure is [`wiki/00-workflow.md`](wiki/00-workflow.md): intake, goal, weekly structure, volume and intensity, session content, progression, quality check, presentation. Numbers come from meta-analyses and position stands (ACSM 2026, WHO 2020), with an evidence grade on each rule. The sources and the verification log are in `research/`.

## Adding another app

Create `apps/<app>/` with an API notes file and a CLI that offers the same jobs (catalog, history, publish), add a row to [`apps/README.md`](apps/README.md), and extend `.claude/skills/app-sync/SKILL.md`. Any adapter must keep credentials in environment variables, keep fetched data under `my-data/`, make writes dry-run by default, and require the user's approval before applying.

## Limits and disclaimer

- This is not medical advice. It screens for red flags and defers to a clinician when any apply. It does not diagnose or treat injuries.
- The Hevy API is unofficial-stability ("may change"). If a response shape surprises you, compare it with `apps/hevy/API.md`.
- The default plans assume a healthy adult. Evidence for some groups (youth, pregnancy, obesity, frailty) is thinner, and the wiki says so where it applies.
