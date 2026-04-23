# Theory Critic Review: Section 5 Round 1

**Date:** 2026-04-15
**Target:** `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
**Reviewer:** `theory-critic`
**Score:** `84/100`

## Summary Verdict

This is a strong, readable section with a clear empirical payoff, but it still leaned too hard on local linear accounting as if it were a structural explanation. The main theoretical risk was not arithmetic; it was over-interpreting a first-order sectoral decomposition as a durable mechanism, especially in the China and euro-area interpretations.

## Findings

### Model Necessity

- The 44-sector spillover matrix was informative, but the section had not yet shown that this granularity was necessary for the core claim. A coarser block decomposition could likely establish the US services-drag and China-amplification contrasts with less visual and conceptual load.

### Assumption Tightness

- The additivity claims are exact only under the linearized, same-steady-state setup and the benchmark closure. Language such as `exact object` and `sign reversal` risked sounding more general than the benchmark-local accounting warranted.

### Result Sharpness

- The line that China is `not mainly a services story` was too strong given that services still account for `50.9%` of absolute spillover mass. The stronger claim is comparative: China is less services-concentrated than the United States.

### Argument Gaps

- The mechanism from sectoral protection to positive US own-sector gains to negative aggregate GDP needed a cleaner separation between tariff protection, tariff-revenue recycling, and demand compression outside the protected sector.
- The `clean third-country example` wording for the euro area was too tidy for an outcome that is still the net of US, China, and ROW channels.

### Exposition

- The opening paragraph collapsed GDP and CPI into one share-weighted story even though the aggregation logic differs across the two objects.

## Hard Seminar Questions

1. If tariff revenue were not rebated lump-sum, which part of the US sign-reversal story would break first?
2. Can the US spillover reversal be derived from a 3-block model, or does it require the full 44-sector network?
3. Why should readers treat the China result as more than a services story once services still exceed half of absolute spillover mass?
4. How sensitive are the sectoral rankings to the sector aggregation scheme and to moving waste out of the services block?
5. What is the precise identifying object in the single-sector experiment: a causal contribution, a local comparative static, or a linear accounting residual?

## Strengths To Preserve

- The section cleanly distinguishes own-sector incidence from aggregate incidence.
- The numerical examples are sharp and memorable.
- The caveat that the lower inflation panels are not exact CPI decompositions is good methodological discipline.
