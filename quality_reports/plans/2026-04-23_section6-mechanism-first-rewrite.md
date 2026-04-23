## Objective

Rewrite the active Section 6 in `55b_sectoral_transmission_decomposition.tex` so it follows the current Section 4 pattern more closely: opening triad, mechanism-first exposition, figures used as supporting evidence rather than as the organizing logic, and a final euro-area subsection framed as an offsetting-margins object.

## Scope

- Rewrite the prose and heading logic of `master_supporting_docs/Tariffs_ECB/0_clean/sections/55b_sectoral_transmission_decomposition.tex`.
- Preserve the current three top-level subsection structure created in the prior merge pass unless a local heading change is needed to make the logic cleaner.
- Keep the earlier user constraint that the formerly separate topics remain distinguishable at the lower heading level.
- Reduce panel-by-panel narration and emphasize:
  - direct exposure as the first-order sorting mechanism,
  - the own-sector versus cross-sector wedge as the core domestic propagation mechanism,
  - the euro area as a third-country offsetting-margins object.

## Files Likely To Change

- `quality_reports/plans/2026-04-23_section6-mechanism-first-rewrite.md`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55b_sectoral_transmission_decomposition.tex`

## Assumptions

- The user wants the active Section 6 to remain organized around the three opening facts, but with the prose inside each subsection rewritten in a more mechanism-led style analogous to current Section 4.
- No figure regeneration is needed; the existing figures are sufficient as evidence objects for the rewrite.
- Previously verified directional claims for the section remain valid, so this pass is primarily a structural and interpretive rewrite rather than a numerical audit.

## Verification

- Compile `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex` with `latexmk -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex`.
- Check `build_verify/0_main.aux` to confirm Section 6 numbering remains coherent after the rewrite.
- Run a manual prose review against:
  - the 2026-04-22 section-6 analogous rewrite instruction set,
  - the mechanism/results ordering used in current Section 4,
  - the user's request to avoid figure-driven narration.
