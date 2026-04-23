# Requirements Specification: Structural Determinants Main-Text Update

**Date:** 2026-04-23
**Status:** DRAFT

---

## Objective

Update the active “Mechanisms behind the sectoral ranking” subsection so the main text uses the new structural-determinants charts and explains the mechanism in terms of bilateral trade share plus consumption share, IO centrality, and price flexibility.

---

## Requirements

### MUST Have (Non-Negotiable)

- [ ] Replace the old `Fig_*_Structural_Scatter_3x4.png` references in the active Section 5 source with the new cross-country GDP and inflation charts.
- [ ] Keep bilateral trade share in the prose as the first-order exposure margin.
- [ ] Present the displayed structural parameters as consumption share, IO centrality, and price flexibility.
- [ ] Update the text so it matches the new cumulative GDP and cumulative inflation figures rather than the retired 3x4 layout.

### SHOULD Have (Preferred)

- [ ] Use the actual current cross-section fits from the benchmark cumulative objects when describing what the new figures show.
- [ ] Keep captions explicit about rows, columns, and cumulative formulas.

### MAY Have (Optional, If Time)

- [ ] Tighten neighboring sentences that still implicitly describe the old figure design.

---

## Clarity Status

| Aspect | Status | Notes |
|--------|--------|-------|
| Target subsection | CLEAR | Interpreted as `55b_sectoral_transmission_decomposition.tex`, which is still included by `0_main.tex` and still references the old 3x4 figures. |
| Bilateral trade share in figures | CLEAR | Bilateral trade share remains in the explanatory text but not in the displayed new figures, which use the old three-parameter set. |
| Displayed parameters | CLEAR | Consumption share, IO centrality, and price flexibility. |

---

## Success Criteria

- The active Section 5 subsection no longer references the old 3x4 structural-scatter PNGs.
- The main manuscript PDF shows the new cross-country GDP and CPI structural-determinants charts and the surrounding text matches them.

---

## Approval

[ ] User approved: 2026-04-23
