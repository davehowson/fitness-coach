# Verification: Conditioning, Hybrid, Goals & Programs

> Research agent output · Topic 13 · 2026-10-08

## Summary

- Audited `03-goals-and-types.md`, `08-conditioning.md`, `09-hybrid-training.md`, `11-reference-programs.md` against primary sources. "Confirmed" means I read the PubMed/Europe PMC abstract (or full text where noted) or the original/official program page myself. Abstract-only reads are flagged; full-text-only details I could not open are marked Unverifiable.
- **Headline numbers hold.** Schumann 2022 (−0.06 / −0.01 / −0.28), Huiberts (−0.43 males), Murlasits (+3.96 kg), Eddens (+6.91%), Robineau (0/6/24 h), Oliveira 2024 (SMD 0.24), Wewege 2017, Milanović 2015, Helgerud 2007, Gist 2014, Buist 2008 (20.8% vs 20.3%), Momma 2022, Mandsager 2018, WHO 2020 and the PAG wording all match the abstracts.
- **Real corrections:**
  - Schumann: training status is *not* a significant moderator. Only same-session vs ≥3 h gap moderated, and only for explosive strength.
  - Oliveira: the polarized VO2peak edge is limited to <12-week interventions and highly trained athletes. All other endpoints (time trial, TTE, VT2 power) were null.
  - Viana 2019 found interval training gave ~28.5% greater absolute fat-mass loss than MICT. Wewege 2017 found no difference. The wiki says "no difference" and should present both.
  - Wewege: running HIIT/MICT cut fat mass; *cycling did not*.
  - The "older adults multicomponent ≥3 days" figure is WHO 2020 only. The PAG key guideline (Piercy, JAMA 2018) gives no day count in its summary.
  - Starting Strength reset: the official article says a 5–10% reset, and a **second consecutive failure** triggers a 5% reset plus a light day. "3 failures" is wrong for SS. (StrongLifts and Reddit PPL do use "3 fails".)
  - nSuns: the original post sets weekly TM changes of 0–1 reps = none, 2–3 = +5 lb, 4–5 = +5–10 lb, >5 = +10–15 lb. The "+5/+10/+15" version is the Liftosaur implementation.
  - Higdon Novice 1: cutbacks are at weeks 3, 6, 9, 12, 14 and 16 (not only every 3rd week). The stated prerequisite is 3–4 running days/week and 15–20 mi/week for 1–2 years.
  - The 5/3/1 stall rule and TM-test week are r/Fitness wiki additions, "not part of the original article".
  - Wilson 2012 "50–60 vs 20–30 min/day" and "≤3 days/wk" are not in the abstract. They stay Unverifiable.
- **Goal-blend rule (#12) "primary goal ~60–70% of weekly hard-set volume":** no source found. Treat as Practitioner-only/author synthesis.
- Programs: full original/official structure verified for Starting Strength, StrongLifts 5x5, GZCLP (via r/Fitness wiki), 5/3/1 for Beginners (via wiki; Wendler's original article not retrievable), BBB (Wendler site), Madcow (StrongLifts guide), Texas Method (Barbell Medicine), Reddit PPL (archived original post), PHAT (Biolayne), Couch to 5K (NHS), Higdon Novice 1, r/bodyweightfitness RR (archived wiki). Not verifiable at original: Greyskull LP (Sheaffer), PHUL original, Texas Method 90% figure, nSuns set tables.

## Verification table

Grades use the 00-output-contract definitions (Strong / Moderate / Practitioner / Contested). "Abs." = abstract read; "FT" = full text read.

| # | Claim (as stated, file:section) | Verdict | Correct statement | Evidence grade | Source |
|---|---|---|---|---|---|
| 1a | Schumann 2022: max strength SMD −0.06, hypertrophy −0.01, explosive −0.28 (09:Key findings 1; 08:Key findings 9; 09:Exec summary) | **Confirmed** (Abs.) | 43 studies. Max strength −0.06 (95% CI −0.20 to 0.09, p=0.446); explosive −0.28 (−0.48 to −0.08, p=0.007); hypertrophy −0.01 (−0.16 to 0.18, p=0.919). Inclusion: supervised concurrent training ≥4 wk vs identical strength training without aerobic work. | Moderate (one large MA; conclusions consistent across subgroup analyses) | [S1] |
| 1b | Moderators: same session / <3 h gap / training status (brief; 09:Key findings 1; 08:Key findings 9) | **Corrected** | Only exercise timing moderated, and only for **explosive strength**: attenuation larger when done in the same session (p=0.043) than when sessions were ≥3 h apart (p>0.05). No significant moderation by aerobic type (cycling vs running), frequency (>5 vs <5 sessions/wk), **training status (untrained vs active)** or age (<40 vs >40). The abstract does not report sex. 08's "sex/training-status moderators … smaller interference in females" is not from Schumann; it belongs to Huiberts (#3). | Moderate | [S1] |
| 1c | "~1,090 subjects" (09:Exec summary / Key findings 1) | **Unverifiable** | Participant total is not in the abstract. Drop the number or confirm in the full text. | – | [S1] |
| 2a | Wilson 2012: 21 studies, 422 effect sizes; interference depends on modality, frequency, duration (09:Key findings 2; 08:Key findings 9) | **Confirmed** (Abs.) | 21 studies, 422 ESs. Mean ES, strength-only / endurance-only / concurrent: hypertrophy 1.23 / 0.27 / 0.85; strength 1.76 / 0.78 / 1.44; power 0.91 / 0.11 / 0.55 (concurrent < strength-only for power, all three groups differed). Running (not cycling) concurrent with RT gave significant decrements in hypertrophy and strength. Correlations with endurance frequency −0.26 to −0.35 and duration −0.29 to −0.75 for hypertrophy, strength and power. | Moderate | [S2] |
| 2b | "50–60 min/day associated with less gain than 20–30 min/day; ≤3 endurance days/wk less problematic" (09:Key findings 2; Numeric table) | **Unverifiable** | These thresholds are not in the abstract; the full text (JSCR) was not accessible. The abstract supports only the dose-response *direction* (negative correlations). Keep the table rows as Practitioner. | Practitioner | [S2] |
| 2c | Running vs cycling: "running interferes more" (09:Finding 3) | **Confirmed for Wilson; Contested overall** | Wilson: running yes, cycling no. Schumann: no moderation by running vs cycling. Both must be stated. | Contested | [S1][S2] |
| 2d | Hickson 1980 design: strength 5 d/wk + endurance 6 d/wk, 10 wk, strength plateau wk 7–8, fall wk 9–10 (09:Core concepts) | **Corrected** (Abs.) | Three groups: S (30–40 min/day, 5 d/wk), E (40 min/day, 6 d/wk), S+E (both). 10 weeks. S+E strength gains matched S for ~7 wk, then **leveled off and declined in weeks 9–10**. VO2max rose ~25% (bike) / ~20% (treadmill) in E and S+E, no change in S. Conclusion: concurrent training reduces strength development and does not affect VO2max gains. "3 cycling + 3 running" and "Hickson suspected overreaching" are **not in the abstract**: Unverifiable here. | Moderate (small historical study) | [S3] |
| 3 | Huiberts 2023/24: lower-body strength SMD −0.43 in males (09:Exec summary / Finding 5) | **Confirmed** (Abs.) | 59 studies, n=1346, ages 18–50. Lower-body strength: males −0.43 (−0.64 to −0.22); females 0.08 (−0.34 to 0.49); group difference P=0.03. No sex difference for upper-body strength (P=0.67), power (P=0.37) or VO2max (P=0.13). Hypertrophy data insufficient. **Training status:** *untrained* but not trained/highly trained endurance athletes had lower VO2max gains with concurrent training (P=0.04). No other status differences. Authors call for more female data. Volume/page numbers cited in 09 (54(2):485–503) were not checked. | Moderate / Contested for sex (sparse female data) | [S4] |
| 4 | Murlasits 2018: lifting first gives ~+4 kg lower-body 1RM (09:Finding 6) | **Confirmed** (Abs.) | Same-session strength→endurance vs endurance→strength: lower-body 1RM +3.96 kg (95% CI 0.81–7.10); VO2max +0.39 mL/kg/min (−1.03 to 1.81, n.s.). Eddens 2018 (10 studies, ≥5 wk): resistance→endurance gave **+6.91%** lower-body dynamic strength (CI 1.96–11.87, p=0.006); no effect for hypertrophy (1.15%, n.s.), static strength, VO2max or body fat. | Moderate | [S5][S6] |
| 5 | Spacing RCT 0 h vs 6 h vs 24 h (09:Finding 7) | **Confirmed** (Abs.) | Robineau et al., JSCR 2016;30(3):672–683. 58 amateur rugby players, 7 wk, randomized to CONT, C-0h, C-6h, C-24h or STR; 2 sessions/week of each quality, **strength always before aerobic**. Bench and half-squat gains were lower in C-0h than in C-6h, C-24h and STR. Isokinetic MVC at 180°/s was likely higher in C-24h and STR than C-0h *and* C-6h. VO2peak rose in all concurrent groups, more in C-24h than C-0h and C-6h. Authors: avoid <6 h between "contradictory qualities". Magnitude-based inference was used; the trial is small. 09's "6 h and 24 h were fine for strength" is slightly generous: C-6h was also below C-24h for MVC at 180°/s. | Moderate (single small RCT) | [S7] |
| 6 | Polarized vs other intensity distributions: SMD 0.24 VO2peak (08:Exec summary / Finding 3) | **Confirmed with major qualifier** (Abs.) | Oliveira, Boppre & Fonseca, Sports Med 2024 (PMID 38717713). 17 studies, n=437; POL superior for VO2peak SMD 0.24 (0.01–0.48; p=0.040; 11 studies, n=284; I²=0%; GRADE high certainty for that outcome). The edge appeared **only in <12-week interventions (SMD 0.40) and in highly trained athletes (SMD 0.46)**. Time trial (−0.01), time to exhaustion (0.30, n.s.) and speed/power at VT2/LT2 (0.04) were all null. Risk of bias: "some concern" for RCTs. | Moderate for VO2peak only; null for performance endpoints | [S8] |
| 7a | HIIT vs MICT, VO2max: Milanović 2015 (brief) | **Confirmed** (Abs.) | 28 controlled trials, n=723, healthy adults 18–45. Vs no-exercise controls: endurance +4.9 mL/kg/min; HIT +5.5. HIT vs endurance: "possibly small beneficial effect" +1.2 ±0.9 mL/kg/min. Larger HIT advantage with older subjects, longer intervals, longer interventions. 08's "as much as or more than MICT" is accurate. | Moderate | [S9] |
| 7b | Patient HIIT vs MICT (08 cites a secondary summary, S5 Liou) | **Confirmed via Weston 2014** (Abs.) | Weston, Wisløff & Coombes, BJSM 2014: 10 studies, n=273 patients with lifestyle-induced cardiometabolic disease; VO2peak MD 3.03 mL/kg/min (2.00–4.07), ~9.1%, HIIT > MICT. The 08 "CAD n=472; HF n=557" figures remain secondary and were not re-checked. | Moderate (patients) | [S10] |
| 7c | HIIT vs MICT, fat loss (08:Finding 6) | **Corrected / Contested** | Wewege 2017 (Obes Rev; 13 studies, 18–45 y, overweight/obese): both reduce fat mass and waist, **no significant difference**, HIIT ~40% less time. *Running* gave large effects (SMD −0.82 HIIT / −0.85 MICT) but **cycling did not reduce fat mass**. Viana 2019 (BJSM, 36 studies in meta-analysis): both reduce %BF; interval training gave **28.5% greater reduction in absolute fat mass (kg)** than MOD. The wiki should say "similar for %fat and waist, possible small edge for interval training in absolute fat mass (Viana), mostly driven by time-efficiency". The Keating 2017 and 2023 review (08 S8b) were not re-checked. | Moderate / Contested | [S11][S12] |
| 7d | Helgerud 4×4 (08:Finding 4) | **Confirmed** (Abs.) | n=40 moderately trained men, 8 wk, 3 d/wk, matched total oxygen consumption. 4×4 min at 90–95% HRmax with 3 min active rest at 70%: VO2max +7.2% (55.5→60.4). 15/15 intervals: +5.5% (60.5→64.4). Both significantly better than LSD (70% HRmax) and lactate-threshold (85% HRmax) training. SV +~10%. | Moderate (single RCT, men) | [S13] |
| 7e | SIT (Gist 2014) (08:Finding 5) | **Confirmed** (Abs.) | 16 RCTs, 17 effects, n=318: overall d=0.32 (~+3.6 mL/kg/min, ~8%); vs no-exercise controls d=0.69 (0.46–0.93); vs endurance-training controls d=0.04 (−0.17 to 0.24, n.s.). The "4–6 × 30 s, ~4 min recovery" protocol is not in the abstract (Practitioner). | Moderate | [S14] |
| 8a | Zone 2: no evidence it is uniquely superior; Z2 insufficient for VO2max (08:Finding 7) | **Confirmed in conclusion** (Abs. only) | Storoschuk et al., Sports Med 2025 (PMID 40560504): evidence "does not support Zone 2 training as the optimal intensity" for mitochondrial or fatty-acid oxidative capacity. Intensities >Zone 2 are "critical to maximize cardiometabolic health benefits, particularly in the context of lower training volumes". Recommendations stem largely from observational data on elite endurance athletes. Narrative review, not a meta-analysis. The finer sub-claims in 08 (e.g., "at equal volume, VO2max gains greater above Z2") need the full text. | Contested (narrative review) | [S15] |
| 8b | Talk test valid for VT1 (08:Finding 8) | **Confirmed** (Abs.) | Vieira et al., Rev Cardiovasc Med 2022 (PMID 39076925): 10 studies, n=414, mostly CAD; validity supported; reliability "satisfactory" but only one study had an adequate reliability analysis; last positive stage correlates with first ventilatory threshold; workload, VO2 and HR at the last positive stage did not differ from VT1. Evidence is mostly cardiac patients, not healthy trained people. | Moderate | [S16] |
| 8c | 10% rule: GRONORUN RCT 20.8% vs 20.3% (08:Finding 10) | **Confirmed** (Abs.) | Buist et al., AJSM 2008 (PMID 17940147): n=532 novice runners preparing for a 4-mile event; 13-wk graded plan (based on the 10% rule) vs 8-wk standard plan; RRI 20.8% vs 20.3%, χ²=0.016, P=.90. RRI = any lower-extremity/back complaint restricting running ≥1 wk. Note the graded plan was also *longer* (13 vs 8 weeks). The ">30% jump" cohort claim (Nielsen, via blog) was **not verified**. | Moderate | [S17] |
| 9a | Muscle-strengthening ~30–60 min/wk and mortality (Momma 2022) (03:Key findings 6) | **Confirmed** (Abs. + FT) | 16 prospective cohorts. Muscle-strengthening activity (MSA) linked to 10–17% lower risk of all-cause mortality, CVD, total cancer, diabetes and lung cancer. J-shaped for all-cause mortality, CVD and total cancer, maximum risk reduction ~10–20% at ~30–60 min/wk (the full text gives e.g. 17% at 40 min/wk for one outcome); L-shaped for diabetes. Combined MSA + aerobic vs none: all-cause mortality RR 0.60 (0.54–0.67) = 40% lower (FT). Authors state the effect of *higher* MSA volume is unclear (J-shape). GRADE in the supplementary table is "very low" for the site-specific cancer outcomes I saw. Observational. | Moderate → treat as low-to-moderate (observational) | [S18] |
| 9b | Cardiorespiratory fitness and mortality (Mandsager 2018) (03:Key findings 7) | **Confirmed** (Abs.) | 122,007 patients referred for symptom-limited treadmill testing at one academic centre (1991–2014), median follow-up 8.4 y, 13,637 deaths. Elite vs low: adjusted HR 0.20 (0.16–0.24) (~80% lower); elite vs high: HR 0.77 (0.63–0.95). Low vs elite HR 5.04; the mortality increase with low fitness was "comparable to or greater than" CAD (HR 1.29), smoking (1.41), diabetes (1.40). Retrospective, referred clinical sample (not general population). The AHA "clinical vital sign" statement (Ross 2016) was **not opened**: Unverifiable here. | Moderate (observational) | [S19] |
| 10a | WHO 2020 exact wording (03:Key findings 5; 08:Finding 1) | **Confirmed** (FT, PMC) | Adults: "at least 150–300 min of moderate-intensity aerobic physical activity, or at least 75–150 min of vigorous-intensity … or an equivalent combination … throughout the week" (strong recommendation). "Adults should also do muscle-strengthening activities at moderate or greater intensity that involve all major muscle groups on 2 or more days a week." Adults may go beyond 300 min moderate / 150 min vigorous. The 10-minute-bout requirement from WHO 2010 was removed. | Strong | [S20] |
| 10b | WHO older adults | **Confirmed** (FT) | "As for adults, plus … varied multicomponent physical activity that emphasises functional balance and strength training at moderate or greater intensity on 3 or more days a week, to enhance functional capacity and to prevent falls" (strong recommendation). | Strong | [S20] |
| 10c | US PAG 2018 (2nd ed.) wording (03:Key findings 5; Decision rule 17) | **Confirmed; Corrected for "≥3 days"** (JAMA summary Abs. + ODPHP page) | Adults "at least 150 minutes to 300 minutes a week of moderate-intensity, or 75 minutes to 150 minutes a week of vigorous-intensity aerobic physical activity, or an equivalent combination", plus "muscle-strengthening activities on 2 or more days a week". Older adults "should do multicomponent physical activity that includes balance training as well as aerobic and muscle-strengthening activities", **with no day count in the key guideline summary**. The "≥3 days" figure is WHO's. The 10-minute-bout rule was dropped in 2nd edition. The full PAG PDF could not be text-extracted here, so the unabridged wording was not checked. A third edition is in development (Call to Action, Transl J ACSM 2024): check whether 03 should cite a newer edition. | Strong | [S21][S22] |
| 11 | Reference programs | **See Program verification** | See per-program verdicts below. | – | – |
| 12 | Goal-blend rule "primary goal ~60–70% of weekly hard-set volume" (03:Exec summary) | **Unverifiable → Practitioner-only** | Searches for a source with this percentage returned nothing. Related ideas exist: "maintenance volume" for secondary qualities and "maximum compatible volume" for secondary priorities (coaching articles), but no 60–70% figure. The Schumann/Huiberts findings (#1, #3) say a moderate endurance dose does not cost strength/hypertrophy, which supports "secondary goal at maintenance-to-moderate dose" qualitatively. Label the 60–70% as the author's heuristic. | Practitioner | Research log |

## Program verification

Versions are noted because the r/Fitness wiki, apps and aggregators often differ from the originals.

### Starting Strength (Rippetoe) — **Confirmed (official site, archived 2024 copy)**
- **Structure:** Day A / Day B, three non-consecutive days/week (Mon/Wed/Fri). Three phases:
  - Phase 1 (usually 1–3 weeks): squat 3×5, press or bench 3×5 (alternate each session), deadlift 1×5, on both days.
  - Phase 2: Day B swaps the deadlift for **power clean 5×3**; Day A keeps deadlift 1×5.
  - Phase 3: Day A alternates deadlift 1×5 and power clean 5×3; Day B adds chin-ups (3 sets to fatigue; weighted 3×5 alternating once 3×10 bodyweight is reached). "Advanced novice": squat load increases only twice weekly with a lighter Wednesday squat.
- **Progression:** add weight every session. Healthy men 18–35/40: +10 lb on squat the first 2–3 sessions, +15–20 lb on deadlift the first couple of sessions then +10 lb, then +5 lb per workout; press/bench/power clean may start with one 10 lb jump or 5 lb jumps, later 2.5 lb or smaller. Women and older lifters: smaller jumps. By end of Phase 1, an 18–35 male: squat +40–50 lb, deadlift +50–70 lb, press/bench +15–20 lb.
- **Reset rules (official article, Alter 2018):** a reset is a 5–10% drop in loads with no programming change. The two numbers that matter: **second consecutive failure (same load) → reset 5% and make Day 2 a light squat day (80% × 2×5)**; if already doing that, switch to 5×3. First missed-rep session: repeat the load; if ≥4 reps on the first two sets, retry 3×5; if ≤3, same load at 5×3 with 2.5 lb jumps. Layoff: 1 week = repeat the last workout; longer = reset 5% (<40) or 10% (>40); 3–4 weeks = 10%. After a failed repeat/reset, change programs (Texas Method etc.) rather than resetting again.
- **Wiki flags:** 11 says "3 failed sessions"; the official text says second consecutive failure. 11's press/bench "pairing differs by source" is resolved: they **alternate every session**; the squat is 3×5 (not 5×5).
- Source: [S23][S24].

### StrongLifts 5x5 (Mehdi) — **Confirmed (official site)**
- **Structure:** A: squat 5×5, bench 5×5, barbell row 5×5. B: squat 5×5, overhead press 5×5, **deadlift 1×5**. Alternate A/B, 3×/week (Mon/Wed/Fri), ~3 min between sets. New lifters start with the empty 45 lb bar (squat/bench/OHP) and ~65–95 lb on rows/deadlifts.
- **Progression:** add 5 lb (2.5 lb/side) when all sets are completed; the site says "5 lb or less", every 1–5 workouts; microloading is endorsed. Deadlift-specific increments are not stated on the pages I read.
- **Failure:** repeat the weight; "if you repeat the weight three times but still fail" → **deload ~10%** and work back up. 11's "2 fails: repeat; 3rd consecutive fail −10%" is consistent. Healthline-style "every 5th week 50%" is not official.
- **Next programs listed:** Plus, Ultra, Ultra Max, Intermediate, Madcow, Lite, Mini.
- Source: [S25][S26][S27].

### GZCLP (Cody LeFever) — **Confirmed (r/Fitness wiki companion to original post)**
- Day 1: T1 squat, T2 bench, T3 lat pulldown. Day 2: OHP / deadlift / DB row. Day 3: bench / squat / lat pulldown. Day 4: deadlift / OHP / DB row. 3 non-consecutive days/week, rotating through the four days.
- Stages: T1 5×3+ → 6×2+ → 10×1+; T2 3×10 → 3×8 → 3×6; T3 3×15+ only. Rest T1 3–5 min, T2 2–3, T3 1–1.5. Last set of "+" sets is AMRAP, leaving 1–2 reps in reserve.
- Progression: after each workout +5 lb bench/OHP, +10 lb squat/deadlift (T1/T2). T3: add weight when 25 reps are reached on the AMRAP set.
- Failure: fail → next stage. After the last T1 stage, **test a new 5RM and restart at 85%**. T2: restart at the last Stage-1 weight +15–20 lb. Matches 11. Original post/infographic not opened directly.
- Source: [S28].

### Greyskull LP (Sheaffer) — **Unverifiable at original; secondary only**
- Original Sheaffer write-up not retrieved (r/Fitness wiki page 404 in Wave 1; not found again). Secondary sources agree on 3 days/week, A/B full body, **2×5 + final set 5+** on main lifts, deadlift 1×5+, upper +2.5 lb / lower +5 lb per session. Phrak's variant adds double jump at ≥10 AMRAP reps, −10% on missing 5 on the final set, plus chins/rows. 11's description of these as Phrak-variant is fair; do not present as "official".
- Source: [S29] (secondary; unchecked).

### 5/3/1 for Beginners (Wendler) — **Confirmed via r/Fitness wiki companion; Wendler original not retrieved**
- 3 days/week, full body, two main lifts/day (Mon: squat + bench; Wed: deadlift + OHP; Fri: bench + squat). Eight sets per lift (3 warm-up optional + 3 core + 5×5 FSL); third core set AMRAP; assistance: one push, one pull, one single-leg/core, **50–100 reps each**.
- Percentages of TM: Wk1 65/75/85×5,5,5+ then 5×5 @65%; Wk2 70/80/90 ×3,3,3+ then 5×5 @70%; Wk3 75/85/95 ×5,3,1+ then 5×5 @75%. Start TM = **90% of estimated 1RM** (from a 3–5 rep max with good bar speed).
- Progression: +5 lb TM upper, +10 lb lower per 3-week cycle, regardless of AMRAP performance.
- **Version note:** the TM-test week every 10th week and the "lower TM by three cycle increments (15/30 lb)" stall rule are described by the wiki as **not part of the original article**. 11 lists them as part of the program ("[S8]"). Mark as wiki-added guidance.
- Source: [S30].

### 5/3/1 BBB (Boring But Big) — **Confirmed (Wendler's own page)**
- 4 days/week, one main lift per day: 5/3/1 main sets + **5 sets of 10** of the same lift (Example 1) or the opposite lift (Example 2: press→bench, deadlift→squat, bench→press, squat→deadlift) with lat work (upper days) or abs (lower days).
- Load: "general rule of thumb is to use **50–60% of your Training Max**" for 5×10; new BBB lifters (especially lower body) should start light, **~30% TM**. Ascending/descending/up-down set variations exist. 11's "50→60% TM" is accurate; the Wave 1 "third-party" label can be upgraded.
- Source: [S31].

### Texas Method (Rippetoe) — **Structure Confirmed (Barbell Medicine reproduction); 90% figure Unverifiable**
- Week template (Barbell Medicine, citing "originally structured"): Day 1 Volume — squat 5×5, bench 5×5 (alternating with press 5×5 week to week), deadlift 1×5; Day 2 Light — squat 2×5 @ 80% of Day 1, press 3×5 (or bench 3×5 @ 90% of last week's Day 1), chins, back extensions; Day 3 Intensity — squat **5RM**, bench/press 3RM, power clean 3×5.
- Progression: set a new 5RM weekly (small increments). Stall remedies (11): cut volume-day sets, lower volume-day weight — consistent with Barbell Medicine's modification list but not re-read in the original Practical Programming text.
- The "volume day = 90% of Friday's 5RM" figure appears only in secondary pages (FitnessVolt etc.). Not verified in Rippetoe's text.
- Source: [S32].

### Madcow 5x5 — **Confirmed (StrongLifts' official Madcow guide, which reproduces "the original Madcow 5×5")**
- A (Mon, "medium"): squat 5×5 ramp, bench 5×5, row 5×5. B (Wed, "light"): squat 4×5, **incline bench (or OHP)** 4×5, deadlift 4×5. C (Fri, "heavy"): squat 4×5 + 1×3 + 1×8, bench same, row same. Assistance optional.
- **Ramp sets** at ~12.5% intervals: e.g., A squat 135/175/205/245/275 ×5; B repeats the first three ramps and repeats set 3 (205 = ~75% of A's top set); C top triple 280 (vs A's 275, i.e., ~+2% in the guide's example, **not "~105%"**) then 1×8 back-off at 205 (~75%).
- Progression: add weight to A's top set each week when 5 reps are completed (squat/deadlift +5 lb; bench/rows/OHP microload +2.5 lb); repeat if not. Rest 1–2 min on easy ramp sets, 3–5 min on heavy sets.
- Schedule/duration (8–12 weeks, first 3 weeks submax) and reset rules: **not found** in the guide. Keep as Practitioner.
- Source: [S33].

### nSuns 5/3/1 LP — **Corrected (original quoted via r/Fitness wiki)**
- Original poster's progression: TM starts at 90% of 1RM; one day a week an AMRAP set determines next week's TM change: **0–1 reps none; 2–3 reps +5 lb; 4–5 reps +5–10 lb; >5 reps +10–15 lb** (weekly cycle). 11's "+5 (2–3), +10 (4–5), +15 (6+)" is the Liftosaur app's version (and it is applied per session).
- Variants: 4-, 5-, 6-day spreadsheet. Two programmed lifts per day followed by accessories. The set tables in 11 (9 working sets, back-off sets) were **not verified** (spreadsheet not opened).
- Source: [S34].

### Reddit PPL (Metallicadpa) — **Confirmed (archived copy of the original r/Fitness post, 2024)**
- 6 days: PPLRPPL or PPLPPLR, recommended order pull-push-legs. Main lifts first, then accessories.
  - Pull: deadlift 1×5+ **or** barbell row 4×5 + 1×5+ (alternate each pull day), then pulldowns/pull-ups 3×8–12, seated cable/chest-supported row 3×8–12, face pulls 5×15–20, hammer curls 4×8–12, DB curls 4×8–12.
  - Push: bench 4×5 + 1×5+ **or** OHP (alternate), the other press 3×8–12, incline DB press 3×8–12, triceps pushdown superset lateral raise, overhead triceps extension superset lateral raise.
  - Legs: squat 2×5 + 1×5+, RDL 3×8–12, leg press 3×8–12, leg curls 3×8–12, calves 5×8–12.
- Progression: **+5 lb upper (bench, row, OHP), +5 lb squat, +10 lb deadlift** per session; accessories double progression (add weight at 3×12). Start weight: work up in 5s until bar slows, back off 5 lb.
- Failure: "fail a session 3 times in a row" → **deload 10%** and work back up. Rest 3–5 min main lift, 1–3 min others.
- **Version note:** 11 reported "+5 vs +10 lb" disagreement. The original is +5 lb for squat and all upper lifts, +10 for deadlift; "+10" appears in app copies. 11's "no AMRAP bench & OHP same day" is not in the original post: bench/OHP simply alternate as main vs accessory press.
- Source: [S35].

### PHUL (Brandon Campbell) — **Partially verified (secondary StrengthLog description; original M&S article not retrieved)**
- 4 days: upper power, lower power, upper hypertrophy, lower hypertrophy. Power days low reps (3–5 compounds), hypertrophy days moderate-high reps; 2–3 min rest on compounds, 1–2 min on isolation (StrengthLog). Progression: add reps first then weight (StrengthLog's example: 3×5 → 3×3 at higher load). Original Campbell article not read.
- Source: [S36] (secondary).

### PHAT (Layne Norton) — **Confirmed (Biolayne)**
- 5 training days + 2 rest: Day 1 upper power, Day 2 lower power, Day 3 rest, Day 4 back & shoulders hypertrophy, Day 5 lower hypertrophy, Day 6 chest & arms hypertrophy, Day 7 rest.
- Power days: 3–5 reps for 3–5 working sets on the big lift (compounds 3×3–5; some 5–8 and 6–10 assistance). Hypertrophy days start with **speed work 6–8 sets of 3 reps at 65–70% of 3–5RM** (missed in 11), then 8–12 / 12–15 / 15–20 rep work; rest 1–2 min; hypertrophy-day volume ~50–75% higher than power days.
- Not found on the Biolayne page: "4-week cycles ×3" and "rotate power lifts every 2–3 weeks" (11) — Unverifiable.
- Source: [S37].

### Couch to 5K (NHS) — **Confirmed (official)**
- 9 weeks, 3 runs/week with a rest day between, each run = 5-min warm-up walk + run/walk work + 5-min cool-down walk. Week 1: run 1 min / walk 1.5 min ×7 then a final 1-min run (28 min 30 s total). Week 2 starts run 1.5 min / walk 2 min ×5. Session totals (including 10 min of walking): Week 5 run 3 = 30 min (20 min continuous), Week 7 = 35 min (25 min), Week 9 = 40 min (30 min continuous). Repeating a run/week is explicitly allowed ("totally okay").
- Source: [S38].

### Hal Higdon Novice 1 — **Confirmed with corrections (official site)**
- 18 weeks; typical week: Mon rest, Tue/Wed/Thu runs, Fri rest, Sat long run, Sun cross-train (4 runs, 1 XT, 2 rest). Long run 6 mi (wk 1) → 20 mi (wk 15); then 3-week taper; week 8 is a half-marathon race; wk 18 is the marathon.
- Weekly long runs: 6, 7, **5**, 9, 10, **7**, 12, race, **10**, 15, 16, **12**, 18, **14**, 20, **12**, 8, race. So cutbacks at weeks 3, 6, 9, 12, 14 and 16 (not "3, 6, 9, 12" only). Mid-week runs 3/3–5/3 mi progressing to 5/10/5.
- Weekly total ~15 mi (wk 1) to ~40 mi (wk 15).
- **Prerequisite on the page:** "need to have been running 3–4 days a week for the last year or two and averaging 15–20 miles weekly". 11's decision rule "can run ~30 min" understates this; Higdon's Novice 1 is for first-time marathoners with an existing base.
- Source: [S39].

### r/bodyweightfitness Recommended Routine — **Confirmed (archived wiki, 2024); version note**
- 3×/week full body with ≥1 rest/skill day between. Warm-up 5–10 min (dynamic stretches, wrist prep, etc.); strength work 40–60 min: Pair 1 pull-up + squat progressions, Pair 2 dip + hinge, Pair 3 row + push-up, each 3×5–8 (rest 90 s between the pair's alternating sets; up to 3 min if reps drop); core triplet 3×8–12 (anti-extension, anti-rotation, extension) with 60 s rests. Tempo ideally 1-0-X-0.
- Progression: pick a progression for 3×5, add a rep per set until **3×8**, then move to the next progression at 3×5. Isometric holds: move on at 30 s for all 3 sets (10–30 s range).
- **Version note:** 11 describes a "10 min skill block". The 2024 archive has no skill block (a FAQ mentions the routine "looks different from how I remember"). Pre-2024 versions had one.
- Source: [S40].

### Not re-verified
Candito 6-week, Sheiko, RP, Nippard, Convict Conditioning, Boostcamp/Viada hybrid examples: outside the brief's list; no change.

## Corrections for the wiki

- **`03-goals-and-types.md`**
  - Line ~14 goal-blend: relabel "primary goal ~60–70% of weekly hard-set volume" as an author heuristic with no source (Practitioner, unsourced).
  - Key finding 6: keep "10–17% lower risk, J-shaped, max reduction ~10–20% at ~30–60 min/wk, combined with aerobic RR 0.60 (40% lower all-cause mortality)", but add "observational; authors say benefit of higher MSA volume unclear; GRADE very low for several outcomes".
  - Key finding 7: add that Mandsager is a single-centre retrospective cohort of treadmill-referred patients (elite vs low HR 0.20; elite vs high HR 0.77). Remove or source the AHA "vital sign" claim (Ross 2016 not opened).
  - Key finding 5 / Decision rule 17: attribute the "multicomponent ≥3 days/week" to WHO 2020, not PAG; PAG gives no day count in its key guideline. Check whether the PAG 3rd edition has replaced the 2018 numbers.
  - Concurrent-training lines: use the Schumann moderators as in #1b (only timing, only for explosive strength).
- **`08-conditioning.md`**
  - Exec summary/Finding 3 (polarized): add "<12-week interventions and highly trained athletes only; TT, TTE and VT2 power null; GRADE high for VO2peak; no recreational data".
  - Finding 9: remove "Sex/training-status moderators … in Schumann/[S12]". Schumann found no training-status moderation; the sex finding is Huiberts (lower-body strength, males −0.43). "Larger when <3 h apart" applies to explosive strength only. Wilson's "50–60 vs 20–30 min" and "≤3 d/wk" remain unverified.
  - Finding 6 (fat loss): replace "no significant difference" with "Wewege 2017: no difference, ~40% less time; running worked, cycling did not reduce fat mass. Viana 2019: interval training 28.5% greater absolute fat-mass loss. Treat as small/inconsistent".
  - Finding 4: replace the secondary CAD/HF numbers with Weston 2014 (+3.03 mL/kg/min, 9.1%, n=273) and Milanović 2015 (healthy adults: HIT vs endurance +1.2 ±0.9 mL/kg/min "possibly small").
  - Finding 4 (Helgerud): give both protocols: 4×4 +7.2%, 15/15 +5.5%, vs LSD and LT groups (n=40 men, 8 wk, 3 d/wk).
  - Finding 10: note the graded GRONORUN plan was 13 weeks vs 8 weeks (so duration differed too); drop or source the ">30% jump" cohort claim.
  - Finding 7 (Zone 2): label "narrative review, abstract-verified"; remove sub-claims not in the abstract unless the full text is read.
- **`09-hybrid-training.md`**
  - Exec summary/Finding 1: delete "~1,090 subjects" unless confirmed; "no significant moderation … training status" is correct for Schumann.
  - Core concepts (Hickson): keep "10 weeks, S 5 d/wk, E 6 d/wk, strength plateau then decline weeks 9–10, VO2max unaffected (~20–25% gains in E and S+E)". Drop or mark unverified "3 cycling + 3 running" and "Hickson suspected overreaching".
  - Finding 2: mark the 50–60 vs 20–30 min and ≤3 d/wk figures as unverified secondary; Numeric table rows stay Practitioner.
  - Finding 5 (Huiberts): add the untrained-only VO2max impairment (P=0.04) and that training status did not moderate strength/power; keep the female-sparse-data caveat.
  - Finding 7 (Robineau): add "strength always before aerobic; 2 sessions/wk each; C-6h MVC at 180°/s also below C-24h".
- **`11-reference-programs.md`**
  - Starting Strength row: reset trigger = second consecutive failure → 5% reset + light day (80% 2×5), then 5×3, per official article; general reset range 5–10%; add phases 1–3 (power clean 5×3 on B from Phase 2; chins from Phase 3) and that press/bench **alternate every session**.
  - StrongLifts: cite official pages (not FitnessVolt/Healthline); "repeat three times and still fail → deload ~10%".
  - GZCLP row stands (cite the wiki companion).
  - Greyskull: keep "Phrak variant" labels; add "original not verified".
  - 5/3/1 for Beginners: label TM-test week and stall rule as wiki-added; BBB: cite Wendler (5×10 @ 50–60% TM, start ~30% for new BBB lifters, two example layouts).
  - Texas Method: add the verified template (volume squat 5×5, light squat 2×5 @80%, intensity 5RM/3RM, power clean 3×5); mark 90% as secondary.
  - Madcow: replace "Fri ramp to a 3 (~105% of Mon)" with "top triple slightly above Monday's top set (guide example 280 vs 275); back-off 1×8 at ~75%", and note A/B/C are Mon/Wed/Fri with B = light.
  - nSuns: replace the +5/+10/+15 rule with the original weekly 0–1 / 2–3 / 4–5 / >5 → none / +5 / +5–10 / +10–15 lb; label the app rule as Liftosaur's.
  - Reddit PPL: increments +5 lb upper & squat, +10 lb deadlift (original); main-lift structure per original (DL/row alternate; bench/OHP alternate; squat 2×5+1×5+); delete "no AMRAP bench & OHP same day".
  - PHAT: add the speed-work block; remove "4-week cycles ×3"/"rotate power lifts" or mark unverified.
  - Higdon Novice 1: cutbacks at weeks 3, 6, 9, 12, 14, 16; prerequisite = established running base (3–4 d/wk, 15–20 mi/wk for 1–2 years); Decision rule 10 should not say "can run ~30 min".
  - RR: remove the "10 min skill block" or flag as a pre-2024 version.
  - Couch to 5K: fine as written; add "run 1.5 min/walk 2 min" in Week 2 if more detail is wanted.

## Research log

- **Tools:** PubMed E-utilities `esearch`+`efetch` (abstracts), Europe PMC REST (`search` and `fullTextXML`), `curl` with a browser user-agent for author/official pages, Wayback Machine (`web.archive.org/web/2024/<url>`) for Starting Strength, Reddit (PPL, RR), WebSearch/WebFetch for locating pages. WebFetch alone returned 403 for startingstrength.com; the Wayback copy worked. PDF text extraction was unavailable (no `pdftotext`/`pypdf`), so the full PAG 2nd-edition PDF was not read; I used the JAMA summary abstract and the ODPHP page instead.
- **Abstract/full-text reads:** Schumann (PMID 34757594), Wilson (22002517), Huiberts (37847373), Murlasits (28783467), Eddens (28917030), Robineau (25546450), Hickson (7193134), Buist (17940147), Oliveira (38717713), Storoschuk (40560504 via Europe PMC), Wewege (28401638), Viana (30765340, abstract only truncated by Europe PMC; conclusion read), Milanović (26243014), Weston (24144531), Helgerud (MSSE 2007), Gist (24129784), Vieira talk test (39076925), Momma (35228201; PMC9209691 full text for RR 0.60), Mandsager (30646252 via PubMed text), WHO 2020 (PMC7719906 full text), Piercy PAG (30418471).
- **Not opened / still unverified:** Wilson full text (modality/duration thresholds); Hickson full text (3+3 cycling/running; overreaching comment); Held 2026 umbrella review (09 mentions as secondary); Keating 2017 and 2023 fat-loss review; Liou CAD and HF meta-analyses; Nielsen cohort (>30% jumps); Ross 2016 AHA statement; San-Millán primary papers; Wendler's original 5/3/1 for Beginners article (jimwendler.com pages for it did not surface); Sheaffer's Greyskull original; Brandon Campbell's PHUL original; Rippetoe *Practical Programming* (Texas Method 90%); nSuns spreadsheet.
- **Searches that failed:** a first Greyskull search returned He-Man toy listings; a first nSuns search returned unrelated results (retried successfully). No source found for the 60–70% goal-blend rule.
- **Note on date:** Schumann et al. 2022 was published open-access (PMC8891239); Huiberts epub 2023 (PMC10933151). Both abstract reads cover the headline numbers; per-moderator p-values beyond those in the abstract were not verified.

## Sources

[S1] Schumann M, Feuerbacher JF, Sünkeler M, Freitag N, Rønnestad BR, Doma K, Lundberg TR. Compatibility of Concurrent Aerobic and Strength Training for Skeletal Muscle Size and Function: An Updated Systematic Review and Meta-Analysis. Sports Med 2022;52(3):601–612. https://pubmed.ncbi.nlm.nih.gov/34757594/ (PMC8891239)
[S2] Wilson JM, Marin PJ, Rhea MR, Wilson SM, Loenneke JP, Anderson JC. Concurrent training: a meta-analysis examining interference of aerobic and resistance exercises. J Strength Cond Res 2012;26(8):2293–2307. https://pubmed.ncbi.nlm.nih.gov/22002517/
[S3] Hickson RC. Interference of strength development by simultaneously training for strength and endurance. Eur J Appl Physiol 1980;45(2–3):255–263. https://pubmed.ncbi.nlm.nih.gov/7193134/
[S4] Huiberts RO, Wüst RCI, van der Zwaard S. Concurrent Strength and Endurance Training: A Systematic Review and Meta-Analysis on the Impact of Sex and Training Status. Sports Med 2024 (epub 2023). https://pubmed.ncbi.nlm.nih.gov/37847373/ (PMC10933151)
[S5] Murlasits Z, Kneffel Z, Thalib L. The physiological effects of concurrent strength and endurance training sequence: a systematic review and meta-analysis. J Sports Sci 2018;36(11):1212–1219. https://pubmed.ncbi.nlm.nih.gov/28783467/
[S6] Eddens L, van Someren K, Howatson G. The Role of Intra-Session Exercise Sequence in the Interference Effect: A Systematic Review with Meta-Analysis. Sports Med 2018;48(1):177–188. https://pubmed.ncbi.nlm.nih.gov/28917030/
[S7] Robineau J, Babault N, Piscione J, Lacome M, Bigard AX. Specific Training Effects of Concurrent Aerobic and Strength Exercises Depend on Recovery Duration. J Strength Cond Res 2016;30(3):672–683. https://pubmed.ncbi.nlm.nih.gov/25546450/
[S8] Oliveira, Boppre & Fonseca. Comparison of Polarized Versus Other Types of Endurance Training Intensity Distribution on Athletes' Endurance Performance: A Systematic Review with Meta-analysis. Sports Med 2024. https://pubmed.ncbi.nlm.nih.gov/38717713/ (PMC11329428; DOI 10.1007/s40279-024-02034-z)
[S9] Milanović Z, Sporiš G, Weston M. Effectiveness of High-Intensity Interval Training (HIT) and Continuous Endurance Training for VO2max Improvements: A Systematic Review and Meta-Analysis of Controlled Trials. Sports Med 2015;45(10):1469–1481. https://pubmed.ncbi.nlm.nih.gov/26243014/
[S10] Weston KS, Wisløff U, Coombes JS. High-intensity interval training in patients with lifestyle-induced cardiometabolic disease: a systematic review and meta-analysis. Br J Sports Med 2014;48(16):1227–1234. https://pubmed.ncbi.nlm.nih.gov/24144531/
[S11] Wewege M, van den Berg R, Ward RE, Keech A. The effects of high-intensity interval training vs. moderate-intensity continuous training on body composition in overweight and obese adults: a systematic review and meta-analysis. Obes Rev 2017;18(6):635–646. https://pubmed.ncbi.nlm.nih.gov/28401638/
[S12] Viana RB et al. Is interval training the magic bullet for fat loss? A systematic review and meta-analysis comparing moderate-intensity continuous training with high-intensity interval training (HIIT). Br J Sports Med 2019. https://pubmed.ncbi.nlm.nih.gov/30765340/ (DOI 10.1136/bjsports-2018-099928)
[S13] Helgerud J et al. Aerobic high-intensity intervals improve VO2max more than moderate training. Med Sci Sports Exerc 2007. https://pubmed.ncbi.nlm.nih.gov/17414804/ (DOI 10.1249/mss.0b013e3180304570)
[S14] Gist NH, Fedewa MV, Dishman RK, Cureton KJ. Sprint interval training effects on aerobic capacity: a systematic review and meta-analysis. Sports Med 2014. https://pubmed.ncbi.nlm.nih.gov/24129784/
[S15] Storoschuk KL, Moran-MacDonald A, Gibala MJ, Gurd BJ. Much Ado About Zone 2: A Narrative Review Assessing the Efficacy of Zone 2 Training for Improving Mitochondrial Capacity and Cardiorespiratory Fitness in the General Population. Sports Med 2025. https://pubmed.ncbi.nlm.nih.gov/40560504/ (DOI 10.1007/s40279-025-02261-y)
[S16] Vieira AM et al. Application and Measurement Properties of the Talk Test in Cardiopulmonary Patients: A Systematic Review. Rev Cardiovasc Med 2022;23(7):225. https://pubmed.ncbi.nlm.nih.gov/39076925/
[S17] Buist I, Bredeweg SW, van Mechelen W, Lemmink KA, Pepping GJ, Diercks RL. No effect of a graded training program on the number of running-related injuries in novice runners: a randomized controlled trial. Am J Sports Med 2008;36(1):33–39. https://pubmed.ncbi.nlm.nih.gov/17940147/
[S18] Momma H, Kawakami R, Honda T, Sawada SS. Muscle-strengthening activities are associated with lower risk and mortality in major non-communicable diseases: a systematic review and meta-analysis of cohort studies. Br J Sports Med 2022;56(13):755–763. https://pubmed.ncbi.nlm.nih.gov/35228201/ (full text PMC9209691)
[S19] Mandsager K, Harb S, Cremer P, Phelan D, Nissen SE, Jaber W. Association of Cardiorespiratory Fitness With Long-term Mortality Among Adults Undergoing Exercise Treadmill Testing. JAMA Netw Open 2018;1(6):e183605. https://doi.org/10.1001/jamanetworkopen.2018.3605
[S20] Bull FC et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. Br J Sports Med 2020. https://pmc.ncbi.nlm.nih.gov/articles/PMC7719906/
[S21] Piercy KL et al. The Physical Activity Guidelines for Americans. JAMA 2018;320(19):2020–2028. https://pubmed.ncbi.nlm.nih.gov/30418471/
[S22] ODPHP, Physical Activity Guidelines for Americans, 2nd ed. – Top 10 things to know. https://odphp.health.gov/our-work/nutrition-physical-activity/physical-activity-guidelines/current-guidelines/top-10-things-know ; PAG 2nd ed. PDF (not text-extracted) https://odphp.health.gov/sites/default/files/2019-09/Physical_Activity_Guidelines_2nd_edition.pdf ; third-edition call to action: https://pmc.ncbi.nlm.nih.gov/articles/PMC11926852/
[S23] Starting Strength, Programs (Wayback copy, 2024). https://web.archive.org/web/2024/https://startingstrength.com/get-started/programs
[S24] Alter R. The Reset: Why and How. Starting Strength, 3 Oct 2018 (Wayback copy). https://web.archive.org/web/2024/https://startingstrength.com/article/the-reset-why-and-how
[S25] Mehdi. Stronglifts 5×5 Workout Program: Quick Start Guide. https://stronglifts.com/stronglifts-5x5/workout-program/
[S26] Mehdi. How to Progress on Stronglifts 5×5. https://stronglifts.com/stronglifts-5x5/progress/
[S27] Mehdi. How to Overcome Failure on Stronglifts 5×5. https://stronglifts.com/stronglifts-5x5/failure/
[S28] The Fitness Wiki (r/Fitness), GZCLP (companion to Cody LeFever's original post). https://thefitness.wiki/routines/gzclp/
[S29] Greyskull LP secondary descriptions: https://fitnessvolt.com/rpe-training/programs/greyskull-lp/ ; https://www.liftosaur.com/programs/phrakgreyskull (not original; unchecked)
[S30] The Fitness Wiki, 5/3/1 for Beginners. https://thefitness.wiki/routines/5-3-1-for-beginners/
[S31] Wendler J. Boring But Big — Jim Wendler's 5/3/1 Assistance Program. https://www.jimwendler.com/blogs/jimwendler-com/101077382-boring-but-big
[S32] Feigenbaum J. 12 Ways To Skin The Texas Method. Barbell Medicine (updated 2023). https://www.barbellmedicine.com/blog/12-ways-to-skin-the-texas-method/
[S33] Mehdi. Madcow 5×5 Workout: The Official Guide (reproduces original Madcow). https://stronglifts.com/stronglifts-5x5/workout/ (served at this URL; also https://stronglifts.com/madcow-5x5/workout-guide/)
[S34] The Fitness Wiki, nSuns LP (quotes u/nSuns original post). https://thefitness.wiki/routines/nsuns-lp/
[S35] Metallicadpa. A Linear Progression Based PPL Program for Beginners. r/Fitness, 2015 (Wayback copy, 2024). https://web.archive.org/web/2024/https://www.reddit.com/r/Fitness/comments/37ylk5/a_linear_progression_based_ppl_program_for/
[S36] StrengthLog, PHUL workout routine (secondary). https://strengthlog.com/phul-workout-routine/
[S37] Norton L. PHAT – Power Hypertrophy Adaptive Training. Biolayne. https://biolayne.com/articles/training/phat-power-hypertrophy-adaptive-training/
[S38] NHS, Couch to 5K running plan. https://www.nhs.uk/better-health/get-active/get-running-with-couch-to-5k/couch-to-5k-running-plan/
[S39] Higdon H. Novice 1 Marathon Training Program. https://www.halhigdon.com/training-programs/marathon-training/novice-1-marathon/
[S40] r/bodyweightfitness, Recommended Routine (Wayback copy, 2024). https://web.archive.org/web/2024/https://www.reddit.com/r/bodyweightfitness/wiki/kb/recommended_routine/
