# Plan: Section 5 Caption Slimming and Pedagogical Review

**Status:** ACTIVE
**Branch:** `codex-ecb-tariffs`
**Scope:** `master_supporting_docs/MCMS/new_process.py`, `master_supporting_docs/Tariffs_ECB/0_clean/sections/*.tex`

## Objective

Tighten the captions for the active Section 4/5 figures, enlarge the spillover-matrix typography, normalize Figure 9 to the ECB blue/gold palette, then run a read-only pedagogical review of Section 5 and fix any material communication issues.

## Files Expected

- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `quality_reports/session_logs/2026-04-13_section5-caption-pedagogy-pass.md`
- optional review artifact in `quality_reports/reviews/`

## Execution Order

1. Patch `new_process.py` for larger spillover-matrix text and ECB blue/gold monetary-policy colors.
2. Trim the active captions in Sections 4 and 5, keeping only object, units, panels, and the minimal interpretation note where needed.
3. Regenerate the active figures from `new_process.py`.
4. Rebuild `0_main.tex` using the clean `build_verify` outdir path.
5. Run a read-only Section 5 pedagogical review with the `narrative-reviewer` agent.
6. Apply any material fixes, then recompile and close the log.

## Non-Negotiables

- Keep reviewer agents read-only.
- Do not touch Overleaf.
- Do not change the quantitative claims unless the review reveals a real communication problem.
