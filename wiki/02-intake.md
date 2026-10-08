# Intake: What to Ask Before Writing a Plan

> Purpose: decide what to collect from the user, what to assume when a field is missing, when to refuse to prescribe and refer, and how each answer changes the plan.
> Use when: before building any plan, and again at each review point (every 4–8 wk).
> Depends on: [principles](01-principles.md); outputs feed [goals](04-goals.md), [splits](06-splits.md), [weekly planning](07-weekly-planning.md), [populations](11-populations.md)

## Key rules (TL;DR)

1. **Order of operations:** (1) safety screen → (2) constraints (time, equipment, injuries) → (3) experience level → (4) population modifiers → (5) recovery-based volume adjustment. [1]
2. **Hard-required fields** (do not build without them, or state the assumption loudly): primary goal, days/week, minutes/session, equipment, injuries/pain, health-screen answer. Everything else has a default.
3. **Ask at most ~8 questions at once.** Use the copy-paste list below; fill gaps with defaults and label each default as an assumption in the plan header.
4. **Any red flag = no hard program.** Advise clinical clearance/referral first. No diagnosis, no treatment advice. [2][3]
5. **Classify experience by progress speed**, not years: beginner = progress session to session; intermediate = week to week; advanced = month to month / block to block. If unsure: intermediate-lite (≈10 sets/muscle/wk, 2–3 RIR), but a person with <6–12 months training or returning after >1 year off is a beginner. (Practitioner) [3]
6. **Time and days beat theory.** The feasible schedule fixes the split. Time-poor plans hit weekly sets, not weekly days.
7. **Re-ask at each review point**: adherence, pain, sleep, schedule changes.
8. **Echo back** a one-paragraph summary of understood inputs and assumptions before or with the plan.

## Intake schema (structured)

Fill this object before planning. `?` = unknown, apply default.

```yaml
safety:
  par_q_flags: []            # chest pain, dizziness/syncope on exertion, known CV/metabolic/renal disease,
                             # uncontrolled hypertension, recent surgery, pregnancy complications, meds. default: ask; never assume "none" silently
  neuro_red_flags: false     # numbness, weakness, loss of bladder/bowel control, sudden neuro symptoms
  pregnancy_postpartum: none # none | pregnant | postpartum
goal:
  primary: general_health    # strength | hypertrophy | fat_loss | general_health | endurance | power | mobility | sport | hybrid
  secondary: []              # max 1-2 per block
  priority_muscles: []       # default none
  event_or_deadline: null    # date + type; default open-ended
schedule:
  days_per_week: 3           # realistic, not aspirational
  minutes_per_session: 45-60
  preferred_days: null
equipment:
  setting: full_gym          # full_gym | home_basic (DB/bands/bench) | bodyweight | mixed
  list: []
person:
  age: adult                 # exact if <18, >=50, >=65
  sex: unspecified
  experience: beginner       # beginner | intermediate | advanced (by progress speed)
  training_history: ""        # lifts known, current vs past, layoff length
  layoff_weeks: 0
limits:
  injuries: []               # site, onset, current symptoms, movements that aggravate
  pain_now: null             # 0-10 and what provokes it
  mobility_limits: []
lifestyle:
  current_activity: sedentary  # steps/day, cardio, sport
  sleep_hours: 7-9
  stress: average
  calorie_deficit: false
preferences:
  likes: []
  dislikes: []
  cardio_type: null
  solo_or_group: null
  tracking: simple_log
history:
  adherence: moderate        # past programs, what made them stop
```

## Field table: required vs optional, defaults, effect on the plan

| # | Field | Req? | Default if missing | How the answer changes the plan |
|---|---|---|---|---|
| 1 | Health screen (PAR-Q+ style) | **Required** | Ask; if user declines to answer and is sedentary/≥45–50, start at RPE ≤6 for 2–4 wk and note limits | Any "yes" → refer first (see red flags). Inactive + asymptomatic + no known disease → light–moderate start. [2][3] |
| 2 | Primary goal | **Required** | General health | Sets rep ranges, load, rest, split, conditioning. See [goals](04-goals.md). |
| 3 | Secondary goal / priority muscles | Optional | None | Priority muscle → 16 sets/wk (≤~22 short-term). Max 1–2 secondary. Primary gets ~60–70% of hard sets (Practitioner heuristic). |
| 4 | Days/week available | **Required** | 3 | 2 → full body A/B; 3 → full body; 4 → upper/lower; 5–6 only if the user asks and is not a beginner. Split choice is owned by [splits](06-splits.md). |
| 5 | Minutes/session | **Required** | 45–60 | ≤30 min → MED design (3–4 compounds, 1–3 sets each, supersets). 45–75 min → 4–8 exercises. Budget warm-up 5–10 min. |
| 6 | Training experience | Optional (but classify) | Beginner (conservative); intermediate-lite if user insists on years of training | Beginner: 8 sets/muscle/wk, 3 RIR, linear progression, 90–120 s rests, few exercises. Intermediate: 12, 2 RIR, double progression. Advanced: 16 for priority muscles, deloads, variation. |
| 7 | Layoff length | Optional | 0 | <2 wk resume; 2–4 wk −10–20% loads one week; >1 month week 1 ≈ ⅓–½ prior loads, ramp over ~half the weeks off (Practitioner); >1 yr treat as beginner. [4] |
| 8 | Current activity | Optional | Sedentary | Aerobic floor gap: build to 150 min/wk moderate; sedentary → low-impact start. |
| 9 | Equipment | **Required** | Full gym | Selects exercises via [exercise library](12-exercise-library.md). Bodyweight/home: overload via near-failure higher reps (15–30), tempo, unilateral, leverage. Flag missing vertical pull. [5] |
| 10 | Injuries / pain | **Required** | None (but ask) | Swap within the same movement pattern (change ROM, load path, grip, stance, machine). Keep training uninjured regions. Pain rule: ≤3/10 during, settled by next day (Practitioner). |
| 11 | Age, sex | Optional | Adult | ≥65: multicomponent ≥3 d/wk, power (fast concentric, 40–70% 1RM), 3 RIR, no routine failure. <18: qualified supervision, technique first. Women: same rules; no cycle programming. [6][7] |
| 12 | Sleep / stress / calorie deficit | Optional | 7–9 h, average, no deficit | Sleep <6 h for several nights or high stress >1 wk → volume −20–40%, +1–2 RIR. Deficit → lower-middle of volume range, keep load. (Practitioner) [8] |
| 13 | Preferences (likes/dislikes, cardio type, group/solo) | Optional | None | Pattern-equivalent swaps; cardio mode choice; accountability design. |
| 14 | Adherence history | Optional | Moderate | Poor → fewer, shorter sessions, simple structure, fallback "minimum session". |
| 15 | Timeframe / event | Optional | Open-ended | Event → periodize backward from date; else 4–8 wk mesocycles. |
| 16 | Tracking preference | Optional | Simple log | Progression rules need logged load × reps × RIR. |

## Copy-paste intake question list

Use as written; skip any the user already answered.

```
Before I build this, a few quick questions (answer what you can; I'll assume sensible defaults for the rest and tell you what I assumed):

SAFETY (please answer)
1. Do you have, or have you ever been told you have, a heart condition, high blood pressure, diabetes, kidney disease, or another chronic condition? Do you take medication for it?
2. Do you ever get chest pain, unexplained shortness of breath, or dizziness/fainting when you exert yourself?
3. Any recent surgery, current pregnancy, or you gave birth in the last 12 months?
4. Any current injury or pain? Where, how bad (0-10), and which movements set it off?

GOAL
5. What is your main goal: get stronger, build muscle, lose fat, general health/fitness, endurance, power/athletic, or a mix? Any secondary goal, specific muscle you want to prioritise, or event/date?

SCHEDULE
6. How many days per week can you realistically train, and for how many minutes per session?

EQUIPMENT
7. Where will you train and what do you have: full gym, dumbbells/bands/bench at home, or bodyweight only?

EXPERIENCE
8. How long have you trained consistently? Which lifts do you know? Are you currently training, or returning from a break (how long)?
   Quick test: can you add weight or a rep to your main lifts every session, every week, or only every month or more?

LIFE
9. Age, sex, and what activity you do now (steps per day, cardio, sports)?
10. Typical sleep (hours) and stress level? Are you currently dieting in a calorie deficit?

PREFERENCES
11. Exercises or cardio you love or hate? Prefer training alone or in a group?
12. Past programs: what did you stick with, and what made you stop?
```

## Red flags: refer or get clearance before prescribing

These are screening rules, not medical advice. Output template: "I can't safely prescribe a hard program until a physician/qualified professional clears this. Meanwhile light walking is generally fine unless they told you otherwise." (Last sentence only if no symptom on exertion.)

| Signal | Action |
|---|---|
| Chest pain, unexplained dyspnea, syncope/dizziness on exertion | **Stop**; clearance first. |
| Known cardiovascular, metabolic (e.g. diabetes) or renal disease; uncontrolled hypertension | Clearance first; do not generate a hard program. [2][3] |
| Any PAR-Q+ "yes" not yet reviewed by a professional | Clearance first. [2] |
| Recent surgery; pregnancy complications | Clearance first. |
| Numbness, weakness, loss of bladder/bowel control, sudden neurological symptoms | Urgent medical referral. |
| Sharp, worsening, radiating pain; night pain; swelling; pain after trauma | Stop the movement; refer. |
| Diagnosed injury or chronic pain | Plan is general; coordinate with clinician. |
| Request to diagnose or treat an injury | Decline medical advice; offer general loading principles only; refer. |
| Pelvic leakage, bulging, pelvic pain/pressure (postpartum) | Refer to pelvic-health professional. |
| Pregnant | Proceed only with clinician clearance; RPE-guided ("can talk"), ≈150 min/wk moderate aerobic + light–moderate RT; avoid contact/fall risk/scuba/heavy Valsalva/prolonged supine. [9] |
| Frail, mobility-limited, fall history | Clinician-informed plan; supported/seated variants; refer for fall-risk assessment. [10] |
| Age <18 | Qualified supervision required; no max testing. [11] |

**Conditional caution (not a hard stop):** sedentary and age ≥45–50, or known risk factors, no symptoms → recommend screening, start at the low end, resistance work at RPE ≤6 for the first 2–4 weeks. Obese/deconditioned (BMI ≥30): walking + machine/low-impact RT, 1–2 sets, RPE 5–6, avoid jumping at first. (Practitioner; ACSM 2026 does not cover these groups.) [1][12]

## How answers map to the plan (quick lookup)

| If intake says | Do this |
|---|---|
| Beginner, 3 days, 45–60 min | Full body ×3; 4–6 exercises; 2–3 sets of 8–12; 3 RIR; 8 sets/muscle/wk; linear progression. |
| Intermediate, 4 days | Upper/lower ×2; 12 sets/muscle/wk; 2 RIR; double progression; 5+1 mesocycle. |
| Advanced, priority muscle | 16 sets/wk to that muscle (≤~22 short-term), maintenance (4–6) elsewhere; deload every 4–8 wk. |
| 1–2 days or ≤30 min | MED: whole body, 1–3 compounds, 1–3 sets each, ≥2 d/wk (1 d/wk gives mostly strength, limited hypertrophy). [13] |
| Home, bodyweight only | Hardest variation allowing ≥8 reps, then 15–30 reps at 1–3 RIR; tempo, unilateral; flag missing vertical pull. [5] |
| Fat loss goal | RT 3–4×/wk as base, steps + moderate cardio, keep load in a deficit; diet creates the deficit. See [goals](04-goals.md). |
| Female | Same rules as men; do not shift to "toning" rep ranges. [6] |
| Age ≥65 | 2–3 RT days, 1–3 sets × 8–12, power sets, balance, 3 RIR; multicomponent ≥3 d/wk. [10] |
| Sleep <6 h / high stress | Volume −20–40%, +1–2 RIR. |
| Returning after layoff | Reduced loads and ramp (row 7 above). |
| Drop-out history | Fewer, shorter sessions; clear success criteria; fallback session. |
| Pain with a movement | Same-pattern swap from [exercise library](12-exercise-library.md). |

## Decision rules

- IF a hard-required field is missing and cannot be asked THEN apply the default, mark it `ASSUMED` in the plan header, and state the one assumption most likely to be wrong.
- IF goal is blank THEN general health: 3 full-body days + walking + 10 min mobility, and reach the floor (150 min aerobic equivalent + ≥2 strength days). [14]
- IF stated days exceed what the recovery or adherence history supports THEN plan the lower number and offer an optional extra day.
- IF user states several goals THEN force one primary; the rest are secondary at maintenance-to-moderate dose. At ≤3 days use full-body sessions covering both.
- IF experience claim conflicts with described progress (e.g. "5 years" but never logged loads or stalled) THEN classify by progress speed and start one level lower.
- IF experience level is unclear THEN intermediate-lite (≈10 sets/muscle/wk, 2–3 RIR). Beginner defaults if <6–12 months training or >1 year off.
- IF the user declines the health screen THEN treat as sedentary with unknown risk: RPE ≤6 first 2–4 wk, no max efforts, note that screening was declined.
- IF user asks for menstrual-cycle periodization THEN state the evidence does not support it; allow symptom-based autoregulation (reduce volume/intensity on severe-symptom days). [7]
- IF pain ≤3/10 during, settled by next day THEN continue; IF pain worsens or persists past next morning THEN regress one level; IF red-flag pattern THEN refer.
- IF review point reached THEN re-ask items 4, 10, 12 and adherence.

## Common mistakes

- Skipping the safety screen because the user "just wants a plan."
- Asking 20 questions in a row; low-value fields should default.
- Trusting self-reported years of training over progress speed.
- Prescribing the user's aspirational days/week instead of their realistic one.
- Silent assumptions: always list defaults in the plan header.
- Giving medical advice: diagnosing pain, naming a condition, prescribing rehab.
- Applying healthy-adult ACSM numbers to obese, sarcopenic or frail users without caution. [1]
- Ignoring sleep/stress/deficit when volume is already near the top of the range.

## Evidence notes

- The safety triggers are screening conventions (PAR-Q+ 2023 and ACSM pre-participation logic via secondary guides); verify against current ACSM guidance. Grade: Moderate (secondary sources). [2][3]
- The "ACSM clearance algorithm" is from secondary study guides only; primary text not retrieved. The red-flag list here deliberately errs conservative.
- Experience classification by progress speed is a Practitioner heuristic. ACSM 2026's "experience had minimal impact" came from the authors' earlier network meta-analysis of mostly novice data; do not overstate it. [1]
- Pain-monitoring thresholds come from tendon/patellofemoral rehab research (≤5/10 convention); the ≤3/10 conservative form is Practitioner and not validated for general lifting or low-back pain. [15]
- Sleep: consecutive nights of restriction reduce force in multi-joint tasks (moderate/weak-quality studies); no hypertrophy-specific review. Volume cuts of 20–40% are Practitioner. [8]
- Youth specifics (1–3 sets × 6–15, 2–3 non-consecutive d/wk), pregnancy/postpartum and obesity RT dosing rest on consensus statements and secondary summaries; full texts were not retrieved. [9][11][12]
- Menstrual cycle: umbrella review finds no reliable basis for phase-based programming; absence of evidence is weak but no reliable alternative exists. [7]

## Sources

[1] Currier BS, D'Souza AC, Fiatarone Singh MA, et al. (Phillips SM senior). ACSM Position Stand: Resistance Training Prescription for Muscle Function, Hypertrophy, and Physical Performance in Healthy Adults: An Overview of Reviews. Med Sci Sports Exerc 58(4):851–872, 2026. https://pmc.ncbi.nlm.nih.gov/articles/PMC12965823
[2] Warburton DER et al. The PAR-Q+ and ePARmed-X+ (2023 consensus version). Health & Fitness Journal of Canada. https://hfjc.library.ubc.ca/index.php/HFJC/article/view/839
[3] ACSM pre-participation screening algorithm via secondary guide (verify against current ACSM guidance): https://open-exam-prep.com/study-guides/ace-cpt/health-screening/preparticipation-health-screening
[4] Nuckols G. A Guide to Detraining. Stronger By Science, 2022 (Practitioner); Bosquet L et al. Effect of training cessation on muscular performance: a meta-analysis. Scand J Med Sci Sports 23(3), 2013. https://www.strongerbyscience.com/detraining/ ; https://doi.org/10.1111/sms.12047
[5] Grgic J et al. The Effects of Low-Load vs. High-Load Resistance Training on Muscle Fiber Hypertrophy: A Meta-Analysis. 2020. https://pubmed.ncbi.nlm.nih.gov/33312275/
[6] Roberts BM, Nuckols G, Krieger JW. Sex Differences in Resistance Training: A Systematic Review and Meta-Analysis. J Strength Cond Res 34(5):1448–1460, 2020. https://doi.org/10.1519/JSC.0000000000003521
[7] Colenso-Semple LM et al. Current evidence shows no influence of women's menstrual cycle phase on acute strength performance or adaptations to resistance exercise training. Front Sports Act Living, 2023. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10076834/
[8] Knowles OE et al. Inadequate sleep and muscle strength: Implications for resistance training. J Sci Med Sport, 2018. https://pubmed.ncbi.nlm.nih.gov/29422383/
[9] ACOG Committee Opinion No. 804: Physical Activity and Exercise During Pregnancy and the Postpartum Period. Obstet Gynecol 135(4):e178–188, 2020. https://opqic.org/acog-committee-opinion-no-804-physical-activity-and-exercise-during-pregnancy-and-the-postpartum-period/
[10] Fragala MS et al. Resistance Training for Older Adults: Position Statement From the NSCA. J Strength Cond Res 33(8):2019–2052, 2019. https://pubmed.ncbi.nlm.nih.gov/31343601/ ; Bull FC et al. WHO 2020 guidelines on physical activity and sedentary behaviour. Br J Sports Med 54:1451–1462, 2020. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7719906/ ; Balachandran AT et al. Power vs traditional strength training in older adults. JAMA Netw Open, 2022. https://pmc.ncbi.nlm.nih.gov/articles/PMC9096601
[11] Lloyd RS, Faigenbaum AD, Stone MH, et al. Position statement on youth resistance training: the 2014 International Consensus. Br J Sports Med 48(7):498–505, 2014. https://dc.etsu.edu/etsu-works/4624
[12] ACSM Position Stand on Appropriate Physical Activity Intervention Strategies for Weight Loss and Prevention of Weight Regain for Adults, 2009 (secondary slide summaries; low reliability). https://obesityaction.org/?p=1966
[13] Nuzzo JL et al. Resistance Exercise Minimal Dose Strategies for Increasing Muscle Strength in the General Population: an Overview. Sports Med 54(5):1139–1162, 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11127831 ; Iversen VM et al. No Time to Lift? Sports Med 51(10), 2021. https://pubmed.ncbi.nlm.nih.gov/34822137/
[14] Bull FC et al. WHO 2020 guidelines (above); US Dept of HHS. Physical Activity Guidelines for Americans, 2nd ed., 2018. https://health.gov/sites/default/files/2019-09/Physical_Activity_Guidelines_2nd_edition.pdf
[15] Pain-monitoring model: Jorgensen et al., BMJ Open 2018. https://bmjopen.bmj.com/content/8/1/e019742 ; https://physicaltherapyfirst.com/blog/continued-sports-activity-using-a-pain-monitoring-model-during-rehabilitation-in-patients-with-achilles-tendinopathy/
