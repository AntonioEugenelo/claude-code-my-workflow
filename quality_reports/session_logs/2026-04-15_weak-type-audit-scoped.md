# Session Log: Scoped Weak-Type Audit

Date: 2026-04-15

## Scope

- `scripts/`
- `.claude/hooks/`
- `master_supporting_docs/MCMS` top-level `.m`/`.py`
- `master_supporting_docs/MCMS/functions/solve_fixed_point.m`
- `master_supporting_docs/MCMS/run_benchmark_irf_export.m`
- `master_supporting_docs/Tariffs_ECB/0_clean/run_horse_race_appendix.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/run_stacked_regressions.py`
- `guide/workflow-guide.qmd`
- `guide/custom.scss`

Excluded generated or out-of-scope files, including `.tex`, `.mod`, and mirrored `docs/*.html`.

## Method

- Inventory maintained source with `git ls-files`, `Get-ChildItem`, and targeted reads.
- Search for explicit weak markers (`dict`, `Dict`, JSON loads, dynamic structs, dynamic field access).
- Trace surrounding code to infer stronger contracts from actual keys, DataFrame columns, MATLAB struct fields, and function usage.
- No code edits performed.

## Main Findings

1. `master_supporting_docs/MCMS/new_process.py` is the dominant weak-typing hotspot.
   - 93 Python functions with no return annotations and 230 unannotated parameters in the scoped count.
   - Multiple stable payloads are represented as anonymous nested dicts: job specs, Dynare solution payloads, transmission block bundles, and figure payloads.

2. `master_supporting_docs/Tariffs_ECB/0_clean/run_horse_race_appendix.py` has decent surface annotations but still relies on schema-less nested dicts for all regression outputs and final results bundles.

3. Root automation uses generic `Dict`/`dict` where the shapes are fixed.
   - `scripts/quality_score.py`
   - `scripts/review_plan.py`
   - several `.claude/hooks/*.py` state/cache helpers

4. MATLAB weak typing is concentrated in scenario/config structs and dynamic field access.
   - `a0_launch.m`, `a0_rerun_DCP.m`, `run_benchmark_irf_export.m`
   - `a2_preprocessing.m`

5. `guide/workflow-guide.qmd` and `guide/custom.scss` are not meaningful weak-type hotspots.
   - The only relevant “typing” issue there is schema duplication in Quarto frontmatter / inline CSS, not code-level type weakness.

## Verification Notes

- Confirmed the scope matches the user’s narrowed file list.
- Confirmed no code changes were made during the audit.
