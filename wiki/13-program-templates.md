# Program Templates

> Purpose: pick and adapt a proven reference program (goal × level × days/week) and output all four parts of a program: session template, weekly schedule, progression rule, failure/reset rule.
> Use when: the user names a program, asks for a "proven" template, or you need a worked example to sanity-check a generated plan.
> Depends on: [splits](06-splits.md), [progression](08-progression.md), [weekly planning](07-weekly-planning.md), [exercise library](12-exercise-library.md), [conditioning](09-conditioning.md), [hybrid](10-hybrid.md), [populations](11-populations.md)

## Key rules (TL;DR)

1. A program = (a) session template (lifts × sets × reps × load rule), (b) weekly schedule, (c) progression rule, (d) failure/reset rule. Always output all four, plus the deload.
2. Reference programs are **worked examples, not gospel**. Nearly all successful ones share one skeleton: few big compounds, 2–3 exposures/week per main lift, a numeric progression rule, a predefined failure response. `Practitioner`
3. **True beginner (progress session to session) → full-body A/B, 3 days, linear progression**: +2.5 kg / 5 lb upper, +5 kg / 10 lb lower per session, defined reset on failure (canonical default).
4. When resets stack up on 2–3 lifts → move to weekly progression (Texas Method, Madcow) or cycle-based (5/3/1). Never run linear progression forever without a reset rule.
5. **Hypertrophy programs** (PHUL, PHAT, Reddit PPL, RP-style): ≥2×/week per muscle, double progression on accessories, volume ramps across a 4–8 week mesocycle (default 5 working + 1 deload), then deload. Volume targets come from [variables](03-variables.md), not from the program's marketing.
6. **Do not hand novices advanced programs** (nSuns 6-day, PHAT, Sheiko) because they "have more volume".
7. **Apply the version corrections below.** Program details drift between sources; name the version and mark unverified parts.
8. Deadlift gets less volume than squat/bench in beginner linear programs (1×5) because of its fatigue cost.
9. AMRAP sets should leave reps in reserve (stop when bar speed slows), not be taken to true failure every session.
10. Never mix rule sets (e.g. 5/3/1 percentages with StrongLifts increments).
11. Sedentary, older, medical-condition or pain users: do not assign these programs unmodified; lower volume, 3 RIR, refer for screening ([populations](11-populations.md)). No medical advice.

## Program model families

| Family | Rule | Used by |
|---|---|---|
| Session-to-session linear progression (LP) | Add fixed load every workout while all reps are completed; beginners only | Starting Strength, StrongLifts, GZCLP, Greyskull, Reddit PPL |
| Weekly linear | Load rises once per week; heavy/light/medium days | Texas Method, Madcow |
| Cycle-based training max (TM) waves | % of TM changes within a 3-week wave; TM bumps per cycle (TM ≈ 90% of estimated 1RM) | 5/3/1 family |
| AMRAP-driven autoregulation | Rep performance on a top set sets the next jump | nSuns, Greyskull, GZCL |
| Double progression | Add reps within a range; add load when the top of the range is hit on all sets (at target RIR) | Accessories in PHUL/PHAT/PPL, bodyweight RR |
| Block / phase periodization | Phases of different emphasis then peak/test | Candito, Sheiko, RP mesocycles |
| Distance/time progression | Gradual time/distance, cutbacks, taper | Couch to 5K, Higdon |

Vocabulary: AMRAP ("5+" = at least 5, as many as possible); TM = training max; FSL = first set last (5×5 at the week's first-set %); T1/T2/T3 = GZCL tiers; RIR/RPE per [variables](03-variables.md).

## Archetype selector (goal × level × days/week → program)

| Goal | Level | Days/wk | Pick | Notes |
|---|---|---|---|---|
| Strength | Beginner | 3 | Starting Strength / StrongLifts 5x5 / GZCLP / Greyskull (Phrak variant) | GZCLP if more volume and back work wanted |
| Strength | Beginner | 4 | GZCLP (4-day rotation) or StrongLifts Ultra (upper/lower) [3][14] | |
| Strength | Early intermediate | 3 | 5/3/1 for Beginners, Texas Method, Madcow | |
| Strength | Intermediate | 4 | 5/3/1 BBB, nSuns 4-day | start with 4-day nSuns |
| Strength | Intermediate–advanced | 5–6 | nSuns 5/6-day | high fatigue; needs recovery capacity |
| Strength peaking | Intermediate–advanced | 4–5 | Candito 6-week, Sheiko | competition prep only; not for recreational lifters |
| Hypertrophy | Beginner | 3 | Nippard-style full body, GZCLP + accessories, 5/3/1 for Beginners | |
| Hypertrophy | Intermediate | 4 | PHUL (unverified original) or upper/lower | |
| Hypertrophy | Intermediate | 5 | PHAT | |
| Hypertrophy | Beginner–intermediate | 6 (or 3) | Reddit PPL | |
| Hypertrophy | Intermediate–advanced | 4–6 | RP-style mesocycle | |
| Aerobic base | No running base | 3 | Couch to 5K | |
| Marathon | Established runner (3–4 d/wk, 15–20 mi/wk for 1–2 yr) | 4 runs + 1 XT | Higdon Novice 1 | prerequisite is a base, not "can run 30 min" |
| Bodyweight / no equipment | Beginner–intermediate | 3 | r/bodyweightfitness Recommended Routine; Convict Conditioning | |
| Strength + endurance | Intermediate | 5–6 | Hybrid week: 2–3 lift + 2–3 run | see [hybrid](10-hybrid.md) |

## Recurring numeric ranges

| Variable | Typical in programs | Note |
|---|---|---|
| Beginner main-lift sets × reps | 3×5, 5×5 (deadlift 1×5) | |
| LP increments | upper +2.5–5 lb (+1–2.5 kg); lower +5–10 lb (+2.5–5 kg) | canonical default: +2.5 kg / 5 lb upper, +5 kg / 10 lb lower |
| Reset after failure | −5 to −15% (typically −10%) | exact trigger differs by program (see each) |
| 5/3/1 TM | 90% of estimated 1RM | |
| 5/3/1 TM jump | +5 lb upper / +10 lb lower per 3-week cycle | |
| Power-day reps (PHUL, PHAT) | 3–5 | |
| Hypertrophy-day reps | 8–12 compounds, 12–20 isolation | |
| Rest | strength 3–5 min heavy, 2–3 min assistance, hypertrophy 60–90 s (programs); canonical defaults 3 min heavy / 2 min compound / 90 s isolation | use [variables](03-variables.md) |
| Mesocycle before deload | 4–8 weeks (default 5 working + 1 deload) | RP-style sources say 4:1–6:1 `Practitioner` |

## Program catalog

Verification status labels: **Verified** = original/official page or archived original read; **Verified (wiki)** = r/Fitness wiki companion to the original; **Secondary** = aggregator/app only; **Unverified** = original not retrieved.

### 1. Starting Strength (Rippetoe) — Verified (official site, archived 2024) [9][11]

- **Goal / level / days:** strength, novice, 3 non-consecutive days (Mon/Wed/Fri).
- **Split:** full body, Day A / Day B alternating.
- **Structure:**
  - Phase 1 (usually 1–3 weeks): squat 3×5, press **or** bench 3×5, deadlift 1×5, on both days.
  - Phase 2: Day B swaps deadlift for power clean 5×3; Day A keeps deadlift 1×5.
  - Phase 3: Day A alternates deadlift 1×5 and power clean 5×3; Day B adds chin-ups (3 sets to fatigue; weighted 3×5 once 3×10 bodyweight is reached). "Advanced novice": squat load rises only twice weekly with a lighter Wednesday squat.
  - **Press and bench alternate every session** (squat is 3×5, not 5×5).
- **Progression:** add weight every session. Healthy men 18–35/40: +10 lb squat first 2–3 sessions, +15–20 lb deadlift first sessions then +10 lb, then +5 lb/workout; press/bench/power clean start with one 10 lb or 5 lb jumps, later 2.5 lb or smaller. Women and older lifters: smaller jumps. Expected by end of Phase 1 (male 18–35): squat +40–50 lb, deadlift +50–70 lb, press/bench +15–20 lb.
- **Reset / failure:** a reset is a 5–10% load drop with no programming change. **Second consecutive failure at the same load → 5% reset and make Day 2 a light squat day (80% × 2×5)**; if already doing that, switch to 5×3. First missed-rep session: repeat the load; if ≥4 reps on the first two sets retry 3×5; if ≤3, same load at 5×3 with 2.5 lb jumps. Layoff: 1 week = repeat last workout; longer = reset 5% (<40 y) or 10% (>40 y); 3–4 weeks = 10%. After a failed repeat/reset, change programs (e.g. Texas Method) instead of resetting again.
- **Strengths:** simple, minimal exercises, fast early strength. **Criticisms:** little back/pulling volume before Phase 3; no hypertrophy accessory work; ends quickly for trainees who adapt slowly.
- **Correction applied:** "3 failed sessions → reset" is **wrong for Starting Strength** (it is StrongLifts/PPL).

### 2. StrongLifts 5x5 (Mehdi) — Verified (official site) [12][13][14]

- **Goal / level / days:** strength, novice, 3 (Mon/Wed/Fri), full-body A/B, ~3 min between sets.
- **Structure:** A: squat 5×5, bench 5×5, barbell row 5×5. B: squat 5×5, overhead press 5×5, **deadlift 1×5**. Start with the empty 45 lb bar (squat/bench/OHP), ~65–95 lb rows/deadlift.
- **Progression:** +5 lb (2.5 lb/side) when all sets are completed ("5 lb or less"); microloading endorsed.
- **Reset / failure:** repeat the weight; if you repeat it three times and still fail → deload ~10% and work back up. ("Every 5th week 50%" is a generic 5x5 variant, not official.)
- **Next steps (official):** Plus, Ultra (4-day upper/lower), Ultra Max, Intermediate, Madcow, Lite, Mini.
- **Strengths:** includes rows; clear rule. **Criticisms:** 5×5 squat every session accumulates fatigue; overhead press and bench often stall first.

### 3. GZCLP (LeFever) — Verified (wiki) [15]

- **Goal / level / days:** strength + some size, novice, 3 non-consecutive days/week rotating through a 4-day cycle (A1/B1/A2/B2).
- **Day layout:** D1: T1 squat, T2 bench, T3 lat pulldown. D2: OHP / deadlift / DB row. D3: bench / squat / lat pulldown. D4: deadlift / OHP / DB row.
- **Stages:** T1 5×3+ → 6×2+ → 10×1+; T2 3×10 → 3×8 → 3×6; T3 3×15+ only. Last set of "+" sets is AMRAP leaving 1–2 reps in reserve. Rest: T1 3–5 min, T2 2–3, T3 1–1.5.
- **Progression:** after each workout +5 lb bench/OHP, +10 lb squat/deadlift (T1/T2). T3: add weight when 25 reps are reached on the AMRAP set.
- **Reset / failure:** fail → next stage. After the last T1 stage, test a new 5RM and restart at 85%. T2: restart at the last stage-1 weight +15–20 lb.
- **Strengths:** back work built in; autoregulating; flexible. **Criticisms:** more complex bookkeeping; T-tier stage details vary slightly between wiki and app versions `Contested`.

### 4. Greyskull LP (Sheaffer; Phrak variant) — Unverified at original; secondary only [16]

- **Goal / level / days:** strength + size, novice, 3 days, full-body A/B.
- **Structure:** main lifts 2×5 + final set 5+ (AMRAP); deadlift 1×5+.
- **Progression (Phrak variant, not original):** upper +2.5 lb / lower +5 lb per session; double jump when ≥10 reps on the AMRAP set.
- **Reset:** Phrak variant: miss 5 on the final set → −10%. The original lacked back work; Phrak adds chins + rows.
- **Status:** original Sheaffer increments not confirmed. **Label every number as "Phrak variant, unverified original". Do not present as official.**

### 5. 5/3/1 for Beginners (Wendler) — Verified (wiki companion); Wendler's original article not retrieved [17]

- **Goal / level / days:** strength, novice–early intermediate, 3 days, full body, two main lifts/day (Mon squat + bench; Wed deadlift + OHP; Fri bench + squat).
- **Structure:** per lift ≈ 8 sets (3 optional warm-up + 3 core + 5×5 FSL); third core set AMRAP. Assistance: one push, one pull, one single-leg/core, **50–100 reps each**.
- **Waves (% of TM):** W1 65/75/85 × 5,5,5+ then 5×5 @65%. W2 70/80/90 × 3,3,3+ then 5×5 @70%. W3 75/85/95 × 5,3,1+ then 5×5 @75%.
- **TM:** start at **90% of estimated 1RM** (from a 3–5 rep max with good bar speed). Increase +5 lb upper / +10 lb lower per 3-week cycle regardless of AMRAP performance.
- **Wiki additions (not in Wendler's original):** stall rule = lower TM by three cycle increments (15 lb upper / 30 lb lower); TM-test week every ~10th week. Mark both as **r/Fitness wiki additions**.
- **Strengths:** conservative, long-lasting, low burnout. **Criticisms:** slow for true novices who can still add weight every session; AMRAP discipline required.

### 6. 5/3/1 BBB (Boring But Big; Wendler) — Verified (Wendler's page) [18]

- **Goal / level / days:** size + strength, intermediate, 4 days, one main lift/day.
- **Structure:** 5/3/1 main sets + **5×10** of the same lift (Example 1) or the opposite lift (Example 2: press→bench, deadlift→squat, bench→press, squat→deadlift), plus lat work on upper days or abs on lower days.
- **Load:** 5×10 at **50–60% of TM**; new BBB lifters (especially lower body) start ~**30% TM**. Ascending/descending/up-down set variations exist.
- **Progression / deload:** TM +5/+10 lb per cycle; deload per 5/3/1 (Forever uses leaders/anchors [16]).
- **Strengths:** high volume at low intensity, size carryover. **Criticisms:** high recovery cost on the lower-body 5×10; fatigue if started at 60% TM.

### 7. Texas Method (Rippetoe) — structure Verified (Barbell Medicine reproduction); 90% figure Unverified [19]

- **Goal / level / days:** strength, intermediate, 3 days, full body.
- **Week:**
  - Day 1 Volume: squat 5×5, bench 5×5 (alternating with press 5×5 week to week), deadlift 1×5.
  - Day 2 Light: squat 2×5 @ 80% of Day 1, press 3×5 (or bench 3×5 @ 90% of last week's Day 1), chins, back extensions.
  - Day 3 Intensity: squat **5RM**, bench/press 3RM, power clean 3×5.
- **Progression:** set a new 5RM weekly with small increments (~+5 lb).
- **Stall fixes:** cut volume-day sets (5×5 → 3×5), lower volume-day weight 5–10%, change the intensity-day rep scheme.
- **Unverified:** "volume day = 90% of Friday's 5RM" appears only in secondary pages. **Do not state 90% as official.**
- **Strengths:** clear weekly stress/recovery wave. **Criticisms:** weekly PR attempts fail quickly without good recovery; high squat frequency/volume.

### 8. Madcow 5x5 — Verified (StrongLifts' official Madcow guide) [20]

- **Goal / level / days:** strength/size, intermediate, 3 days (Mon/Wed/Fri), full body.
- **Structure:** A (Mon, medium): squat 5×5 ramp, bench 5×5, row 5×5. B (Wed, light): squat 4×5, incline bench or OHP 4×5, deadlift 4×5. C (Fri, heavy): squat 4×5 + 1×3 + 1×8, bench same, row same. Assistance optional.
- **Ramps:** ~12.5% steps; e.g. A squat 135/175/205/245/275 ×5. B repeats the first three ramps and repeats set 3 (~75% of A's top). C top triple slightly above Monday's top (guide example 280 vs 275), then 1×8 back-off at ~75%.
- **Progression:** add to A's top set weekly when 5 reps are completed (squat/deadlift +5 lb; bench/rows/OHP microload +2.5 lb); repeat if not. Rest 1–2 min on easy ramps, 3–5 min on heavy sets.
- **Correction applied:** the "Friday triple ≈105% of Monday" figure is wrong; use "slightly above Monday's top set".
- **Not found:** run length (8–12 weeks), first-3-weeks-submax advice and reset rule — `Practitioner` only; say so.

### 9. nSuns 5/3/1 LP — Corrected; original quoted via wiki; spreadsheet set tables Unverified [21][17]

- **Goal / level / days:** strength + mass, intermediate; 4-, 5- or 6-day spreadsheet variants (start with 4-day). Two programmed lifts per day plus accessories.
- **Structure (secondary, unverified):** ~9 working sets: 5/3/1+ at 75/85/95% then 6 back-off sets (squat/OHP 3/3/3/5/5/5+; deadlift 3×6 …); T2 lift 8 sets 50→70%. Set tables were not verified against the spreadsheet.
- **TM rule (original post):** TM starts at 90% of 1RM; once a week an AMRAP set sets next week's TM change: **0–1 reps → no change; 2–3 reps → +5 lb; 4–5 reps → +5–10 lb; >5 reps → +10–15 lb.**
- **Correction applied:** "+5/+10/+15 per session" is the **Liftosaur app implementation**, not the original; label it as such.
- **Reset / deload:** not formally specified; start the TM conservative.
- **Strengths:** high frequency and volume, autoregulated jumps. **Criticisms:** high fatigue; not for novices.

### 10. Reddit PPL (Metallicadpa) — Verified (archived original post) [22]

- **Goal / level / days:** hypertrophy + strength, beginner–intermediate, 6 days (PPLRPPL or PPLPPLR; recommended order pull-push-legs) or 3.
- **Pull:** deadlift 1×5+ **or** barbell row 4×5 + 1×5+ (alternate each pull day); pulldowns/pull-ups 3×8–12; seated cable/chest-supported row 3×8–12; face pulls 5×15–20; hammer curls 4×8–12; DB curls 4×8–12.
- **Push:** bench 4×5 + 1×5+ **or** OHP (alternate); the other press 3×8–12; incline DB press 3×8–12; triceps pushdown superset lateral raise; overhead triceps extension superset lateral raise.
- **Legs:** squat 2×5 + 1×5+; RDL 3×8–12; leg press 3×8–12; leg curls 3×8–12; calves 5×8–12.
- **Progression:** **+5 lb upper lifts (bench, row, OHP) and squat, +10 lb deadlift** per session; accessories double progression (add weight at 3×12). Start weights: work up in 5s until bar slows, back off 5 lb. ("+10 lb" for all lifts appears only in app copies.)
- **Reset:** fail a session 3 times in a row → deload 10% and work back up; repeated stalls → intermediate program. Rest: 3–5 min main lifts, 1–3 min others.
- **Correction applied:** "no AMRAP bench and OHP same day" is not in the original; bench/OHP simply alternate main vs accessory press.
- **Strengths:** each muscle 2×/week, high volume, clear structure. **Criticisms:** 6 days/week and daily linear jumps are unsustainable beyond the novice phase.

### 11. PHUL (Campbell) — Partially verified; original Muscle & Strength article not retrieved [23]

- **Goal / level / days:** size + strength, intermediate, 4 days: upper power, lower power, upper hypertrophy, lower hypertrophy.
- **Structure (secondary):** power days compounds 3–4×3–5, accessories 6–10 reps; hypertrophy days 3–4×8–12; rest 2–3 min compounds, 1–2 min isolation.
- **Progression:** add reps first, then small load increases.
- **Reset / deload:** not formally specified; ≥1 RIR advice. **Label the original as unverified.**

### 12. PHAT (Norton) — Verified (Biolayne) [24]

- **Goal / level / days:** size + power, intermediate–advanced, 5 training days: D1 upper power, D2 lower power, D3 rest, D4 back & shoulders hypertrophy, D5 lower hypertrophy, D6 chest & arms hypertrophy, D7 rest.
- **Power days:** big lift 3–5 reps × 3–5 working sets; compounds 3×3–5, assistance 5–8 and 6–10 reps.
- **Hypertrophy days:** start with **speed work: 6–8 sets of 3 reps at 65–70% of 3–5RM**; then 8–12 / 12–15 / 15–20 rep work; rest 1–2 min; hypertrophy-day volume ~50–75% above power days.
- **Progression:** power days double progression 3→5 reps then +5 lb (secondary).
- **Unverified (do not state):** "4-week cycles ×3" and "rotate power lifts every 2–3 weeks".
- **Criticisms:** high weekly volume and 5 days; not for novices.

### 13. Candito 6-Week and Sheiko — Practitioner; not re-verified [12][13]

- **Candito:** 6-week powerlifting peak: W1–2 conditioning/hypertrophy; W3–4 strength (85–90%+); W5 test; W6 optional deload/retest. Frequency varies by source.
- **Sheiko (#29–32):** very high volume at ~70% average intensity; blocks #29 prep, #30 accumulation, #31 transmutation, #32 realization; day-stress classes. Advanced, competition prep only.
- Do not use Sheiko volumes for recreational lifters.

### 14. RP-style hypertrophy mesocycle — Practitioner, secondary sources [2]

- **Goal / level / days:** size, intermediate–advanced, 4–6 days, flexible split.
- **Structure:** start near minimum effective volume (~6–8 direct sets/muscle/wk as a rough figure), add sets weekly, RIR falling 3 → 1, then deload. Canonical wiki defaults override: hypertrophy 8/12/16 weekly hard sets by level, ~+1 set/muscle/week, 5 working + 1 deload (cut volume 30–50%). Sources differ on increments and deload size (50% volume vs 4:1–6:1 ratio) `Practitioner`.

### 15. Nippard-style Fundamentals — Secondary (app listings only) [11]

- **Goal / level / days:** size, beginner–intermediate, 3-day full body or 4-day upper/lower.
- **Structure:** ~3 sets/exercise at RPE 7–9 (≈1–3 RIR), isolation closer to failure; 8-week progressive blocks. Author's PDF not read.

### 16. Couch to 5K (NHS) — Verified (official) [25]

- **Goal / level / days:** aerobic base, zero running base, 3 runs/week with a rest day between, 9 weeks.
- **Each run:** 5-min warm-up walk + run/walk work + 5-min cool-down walk.
- **Progression:** Week 1 run 1 min / walk 1.5 min ×7 then a final 1-min run (28 min 30 s total). Week 2 starts run 1.5 min / walk 2 min ×5. Week 5 run 3 = 30 min total (20 min continuous). Week 7 = 35 min (25 min continuous). Week 9 = 40 min total (30 min continuous).
- **Reset:** repeating any run or week is explicitly allowed ("totally okay").

### 17. Higdon Novice 1 Marathon — Verified with corrections (official) [26]

- **Goal / level / days:** marathon finish; **prerequisite: established running base** (running 3–4 days/week for the last 1–2 years, averaging 15–20 mi/week). 18 weeks: 4 runs + 1 cross-train + 2 rest (Mon rest; Tue/Wed/Thu runs; Fri rest; Sat long run; Sun cross-train).
- **Long run by week:** 6, 7, **5**, 9, 10, **7**, 12, race (half marathon, week 8), **10**, 15, 16, **12**, 18, **14**, 20 (week 15), **12**, 8, marathon (week 18).
- **Cutbacks at weeks 3, 6, 9, 12, 14 and 16** (bold), then 3-week taper. Mid-week runs progress from 3/3–5/3 mi to 5/10/5. Weekly total ~15 mi (week 1) to ~40 mi (week 15).
- **Correction applied:** cutbacks are not only "every 3rd week"; "can run ~30 min" understates the prerequisite.

### 18. r/bodyweightfitness Recommended Routine — Verified (archived 2024 wiki) [27]

- **Goal / level / days:** general strength/skill, beginner–intermediate, 3×/week full body with ≥1 rest/skill day between.
- **Structure:** warm-up 5–10 min (dynamic stretches, wrist prep); strength work 40–60 min in pairs, each 3×5–8: Pair 1 pull-up + squat progressions; Pair 2 dip + hinge; Pair 3 row + push-up. Rest 90 s between a pair's alternating sets (up to 3 min if reps drop). Core triplet 3×8–12 (anti-extension, anti-rotation, extension), 60 s rests. Tempo ideally 1-0-X-0.
- **Progression:** pick a progression at 3×5, add a rep per set until **3×8**, then move to the next progression at 3×5. Isometric holds: move on at 30 s for all 3 sets (10–30 s range).
- **Version note:** a "10 min skill block" is in pre-2024 versions only; absent from the 2024 archive.

### 19. Convict Conditioning — Secondary [6]

- 6 movements (squat, pull-up, leg raise, bridge, push-up, handstand push-up) × 10 progression steps with rep/set gates (e.g. wall push-up gate 3×50 before incline). Only the push-up gate was verified; other step standards and reset rules not found.

### 20. Hybrid examples (Rogue, StrengthLog) — Practitioner, unverified originals [7][8]

- 2–3 lifting days + 2–3 runs per week (5–7 days): long Zone 2 60+ min, intervals 20–30 min, tempo run 20 min. Most running easy; ≤2 hard sessions; one rest day. Sources warn that ~4 h/wk lifting plus runs can be too much. No authoritative canonical template (Viada's source not accessible). See [hybrid](10-hybrid.md) for design rules.

## Corrections applied (raw/13 over raw/11)

| Program | Wrong / drifted version | Use instead |
|---|---|---|
| Starting Strength | reset after 3 failures; press/bench pairing "differs by source" | Second consecutive failure → 5% reset + light day (80% × 2×5); press/bench alternate every session; squat 3×5 |
| StrongLifts | cited via FitnessVolt/Healthline | Official pages; 3 repeats still failing → ~10% deload |
| nSuns | +5 / +10 / +15 lb by 2–3 / 4–5 / 6+ reps | Original weekly: 0–1 → none, 2–3 → +5, 4–5 → +5–10, >5 → +10–15 lb; app rule labelled as Liftosaur's |
| Reddit PPL | +5 vs +10 lb disagreement; "no AMRAP bench & OHP same day" | +5 lb upper & squat, +10 lb deadlift; bench/OHP alternate |
| Higdon Novice 1 | cutbacks 3, 6, 9, 12 only; prerequisite "can run ~30 min" | Cutbacks 3, 6, 9, 12, 14, 16; established running base |
| 5/3/1 for Beginners | stall rule + TM test listed as part of the program | r/Fitness wiki additions, not original |
| 5/3/1 BBB | third-party % | Wendler: 5×10 @ 50–60% TM, start ~30% TM |
| Texas Method | volume day 90% of 5RM as fact | Verified structure only; 90% unverified |
| Madcow | Friday triple ≈105% of Monday | Slightly above Monday's top set; back-off 1×8 @ ~75% |
| Greyskull | presented with increments as official | Phrak variant; original unverified |
| PHUL | original structure | Secondary description only; unverified |
| PHAT | 4-week cycles ×3; rotate power lifts every 2–3 weeks | Unverified; add speed-work block |
| r/bodyweightfitness RR | 10 min skill block | Pre-2024 version only |

## Recurring design patterns

| Pattern | Seen in |
|---|---|
| Few compound lifts cover squat / hinge / horizontal push / vertical push / pull | SS, SL, GZCLP, PPL, RR |
| 2–3 exposures per lift/muscle per week | All |
| Alternating A/B sessions with ≥1 rest day between | SS, SL, GZCLP, Greyskull, RR, C25K |
| One top/AMRAP set drives autoregulation | GZCLP, Greyskull, nSuns, 5/3/1, PPL |
| Heavy / volume / light day structure for intermediates | Texas, Madcow, PHUL, PHAT |
| Lower-volume deadlift | SS, SL, Greyskull, nSuns |
| Defined failure rule (−10% / stage drop / TM cut) | All good programs |
| Accessories by rep ranges + double progression | PHUL, PHAT, PPL, RR |
| Built-in deload / test week | 5/3/1, Candito, RP, Higdon cutbacks |
| Endurance: gradual time/distance + cutbacks + taper | C25K, Higdon |
| Higher-skill progressions gated by rep standards | RR, Convict Conditioning |

## Decision rules

1. IF true beginner (progress session to session) AND 3 days AND strength/general goal THEN full-body A/B LP (SS/StrongLifts/GZCLP pattern): squat each session, alternate bench/OHP, deadlift 1×5, row/pulldown for back, +2.5 kg / 5 lb upper and +5 kg / 10 lb lower per session.
2. IF beginner wants more back/accessory volume or 4 days THEN GZCLP structure (T1/T2/T3).
3. IF an LP lift fails: apply the **program's own trigger** — Starting Strength: second consecutive failure → 5% reset + light day; StrongLifts / Reddit PPL: three failures → ~10% deload; GZCLP: move down a stage. IF repeated resets on 2–3 lifts THEN move to Texas/Madcow or 5/3/1.
4. IF intermediate AND 3 days AND strength THEN Texas Method, Madcow or 5/3/1 for Beginners. IF Texas stalls THEN cut volume-day sets (5×5 → 3×5) or lower volume-day weight 5–10%.
5. IF strength-with-size, 4 days THEN 5/3/1 BBB or PHUL. IF 5–6 days AND high recovery AND surplus THEN nSuns / PHAT / PPL; start with the 4-day nSuns.
6. IF hypertrophy AND intermediate THEN each muscle ≥2×/week; set weekly volume from [variables](03-variables.md) (default 12, range 10–20), start lower and ramp ~+1 set/muscle/week over the mesocycle, RIR 3 → 1, then deload 30–50% volume.
7. IF 5/3/1 lifter misses reps across a full cycle THEN lower the TM 15 lb upper / 30 lb lower (wiki rule); IF AMRAP is near failure THEN lower effort and stop when bar speed slows.
8. IF user has no running base THEN Couch to 5K: 3 runs/week, ≥1 rest day between, repeat any week not yet comfortable.
9. IF user has an established base (3–4 d/wk, 15–20 mi/wk for 1–2 years) AND wants a marathon THEN Higdon Novice 1 (18 weeks, cutbacks 3, 6, 9, 12, 14, 16, 3-week taper).
10. IF no equipment THEN r/bodyweightfitness RR pattern: 3×/week, pairs at hardest manageable progression for 3×5–8, advance at 3×8.
11. IF hybrid strength + endurance THEN 2–3 lift days + 2–3 runs, mostly easy with ≤2 hard sessions, one rest day; see [hybrid](10-hybrid.md).
12. IF competitive powerlifter in a meet cycle THEN phased program (Candito/Sheiko style); IF recreational THEN do not use Sheiko volumes.
13. IF sedentary, older, medical condition or pain THEN do not assign unmodified; lighter volume, 3 RIR, recommend professional screening.
14. IF presenting any program THEN state schedule, sets×reps×load rule, progression, failure/reset rule, deload, version, and which parts are unverified.

## Common mistakes

- Giving a novice an advanced program (nSuns 6-day, PHAT, Sheiko) for "more volume".
- Linear progression forever: no reset rule or no transition to weekly/cycle progression [1][9].
- Using 100% of 1RM as the 5/3/1 base instead of ~90% TM.
- Taking AMRAP sets to true failure every session.
- Mixing program rules (5/3/1 percentages with StrongLifts increments).
- Forgetting back/pulling work in press/squat-centric programs (original Greyskull gap).
- 5×5 deadlifts in a beginner LP.
- Treating Couch to 5K weeks as mandatory pace: repeating weeks is allowed.
- Naming a program without a version (Texas %, Madcow %, PPL increments, nSuns TM rule differ by source).
- Stacking lifting and running volume without accounting for total load.
- Using the Starting Strength 3-failures reset, or Higdon "every 3rd week" cutbacks, or nSuns +5/+10/+15 as if original.

## Evidence notes

- Program structure is `Practitioner` throughout; none of these programs was RCT-tested. The shared skeleton (2–3 exposures, progression rule, reset rule) is consistent with the evidence that frequency barely matters when weekly volume is equated and that periodized > non-periodized for 1RM strength only modestly (see [progression](08-progression.md)).
- Volume dose-response meta-regression (15 studies): each added weekly set ≈ +0.37% muscle gain; higher vs lower volume ≈ +3.9%; data thin above ~10 sets/muscle/week and mostly untrained subjects [3] `Moderate`. Frequency: hypertrophy ES 0.49 vs 0.30 for higher frequency but confounded with volume [4]; strength frequency effect not significant in volume-equated studies (p=0.421) [10] `Moderate`.
- Canonical volume and progression numbers (ACSM 2026; Pelland 2025) live in [variables](03-variables.md) and [progression](08-progression.md); program-quoted set counts do not override them.
- **Version drift** (`Contested`): Texas volume-day %, Madcow increments, nSuns back-off schemes, GZCLP T1 stages, Greyskull increments differ by source.
- **Unverified / not found:** Greyskull original; PHUL original; Texas Method 90%; nSuns spreadsheet set tables; Nippard and RP primary PDFs; Convict Conditioning steps beyond push-up; Wendler's original 5/3/1 for Beginners article; hybrid templates' originals; Candito/Sheiko not re-verified.
- ACSM 2009 novice frequency numbers (2–3 d/wk) are superseded by ACSM 2026 for volume guidance; do not cite 2009 numbers over the canonical defaults [5].

## Sources

[1] Starting Strength / Barbell Logic, Novice Linear Progression Program Explained. https://barbell-logic.com/starting-strength-novice-linear-progression/
[2] Arvo / LiftVault, RP training volume landmarks and mesocycles (secondary). https://arvo.guru/resources/methods/rp-training ; https://liftvault.com/programs/bodybuilding/mike-israetel-5-week-hypertrophy-workout-routine-spreadsheet/
[3] Schoenfeld, Ogborn, Krieger, Dose-response relationship between weekly resistance training volume and increases in muscle mass: SR & MA, J Sports Sci, 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC6303131/
[4] Schoenfeld, Ogborn, Krieger, Effects of resistance training frequency on measures of muscle hypertrophy: SR & MA, Sports Med, 2016. https://pubmed.ncbi.nlm.nih.gov/27102172/
[5] ACSM, Progression Models in Resistance Training for Healthy Adults, 2009; 2026 position stand overview. https://acsm.org/science-spotlight-acsm-releases-new-position-stand-on-resistance-training/ ; 2026: Currier BS … Phillips SM, Med Sci Sports Exerc 58(4):851–872, doi:10.1249/MSS.0000000000003897 (PMC12965823)
[6] Brikman, Convict Conditioning review; Breaking Muscle review. https://www.ybrikman.com/blog/2020/08/10/convict-conditioning/ ; https://breakingmuscle.com/book-review-convict-conditioning-by-paul-wade/
[7] Rogue Fitness, How to train as a hybrid athlete. https://www.roguefitness.com/eu/de/theindex/movement-library/how-to-train-as-a-hybrid-athlete-strength-and-endurance-plan
[8] StrengthLog, 12-Week Intermediate Hybrid Athlete Program. https://www.strengthlog.com/?p=37034
[9] Starting Strength, Programs (Wayback copy, 2024). https://web.archive.org/web/2024/https://startingstrength.com/get-started/programs
[10] Grgic et al., Effect of resistance training frequency on gains in muscular strength: SR & MA, Sports Med, 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC6081873/
[11] Alter R., The Reset: Why and How, Starting Strength, 2018 (Wayback copy). https://web.archive.org/web/2024/https://startingstrength.com/article/the-reset-why-and-how ; Nippard Fundamentals listings (secondary): https://www.boostcamp.app/users/vmY3Wd-jeff-nippard-lu-fundamentals-hypertrophy-program
[12] Mehdi, StrongLifts 5×5 Workout Program: Quick Start Guide. https://stronglifts.com/stronglifts-5x5/workout-program/ ; Candito 6-Week reviews: https://fitnessvolt.com/powerlifting/programs/candito-6-week/ ; https://www.powerliftingtowin.com/candito-6-week-strength-program/
[13] Mehdi, How to Progress on Stronglifts 5×5. https://stronglifts.com/stronglifts-5x5/progress/ ; Sheiko: https://powerliftingtowin.com/sheiko ; https://www.jtsstrength.com/what-i-learned-at-the-russian-strength-seminar/
[14] Mehdi, How to Overcome Failure on Stronglifts 5×5. https://stronglifts.com/stronglifts-5x5/failure/ ; overview https://stronglifts.com/stronglifts-5x5/
[15] The Fitness Wiki (r/Fitness), GZCLP (companion to Cody LeFever's original post). https://thefitness.wiki/routines/gzclp/
[16] Greyskull LP secondary descriptions (not original, unchecked): https://fitnessvolt.com/rpe-training/programs/greyskull-lp/ ; https://www.liftosaur.com/programs/phrakgreyskull ; 5/3/1 BBB secondary: https://liftvault.com/resources/boring-but-strong/
[17] The Fitness Wiki, 5/3/1 for Beginners. https://thefitness.wiki/routines/5-3-1-for-beginners/
[18] Wendler J., Boring But Big — Jim Wendler's 5/3/1 Assistance Program. https://www.jimwendler.com/blogs/jimwendler-com/101077382-boring-but-big
[19] Feigenbaum J., 12 Ways To Skin The Texas Method, Barbell Medicine. https://www.barbellmedicine.com/blog/12-ways-to-skin-the-texas-method/
[20] Mehdi, Madcow 5×5 Workout: The Official Guide. https://stronglifts.com/stronglifts-5x5/workout/ ; https://stronglifts.com/madcow-5x5/workout-guide/
[21] The Fitness Wiki, nSuns LP (quotes u/nSuns original post). https://thefitness.wiki/routines/nsuns-lp/ ; Liftosaur implementation: https://www.liftosaur.com/programs/nsuns
[22] Metallicadpa, A Linear Progression Based PPL Program for Beginners, r/Fitness, 2015 (Wayback copy, 2024). https://web.archive.org/web/2024/https://www.reddit.com/r/Fitness/comments/37ylk5/a_linear_progression_based_ppl_program_for/
[23] StrengthLog, PHUL workout routine (secondary). https://strengthlog.com/phul-workout-routine/
[24] Norton L., PHAT – Power Hypertrophy Adaptive Training, Biolayne. https://biolayne.com/articles/training/phat-power-hypertrophy-adaptive-training/
[25] NHS, Couch to 5K running plan. https://www.nhs.uk/better-health/get-active/get-running-with-couch-to-5k/couch-to-5k-running-plan/
[26] Higdon H., Novice 1 Marathon Training Program. https://www.halhigdon.com/training-programs/marathon-training/novice-1-marathon/
[27] r/bodyweightfitness, Recommended Routine (Wayback copy, 2024). https://web.archive.org/web/2024/https://www.reddit.com/r/bodyweightfitness/wiki/kb/recommended_routine/
