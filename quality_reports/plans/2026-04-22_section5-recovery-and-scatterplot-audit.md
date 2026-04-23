## Plan: Section 5 Recovery And Scatterplot Audit

**Date:** 2026-04-22
**Status:** ACTIVE

### Objective

1. Recover the pre-change Section 5 version that still contained the subsection on determinants of sectoral impact.
2. Save that recovered Section 5 into a separate standalone `.tex` file without changing the active manuscript source.
3. Trace the scatterplot-grid figures used for Section 5 back to the code and model objects that generate them.
4. Document every plotted variable and parameter: code name, source file, and economic meaning.
5. Regenerate the relevant figures from source and compare the outputs against the current tracked figures.

### Scope

- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- recovered standalone Section 5 `.tex` file under `master_supporting_docs/Tariffs_ECB/0_clean/sections/`
- scatterplot-grid generation code under `master_supporting_docs/Tariffs_ECB/`
- verification artifacts and this plan

### Assumptions

- "Before a recent change" refers to the latest git-tracked Section 5 version that still included a subsection explicitly focused on determinants of sectoral impact.
- "Scatterplot grids" refers at minimum to the structural scatter-grid figures currently tracked for the US, China, and the EA in `0_clean/figures/`.
- The user wants a recovery plus an audit and verification report, not an in-place rewrite of the active Section 5 source.

### Planned Steps

1. Inspect the git history of `56_sectoral_channels.tex` to identify the commit/version that still contains the determinants subsection.
2. Recover that full Section 5 source into a new standalone `.tex` file with a descriptive archival filename.
3. Locate the scripts and intermediate objects that generate the scatterplot-grid figures.
4. Map each plotted variable/parameter to the model or post-processing code, and record what it means economically.
5. Re-run the figure-generation pipeline for the scatterplot grids.
6. Compare regenerated outputs to the currently tracked figures and record any differences.
7. Report the recovered file path, variable/parameter mapping, regeneration status, and discrepancies.

### Verification

- `git log --follow` / `git show` confirms the recovered source matches the intended historical version.
- The recovered `.tex` file is present on disk and remains separate from the active manuscript include chain.
- The relevant figure-generation command(s) run successfully from source.
- Regenerated figure files are compared against the current tracked outputs using file diffs, hashes, timestamps, or image comparison as appropriate.

### Likely Files To Change

- `quality_reports/plans/2026-04-22_section5-recovery-and-scatterplot-audit.md`
- recovered standalone `.tex` file under `master_supporting_docs/Tariffs_ECB/0_clean/sections/`
- `quality_reports/session_logs/2026-04-22_section5-recovery-and-scatterplot-audit.md` if the task expands enough to warrant a full session record
- regenerated figure outputs if the source pipeline writes into the tracked `0_clean/figures/` directory
