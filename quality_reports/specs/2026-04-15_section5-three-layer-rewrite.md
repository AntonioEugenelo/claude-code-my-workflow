# Requirements Specification: Section 5 Three-Layer Rewrite

**Date:** 2026-04-15
**Status:** DRAFT

---

## Objective

Rewrite active Section 5 so it advances a clear three-layer decomposition argument for tariff transmission, then verify the manuscript and run the full adversarial review loop on the rewritten section.

---

## Requirements

### MUST Have (Non-Negotiable)

- [ ] Reorganize Section 5 around the sequence: sectoral leaders -> own-sector versus cross-sector incidence -> demand versus marginal-cost interpretation of cross-sector responses -> separate euro-area total-response statement.
- [ ] Use model-produced numbers and accounting identities to explain mechanisms rather than only describing figures.
- [ ] Push back on the strongest theory-critic caveats by stating what is benchmark-local accounting, what is identified, and what remains descriptive.
- [ ] Avoid Eugenelo-style prose; keep the tone clear, analytic, and non-repetitive.
- [ ] Verify the rewritten manuscript with a LaTeX build.
- [ ] Run the full adversarial review loop with the routed read-only review agents and save artifacts on disk.

### SHOULD Have (Preferred)

- [ ] Minimize repeated explanations across subsections by assigning each subsection one analytical job.
- [ ] Make the transition between the three decomposition layers explicit so each figure earns its place.
- [ ] Keep the euro-area discussion separate from the US/China mechanism stack so the third-country result reads as a payoff, not a detour.

### MAY Have (Optional, If Time)

- [ ] Add a short opening thesis paragraph that states the section's decomposition logic in one pass.
- [ ] Tighten captions or cross-references if they become misleading after the rewrite.

---

## Clarity Status

| Aspect | Status | Notes |
|--------|--------|-------|
| Active Section 5 source | CLEAR | `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex` is the live Section 5 file in `0_main.tex`. |
| Target structure | CLEAR | User specified the desired analytical order and requested a rewrite rather than incremental polishing. |
| Tone | CLEAR | User explicitly requested non-Eugenelo style. |
| Review depth | CLEAR | User explicitly requested the full adversarial review loop after the rewrite. |
| Scope limits | ASSUMED | Primary edits stay within Section 5 and review/session artifacts unless verification or reviewer findings require a small supporting change elsewhere. |

**Status Definitions:**
- **CLEAR:** Fully specified, no ambiguity
- **ASSUMED:** Reasonable assumption made in absence of clarity; user can override
- **BLOCKED:** Cannot proceed until this is answered

---

## Success Criteria

- The rewritten Section 5 presents a coherent three-layer decomposition argument, supported by model numbers and benchmark-local accounting.
- `latexmk` builds the manuscript without a Section 5 blocking error.
- The adversarial review loop runs on the current rewritten file and each required reviewer report is saved under `quality_reports/reviews/`.

---

## Approval

[ ] User approved: 2026-04-15
