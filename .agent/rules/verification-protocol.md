---
paths:
  - "Slides/**/*.tex"
  - "Quarto/**/*.qmd"
  - "docs/**"
---

# Task Completion Verification Protocol

**At the end of EVERY task, the agent MUST verify the output works correctly.** This is non-negotiable.

## For Quarto/HTML Slides:
1. Run `./scripts/sync_to_docs.sh` (or `./scripts/sync_to_docs.sh LectureN`) to render and deploy
2. Open the HTML in browser: `open docs/slides/LectureX.html`
3. Verify images display by reading 2-3 image files to confirm valid content
4. Check HTML source for correct image paths
5. Check for overflow by scanning dense slides
6. Verify environment parity: every Beamer box environment has a CSS equivalent in the QMD
7. Report verification results

## For LaTeX/Beamer Slides:
1. Compile with xelatex and check for errors
2. Open the PDF to verify figures render
3. Check for overfull hbox warnings
4. **MANDATORY: Run adversarial review loop** (see below)

## Adversarial Review Loop (NON-NEGOTIABLE)

**After EVERY successful compilation of a `.tex` or `.qmd` file, the agent MUST run the full adversarial review loop as defined in `orchestrator-protocol.md`.** This is not optional. Skipping this step is a protocol violation.

### The Loop:
1. **REVIEW** — Run all applicable review agents (proofreader, slide-auditor, pedagogy-reviewer, domain-reviewer, tikz-reviewer if TikZ present)
2. **SCORE** — Compute quality score per `quality-gates.md` rubrics
3. **FIX** — Apply fixes for any CRITICAL or MAJOR issues found
4. **RE-COMPILE** — Verify fixes compile cleanly
5. **RE-REVIEW** — Run review agents again on the fixed file
6. **RE-SCORE** — Confirm score ≥ 90/100
7. **LOOP** — If score < 90, repeat from step 3 (max 5 rounds)
8. **REPORT** — Save scored report to `quality_reports/`

### Exit Conditions:
- Score ≥ 90 → present report to user with remaining recommendations
- 5 rounds exhausted → present report with all remaining issues listed
- **NEVER present work as "done" without a scored review report**

## For TikZ Diagrams in HTML/Quarto:
1. Browsers **cannot** display PDF images inline — ALWAYS convert to SVG
2. Use SVG (vector format) for crisp rendering: `pdf2svg input.pdf output.svg`
3. **NEVER use PNG for diagrams** — PNG is raster and looks blurry
4. Verify SVG files contain valid XML/SVG markup
5. Copy SVGs to `docs/Figures/LectureX/` via `sync_to_docs.sh`
6. **Freshness check:** Before using any TikZ SVG, verify extract_tikz.tex matches current Beamer source

## For R Scripts:
1. Run `Rscript scripts/R/filename.R`
2. Verify output files (PDF, RDS) were created with non-zero size
3. Spot-check estimates for reasonable magnitude

## Common Pitfalls:
- **PDF images in HTML**: Browsers don't render PDFs inline → convert to SVG
- **Relative paths**: `../Figures/` works from `Quarto/` but not from `docs/slides/` → use `sync_to_docs.sh`
- **Assuming success**: Always verify output files exist AND contain correct content
- **Stale TikZ SVGs**: extract_tikz.tex diverges from Beamer source → always diff-check

## Verification Checklist:
```
[ ] Output file created successfully
[ ] No compilation/render errors
[ ] Images/figures display correctly
[ ] Paths resolve in deployment location (docs/)
[ ] Opened in browser/viewer to confirm visual appearance
[ ] Reported results to user
```
