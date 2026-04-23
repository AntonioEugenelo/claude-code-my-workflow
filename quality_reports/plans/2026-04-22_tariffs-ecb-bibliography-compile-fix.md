## Objective

Restore a clean, openable `0_main.pdf` for `master_supporting_docs/Tariffs_ECB/0_clean` by fixing the bibliography issues currently blocking the LaTeX build.

## Scope

- Inspect the current `pdflatex` / BibTeX failure logs.
- Identify duplicate or conflicting entries in `bibliography.bib`.
- Normalize the problematic bibliography entry that generates the `Plagborg-M{\o}ller` failure in `0_main.bbl`.
- Rebuild the paper until the compile completes successfully.

## Constraints

- Do not revert unrelated manuscript edits already present in the worktree.
- Treat `bibliography.bib` as the source of truth; do not hand-edit generated output as a final fix.
- Keep the newly added EA decomposition figure in place.

## Verification

- Run BibTeX / LaTeX passes from `master_supporting_docs/Tariffs_ECB/0_clean`.
- Confirm `0_main.pdf` is produced successfully and is openable.
- Confirm the previous bibliography errors no longer appear in the build logs.
