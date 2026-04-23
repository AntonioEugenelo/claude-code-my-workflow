# Figure Reviewer Review: Section 5, Round 1

**Target:** `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
**Reviewer:** `figure-reviewer`
**Round:** 1
**Score:** `92/100`

## Findings

1. `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex:51` claim: “Pooling across rows, service sectors account for 82.5% of the absolute US spillover mass.” Verdict: `FAIL`. Using the current sector map (`services = 24-44`) and `Figure_SectoralSpillover_Matrix.csv`, services account for `77.5%` of the absolute US spillover mass, not `82.5%`.
2. `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex:11,29,49,75-79` and the linked cross-section tables: `PASS` to rounding. The section’s bar rankings, spillover arithmetic, and euro-area own-vs-aggregate incidence statements match the current generated artifacts.
3. `Fig_SectoralSpillover_USA.png`, `Fig_SectoralSpillover_CHN.png`, and `Fig_EA_Sectoral_Heatmap_USCN.png`: `PASS`. The rendered matrices are vertically stacked, the diagonal cells are black outlined, and the blue/yellow sign convention matches the captions.

## Notes

- The bar and matrix objects are consistent with the current figure/data outputs after rounding.
