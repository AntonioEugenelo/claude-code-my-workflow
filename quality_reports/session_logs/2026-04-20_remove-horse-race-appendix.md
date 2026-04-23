## Session Log: Remove Horse-Race Appendix

**Date:** 2026-04-20

### Request

Remove the horse-race appendix from the compiled Tariffs_ECB paper and rebuild the PDF.

### Changes

- Commented out `\input{sections/a_appendix_horse_race}` in `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`.

### Verification

- Recompiled `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex` with:
  - `latexmk -pdf -interaction=nonstopmode -file-line-error -outdir='build_redline_20260420' '0_main.tex'`
- Confirmed the rebuilt PDF exists at:
  - `master_supporting_docs/Tariffs_ECB/0_clean/build_redline_20260420/0_main.pdf`
- Confirmed the compiled auxiliary file no longer contains `sec:horse_race` or `Cross-Sectoral Regression Results`.

### Residual Warnings

- Pre-existing unresolved references remain in the model appendix and calibration section.
- Pre-existing duplicate labels remain in the theory sections.
