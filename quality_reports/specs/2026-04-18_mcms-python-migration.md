## Requirements Specification: MCMS Python Migration

**Date:** 2026-04-18
**Status:** DRAFT

---

## Objective

Move the Tariffs ECB paper's Python-owned data-processing and regression capabilities into the MCMS repository so they run natively from `master_supporting_docs/MCMS/` while preserving seamless paper-side output generation.

---

## Requirements

### MUST Have (Non-Negotiable)

- [ ] MCMS becomes the source owner for the Python logic currently used to generate horse-race appendix and stacked-regression outputs.
- [ ] The migrated Python entrypoints run successfully from inside `master_supporting_docs/MCMS/` without depending on being launched from `master_supporting_docs/Tariffs_ECB/0_clean/`.
- [ ] Paper-facing generated outputs still land in the locations expected by the Tariffs ECB manuscript workflow, or compatibility shims preserve that behavior.
- [ ] Imports, path resolution, and data-loading logic are robust to the new ownership location.
- [ ] The migration does not disturb unrelated staged or dirty work already present in the top repo or nested repos.

### SHOULD Have (Preferred)

- [ ] Legacy paper-side entrypoints are reduced to thin wrappers or removed cleanly if no longer needed.
- [ ] MCMS documentation reflects the new Python ownership and how to run the migrated scripts.
- [ ] Shared helpers are organized so future Python post-processing lives in MCMS instead of being reintroduced in the paper repo.

### MAY Have (Optional, If Time)

- [ ] MCMS gains a small dedicated Python package or namespace directory for post-processing helpers instead of keeping multiple flat scripts at repo root.
- [ ] The migrated scripts expose a clearer command-line interface for output destinations or paper-root overrides.

---

## Clarity Status

| Aspect | Status | Notes |
|--------|--------|-------|
| Scope of "all Python capacities" | ASSUMED | Interpreted as the four Python files in `master_supporting_docs/Tariffs_ECB/0_clean/` that implement horse-race appendix and stacked-regression logic. |
| Ownership target inside MCMS | CLEAR | Python logic should live under `master_supporting_docs/MCMS/`, which already owns model outputs and Python post-processing. |
| Backward compatibility for old paper-side commands | ASSUMED | Prefer preserving seamless behavior with wrappers or compatible output paths unless inspection shows there are no callers to preserve. |
| Verification bar | CLEAR | The migrated scripts must execute from MCMS and still produce the expected paper-facing artifacts without import or path failures. |

**Status Definitions:**
- **CLEAR:** Fully specified, no ambiguity
- **ASSUMED:** Reasonable assumption made in absence of clarity; user can override
- **BLOCKED:** Cannot proceed until this is answered

---

## Success Criteria

- The relevant Python source files are owned by MCMS, with no paper-side business logic left behind beyond optional wrappers.
- Running the migrated entrypoints from MCMS succeeds and writes the expected regression/table artifacts to the paper workflow's expected locations.
- Repository docs and path contracts match the new layout closely enough that future use does not require ad hoc path edits.

---

## Approval

[ ] User approved: 2026-04-18
