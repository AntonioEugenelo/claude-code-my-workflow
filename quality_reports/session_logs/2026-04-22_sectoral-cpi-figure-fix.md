## Summary

Updated the section-5 benchmark inflation-figure pipeline to use exact sector-bundle CPI contributions from the full Dynare first-order solution instead of the legacy `pi_{k,i}` object.

## Files

- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_6_Baseline_Bars_CrossSection.csv`
- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_SectoralSpillover_Matrix.csv`
- `master_supporting_docs/MCMS/output_python/extra_charts/Fig_Sectoral_Bars_CPI.png`
- `master_supporting_docs/MCMS/output_python/extra_charts/Fig_CN_Sectoral_Heatmap.png`
- `master_supporting_docs/MCMS/output_python/extra_charts/Fig_CN_Structural_Scatter.png`
- `master_supporting_docs/MCMS/output_python/extra_charts/Fig_SectoralSpillover_USA.png`
- `master_supporting_docs/MCMS/output_python/extra_charts/Fig_SectoralSpillover_CHN.png`

## Verification

- Regenerated the benchmark cross-section CSV plus the CPI-related PNG outputs from `new_process.py`.
- Synced the refreshed figure files into `master_supporting_docs/Tariffs_ECB/0_clean/figures/`.
- Verified from the regenerated CSVs that, after mapping the benchmark rows to the actual tariffed model sector IDs, the spillover-matrix row sums match aggregate CPI to machine precision.
- Verified that the spillover diagonal matches the regenerated own-sector CPI contribution columns exactly.

## Notes

- Figure labels now refer to CPI contributions rather than sectoral inflation where the underlying object changed.
- Manuscript captions/body text were not updated in this pass.
