# Reference Programs Catalog

> Research agent output · Topic 11 · 2026-10-08

## Executive summary

- Proven programs are **worked examples**, not gospel. Nearly all successful ones share the same skeleton: few big compound lifts, 2–3 exposures/week per main lift, a clear numeric progression rule, and a pre-defined failure response (reset/deload). [S1][S5][S7][S9]
- **Beginner strength** = full-body, 3 days/week, linear progression (add weight each session). Examples: Starting Strength, StrongLifts 5x5, GZCLP, Greyskull LP, 5/3/1 for Beginners. All use ~5 lb upper / 10 lb lower jumps and a ~10% reset after repeated failure. [S1][S2][S3][S4]
- **Intermediate strength** = progression slows to weekly/cycle-based: Texas Method (weekly), Madcow (weekly), 5/3/1 (per 3-week cycle, training max +5/+10 lb), nSuns (AMRAP-driven TM changes). [S5][S6][S7][S8]
- **Hypertrophy programs** (PHUL, PHAT, Reddit PPL, RP, Nippard-style) use higher reps (6–15+), ≥2×/week/muscle, double progression, and volume ramps across a mesocycle ending in a deload. [S9][S10][S11][S12]
- Evidence base for these patterns: volume dose-response (more weekly sets → more growth, up to ≥10 sets/muscle/week in available data), frequency ≥2×/wk is a sensible default but its effect largely vanishes when volume is equated. [S13][S14][S15]
- **Non-barbell archetypes**: Couch to 5K (3 runs/wk, 9 wk, run/walk intervals → 30 min continuous), Higdon marathon Novice 1 (18 wk, 4 runs/wk, long run 6→20 mi, cutback ~every 3rd week), r/bodyweightfitness RR (3×/wk full-body, 3×5–8 → progress at 3×8), Convict Conditioning (6 movements × 10 steps). [S16][S17][S18][S19]
- **Hybrid** has no single canonical template; published examples (Rogue, Strengthlog) share: 2–4 lifts + 2–4 runs/wk, mostly easy/Zone 2 with 1–2 hard sessions, one long session. Treat as `Practitioner`. [S20][S21]
- Source quality caveat: many program details here come from reputable wikis/aggregators (r/Fitness wiki, Liftosaur, StrengthLog, Muscle & Strength) rather than original authors (some original pages blocked/unreachable). Where versions differ it is flagged. Verify exact numbers before presenting any program as "official".

## Core concepts

**What a "program" is** — a (a) session template (lifts × sets × reps × load rule), (b) weekly schedule, (c) progression rule, (d) failure/reset rule. An LLM generating plans should always output all four.

**Progression model families (generic → specific)**
1. *Session-to-session linear progression (LP)*: add fixed load each workout while all reps are completed. Only works for true beginners (fast adaptation). Starting Strength, StrongLifts, GZCLP T1/T2, Greyskull, Reddit PPL.
2. *Weekly linear (intermediate)*: load rises once per week; week has heavy/light/medium days. Texas Method, Madcow.
3. *Cycle-based training-max (TM) waves*: percentages of a TM (≈90% of true/estimated 1RM) change within a 3-week wave; TM bumps each cycle. 5/3/1 family.
4. *AMRAP-driven autoregulated*: rep performance on a top set decides next jump. nSuns, Greyskull, GZCL.
5. *Double progression*: add reps inside a range, then add load when top of range hit on all sets. PHUL/PHAT/PPL accessories, bodyweight RR.
6. *Block/phase periodization*: phases of different emphasis then peak/test. Candito, Sheiko, RP mesocycles.
7. *Distance/time progression (endurance)*: Couch to 5K, Higdon.

**Intensity vocabulary used in these programs**: AMRAP ("5+" = at least 5, as many as possible, usually leaving some reps in reserve); training max (TM); FSL (first set last: 5×5 at the week's first-set %); T1/T2/T3 tiers (GZCL); RPE/RIR.

## Key findings

1. **Beginner full-body, 3×/week, LP is the dominant proven beginner template.** All four of Starting Strength, StrongLifts, GZCLP, Greyskull alternate A/B (or A1/B1/A2/B2) full-body days with squat every session or nearly. *Evidence:* `Practitioner` (consistent across sources [S1][S2][S3][S4]); consistent with ACSM 2009 novice frequency 2–3 d/wk [S15] (`Moderate`; note newer ACSM update exists, see Controversies).
2. **Failure response is standardized**: after ~3 consecutive failures at a weight → drop ~10% (StrongLifts, Starting Strength reset 5–10%/up to 15%, Reddit PPL, Greyskull variant) or move to a lower-rep "stage" (GZCLP). `Practitioner` [S1][S2][S3][S22].
3. **Deadlift gets less volume than squat/bench** in beginner LPs (1×5 in SS/StrongLifts/Greyskull) because of higher fatigue cost. `Practitioner` [S1][S2][S22].
4. **Intermediate = slower progression clock.** Texas Method (week), Madcow (week), 5/3/1 (3-week cycle). Common pattern: one high-volume day, one light/recovery day, one high-intensity day. `Practitioner` [S6][S7][S8].
5. **5/3/1 family uses a conservative TM (≈90% of est. 1RM)** and increments +5 lb upper / +10 lb lower per cycle regardless of AMRAP performance; stall rule = lower TM by 3 increments (15/30 lb). Accessories prescribed as rep totals (50–100 reps per category) rather than fixed sets. `Practitioner` [S8].
6. **Split-based hypertrophy programs (PHUL, PHAT, PPL) hit each muscle 2×/week** and mix heavy (3–5 reps) with moderate/high (8–15+) work. `Practitioner`, supported by `Moderate` evidence that ≥2×/wk is sensible and that volume, not frequency per se, drives the difference [S9][S10][S11][S14][S23].
7. **Volume dose-response**: meta-regression of 15 studies: each added weekly set ≈ +0.37% muscle gain; higher vs lower volume groups ≈ +3.9% difference; grouping <5, 5–9, ≥10 sets/muscle/wk trended (p=0.074) toward more growth; data thin above ~10 and mostly untrained subjects. `Moderate` [S13].
8. **Frequency**: hypertrophy meta-analysis found higher frequency had larger ES (0.49 vs 0.30) but could not separate from volume; strength meta-analysis found no significant frequency effect in volume-equated studies (p=0.421). `Moderate` [S14][S23]. Implication: choose split by schedule and per-session volume tolerance; ≥2×/wk/muscle is a default, not a law.
9. **RP-style hypertrophy** = mesocycle of ~4–6 weeks starting near MEV (~6–8 direct sets/muscle/wk is a rough figure), +sets/+load weekly, RIR falling from ~3 toward 0–1, then deload week (~50% volume). Sources conflict on exact increments/deload (4:1–6:1 week ratio). `Practitioner` (secondary sources; official RP pages not fetched) [S12].
10. **Nippard-style programs** use ~3 sets/exercise at RPE 7–9 (≈1–3 RIR) with isolation work closer to failure; 8-week progressive blocks; full-body 3d and upper/lower 4d variants. Details from app listings only, not author's PDF. `Practitioner` [S24].
11. **Powerlifting-specific programs (Candito, Sheiko) are peaking tools**: Candito = 6-week phased (conditioning/hypertrophy → strength → test → optional deload); Sheiko = very high volume at ~70% average intensity, numbered blocks (#29 prep, #30 accumulation, #31 transmutation, #32 realization). Not for beginners. `Practitioner` [S25][S26].
12. **Endurance beginner plans progress by time-on-feet with walk breaks**; Couch to 5K goes from 1-min runs to 30 continuous minutes in 9 weeks, 3 sessions/wk, repeatable weeks. Higdon Novice 1: 18 wk, 4 runs + 1 cross-train + 2 rest, long run 6 → 20 mi at week 15, cutbacks ~every 3rd week, 3-week taper. Official-source verified (NHS, Higdon site). [S16][S17] Evidence for specific design: `Practitioner` (institutionally endorsed, but not RCT-graded here).
13. **Bodyweight**: RR = skill block + 6 exercises in pairs + core triplet, 3×/wk, 3×5–8 work at hardest manageable progression, advance on 3×8 (reset to 5 reps next level). Convict Conditioning = 6 movements × 10 steps with rep/set gates (e.g. pushup step 1 → 3×50 wall pushups before incline). `Practitioner` [S18][S19].
14. **Hybrid templates are heterogeneous**; published sample weeks pair lifts with Zone 2, one interval day and one tempo run, and warn that 4 h/wk lifting plus runs can be too much. `Practitioner`/anecdote [S20][S21].

## Numeric guidelines

### Catalog table (one row per program)

| Program | Goal | Level | Days/wk | Split | Core structure | Progression | Reset/deload |
|---|---|---|---|---|---|---|---|
| Starting Strength (Rippetoe) | Strength | Novice | 3 (A/B alternating) | Full body | Squat 3×5 every day; bench/press 3×5; deadlift 1×5 (power clean / rows added to B later) | +~5 lb squat, +2.5–5 bench/press, +5–10 deadlift per session [S1] | Reset 5–10% (sheet: 5–15%) after 3 failed sessions at same weight [S1][S22]. Pairing of press/bench on A vs B differs across sources. |
| StrongLifts 5x5 (Mehdi) | Strength | Novice | 3 | Full body A/B | A: squat, bench, barbell row; B: squat, OHP, deadlift. 5×5 each, deadlift 1×5 [S2] | +5 lb (2.5 kg) per session [S2] | 2 fails: repeat; 3rd consecutive fail: −10% [S2]. (Healthline's "every 5th week 50%" is a generic 5x5 variant, not official.) Official site lists Ultra (4d U/L), Madcow, Intermediate as next steps [S27] |
| GZCLP (Cody LeFever) | Strength + some size | Novice | 3–4 rotation (A1/B1/A2/B2) | Full body | T1: 5×3+ main lift; T2: 3×10 secondary lift; T3: 3×15+ accessory (lat pulldown, rows) [S3][S28] | T1/T2 +5 lb bench/OHP, +10 lb squat/DL per session; T3 +5 lb when 25 reps on AMRAP set [S3] | Fail → next stage. T1: 5×3→6×2→10×1; T2: 3×10→3×8→3×6. T1 after final stage: test new 5RM, restart at 85%. T2: last stage-1 weight +15–20 lb [S3]. Wiki vs Liftosaur differ slightly on T2 stages |
| Greyskull LP (John Sheaffer) | Strength + size | Novice | 3 | Full body A/B | 2×5 + final set 5+ (AMRAP) on main lifts; deadlift 1×5+ [S4] | Original increments not confirmed in sources; Phrak variant: +2.5 lb upper/+5 lb lower, double jump if ≥10 reps on AMRAP [S4] | Phrak variant: miss 5 on final set → −10%. Original lacked back work; Phrak adds chins + rows [S4] |
| 5/3/1 for Beginners (Wendler) | Strength | Novice–early inter. | 3 | Full body | Wave %TM: W1 65/75/85×5,5,5+; W2 70/80/90×3,3,3+; W3 75/85/95×5,3,1+; FSL 5×5 at first-set %; assistance 50–100 reps push/pull/single-leg-core [S8] | +5 lb upper, +10 lb lower TM per 3-week cycle [S8] | Stall: cut TM 15 lb upper/30 lb lower; TM test every ~10 weeks [S8] |
| 5/3/1 BBB (Boring But Big) | Size + strength | Intermediate | 4 (one lift/day) | Per lift | 5/3/1 main sets + 5×10 same or opposite lift at ~50–60% TM (third-party; some run 5×10 at 50→60%) | TM +5/+10 lb per cycle | Deload week per 5/3/1; Forever uses leaders/anchors [S29]. Exact BBB % from secondary sources only |
| Texas Method (Rippetoe) | Strength | Intermediate | 3 | Full body | Mon volume 5×5 @ ~90% of 5RM (many use 80–90% of Fri; ~85% best per forum); Wed light: squat 2×5 @ ~80% of Mon; Fri intensity: new 5RM/3RM PR [S6] | Weekly PR on Friday; +~5 lb | Stall fixes: cut Mon sets 5×5→3×5, drop Mon weight 5–10%, change Fri rep scheme [S6] |
| Madcow 5x5 | Strength/size | Intermediate | 3 | Full body | Mon ramp 5 sets to top 5×5 (12.5% steps); Wed light (cap at 70–80% Mon); Fri ramp to a 3 (~105% of Mon) + 1×8 backoff at 75% [S7] | Weekly: ~2.5% or +5 lb squat/DL, +2.5 lb upper | Run ~8–12 wk then deload/reset; first ~3 weeks submax. Details vary by source; % come from a calculator [S7] |
| nSuns 5/3/1 LP | Strength + mass | Intermediate | 4 (U/L), 5, 6 variants | Lift-per-day | 9 working sets: 5/3/1+ at 75/85/95% then 6 back-off sets (squat/OHP 3/3/3/5/5/5+; DL 3×6 …+); T2 8 sets 50→70% [S30] | App implementation: top set AMRAP reps → TM +5 lb (2–3 reps), +10 (4–5), +15 (6+) [S30] | Not formally specified in sources found; start TM conservative; start with 4-day version [S30] |
| Reddit PPL (Metallicadpa) | Hypertrophy + strength | Beginner–inter. | 6 (or 3) | Push / Pull / Legs ×2 | Main lift last set AMRAP ≥5; main lifts DL, bench, squat, row, OHP (no AMRAP bench & OHP same day); accessories 8–12 reps [S31] | Sources disagree: +5 lb/session (+10 DL) vs +10 lb; accessories double progression [S31] | 3 fails → −10%; repeated stalls → intermediate program [S31]. Original thread unreachable |
| PHUL (Brandon Campbell) | Size + strength | Intermediate | 4 | Upper power / Lower power / Upper hyp / Lower hyp | Power: compounds 3–4×3–5, accessories 6–10; Hyp: 3–4×8–12, 60–90 s rest [S9] | Add reps first, then small load | Not formally specified; at least 1 RIR advice [S9] |
| PHAT (Layne Norton) | Size + power | Intermediate–adv. | 5 | Upper power, lower power, back/shoulders hyp, lower hyp, chest/arms hyp | Power: 3×3–5 main, 2–3×6–10 assist; Hyp: 8–12 compounds, 12–15 mid, 15–20 high-rep isolation [S10] | Power: double progression 3→5 reps then +5 lb; rotate power lifts every 2–3 wk | Run 4-week cycles ×3 (Biolayne) or 8–12 wk then deload (other source) [S10] |
| Candito 6-Week | Powerlifting peak | Intermediate–adv. | 4–5 (varies) | U/L variants | W1–2 conditioning/hypertrophy; W3–4 strength (85–90%+); W5 test; W6 optional deload/retest [S25] | Phase-based % | Built-in deload week; sources disagree on frequency |
| Sheiko (#29–32) | Powerlifting | Advanced | 3–4 | Comp lifts | ~70% avg intensity, very high volume, day stress classes (72h/24–48h/12–24h recovery) [S26] | Block sequence prep→accum→transmute→peak | Block structure; not beginner-friendly |
| RP hypertrophy | Size | Intermediate–adv. | 4–6 | Flexible | Start ~MEV, +1–2 sets/muscle/wk over 4–6 wk, RIR 3→0–1 [S12] | Volume then load | Deload ~wk 5 (~50% volume) or 4:1–6:1 ratio [S12] |
| Nippard Fundamentals | Size | Beginner–inter. | 3 FB / 4 U-L | FB or U/L | ~3 sets/exercise at RPE 7–9; 8-week linear progression [S24] | Weekly load/rep | Built into block; listing-based data |
| Couch to 5K (NHS) | Aerobic base | Zero base | 3 | Run/walk | 5 min warm walk + intervals + 5 min cool walk; W1 1 min run/1.5 walk ×7+1; W5 first 20 min continuous; W9 30 min [S16] | Longer intervals; repeat any week | Repeat any week until ready [S16] |
| Higdon Novice 1 marathon | Marathon finish | Beginner runner | 4 runs +1 XT +2 rest | Easy runs + long run | Long run 6→20 mi (wk 15); ~15→~40 mi/wk; half-marathon race wk 8 [S17] | Mileage | Cutbacks wks 3,6,9,12; taper wks 16–18 [S17] |
| r/bodyweightfitness RR | Gen. strength/skill | Beginner–inter. | 3 | Full body | Warm-up; 10 min skill; 3×5–8 in pairs (pull/squat, dip/hinge) + core triplet [S18] | Reach 3×8 → next progression at 3×5 | Not formal; repeat/regress level |
| Convict Conditioning | Bodyweight strength | Any | Flexible (3–6) | 6 movements | Squat, pull-up, leg raise, bridge, push-up, HSPU × 10 steps; e.g. 3×50 wall push-ups gate (only pushup fully verified) [S19] | Step gates | Not found in verified sources |
| Hybrid (Rogue/Strengthlog examples) | Strength + endurance | Inter. | 5–7 | Mixed | Mix: long Zone 2 60+ min, intervals 20–30 min, tempo run 20 min, 2–3 lifting days [S20][S21] | Practitioner | Not specified |

### Archetype selector: goal × level × days/week

| Goal | Level | Days/wk | Pick archetype | Notes |
|---|---|---|---|---|
| Strength | Novice | 3 | Starting Strength / StrongLifts / GZCLP / Greyskull | GZCLP if want more volume & back work |
| Strength | Novice | 4 | GZCLP 4-day, or SL5x5 Ultra (upper/lower) | [S2][S27] |
| Strength | Early inter. | 3 | 5/3/1 for Beginners, Texas Method, Madcow | [S6][S7][S8] |
| Strength | Inter. | 4 | 5/3/1 BBB, nSuns 4-day | |
| Strength | Inter./adv. | 5–6 | nSuns 5/6-day | high fatigue; surplus helpful |
| Strength peaking | Inter./adv. | 4–5 | Candito 6-week, Sheiko | competition prep only |
| Hypertrophy | Beginner | 3 | Nippard FB-style, GZCLP + accessories, 5/3/1 Beginners | |
| Hypertrophy | Inter. | 4 | PHUL / upper-lower | |
| Hypertrophy | Inter. | 5 | PHAT | |
| Hypertrophy | Inter. | 6 | Reddit PPL | |
| Hypertrophy | Inter.–adv. | 4–6 | RP mesocycle template | |
| Aerobic base | Zero | 3 | Couch to 5K | |
| Marathon | Beginner runner (can already run) | 4+1 | Higdon Novice 1 | |
| Bodyweight | Any | 3 | r/bodyweightfitness RR; Convict Conditioning | |
| Strength + endurance | Inter. | 5–6 | Hybrid weeks (lift 2–3 + run 2–3) | |

### Recurring numeric ranges across programs

| Variable | Typical range | Notes |
|---|---|---|
| Beginner main-lift sets × reps | 3×5, 5×5 (deadlift 1×5) | [S1][S2][S4] |
| Upper increments (LP) | +2.5–5 lb | [S1][S3] |
| Lower increments (LP) | +5–10 lb | [S1][S3] |
| Reset after failure | −10% (range −5 to −15%) | after 3 fails [S2][S22] |
| 5/3/1 TM | 90% of e1RM | [S8] |
| 5/3/1 TM jumps | +5 upper / +10 lower per 3-wk cycle | [S8] |
| Power-day reps (hybrid programs) | 3–5 | PHUL, PHAT [S9][S10] |
| Hypertrophy-day reps | 8–12 compounds; 12–20 isolation | [S9][S10] |
| Hypertrophy weekly sets per muscle | ≥10 trends better (meta); MEV start ~6–8 (RP rough) | [S12][S13] |
| Rest (strength) | 3–5 min heavy; 2–3 min assist; 60–90 s hyp | [S3][S9] |
| Mesocycle length before deload | 4–6 wk (ratio 4:1–6:1) | [S12] |
| Frequency per muscle | 2–3×/wk novice (ACSM 2009: 2–3 novice, 3–4 inter., 4–5 adv. days) | [S15] |

## Decision rules

1. IF user is a true beginner (<~6 months) AND 3 days/week AND strength/general goal THEN use full-body A/B LP (SS/StrongLifts/GZCLP pattern): squat each session, alternate bench/OHP, deadlift 1×5, row/pulldown for back, +5 lb upper/+10 lb lower per session.
2. IF beginner AND wants more back/accessory volume or 4 days THEN use GZCLP structure (T1/T2/T3) instead of 5x5.
3. IF LP lift fails the same weight 3 sessions in a row THEN reduce load ~10% (5–15%) and resume, or move down a GZCL stage; IF repeated resets on 2–3 lifts THEN move to weekly-progression (Texas/Madcow) or 5/3/1.
4. IF intermediate AND 3 days AND strength THEN Texas Method (volume/light/intensity) or Madcow, or 5/3/1 for Beginners; IF Texas stalls THEN cut volume-day sets (5×5→3×5) or lower volume-day weight 5–10%.
5. IF user wants strength-with-size, 4 days THEN 5/3/1 BBB or PHUL; IF 5–6 days AND high recovery capacity AND surplus THEN nSuns / PHAT / PPL; IF user is new to these THEN start with the 4-day version.
6. IF hypertrophy goal AND intermediate THEN each muscle ≥2×/week; target ≥10 hard sets/muscle/week (if recovery allows) — start lower (≈6–8) and ramp across 4–6 weeks.
7. IF running a hypertrophy mesocycle THEN ramp +1–2 sets/muscle/week and reduce RIR across weeks; deload after 4–6 weeks (≈50% volume) or earlier if performance drops.
8. IF 5/3/1 lifter misses reps across a full cycle THEN reduce TM 15 lb (upper)/30 lb (lower); IF AMRAP is at/near failure THEN lower effort, stop when bar speed slows.
9. IF user cannot run continuously (no base) THEN Couch to 5K: 3 runs/wk, ≥1 rest day between, repeat any week not yet comfortable.
10. IF user can run ~30 min and wants a marathon THEN 18-week Higdon-style: 4 runs, long run weekly rising to ~20 mi, cutback every ~3rd week, 3-week taper.
11. IF user has no equipment THEN r/bodyweightfitness RR pattern: 3×/wk, pull/squat and dip/hinge pairs at hardest progression for 3×5–8; progress at 3×8.
12. IF user wants hybrid strength + endurance THEN 2–3 lifting days + 2–3 runs; most running easy/Zone 2 with ≤2 hard sessions; avoid >~4 h lifting + runs without monitoring recovery; keep 1 rest day.
13. IF user is a competitive powerlifter in a meet cycle THEN use phased program (Candito/Sheiko style); IF recreational THEN do not use Sheiko volumes.
14. IF the user is sedentary, older, has a medical condition, or pain THEN do not auto-assign these programs unmodified; default to lighter volume and recommend professional screening (no medical advice here).
15. IF presenting a program to user THEN always state: schedule, sets×reps×load rule, progression, failure/reset rule, deload; and note which parts are variant-specific.

## Common mistakes

- Giving a novice an advanced program (nSuns 6-day, PHAT, Sheiko) because it "has more volume".
- Prescribing LP forever: no reset/failure rule, or no transition to weekly/cycle progression. [S1][S22]
- Using 100% of 1RM as the 5/3/1 base instead of a ~90% TM. [S8]
- Running AMRAP sets to true failure on every session; AMRAPs should leave reps in reserve. [S3][S8]
- Mixing program rules (e.g. 5/3/1 percentages with StrongLifts increments).
- Forgetting back/pulling work in press/squat-centric programs (original Greyskull gap). [S4]
- Deadlifting with 5 sets of 5 in a beginner LP; fatigue cost is high. [S1][S2]
- Treating Couch to 5K weeks as mandatory pace: repeating weeks is allowed. [S16]
- Using a program name without specifying version (Texas Method %, Madcow %, PPL increments differ by source).
- Stacking lifting and running volume without accounting for total load in hybrid plans.

## Controversies & open questions

- **Version drift**: Texas Method volume-day % (90% of 5RM vs 80–90% of intensity day), Madcow increments, PPL increments, nSuns back-off schemes, GZCLP T1 stages, Greyskull increments all differ by source. `Contested`.
- **Frequency vs volume**: small hypertrophy meta-analysis effect for higher frequency confounded by volume; strength effect vanishes when volume equated. `Moderate`/`Contested`. [S14][S23]
- **Volume ceiling**: dose-response data above ~10 sets/muscle/wk are sparse and mostly untrained subjects. [S13]
- **ACSM updated**: ACSM has issued a replacement for the 2009 position stand (overview of reviews); 2009 numbers cited here may be outdated — not verified in detail. [S15]
- **Deload necessity/timing** in RP-style approaches (50% vs ratio-based) is practitioner-derived, not RCT-backed. `Practitioner`.
- **Hybrid templates** lack an authoritative canonical source (Viada's book/app not accessible). Whether original published templates match the examples used is unverified.
- **Not found/unverified**: original r/Fitness PPL post, original Greyskull increments (Sheaffer), 5/3/1 Forever/BBB official percentages, Nippard/RP primary PDFs, Convict Conditioning step standards beyond pushup, Starting Strength official reset article (403), StrongLifts official progression pages (not retrieved).

## Related topics

- Volume landmarks & frequency (volume/frequency topic) — [S13][S14][S23].
- Progression & periodization (linear, double progression, block, deload topics).
- Splits & days-per-week mapping (upper/lower, PPL, full-body).
- Conditioning & hybrid / concurrent training (interference, Zone 2, sequencing).
- Beginners/special populations (older adults, return from layoff).
- Quality-control checklist: use the "design patterns" below to validate generated plans.

### Recurring design patterns (extracted)

| Pattern | Seen in |
|---|---|
| Few compound lifts cover squat/hinge/horizontal push/vertical push/pull | SS, SL, GZCLP, PPL, RR |
| 2–3 exposures per lift/muscle per week | All |
| Alternating A/B sessions with ≥1 rest day between | SS, SL, GZCLP, Greyskull, RR, C25K |
| One top/AMRAP set to drive autoregulation | GZCLP, Greyskull, nSuns, 5/3/1, PPL |
| Heavy/volume/light day structure for intermediates | Texas, Madcow, PHUL, PHAT |
| Lower-volume deadlift | SS, SL, Greyskull, nSuns |
| Defined failure rule (−10% / stage drop / TM cut) | All good programs |
| Accessories by rep ranges + double progression | PHUL, PHAT, PPL, RR |
| Built-in deload/test week | 5/3/1, Candito, RP, Higdon cutbacks |
| Endurance: gradual time/distance + cutbacks + taper | C25K, Higdon |
| Higher-skill progressions gated by rep standards | RR, Convict Conditioning |

## Research log

Searches: GZCLP; 5/3/1 BBB; StrongLifts; Starting Strength; Reddit PPL; r/bodyweightfitness RR; Couch to 5K; Texas Method; Greyskull; Madcow; PHUL; PHAT; nSuns; RP hypertrophy; Candito; Sheiko; Nippard; Higdon; hybrid athlete; Convict Conditioning; Schoenfeld volume & frequency meta-analyses; ACSM 2009.
Fetched OK: thefitness.wiki GZCLP and 5/3/1 for Beginners; NHS C25K; Higdon Novice 1; StrongLifts home page (limited).
Failed/blocked: thefitness.wiki Greyskull & PHUL (404), Starting Strength reset article (403), Reddit PPL thread (blocked); Nippard/RP/Viada primary materials not accessible.
Rejected: generic PDFs of unclear authorship (Nippard), marketing pages used only as secondary corroboration.
Search-tool summaries were relied upon for several programs; flagged as secondary where used.

## Sources

[S1] Starting Strength / Barbell Logic, Novice Linear Progression Program Explained. https://barbell-logic.com/starting-strength-novice-linear-progression/
[S2] FitnessVolt, StrongLifts 5x5 program summary (secondary). https://fitnessvolt.com/powerlifting/programs/stronglifts-5x5/
[S3] r/Fitness wiki mirror (thefitness.wiki), GZCLP routine page. https://thefitness.wiki/routines/gzclp/
[S4] FitnessVolt / Liftosaur, Greyskull LP and Phrak's Greyskull. https://fitnessvolt.com/rpe-training/programs/greyskull-lp/ ; https://www.liftosaur.com/programs/phrakgreyskull
[S5] Liftosaur, Texas Method program page. https://www.liftosaur.com/programs/texasmethod
[S6] Barbell Medicine, 12 Ways to Skin the Texas Method. https://www.barbellmedicine.com/blog/12-ways-to-skin-the-texas-method/
[S7] StrengthLog, Madcow 5x5 (and FitnessVolt Madcow). https://www.strengthlog.com/madcow-5x5/ ; https://fitnessvolt.com/madcow-5x5/
[S8] thefitness.wiki, 5/3/1 for Beginners. https://thefitness.wiki/routines/5-3-1-for-beginners/
[S9] Muscle & Strength / StrengthLog, PHUL workout. https://strengthlog.com/phul-workout-routine/ ; https://www.muscleandstrength.com/node/46929
[S10] Biolayne (Layne Norton), PHAT; StrengthLog PHAT. https://biolayne.com/articles/training/phat-power-hypertrophy-adaptive-training/ ; https://www.strengthlog.com/phat-workout-routine/
[S11] Liftosaur, Metallicadpa PPL. https://www.liftosaur.com/programs/metallicadpappl
[S12] Arvo / LiftVault, RP training volume landmarks and mesocycles (secondary). https://arvo.guru/resources/methods/rp-training ; https://liftvault.com/programs/bodybuilding/mike-israetel-5-week-hypertrophy-workout-routine-spreadsheet/
[S13] Schoenfeld, Ogborn, Krieger, Dose-response relationship between weekly RT volume and muscle mass: SR & MA, J Sports Sci, 2017. https://pmc.ncbi.nlm.nih.gov/articles/PMC6303131/ (see also https://paulogentil.com/pdf/Dose-response%20relationship%20between%20weekly%20resistance%20training%20volume%20and%20increases%20in%20muscle%20mass%20-%20A%20systematic%20review%20and%20metaanalysis.pdf)
[S14] Schoenfeld, Ogborn, Krieger, Effects of RT frequency on hypertrophy: SR & MA, Sports Med, 2016. https://pubmed.ncbi.nlm.nih.gov/27102172/
[S15] ACSM, Progression Models in Resistance Training for Healthy Adults (position stand), 2009; updated 2026 overview. https://www.sportgeneeskunde.com/wp-content/uploads/ACSM-Position-Stand-Progression-Models-in-Resistance-Training-for-Healthy-Adults.pdf ; https://acsm.org/science-spotlight-acsm-releases-new-position-stand-on-resistance-training/
[S16] NHS, Couch to 5K running plan. https://www.nhs.uk/better-health/get-active/get-running-with-couch-to-5k/couch-to-5k-running-plan/
[S17] Hal Higdon, Novice 1 Marathon. https://www.halhigdon.com/training-programs/marathon-training/novice-1-marathon/
[S18] r/bodyweightfitness, Recommended Routine (wiki mirrors). https://lr.psf.lt/r/bodyweightfitness/wiki/kb/recommended_routine_2017 ; https://reddit.rtrace.io/r/bodyweightfitness/wiki/kb/recommended_routine
[S19] Brikman / Breaking Muscle, Convict Conditioning reviews. https://www.ybrikman.com/blog/2020/08/10/convict-conditioning/ ; https://breakingmuscle.com/book-review-convict-conditioning-by-paul-wade/
[S20] Rogue Fitness, How to train as a hybrid athlete. https://www.roguefitness.com/eu/de/theindex/movement-library/how-to-train-as-a-hybrid-athlete-strength-and-endurance-plan
[S21] StrengthLog, 12-Week Intermediate Hybrid Athlete Program. https://www.strengthlog.com/?p=37034
[S22] Starting Strength, The Reset: Why and How. https://startingstrength.com/article/the-reset-why-and-how (not directly retrieved; cited via search summary)
[S23] Grgic et al., Effect of RT frequency on gains in muscular strength: SR & MA, Sports Med, 2018. https://pmc.ncbi.nlm.nih.gov/articles/PMC6081873/
[S24] Boostcamp listings of Jeff Nippard Fundamentals Hypertrophy (secondary). https://www.boostcamp.app/users/vmY3Wd-jeff-nippard-lu-fundamentals-hypertrophy-program
[S25] FitnessVolt / Powerlifting to Win, Candito 6-Week review. https://fitnessvolt.com/powerlifting/programs/candito-6-week/ ; https://www.powerliftingtowin.com/candito-6-week-strength-program/
[S26] Powerlifting to Win, Sizing Up Sheiko; JTS Strength. https://powerliftingtowin.com/sheiko ; https://www.jtsstrength.com/what-i-learned-at-the-russian-strength-seminar/
[S27] StrongLifts, 5x5 program overview. https://stronglifts.com/stronglifts-5x5/
[S28] Boostcamp, GZCL methodology. https://www.boostcamp.app/methodology/gzcl
[S29] LiftVault, Boring But Strong / 5/3/1 BBB pages (secondary). https://liftvault.com/resources/boring-but-strong/
[S30] Liftosaur / Boostcamp, nSuns 5/3/1 LP. https://www.liftosaur.com/programs/nsuns ; https://www.boostcamp.app/methodology/nsuns
[S31] Jefit/Liftosaur copies of Metallicadpa PPL (original r/Fitness post https://www.reddit.com/r/Fitness/comments/37ylk5 not retrievable). https://www.jefit.com/my-jefit/workouts/56252/ppl-metallicadpa
