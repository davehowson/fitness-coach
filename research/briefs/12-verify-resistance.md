# Brief 12: Verification — Resistance-Training Headline Numbers

**Output file:** `research/raw/12-verify-resistance.md`
**Context:** Wave 1 research agents could not fetch many primary papers (PMC, Springer, PDFs blocked) and relied on search snippets. Your job is to verify the headline claims the wiki will depend on. Read `research/briefs/00-output-contract.md` for evidence-grade definitions, then read the raw files listed below.

## Files to audit (read-only)
`research/raw/01-foundations.md`, `02-training-variables.md`, `04-session-anatomy.md`, `05-splits.md`, `06-days-per-week.md`, `07-periodization-progression.md`, `10-individualization.md`.

## Access tips (blocked sites)
- Europe PMC REST API returns abstracts and often full text without bot blocks: `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=<terms>&format=json&resultType=core` and `https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML`.
- PubMed E-utilities: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=<terms>&retmode=json`, then `efetch.fcgi?db=pubmed&id=<PMID>&rettype=abstract&retmode=text`.
- Crossref for DOIs/metadata: `https://api.crossref.org/works?query=<terms>`.
- SportRxiv / OSF for preprints.

## Claims to verify (minimum)
1. **ACSM 2026 resistance-training position stand**: does it exist, exact citation, and what does it actually say (days/wk, sets, intensity, RIR, effect of training experience)? File 10 states specifics while files 01/03 say the full text was paywalled. Confirm or correct each specific claim in file 10.
2. Volume dose-response: Schoenfeld 2017 and Pelland et al. (2024/2025) meta-regression — fractional set counting (direct 1, indirect 0.5), diminishing returns, per-session diminishing-returns points (~2 sets strength, ~11 fractional sets hypertrophy) — publication status (preprint vs peer-reviewed).
3. Frequency: Schoenfeld 2016 and 2019, Grgic 2018 — volume-equated frequency effects on hypertrophy and strength.
4. Proximity to failure: Refalo 2023/2024, Robinson 2024 — RIR and hypertrophy/strength.
5. Load: Schoenfeld 2017 low- vs high-load meta-analysis; Lopez 2021.
6. Rest intervals: Singer 2024 and Schoenfeld 2016 rest studies; ACSM 3–5 min for heavy loads. **Resolve:** what single default rule should the wiki give for rest by exercise type/load?
7. **Resolve per-session volume cap:** Wave 1 gives 4–10, 6–10 and ~11 fractional. State one evidence-weighted default.
8. Minimum effective dose: Androulakis-Korakakis 2020; strength maintenance (Bickel 2011; Spiering 2021).
9. Periodization: Williams 2017, Moesgaard 2022 meta-analyses; DUP vs linear for hypertrophy.
10. Deload RCT (Coleman 2024); detraining/retraining (layoff ~half the time to regain).
11. Sex differences (Roberts 2020; Refalo 2023 sex), older adults power training.
12. Any other number in those files that an LLM would use as a default and that you find questionable.

## Output structure (replaces the standard contract for this task)
```markdown
# Verification: Resistance-Training Numbers
> Research agent output · Topic 12 · <date>

## Summary
## Verification table
| # | Claim (as stated, file:section) | Verdict (Confirmed / Corrected / Unverifiable / Wrong) | Correct statement | Evidence grade | Source |
## Resolutions
Single recommended defaults for: rest intervals; per-session volume cap; default RIR; weekly set ranges per goal.
## Corrections for the wiki
Bullet list: file → what to change.
## Research log
## Sources
```

## Rules
- Write ONLY `research/raw/12-verify-resistance.md`. Do not edit the files you audit. No git commits.
- Mark a claim Confirmed only if you read the primary abstract or full text yourself.

## Done when
All claims 1–11 have a verdict with a primary source (or are marked Unverifiable with the reason), and the Resolutions section gives single defaults.
