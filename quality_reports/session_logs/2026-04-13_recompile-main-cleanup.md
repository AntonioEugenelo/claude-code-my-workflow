# Recompile main and cleanup

Date: 2026-04-13

## Actions

- Forced a fresh LaTeX rebuild with `latexmk -g -pdf -interaction=nonstopmode -halt-on-error -outdir=build_verify 0_main.tex` in `master_supporting_docs/Tariffs_ECB/0_clean`.
- Copied the verified output to `master_supporting_docs/Tariffs_ECB/0_clean/0_main.pdf`.
- Removed the temporary `master_supporting_docs/Tariffs_ECB/0_clean/build_verify/` directory after the promoted PDF was in place.
- Removed the unused legacy figure `master_supporting_docs/Tariffs_ECB/0_clean/figures/Fig_SectoralSpillover_Matrix.png`, which is not referenced by the manuscript.

## Verification

- `0_main.pdf` refreshed successfully at 2026-04-13 23:44 local time.
- `git -C master_supporting_docs/Tariffs_ECB status --short -- 0_clean/0_main.pdf 0_clean/build_verify 0_clean/figures/Fig_SectoralSpillover_Matrix.png 0_clean/sections/55a_benchmark_and_robustness.tex 0_clean/sections/56_sectoral_channels.tex` shows only the intentional section source edits; the temporary build directory and unused matrix figure are gone.
