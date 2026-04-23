Status: In progress

Task: verify that the DCP footnote citations match the actual papers online, then compare the current Tariffs manuscript tree against `overleaf/master` and list all differences other than color-only markup.

Scope:
- Check the three footnote citations in `master_supporting_docs/Tariffs_ECB/0_clean/sections/12_related_literature.tex` against online primary sources.
- Confirm that the cited claims are directionally accurate and not hallucinated.
- Compare the current local `Tariffs_ECB` repo state against `overleaf/master`.
- Separate substantive differences from pure `\textcolor{...}` / `{\color{...} ...}` markup changes.

Files likely to change:
- `quality_reports/session_logs/2026-04-17_dcp-citation-audit-and-overleaf-diff.md`
- No manuscript source edits are planned unless the citation audit reveals a real mismatch that should be corrected.

Verification:
- Use official journal or publisher pages for the citation metadata.
- Use local git diff against `overleaf/master` for manuscript differences.
- Record exact file-level substantive differences and note any local untracked artifacts separately.

Assumptions:
- “Besides for differences in coloring” means to exclude review-color markup wrappers but still report any wording, title, author, spacing, or other source differences.
- The relevant Overleaf target is the configured remote branch `overleaf/master`.
