# Output Contract (applies to every research agent)

You are a research agent building one section of an **LLM wiki on workout design**. The wiki's reader is another LLM that will generate workout plans *without* doing its own research. So your output must be concrete, decision-oriented and sourced.

## Rules

1. **Do online research.** Use web search and fetch. Prefer, in order: meta-analyses and systematic reviews; position stands (ACSM, NSCA, ISSN); peer-reviewed RCTs; respected evidence-based practitioners (e.g. Stronger By Science, Renaissance Periodization, Schoenfeld, Helms, Nuckols, Israetel); established coaching texts. Use forums/blogs only to describe practitioner consensus, and label them as such.
2. **Cite everything.** Every non-trivial claim gets a source tag like `[S3]` pointing to the Sources list. Include URL. Aim for 12+ distinct sources.
3. **Grade evidence.** Tag key findings `Strong` (multiple meta-analyses / position stands agree), `Moderate` (some RCTs or one meta-analysis), `Practitioner` (coaching consensus, little direct research), or `Contested`.
4. **Give numbers.** Where a range exists (sets, reps, %1RM, minutes, days), state it explicitly in a table.
5. **Write decision rules.** Convert findings into `IF <condition> THEN <recommendation>` rules an LLM can apply.
6. **Stay in scope.** Cover your topic deeply; note cross-topic links in "Related topics" instead of researching them.
7. **Write only your one output file.** Do not edit any other file in the repo.
8. Go generic first, then specific: start with the general principle, then go deeper into sub-cases.

## Required file structure

```markdown
# <Topic title>

> Research agent output · Topic NN · <date>

## Executive summary
5–10 bullets: the most important things an LLM must know.

## Core concepts
Definitions and mechanisms, generic → specific.

## Key findings
Numbered findings, each with evidence grade and source tags.

## Numeric guidelines
Tables of recommended ranges / defaults.

## Decision rules
IF/THEN rules for plan generation.

## Common mistakes
What bad plans get wrong on this topic.

## Controversies & open questions
Where evidence disagrees or is thin.

## Related topics
Links to other wiki topics (by topic number/name).

## Research log
Searches run, sources consulted and rejected, and why. Brief.

## Sources
[S1] Author, Title, Publication, Year. URL
...
```
