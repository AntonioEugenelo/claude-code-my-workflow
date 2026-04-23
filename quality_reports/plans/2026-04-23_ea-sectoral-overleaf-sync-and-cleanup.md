## Plan: EA Sectoral Overleaf Sync And Cleanup

**Date:** 2026-04-23
**Status:** IN PROGRESS

## Objective

Pull the full `Tariffs_ECB` manuscript from Overleaf, add an EA bilateral sectoral exports/imports figure for the sectoral-dimension discussion, use that figure to complete the EA subsection in Section 5, and archive unused manuscript sections/assets into an `old/` directory without disturbing active sources.

## Scope

- Sync `master_supporting_docs/Tariffs_ECB` from Overleaf and reconcile any local derived-file conflicts needed to complete the pull.
- Audit the active manuscript structure and current Section 5 / Section 6 sectoral-dimension material after the pull.
- Confirm the available MCMS bilateral trade-margin series and extend the figure-generation pipeline if needed.
- Generate an EA-focused bilateral sectoral exports/imports figure from source code.
- Update the active manuscript subsection and captions/prose to match the new figure and the underlying trade accounting.
- Move unused sections and unused figure assets into an `old/` directory, preserving active build inputs.
- Verify by regenerating the relevant figures and compiling the manuscript or a scoped verification target.

## Constraints

- Do not revert unrelated local changes in either nested repo.
- Treat source `.tex`, `.py`, `.m`, and model files as authoritative; copied figures and PDFs are derived.
- Any local file moved to clear an Overleaf pull conflict must be backed up rather than deleted.
- "Unused" will mean not included by the active `0_main.tex` build and not referenced by the active figure/text pipeline after the post-pull audit.

## Likely Files

- `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55b_sectoral_transmission_decomposition.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/a_appendix_horse_race.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/figures/*`
- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_6_Baseline_Bars_CrossSection.csv`
- `quality_reports/session_logs/2026-04-23_ea-sectoral-overleaf-sync-and-cleanup.md`

## Work Plan

1. Complete the Overleaf pull safely, backing up any local untracked derived files that block the merge.
2. Audit the pulled manuscript structure to identify the active Section 5 EA subsection and any unused sections/assets.
3. Inspect the current MCMS bilateral export/import series and determine the exact EA figure specification that best matches the subsection’s accounting needs.
4. Implement or refresh the figure-generation code and regenerate the EA bilateral sectoral exports/imports figure.
5. Update the active EA subsection prose/caption cross-references to use the new figure and close the sectoral-dimension argument.
6. Move unused sections/assets into an `old/` directory, preserving a clean mapping between active files and the compiled manuscript.
7. Compile a verification target and record any remaining warnings or blockers.

## Verification

- Successful Overleaf pull into `master_supporting_docs/Tariffs_ECB`.
- Direct inspection of active includes from `0_main.tex`.
- Regenerated EA bilateral sectoral trade-margin figure from source code.
- Successful compile of the main manuscript or a scoped verification wrapper if the full build is blocked by unrelated pre-existing assets.

## Assumptions

- The requested EA figure should decompose the EA trade response along bilateral partner and sector dimensions using the existing `exp_1_l_i_*` and `imp_1_l_i_*` IRFs already present in the benchmark export.
- The active section to update is the main-text sectoral-dimension discussion, even if related backup or preserved variants still exist elsewhere.
- Archiving unused files into `old/` should preserve them verbatim rather than editing their contents.
