# Requirements Specification: Sectoral Transmission Matrices to Three-Year Cumulative Metrics

**Date:** 2026-04-23
**Status:** APPROVED

---

## Objective

Recreate the active sectoral transmission matrices so both the GDP panel and the inflation panel report 12-quarter cumulative responses rather than the current impact/4-quarter objects, and align the manuscript text with those regenerated figures.

---

## Requirements

### MUST Have (Non-Negotiable)

- [x] Update the active spillover-matrix generator in `master_supporting_docs/MCMS/new_process.py` so the GDP matrix uses 12-quarter cumulative sectoral value-added responses aggregated with the existing GDP weights.
- [x] Update the inflation matrix so it uses 12-quarter cumulative sectoral inflation contributions rather than the current 4-quarter cumulative measure.
- [x] Refresh the exported matrix CSV and the active paper figures `Fig_SectoralSpillover_USA.png` and `Fig_SectoralSpillover_CHN.png`.
- [x] Update the active manuscript captions and nearby explanatory text so they describe the new three-year cumulative matrix objects accurately.
- [x] Rebuild `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex` and verify the rebuilt PDF references the updated figures.

### SHOULD Have (Preferred)

- [x] Preserve the current figure layout, ordering, labels, and upstreamness sorting so the change is metric-only.
- [x] Keep the row-sum decomposition checks against the benchmark cross-section export, but repoint them to the cumulative benchmark columns.

### MAY Have (Optional, If Time)

- [ ] Update any standalone verification or appendix-only helper documents that duplicate the same matrix captions if they are in active use.
- [ ] Add a note in project memory if this uncovers a non-obvious figure-pipeline dependency.

---

## Clarity Status

| Aspect | Status | Notes |
|--------|--------|-------|
| Horizon for "three year cumulative" | CLEAR | The MCMS active pipeline already uses `Cum12` naming and `HORIZON = 12`, so the natural interpretation is a 12-quarter sum. |
| GDP object in the matrix top panel | ASSUMED | Interpreted as the 12-quarter sum of sectoral value-added responses weighted by the existing GDP weights, because the current top panel already uses weighted sectoral VA contributions. |
| Scope of manuscript edits | CLEAR | Active references are in `55b_sectoral_transmission_decomposition.tex` and `56_sectoral_channels.tex`, which already cite these matrix figures. |

**Status Definitions:**
- **CLEAR:** Fully specified, no ambiguity
- **ASSUMED:** Reasonable assumption made in absence of clarity; user can override
- **BLOCKED:** Cannot proceed until this is answered

---

## Success Criteria

- The matrix generator writes cumulative 12-quarter GDP and inflation contributions to `Figure_SectoralSpillover_Matrix.csv`.
- The refreshed USA and China spillover PNGs are regenerated from source and synced into the paper figures directory.
- The active manuscript compiles successfully and its matrix captions/text describe three-year cumulative GDP and inflation rather than on-impact GDP or four-quarter inflation.

---

## Approval

[x] User approved: 2026-04-23
