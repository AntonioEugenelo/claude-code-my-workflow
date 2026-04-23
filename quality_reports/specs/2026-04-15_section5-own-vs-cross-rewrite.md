# Requirements Specification: Section 5 Own-vs-Cross Rewrite

**Date:** 2026-04-15
**Status:** ACTIVE

---

## Objective

Rewrite active Section 5 so it uses an own-sector versus cross-sector framing, removes the misleading temporal sequencing of channels, adds a data-based discussion of when service losses are demand-led versus input-cost / network-led, and then starts the full adversarial review workflow.

---

## Requirements

### MUST Have

- [ ] Rewrite `56_sectoral_channels.tex` in a neutral analytic voice rather than the repo's Eugenelo prose style.
- [ ] Replace the "network term" framing with an own-sector versus cross-sector decomposition.
- [ ] Remove language implying that the tariff first generates one effect and only later another; the manuscript should state that the tariff jointly induces own-sector and cross-sector effects within the same linear equilibrium response.
- [ ] Add a data-based paragraph on the US service decline explaining where the household-demand block dominates and where the intermediate / cost side dominates.
- [ ] Keep claims disciplined: if the available accounting does not separately identify marginal costs, say so and use the closest observable decomposition rather than over-claiming.
- [ ] Verify the revised manuscript with a LaTeX build.
- [ ] Start the full adversarial review workflow after the rewrite.

### SHOULD Have

- [ ] Keep the existing figure set unless a figure reference becomes misleading after the rewrite.
- [ ] Make the own-vs-cross distinction do the main conceptual work of the section.
- [ ] Use concrete sector examples with numbers rather than abstract mechanism prose.

### MAY Have

- [ ] Tighten subsection titles so they reflect the new framing directly.
- [ ] Update the active session log with the key quantitative examples used in the rewrite.

---

## Clarity Status

| Aspect | Status | Notes |
|--------|--------|-------|
| Active manuscript source | CLEAR | `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex` |
| Tone requirement | CLEAR | User explicitly said "NOT in Eugenelo style". |
| Mechanism framing | CLEAR | User wants own-sector vs cross-sector, not network-term language. |
| Timing claim | CLEAR | User wants simultaneous effects, not sequential storytelling. |
| Service-margin discussion | CLEAR | Use data to distinguish household-demand-dominant service losses from opposite cases. |
| Review follow-up | CLEAR | Start full adversarial review after the rewrite. |

---

## Success Criteria

- Section 5 reads as a coherent own-sector versus cross-sector argument.
- The service-loss discussion uses concrete numbers from current model outputs and does not overstate identification.
- `latexmk` succeeds on `0_main.tex`.
- The adversarial review workflow is planned and started on the rewritten file.
