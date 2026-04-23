# Three-Repo Cleanup Plan

Status: in progress

Scope:
- Root repo `C:\CustomTools\claude-code-my-workflow`
- Nested repo `master_supporting_docs\MCMS`
- Nested repo `master_supporting_docs\Tariffs_ECB`

Goal:
- Remove files and directories that are clearly unnecessary because they are derived build artifacts, temporary verification outputs, stale logs, disposable local scratch files, or superseded generated copies.
- Preserve source files, workflow records, exploration material, and any untracked content whose status is ambiguous.

Assumptions:
- "Unnecessary" means safe-to-regenerate or clearly temporary.
- Tracked source changes already present in the repos are not part of this cleanup.
- Untracked plans, session logs, specs, docs, and exploration folders are kept unless they are unmistakably disposable.

Likely cleanup targets:
- LaTeX build directories and verification folders under `Tariffs_ECB/0_clean/`
- Temporary PDFs/TeX wrappers used only for local verification in `Tariffs_ECB/0_clean/`
- Stale temp files such as `codex_write_test.tmp`
- Generated logs and obsolete figure-output folders/files in `MCMS/output_python/`
- Root-level disposable generated artifacts if any are clearly derived and not source

Likely preserved:
- `quality_reports/` plans, session logs, specs, reviews
- `explorations/` subfolders
- `.agents/`, `.codex/`, and workflow docs unless they are proven disposable
- Untracked source `.tex`, `.py`, `.m`, `.md`, `.qmd`, and figures that are part of current work

Execution steps:
1. Inventory ambiguous root-level untracked files and classify only obviously disposable artifacts for deletion.
2. Clean `Tariffs_ECB/0_clean/` of build/verify/temp files and folders.
3. Clean `MCMS/` of obsolete generated outputs and logs that are not source-of-truth.
4. Recheck git status in all three repos.
5. Summarize what was removed and what was intentionally kept.

Verification:
- `git status --short` in all three repos after cleanup
- Ensure no source files needed for the active manuscript or figure pipeline were removed

Known risk:
- Some generated outputs in `MCMS/output_python/` may still be useful as local references, so only clearly obsolete or duplicated generated artifacts should be removed.
