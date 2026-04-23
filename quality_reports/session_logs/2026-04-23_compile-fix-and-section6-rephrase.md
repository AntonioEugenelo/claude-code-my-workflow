## Summary

Fixed the active `0_clean` compile blocker and rephrased the Section 6 US/China propagation subsection in mechanism language.

## Changes Made

- In `master_supporting_docs/Tariffs_ECB/0_clean/bibliography.bib`:
  - removed duplicate-key collisions by renaming the unused duplicate entries for `AmitiReddingWeinstein2019`, `Armington1969`, `acemoglu2012`, `baqaee24`, and `pasten2020`
  - normalized the cited DCP entry `GopinathBozCasasDiezGourinchasPlagborgMoller2020` to `Plagborg-Moeller` so BibTeX no longer generates the crashing `\textsc{Plagborg-M{\o}ller}` line in `0_main.bbl`
- In `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`:
  - renamed `Cross-Sector Propagation in the US and China` to `Domestic Propagation Beyond the Tariffed Sector`
  - rewrote the subsection prose to describe the mechanism in words rather than through the old `g^{\mathrm{own}}` / `g^{\mathrm{cross}}` shorthand
- Cleared corrupted generated write files (`0_main.out`, `0_main.lof`, `0_main.toc`) after a stale truncated bookmark entry caused a non-source `Runaway argument` failure during the first rebuild pass

## Verification

- Ran `latexmk -pdf -interaction=nonstopmode -halt-on-error 0_main.tex` in `master_supporting_docs/Tariffs_ECB/0_clean`
- Result: success, with rebuilt output at `master_supporting_docs/Tariffs_ECB/0_clean/0_main.pdf`

## Residual Warnings

- The build still reports pre-existing undefined references:
  - `sec:robustness`
  - `sec:benchmark`
  - `sec:analytical_insights`
  - `eq:general_model_budget_constraint`
  - `eq:bilateral_nominal_exchange_rate_MU`
  - `sec:invoicing`
  - plus a few related repeats from the appendix
- The build still reports pre-existing multiply-defined labels:
  - `eq:general_model_price_setting_foreign`
  - `eq:budget_constraint`
  - `eq:calvo_inflation_dynamics_2`
- `latexmk` also reports a non-blocking SyncTeX file-lock warning for `0_main.synctex.gz`
