# Brief 14: Exercise Library for Workout Generation

**Output file:** `research/raw/14-exercise-library.md`
**Output format:** follow `research/briefs/00-output-contract.md` sections, plus the library tables below. Read the contract, `research/01-domain-map.md`, and skim `research/raw/02-training-variables.md`, `04-session-anatomy.md` and `10-individualization.md` (do not edit them) so your library fits their terminology.

## Why
An LLM generating a workout must pick concrete exercises. It needs a structured catalog it can filter by movement pattern, target muscle, equipment, skill level and fatigue cost, without its own research.

## Scope — research all of the following
- Movement-pattern taxonomy: squat, hinge, lunge/single-leg, horizontal push, vertical push, horizontal pull, vertical pull, carry, core (anti-extension, anti-rotation, anti-lateral-flexion, flexion), plus isolation categories (biceps, triceps, lateral delts, rear delts, calves, hamstrings knee-flexion, quads knee-extension, glutes, adductors, abductors, neck/forearms optional).
- For each pattern: 6–12 exercises spanning barbell, dumbbell, machine/cable, kettlebell, bodyweight and band options.
- For every exercise give: primary muscles, secondary muscles (for fractional set counting), equipment, skill level (beginner/intermediate/advanced), systemic fatigue cost (low/medium/high), axial/spinal loading (low/medium/high), typical rep range, stimulus-to-fatigue notes, common substitutions, and safety/contraindication notes (general, non-medical).
- EMG and muscle-growth evidence on exercise selection where it exists: e.g. lengthened-position bias (overhead triceps extension, seated vs lying leg curl, incline curls), hip thrust vs squat for glutes, regional hypertrophy and need for multiple exercises per muscle (e.g. quads: squat + leg extension for rectus femoris).
- Which exercises are best as "main lifts" vs accessories; which are good for supersets.
- Plyometric and power exercises (jumps, throws, Olympic-lift derivatives) with skill and fatigue notes.
- Conditioning exercises/modalities for metcons and finishers (sled, rower, bike, burpees, kettlebell swings), with impact level.
- Mobility/warm-up drills commonly used in the RAMP warm-up.

## Required library table format
Per pattern:
| Exercise | Equipment | Primary | Secondary | Skill | Fatigue | Axial load | Reps | Role (main/secondary/accessory) | Substitutes | Notes |

## Rules
- Cite sources (12+), grade evidence for selection claims. Write ONLY `research/raw/14-exercise-library.md`. No git commits. No medical treatment advice.

## Done when
Every pattern has a populated table; the evidence section covers the selection findings above; 12+ sources with URLs.
