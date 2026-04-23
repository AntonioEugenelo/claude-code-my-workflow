## Plan: Section 4 Reciprocal Benchmark Restore

**Date:** 2026-04-20  
**Status:** ACTIVE

### Objective

Update the live `Tariffs_ECB` manuscript so that Section 4.1 once again presents the intended two-leg benchmark:

- the China-retaliation line is shown in Figure 1
- the corresponding discussion from the synced Overleaf head is restored
- subsection 4.1.2 explicitly states the euro-area consumption response
- the final paragraph of 4.1.1 no longer implies that tariff revenue "compensates" GDP losses

### Scope

- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`
- `master_supporting_docs/MCMS/new_process.py`
- regenerated Figure 1 assets used by `0_main.tex`

### Assumptions

- For this request, the intended baseline for Section 4.1 is the synced Overleaf `HEAD` version that still includes the reciprocal benchmark discussion and the dashed China-retaliation series.
- The user wants the benchmark presentation restored only where it affects Section 4.1 and Figure 1; the broader unilateral rewrites elsewhere in the paper are not being revisited unless required for consistency.

### Planned Steps

1. Restore the reciprocal-benchmark discussion in Section 4.1 from the synced Overleaf head, while revising the tariff-revenue language to describe an accounting cushion rather than a compensation claim.
2. Re-enable the reverse benchmark line in the MCMS focused benchmark figure export and regenerate Figure 1.
3. Recompile `0_main.tex` and verify that the updated PDF contains the restored dashed retaliation line and revised Section 4.1 text.

### Verification

- Regenerate benchmark figure assets from the MCMS pipeline.
- `latexmk -pdf -interaction=nonstopmode -file-line-error 0_main.tex`

### Known Risk

- Some current redline markup in Section 4.1 reflects earlier local cleanup rather than a clean diff against the user’s intended baseline, so restoring the Overleaf wording may require selective manual redline cleanup afterward.
