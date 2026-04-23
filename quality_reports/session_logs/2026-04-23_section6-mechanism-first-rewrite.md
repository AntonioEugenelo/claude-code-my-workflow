## Summary

Rewrote the active Section 6 in `55b_sectoral_transmission_decomposition.tex` so it follows the current Section 4 logic more closely. The section now leads with mechanisms and uses the figures as supporting evidence rather than as the organizing narrative.

## Files Changed

- `quality_reports/plans/2026-04-23_section6-mechanism-first-rewrite.md`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55b_sectoral_transmission_decomposition.tex`

## What Changed

- Preserved the current three-part section structure:
  - `6.1 Direct Exposure and the Aggregate Ranking`
  - `6.2 Own-Sector versus Cross-Sector Incidence`
  - `6.3 The Euro Area as an Offsetting-Margins Object`
- Kept the earlier merged lower-level topics as subsubsections:
  - `6.1.1 Benchmark Sectoral Incidence`
  - `6.1.2 Mechanisms behind the sectoral ranking`
  - `6.2.1 Direct Incidence Inside the Tariffed Sector`
  - `6.2.2 Cross-Sector Propagation in the United States and China`
- Replaced figure-led exposition with mechanism-led exposition:
  - direct bilateral exposure now appears explicitly as the first-stage sorting mechanism for the US/China cross section,
  - IO centrality and price flexibility are described as conditional amplification/composition mechanisms rather than competing first-order sorters,
  - the own-versus-cross identity is used as the core mechanism linking direct incidence to aggregate incidence,
  - the euro area is framed as a third-country net object driven by offsetting gross margins.
- Reduced sentence-level figure narration. The revised prose now states the mechanism first and then points to the relevant figures as evidence for that mechanism.
- Tightened the closing bridge so the section now hands off to the next section in a claim-driven way.

## Verification

- Recompiled from `master_supporting_docs/Tariffs_ECB/0_clean` with:
  - `latexmk -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex`
- Compile succeeded after the rewrite and again after the final wording polish.
- Checked `build_verify/0_main.aux` and confirmed the section numbering remains:
  - `6.1` `sec:new_sectoral_ranking`
  - `6.1.1` `sec:new_sectoral_aggregate_effects`
  - `6.1.2` `sec:new_sectoral_determinants`
  - `6.2` `sec:new_sectoral_incidence_wedge`
  - `6.2.1` `sec:new_sectoral_own_effects`
  - `6.2.2` `sec:new_sectoral_cross_terms`
  - `6.3` `sec:new_sectoral_ea`

## Review Notes

- Manual prose review only.
- Checked specifically for the user's reported failure mode:
  - benchmark paragraphs now state the asymmetry before mentioning figures,
  - mechanism subsections explain causal roles before citing visual support,
  - the euro-area discussion is framed as an offsetting-margins explanation rather than as a panel summary.
- The rewritten section is materially closer to the current Section 4 pattern than the prior draft.

## Residual Issues

- The manuscript still reports the same pre-existing duplicate-label and undefined-reference warnings outside this task.
- Inside the nested `master_supporting_docs/Tariffs_ECB` repo, `55b_sectoral_transmission_decomposition.tex` continues to appear as an untracked file; this does not affect compilation but is worth keeping in mind for any later git operation inside the nested repo.
