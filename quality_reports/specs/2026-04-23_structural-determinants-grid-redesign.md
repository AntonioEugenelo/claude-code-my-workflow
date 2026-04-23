# Requirements Specification: Structural Determinants Grid Redesign

**Date:** 2026-04-23
**Status:** DRAFT

---

## Objective

Replace the current three country-specific structural-determinants scatter grids with two manuscript figures: one for cumulative GDP and one for cumulative inflation, each arranged as a 3x3 grid with countries in rows and structural determinants in columns.

---

## Requirements

### MUST Have (Non-Negotiable)

- [ ] Use three-year cumulative responses for both GDP and inflation on the vertical axis.
- [ ] Produce exactly two structural-determinants figures for the active manuscript pipeline: one GDP chart and one inflation chart.
- [ ] Use 3x3 layouts with three structural columns: consumption share, IO centrality, and price flexibility.
- [ ] Consumption-share column must use the benchmark consumption-share object `\beta_{ki}`, not the bilateral trade share proxy.
- [ ] Column titles must include the relevant model object in parentheses.
- [ ] Captions must state the formula used to compute the cumulative response shown in the rows.

### SHOULD Have (Preferred)

- [ ] Preserve the existing point colors by country and the current regression-overlay style.
- [ ] Keep the charts sourced from the MAT/calibration-driven pipeline in `master_supporting_docs/MCMS/new_process.py`.
- [ ] Update manuscript references and captions so the paper compiles without stale references to the retired 3x4 figures.

### MAY Have (Optional, If Time)

- [ ] Retire the old 3x4 structural-scatter filenames from the active-figure manifest if they are no longer referenced.

---

## Clarity Status

| Aspect | Status | Notes |
|--------|--------|-------|
| Grid rows | ASSUMED | Interpreted as rows for `USA`, `CHN`, and `EA`, because the user requested two 3x3 charts and fixed the three columns explicitly. |
| Cumulative horizon | CLEAR | “3 year cumulative” is interpreted as the 12-quarter sum already used elsewhere in the active cross-section export. |
| Consumption-share object | CLEAR | Use benchmark `\beta_{ki}` / `C_Share_{country}` columns, not bilateral-trade-share columns. |
| Caption formulas | CLEAR | Captions will state the 12-quarter sums for GDP and CPI used in the plotted dependent variables. |

---

## Success Criteria

- The active manuscript figure pipeline writes two updated structural-determinants PNGs with 3x3 layouts and the requested x-axis objects.
- `0_main.tex` compiles using the updated figures and captions with no broken figure references.

---

## Approval

[ ] User approved: 2026-04-23
