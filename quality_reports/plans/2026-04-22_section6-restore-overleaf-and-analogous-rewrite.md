## Objective

Restore the Overleaf-synced `Section 5` sectoral-channels text as a preserved baseline, add a new preceding improved section that follows the 2026-04-22 Section 6 analogous rewrite instruction set, and verify every substantive claim in the new section against the data / figure pipeline before finalizing prose.

## Scope

- Reconstruct the current Overleaf version of `56_sectoral_channels.tex` as the preserved baseline section text.
- Create a new improved sectoral-transmission section before that preserved baseline, with the requested subsection structure:
  - section introduction / roadmap
  - aggregate effects of sectoral tariffs
  - determinants of sectoral rankings with structural scatterplots
  - own-sector value added and inflation
  - own-sector vs cross-sector terms
  - euro-area sectoral dimension
- Use horse-race evidence to compare the China-trade margin against sector size for aggregate incidence.
- Check each numerical / directional claim in the new section against the saved outputs or regenerated data.
- Update manuscript structure in `0_main.tex` and any new section files needed.
- Compile `0_main.tex` after edits.

## Constraints

- Preserve the Overleaf-synced baseline sectoral section content rather than silently overwriting it.
- Do not disturb Jose-Elias changes outside the targeted restructuring.
- Use the `2026-04-22_section6-analogous-rewrite-instruction-set.md` as the prose/structure rule set after the claim audit is complete.
- Keep user placeholders only where explicitly requested by the current task; otherwise avoid introducing fresh placeholders.
- Do not revert unrelated worktree changes.

## Verification

- Audit claim-supporting numbers against:
  - current figure files
  - horse-race appendix objects / scripts
  - saved sectoral decomposition outputs
- Rebuild with:
  - `latexmk -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex`
- Review changed prose / references for internal consistency after the compile succeeds.
