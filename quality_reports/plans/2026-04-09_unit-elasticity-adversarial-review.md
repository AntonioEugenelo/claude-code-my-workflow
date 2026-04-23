Status: IN PROGRESS

Goal
- Run a deep adversarial review on the unit-elasticity paper rewrite and its figure-generation pipeline, using external reviewer agents for all assessment passes.

Scope
- Active paper sources under `master_supporting_docs/Tariffs_ECB/0_clean/sections/`.
- Compiled paper target `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`.
- Figure/pipeline sources under `master_supporting_docs/MCMS/` that were changed for the unit-elasticity rewrite.

Review Mode
- Deep paper review per `docs/codex-workflows/review-routing.md`.
- Required lenses: proofreader, derivation, figure-consistency, theory, narrative.
- Threshold rule from user: theory and narrative must each be rated at least `90/100` by external reviewer agents before completion.
- No self-scoring; every assessment pass must come from spawned reviewer agents.

Execution Plan
1. Launch external reviewer agents for proofreader, derivation, figure-consistency, theory, and narrative.
2. Aggregate findings, prioritize by severity, and fix manuscript or pipeline issues.
3. Re-run verification commands after material fixes.
4. Launch fresh theory and narrative reviewer agents on the updated state.
5. Repeat fix/review loop until both theory and narrative reviewers report `>= 90`, or until the repo review-loop limit is reached.

Verification
- `SKIP_MATLAB_PREPROCESSING=1; python new_process.py`
- `python output_python/extra_charts/gen_section5_figs.py`
- `latexmk -pdf 0_main.tex`

Constraints
- Use the existing `_UnitElast` MAT files; do not rerun MATLAB IRFs.
- Preserve unrelated user edits.
- Stop and report if the same blocking verification issue fails twice for the same reason.
