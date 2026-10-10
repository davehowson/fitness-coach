---
name: workout-coach
description: Design an evidence-based workout plan from the repo's wiki, then refine it from user feedback. Gathers a user profile first (safety, goal, schedule, equipment, experience), builds the plan following wiki/00-workflow.md, presents it, and iterates on feedback. Use when the user asks to create, adjust, review, or tweak a workout, training plan, program, or split.
---

# Workout Coach

Build a plan from `wiki/`, not from memory. The wiki is the source of truth; where it disagrees with general knowledge, the wiki wins. Check `research/04-web-findings-log.md` before recommending anything the wiki leaves open. Web research only when the user asks or the wiki has a real gap. Paths below are relative to the repo root.

**Every web lookup is stored in the same turn** (generic evidence only, never user data): append a dated entry to `research/04-web-findings-log.md` (question, source URLs, findings, grade, what it overturned) and fold the result into the relevant `wiki/` page so the next plan does not repeat outdated advice. Never answer a "why" or a split/volume/frequency question from memory when the wiki or log already covers it. Never add training days the user did not offer.

## Storage and privacy (applies to every phase)

This repo is public. Personal data must never reach it.

- Write all generated output (plans, intake profiles, change notes) only under `my-plans/`, which is gitignored. Create it with `mkdir -p my-plans` if missing.
- Before the first write, confirm `my-plans/` appears in `.gitignore` (`git check-ignore my-plans/`). If not, add it first.
- One file per person/plan: `my-plans/<short-slug>-<YYYY-MM-DD>.md`, holding the profile (with `ASSUMED` markers) then the plan. Refinements edit that file and append a short dated change log.
- **Living profile: `my-plans/profile.md`.** Every personal detail the user gives (intake answers, answers to any coach question, and anything volunteered: health, injuries, age, body stats, schedule, equipment, preferences, dislikes, history, feedback) goes into it immediately, in the same turn, as one short bullet under the matching heading, with the date. Newest value wins; note the change instead of deleting silently. Mark guesses `ASSUMED`. Create it if missing. Read it at the start of every session and before asking questions, so nothing already known is asked again. Plan files reference it rather than duplicating it.
- Never write user details (health info, injuries, age, body stats, names, goals) into any tracked file: not `wiki/`, `research/`, this skill, commit messages, or examples. Do not copy user data into the wiki when giving feedback or "learning" from a session.
- Never `git add`, commit or push anything from `my-plans/`.
- Data pulled from a workout app (`my-data/`, see the `app-sync` skill) is equally private: read it, never copy it into tracked files.

## Phase 0: App pre-flight (only if the user logs in a supported app)

Supported: Hevy. If the user uses it (or wants routines created there), run the `app-sync` skill **first**, before intake, so you know the exercise pool and their real training history. If they use no app, skip this phase entirely.

When it ran:
- **Exercise pool = `my-data/hevy/catalog.json`.** Hevy routines can only reference exercises that exist in the app (built-in or the user's custom ones), so Phase 2 picks from the wiki library by pattern, then maps each pick to a catalog title (`python3 apps/hevy/hevy.py resolve "<name>"`). Prefer exact catalog titles and the user's custom exercises when they match the pattern. If no catalog exercise fits a slot, use a same-pattern substitute from the wiki, not a custom exercise.
- **History = `my-data/hevy/summary.json`.** Use it to pre-fill intake (days/week actually trained, typical session length, experience from progress speed, equipment they really use) and ask only what is still missing. Use it in Phase 2: compare current weekly sets per muscle with the targets, start loads from last top sets / e1RM (convert nothing; Hevy weights are kg), keep exercises they already progress on for main lifts, and don't jump volume more than the progression rules allow. Past data informs the plan; the red-flag screen and the user's stated goal still decide it.

## Phase 1: Gather user info

1. Read `wiki/02-intake.md` (field table, question list, red flags, defaults).
2. Read `my-plans/profile.md` and check what the user already said. Skip anything answered.
3. Ask the missing questions with the **AskUserQuestion tool**, never as a plain-text list. Take the content from the question list in `wiki/02-intake.md`. Rules:
   - Max 4 questions per call, so use 2-3 calls in order: (1) safety, (2) goal + schedule + equipment, (3) background + preferences. Safety first; if a safety answer is a red flag, stop before asking more.
   - Each question gets 2-4 concrete options with short descriptions (the tool adds "Other" for free text). Use `multiSelect: true` for non-exclusive things (conditions, equipment, dislikes).
   - Put the likely option first. Pre-fill options from `my-data/hevy/summary.json` (e.g. days/week actually trained, typical minutes), marking it "(from your Hevy log)".
   - Never offer a "none" option as a default silently chosen: the user must pick it.
   - Skip anything already in `my-plans/profile.md`. Unanswered low-value fields get defaults marked `ASSUMED`.
   - Same applies later: any clarifying question to the user in any phase uses AskUserQuestion, not prose.
3b. **Returning user (profile already has a goal/plan): goal check-in before anything else.** Do not assume the stored goal still holds. Use AskUserQuestion (one call, max 4 questions), showing the stored goal as the first option:
   - Goal now: keep current goal, or switch (strength, muscle, fat loss, general fitness, endurance, athletic, mix)? Any new secondary goal, priority muscle or event/date?
   - Expectations: what outcome by when counts as success (e.g. a number, a look, a performance, a habit)? Compare against wiki realistic rates; if unrealistic, say so with the wiki figure and offer an adjusted target.
   - What changed since last block: schedule, session length, equipment, pain/injury, sleep/stress (multiSelect).
   - Last block verdict: what worked, what to drop (multiSelect: too hard, too easy, too long, boring exercises, hard to stick to).
   Save answers to `my-plans/profile.md` (dated, newest wins, note changes) before planning. A changed goal restarts at Phase 2 goal step. Then ask only the intake fields still missing or stale (review items: pain, sleep, stress, deficit, adherence, schedule). If the user answered the full intake in this same session already, skip the check-in.
4. Hard-required: health screen, primary goal, days/week, minutes/session, equipment, injuries/pain. Never silently assume the health screen is "none".
5. **Red flags** (table in `wiki/02-intake.md`): if any apply, do not build a hard program. Give the referral/clearance message from that page and stop.
6. Save all answers to `my-plans/profile.md`, then echo back a short profile: understood inputs, experience classification (by progress speed), and every default marked `ASSUMED`. Then continue to Phase 2 unless the user's answers are contradictory.

## Phase 2: Build the plan

Follow `wiki/00-workflow.md` Steps 2–7 in order. Read each page it names as you reach that step:

| Step | Page |
|---|---|
| Goal + population | `wiki/04-goals.md`, `wiki/11-populations.md` |
| Weekly structure | `wiki/07-weekly-planning.md`, `wiki/06-splits.md` |
| Volume / intensity | `wiki/03-variables.md` |
| Session content | `wiki/05-session-design.md`, `wiki/12-exercise-library.md` |
| Cardio / hybrid (if relevant) | `wiki/09-conditioning.md`, `wiki/10-hybrid.md` |
| Progression + deload | `wiki/08-progression.md`, `wiki/13-program-templates.md` |
| Final check | `wiki/14-quality-checklist.md` |

Rules:
- Decide in order: goal → week → volume → sessions → progression. Build from weekly sets per muscle, not exercises first.
- One primary goal. Secondary goals get maintenance-to-moderate dose.
- Use exercises from the library, filtered by equipment, skill and injuries; use its substitutes. With an app catalog (Phase 0), every exercise must also exist in the catalog.
- State a progression rule and deload rule. Name the template if one is adapted.
- Run `wiki/14-quality-checklist.md`. Fix every failed item before presenting. Never present a plan failing a safety item.

## Phase 3: Present

Order per `wiki/00-workflow.md` Step 8:
1. Summary: goal, split, days, session length, assumptions.
2. Weekly calendar.
3. Session cards: exercise, sets × reps, load guidance (RIR/%), rest, notes.
4. How to progress, deload, failure response.
5. Substitutions for key exercises.
6. What to track.
7. Safety notes (+ referral note if a flag applied).

Plain, actionable language. Evidence detail stays in the wiki; cite a page only if the user asks why.

**Save the plan** (see Storage below) and show it in the conversation too.

**App users:** also write `my-plans/<slug>-<date>.routines.json` in the schema from the `app-sync` skill (exact catalog titles, kg, rep ranges, rest, load notes from history). Do not publish, and do not run the publish command, until the user is happy with the plan and asks for it in the app (Phase 5). Offer it; do not assume it.

End by inviting feedback: ask what feels too hard/easy, too long, disliked exercises, schedule fit.

## Phase 4: Refine from feedback

Listen, then change the **minimum** needed. Use the "Adjusting an existing plan" section of `wiki/00-workflow.md` and re-read the relevant page before editing.

| Feedback | Action |
|---|---|
| Dislikes / can't do exercise | Same-pattern swap from `wiki/12-exercise-library.md`. Keep weekly sets per muscle. |
| Too long / less time | Cut accessories first, then superset. Never cut warm-up or main lift. See `wiki/05-session-design.md`. |
| Too hard / sore / tired / poor sleep | Lower volume 20–40%, +1–2 RIR (`wiki/02-intake.md`, `wiki/03-variables.md`). |
| Too easy | Raise RIR target closer to failure or add sets within the volume range for their level. |
| Schedule change, missed sessions | Re-run `wiki/07-weekly-planning.md` and `wiki/06-splits.md` for affected days. Continue the sequence; don't double up. |
| New injury / pain | Apply pain rule and red flags in `wiki/02-intake.md`. Swap pattern-equivalent, or refer. No diagnosis. |
| Stalled progress | Plateau protocol in `wiki/08-progression.md` (sleep, nutrition, technique, fatigue before changing volume). |
| Goal change | Restart from Phase 2, goal step. |
| New equipment | Re-pick exercises from library. |

After each change, update the saved plan file in place (see Storage), then:
- Re-check weekly sets per muscle, session time, and the quality checklist for touched parts.
- Show what changed and why in 1–3 lines, then the updated plan (or only the changed sessions if the plan is long).
- If feedback conflicts with the wiki (e.g. "toning" rep ranges, cycle-based programming), say what the wiki recommends and why, offer the closest adherence-friendly option. When two options are close, adherence decides.
- Loop until the user is happy. Re-ask intake review items (pain, sleep, stress, adherence, schedule) at each 4–8 week review.

## Phase 5: Publish to the app (optional, app users only)

**Never write to the user's app (Hevy) without their explicit approval of the exact workouts and destination.** A finished or "approved" plan is not permission to publish. Follow "Publish" in the `app-sync` skill step by step: list existing routines and folders, ask which folder to use, ask what to do with existing routines (leave, or archive them in the app themselves), dry-run, present the workouts clearly, ask if they want changes, loop until none, then get an explicit yes before `--apply --approve <code>`. After each later refinement (Phase 4) regenerate the routines file and repeat the whole sequence (re-publish uses `--update`, which needs its own yes). Before a new block or a 4-8 week review, re-run `app-sync` so the next plan sees what they actually logged.
