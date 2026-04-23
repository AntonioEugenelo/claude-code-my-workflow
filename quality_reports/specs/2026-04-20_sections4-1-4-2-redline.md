# Requirements Specification: Sections 4.1/4.2 Redline Fix Pass

**Date:** 2026-04-20
**Status:** DRAFT

---

## Objective

Revise the active Section 4 manuscript material so the Section 4.1 and 4.2 text, captions, and benchmark figure presentation match the MCMS source of truth, then compile a full-paper PDF with the new edits highlighted in red for inspection.

---

## Requirements

### MUST Have (Non-Negotiable)

- [ ] Fix the Section 4.1/4.2 wording and captions in `master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex`.
- [ ] Correct the elasticity definition so the text/caption matches the current MCMS export (`\delta=\mu=1`) unless a rerun is performed.
- [ ] Correct the tariff definition anywhere the robustness and invoicing exercises are described as bilateral when the active code path is US-on-China only.
- [ ] Fill the still-open Section 4 robustness placeholders that belong to the active manuscript route.
- [ ] Recompile the full `0_main.tex` manuscript successfully.
- [ ] Make the new manuscript changes visibly red in the compiled PDF for user inspection.

### SHOULD Have (Preferred)

- [ ] Improve the benchmark Figure 1 presentation in the active generation path if it can be done without disturbing unrelated dirty-worktree changes.
- [ ] Rebalance Section 4.1.1/4.1.2 so the euro-area discussion sits in the euro-area subsection rather than the US/China subsection.
- [ ] Remove old blue markup in the touched Section 4.2 text if that material is being retained in revised form.

### MAY Have (Optional, If Time)

- [ ] Clean nearby wording issues in the touched paragraphs if they are obvious and source-safe.
- [ ] Add a focused session log for this implementation pass.

---

## Clarity Status

| Aspect | Status | Notes |
|--------|--------|-------|
| “Sections 4.1 and 4.2” target | ASSUMED | Interpreted as the active Section 4 source in `55a_benchmark_and_robustness.tex`, plus the benchmark figure route it cites. |
| “All the points” scope | ASSUMED | Interpreted as the open action-point items that directly affect Section 4.1/4.2: benchmark-figure cleanup, 4.1.2 rebalance, household paragraph, IO placeholders, elasticity definition, tariff-definition/caption fixes, and blue-markup cleanup in Section 4.2. |
| Red inspection markup | CLEAR | The compiled manuscript should intentionally keep the newly edited text in red so the user can inspect it. |
| Need to rerun MCMS elasticity experiment | ASSUMED | Not required unless the user insists on `\delta=1,\mu=2`; current task will align prose to the existing `\delta=\mu=1` export. |

**Status Definitions:**
- **CLEAR:** Fully specified, no ambiguity
- **ASSUMED:** Reasonable assumption made in absence of clarity; user can override
- **BLOCKED:** Cannot proceed until this is answered

---

## Success Criteria

- The active Section 4 source no longer mislabels the robustness and invoicing exercises as bilateral when the code path is US-on-China only.
- The elasticity text/caption matches the current MCMS export provenance.
- The full manuscript compiles to PDF from source.
- The resulting PDF visibly highlights this pass’s manuscript edits in red.

---

## Approval

[ ] User approved: pending
