## Plan: Section 4.1.2 And Action-Plan Status Refresh

**Date:** 2026-04-20  
**Status:** ACTIVE

### Objective

1. Keep the strengthened euro-area discussion in Section 4.1.2, but adapt it to the restored two-sided US--China benchmark.
2. Recover the 10-point action plan and assess what remains open against the current live manuscript tree.

### Scope

- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
- `quality_reports/specs/2026-04-18_action-point-response-memo.md`
- session logging for this pass

### Planned Steps

1. Move the euro-area trade-balance and REER material out of 4.1.1 and into 4.1.2, preserving the explicit consumption-response language and adapting it to the two-sided benchmark.
2. Refresh the action-point memo with a concise current-status snapshot against the live tree.
3. Recompile `0_main.tex` and verify the updated PDF.

### Verification

- `latexmk -pdf -interaction=nonstopmode -file-line-error 0_main.tex`

### Known Risk

- The current manuscript mixes unilateral framing outside Section 4 with a restored two-sided Section 4 benchmark. That broader framing inconsistency may need a separate pass beyond this targeted request.
