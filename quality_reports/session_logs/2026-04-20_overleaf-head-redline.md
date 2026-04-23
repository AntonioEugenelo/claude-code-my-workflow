# 2026-04-20 Overleaf-Head Redline Build

## Objective

Generate a manuscript PDF in which highlights reflect only the current local diff against the current Overleaf head for `master_supporting_docs/Tariffs_ECB`.

## Baseline

- `scripts/sync-overleaf.sh status` reported:
  - Local: `adcd6719e76df9e0072c7f3f502905c4e9e61ea4`
  - GitHub: `adcd6719e76df9e0072c7f3f502905c4e9e61ea4`
  - Overleaf: `adcd6719e76df9e0072c7f3f502905c4e9e61ea4`
- Therefore the correct comparison baseline is the current `HEAD` of the nested `Tariffs_ECB` repo.

## Implementation

- Added helper script:
  - `scripts/build_overleaf_head_redline.py`
- The script:
  1. copies the current `0_clean/` tree into a timestamped temporary directory under `master_supporting_docs/Tariffs_ECB/`
  2. strips pre-existing manual red/blue markup while preserving line layout
  3. computes `git diff --unified=0 HEAD` for `0_clean/*.tex` and `0_clean/sections/*.tex`
  4. wraps only current-side changed line ranges in red
  5. compiles the temporary tree with `latexmk`

## Output

- PDF:
  - `master_supporting_docs/Tariffs_ECB/build_redline_overleaf_head_20260420_124023/src/build/0_main.pdf`

## Final In-Place Update

- Applied the Overleaf-head-only highlighting back onto the live `0_clean` manuscript inputs instead of relying on a temporary folder for delivery.
- Recompiled the live target:
  - `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`
- Final live PDF:
  - `master_supporting_docs/Tariffs_ECB/0_clean/0_main.pdf`
- Removed old build folders created during the redline attempts:
  - `build_redline_overleaf_head/`
  - `build_redline_overleaf_head_20260420_123915/`
  - `build_redline_overleaf_head_20260420_124023/`
  - `0_clean/build_redline_20260420/`
  - `0_clean/__pycache__/`

## Verification

- Confirmed the temporary `12_related_literature.tex` no longer contains the historical unchanged red footnote markup from `HEAD`.
- Confirmed the temporary `43_calibration.tex` no longer contains the unchanged red dagger markup from `HEAD`.
- Confirmed the temporary `0_main.tex` still comments out `\input{sections/a_appendix_horse_race}`.
- Tightened the live manuscript markup so unchanged paragraphs are no longer wrapped in block-level red; the redline now uses inline `\textcolor{red}{...}` for phrase-level changes in the compiled `0_clean` inputs, with full red reserved for genuinely new sentences.
- Removed the unit-elasticity footnote in Section 4 (`The current Figure~\ref{fig:robust_elast} export is generated from the MCMS unit-elasticity configuration`).
- Reset the title page, introduction baseline text, and the `Tariff revenue and its disposition` paragraph to black in the live manuscript so they are no longer treated as current redline changes.
- Removed non-essential Tariffs_ECB files outside the live `0_main` path:
  - horse-race helper `.py` files
  - standalone subset drivers `0_section_5_only.tex` and `0_sections_4_5_only.tex`
  - standalone subset PDFs
  - unused legacy section and appendix `.tex` files outside the `0_main` include graph
  - generated horse-race table `.tex` files
  - remaining `build_verify` PDF artifact
- Compile command:
  - `python scripts/build_overleaf_head_redline.py`
- Final compile completed successfully.
- Live in-place compile completed successfully with the same pre-existing unresolved-reference warnings only.

## Residual Limitations

- The redline highlights changed current-side content blocks relative to `HEAD`.
- Pure deletions appear as absence rather than as struck-out text because `latexdiff` is not available in the local TinyTeX environment.
- Remaining LaTeX warnings are pre-existing:
  - undefined refs: `sec:analytical_insights`, `eq:general_model_budget_constraint`, `eq:bilateral_nominal_exchange_rate_MU`
  - multiply defined labels: `eq:general_model_price_setting_foreign`, `eq:budget_constraint`, `eq:calvo_inflation_dynamics_2`
