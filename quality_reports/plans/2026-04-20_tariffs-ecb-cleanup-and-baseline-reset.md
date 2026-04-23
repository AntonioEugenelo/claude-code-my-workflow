## Plan: Tariffs ECB Cleanup And Baseline Reset

**Date:** 2026-04-20  
**Status:** ACTIVE

### Objective

Update the live `master_supporting_docs/Tariffs_ECB/0_clean` manuscript so that:

- footnote 20 in the trade-elasticity discussion is removed
- text the user identifies as already live on Overleaf is treated as baseline rather than current redline content
- non-essential `.py`, `.pdf`, and `.tex` files are removed from the nested `Tariffs_ECB` repo without breaking `0_main.tex`

### Scope

- Live manuscript sources under `master_supporting_docs/Tariffs_ECB/0_clean/`
- File cleanup only inside the nested `master_supporting_docs/Tariffs_ECB/` repo
- Recompile target: `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`

### Assumptions

- "Already live in Overleaf" means the user wants that wording to appear as baseline black text in the compiled manuscript, even if the synced git `HEAD` still contains historical red markup or older wording.
- "Non-essential `.tex` files" means files outside the current `0_main.tex` include graph, plus standalone section-only drivers and unused horse-race appendix sources.
- "Non-essential `.pdf` files" means standalone manuscript subset PDFs not required for the live `0_main` build. `0_main.pdf` remains.
- All `.py` files currently inside `master_supporting_docs/Tariffs_ECB/0_clean/` are non-essential to the live paper build and can be removed.

### Planned Steps

1. Confirm the current `0_main.tex` include graph and list file-deletion targets that sit outside it.
2. Edit `55a_benchmark_and_robustness.tex` to remove the unit-elasticity footnote and strip red markup from the tariff-revenue paragraph.
3. Edit other live manuscript files so the user-designated baseline wording is black rather than red.
4. Delete the non-essential `.py`, `.pdf`, and `.tex` files identified from step 1.
5. Recompile `0_main.tex` with `latexmk` and check for blocking regressions.
6. Update the session log with the final cleanup actions and verification result.

### Verification

- `latexmk -pdf -interaction=nonstopmode -file-line-error 0_main.tex`
- Confirm the deleted files are absent afterward.
- Confirm `0_main.pdf` still builds successfully.

### Known Risk

- The synced git `HEAD` does not fully match the user’s intended baseline for title/introduction wording, so the cleanup is guided by the current user instruction rather than strict diff-to-`HEAD` fidelity.
