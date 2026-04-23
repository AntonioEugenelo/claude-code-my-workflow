Status: in progress

Task:
- Rebuild the horse-race appendix on the elasticity-two benchmark, rerun the computations from source, rewrite the appendix, and iterate external theory/narrative review until both reviewer agents score at least 90.

Scope:
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/a_appendix_horse_race.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/run_stacked_regressions.py`
- model-side preprocessing / regression helpers in `master_supporting_docs/MCMS/`
- generated tables or CSV outputs used by the appendix

Core requirements:
- Use the elasticity-two benchmark only.
- Recompute all appendix numbers from source code, not by hand.
- Clarify whether bilateral trade share or IO intensity is the primary predictor, and distinguish direct exposure from amplification margins.
- Keep the appendix consistent with the earlier `2026-04-09_section5-finding3-correction`.
- Run theory and narrative reviewer agents after substantive fixes, and continue until both score >= 90.
- For each correction round, provide a complaint table with issue, reviewer, and fix.

Likely implementation approach:
- Use a clean elasticity-two MCMS worktree or checkout to avoid contamination from the dirty unit-elasticity branch.
- Replace the ad hoc Excel-based regression script with a reproducible pipeline keyed off current benchmark outputs / calibration objects.
- Export appendix-ready regression results to a machine-readable artifact.
- Rewrite the appendix around those results and compile the paper.

Verification:
- rerun the regression pipeline on elasticity-two inputs
- inspect generated tables/CSV outputs
- compile `0_main.tex` with a scratch jobname
- run reviewer agents; fix issues; recompile; rerun reviewers until threshold is met

Known risks:
- current paper repo has unrelated dirty files; do not overwrite unrelated user edits
- current MCMS repo is on a dirty unit-elasticity branch, so analysis must be isolated from that state
