## Objective

Restore a clean `0_main.pdf` in `master_supporting_docs/Tariffs_ECB/0_clean` and rewrite the Section 6 propagation subsection so it no longer relies on the old `g^{\mathrm{own}}` / `g^{\mathrm{cross}}` notation.

## Scope

- Fix the current bibliography source error that breaks the LaTeX build.
- Update the active manuscript file `0_clean/sections/56_sectoral_channels.tex`.
- Keep the new Figure 15 decomposition framing, but rewrite the propagation subsection title and prose in more mechanism-first language.

## Files Likely To Change

- `quality_reports/plans/2026-04-23_compile-fix-and-section6-rephrase.md`
- `master_supporting_docs/Tariffs_ECB/0_clean/bibliography.bib`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`

## Assumptions

- The current compile failure is fully explained by duplicate / conflicting BibTeX entries, especially the duplicate dominant-currency entry with `Plagborg-M{\o}ller`.
- The user wants the active section file `56_sectoral_channels.tex`, not the inactive draft in `55b_*`.
- The requested prose change is local to the subsection title and the discussion immediately below it, not a full Section 6 rewrite.

## Verification

- Run `latexmk -pdf -interaction=nonstopmode -halt-on-error 0_main.tex` in `master_supporting_docs/Tariffs_ECB/0_clean`.
- Confirm the PDF is produced successfully.
- Inspect the edited subsection in `56_sectoral_channels.tex` to ensure the mechanism framing no longer uses the old shorthand notation.
