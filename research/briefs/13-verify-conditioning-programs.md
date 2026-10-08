# Brief 13: Verification — Conditioning, Hybrid, Goals & Reference Programs

**Output file:** `research/raw/13-verify-conditioning-programs.md`
**Context:** Wave 1 research agents could not fetch many primary papers and program originals, and relied on search snippets and aggregators. Verify the headline claims the wiki will depend on. Read `research/briefs/00-output-contract.md` for evidence-grade definitions, then read the raw files below.

## Files to audit (read-only)
`research/raw/03-goals-and-types.md`, `08-conditioning.md`, `09-hybrid-training.md`, `11-reference-programs.md`.

## Access tips (blocked sites)
- Europe PMC REST API: `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=<terms>&format=json&resultType=core` and `.../rest/<PMCID>/fullTextXML`.
- PubMed E-utilities: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=<terms>&retmode=json`, then `efetch.fcgi?db=pubmed&id=<PMID>&rettype=abstract&retmode=text`.
- For programs: author sites, archived copies via `https://web.archive.org/web/2024*/<url>`, the r/Fitness wiki, and the authors' books' published descriptions.

## Claims to verify (minimum)
1. Schumann 2022 concurrent-training meta-analysis: SMDs for max strength (−0.06), hypertrophy (−0.01), explosive strength (−0.28); moderators (same session, <3 h gap, training status).
2. Wilson 2012 meta-analysis: interference by endurance modality, frequency, duration. Hickson 1980 design.
3. Huiberts 2023/2024 sex-difference finding (SMD −0.43 males lower-body strength).
4. Murlasits 2018 sequencing meta-analysis (lifting first, ~+4 kg lower-body 1RM).
5. Spacing RCT(s) (0 h vs 6 h vs 24 h) — exact paper and findings.
6. Polarized vs other intensity distributions meta-analysis (SMD 0.24 VO2peak) — exact paper.
7. HIIT vs MICT for VO2max and fat loss — key meta-analyses (e.g. Milanović 2015, Wewege 2017, Viana 2019).
8. Zone 2 evidence claims; talk-test validity; the 10% rule RCT (Buist 2008).
9. Longevity: muscle-strengthening ~30–60 min/wk dose and mortality (Momma 2022); cardiorespiratory fitness and mortality.
10. WHO 2020 / US PAG 2018 exact wording (aerobic minutes; muscle-strengthening ≥2 days; older adults multicomponent ≥3 days).
11. Reference programs — verify exact structure from original or authoritative sources: Starting Strength, StrongLifts 5x5, GZCLP, Greyskull LP, 5/3/1 (+BBB, for Beginners), Texas Method percentages, Madcow 5x5, nSuns, Reddit PPL (Metallicadpa), PHUL, PHAT, Couch to 5K, Hal Higdon Novice 1, r/bodyweightfitness RR. Note version differences.
12. Goal-blend rule "primary goal ~60–70% of weekly hard-set volume": any source, or confirm it is Practitioner-only.

## Output structure (replaces the standard contract for this task)
```markdown
# Verification: Conditioning, Hybrid, Goals & Programs
> Research agent output · Topic 13 · <date>

## Summary
## Verification table
| # | Claim (as stated, file:section) | Verdict (Confirmed / Corrected / Unverifiable / Wrong) | Correct statement | Evidence grade | Source |
## Program verification
Per program: verified structure, progression, reset rules, version notes, source.
## Corrections for the wiki
Bullet list: file → what to change.
## Research log
## Sources
```

## Rules
- Write ONLY `research/raw/13-verify-conditioning-programs.md`. Do not edit audited files. No git commits.
- Mark Confirmed only if you read the primary abstract/full text or the original program source yourself.

## Done when
All claims 1–12 have a verdict with a source (or Unverifiable with reason).
