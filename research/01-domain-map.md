# Domain Map: What Goes Into a Good Workout

Status: **Phase 1 — pre-research understanding.** Written from prior knowledge only, before any online research. Its purpose is to define the question space so research agents can be scoped precisely. Every claim here is a hypothesis to be confirmed, refined, or corrected by Phase 2 research.

## The core question

"A good workout" is not one thing. It is a **fit between a plan and a person's inputs**. A plan is good when it:

1. Serves the stated goal (specificity).
2. Provides enough stimulus to drive adaptation (overload), but not more than the person can recover from (fatigue management).
3. Progresses over time in a defined way.
4. Fits the person's real constraints (days, time, equipment, experience, injuries).
5. Is balanced (movement patterns, muscle groups, joint health).
6. Is sustainable (adherence beats optimality).

So the LLM wiki must teach two things: **the inputs to collect** and **the decision rules that map inputs to a plan**.

## Layer 1 — Inputs (what an LLM must know about the person)

| Input | Why it matters |
|---|---|
| Primary goal (strength, hypertrophy, endurance, power, fat loss, general health, sport, hybrid) | Drives every downstream variable |
| Secondary goals | Determines blend / hybrid structure |
| Days per week available | Determines split options |
| Session length | Caps volume per session, drives superset/density choices |
| Training experience (beginner / intermediate / advanced) | Determines progression model, volume, complexity |
| Equipment access (full gym, home, bodyweight, dumbbells only) | Constrains exercise selection |
| Injuries / limitations | Exercise substitutions, contraindications |
| Age, sex, special population | Recovery capacity, emphasis, safety |
| Recovery context (sleep, stress, job) | Volume tolerance |
| Preferences / dislikes | Adherence |

## Layer 2 — Universal training principles

Hypotheses to confirm: specificity, progressive overload, SRA (stimulus-recovery-adaptation), individualization, variation, fatigue management, reversibility, minimum effective dose, adherence.

## Layer 3 — Programming variables (the "dials")

- **Volume** — sets per muscle per week; landmarks (MEV / MAV / MRV).
- **Intensity** — %1RM, RPE, RIR; proximity to failure.
- **Frequency** — sessions per muscle per week.
- **Rep ranges** — and their link to goal.
- **Rest intervals.**
- **Tempo / time under tension.**
- **Exercise selection** — compound vs isolation, movement patterns (squat, hinge, push horizontal/vertical, pull horizontal/vertical, carry, lunge/single-leg, core/anti-movement).
- **Exercise order** — big/complex first, power before strength before hypertrophy.
- **Density techniques** — supersets, circuits, drop sets, rest-pause.

## Layer 4 — Workout types / goals

Strength, hypertrophy, power, muscular endurance, cardiovascular endurance (aerobic base, threshold, VO2max), general fitness, fat loss / body recomposition, mobility, sport-specific, hybrid (strength + endurance).

## Layer 5 — Session anatomy (one workout)

Warm-up (general → specific, ramp sets) → power/explosive work → main compound lift(s) → secondary compounds → accessories/isolation → conditioning/finisher → cool-down. Time budgeting per block.

## Layer 6 — Weekly structure (splits)

Candidate splits to research: full body, upper/lower, push/pull/legs, PPL + upper/lower hybrids, body-part ("bro") split, Arnold split, torso/limbs, PHUL, PHAT, anterior/posterior, push/pull, specialization splits, hybrid strength+cardio weeks.

Key questions: how each split distributes frequency and volume, which day counts suit each, how splits combine (e.g. 5-day = upper/lower + PPL), rest-day placement, and what happens when a person misses days.

## Layer 7 — Days-per-week mapping

For each of 1, 2, 3, 4, 5, 6, 7 days: recommended split(s), per-muscle frequency achieved, volume per session, trade-offs, and how it changes with goal (pure strength vs hypertrophy vs hybrid).

## Layer 8 — Long-term structure (periodization & progression)

Linear progression, double progression, RPE/RIR autoregulation, daily undulating (DUP), weekly undulating, block periodization, conjugate, mesocycles, deloads, how progression differs beginner → advanced, plateaus.

## Layer 9 — Conditioning & hybrid

Energy systems, zone model (zone 2, threshold, VO2max), LISS vs HIIT vs SIT, polarized/pyramidal distribution, weekly cardio dose. Concurrent training: interference effect, sequencing (same day vs separate, order, gap hours), modality choice (cycling vs running), hybrid programs (e.g. HYROX, CrossFit-style, "hybrid athlete").

## Layer 10 — Individualization & special cases

Beginners, older adults, women-specific considerations, youth, injuries, time-crunched, home/minimal equipment, returning after layoff, high-stress lifestyle.

## Layer 11 — Quality control

A checklist to evaluate any generated plan: goal alignment, volume in range per muscle, frequency adequate, pattern balance (push:pull), recovery between similar sessions, progression defined, deload defined, fits time budget, substitutions given.

## Layer 12 — Reference programs

Known, proven programs as concrete templates (e.g. Starting Strength, StrongLifts 5x5, GZCLP, 5/3/1 variants, PHUL, Reddit PPL, nSuns, Texas Method). Useful as worked examples for an LLM.

## Open questions for research

- What does current evidence (meta-analyses, position stands) actually say about volume dose-response, frequency, and proximity to failure?
- Is frequency independent of volume once volume is equated?
- How real and how large is the concurrent-training interference effect, and for whom?
- What do practitioners agree on vs. where evidence is thin?
- Which numeric ranges are safe defaults an LLM can use without further research?
