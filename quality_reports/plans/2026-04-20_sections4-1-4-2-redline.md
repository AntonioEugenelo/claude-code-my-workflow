# Plan: Sections 4.1/4.2 Redline Fix Pass

**Date:** 2026-04-20
**Status:** ACTIVE

## Objective

Implement the pending Section 4.1 and 4.2 manuscript fixes in the active Tariffs_ECB paper, align the elasticity and tariff-shock definitions with the MCMS source of truth, regenerate the benchmark figure if needed, and compile a full-paper redline PDF for inspection.

## Scope

Primary manuscript target:

- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`

Likely supporting files:

- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/figures/Fig_Benchmark_Combined.png` via regeneration
- `quality_reports/specs/2026-04-20_sections4-1-4-2-redline.md`
- `quality_reports/session_logs/2026-04-20_sections4-1-4-2-redline.md`

Reference evidence:

- `quality_reports/specs/2026-04-18_action-point-response-memo.md`
- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_1*.csv`
- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_2_Cumul_IO_Decomposition_TimeSeries.csv`
- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_4_UnitElast_vs_HighElast_TimeSeries.csv`
- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_17_DCP_PCP_FullDCP_TimeSeries.csv`
- `master_supporting_docs/MCMS/a1_calibration.m`

## Planned Changes

1. Verify the current Section 4 text/captions against the action memo and MCMS export definitions.
2. Edit Section 4.1 to rebalance the euro-area discussion, strengthen the household paragraph, and keep the new edits visibly red.
3. Edit Section 4.2 / robustness captions and paragraphs to fix the US-on-China-only experiment definition, fill IO and elasticity placeholders, and align the elasticity definition with the current `\delta=\mu=1` export.
4. If safe against the current dirty MCMS worktree, patch the benchmark-figure generator to simplify the title/legend stack and darken the reverse-shock line, then regenerate the active benchmark figure.
5. Compile the full paper to a fresh verification directory and confirm the redlined changes are visible in the output PDF.
6. Run the available documentation/manuscript checks required by the repo workflow, then log the session.

## Verification

- Inspect the edited source to confirm the bilateral/unilateral wording is corrected and the elasticity definition is consistent.
- Regenerate `Fig_Benchmark_Combined.png` if `new_process.py` is edited.
- Rebuild `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex` in a fresh output directory.
- Confirm the output PDF exists and that the intended Section 4 edits appear in red.

## Assumptions

- The user wants a reviewable redline build now, not a cleaned final manuscript with color removed.
- “Yield back the full pdf compiled” means produce the compiled PDF on disk and report its path.
- It is acceptable to limit this pass to the active Section 4 source and the figure-generation route it directly cites, without expanding into unrelated theory-file cleanup.
