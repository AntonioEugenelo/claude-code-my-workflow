Status: IN PROGRESS

Goal
- Compute the Section 5 bilateral-trade horse-race regression table under the unit-elasticity benchmark and add it to the manuscript through the existing MCMS/Tariffs_ECB pipeline.

Scope
- `master_supporting_docs/MCMS/output_python/extra_charts/`
- `master_supporting_docs/MCMS/new_process.py` if sync logic needs extension
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- Any generated CSV/LaTeX table artifact needed for reproducibility

Plan
1. Confirm the benchmark cross-section CSV contains the required predictors and dependent variables for the China sectoral horse-race table.
2. Add a reproducible computation step in the Python side of the pipeline that outputs the regression table from the existing unit-elasticity benchmark data.
3. Insert the resulting table and supporting narrative into the active paper source.
4. Re-run the relevant Python generator(s) and rebuild the paper PDF.

Constraints
- Use the existing `_UnitElast` benchmark files only; do not rerun MATLAB IRFs.
- Keep the computation tied to the pipeline rather than hand-entering numbers.
