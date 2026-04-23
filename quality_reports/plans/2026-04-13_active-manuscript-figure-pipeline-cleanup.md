Status: in progress

Task:
- Clean up unnecessary figure-generation files and consolidate all active paper-facing figure generation into `master_supporting_docs/MCMS/new_process.py`, treating the active paper text as the authority.

Scope:
- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/MCMS/output_python/extra_charts/gen_section5_figs.py`
- paper-facing figure assets under `master_supporting_docs/Tariffs_ECB/0_clean/figures/`
- any sync manifest or helper functions in MCMS that define which paper figures are copied into `Tariffs_ECB`

Core requirements:
- Use `0_main.tex` and the sections it includes to define the active figure set.
- Eliminate the separate Section 5 figure-generation script by moving that logic into `new_process.py`.
- Keep the current manuscript's figures and appendix tables working.
- Remove obsolete paper-facing figure artifacts and obsolete pipeline files when they are clearly outside the active manuscript manifest.
- Preserve unrelated dirty changes in nested repos.

Likely implementation approach:
- Build an explicit active figure manifest from the current paper sections.
- Inspect `new_process.py` to identify existing CSV extraction, plotting, sync, and cleanup hooks.
- Port the `gen_section5_figs.py` logic into `new_process.py` as local helpers driven by the same MAT/CSV inputs.
- Reduce the sync list to active figures only and add cleanup for stale paper-facing figure copies.
- Remove the retired Section 5 generator file if no longer needed.

Verification:
- run `new_process.py` to regenerate active figure outputs
- confirm the active figure files are present in `Tariffs_ECB/0_clean/figures/`
- compile `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`
- inspect the build log for blocking errors and spot-check the figure-bearing pages

Known assumptions and risks:
- “Unnecessary files” is interpreted narrowly as obsolete figure-pipeline scripts and paper-facing figure artifacts, not arbitrary historical manuscript source files.
- Some older figure assets may still be referenced by inactive sections; those references do not define the active pipeline.
- The nested repos are dirty, so deletions must avoid unrelated user-owned material.
