# Plan: Section 4/5 comment incorporation

**Status:** ACTIVE  
**Branch:** `codex-ecb-tariffs`

## Objective

Incorporate the new manuscript comments by tightening the abstract, rewriting Section 5 for clearer sequencing and definitions, removing redundant references, trimming the invoicing discussion in Section 4, and adapting the conclusion to the revised emphasis.

## Files

- `master_supporting_docs/Tariffs_ECB/0_clean/sections/02_title_page.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/60_Conclusions.tex`
- `quality_reports/session_logs/2026-04-14_section4-5-comment-incorporation.md`

## Steps

1. Rewrite the Section 5 opening so it explains why aggregates are small before introducing the decomposition objects.
2. Restructure Section 5.1 to discuss aggregate sectoral contributions first, then own-sector responses, then the mechanism behind the divergence.
3. Remove redundant references to Appendix Figure A1 / diagonal-restoration language and delete the specified Section 4 paragraph on cross-regime ROW movement.
4. Shorten the abstract and adapt the conclusion to the revised narrative, explicitly noting the US services drag if it remains numerically correct.
5. Recompile `0_main.tex`, run a focused prose review, and update the session log.
