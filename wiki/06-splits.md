# Training Splits Catalog

> Purpose: choose a split (how muscles/patterns are distributed across training days) and decide fixed-calendar vs rolling scheduling and missed-day handling.
> Use when: the plan needs a day layout; the user names a split; the user asks "which split is best"; a session is missed.
> Depends on: [principles](01-principles.md) (volume/frequency), [variables](03-variables.md) (sets, RIR, rest), [session design](05-session-design.md), [weekly planning](07-weekly-planning.md) (days-per-week playbook), [hybrid](10-hybrid.md)

## Key rules (TL;DR)

1. A split is only a way to distribute weekly hard sets per muscle across days. **Weekly sets and effort matter more than the split label.** At equal weekly volume, higher vs lower frequency gives no significant hypertrophy difference [2] (Strong) and no significant strength difference in volume-equated subgroups [3][4][5] (Moderate). No trial shows any named split is superior long term [8][9][12] (Moderate; short trials).
2. **Default frequency: 2×/muscle/week.** 1×/week is fine at <~10 weekly sets per muscle; 3× is for high volume or to keep per-session sets down. (Canonical defaults.)
3. **Weekly set targets (hard sets/muscle):** beginner hypertrophy 8, intermediate 12, advanced/priority 16 (range 12–20, ≤~22 short-term specialization), max strength 6 (2–3 sets × 2–3 sessions), maintenance 4–6, minimum useful ≥1 hard set per major pattern on ≥2 d/wk. Fractional counting: direct = 1, indirect = 0.5.
4. **Per-session soft cap: 10 fractional hard sets per muscle (≈6–8 direct).** If the weekly target needs more, add a session for that muscle. Sets/session = weekly target ÷ frequency. (Contested: the cap derives from a preprint's "point of undetectable further benefit", not a proven ceiling [7].)
5. **Choose by: (a) days/week the person will keep, (b) frequency ≥2×, (c) session length, (d) recovery, (e) preference. Adherence breaks ties.** Honor a stated split preference if weekly sets and frequency are acceptable.
6. **Default map:** 1–3 d → full body (if the person dislikes full body at 3 d: alternating upper/lower, ≈1.5×/muscle, or lower/upper/lower; never add a day they did not offer); 4 d → upper/lower; 5 d → ULPPL (or PHAT-style, advanced); 6 d → PPL×2 (Arnold only if very high tolerance); body-part (1×) only for preference/specialization, with a second hit on lagging muscles. Details per day count: [weekly planning](07-weekly-planning.md).
7. Beginners: full body 2–3×/week. Never prescribe bro split, Arnold or PHAT to a beginner.
8. Leave ≥1 rest day (or a non-overlapping day) between sessions hitting the same muscle hard (~48 h, ACSM 2009 [11]).
9. Irregular life → **rolling** schedule (next workout in sequence regardless of weekday). Stable life → fixed calendar.
10. Missed session → skip or resume the sequence. **Never double up to catch up.** 1–3 weeks off costs little strength [15][16].
11. Named-split details (PHUL, PHAT, Arnold, torso/limbs, anterior/posterior) are Practitioner-grade and vary by source. PHUL and PHAT originals are unverified; treat the layouts below as templates, not canon.

## Core concepts

- **Split**: assignment of muscles/movement patterns to training days in a weekly cycle.
- **Per-muscle frequency**: sessions/week that train a muscle with meaningful direct sets or ≥ meaningful indirect work. Count indirect work at 0.5 (e.g. triceps from pressing).
- **Frequency–volume coupling**: in non-volume-equated studies higher frequency "wins" mostly because it carried more volume [1][2][3]. Frequency is a *tool to reach volume with good-quality sets*, plus more skill practice on lifts.
- **Fixed-calendar split**: days tied to weekdays (Mon = Upper).
- **Rolling split**: workouts run in order; rest days inserted by pattern ("2 on 1 off") or need.
- **Overlap fatigue**: next-day work that uses synergists of yesterday's muscles (push day → shoulder day) lowers quality. Order days to avoid it.

## Master comparison table

Frequency = exposures per muscle/week. Sets/session assumes the weekly target ÷ frequency (e.g. 12/wk ÷ 2 = 6). All layouts: Practitioner; frequency logic: see rule 1.

| Split | Days/wk | Day layout | Freq | Sets/muscle/session at 12/wk | Best fit | Main con |
|---|---|---|---|---|---|---|
| Full body (FB) | 2–4 (3 typical) | Each day: squat/hinge + push + pull + accessories; A/B emphasis | 2–4× | 3–6 (12 ÷ 2–4) | Beginners, time-poor, 2–3 d, strength | Long sessions at high volume; per-session cap limits weekly total |
| Upper/Lower (UL) | 4 | U / L / R / U / L | 2× | 6 | Intermediate, 4 d, strength + size | Upper day crowded (arms/delts after pressing) |
| Push/Pull/Legs once | 3 | Pu / Pl / Lg | 1× | 12 (over cap → ≤8 direct realistic) | 3 d, preference, higher per-muscle volume | 1× frequency; low-ranked unless done 6 d |
| PPL×2 | 6 | PPL PPL + R | 2× | 6 | Intermediate/advanced, 6 d, hypertrophy | Fatigue; missed day breaks frequency |
| Body-part ("bro") | 5–6 | Chest / Back / Shoulders / Arms / Legs | 1× (indirect adds ~1.5×) | 12 (above cap) | Preference, advanced, specialization | No evidence of superiority [8]; a missed day skips a muscle for a week |
| Arnold | 6 | Chest+Back / Shoulders+Arms / Legs, ×2 | 2× | 6 | Advanced, high tolerance | Very high total volume (sample ≈80 sets/day-triplet) [17] |
| Torso/Limbs (TL) | 4 | T / Lm / R / T / Lm | 2× | 6 | Arm/leg emphasis; fixes crowded upper day | Limb day long and leg-heavy |
| Anterior/Posterior (AP) | 4 | Front (chest, quads, abs, front delt) / Back (back, hams, glutes, rear delt) | 2× | 6 | Pattern-based balance | Squat/deadlift overlap decisions; thinly documented [19] |
| Push/Pull 2-way | 4 | Push / Pull / R / repeat (legs placed with either) | 2× | 6 | 4 d alternative to UL | Ambiguous definition; legs awkward |
| PHUL | 4 | Upper Power / Lower Power / R / Upper Hyp / Lower Hyp | 2× | 6 | Intermediate wanting strength + size | Sources vary; hypertrophy-day compounds fatigued |
| PHAT | 5 | Upper Power, Lower Power, then 3 hypertrophy days (back/shoulders, legs, chest/arms) | ~2× | 6 | Advanced, 5 d | Heavy, long, complex |
| ULPPL | 5 | U / L / Pu / Pl / Lg | 2× (all patterns) | 6 | 5-d intermediate | Uneven indirect volume (delts/triceps) |
| Specialization | 4–6 | Base split + extra day/sets for 1–2 muscles; others at maintenance | priority 3–4×; others 1–2× | priority 16 ÷ 3 ≈ 5 | Lagging muscles, advanced | Recovery limit; others stall if starved |
| Powerlifting SBD | 3–5 | Squat / Bench / Deadlift days + variants | squat 2×, bench 2–3×, deadlift 1–2× | comp lift 2–3 sets × 2–3 sessions (strength = 6/wk) | Competitive powerlifters | Neglects hypertrophy accessories |

## Split catalog

Format per split: layout · muscles/day · frequency · sessions/wk · sets/session · pros · cons · best fit · variants. Set counts apply the canonical weekly target ÷ frequency.

### 1. Full body (FB)
- **Layout**: every session has a squat or hinge pattern + horizontal/vertical push + horizontal/vertical pull + optional core/accessories. Alternate A/B emphasis (A: squat + bench + row; B: hinge + overhead press + pulldown).
- **Muscles/day**: all major groups. **Frequency**: 2–4×. **Sessions/wk**: 2–4 (3 typical).
- **Sets/muscle/session**: 3–6. Example 3 d: beginner 8/wk → ~3; intermediate 12/wk → 4; advanced 16/wk → ~5–6. 2 d: 12/wk → 6.
- **Pros**: high frequency with few days, forgiving of missed days, skill practice, ≥1 rest day between sessions comes naturally.
- **Cons**: long sessions at high volume; per-session cap makes >~16/wk per muscle hard on 3 d.
- **Best fit**: beginners, 1–3 d/wk, time-poor, strength, rolling schedules.
- **Variants**: A/B/A; FB×4 low-volume (<40 min); FB + upper/lower mix (U/L/FB).

### 2. Upper/Lower (UL)
- **Layout**: U / L / R / U / L (+ weekend rest). **Muscles**: upper = chest, back, shoulders, arms; lower = quads, hams, glutes, calves, core. **Frequency**: 2×. **Sessions**: 4 (2–3 UL variants).
- **Sets/muscle/session**: 4 (8/wk), 6 (12/wk), 8 (16/wk). Pressing gives triceps/front-delt 0.5 credit, so cut direct triceps/delt sets accordingly.
- **Pros**: simple, balanced, recoverable. **Cons**: upper day crowded (chest, back, shoulders, arms all in one session).
- **Best fit**: intermediate, 4 d, strength + size. **Variants**: U/L/FB (3 d), U/L×3 (6 d, 3×), alt strength/hypertrophy days (see PHUL).

### 3. Push/Pull/Legs (PPL, once weekly)
- **Layout**: Pu (chest, shoulders, triceps) / Pl (back, biceps, rear delts) / Lg (quads, hams, glutes, calves). **Frequency**: 1×. **Sessions**: 3.
- **Sets/session**: weekly target = session sets (8–12). 12 direct sets is above the 6–8 direct soft cap, so effective ceiling ≈8–10/muscle/wk. Use only on explicit preference at 3 d; full-body ×3 usually beats it on frequency.

### 4. PPL×2 (6 d)
- **Layout**: Pu / Pl / Lg / Pu / Pl / Lg / R (or "3 on 1 off" rolling). **Frequency**: 2×. **Sessions**: 6.
- **Sets/session**: 4 (8/wk), 6 (12/wk), 8 (16/wk). Differentiate day A vs day B (heavy/low-rep vs moderate/high-rep; different exercise variants) to manage fatigue.
- **Pros**: 2× frequency, high weekly capacity, easy to remember, rolling-friendly. **Cons**: 6 d commitment, fatigue accumulation, missed day breaks frequency (fix: roll it).
- **Best fit**: intermediate/advanced with 6 d, good sleep, hypertrophy. **Not** for beginners or low-recovery users.

### 5. Body-part ("bro") split
- **Layout**: Chest / Back / Shoulders / Arms / Legs, Mon–Fri. **Frequency**: 1× direct (+ indirect ≈ 1.5×). **Sessions**: 5–6.
- **Sets/session**: 12–20 per muscle (typical practice) = above the 10-fractional cap; quality drops.
- **Evidence**: volume-equated well-trained men: high-frequency matched or beat bro split; bro split had more soreness [8] (Moderate; one trial, secondary summary). Not shown superior.
- **Pros**: per-muscle focus, long recovery, preference. **Cons**: one missed day = muscle skipped for a week; low skill practice; soreness.
- **Rule**: IF used THEN ensure each muscle ≥2 hits/wk when weekly sets >12 (pair chest/back, shoulders/arms with indirect + a second light exposure).

### 6. Arnold split
- **Layout**: Chest+Back / Shoulders+Arms / Legs, ×2 (6 d). **Frequency**: 2×. Antagonist supersets. Sample volume ≈80 sets/day [17] (Practitioner; original routine unauthenticated).
- **Best fit**: advanced, long sessions, high tolerance. **Cons**: very high volume, 6 d. Cap at 12–16 weekly sets per muscle by trimming sets; do not copy the 80-set figure.
- **Overlap**: Shoulders+Arms day follows Chest+Back: front delts/triceps get indirect work first. Insert rest or accept reduced pressing.

### 7. Torso/Limbs (TL)
- **Layout**: Torso (chest, back, shoulders) / Limbs (quads, hams, glutes, calves, biceps, triceps) / R / Torso / Limbs. **Frequency**: 2×. **Sessions**: 4.
- **Sets/session**: torso ≈10–14 total per day; limbs ≈12–18 total per day [20] (Practitioner). Per muscle: weekly ÷ 2.
- **Pros**: arms + legs get fresh quality work; fixes crowded upper day. **Cons**: long limb day; less strength-oriented.
- **Best fit**: arm/leg emphasis (hypertrophy).

### 8. Anterior/Posterior (AP)
- **Layout**: Front = chest, quads, abs, front delts, triceps(if pressing) / Back = back, hams, glutes, rear delts, biceps. 4 d, 2×. Sets/session 6 at 12/wk.
- **Cons**: squat vs deadlift placement needs decisions (deadlift day on Back; keep heavy deadlift away from heavy squat day); thinly documented [19].
- **Best fit**: lifters wanting pattern-based balance and knee/hip separation.

### 9. Push/Pull (2-way, 4 d)
- Push (chest, shoulders, triceps, ± quads) / Pull (back, biceps, hams) / R / repeat. 2×. Ambiguous definition; legs split awkwardly. Prefer UL.

### 10. PHUL (Power Hypertrophy Upper Lower)
- **Layout**: Upper Power / Lower Power / R / Upper Hyp / Lower Hyp. Power days 3–5 reps, hypertrophy days 8–15 reps [18]. DUP-like. Frequency 2×.
- **Status**: original program unverified; secondary sources vary. Keep power-day loads ≥80% 1RM, 1–6 reps (strength default); hypertrophy days 6–15 reps at 2 RIR.
- **Best fit**: intermediates wanting strength + size, 4 d.

### 11. PHAT (Power Hypertrophy Adaptive Training)
- **Layout (5 d)**: Upper Power, Lower Power, R, Back+Shoulders Hyp, Legs Hyp, Chest+Arms Hyp [18]. Upper muscles ~2×, legs 2×.
- **Status**: original unverified. Advanced only; heavy and long. Trim volume to the canonical weekly target (16 for advanced).

### 12. ULPPL (UL + PPL hybrid, 5 d)
- **Layout**: U / L / R / Pu / Pl / Lg (rest after Lg). Chest/back/shoulders: U + Pu/Pl = 2×; legs: L + Lg = 2×.
- **Sets/session**: 6 at 12/wk. Watch indirect volume: delts/triceps get pressing on both U and Pu; delts/biceps get pulling on U and Pl. Count at 0.5.
- **Best fit**: intermediate, 5 d. **Con**: uneven frequency by muscle; the Pl→Lg adjacency needs light hinge on Pl.
- **Variants**: UL + FB (U / L / R / U / L / FB-light); UL + specialization day.

### 13. Specialization (priority muscle)
- **Layout**: base split (UL, PPL×2, ULPPL) + extra sets and/or an extra session for 1–2 lagging muscles.
- **Targets**: priority muscle 16 (12–20, ≤~22 short-term) at 3–4×; every other muscle at maintenance 4–6/wk (1–2×). Limit to 1–2 priority muscles per block. Keep priority-muscle sets per session ≤8 direct.
- **Evidence**: indirect (volume dose-response). Grade: Practitioner. Con: recovery limits; others stall if starved below 4.

### 14. Powerlifting-style (SBD days)
- **Layout (4 d)**: Squat / Bench / R / Deadlift / Bench-variation. **Frequency**: squat 2×, bench 2–3×, deadlift 1–2× (survey of 548 powerlifters: ~4.25 sessions/wk; squat ~1.6×, bench ~2.5×, deadlift ~1.4× per week [14]; Practitioner).
- **Volume**: max-strength default 6 weekly sets per lift-specific muscle (2–3 sets × 2–3 sessions), ≥80% 1RM, 1–6 reps; sets per exercise 2–3 (up to 5 for peaking).
- **Study**: Norwegian powerlifters, 15 weeks: 6 sessions/wk gained more squat/bench than 3; deadlift no difference [13] (Moderate; authors asked figures removed, treat sizes with caution).
- **Rule**: IF deadlift fatigue high THEN deadlift 1×/wk, second hit a lighter variation. Keep deadlift away from heavy squat day.

## Rest-day patterns (fixed calendar)

| Split | Template (Mon–Sun) | Note |
|---|---|---|
| FB 3 d | FB R FB R FB R R | ≥1 day between sessions (~48 h) |
| FB 2 d | FB R R FB R R R | 3+ days apart |
| UL 4 d | U L R U L R R | Weekend rest |
| UL 4 d (alt) | U R L R U L R | Spreads leg days |
| PPL once | Pu R Pl R Lg R R | |
| PPL×2 | Pu Pl Lg Pu Pl Lg R (or Pu Pl Lg R Pu Pl Lg rolling) | Rest on day 4 or 7 |
| Arnold | CB Sh+Ar Lg CB Sh+Ar Lg R | |
| ULPPL | U L R Pu Pl Lg R | Rest between L and Pu |
| PHUL | UP LP R UH LH R R | |
| PHAT | 5 d, 2 rest days; heavy days separated | |
| Bro 5 d | Mon–Fri, weekend off | |
| Powerlifting 4 d | Sq Bn R Dl Bn-var R R | Deadlift away from heavy squat |

## Rolling vs fixed-calendar schedules

| | Fixed calendar | Rolling (sequence-based) |
|---|---|---|
| Definition | Day-of-week → session (Mon = Upper) | Next session in the cycle is done next training day |
| Best for | Stable week, coach-led, group classes, hybrid plans with fixed cardio | Shift work, travel, kids, variable recovery, PPL, FB |
| Rest days | Fixed | Inserted by pattern ("3 on 1 off", "2 on 1 off") or by need |
| Missed day | Session lost or moved; may shift a muscle's frequency | Nothing lost; sequence pauses |
| Risk | Muscle skipped for a week (bro, PPL once) | Weekly frequency becomes irregular; weekly sets can drift below target |

Evidence: no trials compare rolling vs fixed adherence (Practitioner; rolling PPL described in [21]). Rolling is a scheduling convenience, not a physiological advantage.

**Rolling rules**
1. Keep the cycle length (e.g. 6 sessions for PPL×2) and cap rest gaps: ≤2 consecutive rest days in a normal week.
2. Count a "week" as the last 7 days; IF a muscle fell below target sets in the last 7 days THEN reorder the next sessions so it is hit sooner.
3. Never run more than 3 consecutive training days without a rest or easy day.
4. Rolling is the default for irregular schedules; fixed for stable schedules.

## Missed sessions and layoffs

| Situation | Action | Grade |
|---|---|---|
| 1 session missed | Skip it or resume the sequence; do **not** double up. If it was the only hit of a muscle this week and ≥2 days remain, move it to the next free day and drop that day's lowest-priority accessories | Practitioner |
| Several sessions missed in a week | Resume at the planned point; do not compress two hard sessions into consecutive days | Practitioner |
| 1–3 weeks off | Minimal strength loss [15][16]. Resume at the planned week; first session ~90–95% loads if rusty | Moderate / Practitioner |
| 3–4+ weeks off | Reduce loads ~10%, ramp over 1–2 weeks (a few weeks per the canonical layoff rule); regaining is faster than building ("about half the layoff time" is a practitioner estimate, not measured) | Practitioner |
| Meaningful decay | ~5–16 wk of inactivity; strength-trained athletes lost ~7–12% over 8–12 wk [15] | Moderate |
| Time-poor week | Maintenance dose: 4–6 weekly sets/muscle, 1–2 sessions, heavy loads [16] | Moderate |

## Decision rules

1. IF days/week ≤3 THEN full body A/B with ≥1 rest day between sessions.
2. IF 4 d AND goal strength or general hypertrophy THEN upper/lower. IF arms/delts/calves are priority THEN torso/limbs. IF user wants pattern-based balance and tolerates ordering complexity THEN anterior/posterior. IF user wants strength + size with rep-range variety THEN PHUL.
3. IF 5 d AND intermediate THEN ULPPL (or UL + FB). IF advanced AND wants power + size THEN PHAT-style.
4. IF 6 d AND intermediate+ AND sleeps ≥7 h THEN PPL×2. IF very advanced, long-session capable, high volume tolerance THEN Arnold. OTHERWISE cap at 5 d.
5. IF user wants body-part split THEN allow it, but ensure ≥2 exposures/wk for any muscle with weekly sets >12.
6. IF weekly sets for a muscle ≤10 THEN 1×/wk is acceptable. IF >10–12 THEN spread across ≥2 sessions.
7. IF beginner THEN full body 2–3×/wk. No bro/Arnold/PHAT.
8. IF schedule irregular THEN rolling FB or rolling UL/PPL. IF stable THEN fixed calendar.
9. IF a split has two same-muscle sessions back-to-back at high volume THEN reorder or insert rest (~48 h).
10. IF session time <45 min THEN more days with fewer sets (FB/UL) over long body-part sessions.
11. IF powerlifter THEN squat 2×, bench 2–3×, deadlift 1–2×.
12. IF specialization THEN priority muscle 16/wk (≤~22 short term) at 3–4×, others 4–6/wk, max 1–2 priorities.
13. IF a per-session muscle count exceeds 10 fractional sets THEN add a session.
14. IF user prefers a split THEN honor it when frequency/volume are acceptable [2].

## Common mistakes

- Treating the split label as the cause of results; ignoring weekly sets.
- 6-day PPL for a beginner or low-recovery person.
- Body-part split for someone who misses days (one missed Monday = chest untrained for two weeks).
- Crowded upper day with all of chest/back/shoulders/arms at high volume.
- Doubling sessions to catch up.
- Heavy squat and heavy deadlift on adjacent days.
- 12+ sets of one muscle in one session instead of adding a session.
- 3 FB days on consecutive days.
- Copying a named program's exact volumes (secondary-source summaries; Arnold ~80 sets/day, PHAT) instead of the canonical weekly targets.
- Counting indirect work as direct (double-counting delts/triceps in ULPPL, Arnold).

## Evidence notes

- **Frequency (hypertrophy)**: Schoenfeld 2016 (10 studies) ES 0.49 (higher) vs 0.30 (lower) was not cleanly volume-equated [1]; Schoenfeld 2019 (25 studies) found no significant difference on a volume-equated basis [2]. Strong. Pelland: hypertrophy–frequency slope compatible with negligible; strength–frequency positive with diminishing returns [22][23] (Moderate).
- **Frequency (strength)**: Grgic 2018 22 studies: ES 0.74/0.82/0.93/1.08 for 1/2/3/4+ d/wk, but the volume-equated subgroup showed no effect (P = 0.421); significance only for multi-joint lifts and upper body [3][4] (Moderate).
- **Trained men**: 3 vs 6 sessions/wk, equal volume, similar hypertrophy/strength [12] (Moderate, small RCT). Other small trials reported slight edges for full body; none favored split routines [8][9].
- **Untrained**: 2× FB vs 4× split, 50 women, 12 wk, no between-group difference [6]; untrained men 8 wk similar at equal sets [10] (design details inconsistent across summaries).
- **ACSM 2009 day staging** (novice 2–3, intermediate 3–4, advanced 4–5 d/wk; 48 h recovery) [11] is legacy: ACSM 2026 says it rested on thin evidence (3 studies, n = 59). Present as Practitioner guidance, not as a target [22].
- **Per-session cap** is Contested (preprint [7]); weekly volume matters more than session distribution once frequency ≥2.
- **Named splits** (PPL, Arnold, PHUL, PHAT, TL, AP): no head-to-head trials; rationale is scheduling/fatigue overlap. Practitioner [17][18][19][20].
- **Unverified**: PHUL/PHAT original specifications; Arnold's actual routine; secondary-source set counts.
- **Not found**: peer-reviewed PPL vs UL, TL or AP comparison; rolling vs fixed adherence trials. Re-checked online 2026-10-10: still none; frequency effect at equal volume remains negligible (see `research/04-web-findings-log.md`).

## Sources

1. Schoenfeld BJ, Ogborn D, Krieger JW. Effects of Resistance Training Frequency on Measures of Muscle Hypertrophy: A Systematic Review and Meta-Analysis. Sports Medicine, 2016. https://pubmed.ncbi.nlm.nih.gov/27102172/
2. Schoenfeld BJ, Grgic J, Krieger J. How many times per week should a muscle be trained to maximize muscle hypertrophy? J Sports Sci, 2019. https://pmc.ncbi.nlm.nih.gov/articles/PMC6724585 ; summary: https://mennohenselmans.com/training-frequency-2018-meta-analysis-review/
3. Grgic J, Schoenfeld BJ, et al. Effect of Resistance Training Frequency on Gains in Muscular Strength: A Systematic Review and Meta-Analysis. Sports Med, 2018. https://vuir.vu.edu.au/37695/
4. Ralston GW et al. Weekly Training Frequency Effects on Strength Gain: A Meta-Analysis. Sports Med Open, 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC6081873/
5. Stronger By Science. Research Spotlight: Frequency. https://www.strongerbyscience.com/research-spotlight-frequency/
6. Full-body vs split routine in untrained women, 12 weeks. BMC Sports Sci Med Rehabil, 2022. https://bmcsportsscimedrehabil.biomedcentral.com/articles/10.1186/s13102-022-00481-7
7. Pelland JC, Remmert JF, Robinson ZP, Hinson SR, Zourdos MC. The Resistance Training Dose-Response: Meta-Regressions of Weekly Volume and Frequency. SportRxiv preprint, 2024. https://sportrxiv.org/index.php/server/preprint/view/460 (per-session paper: Remmert/Pelland, SportRxiv 10.51224/srxiv.537, a preprint)
8. Henselmans M. High-frequency resistance training is not more effective than low-frequency in well-trained men (review of high-frequency vs bro split RCT). https://mennohenselmans.com/high-frequency-resistance-training-is-not-more-effective-than-low-frequency-resistance-training-in-increasing-muscle-mass-and-strength-in-well-trained-men/
9. Biolayne. Full Body vs Split Routine Wars (Reps issue 25). https://biolayne.com/reps/issue-25/full-body-vs-split-routine-wars/
10. Untrained men, split vs full body, 8 weeks. https://pmc.ncbi.nlm.nih.gov/articles/PMC9107721/ (design details inconsistent across summaries)
11. ACSM Position Stand: Progression Models in Resistance Training for Healthy Adults, MSSE, 2009. https://www.sportgeneeskunde.com/wp-content/uploads/ACSM-Position-Stand-Progression-Models-in-Resistance-Training-for-Healthy-Adults.pdf
12. Resistance Training Frequencies of 3 and 6 Times Per Week Produce Similar Muscular Adaptations in Resistance-Trained Men. J Strength Cond Res, 2018 (author attribution varies across raw files; Grgic & Schoenfeld per raw/06). https://pubmed.ncbi.nlm.nih.gov/30363041/
13. Stronger By Science. High-frequency training for a bigger total: Norwegian powerlifters. https://www.strongerbyscience.com/high-frequency-training/
14. Survey of 548 powerlifters (J Strength Cond Res, 2025), secondary summary. https://www.socalpowerlifting.net/post/how-often-should-a-powerlifter-train
15. Bosquet L et al. Effects of detraining on strength (meta-analysis, 2013), summary. https://sportsperformancebulletin.com/training/strength-conditioning--flexibility/cut-your-losses-strength-detraining-truths
16. Stronger By Science. Training for the time-poor. https://www.strongerbyscience.com/training-for-time-poor/
17. Setgraph. Arnold Split Workout: The Complete 6-Day Guide (practitioner). https://setgraph.app/articles/arnold-split-workout-complete-guide
18. Hevy. PHUL: Power Hypertrophy Upper Lower (practitioner). https://www.hevyapp.com/phul-power-hypertrophy-upper-lower/
19. Jefit. Anterior Posterior Split: Complete Guide (practitioner). https://www.jefit.com/blog/anterior-posterior-split-the-complete-guide-to-front-back-training
20. J3University. Torso/Limb Split (practitioner). https://j3university.com/assets/downloads/torso-limb-split.pdf
21. Setgraph. Push Pull Legs Reddit: Practical Guide (rolling PPL, practitioner). https://setgraph.app/ai-blog/push-pull-legs-reddit
22. Currier BS … Phillips SM. ACSM Position Stand: Resistance Training Prescription for Muscle Function, Hypertrophy, and Physical Performance in Healthy Adults: An Overview of Reviews. Med Sci Sports Exerc 58(4):851–872, 2026. doi:10.1249/MSS.0000000000003897 (PMC12965823)
23. Pelland et al. Sports Med 56(2):481–505 (online Dec 2025), peer-reviewed (cited via research/03-canonical-defaults.md and raw/12; no URL in repo).
