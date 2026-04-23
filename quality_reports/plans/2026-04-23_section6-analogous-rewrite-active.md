## Objective

Rewrite the active sectoral-transmission section in `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex` so it follows the `2026-04-22_section6-analogous-rewrite-instruction-set.md` while preserving the current empirical content and figure set.

## Scope

- Keep the current active section architecture centered on:
  - aggregate sectoral ranking
  - structural determinants
  - own-sector incidence
  - own-vs-cross propagation
  - euro-area third-country accounting
- Rewrite prose to be more claim-driven, asymmetry-driven, and mechanism-first.
- Add at least one overall quantitative measure of the relative strength of the cross-sector term against the own-sector term.
- Keep labels and figure references stable where possible.
- Recompile `0_main.tex` in place after the rewrite.

## Source Inputs

- `quality_reports/specs/2026-04-22_section6-analogous-rewrite-instruction-set.md`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- current active figure pipeline outputs in `master_supporting_docs/MCMS/output_python/extra_charts/`

## Intended Quantitative Summary

- Use current decomposition objects to summarize cross-vs-own strength:
  - US: absolute cross-sector mass is about 78% of absolute own-sector mass; cross term larger than own term in 11 of 20 rows
  - China: about 37%; 7 of 20 rows
  - EA: about 29%; 6 of 20 rows

## Verification

- Compile `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex` in place.
- Check that section references still resolve as before apart from the manuscript’s pre-existing undefined refs.
- Review the rewritten section locally for compliance with the instruction set: opening triad, claim-first paragraphs, mechanism ordering, and offsetting-margins framing.
