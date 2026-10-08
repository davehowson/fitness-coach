# Synthesis Contract (Wave 3 — applies to every wiki writer)

You are turning existing research into pages of an **LLM wiki on workout design**. The reader is another LLM that will build workout plans for real people **without doing any research**. Every page must let it make concrete decisions.

## Hard rules

1. **NO web research.** Do not use web search or fetch. Use only files in this repo. The research phase is closed.
2. **Precedence:** `research/03-canonical-defaults.md` > `research/raw/12-verify-resistance.md` and `research/raw/13-verify-conditioning-programs.md` (corrections) > Wave 1 raw files. Where a raw file conflicts with the canonical defaults, use the canonical number and do not repeat the conflicting one.
3. **Write only the wiki files assigned to you.** Do not edit research files or other wiki pages. No git commits.
4. **Keep evidence grades** (`Strong`, `Moderate`, `Practitioner`, `Contested`) on key claims so the reader knows how firm a rule is.
5. **Keep sources.** Each page ends with a `## Sources` section listing the sources actually used on that page (author, title, year, URL), carried over from the raw files. Cite inline as `[1]`, `[2]`… numbered per page. Never invent a source or URL.
6. **Write for an LLM:** dense, no fluff, no motivational text. Prefer tables, numbered rules and `IF … THEN …` decision rules. Generic first, then specific.
7. **Cross-link** other wiki pages by relative path, e.g. `[weekly planning](07-weekly-planning.md)`. Wiki pages (all in `wiki/`):
   - `README.md`, `00-workflow.md` (orchestrator writes these)
   - `01-principles.md`, `02-intake.md`, `03-variables.md`, `04-goals.md`, `05-session-design.md`, `06-splits.md`, `07-weekly-planning.md`, `08-progression.md`, `09-conditioning.md`, `10-hybrid.md`, `11-populations.md`, `12-exercise-library.md`, `13-program-templates.md`, `14-quality-checklist.md`
8. Don't duplicate another page's core content. Give a one-line summary and link to it instead (e.g. session pages link to `03-variables.md` for rest times instead of re-deriving them).

## Page skeleton

```markdown
# <Title>

> Purpose: <one line — what decision this page lets the LLM make>
> Use when: <situations>
> Depends on: <links>

## Key rules (TL;DR)
5–12 numbered, decision-ready rules.

## <Body sections, generic → specific>

## Decision rules
IF/THEN list.

## Common mistakes

## Evidence notes
Grades, controversies, what is unverified.

## Sources
```
