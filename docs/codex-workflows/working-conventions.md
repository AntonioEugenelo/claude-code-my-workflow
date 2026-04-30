# Working Conventions

Use this document for the active conventions that were previously scattered across legacy rules.

## Source of Truth

Treat source files as authoritative and derived artifacts as disposable outputs.

- Edit `.tex`, `.qmd`, `.R`, `.py`, `.m`, and figure scripts first.
- Do not hand-edit exported PDFs, generated SVGs, copied figures, or rendered HTML.
- For Beamer to Quarto work, update the Beamer source first, then regenerate the derived Quarto/TikZ artifacts.

## Exploration Workflow

All experimental work starts in `explorations/`.

- Create a dedicated subfolder for each exploration.
- Use the fast-track quality floor of `60/100` while exploring.
- Graduate work to production only after it is reproducible, documented, and strong enough for the normal production gate.
- Archive dead ends with a short explanation rather than leaving ambiguous leftovers.

Suggested exploration structure:

```text
explorations/
  [project]/
    README.md
    R/
    scripts/
    output/
    SESSION_LOG.md
```

## Local-First Reference Checks

Before going online, check the local supporting material under `master_supporting_docs/`.

- Search `supporting_papers/`, `supporting_slides/`, and nearby project folders first.
- Use PyMuPDF (`fitz`) for PDF extraction on this machine when you need text from local papers.
- On Windows, wrap stdout in UTF-8 and use `glob.glob()` for paths with special characters.
- Pull only the relevant pages or sections into context; do not bulk-load whole papers.

## Replication Before Extension

When porting or extending analysis:

1. inventory the original scripts, data, and target outputs
2. record benchmark numbers before editing
3. replicate the baseline result first
4. save intermediate outputs
5. extend only after the baseline matches within tolerance

If the baseline does not match, stop the extension work and isolate the discrepancy first.

## Reproducibility Defaults

- Use relative paths.
- Create output directories programmatically.
- Save intermediate results when computations are heavy.
- Record verification commands and outcomes in the session log.
- Update repo maps or equivalent structure notes after material directory or pipeline changes.
