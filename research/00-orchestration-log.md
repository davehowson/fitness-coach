# Orchestration Log

Chronological record of everything done to build the workout-design LLM wiki.

## 2026-10-08 — Phase 1: scoping (no research yet)

- User request: build an LLM wiki on how to create a good workout, top-down from generic principles to specifics (types, hybrid, strength, days-per-week, splits, composition). Understand the domain first; then orchestrate Sonnet research agents via Orca; document everything in Markdown.
- Verified Orca runtime: `orca` runtime `ready`. Loaded `orchestration` and `orca-cli` skill guides plus `references/coordinator-loop.md` (model selection via `--model`).
- Wrote `research/01-domain-map.md`: 12-layer map of what goes into a good workout (inputs → principles → variables → goals → session → splits → days/week → periodization → conditioning/hybrid → individualization → QA → reference programs). Written from prior knowledge, flagged as hypotheses.
- Wrote `research/02-research-plan.md`: 3 waves (parallel research → gap review → wiki synthesis), 11 Wave-1 topics, provisional wiki structure.
- Wrote `research/briefs/00-output-contract.md` (shared output format: evidence grades, numeric tables, IF/THEN decision rules, sources) and 11 topic briefs `research/briefs/01..11-*.md`.
- **Next:** user approval, then launch Wave 1 (11 Sonnet workers via `orca orchestration worker-start --agent claude --model sonnet`).

## 2026-10-08 — Wave 1 launched

- User approved launch.
- Orca Run created.
- 11 workers started with `orca orchestration worker-start --worktree current --agent claude --model sonnet`; every receipt confirmed `launch.effective.model = sonnet`.

| Topic | Task | Dispatch |
|---|---|---|
| 01-foundations | task_9c067bab69c2 | ctx_8a33f250cbfc |
| 02-training-variables | task_f974a58e8ae2 | ctx_8209fb47afc1 |
| 03-goals-and-types | task_c8c66cb748e9 | ctx_662f1cc3a8d6 |
| 04-session-anatomy | task_56a0ac8a2416 | ctx_8ac6db18d1e2 |
| 05-splits | task_85bc38101f00 | ctx_1283d73f44d6 |
| 06-days-per-week | task_c10fbf57ac7b | ctx_1e826f3e4e9c |
| 07-periodization-progression | task_a748d100cf12 | ctx_8a6b1563bc46 |
| 08-conditioning | task_1eb96deafd96 | ctx_3b051861e239 |
| 09-hybrid-training | task_2189774213f1 | ctx_1b6f85a677b1 |
| 10-individualization | task_385338bac373 | ctx_6d6380579ef4 |
| 11-reference-programs | task_acd5c1966f20 | ctx_04bc6828a6c9 |

## Wave 1 completions

- **04-session-anatomy** (ctx_8ac6db18d1e2) — succeeded. 19 sources. Worker caveat: relied on search summaries rather than full-text fetches; some figures secondary, URLs S3/S5/S19 unverified; not findable: Maia 2019 superset paper, push:pull injury trials, carry/anti-rotation dosing. → flag for Wave 2 verification. Worker released.
- **01-foundations** (ctx_8a33f250cbfc) — succeeded. 18 sources. Caveat: WHO full text, 2026 ACSM stand, US PAG PDF, ACSM 2009 PDF failed to fetch; WHO strength wording and 2026 ACSM parameters flagged unverified; S5/S6 overlap. → Wave 2 verification. Released.
- **05-splits** (ctx_1283d73f44d6) — succeeded. 21 sources, 14-split comparison table. Core finding: volume-equated frequency has no significant effect on hypertrophy (Strong) or strength (Moderate). Caveat: secondary summaries; S10/S12/S14 unverified; missed-day/rolling-split guidance is practitioner synthesis. → Wave 2 verification. Released.
- **03-goals-and-types** (ctx_662f1cc3a8d6) — succeeded. 22 sources, 22 rules. Caveat: abstracts only; ACSM 2026 RT position stand paywalled (HTTP 402), numbers not used; goal-blending ratios Practitioner-level. Released.
- **09-hybrid-training** (ctx_1b6f85a677b1) — succeeded. 23 sources, 3–7 day templates. Key: concurrent training barely affects strength/hypertrophy (SMD −0.06/−0.01), hurts power (−0.28). Caveat: Wilson/Hickson/Schumann via secondary summaries; Bare/Crawley/Viada exact programs not findable. Released.
- **08-conditioning** (ctx_3b051861e239) — succeeded. 15 sources, 2–5 session weekly plans. Caveat: Schumann/Oliveira/Garber/Wilson/Helgerud not fetchable; figures marked "(secondary)". Released.
- **07-periodization-progression** (ctx_8a6b1563bc46) — succeeded. 25 sources. Caveat: PMC/Springer bot-blocked; Bell 2023, Hickmott 2022, Coleman 2024, RP and 5/3/1 details from summaries; %-RPE table is general convention. Released.
- **Cross-cutting observation:** workers repeatedly report PMC/Springer/PDF fetches blocked, so many primary numbers are secondary. Wave 2 must include a targeted verification pass on the headline numbers.
- **06-days-per-week** (ctx_1e826f3e4e9c) — succeeded. 19 sources, Mon–Sun calendars (2–4 options) for 1–7 days. Caveat: ACSM 2026, Grgic 2018, Wilson 2012, Fyfe 2014 unreachable; calendars and per-session set ranges are practitioner synthesis. Released.
- **02-training-variables** (ctx_8209fb47afc1) — succeeded. 23 sources, per-goal default tables. Caveat: many figures from abstracts; no controlled myo-rep evidence found. Released.
- **11-reference-programs** (ctx_04bc6828a6c9) — succeeded. ~20 programs, 31 sources, archetype selector. Caveat: Greyskull, Madcow, nSuns, PPL, PHUL/PHAT, Nippard, RP, Sheiko, hybrid from secondary sources; Texas Method % and Greyskull increments worth verifying. Released.
- **10-individualization** (ctx_6d6380579ef4) — succeeded. 20 sources, pattern × equipment substitution matrix. Caveat: youth set/rep numbers, NSCA older-adult dosing, WHO ≥2 d/wk wording, ACSM obesity figures from secondary sources. Released.
- **Wave 1 complete:** 11/11 succeeded, all workers released.

## 2026-10-08 — Wave 2: review, verification, gap-fill

Orchestrator review of Wave 1 executive summaries found:
1. **ACSM 2026 stand conflict:** file 10 states specific findings from it; files 01/03 report its full text was paywalled. Needs verification.
2. **Rest for heavy lifts:** 02 says 2–3 min for compounds; 04 cites ACSM 3–5 min for 1–6RM. Needs one rule.
3. **Per-session volume cap:** 4–10 (06), ≤6–10 (04), ~11 fractional (preprint, 04). Needs one default.
4. **Systemic:** primary papers mostly read via secondary summaries (PMC/Springer bot-blocked).
5. **Gap:** no exercise library (pattern × muscle × equipment × fatigue) for concrete exercise selection.

Otherwise the files agree on the core: weekly hard sets per muscle as the main dial, ≥2×/muscle/week as default frequency, frequency ~irrelevant when volume equated, interference minimal for strength/hypertrophy but real for power, double progression default, adherence as tiebreaker.

Wave 2 workers (Sonnet), with briefs pointing them to Europe PMC / PubMed E-utilities / Crossref APIs to bypass blocks:

| Topic | Task | Dispatch |
|---|---|---|
| 12-verify-resistance | task_4ed549230e43 | ctx_1d98ff61f53d |
| 13-verify-conditioning-programs | task_13e6db736b33 | ctx_80f331563181 |
| 14-exercise-library | task_ce84aab75f74 | ctx_33287ff3437e |
- **14-exercise-library** (ctx_33287ff3437e) — succeeded. Tables for all patterns, 12 isolation groups, power, conditioning, RAMP drills; 16 sources. Caveat: figures from search summaries; skill/fatigue/axial ratings are practitioner defaults (acceptable for a library). Released.
- **12-verify-resistance** (ctx_1d98ff61f53d) — succeeded. Primary abstracts/full text via Europe PMC/PubMed/Crossref. Key: ACSM 2026 (Currier et al.) full text read — 2–3 RIR only a hedged suggestion, no rest guidance, experience claim carried from 2023 NMA; Pelland peer-reviewed (Sports Med 2025), but ~2/~11 per-session figures are a preprint point-of-diminishing-returns, not a cap; "retrain in half the layoff" is a blog estimate only. Released.

## 2026-10-08 — User direction: no further research

User: stop new research unless absolutely necessary; synthesize what exists. Worker 13 (already running) allowed to finish; no further research tasks will be launched. Wave 3 synthesis workers are instructed not to do web research.
- **13-verify-conditioning-programs** (ctx_80f331563181) — succeeded. Headline stats confirmed via PubMed/Europe PMC, WHO/PAG text, official program pages. Corrections: Schumann moderators, Oliveira polarized qualifiers, HIIT fat loss (Viana vs Wewege), PAG older-adult wording, Starting Strength reset rule, nSuns TM rule, Madcow, PPL increments, Higdon cutbacks; 60–70% goal-blend rule is Practitioner-only. Unverifiable: Wilson thresholds, Hickson details, Greyskull/PHUL originals, Texas Method 90%, Wendler beginners article. Released.
- **Wave 2 complete:** 3/3 succeeded, 0 reclaimable workers.

## 2026-10-08 — Wave 3: wiki synthesis (no web research)

- Orchestrator wrote `research/03-canonical-defaults.md`: binding numbers that resolve all Wave 1 conflicts using the Wave 2 verifications (rest 3 min heavy / 2 min hypertrophy compound / 90 s isolation; per-session soft cap 10 fractional sets; default 2 RIR; weekly sets by goal and level; conditioning/hybrid corrections; program corrections).
- Wrote `research/briefs/20-synthesis-contract.md` (no web research; precedence canonical > verify > raw; per-page skeleton; sources carried over) and 7 synthesis briefs `21-synth-*.md`.
- Launched 7 Sonnet synthesis workers:

| Group | Wiki pages | Task | Dispatch |
|---|---|---|---|
| A-foundations | 01-principles, 02-intake, 14-quality-checklist | task_adcc603daf5c | ctx_0565fca0f15a |
| B-variables-session | 03-variables, 05-session-design | task_72befdae5c89 | ctx_f24231ba441e |
| C-goals-populations | 04-goals, 11-populations | task_42377bf95bfa | ctx_fae66259d801 |
| D-splits-weekly | 06-splits, 07-weekly-planning | task_66180ad6006b | ctx_f12ef604ca70 |
| E-progression | 08-progression | task_e919dfa44bdc | ctx_68c09fbe36ba |
| F-conditioning-hybrid | 09-conditioning, 10-hybrid | task_aefb2a29da4a | ctx_724ef5ca900d |
| G-exercises-programs | 12-exercise-library, 13-program-templates | task_c3e329cb558b | ctx_bac3dd575da0 |

- Orchestrator writes `wiki/README.md` and `wiki/00-workflow.md`.
- **E-progression** (ctx_68c09fbe36ba) — succeeded: wiki/08-progression.md. Note: raw/07 and raw/12 shared one PMC URL (PMC10809978) for Bell 2023 and Coleman 2024; writer used the shura PDF for Bell and PMC for Coleman. Released.
- **B-variables-session** (ctx_f24231ba441e) — succeeded: wiki/03-variables.md, wiki/05-session-design.md (7 session templates). Released.
- **C-goals-populations** (ctx_fae66259d801) — succeeded: wiki/04-goals.md, wiki/11-populations.md. Youth and obese dosing remain Practitioner. Released.
- **G-exercises-programs** (ctx_bac3dd575da0) — succeeded: wiki/12-exercise-library.md, wiki/13-program-templates.md (20 programs, raw/13 corrections applied, unverified items labelled). Released.
- **F-conditioning-hybrid** (ctx_724ef5ca900d) — succeeded: wiki/09-conditioning.md, wiki/10-hybrid.md. Writer adjusted raw templates so no hard run follows heavy legs within 24 h; 10×1 protocol and calendars Practitioner. Released.
- **A-foundations** (ctx_0565fca0f15a) — succeeded: wiki/01-principles.md, wiki/02-intake.md (YAML schema, question list, defaults, red flags), wiki/14-quality-checklist.md (14-item scored checklist with critical gates). Released.
- **D-splits-weekly** (ctx_f12ef604ca70) — succeeded: wiki/06-splits.md, wiki/07-weekly-planning.md (1–7 day playbook, 2–4 calendars each). Released.
- **Wave 3 complete:** 7/7 succeeded, 0 reclaimable workers.

## 2026-10-08 — Final QA and close-out

- Orchestrator QA: 16 wiki pages, ~3,900 lines. Automated checks: no broken relative links; every topic page has Key rules / Decision rules / Sources; no conflicting canonical numbers found (remaining "3–5 min" mentions are labelled ACSM 2009 or program-specific rest; the "3 failures" mentions are correctly attributed to StrongLifts/PPL). Spot-checked `07-weekly-planning.md`: arithmetic, calendars and recovery spacing consistent with canonical defaults.
- Orca Run: 21 dispatches in total (11 research + 3 verification/gap + 7 synthesis), all succeeded and all released; 0 reclaimable terminals.
- Known limitations carried into the wiki (labelled there): calendars, exercise ratings, youth/obese dosing and the goal-blend heuristic are Practitioner; Greyskull, PHUL originals, Texas Method 90% and Wilson 2012 thresholds are unverified; the per-session volume figures come from a preprint.
- Nothing committed to git (awaiting user approval).
