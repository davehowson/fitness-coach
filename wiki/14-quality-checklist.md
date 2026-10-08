# Plan Quality Checklist

> Purpose: score any generated plan against fixed pass conditions before returning it, and fix failures.
> Use when: every plan, after drafting and before output; also when auditing a user's existing plan.
> Depends on: [principles](01-principles.md), [intake](02-intake.md), [variables](03-variables.md), [session design](05-session-design.md), [splits](06-splits.md), [weekly planning](07-weekly-planning.md), [progression](08-progression.md), [conditioning](09-conditioning.md), [exercise library](12-exercise-library.md)

## Key rules (TL;DR)

1. Run all 14 items. Score each **Pass = 1, Partial = 0.5, Fail = 0**. Return the plan only at **≥ 12.5 / 14 with no Critical item failed**.
2. **Critical items** (any Fail blocks output until fixed): #1 goal alignment, #11 time fit, #12 equipment fit, #14 safety. Also #13 health floor if the user is sedentary or older.
3. Fix in the order listed in the "Fix" column; re-run the whole checklist after any fix (fixes interact: adding sets breaks time fit).
4. Count sets **fractionally**: direct = 1, indirect (synergist) = 0.5. Bench press counts 1 for chest and 0.5 each for front delts and triceps.
5. Weekly volume targets are in hard sets per muscle per week: hypertrophy beginner 8 (6–10), intermediate 12 (10–20), advanced/priority 16 (12–20, ≤~22 short-term), max strength 6 (4–10), maintenance 4–6. Diminishing returns ~18–20. [1][2]
6. Per-session soft cap: **10 fractional hard sets per muscle** (≈6–8 direct). Contested, preprint-derived; treat as a soft cap, not a hard rule. [3]
7. Report the score and any assumptions in a short block at the end of the plan (template below).
8. A numeric rule violated for a documented reason (injury, user request, time) is a Partial, not a Fail, if the plan states the reason.

## Scorecard

| # | Item | Crit? | Pass condition (numbers from canonical defaults) | Fix if it fails |
|---|---|---|---|---|
| 1 | **Goal alignment** | Yes | Primary goal is single and named. Reps/load/rest match it: strength ≥80% 1RM, 1–6 reps, 3 min rest; hypertrophy hard sets at any load, practical 6–15 reps (up to 30), 2 min compounds / 90 s isolation; power 30–70% 1RM, max-velocity intent, full rest, first in session; maintenance 4–6 sets/wk heavy. ≤1–2 secondary goals. | Re-pick rep range, load and rest from [goals](04-goals.md); drop extra goals; reorder power/strength first. |
| 2 | **Weekly sets per muscle in range** | | Every trained muscle within range for goal × level (see TL;DR 5), counted fractionally. Priority muscles at the top of the range; non-priority at 4–6 maintenance or the normal range. No muscle >20 (≤~22 specialization). No major muscle at 0 unless intentionally excluded. | Below range: add 1 set/muscle/wk to exercises already in the plan, or add a session. Above: remove sets from indirect-heavy exercises first, then isolation. |
| 3 | **Frequency** | | Each muscle 2×/wk by default. Allowed: 1× only if <~10 sets/wk or days <2; 3× for high volume. Strength lifts ≥2×/wk. | Re-split so each muscle gets two exposures (full body or upper/lower); see [splits](06-splits.md). |
| 4 | **Per-session cap** | | ≤10 fractional hard sets per muscle per session (≈6–8 direct); 2–4 sets/exercise (strength 2–3; up to 5 only for peaking/technique); 4–8 exercises per session. | Move surplus sets to another session; cut to 3 sets/exercise; merge redundant exercises. |
| 5 | **Pattern balance** | | Squat, hinge, horizontal push, horizontal pull, vertical push, vertical pull, plus core/carry are each present weekly (or the omission is stated, e.g. no vertical pull without a bar). Push:pull ≈ 1:1 or slightly more pulling (count sets). Single-leg work present when days allow. | Swap an exercise to fill the gap; add pulling sets to hit ≥1:1. |
| 6 | **Recovery spacing** | | Hard sessions for the same muscle are ≈48 h apart (≥1 day between; Practitioner). At least 1 full rest day/wk (or only easy aerobic on it). Hard intervals/long sessions not placed the day before heavy leg work or key runs. Concurrent sessions in one day ≥6 h apart or lift first when strength is the priority. | Reorder days; move conditioning off heavy leg days; convert one session to full rest. |
| 7 | **Effort (RIR)** | | Working sets at **2 RIR (RPE 8)**, range 1–3. Beginners, older adults, heavy barbell compounds: 3 RIR. Only isolation final sets go to 0–1 RIR. No routine failure. | Lower loads / stop sets earlier; remove "AMRAP/to failure" instructions on compounds. |
| 8 | **Progression rule** | | Each main lift has an explicit rule. Default: double progression (rep range + target RIR; add load when top of range is hit at target RIR). Beginner barbell lifts: linear +2.5 kg / 5 lb upper, +5 kg / 10 lb lower per session with a defined reset on failure. Rule states what to do on a miss. | Write the rule per lift from [progression](08-progression.md). |
| 9 | **Deload / mesocycle** | | Mesocycle 4–8 wk (default 5 working + 1 deload); volume ramp ≈ +1 set/muscle/wk; RIR falls 3 → 1; deload ≈1 wk, volume −30–50%, load mostly kept; also triggered by fatigue signals. Plateau rule: no progress 3–4+ wk with sleep/nutrition consistent → check fatigue, volume, technique first. Review date set. | Add deload week and trigger list; shorten the block if the person is older, in a deficit or sleeping poorly. |
| 10 | **Session structure** | | Warm-up 5–10 min general + ramp sets for the first lift. Order: power → strength → hypertrophy → isolation → core → conditioning (priority / most technical first). Rest: 3 min heavy compounds, 2 min hypertrophy compounds, 90 s isolation, beginner 90–120 s, never <60 s. Tempo controlled (0.5–8 s/rep; no reps >10 s). Full ROM default. | Reorder; add warm-up line; set rest per exercise. |
| 11 | **Time fit** | Yes | Summed session time ≤ stated minutes. Estimate: Σ(sets × (≈40 s work + rest)) + warm-up 5–10 min + transitions ~1 min/exercise. With 3-min/2-min/90-s rests a 5-exercise × 3-set session ≈ 45–60 min. Weekly day count ≤ stated days. | Over: antagonist/non-competing supersets (cut time with no outcome loss), 60–90 s rests on isolation, drop optional isolation, 1–2 hard sets per exercise. Never drop days to fit; cut sets. Under: add sets within range. |
| 12 | **Equipment fit** | Yes | Every exercise is doable with the stated equipment. No barbell lifts for a bodyweight-only user, etc. | Swap by pattern from [exercise library](12-exercise-library.md) / substitution matrix. |
| 13 | **Health floor, conditioning and substitutions** | Yes if sedentary/≥65 | (a) ≥2 d/wk muscle strengthening of all major groups. (b) Aerobic: 150–300 min/wk moderate OR 75–150 min/wk vigorous (1 vigorous ≈ 2 moderate), or a stated ramp for a sedentary user. Age ≥65: multicomponent (balance + strength) ≥3 d/wk. (c) Mostly easy (RPE 3–4) + 1–2 hard sessions/wk. (d) Lifters' cardio 2–3 sessions/wk, preferring cycling/rowing/incline walk, hard intervals away from heavy leg days. (e) Each main exercise has ≥1 listed substitution (equipment-down, pain-friendly). (f) A minimum-dose fallback session is given. | Add walking/zone-2 or a short interval session; add balance work; write substitutions from the matrix; write a 20–30 min fallback. |
| 14 | **Safety** | Yes | Intake red flags resolved (referral advised or none). Injuries/pain have same-pattern swaps; pain rule stated (≤3/10 during, settled by next day). Population modifiers applied (older, youth, pregnancy with clearance, obese/deconditioned start at RPE 5–6). No diagnosis or treatment advice. Beginners get no Olympic lifts or high-fatigue technical lifts. Assumptions listed. | Replace the offending exercise; add the referral line; downgrade intensity; list assumptions. |

## Scoring procedure

1. Score 1–14 in order; for each Partial, write the one-line gap.
2. Sum. Compute `score / 14`.
3. Decision:
   - **≥ 12.5 and all Critical items Pass** → output.
   - **10–12 or one non-Critical Fail** → apply fixes, re-run, then output; note remaining Partials.
   - **<10 or any Critical Fail** → rebuild from [principles](01-principles.md) step 3 (structure) or step 1 (intake) as indicated.
4. At most 2 fix-and-rerun cycles. If still failing, output with an explicit limitation note, or ask the user for the missing constraint.

## Compact audit worksheet (fill per plan)

```
PLAN QC
goal:                primary=___ secondary=___           [1] P/Pt/F
sets/muscle/wk:      ___ (target ___ for level ___)      [2] P/Pt/F
frequency:           min ___x/wk                          [3] P/Pt/F
per-session max:     ___ fractional sets (cap 10)         [4] P/Pt/F
patterns missing:    ___ ; push:pull = ___                [5] P/Pt/F
spacing violations:  ___                                  [6] P/Pt/F
RIR:                 ___ (default 2; 3 for beginner/older/heavy compounds)  [7]
progression rule:    ___ per main lift                    [8] P/Pt/F
deload/mesocycle:    ___ wk block, deload wk ___          [9] P/Pt/F
session structure:   warm-up ___ order ___ rest ___       [10] P/Pt/F
time:                est ___ min vs stated ___ min        [11] P/Pt/F
equipment:           violations ___                       [12] P/Pt/F
floor/cond/subs:     strength d/wk ___ aerobic min ___ subs ___ fallback ___  [13]
safety:              flags ___ pain rule ___ assumptions ___  [14]
SCORE: ___/14   CRITICAL FAILS: ___   DECISION: output / fix / rebuild
```

## Quick numeric reference (all binding defaults)

| Variable | Default | Range |
|---|---|---|
| Frequency per muscle | 2×/wk | 1× if <~10 sets; 3× high volume |
| Hard sets/muscle/wk | 8 / 12 / 16 (beg / int / adv-priority hypertrophy); 6 strength; 4–6 maintenance | 6–10 / 10–20 / 12–20 (≤~22) / 4–10 |
| Per-session soft cap | 10 fractional sets/muscle | Contested |
| Sets per exercise | 2–4 (strength 2–3) | up to 5 peaking |
| Effort | 2 RIR (RPE 8) | 1–3; 3 for beginners/older/heavy barbell |
| Load | hypertrophy any 30–100% 1RM, practical 6–15 reps (up to 30); strength ≥80%, 1–6 reps; power 30–70% | |
| Rest | 3 min heavy; 2 min hypertrophy compound; 90 s isolation; beginner 90–120 s; time-poor 60–90 s | never default <60 s |
| Exercises/session | 4–8 (45–75 min) | |
| Warm-up | 5–10 min + ramp sets | |
| Push:pull | ~1:1 or slightly more pull | |
| Mesocycle | 5 + 1 deload | 4–8 wk |
| Deload | ~1 wk, volume −30–50% | every 4–8 wk or on fatigue signals |
| Aerobic floor | 150–300 min moderate or 75–150 vigorous | + strength ≥2 d/wk |

## Decision rules

- IF a plan has high volume but the user has ≤2 days THEN fail #11/#3; rebuild as whole-body MED (1–3 compounds, 1–3 sets each, ≥2×/wk). [4]
- IF the weekly total is in range but one session carries >10 fractional sets for a muscle THEN fail #4, not #2; redistribute.
- IF set counts differ by method (direct-only vs fractional) THEN use fractional; direct-only counting fit worse in the dose-response data. [2]
- IF a fix for #2 (add sets) breaks #11 (time) THEN prefer supersets or a lower rest on isolation work before cutting sets below the range floor.
- IF the user is a beginner THEN accept the low end of #2 (6–10) and require #7 at 3 RIR and linear progression in #8.
- IF the user is older (≥65) THEN require power (fast concentric, 40–70% 1RM) and balance work in #13, 3 RIR in #7, and no routine failure.
- IF goal = fat loss THEN #2 stays in range and load is maintained; require resistance 3–4×/wk, steps, no cardio-only plan.
- IF hybrid (lifting + endurance) THEN #6 must separate hard runs from heavy leg days and keep interval/long sessions off the day before heavy lower-body work; same-session lifting goes first if strength is the priority. [5]
- IF a plan item rests on an unverified figure (e.g. "primary goal gets 60–70% of volume") THEN label it as a heuristic, do not use it as a Pass criterion.

## Common mistakes

- Counting only direct sets, then double-counting triceps and delts from pressing; use fractional counts.
- Scoring "frequency" by days per week instead of exposures per muscle.
- Treating the ~11-fractional-set per-session figure as a ceiling or the ~2-direct-set figure as a strength cap; they are points of undetectable further benefit from a preprint. [3]
- Skipping time arithmetic; plans that look fine often run 90+ min.
- Passing a plan with no substitutions or fallback session.
- Failing a plan for exceeding the weekly range by 1–2 sets when the reason is stated and recovery is fine.
- Using 2009 day-count staging (2–3 / 3–4 / 4–5 days) as a pass criterion; it is legacy and weakly supported. [1]
- Declaring a periodization model "wrong"; the model matters less than having progression. [6]

## Evidence notes

- Volume ranges: ACSM 2026 states ≥10 sets/muscle/wk for hypertrophy (Strong as ACSM text), diminishing returns ~18–20 (derived from Pelland 2025, so not independent). 8 / 12 / 16 level defaults and 6 for max strength are Practitioner/Moderate syntheses. [1][2]
- Per-session cap 10 fractional: Contested. Sits under the only quantified figure (~11 fractional, preprint PUOS) and matches the ACSM weekly floor. "6–10 direct per session" has no primary source. A 2026-10 preprint re-analysis suggests weekly volume, not its division into sessions, drives hypertrophy, which would weaken per-session caps (unreviewed). [3]
- Frequency: negligible effect on hypertrophy when volume is equated; ≥2 sessions helps strength. [1][7]
- 2 RIR: ACSM 2026 offers "near-failure or 2–3 RIR" but states exact RIR targets cannot be quantified; failure is not required. Experience-specific RIR is Practitioner. [1][8]
- Deload: Practitioner. Coleman 2024 (n=39) found a full rest week left hypertrophy unchanged and continuous training gave slightly better lower-body strength. [9]
- Rest: ACSM 2026 gives no rest guidance; defaults come from Singer 2024, Schoenfeld 2016 and Grgic 2018 (Moderate). [10]
- Push:pull ~1:1, ≈48 h spacing and the 12.5/14 pass threshold on this scorecard are Practitioner conventions; no injury trial supports a ratio.
- Interference: negligible for max strength and hypertrophy; only same-session / <3 h gaps for explosive strength. [5]
- Cool-down is optional and does not reduce soreness or speed recovery (low-quality evidence), so it is not scored.

## Sources

[1] Currier BS, D'Souza AC, Fiatarone Singh MA, et al. (Phillips SM senior). ACSM Position Stand: Resistance Training Prescription for Muscle Function, Hypertrophy, and Physical Performance in Healthy Adults: An Overview of Reviews. Med Sci Sports Exerc 58(4):851–872, 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC12965823
[2] Pelland JC, Remmert JF, Robinson ZP, Hinson SR, Zourdos MC. The Resistance Training Dose Response: Meta-Regressions Exploring the Effects of Weekly Volume and Frequency on Muscle Hypertrophy and Strength Gains. Sports Med 56(2):481–505, 2025/26. https://link.springer.com/article/10.1007/s40279-025-02344-w
[3] Remmert JF, Pelland JC, et al. Is There Too Much of a Good Thing? (per-session set volume meta-regression). SportRxiv preprint, 2025 (preprint). https://sportrxiv.org/index.php/server/preprint/view/537
[4] Androulakis-Korakakis P, Fisher JP, Steele J. The Minimum Effective Training Dose Required to Increase 1RM Strength in Resistance-Trained Men. Sports Med 50(4):751–765, 2020. https://doi.org/10.1007/s40279-019-01236-0 ; Nuzzo JL et al. Sports Med 54(5):1139–1162, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11127831
[5] Schumann M et al. Compatibility of Concurrent Aerobic and Strength Training for Skeletal Muscle Size and Function: An Updated Systematic Review and Meta-Analysis. Sports Med 52:601–612, 2022. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8891239/
[6] Moesgaard L et al. Effects of Periodization on Strength and Muscle Hypertrophy in Volume-Equated Resistance Training Programs. Sports Med 52(7):1647–1666, 2022. https://doi.org/10.1007/s40279-021-01636-1
[7] Schoenfeld BJ, Grgic J, Krieger J. How many times per week should a muscle be trained to maximize muscle hypertrophy? J Sports Sci 37(11):1286–1295, 2019. https://doi.org/10.1080/02640414.2018.1555906 ; Grgic J et al. Effect of Resistance Training Frequency on Gains in Muscular Strength. Sports Med 48:1207–1220, 2018. https://doi.org/10.1007/s40279-018-0872-x
[8] Robinson ZP et al. Sports Med 54(9):2209–2231, 2024. https://doi.org/10.1007/s40279-024-02069-2 ; Refalo MC et al. Sports Med 53:649–665, 2023. https://pmc.ncbi.nlm.nih.gov/articles/PMC9935748
[9] Coleman M et al. Gaining more from doing less? The effects of a one-week deload period during supervised resistance training on muscular adaptations. PeerJ 12:e16777, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC10809978
[10] Singer A et al. Give it a rest: a systematic review with Bayesian meta-analysis on the effect of inter-set rest interval duration on muscle hypertrophy. Front Sports Act Living 6:1429789, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11349676 ; Schoenfeld BJ et al. Longer Interset Rest Periods Enhance Muscle Strength and Hypertrophy in Resistance-Trained Men. J Strength Cond Res 30(7):1805–1812, 2016. https://doi.org/10.1519/JSC.0000000000001272 ; Grgic J et al. Sports Med 48(1):137–151, 2018. https://doi.org/10.1007/s40279-017-0788-x
