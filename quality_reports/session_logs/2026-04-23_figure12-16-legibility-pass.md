# 2026-04-23 Figure 12 and Figure 16 Legibility Pass

## Scope

- Increased typography in the active EA sectoral trade-margin figure.
- Matched the center-panel gross import/export bar thickness to the side panels.
- Switched the net-balance marker to a brighter gold marker with a darker edge.
- Reduced label density in the own-sector value-added/inflation scatter and increased label size and legibility.

## Source Edit

- `master_supporting_docs/MCMS/new_process.py`

## Verification

- Scoped figure regeneration succeeded via direct calls to:
  - `create_active_ea_sectoral_trade_margins(...)`
  - `create_active_cn_structural_scatter(...)`
  - `sync_paper_figures(...)`
- Refreshed paper-facing outputs:
  - `master_supporting_docs/Tariffs_ECB/0_clean/figures/Fig_EA_Sectoral_Trade_Margins.png`
  - `master_supporting_docs/Tariffs_ECB/0_clean/figures/Fig_CN_Structural_Scatter.png`
- Direct image inspection confirmed:
  - larger text and thicker center-panel bars in the EA trade figure
  - 14 larger labels in the own-sector scatter with visibly lower clutter

## Compile Status

- `latexmk -pdf -interaction=nonstopmode -halt-on-error 0_main.tex` did not complete because of pre-existing manuscript issues outside this figure edit:
  - duplicate BibTeX keys in `bibliography.bib`
  - Unicode minus `U+2212` in `sections/11_introduction.tex`
