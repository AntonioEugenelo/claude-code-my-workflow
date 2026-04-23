# 2026-04-17 DCP Footnote And Shock Timing

## Scope

- Checked the DCP literature footnote references in `master_supporting_docs/Tariffs_ECB/0_clean/sections/12_related_literature.tex`.
- Removed the final footnote sentence requested by the user.
- Verified the implemented tariff-shock process in `master_supporting_docs/MCMS`.
- Updated Section 4.1 in `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex` to match the model.

## Reference Check

- Footnote 1 cites `Gopinath2020`, `mukhin2023`, and `devereux2003`.
- Corresponding bibliography entries are present in `master_supporting_docs/Tariffs_ECB/0_clean/bibliography.bib`.
- No citation-key mismatch was found.

## Model Check

- `master_supporting_docs/MCMS/dynare_files/b4_declare_model.mod:668` defines tariffs as an AR(1) process.
- `master_supporting_docs/MCMS/a1_calibration.m:704-710` sets tariff persistence to `0.96` when `persistence == 1`.
- `master_supporting_docs/MCMS/mcms_runner_support.m:88` uses `config.persistence = 1` in the default IRF configuration.
- `master_supporting_docs/MCMS/README.md:18` also documents the tariff shock as AR(1).
- Conclusion: the model does not implement a shock that is flat for 12 quarters and then declines. The manuscript was updated to state the implemented persistent AR(1) process instead.

## Edits Made

- Removed the final sentence from the DCP literature footnote in `sections/12_related_literature.tex`.
- Added an accurate benchmark-shock description to `sections/55a_benchmark_and_robustness.tex`: AR(1), `rho_tau = 0.96`, gradual decay over the 12-quarter plotting horizon.

## Verification

- Fresh build run from `master_supporting_docs/Tariffs_ECB/0_clean`:
  - `pdflatex -interaction=nonstopmode -halt-on-error -jobname=0_main_verify_20260417 -output-directory=build_verify_20260417 0_main.tex`
  - `bibtex build_verify_20260417/0_main_verify_20260417`
  - `pdflatex ...`
  - `pdflatex ...`
  - `pdflatex ...`
- Verified PDF: `master_supporting_docs/Tariffs_ECB/0_clean/build_verify_20260417/0_main_verify_20260417.pdf`
- Non-blocking warnings remaining:
  - TinyTeX duplicate fontmap warnings
  - `microtype` footnote patch warning
  - two `Hfootnote` destination warnings
