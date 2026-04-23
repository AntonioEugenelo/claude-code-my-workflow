## Objective

Update the active Section 6 so Figure 16 is removed from the manuscript discussion, Figure 15 labels as many points as possible without overlap, and the own-versus-cross accounting equation is replaced by the explicit value-added decomposition requested by the user.

## Scope

- Edit `master_supporting_docs/Tariffs_ECB/0_clean/sections/55b_sectoral_transmission_decomposition.tex`.
- Edit the Figure 15 generator in `master_supporting_docs/MCMS/new_process.py`.
- Regenerate the affected figure asset used by the paper.
- Recompile the manuscript.

## Files Likely To Change

- `quality_reports/plans/2026-04-23_section6-figure15-and-equation-update.md`
- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55b_sectoral_transmission_decomposition.tex`
- regenerated `master_supporting_docs/Tariffs_ECB/0_clean/figures/Fig_CN_Structural_Scatter.png`

## Assumptions

- “Remove Figure 16” means remove the United States/China heatmap figure from the active Section 6 text, not necessarily delete the PNG from disk.
- “All the points you can” means maximize labels subject to readability, not force all labels when they would overlap materially.
- The requested decomposition formula should replace the current compact identity in the Section 6.2.2 discussion while keeping the own-sector and cross-sector interpretation explicit.

## Verification

- Regenerate Figure 15 and confirm the output file updates successfully.
- Compile `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex` with `latexmk -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex`.
- Manually review:
  - Figure 15 label density/readability
  - absence of Figure 16 from Section 6
  - correctness and readability of the new decomposition equation
