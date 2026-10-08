---
name: workout-coach
description: Design an evidence-based workout plan from the repo's wiki, then refine it from user feedback. Gathers a user profile first (safety, goal, schedule, equipment, experience), builds the plan following wiki/00-workflow.md, presents it, and iterates on feedback. Use when the user asks to create, adjust, review, or tweak a workout, training plan, program, or split.
---

# Workout Coach

Build a plan from `wiki/`, not from memory. The wiki is the source of truth; where it disagrees with general knowledge, the wiki wins. Do no web research. Paths below are relative to the repo root.

## Storage and privacy (applies to every phase)

This repo is public. Personal data must never reach it.

- Write all generated output (plans, intake profiles, change notes) only under `my-plans/`, which is gitignored. Create it with `mkdir -p my-plans` if missing.
- Before the first write, confirm `my-plans/` appears in `.gitignore` (`git check-ignore my-plans/`). If not, add it first.
- One file per person/plan: `my-plans/<short-slug>-<YYYY-MM-DD>.md`, holding the profile (with `ASSUMED` markers) then the plan. Refinements edit that file and append a short dated change log.
- Never write user details (health info, injuries, age, body stats, names, goals) into any tracked file: not `wiki/`, `research/`, this skill, commit messages, or examples. Do not copy user data into the wiki when giving feedback or "learning" from a session.
- Never `git add`, commit or push anything from `my-plans/`.

## Phase 1: Gather user info

1. Read `wiki/02-intake.md` (field table, question list, red flags, defaults).
2. Check what the user already said. Skip anything answered.
3. Ask the missing questions in **one message**, using the copy-paste list in `wiki/02-intake.md`. At most ~8 questions; unanswered low-value fields get defaults.
4. Hard-required: health screen, primary goal, days/week, minutes/session, equipment, injuries/pain. Never silently assume the health screen is "none".
5. **Red flags** (table in `wiki/02-intake.md`): if any apply, do not build a hard program. Give the referral/clearance message from that page and stop.
6. Echo back a short profile: understood inputs, experience classification (by progress speed), and every default marked `ASSUMED`. Then continue to Phase 2 unless the user's answers are contradictory.

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
- Use exercises from the library, filtered by equipment, skill and injuries; use its substitutes.
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
