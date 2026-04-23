# Requirements Specification: Unit Elasticity Paper Rewrite

**Date:** 2026-04-09
**Status:** DRAFT

---

## Objective

Rebase the Tariffs_ECB paper and its figure pipeline on the full unit-elasticity calibration, with both household and firm Armington elasticities set to one in the paper-facing baseline.

---

## Requirements

### MUST Have (Non-Negotiable)

- [x] Regenerate the paper-facing MCMS outputs under the full unit-elasticity mapping (`armington = 2`, implying `Delta_C = 1`, `Delta_X = 1`).
- [x] Rerun the downstream preprocessing and figure-generation pipeline from source code rather than editing numbers or figures by hand.
- [x] Update the compiled Tariffs_ECB manuscript so the benchmark calibration, captions, numbers, and narrative all match the regenerated unit-elasticity outputs.
- [x] Keep Overleaf `master` untouched during implementation; isolate the work on a separate local `Tariffs_ECB` git branch first.
- [x] Preserve and incorporate the current uncommitted Tariffs_ECB edits already present in the title page, introduction, and conclusions unless the user overrides that choice.
- [x] Recompile the paper after the rewrite and report verification status from actual commands.

### SHOULD Have (Preferred)

- [x] Preserve the existing manuscript structure and figure inventory where possible, so the rewrite is a baseline swap rather than a paper redesign.
- [x] Recast the old elasticity robustness figure into a comparison between the new unit-elasticity baseline and the former high-elasticity benchmark, instead of leaving a redundant “low elasticity” exercise.
- [x] Update any pipeline labels, legends, helper scripts, or notes that would otherwise misdescribe the new baseline.

### MAY Have (Optional, If Time)

- [ ] Update supporting MCMS documentation (`README.md`, `PIPELINE_MAP.md`) if the pipeline logic changes materially.
- [ ] Refresh any paper-number extraction helper script that becomes stale after the baseline swap.

---

## Clarity Status

| Aspect | Status | Notes |
|--------|--------|-------|
| “Separate overleaf branch” | ASSUMED | The configured Overleaf git remote only exposes `master`. I will use a separate local `Tariffs_ECB` git branch and avoid pushing to `overleaf/master` during this task. |
| Existing dirty Tariffs_ECB state | ASSUMED | Current local edits in `02_title_page.tex`, `11_introduction.tex`, and `60_Conclusions.tex` are treated as live work to preserve and carry forward. |
| Unit-elasticity baseline mapping | CLEAR | Existing repo note and code agree that the paper-facing unit-elasticity case is `armington = 2`, giving `Delta_C = 1` and `Delta_X = 1`. |
| Elasticity robustness slot after baseline swap | ASSUMED | Figure 4 and related prose will be inverted to compare the new unit-elasticity baseline with the former `delta=mu=2` benchmark, unless the regenerated pipeline shows a better manuscript fit. |

**Status Definitions:**
- **CLEAR:** Fully specified, no ambiguity
- **ASSUMED:** Reasonable assumption made in absence of clarity; user can override
- **BLOCKED:** Cannot proceed until this is answered

---

## Success Criteria

- The MCMS rerun, preprocessing, and figure scripts complete against the unit-elasticity baseline and regenerate the paper-facing figures from source.
- The Tariffs_ECB source compiles successfully, and the benchmark calibration, figures, captions, and quoted quantitative claims are consistent with the regenerated outputs.

---

## Approval

[ ] User approved: pending
