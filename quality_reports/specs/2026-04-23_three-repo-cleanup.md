# Requirements Specification: Three-Repo Cleanup

**Date:** 2026-04-23
**Status:** DRAFT

---

## Objective

Remove files that are clearly unnecessary across the root repo, `MCMS`, and `Tariffs_ECB`, while preserving source files and ambiguous local work.

---

## Requirements

### MUST Have (Non-Negotiable)

- [x] Delete only files that are clearly derived, temporary, duplicated, or disposable.
- [x] Preserve source-of-truth files such as `.tex`, `.py`, `.m`, `.md`, `.qmd`, and current figure scripts.
- [x] Preserve ambiguous untracked work products unless they are unmistakably temporary.
- [x] Recheck `git status --short` in all three repos after cleanup.

### SHOULD Have (Preferred)

- [x] Remove stale build directories and verification artifacts from `Tariffs_ECB/0_clean/`.
- [x] Remove obsolete generated outputs and logs from `MCMS/output_python/` where safe.
- [x] Leave each repo in a cleaner state without broad destructive operations like `git clean -fdx`.

### MAY Have (Optional, If Time)

- [ ] Add ignore coverage for recurring disposable artifacts if a pattern is clear and low-risk.
- [ ] Consolidate duplicated generated outputs if a single retained location is clearly preferable.

---

## Clarity Status

| Aspect | Status | Notes |
|--------|--------|-------|
| Meaning of "unnecessary" | ASSUMED | Interpreted as safe-to-regenerate or clearly temporary/disposable. |
| Root-repo untracked workflow material | ASSUMED | Kept by default because plans, logs, docs, and exploration material may be intentional. |
| Nested repo build artifacts | CLEAR | Build directories, verify outputs, temp PDFs, and transient logs are disposable. |
| Deletion of ambiguous untracked source files | BLOCKED | Will not delete unless clearly not needed. |

---

## Success Criteria

- Only clearly disposable artifacts are removed.
- No active source files are deleted.
- `git status --short` in all three repos shows fewer disposable artifacts than before.

---

## Approval

[ ] User approved: 2026-04-23
