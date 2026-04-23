## Objective

Audit all figures used in the live Section 4 and Section 5 manuscript state, checking whether each figure matches its caption and whether the surrounding paper text describes the displayed object correctly.

## Scope

- Use the last synced paper commit as the audit baseline because the working tree currently contains unmerged local changes in live manuscript files.
- Inventory all figures included by the synced `0_main.tex` for:
  - `0_clean/sections/55a_benchmark_and_robustness.tex`
  - `0_clean/sections/56_sectoral_channels.tex`
- Trace each figure back to the MCMS generator, exported CSVs, and model objects where applicable.
- Compare, for each figure:
  - displayed horizon / transformation / normalization
  - countries / sectors / scenarios shown
  - variable definitions in the caption
  - claims made in the adjacent manuscript text
- Produce a findings-first audit report with exact file references and explicit notes on residual uncertainty where code or captions are ambiguous.

## Likely Files To Read

- `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/MCMS/a2_preprocessing.m`
- `master_supporting_docs/MCMS/dynare_files/b4_declare_model.mod`
- exported CSVs under `master_supporting_docs/MCMS/output_python/extra_charts/`

## Assumptions

- “As they currently are in the paper” refers to the last synced paper state on Overleaf / HEAD, not the unresolved local merge-conflict worktree.
- The audit is read-only unless the user asks for fixes after reviewing the findings.
- Existing exported figures and CSVs in MCMS are the source of truth for what the figure code currently displays.

## Verification

- Confirm the paper baseline commit with `sync-overleaf.sh status`.
- Confirm which section files are live from `0_main.tex`.
- For each figure, cross-check the paper caption against the MCMS generator and, where needed, the exported CSV values.
- If a claim depends on a compiled artifact rather than source alone, inspect the current image asset directly.
