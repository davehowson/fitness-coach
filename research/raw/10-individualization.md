# Individualization & Special Populations

> Research agent output · Topic 10 · 2026-10-08

Scope note: this file is training-program design guidance, not medical advice. Where a population has a medical condition, the rule is "get clearance / refer", not "treat".

Verification note: search tools returned abstracts and secondary summaries for several papers. Numbers marked **(secondary)** were not checked against the full primary text. Numbers marked **(background)** come from the author's prior knowledge and were not confirmed online in this session. The LLM consumer should prefer conservative defaults for those.

## Executive summary

- Individualization changes **dose, complexity, exercise selection and progression speed**, not the underlying principles. The 2026 ACSM position stand finds training experience had minimal impact on strength and hypertrophy outcomes for most variables, so the same core template (≥2 days/wk, ≥10 hard sets/muscle/wk for hypertrophy, 2–3 sets/exercise for strength, stop ~2–3 RIR) applies to novices through experienced lifters [S1]. Beginners just need less volume to progress and get simpler programs.
- Classify experience by **progression behavior and technique**, not years: beginner = linear session-to-session load gains; intermediate = week-to-week or monthly gains; advanced = gains over months, needs periodization (ACSM 2009: novice ≈ untrained or off for years; intermediate ≈ ~6 months consistent training; advanced = years) [S2].
- **Older adults (65+)**: resistance training is the highest-value intervention; add power (fast concentric, 40–70% 1RM), balance, and multicomponent work ≥3 days/wk (WHO) [S3][S4][S5]. Avoid failure training in many older people (vascular/injury risk) [S1]. Strength loss from layoffs is ~2× that of younger adults [S9].
- **Women** need no fundamentally different programming. Relative hypertrophy and lower-body strength gains are similar to men; relative upper-body strength gains are equal or greater in women [S6][S7]. **Menstrual-cycle-based programming is not supported**: evidence is low quality and inconsistent [S8]. Pregnancy/postpartum: continue/start exercise with clinician clearance [S10].
- **Youth**: supervised, technique-first resistance training is considered safe and beneficial by international consensus; low volume, 2–3 non-consecutive days/wk [S11].
- **Time-poor**: frequency matters less than total hard weekly sets. Strength is gained with as little as 1 hard set/exercise or one ~20–30 min session/wk; hypertrophy needs more (≈4+ sets/muscle/wk detectable, ≥10 for good growth) [S1][S12][S13].
- **Home/bodyweight**: low-load training near failure produces hypertrophy similar to heavy loading; strength gains slightly lower [S14][S1]. Overload comes from leverage, tempo, unilateral work, ROM, reps-to-near-failure, not just weight.
- **Layoffs**: strength mostly preserved for ~4 weeks (younger); regaining takes about **half** the time off [S9]. Re-start at ~⅓ of old loads (week 1), ramp over several weeks.
- **Recovery** (sleep, stress, nutrition): multi-night sleep restriction impairs maximal compound-lift output [S15]. Reduce volume/intensity ceilings when recovery is poor; do not stack high volume on poor sleep + high stress.
- **Injury/pain**: work around, don't through; substitute by movement pattern (matrix below); use a pain-monitoring rule (≤ ~3–5/10 during, settled by next day) as a conservative practitioner convention, and **refer** for red flags [S16].

## Core concepts

**Individualization = matching inputs to dials.** The general plan (Topics 02–09) gets adjusted by: training age, age/sex/life-stage, time, equipment, injury, recovery capacity. Order of operations for an LLM: (1) safety screen → (2) constraints (time, equipment, injuries) → (3) experience level → (4) population modifiers → (5) recovery-based volume adjustment.

**Training-experience classification (generic → specific).**
- *Beginner*: <~6–12 months consistent training or returning after ≥1 year off. Adds load nearly every session; most gains come from neural/skill adaptation early. Low volume is sufficient. Needs simple movements, high repetition of few exercises.
- *Intermediate*: ~1–3 years consistent. Load increases weekly–monthly; needs more volume, rep-range/RIR management, some variation.
- *Advanced*: multi-year; progress over months; needs periodization/deloads, specialization, more exercise variety to manage joint stress.
- Behavior-based test: "Can the lifter add weight or a rep to main lifts each session (beginner), each week (intermediate), each block (advanced)?" This is a practitioner heuristic (Practitioner), consistent with ACSM's staged recommendations [S2].

**Mechanisms relevant to special cases.**
- *Sarcopenia/age*: muscle power declines faster than strength and correlates strongly with physical function, hence power training [S5].
- *Muscle memory*: prior training leaves lasting adaptations. Myonuclear permanence is plausible but evidence is conflicting (animal-heavy; human data mixed) [S17]. Practically, retraining is faster than initial training regardless of mechanism [S9].
- *Low-load training*: when sets approach failure, motor-unit recruitment is high enough that hypertrophy is similar across 30–100% 1RM [S1][S14].

## Key findings

1. **Core template is largely experience-independent in effect.** ACSM 2026 overview of reviews: ≥2 days/wk, ≥10 sets/muscle/wk for hypertrophy (diminishing returns ≳18–20), 2–3 sets/exercise for strength, loads ≥80% 1RM for max strength, 30–100% 1RM for hypertrophy, 30–70% for power, near-failure (~2–3 RIR) not required to failure; periodization not clearly superior to non-periodized with progressive overload; training experience had minimal impact on outcomes. Scope is healthy adults only (excludes obesity, sarcopenia, frailty as clinical populations). **Strong** [S1].
2. **Older ACSM staging by experience (2009).** Novice: 8–12RM, 2–3 d/wk. Intermediate: 1–12RM periodized, 3–4 d/wk. Advanced: 1–12RM with emphasis on heavy 1–6RM, 3–5 min rest, 4–5 d/wk. Load increase 2–10% when 1–2 reps over target. Criticized for weak evidence synthesis; use as practitioner staging. **Moderate/Practitioner** [S2] (secondary).
3. **Older adults benefit substantially from resistance training; NSCA position statement (Fragala 2019) endorses RT for older adults including those with disabilities or in assisted living, with adapted programs.** Detailed dosing was not retrievable in-session. **Strong (position stand)** [S3]. Dosing specifics: see rules below, built from [S4][S5].
4. **WHO 2020**: all adults ≥2 days/wk muscle strengthening; adults ≥65 add multicomponent (balance + strength + coordination) activity ≥3 days/wk to prevent falls; 150–300 min/wk moderate aerobic. **Strong (guideline)** [S4] (the ≥2 d/wk figure is from background; the 3+ d multicomponent figure was confirmed secondarily).
5. **Power training in older adults**: meta-analysis of 20 RCTs (n=566): modest improvement in physical function vs traditional strength training; no difference in strength, mass or gait speed; low-certainty evidence; typical protocol 12 wks, 1–3 d/wk, 2–4 sets, 40–70% intensity. **Moderate** [S5].
6. **Sex differences**: meta-analysis of 10 studies: no sex difference in relative hypertrophy (ES 0.07) or lower-body strength; upper-body relative strength gains favored women (ES −0.60, heterogeneous). 2025 Bayesian meta-analysis: absolute muscle gain slightly favors males (upper body), relative gains similar. Older adults: absolute size gains favor men; relative similar. **Moderate-Strong** [S6][S7].
7. **Menstrual cycle**: umbrella review of meta-analyses/systematic reviews concludes it is premature to claim cycle phase appreciably alters acute performance, strength or hypertrophy adaptations; the literature is low quality, with poor phase verification. Only soreness markers showed trivial–small effects. **Moderate** (evidence of absence is weak; "no reliable basis for phase-periodization") [S8].
8. **Pregnancy/postpartum**: ACOG Committee Opinion 804: for uncomplicated pregnancies exercise is safe and desirable; previously active women can continue vigorous activity; ≈150 min/wk moderate aerobic; avoid activities with abdominal-trauma risk or scuba; individualize and do clinical evaluation first; resume postpartum as encouraged. **Strong (professional guideline)** [S10] (secondary).
9. **Youth**: 2014 international consensus (UKSCA-derived, endorsed by AAP, AMSSM and others) supports youth resistance training as safe and effective when qualified-supervised and technique-focused. Specific set/rep numbers were not retrievable in-session; widely cited defaults: 1–3 sets of 6–15 reps, 2–3 non-consecutive days **(background)**. **Strong (consensus)** [S11].
10. **Minimum effective dose**: a 2024 overview (Nuzzo) finds all minimal-dose approaches raise strength; single-set resistance exercise and "weekend warrior" (concentrated weekly session) are best supported. A SportRxiv preprint (67 studies) estimated ~1 set/wk for small strength gains and ~4 sets/wk as minimum for detectable hypertrophy, diminishing beyond ~12–20 (preprint, unreviewed, secondary). ACSM 2026 states minimal doses produce meaningful gains but need more study. **Moderate** [S1][S12][S13].
11. **Frequency vs volume**: when volume is equated, hypertrophy does not differ between 1 and >5 days/wk (ACSM 2026); earlier meta-analysis recommended ≥2×/wk as default, noting confounding by volume. **Moderate-Strong** [S1][S18].
12. **Low-load / bodyweight training**: meta-analysis of fiber hypertrophy at failure: no significant difference low vs high load (very wide intervals). Whole-muscle: similar hypertrophy, lower strength gains with low load. Push-up studies (small, untrained men) show hypertrophy at near-failure; no meta-analysis isolating bodyweight exercises. **Moderate** [S14][S1].
13. **Detraining/retraining**: meta-analysis (103 studies): stopping reduces submaximal strength (SMD −0.62), maximal force (−0.46), power (−0.20); losses grow with break length and are larger >65 y. Practitioner synthesis: younger adults mostly fine ≤~28 days; regain time ≈ ½ time off (range ⅓–⅔); maintenance possible on ~⅑ (young) to ~⅓ (older) of prior volume. **Moderate (meta-analysis) / Practitioner (synthesis numbers)** [S9][S19].
14. **Sleep**: systematic review (17 studies, moderate/weak quality): a single night of total deprivation has limited effect on strength; consecutive nights of restriction reduce force in multi-joint but not single-joint tasks; mitigated by caffeine/group training/motivation. No hypertrophy-specific review found. **Moderate** [S15].
15. **Pain during exercise**: pain-monitoring model (from patellofemoral/Achilles research): keep pain ≤5/10 during and after activity, settled by next morning; 5/10 is a clinical convention, not a validated resistance-training cutoff; transfer to low back pain is unproven. **Practitioner** [S16].
16. **Obesity/sedentary starts**: ACSM weight-management stand: ~250–300 min/wk moderate activity for greater weight loss / less regain (secondary); start ~30 min/day and build gradually; low-impact modalities; medical screening (e.g. PAR-Q+) before intense exercise. ACSM 2026 explicitly excludes obesity/sarcopenia/frailty from its scope. **Moderate/Practitioner** [S20][S1].

## Numeric guidelines

### A. Experience-level defaults (general resistance training)

| Variable | Beginner | Intermediate | Advanced | Source/Grade |
|---|---|---|---|---|
| Days/wk (ACSM 2009) | 2–3 | 3–4 | 4–5 | [S2] Practitioner |
| Sets/muscle/wk (hypertrophy) | 4–10 (start ~6–8) | 10–16 | 12–20 | [S1][S12] Moderate; start-low is Practitioner |
| Sets/exercise (strength) | 2–3 | 2–4 | 2–5 | [S1][S2] |
| Rep range | 8–12 (some 5–15) | 5–12 (varied) | 1–12, periodized | [S2] |
| RIR target | 2–4 | 1–3 | 0–3 (selectively near failure) | [S1] says ~2–3 RIR; spread is Practitioner |
| Progression | Add load/reps each session or week (2–10% when 1–2 reps over) | Weekly/monthly double progression | Block/wave-loaded; deloads every ~4–8 wks | [S2]; Practitioner |
| Exercise complexity | Machines, goblet/DB, simple barbell | Barbell + variations | Variations, specialization | Practitioner |
| Exercise variety | Few (4–6 per session), repeated | Moderate | Higher (joint-stress rotation) | Practitioner |

### B. Special populations

| Population | Frequency | Sets × reps / intensity | Extra components | Notes |
|---|---|---|---|---|
| Older 50–64, healthy | 2–3 d/wk | 2–3 sets × 6–12; ~2–3 RIR | Add 1–2 power sets, balance | Same core template [S1] |
| Older 65+ | 2–3 d/wk RT; multicomponent ≥3 d/wk | 1–3 sets × 8–12 at moderate load; power 40–70% 1RM, 2–4 sets, fast concentric, controlled eccentric | Balance/coordination ≥3 d/wk [S4][S5] | Avoid failure by default [S1]; slower progression |
| Frail / mobility-limited | Clinician-informed | Light loads, supported/seated | Fall-prevention | Refer (see rules) [S3] |
| Women (healthy, general) | Same as men | Same | None cycle-based | [S6][S7][S8] |
| Pregnant (uncomplicated, cleared) | Most days | ≈150 min/wk moderate aerobic + light-moderate RT; RPE-based | Avoid supine-heavy, contact, scuba, abdominal-trauma risk | [S10]; clinician clearance |
| Postpartum | Resume gradually after clearance | Start low, progress | Pelvic-floor/core symptoms → refer | [S10] |
| Youth (≈7–17, qualified supervision) | 2–3 non-consecutive d/wk | 1–3 sets × 6–15, technique-first, light-moderate loads | Fundamental movement skill | [S11]; numbers (background) |
| Overweight/obese beginner | 2–3 d/wk RT; walking daily | 1–2 sets × 8–15 of 6–8 machine/low-impact moves; RPE 5–6/10 | Aerobic: start ~30 min/day, build gradually | [S20] (secondary); screen first |
| Sedentary beginner | 2 d/wk | 1–2 sets × 10–15, 3–5 RIR first 2–4 wks | Habit building | Practitioner |

### C. Time-constrained designs

| Available time | Structure | Sets/muscle/wk reached | Expected outcome |
|---|---|---|---|
| ~20–30 min, 1 d/wk | Full body, 5–6 compound/machine exercises, 1–2 hard sets each, 5–10 reps | ~1–4 | Meaningful strength gains (≈30% yr 1 in novices, secondary); limited hypertrophy [S12] |
| 2 × 30 min | Full-body A/B, 4–5 exercises, 2 sets | ~4–8 | Good strength; moderate hypertrophy [S1] |
| 3 × 30–45 min | Full body, supersets of non-competing pairs | ~8–14 | Near-full results [S18][S1] |
| Any | Minimum to *maintain* | 1–3 sets of key lifts/wk (≈⅑–⅓ of prior volume) | Maintenance [S19] |

Time-saving levers: compound lifts, antagonist/non-competing supersets, shorter rests on isolation work (keep 2–3 min on heavy compounds if strength is the goal), drop optional isolation, 1–2 hard sets/exercise [S12][S13].

### D. Retraining after a layoff

| Time off | Expected loss | Re-entry plan (Practitioner, built on [S9][S19]) |
|---|---|---|
| <2 weeks | Negligible | Resume normally |
| 2–4 wks | Small (older adults earlier) | Week 1 at ~80–90% of last loads (~20% reduction) then normal |
| 1–3 months | Moderate strength loss | Week 1 ≈ ⅓–½ previous loads, same sets × reps; week 2 loads at 3–5 RIR; ramp back over ≈½ the weeks off |
| 3–12 months | Substantial | Treat first 2 wks as technique/ramp; regain in ≈ ½ time off (range ⅓–⅔) |
| >1 year | Near-novice for planning | Use beginner linear progression; expect faster than first-time progress |
| Older adults | ~2× losses | Longer ramp; bias to lighter loads and RIR 3+ |

### E. Recovery-based volume adjustment (Practitioner unless noted)

| State | Volume | Intensity/RIR |
|---|---|---|
| Good sleep (7–9 h), low stress | Planned volume | Planned |
| 1–2 poor nights | Keep volume; maybe trim last set/accessory | Keep loads, +1 RIR on multi-joint lifts [S15] |
| Chronic poor sleep (<6 h) or high life stress for >1 wk | Cut ~20–40% of sets | +1–2 RIR; avoid failure; prefer machines/stable lifts |
| Large calorie deficit | Use lower end of volume range | Keep load, reduce junk volume |
| Protein | Total intake in typical evidence-based range (see Topic on nutrition) | n/a |

### F. Exercise-substitution matrix (movement pattern × equipment level)

| Pattern | Full gym | Dumbbells / bands / basic home | Bodyweight only | Joint-friendly / limitation-friendly swap |
|---|---|---|---|---|
| Squat (knee-dominant) | Back/front squat, leg press, hack squat | Goblet squat, DB front-foot-elevated split squat, band squat | Tempo squat, box squat, pistol-to-box, sissy-squat progression | Box squat, leg press with limited ROM, TRX-assisted squat (knee/hip pain, balance issues) |
| Hinge | Deadlift, RDL, hip thrust, back extension | DB/KB RDL, single-leg RDL, DB hip thrust, KB swing | Single-leg hip thrust, glute bridge (feet elevated), Nordic/slider ham curl, good-morning | Hip thrust or 45° back extension, trap-bar/elevated deadlift, cable pull-through (low-back irritation) |
| Lunge/single-leg | Walking lunge, Bulgarian split squat, step-up | DB split squat, step-up, reverse lunge | Reverse lunge, step-up, Bulgarian split squat, skater squat | Supported split squat, step-up to low box, reverse lunge (knee-friendly) |
| Horizontal push | Barbell/DB bench, machine chest press, cable fly | DB floor press, band push-up, DB fly | Push-up variations (incline → standard → decline/deficit/archer/one-arm), ring push-up | Incline push-up, neutral-grip DB press, machine press (shoulder pain), floor press (limited ROM) |
| Vertical push | OHP, machine shoulder press | DB/KB press, landmine press, band press | Pike push-up → elevated pike → wall handstand push-up | Landmine press, high-incline press, scapular-plane raises (shoulder impingement-type irritation) |
| Horizontal pull | Barbell/cable/machine row, chest-supported row | DB row, band row, inverted row on table/bar | Inverted/bodyweight row (table, rings, door), towel row | Chest-supported row, neutral-grip row (low back/shoulder) |
| Vertical pull | Pull-up/chin-up, lat pulldown | Band-assisted pull-up, band/DB pullover, lat pulldown with band | Pull-ups/chin-ups (assisted/negatives), scapular pulls; if no bar: towel/door row emphasis | Lat pulldown neutral grip, assisted pull-up, straight-arm pulldown (shoulder/elbow irritation) |
| Carry / trunk bracing | Farmer, suitcase carry, Pallof press | KB/DB carries, band Pallof | Plank variations, dead bug, bird dog, side plank, bear crawl | Dead bug/bird dog, Pallof press (low-back sensitivity) |
| Calf/ankle | Standing/seated calf raise | DB calf raise | Single-leg calf raise (step) | Seated calf raise (Achilles irritation → reduce stretch/ballistic) |
| Biceps / triceps (optional) | Cable curl/pushdown | DB curl, band pushdown, overhead DB extension | Chin-up/biceps iso-hold, close-grip/diamond push-up, bench dip (shoulder caution) | Neutral-grip/cable variants (elbow irritation) |

Overload without heavy load (bodyweight/home), ordered by ease of use: (1) get closer to failure (≈1–3 RIR) with higher reps (15–30+) [S14][S1]; (2) slower eccentrics 3–4 s, pauses; (3) harder leverage (incline → decline, two-leg → single-leg); (4) increase ROM (deficit, elevated feet); (5) add load via backpack/bands/water jugs; (6) shorter rest/density techniques; (7) unilateral variants. Practitioner except where tagged.

## Decision rules

**Triage and safety**
- IF user reports chest pain, unexplained dyspnea, syncope/dizziness on exertion, known cardiovascular/metabolic/renal disease, uncontrolled hypertension, recent surgery, pregnancy complications, or sudden neurological symptoms (numbness, weakness, loss of bladder/bowel control) THEN do not generate a hard program; advise clinical clearance/referral first.
- IF user is sedentary AND age ≥ 45–50, or has known risk factors THEN recommend screening (e.g. PAR-Q+) and start at the low end; hold RT at RPE ≤6 for the first 2–4 weeks [S20].
- IF user asks for diagnosis or treatment of an injury THEN decline medical advice, offer general loading principles only, and refer to a physician/physiotherapist.

**Experience level**
- IF training history <6–12 months OR returning after >1 year THEN beginner template: full-body 2–3 d/wk, 4–6 simple exercises/session, 2–3 sets of 8–12, 2–4 RIR, add load/reps each session/week [S1][S2].
- IF lifter stalls on linear progression for ≥2–3 consecutive attempts at a lift THEN move to intermediate: double progression / weekly progression, upper–lower or PPL, 10–16 sets/muscle/wk [S2].
- IF progress is slower than monthly on main lifts and >2–3 years consistent THEN advanced: periodized blocks/wave loading, planned deload every ~4–8 weeks, selective near-failure work [S1][S2].
- IF unsure of level THEN default to intermediate-lite (≈10 sets/muscle/wk, 2–3 RIR) because ACSM finds the core template works across experience [S1].

**Older adults**
- IF age ≥65 and healthy THEN: 2–3 RT days/wk full-body, 1–3 sets × 8–12 at moderate loads, add 1–2 power sets (fast concentric 40–70% 1RM) on leg press/chair rise/step-up, and balance/coordination work so multicomponent activity totals ≥3 d/wk [S3][S4][S5].
- IF older adult with poor balance or fall history THEN use supported variants (machines, chair, rail), seated alternatives, and refer for fall-risk assessment.
- IF older adult THEN default to 2–4 RIR and avoid sets to failure and breath-holding/Valsalva-heavy maximal efforts unless cleared [S1].
- IF older adult returns after illness/layoff THEN progress slower (losses ~2× faster than younger adults; allow longer ramp) [S9].

**Women / pregnancy**
- IF user is female THEN use the same volume/frequency/load rules as for men; do not reduce load or restrict to "toning" rep ranges [S6][S7].
- IF user asks for menstrual-cycle periodization THEN state evidence does not support phase-based programming; allow subjective autoregulation (reduce volume/intensity on days with severe symptoms) [S8].
- IF user is pregnant AND cleared by clinician THEN continue/begin moderate RT + aerobic (~150 min/wk), RPE-guided ("can talk"), avoid contact/fall-risk/scuba/heavy Valsalva/prolonged supine, stop on warning signs and refer [S10].
- IF postpartum THEN resume only after clearance; start low and rebuild gradually; IF leakage, bulging, pelvic pain or pressure THEN refer to a pelvic-health professional.

**Youth**
- IF age <18 THEN require qualified supervision, technique first, 1–3 sets × 6–15, light–moderate loads, 2–3 non-consecutive days; no max testing or ego lifting; include movement skill/play [S11].

**Time**
- IF only 1 day/wk THEN full-body 5–6 compound/machine exercises, 1–2 hard sets each, 5–10 reps, near effort; expect mostly strength gains [S12][S13].
- IF 2–3 days of 30–45 min THEN full-body, 4–6 exercises, supersets of non-competing pairs, 2 sets each [S1][S12].
- IF goal is hypertrophy AND time is short THEN prioritize total hard weekly sets per muscle (≥4 minimum, ≥10 ideal) over spreading across more days [S1][S18].
- IF time shrinks temporarily THEN maintain loads and cut sets to ≈⅓ rather than dropping training entirely [S19].

**Home/bodyweight**
- IF only bodyweight THEN pick the hardest variation that allows ≥8 reps, then use 15–30 reps at 1–3 RIR, tempo and unilateral work; progress by leverage before reps [S14][S1].
- IF bodyweight exercise exceeds ~30 reps easily THEN advance the variation (incline→flat→decline→archer; two-leg→single-leg).
- IF vertical pulling is impossible (no bar) THEN substitute inverted/towel rows and band pull-downs; flag the missing vertical-pull pattern in the plan.
- IF user has dumbbells only THEN use unilateral lifts, slow eccentrics and rep ranges 8–20.

**Injury / pain**
- IF pain is sharp, worsening, radiating, associated with numbness/weakness, night pain, swelling or following trauma THEN stop the movement and refer.
- IF a movement aggravates a joint THEN swap within the same pattern using the matrix (change ROM, load path, grip, stance or machine) and keep training uninjured regions.
- IF using a pain-monitoring rule THEN conservative convention: pain ≤3/10 (maximum 5/10), not worsening during session, back to baseline by next morning; otherwise regress one level [S16].
- IF the person has diagnosed injury/chronic pain THEN note that the plan is general, and coordinate with their clinician.

**Layoff / retraining**
- IF off <2 weeks THEN resume normally; IF 2–4 weeks THEN −10–20% loads for one week; IF >1 month THEN week 1 ≈ ⅓–½ prior loads, then ramp over about half the weeks off; IF >1 year THEN beginner progression [S9][S19].
- IF user is returning THEN expect strength to rebound fast; cap weekly load jumps at ≈5–10% and keep 3–5 RIR in the first two weeks.

**Recovery**
- IF sleep <6 h/night for several nights or life stress is high THEN cut volume 20–40%, lift to ≥2–3 RIR, favor stable multi-joint lifts you know; consider an earlier deload [S15].
- IF a single bad night THEN train as planned but accept reduced top-set performance; do not chase PRs [S15].
- IF in a calorie deficit THEN stay near the lower-middle of the volume range and preserve intensity.

**Obesity / sedentary**
- IF BMI ≥30 or deconditioned THEN start with walking + machine/low-impact RT, 1–2 sets, RPE 5–6; avoid high-impact jumping initially; progress 5–10% per week after 4–6 weeks as tolerated [S20] (secondary).
- IF joint pain on weight-bearing moves THEN use seated/supported variants and cycling/pool-based aerobic options.

## Common mistakes

- Giving beginners advanced volume/complexity (high-volume splits, Olympic lifts, failure sets) when a simple 2–3 day full-body plan produces progress.
- Giving older adults only light "toning" and no power, balance or heavy-enough strength work.
- Using fixed "women's programs" (light weights, high reps) or cycle-phase periodization with no evidence basis [S6][S8].
- Treating youth as small adults, or banning youth RT on stunting myths, instead of supervised technique-first training [S11].
- Writing 6-day plans for time-poor users; adherence collapses. Time-poor plans should hit weekly sets, not weekly days.
- Believing bodyweight cannot build muscle; or relying on high reps far from failure [S14].
- Resuming a layoff at pre-layoff loads (injury and soreness risk) or being too timid (ignoring fast regain) [S9].
- Ignoring recovery data: high volume stacked on poor sleep and stress [S15].
- "Pushing through" pain or giving diagnostic/treatment claims instead of substituting patterns and referring.
- Copying ACSM 2026 numbers to clinical populations (obese, sarcopenic, frail), which that position stand explicitly excludes [S1].

## Controversies & open questions

- **Experience level effects**: ACSM 2026 finds minimal impact of training status on outcomes; practitioner frameworks still scale volume and complexity by level. Both can be right (response to *adding* sets differs from the starting dose needed) [S1].
- **Menstrual cycle**: low-quality studies, mostly poor verification of phase; absence of evidence is not proof of no effect; individual symptom-based autoregulation remains reasonable [S8].
- **Power training in older adults**: modest, low-certainty benefit over traditional strength training [S5].
- **Failure training in older adults**: ACSM cautions; evidence is thin; individual risk varies [S1].
- **Muscle memory**: myonuclear permanence is supported by animal work and some human data but contested; practical faster retraining is more certain than the mechanism [S17].
- **Minimum effective dose numbers** vary by source/preprint and outcome; single-session/week programs probably underdeliver on hypertrophy [S12][S13].
- **Pain thresholds** in training are conventions from rehab research (knee/tendon), not validated for general lifting or low-back pain [S16].
- **Youth set/rep specifics** and sleep effects on hypertrophy (as opposed to strength) lack retrieved high-quality evidence.
- **Overweight/obese RT prescriptions**: no population-specific resistance guidance retrieved; defaults here are Practitioner.

## Related topics

- Topic 02–03: volume, intensity, frequency, proximity to failure (dose landmarks used here).
- Topic on progression/periodization/deloads (how to progress beginner → advanced).
- Topic on splits and days-per-week mapping (time-constrained structures).
- Topic on exercise selection and movement patterns (matrix above).
- Topic on conditioning/cardio (WHO aerobic volumes; obesity and older adult aerobic dose).
- Topic on nutrition/recovery (protein, calorie deficit effects).
- Topic on warm-up/mobility and quality-control checklist (substitutions given; red-flag screening).

## Research log

Searches run (standard mode): NSCA older adults position statement; menstrual cycle meta-analysis; youth RT consensus; minimum effective dose; muscle memory/myonuclei; low-load vs high-load/bodyweight; sex differences (Roberts 2020); WHO 2020 guidelines; ACOG pregnancy opinion; sleep and RT; power training older adults; ACSM progression models; detraining/retraining; pain-monitoring; ACSM obesity guidance; frequency meta-analyses/minimal dose. Fetches: ACSM 2026 position stand (PMC12965823, first 100k chars read only), Stronger By Science detraining article and sex-differences article, Nuzzo 2024 minimal-dose overview (redirected, not read), PubMed NSCA abstract (blocked by cookies), Lloyd 2014 PDF (404) and ETSU record (no abstract).

Gaps: could not retrieve full text of NSCA older adults statement (dosing), Lloyd 2014 (youth numbers), ACOG 804 (exact text), WHO document (exact ≥2 d/wk wording), ACSM 2009 stand primary text. Youth numbers and several older-adult rep ranges are therefore partly background knowledge and flagged as such. No dedicated evidence on pregnancy/postpartum resistance specifics or overweight RT specifics was found. Sources rejected: blog claims on push-ups without cited studies (BoxRox), mirror-site PDFs of ACSM guidelines (untraceable), listicle sites.

## Sources

[S1] Currier BS, D'Souza AC, Fiatarone Singh MA, et al. ACSM Position Stand: Resistance Training Prescription for Muscle Function, Hypertrophy, and Physical Performance in Healthy Adults: An Overview of Reviews. Med Sci Sports Exerc 58(4):851–872, 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC12965823
[S2] American College of Sports Medicine. Position Stand: Progression Models in Resistance Training for Healthy Adults. Med Sci Sports Exerc, 2009 (secondary copy). https://www.sportgeneeskunde.com/wp-content/uploads/ACSM-Position-Stand-Progression-Models-in-Resistance-Training-for-Healthy-Adults.pdf
[S3] Fragala MS, Cadore EL, Dorgo S, et al. Resistance Training for Older Adults: Position Statement From the National Strength and Conditioning Association. J Strength Cond Res 33(8):2019–2052, 2019. https://pubmed.ncbi.nlm.nih.gov/31343601/
[S4] Bull FC, et al. World Health Organization 2020 guidelines on physical activity and sedentary behaviour. Br J Sports Med, 2020 (via summary). https://www.croakey.org/who-2020-guidelines-on-physical-activity-and-sedentary-behaviour-what-is-new-and-why-it-matters/
[S5] Balachandran AT, et al. Comparison of Power Training vs Traditional Strength Training on Physical Function in Older Adults: A Systematic Review and Meta-analysis. JAMA Netw Open, 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9096601
[S6] Roberts BM, Nuckols G, Krieger JW. Sex Differences in Resistance Training: A Systematic Review and Meta-Analysis. J Strength Cond Res, 2020. https://pubmed.ncbi.nlm.nih.gov/32218059/
[S7] Refalo MC, et al. Sex differences in absolute and relative changes in muscle size following resistance training in healthy adults: a systematic review with Bayesian meta-analysis. 2025. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11869894/ ; and Stronger By Science, Sex Differences in Muscle & Strength. https://www.strongerbyscience.com/sex-differences-muscle-strength/ (Practitioner summary)
[S8] Colenso-Semple LM, et al. Current evidence shows no influence of women's menstrual cycle phase on acute strength performance or adaptations to resistance exercise training. Front Sports Act Living, 2023. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10076834/
[S9] Bosquet L, et al. Effect of training cessation on muscular performance: A meta-analysis. Scand J Med Sci Sports, 2013. https://ekoizpen-zientifikoa.ehu.eus/documentos/5f1cda5129995265e44d37a4?lang=en
[S10] ACOG Committee Opinion No. 804: Physical Activity and Exercise During Pregnancy and the Postpartum Period. Obstet Gynecol 135(4):e178–188, 2020. https://opqic.org/acog-committee-opinion-no-804-physical-activity-and-exercise-during-pregnancy-and-the-postpartum-period/
[S11] Lloyd RS, Faigenbaum AD, Stone MH, et al. Position statement on youth resistance training: the 2014 International Consensus. Br J Sports Med 48(7):498–505, 2014. https://dc.etsu.edu/etsu-works/4624
[S12] Nuzzo JL, et al. Resistance Exercise Minimal Dose Strategies for Increasing Muscle Strength in the General Population: an Overview. Sports Med, 2024. https://pubmed.ncbi.nlm.nih.gov/38509414/
[S13] Iversen VM, Norum M, Schoenfeld BJ, Fimland MS. No Time to Lift? Designing Time-Efficient Training Programs for Strength and Hypertrophy: A Narrative Review. Sports Med 51(10), 2021. https://pubmed.ncbi.nlm.nih.gov/34822137/
[S14] Grgic J, et al. The Effects of Low-Load vs. High-Load Resistance Training on Muscle Fiber Hypertrophy: A Meta-Analysis. 2020. https://pubmed.ncbi.nlm.nih.gov/33312275/
[S15] Knowles OE, et al. Inadequate sleep and muscle strength: Implications for resistance training. J Sci Med Sport, 2018. https://pubmed.ncbi.nlm.nih.gov/29422383/
[S16] Thomeé R. pain-monitoring model; Achilles tendinopathy application (Silbernagel et al.) and low back pain protocol, Jorgensen et al., BMJ Open 2018. https://bmjopen.bmj.com/content/8/1/e019742 ; https://physicaltherapyfirst.com/blog/continued-sports-activity-using-a-pain-monitoring-model-during-rehabilitation-in-patients-with-achilles-tendinopathy/
[S17] Rahmati M, McCarthy JJ, Malakoutinia F. Myonuclear permanence in skeletal muscle memory: a systematic review and meta-analysis of human and animal studies. J Cachexia Sarcopenia Muscle, 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9530508
[S18] Schoenfeld BJ, Ogborn D, Krieger JW. Effects of Resistance Training Frequency on Measures of Muscle Hypertrophy: A Systematic Review and Meta-Analysis. Sports Med, 2016; and Schoenfeld, Grgic, Krieger, J Sports Sci, 2019 (via search summaries). https://ro.ecu.edu.au/ecuworkspost2013/5665
[S19] Nuckols G. Detraining (Stronger By Science, Practitioner synthesis), plus Grgic et al., Use It or Lose It? Meta-analysis of RT cessation on muscle size in older adults, 2022. https://www.strongerbyscience.com/detraining/ ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9657634/
[S20] ACSM Position Stand on Appropriate Physical Activity Intervention Strategies for Weight Loss and Prevention of Weight Regain for Adults, 2009 (via secondary slide summaries; low reliability, verify). https://obesityaction.org/?p=1966
