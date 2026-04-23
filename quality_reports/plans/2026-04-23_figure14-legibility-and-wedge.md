## Objective

Improve the legibility of Figure 14 (`Fig_CN_Structural_Scatter.png`) by decompressing the y-dimension within the existing figure footprint, verify that the claims in Section 6.2.2 match the cumulative transmission-matrix data, and move the own-versus-cross aggregate wedge decomposition to the start of Section 6.2 with explicit underbraces.

## Scope

- Update the active scatter generator in `master_supporting_docs/MCMS/new_process.py`.
- Regenerate and sync the updated Figure 14 export.
- Rewrite the opening of Section 6.2 in `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`.
- Tighten the Section 6.2.2 narrative only where the current wording overstates or misstates the matrix evidence.
- Recompile the manuscript and confirm the active PDF reflects the updated figure and text.

## Likely Files To Change

- `quality_reports/plans/2026-04-23_figure14-legibility-and-wedge.md`
- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `quality_reports/session_logs/2026-04-23_figure14-legibility-and-wedge.md`

## Assumptions

- A transformed y-axis is acceptable so long as the sign and ordering of own-sector inflation are preserved and the figure remains the same overall size.
- The user wants the accounting decomposition moved to the start of subsection 6.2, before the own-sector and matrix subsubsections.
- Existing regenerated cumulative CSVs remain the source of truth for checking the Section 6.2.2 claims.

## Verification

- Regenerate the active scatter figure from source and sync it into the paper figures directory.
- Recompile `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex` with `latexmk -g -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex`.
- Visually inspect the updated Figure 14 for improved y-axis legibility.
- Re-check the Section 6.2.2 prose against the cumulative matrix CSV summaries before closing the task.
