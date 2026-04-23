# Plan: Final EA Subsection Rewrite

**Status:** ACTIVE
**Date:** 2026-04-20
**Branch:** `codex-ecb-tariffs`

## Objective

Rewrite the final euro-area subsection in Section 5 so it is more coherent with the preceding own-versus-cross discussion, keep the new subsection visibly red against the current baseline, tighten the prose so every numerical claim is tied to a direct object, and extend the benchmark IRF export so the compact MAT can carry the sectoral bilateral trade object needed for a cleaner follow-up.

## Scope

- Primary source: `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- Supporting evidence:
  - `master_supporting_docs/MCMS/output_matlab/irf_Het_DCP_Baseline.mat`
  - `master_supporting_docs/MCMS/output_matlab/calib.mat`
  - `master_supporting_docs/MCMS/dynare_files/b0_main/Output/b0_main_results.mat`
  - `master_supporting_docs/MCMS/dynare_files/b1_declare_var.mod`
  - `master_supporting_docs/MCMS/dynare_files/b4_declare_model.mod`
  - `master_supporting_docs/MCMS/new_process.py`
- Verification targets:
  - `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`
  - `master_supporting_docs/MCMS/output_matlab/irf_Het_DCP_Baseline.mat`
- Tracking file: `quality_reports/session_logs/2026-04-20_final-ea-subsection-rewrite.md`

## Assumptions

1. The active target is the subsection `Third-Country Gross Incidence in the Euro Area` in `56_sectoral_channels.tex`.
2. The existing figure set remains unchanged; this pass is a prose-only rewrite unless a later follow-up asks for new export tables.
3. The compact benchmark IRF MAT and the full Dynare results MAT are different evidence layers and must not be conflated.
4. Import/export language must stay careful about the underlying object and avoid overclaiming identification.

## Planned Steps

1. Pull the exact EA sector rankings and trade-response numbers from direct IRFs and the repo calibration objects.
2. Rewrite the subsection so it:
   - keeps the own-sector versus aggregate wedge visible,
   - distinguishes exact accounting claims from interpretive claims,
   - uses import-side language only where the underlying object supports it,
   - avoids mixed-object shortcuts.
3. Audit the MAT / Dynare paths for sectoral imports and state whether:
   - they already exist in the compact benchmark IRF export,
   - they can be reconstructed from the full Dynare results file without rerunning Dynare,
   - or they require a fresh rerun / export extension.
4. Turn the revised EA subsection text red, matching the active manuscript redline convention without broadening the red markup to unrelated Section 5 text.
5. Add the sectoral bilateral trade object needed for follow-up extraction to the model/export path:
   - declare the new trade variable family in Dynare,
   - define it in the model block,
   - include it in the benchmark `stoch_simul` export list.
6. Rerun the benchmark IRF export so the compact MAT reflects the new export list.
7. Compile the manuscript to a fresh verification directory.
8. Record the edit and verification result in the session log.

## Verification

- Source audit of the revised subsection against direct IRFs and calibration weights
- Local code/model audit of sectoral-import recoverability
- Re-run `run_benchmark_irf_export.m` and confirm the new sectoral trade IRFs are present in `irf_Het_DCP_Baseline.mat`
- `latexmk -pdf -outdir=build_verify_codex -interaction=nonstopmode -halt-on-error 0_main.tex`

## Likely Files To Change

- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `master_supporting_docs/MCMS/dynare_files/b0_main.mod`
- `master_supporting_docs/MCMS/dynare_files/b1_declare_var.mod`
- `master_supporting_docs/MCMS/dynare_files/b4_declare_model.mod`
- `quality_reports/plans/2026-04-20_final-ea-subsection-rewrite.md`
- `quality_reports/session_logs/2026-04-20_final-ea-subsection-rewrite.md`
