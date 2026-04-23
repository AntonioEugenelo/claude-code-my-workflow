Task: clarify Figure 15, remove the household/intermediate discussion from Section 5, add a blue caveat footnote, and refresh the Section 5 wrapper.

Files changed:
- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`

What changed:
- Replaced the euro-area dual-y-axis Figure 15 generator with a two-panel shared-x bar chart so aggregate GDP contributions and own-sector value added use the same sector ordering visibly.
- Made the figure generator robust to both legacy and current benchmark CSV column names.
- Removed the explicit household/intermediate decomposition language from Section 5.
- Replaced it with a softer interpretive explanation: service losses read mainly as demand redirection, while upstream tradable losses read more like input-cost pressure.
- Added a blue footnote stating that this channel reading still needs formal checking.
- Updated the euro-area paragraph and Figure 15 caption to match the new stacked-panel figure.

Verification:
- Regenerated `Fig_EA_Sectoral_Heatmap_USCN.png` and synced it into `Tariffs_ECB/0_clean/figures/`.
- Compiled `master_supporting_docs/Tariffs_ECB/0_clean/0_section_5_only.tex` successfully with `latexmk -pdf -interaction=nonstopmode -halt-on-error 0_section_5_only.tex`.
- Compiled `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex` successfully with `latexmk -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex`.

Notes:
- The wrapper still has the known non-clickable imported upstream labels by construction.
- The full build still emits the manuscript's existing hyperref-style footnote destination warnings (`Hfootnote.*`), but no compile failure occurred.
