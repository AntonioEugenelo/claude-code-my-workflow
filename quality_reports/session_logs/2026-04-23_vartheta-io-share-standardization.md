# 2026-04-23 vartheta IO share standardization

- Standardized active manuscript prose in `master_supporting_docs/Tariffs_ECB/0_clean` so `\vartheta_{ki}` is described as the `IO share`, not `IO centrality`.
- Updated active chart labels in `master_supporting_docs/MCMS/new_process.py` from older variants (`IO centrality`, `Input-Output Share`) to `IO Share` where relevant.
- Patched generated appendix horse-race tables in `master_supporting_docs/Tariffs_ECB/0_clean/generated/` so the compiled appendix no longer reintroduced `IO intensity`.
- Added an active appendix `3x4` structural-scatter refresh path in `master_supporting_docs/MCMS/new_process.py`, regenerated:
  - `Fig_EA_Structural_Scatter_3x4.png`
  - `Fig_CHN_Structural_Scatter_3x4.png`
  - `Fig_US_Structural_Scatter_3x4.png`
- Fixed the paper-figure sync manifest so those appendix figures are copied into `master_supporting_docs/Tariffs_ECB/0_clean/figures/`.
- Recompiled the manuscript successfully with:
  - `latexmk -pdf -interaction=nonstopmode -halt-on-error 0_main.tex`

Remaining compile warnings are pre-existing and non-blocking:
- undefined references
- multiply defined labels
- SyncTeX file-lock warning
