# Derivation Audit: 55a_benchmark_and_robustness.tex + 56_sectoral_channels.tex
**Date:** 2026-04-08
**Auditor:** derivation-auditor agent

## Summary
- **Verdict:** VERIFIED WITH MINOR ISSUES
- **Equations checked:** 6 core derivation dependencies, plus the section-level accounting identities they rely on
- **Errors found:** 1 (CRITICAL: 0, MAJOR: 0, MINOR: 1)
- **Propagation risk:** No critical propagation to the paper's main claims
- **Overall:** The section-4/5 argument is internally consistent given the intended first-order linearization and the model equations in the firms, government, market-clearing, and appendix derivation sections
- **Suggested score:** 97/100 before any other non-derivation issues

## Findings

### Finding D-1: Intermediate-input aggregator uses inconsistent source-country index notation
- **Location:** [23_firms.tex:37-52](c:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/23_firms.tex#L37) and [a_appendix.tex:226-230](c:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/a_appendix.tex#L226)
- **Severity:** MINOR
- **Category:** Algebra / Notation
- **Stated result:** The nested CES/Armington structure over sectoral intermediates is intended to aggregate source-country inputs into the sectoral intermediate bundle, which then feeds the marginal-cost equation used in sections 4 and 5.
- **Issue:** The printed final-layer aggregator in `eq:final_layer_intermediate_aggregator` reuses `j` as both the buying-sector index and the summation index, while the surrounding definitions and the footnote indicate the intended summation is over source countries `l`. The notation is therefore not type-safe as written.
- **Impact:** This does not overturn the downstream cost-propagation logic in sections 4 and 5, because the later derivation and narrative clearly use the intended corrected interpretation. However, the equation should be corrected for formal consistency, since the Leontief/IO amplification mechanism in section 5 rests on this aggregator hierarchy.
- **Score effect:** -3

## Verified Correct
- The trade-balance and GDP decomposition used in section 4 is consistent with the market-clearing and GDP accounting identities in [25_market_clearing_and_gdp.tex](c:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/25_market_clearing_and_gdp.tex#L1).
- The tariff-revenue rebate and policy-rate logic used in the benchmark and counterfactual narratives are consistent with [24_government.tex](c:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/24_government.tex#L1).
- The DCP export Phillips-curve interpretation in section 4 is consistent with the appendix derivation in [a_appendix.tex](c:/CustomTools/claude-code-my-workflow/master_supporting_docs/Tariffs_ECB/0_clean/sections/a_appendix.tex#L210).
- The superposition claim in section 5 is valid under the explicitly stated first-order perturbation setting.

## Bottom Line
- No CRITICAL derivation errors were found in the audited sections.
- No MAJOR derivation errors were found in the audited sections.
- The only issue is a MINOR notation inconsistency upstream of the section-5 channel discussion.
