# Proofreader Review: Section 5, Round 1

**Target:** `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
**Reviewer:** `proofreader`
**Round:** 1
**Score:** `87/100`

## Findings

1. `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex:16` and `:25` misdescribe the shock as an “aggregate 10 percentage-point bilateral tariff increase across all 20 tradeable sectors.” The surrounding text and figure labels describe a US tariff on Chinese imports with sector-by-sector decomposition, not a bilateral tariff. Proposed fix: `Shock: 10 percentage-point US tariff on Chinese imports, aggregated across the 20 sectoral decompositions.` Use the same wording in both captions.
2. `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex:53` leaves the spillover decomposition incomplete: `services` account for `51.0%` and `other tradeables` for `41.0%`, which sums to `92.0%` without explaining the remaining `8.0%`. That reads like an unfinished partition. Proposed fix: name the residual category explicitly, or revise the shares so they sum to `100%`.
3. `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex:77` says EA imports from China are “flat on impact” while reporting `-0.0009%`. That is small, but not flat. Proposed fix: `essentially flat on impact` or `near zero on impact`.

## Residual Risks

- The section is numerically dense, and several claims rely on figures or tables outside this file. This review checked prose consistency, not the underlying data.
