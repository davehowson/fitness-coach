# Workflow: From Request to Plan

> Purpose: the step-by-step procedure for generating a workout plan. Each step names the page that holds the rules.
> Use when: any request to create, adjust or review a workout or training plan.
> Depends on: every other page in this wiki.

## Key rules (TL;DR)

1. Never write a plan before you know at least: **goal, days/week, session length, experience, equipment, injuries.** Ask, or state the defaults you are assuming.
2. Decide in this order: **goal → weekly structure → volume → session content → progression → check.** Later choices depend on earlier ones.
3. Pick **one** primary goal. Secondary goals get a maintenance-to-moderate dose.
4. Build the week from **weekly sets per muscle**, then split those sets across sessions. Don't pick exercises first.
5. Every plan must state its **progression rule** and its **deload rule**.
6. Run the [quality checklist](14-quality-checklist.md) and fix every failed item before returning the plan.

## Step 1: Intake → [02-intake.md](02-intake.md)

Collect the required fields. If the person can't or won't answer, use the defaults from the intake page and **say what you assumed** in the output. Screen for red flags; if any apply, recommend medical clearance before (or alongside) the plan.

**Output of this step:** a filled intake profile.

## Step 2: Set the goal → [04-goals.md](04-goals.md)

- Map the person's words to a goal type ("tone up" usually → hypertrophy + fat loss; "get fit" → general fitness; "run a 10K and stay strong" → hybrid, endurance-primary).
- Check goal compatibility. If goals compete (e.g. max strength + marathon), pick a primary for this block and plan the other at a lower dose.
- Apply population adjustments from [11-populations.md](11-populations.md) (experience level, age, constraints).

**Output:** primary goal, secondary goal(s), experience level, population modifiers.

## Step 3: Choose weekly structure → [07-weekly-planning.md](07-weekly-planning.md), [06-splits.md](06-splits.md)

- Use days/week and session length to choose a split from the days-per-week playbook. Default to the top-ranked option for the goal.
- Place rest days so heavy sessions with the same pattern are never on back-to-back days.
- If there is cardio or a hybrid goal, place endurance sessions per [10-hybrid.md](10-hybrid.md) and [09-conditioning.md](09-conditioning.md).
- If the schedule is irregular, use a rolling (sequence-based) split instead of fixed weekdays.

**Output:** a Mon–Sun calendar with session types.

## Step 4: Set volume and intensity → [03-variables.md](03-variables.md)

- Set the weekly hard-set target per muscle from the goal and experience level.
- Divide by sessions per muscle to get sets per muscle per session. Stay ≤10 fractional sets per muscle per session; if you'd exceed that, add a session or lower the target.
- Set rep ranges, RIR and rest per exercise role (main lift / secondary / accessory).

**Output:** a sets/reps/RIR/rest target per muscle and per session.

## Step 5: Build each session → [05-session-design.md](05-session-design.md), [12-exercise-library.md](12-exercise-library.md)

- Order the session: warm-up → power (if any) → main lift → secondary compound → accessories → core → conditioning.
- Pick exercises by movement pattern, filtered by equipment, skill level and injuries. Cover every major pattern across the week. Use the library's substitutes for anything the person can't do.
- Check the time budget. If a session is too long, cut accessories first, then use supersets. Never cut the main lift or the warm-up.
- Count fractional sets (indirect = 0.5) to confirm the weekly targets are met.

**Output:** full session cards: exercise, sets × reps, load guidance (RIR or %), rest, notes.

## Step 6: Add progression → [08-progression.md](08-progression.md)

- Pick the progression model by experience: beginners use linear progression on main lifts; intermediates use double progression or weekly progression; advanced lifters use block or undulating periodization.
- Define the mesocycle length, the weekly volume/RIR ramp, the deload, and what to do when the person fails to progress.
- If a known program fits the profile well, use it or adapt it from [13-program-templates.md](13-program-templates.md) and name it.

**Output:** a progression rule per exercise type, a mesocycle outline, deload rules, and a failure response.

## Step 7: Check quality → [14-quality-checklist.md](14-quality-checklist.md)

Score the plan. Fix every failed item, then re-check. Don't return a plan that fails a safety item.

## Step 8: Present the plan

The output should contain, in this order:
1. **Summary:** goal, split, days, session length, and the assumptions you made.
2. **Weekly calendar.**
3. **Session cards** (Step 5 format).
4. **How to progress**, plus the deload and failure rules.
5. **Substitutions** for key exercises.
6. **What to track:** load, reps, RIR, and session notes.
7. **Safety notes**, plus a referral note if any red flag applied.

Keep the plan's language plain and actionable for the person. The evidence detail stays in this wiki; the plan only needs the result.

## Adjusting an existing plan

- **Missed sessions:** continue the sequence; don't double up (see [06-splits.md](06-splits.md)).
- **Stalled progress:** follow the plateau protocol in [08-progression.md](08-progression.md) (check fatigue, sleep, nutrition and technique before changing volume or exercises).
- **New constraint** (injury, less time, new equipment): re-run Steps 3–7 for the affected sessions only.
- **Goal change:** start from Step 2.
