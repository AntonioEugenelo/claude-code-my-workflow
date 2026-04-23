# Requirements Specification: Active-Manuscript Figure Pipeline Cleanup

**Date:** 2026-04-13
**Status:** DRAFT

---

## Objective

Clean up unnecessary figure-generation artifacts and consolidate paper-facing figure generation into `master_supporting_docs/MCMS/new_process.py`, using the active `0_main.tex` text as the authority on which figures are required and which versions should be treated as canonical.

---

## Requirements

### MUST Have (Non-Negotiable)

- [ ] The active figure set must be derived from the sections actually included by `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`.
- [ ] `master_supporting_docs/MCMS/new_process.py` must become the single Python entry point for generating all active paper-facing figures used by the current manuscript.
- [ ] Section 5 figures currently delegated to `gen_section5_figs.py` must be generated directly inside `new_process.py`.
- [ ] Sync/copy logic from MCMS to `Tariffs_ECB/0_clean/figures/` must include only the active manuscript figure set.
- [ ] Obsolete paper-facing figure artifacts and obsolete helper scripts that are outside the active manuscript manifest must be removed or no longer produced.
- [ ] The paper must still compile locally after the cleanup.

### SHOULD Have (Preferred)

- [ ] The active figure manifest should be explicit in code so future drift between manuscript text and generated assets is harder to reintroduce.
- [ ] Cleanup should preserve unrelated user-owned edits in the dirty nested repos.
- [ ] Figure-generation code should reuse existing data extraction helpers where practical instead of duplicating logic.

### MAY Have (Optional, If Time)

- [ ] Add small comments or helper structure in `new_process.py` that clarify which figure blocks correspond to the active manuscript.
- [ ] Remove redundant paper copies or sync targets for figures referenced only by archived or commented-out sections.

---

## Clarity Status

| Aspect | Status | Notes |
|--------|--------|-------|
| What counts as “necessary” | CLEAR | Necessary means referenced by sections actively included by `0_main.tex`, plus current appendix table inputs. |
| Which manuscript is authoritative | CLEAR | The local `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex` tree is the authority. |
| Cleanup scope for archived `.tex` sections | ASSUMED | I will not delete historical/inactive section source files unless they are directly part of the obsolete Python figure pipeline. |
| Cleanup scope for generated figures | CLEAR | I will remove or stop syncing paper-facing figure artifacts not used by the active manuscript. |
| Cleanup scope for non-figure generated outputs | ASSUMED | I will not broadly delete CSV/PDF analysis outputs unless they are clearly obsolete figure-side artifacts of the retired pipeline. |

**Status Definitions:**
- **CLEAR:** Fully specified, no ambiguity
- **ASSUMED:** Reasonable assumption made in absence of clarity; user can override
- **BLOCKED:** Cannot proceed until this is answered

---

## Success Criteria

- `new_process.py` can regenerate the active paper-facing figures without calling `gen_section5_figs.py`.
- The paper-facing figure directory no longer contains obsolete synced figures from archived sections.
- `0_main.tex` compiles locally using the cleaned pipeline outputs.

---

## Approval

[ ] User approved: 2026-04-13
