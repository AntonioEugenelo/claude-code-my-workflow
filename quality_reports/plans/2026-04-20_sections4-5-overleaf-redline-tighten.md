## Plan: Sections 4 And 5 Overleaf Redline Tighten

**Date:** 2026-04-20  
**Status:** ACTIVE

### Objective

Update the live `0_main` source so that, in Sections 4 and 5 only, red text marks only the differences from the synced Overleaf baseline.

### Scope

- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`

### Planned Steps

1. Compare the live Section 4 and 5 sources against `HEAD`/Overleaf and identify any changed text that is still black, plus any red text that is not an actual delta.
2. Patch the two section files in place so only the actual textual deltas remain red.
3. Recompile `0_main.tex` and verify the PDF.

### Verification

- `latexmk -pdf -interaction=nonstopmode -file-line-error 0_main.tex`

### Known Risk

- Pure deletions relative to Overleaf still show up as absence rather than strikeout because this is a manual redline in the live source rather than a `latexdiff` build.
