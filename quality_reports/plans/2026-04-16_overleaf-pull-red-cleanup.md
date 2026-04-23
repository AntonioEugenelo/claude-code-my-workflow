Status: In progress

Task: pull the latest Tariffs_ECB changes from Overleaf, then turn red manuscript text back to black everywhere except Sections 2 and 3 and footnotes in Section 1.

Scope:
- Sync `master_supporting_docs/Tariffs_ECB` from Overleaf using the repo sync script.
- Inspect the pulled manuscript for conflict markers or red-markup drift.
- Update the manuscript sources so red markup remains only where requested.
- Compile the main manuscript to verify the edited source still builds.

Likely files:
- `master_supporting_docs/Tariffs_ECB`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/*.tex`
- `quality_reports/session_logs/2026-04-16_overleaf-pull-red-cleanup.md`

Verification:
- `./scripts/sync-overleaf.sh pull`
- Search for `textcolor{red}`, `color{red}`, and related red markup outside the allowed sections.
- `latexmk -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex`

Assumptions:
- "section 1" means the introduction block in `sections/11_introduction.tex`.
- Preserve red markup only in Sections 2 and 3 and in footnotes inside Section 1; convert other red-marked body text to black by removing the red color commands rather than rewriting prose.
- If the Overleaf pull introduces merge conflicts, stop and report the blocker instead of making manual conflict-resolution guesses.
