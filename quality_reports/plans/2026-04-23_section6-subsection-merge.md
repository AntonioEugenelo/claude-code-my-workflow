## Objective

Merge subsections `6.1` with `6.2` and `6.3` with `6.4` in the active Section 6 (`55b_sectoral_transmission_decomposition.tex`), while preserving the original topics as subsubsections and keeping the prose aligned with the 2026-04-22 analogous rewrite instruction set.

## Scope

- Restructure the live Section 6 in `master_supporting_docs/Tariffs_ECB/0_clean/sections/55b_sectoral_transmission_decomposition.tex`.
- Keep the existing three opening paragraphs and the section's claim-driven logic.
- Recast the merged subsections so each top-level subsection maps to one of the section's three preview facts:
  - direct exposure and the aggregate ranking
  - own-sector versus cross-sector incidence
  - the euro area as an offsetting-margins object
- Preserve existing figures and labels unless a structural edit requires a local reference update.

## Files Likely To Change

- `quality_reports/plans/2026-04-23_section6-subsection-merge.md`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55b_sectoral_transmission_decomposition.tex`

## Assumptions

- The user's "Section 6" request refers to the active analytical section in `55b_sectoral_transmission_decomposition.tex`, not the preserved Overleaf section in `56_sectoral_channels.tex`.
- "Keep the original topics separated as subsubsections" means retaining the existing analytical units from `6.1` through `6.4` as lower-level headings inside the merged subsections.
- No fresh numeric audit is required if the rewritten prose keeps the previously verified directional claims and only uses numbers where necessary.

## Verification

- Compile `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex` with `latexmk -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex`.
- Check the compile artifacts to confirm the new subsection numbering is `6.1`, `6.2`, `6.3`, with the preserved subtopics appearing as subsubsections.
- Run a manual prose review on the changed section for:
  - alignment with the introduction's sectoral finding
  - compliance with the analogous rewrite instruction set
  - internal consistency of claims and cross-references
