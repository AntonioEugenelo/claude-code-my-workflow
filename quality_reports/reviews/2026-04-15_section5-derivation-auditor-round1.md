# Derivation Auditor Review: Section 5 Round 1

**Date:** 2026-04-15
**Target:** `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
**Reviewer:** `derivation-auditor`
**Score:** `97/100`

## Equations Or Derivations Checked

- GDP / trade-balance accounting identity in [25_market_clearing_and_gdp.tex](</C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/25_market_clearing_and_gdp.tex:13>) and the linear superposition claim in [56_sectoral_channels.tex](</C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex:11>).
- Sectoral own-versus-aggregate decomposition and the row-sum identity in [56_sectoral_channels.tex](</C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex:45>).
- CPI-weighting convention in [24_government.tex](</C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/24_government.tex:15>) and benchmark EA trade-balance arithmetic in [55a_benchmark_and_robustness.tex](</C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/55a_benchmark_and_robustness.tex:33>).

## Discrepancies

- No material numerical or algebraic discrepancy found.
- Minor wording ambiguity at [56_sectoral_channels.tex](</C:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex:65>): the sentence that the lower panels `do not exactly decompose aggregate CPI` is correct for the domestic-price panels, but it could be misread as contradicting the earlier exact CPI-contribution bars.

## Propagation Risk

- Low. The checked arithmetic supports the core downstream claims on US sign reversal, Chinese amplification, the US services drag, and the small-but-nonzero euro-area trade-balance channel.
- Residual risk is interpretive rather than mathematical.

## Verified Correct

- `g_{k,j}^{agg} = g_{k,j}^{own} + g_{k,j}^{spill}` within the linearized solution.
- `3.19% × 0.19% ≈ 0.0062%` and `0.0369% × 16.7% ≈ 0.0062%`.
- `0.0785 = 0.0598 - (-0.0187)`, `-0.0604 = -0.0613 - (-0.0009)`, and `0.0171 ≈ 0.0785 - 0.0604 - 0.0010`.
- The quoted spillover-share calculations are internally consistent with the stated own/spill magnitudes.
- The benchmark trade-balance / GDP accounting in Section 5 is consistent with the model identities in Sections 24 and 25.
