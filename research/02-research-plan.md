# Research Plan

Status: **Complete.** All three waves ran; see `00-orchestration-log.md`. Final wiki pages are listed in `wiki/README.md` (the structure below was provisional).

## Approach

- **Orchestrator:** main Claude session (Opus), coordinating through Orca orchestration (Run → Tasks → Dispatches).
- **Workers:** Claude agents on **Sonnet** (`worker-start --agent claude --model sonnet`), one per research topic, all working in this repo.
- **Wave 1:** 11 independent research tasks, run in parallel. Each writes one raw research file.
- **Wave 2:** orchestrator reviews raw files for gaps and contradictions, may dispatch follow-up tasks.
- **Wave 3:** synthesis into `wiki/` — the LLM-facing knowledge base.

## Directory layout

```
research/
  00-orchestration-log.md   # chronological log of everything done
  01-domain-map.md          # pre-research understanding (Phase 1)
  02-research-plan.md       # this file
  briefs/NN-topic.md        # full brief given to each research agent
  raw/NN-topic.md           # raw research output, one per agent, with sources
wiki/                       # final LLM wiki (built in Wave 3)
```

## Wave 1 tasks

| # | Topic | Covers domain-map layers | Output |
|---|---|---|---|
| 01 | Foundations: what makes a good program | 1, 2, 11 | `raw/01-foundations.md` |
| 02 | Resistance training variables & dose-response | 3 | `raw/02-training-variables.md` |
| 03 | Training goals & workout types | 4 | `raw/03-goals-and-types.md` |
| 04 | Session anatomy: building a single workout | 5 | `raw/04-session-anatomy.md` |
| 05 | Training splits catalog | 6 | `raw/05-splits.md` |
| 06 | Days-per-week mapping & combining splits | 6, 7 | `raw/06-days-per-week.md` |
| 07 | Periodization & progression | 8 | `raw/07-periodization-progression.md` |
| 08 | Cardio & conditioning | 9 | `raw/08-conditioning.md` |
| 09 | Hybrid / concurrent training | 9 | `raw/09-hybrid-training.md` |
| 10 | Individualization & special populations | 10 | `raw/10-individualization.md` |
| 11 | Reference programs catalog | 12 | `raw/11-reference-programs.md` |

Full briefs: `research/briefs/`. All briefs share the output contract in `research/briefs/00-output-contract.md`.

## Planned wiki structure (Wave 3, provisional)

```
wiki/
  README.md                     # entry point: how an LLM should use this wiki
  00-workflow.md                # step-by-step: intake → plan → QA
  01-principles.md
  02-variables/                 # volume, intensity, frequency, rest, selection, order
  03-goals/                     # one file per goal type
  04-session-design.md
  05-splits/                    # one file per split + comparison
  06-weekly-planning/           # one file per days-per-week (1–7)
  07-periodization.md
  08-conditioning.md
  09-hybrid.md
  10-populations/
  11-templates/                 # reference programs as worked examples
  12-quality-checklist.md
  sources.md
```
