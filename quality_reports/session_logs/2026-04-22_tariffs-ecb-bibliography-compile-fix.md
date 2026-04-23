## Task

Restore a successful `0_main` build for `master_supporting_docs/Tariffs_ECB/0_clean`.

## Blocking Issues Found

- Raw Unicode / mojibake in manuscript text:
  - `0_clean/sections/11_introduction.tex`
  - `0_clean/sections/22_households.tex`
  - `0_clean/sections/26_sectoral_tariffs.tex`
  - `0_clean/sections/56_sectoral_channels.tex` comment
  - `0_clean/sections/60_Conclusions.tex`
  - `0_clean/sections/a_appendix.tex`
- Duplicate BibTeX keys in `0_clean/bibliography.bib`:
  - `AmitiReddingWeinstein2019`
  - `Armington1969`
  - `baqaee24`
  - `acemoglu2012`
  - `pasten2020`
- Bibliography compile failure from `Plagborg-M{\o}ller` in the cited `GopinathBozCasasDiezGourinchasPlagborgMoller2020` entry.

## Changes Made

- Normalized the malformed introduction sentence to LaTeX-safe ASCII.
- Replaced raw Greek `ρ`, `τ` in `26_sectoral_tariffs.tex` with `\rho`, `\tau`.
- Replaced a small set of compile-problematic Unicode punctuation in live `0_main` section files with ASCII-safe forms.
- Removed only the redundant duplicate BibTeX entries after their first occurrence.
- Normalized `Plagborg-M{\o}ller` to `Plagborg-Moeller` in the cited DCP bibliography entry to avoid the `pdflatex` failure in `0_main.bbl`.
- Repaired an intermediate mojibake side effect in `bibliography.bib` and verified the final diff only contains the intended duplicate deletions plus the `Moeller` normalization.

## Verification

Successful build command:

```powershell
latexmk -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex
```

Successful output:

- `master_supporting_docs/Tariffs_ECB/0_clean/build_verify/0_main.pdf`

Quick review pass:

- `git -C master_supporting_docs/Tariffs_ECB diff --check -- 0_clean/sections/11_introduction.tex 0_clean/sections/22_households.tex 0_clean/sections/26_sectoral_tariffs.tex 0_clean/sections/56_sectoral_channels.tex 0_clean/sections/60_Conclusions.tex 0_clean/sections/a_appendix.tex 0_clean/bibliography.bib`

## Residual Warnings

- Pre-existing undefined references remain:
  - `sec:benchmark`
  - `sec:analytical_insights`
  - `eq:general_model_budget_constraint`
  - `eq:bilateral_nominal_exchange_rate_MU`
- Pre-existing multiply-defined labels remain:
  - `eq:general_model_price_setting_foreign`
  - `eq:budget_constraint`
  - `eq:calvo_inflation_dynamics_2`
- Environment / toolchain warnings remain:
  - TinyTeX fontmap duplicate warnings
  - `microtype` footnote patch warning
  - `latexmk` Perl `quotemeta` warnings on this Windows setup
