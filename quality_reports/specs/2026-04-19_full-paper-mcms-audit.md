# Requirements Specification: Full Paper MCMS Audit

**Date:** 2026-04-19
**Status:** DRAFT

---

## Objective

Produce a model-grounded audit of the active tariff manuscript that verifies quoted numbers, figure descriptions, and shock definitions against the MCMS code and generated outputs, and separately run an adversarial review of the generating code itself.

---

## Requirements

### MUST Have (Non-Negotiable)

- [ ] Check the manuscript against MCMS model/code/output artifacts rather than against manuscript prose alone.
- [ ] Record each audited number with a verdict and evidence path to the MCMS source, generated CSV/MAT output, or plotting code.
- [ ] Record for each audited figure what scenario/shock it represents and whether the manuscript description matches the pipeline.
- [ ] Run a read-only adversarial review loop on the audit memo.
- [ ] Run a read-only adversarial code review on the generating code.

### SHOULD Have (Preferred)

- [ ] Build a reproducible inventory of manuscript numeric claims and figure references.
- [ ] Distinguish exact matches, rounding-consistent matches, unsupported claims, stale claims, and pipeline-label mismatches.
- [ ] Separate model-truth findings from presentation-only findings.
- [ ] Save review artifacts and session notes on disk.

### MAY Have (Optional, If Time)

- [ ] Add helper scripts or structured extraction outputs to make future audits faster.
- [ ] Group findings by manuscript section and by figure family.

---

## Clarity Status

| Aspect | Status | Notes |
|--------|--------|-------|
| Audit target manuscript | CLEAR | Use the active source in `master_supporting_docs/Tariffs_ECB/0_clean/sections/`. |
| Source of truth | CLEAR | Use MCMS code, saved run configuration, and generated outputs as authoritative. |
| Need for manuscript edits | ASSUMED | This request asks for an audit and review, not immediate fixes. |
| Scope of "all numbers" | ASSUMED | Includes numeric claims in active manuscript prose/captions, not bibliography or administrative metadata. |
| Scope of "pictures" | ASSUMED | Includes figures referenced by the active manuscript and generated through MCMS or its post-processing pipeline. |

**Status Definitions:**
- **CLEAR:** Fully specified, no ambiguity
- **ASSUMED:** Reasonable assumption made in absence of clarity; user can override
- **BLOCKED:** Cannot proceed until this is answered

---

## Success Criteria

- An on-disk audit report exists that maps manuscript numeric claims and figure descriptions to MCMS-backed evidence and clearly identifies all discrepancies.
- An on-disk adversarial review report exists for the audit memo.
- An on-disk adversarial review report exists for the generating code.
- Reviewer scores and unresolved risks are recorded explicitly rather than estimated.

---

## Approval

[ ] User approved: 2026-04-19
