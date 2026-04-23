# Section 5 Unit Elasticity Check

## Goal
Check whether the current active `Tariffs_ECB` Section 5 argument still works, in substance, under the saved unit-elasticity calibration (`delta = mu = 1`) relative to the current elasticity-two benchmark.

## Status
IN PROGRESS (started 2026-04-19)

## Hypotheses to Test
1. The current Section 5 sign patterns and top-sector rankings are broadly stable under unit elasticity.
2. The euro-area offset logic remains qualitatively valid under unit elasticity even if the exact magnitudes move.

## Success Criteria
- Produce a reproducible comparison of the core Section 5 objects under both elasticities.
- Identify which current claims survive with number swaps and which would need textual restructuring.

## Findings
- The US and China top-three aggregate GDP rankings are unchanged under unit elasticity: Textiles, Electronics, and Other Manufacturing still dominate.
- The current US own-vs-cross logic becomes stronger under unit elasticity: the cross-sector term exceeds the own-sector term in all 20 tariffed US sectors, versus 9 of 20 in the active elasticity-two benchmark.
- The EA section changes materially under unit elasticity. The on-impact EA aggregate GDP effect moves from `+0.0011%` to `-0.0100%`, and the current “small and mixed” bar pattern becomes more uniformly negative.
- The broad logic survives, but the active Section 5 would need targeted rewriting rather than a simple number swap, especially in the EA subsection and in the discussion of how exceptional the US sign-reversal pattern is.

## Timeline
- 2026-04-19: Started exploration and built a MAT-based comparison script.
- 2026-04-19: Generated unit-elasticity Section 5 benchmark bars/spillovers from saved `_UnitElast` MAT outputs and compared them to the active elasticity-two CSV layer.
