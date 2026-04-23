Task
- Deep cleanup of `master_supporting_docs/Tariffs_ECB/0_clean/`.

Plan
- `quality_reports/plans/2026-04-23_0-clean-deep-cleanup.md`

Changes
- Removed dead root-level wrapper files:
  - `0_section_5_only.tex`
  - `0_sections_4_5_only.tex`
- Removed stale wrapper build artifacts and orphan `pdflatex*.fls` files from the root of `0_clean`.
- Removed the stale verification directory:
  - `build_verify_20260420_robustness_inflation/`
- Removed inactive appendix/source files that were outside the active `0_main.tex` closure:
  - `sections/a_appendix_dynamics.tex`
  - `sections/a_appendix_liberation_day.tex`
  - `sections/a_appendix_sectoral_targeting.tex`
- Removed unused calibration heatmap assets that were only referenced in commented-out lines:
  - `figures/alpha_heatmap.png`
  - `figures/calvo_heatmap.png`
  - `figures/consumption_shares_heatmap.png`
  - `figures/omega_foreign_heatmap.png`
  - `figures/omega_inside_EA_heatmap.png`
- Cleaned dead commented references from:
  - `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`
  - `master_supporting_docs/Tariffs_ECB/0_clean/sections/43_calibration.tex`

Verification-related fixes
- Replaced a Unicode minus / mojibake issue in `sections/11_introduction.tex` so `pdflatex` would run.
- Deduplicated repeated BibTeX keys in `0_clean/bibliography.bib`.
- Normalized one problematic author spelling (`Plagborg-M{\o}ller` -> `Plagborg-Moeller`) to avoid a `.bbl` compile failure under the current BibTeX style.

Verification
- Compiled in place from `master_supporting_docs/Tariffs_ECB/0_clean/` with:
  - `latexmk -pdf -interaction=nonstopmode -halt-on-error 0_main.tex`
- Final rerun completed with:
  - `Latexmk: Nothing to do for '0_main.tex'.`
  - `Latexmk: All targets (0_main.pdf) are up-to-date`
- After verification, cleaned remaining `0_main` aux files so the `0_clean` root now keeps only:
  - `0_main.tex`
  - `0_main.pdf`
  - source/support directories and non-derived support files

Residual notes
- The main compile still reports pre-existing unresolved references / multiply defined labels in the manuscript.
- `sections/56_sectoral_channels.tex` already had active unstaged edits before this cleanup and remains modified.
