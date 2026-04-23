## Plan: Overleaf-Head Redline Rebuild

**Date:** 2026-04-20  
**Status:** ACTIVE

### Objective

Build a manuscript PDF in which highlighted changes reflect only the current local diff against the current Overleaf head commit for `master_supporting_docs/Tariffs_ECB`.

### Context

- `scripts/sync-overleaf.sh status` reports `Local`, `GitHub`, and `Overleaf` all at commit `adcd6719e76df9e0072c7f3f502905c4e9e61ea4`.
- The working tree under `master_supporting_docs/Tariffs_ECB` contains uncommitted manuscript edits and figure updates.
- The source tree already contains some older manual `\textcolor{red}{...}` markup that is present in `HEAD`, so compiling the current working tree directly does not yield a clean Overleaf-vs-local redline.
- `latexdiff` is not available locally and cannot be installed via the current TinyTeX setup.

### Planned Steps

1. Build a temporary copy of `0_clean/` from the current working tree.
2. Strip pre-existing manual red markup from the temporary `.tex` sources so unchanged historical red text does not survive into the redline.
3. Compute the current diff against `HEAD` for the active `0_main.tex` source tree and wrap only the changed current-side line ranges in red.
4. Compile the temporary redline target and verify the output opens cleanly.
5. Record the output path and residual limitations in a session log.

### Verification

- Confirm Overleaf/head sync status before building.
- Verify the generated temporary tree compiles with `latexmk`.
- Scan the temporary sources to ensure unchanged historical red markup from `HEAD` is removed.
- Confirm the resulting PDF is newer than the previous redline build artifact.

### Known Limitation

This redline method will highlight changed current-side content blocks. Pure deletions relative to `HEAD` will appear as absence rather than as struck-out text unless a full `latexdiff` workflow becomes available.
