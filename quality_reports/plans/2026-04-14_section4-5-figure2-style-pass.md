# Plan: Section 4/5 style pass and Figure 2 reorder

**Status:** ACTIVE  
**Branch:** `codex-ecb-tariffs`

## Objective

Incorporate the new drafting comments by restoring the conclusion to the compiled manuscript, smoothing the Section 4/5 prose without undoing the accepted argument, trimming non-essential footnotes and stray draft phrases, reordering Figure 2 to match the text, and rebuilding the manuscript.

## Files

- `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `master_supporting_docs/MCMS/new_process.py`
- plus any source file containing “available from authors on request”
- `quality_reports/session_logs/2026-04-14_section4-5-figure2-style-pass.md`

## Steps

1. Find and edit the exact prose blocks flagged by the user in Section 4 and Section 5.
2. Add the conclusion back to `0_main.tex`.
3. Remove “available from authors on request” language and the specified half-life sentence.
4. Reorder Figure 2 in the figure-generation script to match the narrative order in the text.
5. Remove only non-useful footnotes while preserving issue-flagging footnotes.
6. Rebuild `0_main.tex`, check the resulting PDF, and log the pass.
