Status: in progress

Scope
- Deep cleanup of `master_supporting_docs/Tariffs_ECB/0_clean/`.
- Remove or archive files that are not part of the active `0_main.tex` manuscript source tree or its required supporting generated assets.
- Preserve the live manuscript sources, active figures, active generated appendix tables, and the in-place `0_main.pdf` verification target.

Files Likely To Change
- `master_supporting_docs/Tariffs_ECB/0_clean/*`
- `master_supporting_docs/Tariffs_ECB/0_clean/old/*`
- `quality_reports/session_logs/2026-04-23_0-clean-deep-cleanup.md`

Plan
1. Audit `0_main.tex` dependency closure for included section files, generated inputs, and referenced figure assets.
2. Classify root-level wrappers, stale verification folders, wrapper build artifacts, and orphan LaTeX aux files.
3. Remove dead build artifacts and archive inactive source wrappers or inactive sections/assets if they are outside the active closure.
4. Recompile `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex` in place and confirm the cleaned tree still builds.
5. Record the cleanup outcome and any residual caveats in the session log.

Verification
- Compile `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex` in place with `latexmk -pdf -interaction=nonstopmode -halt-on-error 0_main.tex`.
- Re-list the `0_clean` tree to confirm dead wrappers and stale aux files are gone.

Assumptions
- The active manuscript target is only `0_main.tex`.
- Root-level wrapper `.tex` files and their side-product build artifacts are dead unless they are still referenced by the active tree.
- Files inside `0_clean/generated/` remain if they are input by active appendix sections.
