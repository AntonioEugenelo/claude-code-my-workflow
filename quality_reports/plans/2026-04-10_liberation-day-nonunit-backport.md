Status: in progress

Task: Backport non-unit-elasticity changes from the current ECB tariffs workspace into the `liberation-day-scenarios` line, excluding any Armington-1 / unit-elasticity logic.

Scope:
- `master_supporting_docs/MCMS/`
- potentially `master_supporting_docs/Tariffs_ECB/` if paper-facing layout or figure references also changed

Likely files:
- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/MCMS/output_python/extra_charts/gen_section5_figs.py`
- figure-output directories under `master_supporting_docs/MCMS/output_python/`
- paper-facing `.tex` or `figures/` files only if they are tied to non-unit layout updates

Assumptions:
- The target branch for the model-side backport is `master_supporting_docs/MCMS` branch `liberation-day-scenarios`.
- "Do not involve the unit elasticity" excludes Armington-1 comparisons, `_UnitElast` inputs, figure labels/captions/narrative for the elasticity-one benchmark, and any manuscript claims tied to that benchmark.
- Layout/UI improvements that are branch-agnostic, such as revised figure arrangement for benchmark figures, should be carried over.

Verification:
- inspect branch diffs to identify candidate changes
- apply only selected non-unit changes onto the target branch
- run the relevant Python figure-generation command(s) on the target branch
- compile the relevant paper target if paper-facing assets are updated

Open questions to resolve from code:
- Whether the figure-5 layout change lives in the model pipeline, paper source, or both
- Whether the current dirty unit-elasticity work contains any non-committed general improvements worth backporting
