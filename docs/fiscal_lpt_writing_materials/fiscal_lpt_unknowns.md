# Fiscal LPT Unknowns and Calibration Choices

This branch implements the fiscal LPT mechanics from the `fiscal_lpt_*` files, but
the fiscal calibration remains provisional. The items below must be pinned down
before the model is quantitatively operational.

| Item | Current runtime value or status | Why it matters | Fix options |
| --- | --- | --- | --- |
| EA price-rigidity MAT input | Restored: `input_data/Price_Rigidities_Countries_EA/theta_es_de_fr_it.mat` | The standard `calibrate()` path needs this artifact before equation generation. | No current action required unless the artifact should be rebuilt from source spreadsheets. |
| `Tbar_C_k` steady-state VAT/consumption tax | Country-specific effective-wedge benchmark `[0.18, 0.12, 0.14, 0.05]` in EA, China, ROW, USA order | Converts VAT wedge innovations into revenue and affects budget dynamics. | Replace with constructed effective consumption-tax rates from revenue statistics and national-account bases when the full data build is added. |
| `Tbar_N_k` steady-state labour-income tax | Country-specific effective-wedge benchmark `[0.38, 0.25, 0.25, 0.28]` in EA, China, ROW, USA order | Converts labour-tax wedge innovations into revenue and controls the distortionary wage wedge scale. | Replace with constructed effective labour-tax wedges; split employee/employer incidence if needed. |
| `Tbar_Y_k_i` sectoral production tax/subsidy | Markup-offsetting steady-state subsidy `1/M_k_i - 1` | Determines whether production-tax revenue responds only to the new wedge or also to base movements. | Keep as a normative markup-offsetting benchmark; replace only if the experiment needs observed production taxes/subsidies instead. |
| `s_C_k` household-consumption base/GDP | Country-specific WDI benchmark `[0.5141, 0.3993, 0.5523, 0.6839]` in EA, China, ROW, USA order | Scales VAT revenue in the government budget. | Replace ROW with a true model-weighted residual aggregate when the data pipeline is expanded. |
| `s_L_k` labour-income base/GDP | Model-implied proxy `1 - sum_i (1 - psi_ki/M_ki) lambda_ki` | Scales labour-tax revenue and debt stabilization. | Validate against compensation-of-employees/GDP; replace with country-specific labour tax bases; or keep the model proxy only for qualitative experiments. |
| `s_MCY_k_i` production-tax base/GDP | Model-implied proxy `lambda_ki/M_ki` | Scales production-tax revenue by sector. | Validate against sector gross output, value added, or marginal-cost production-base data; aggregate sectors if data are too noisy. |
| `bgov_ss_k` public debt/GDP | Country-specific benchmark `[0.878, 0.8833, 0.94, 1.2079]` in EA, China, ROW, USA order | Multiplies interest-rate and inflation terms in the linearized budget. | Replace ROW with a true model-weighted residual aggregate when the data pipeline is expanded. |
| `psi_bgov_spread_k` debt-spread elasticity | Set to `0.00` | Avoids adding sovereign-risk transmission to a fiscal-accounting closure. | Add positive spread elasticities only in a sovereign-risk robustness exercise. |
| `rho_tau_C_k`, `rho_tau_N_k`, `rho_tau_Y_k_i` | Country-specific persistence; `rho_tau_Y` is common across sectors within country | Controls persistence of fiscal instruments and IRF shape. | Estimate AR terms from constructed tax-rate series when available. |
| `phi_tau_C_y_k`, `phi_tau_N_y_k`, `phi_tau_Y_y_k_i` | Country-specific output feedback; `phi_tau_Y_y` is common across sectors within country | Determines automatic stabilizer response to current output. | Estimate fiscal reaction functions; use lagged output to avoid simultaneity; use natural-output gaps if available. |
| `phi_tau_C_b_k`, `phi_tau_N_b_k`, `phi_tau_Y_b_k_i` | Country-specific debt feedback; `phi_tau_Y_b` is common across sectors within country | Debt stability depends on these coefficients. | Calibrate feedback to satisfy determinacy and bounded debt IRFs; compare closures using VAT, labour tax, production tax, or spending adjustments. |
| `sigma_tau_C_k`, `sigma_tau_N_k`, `sigma_tau_Y_k_i` | Country-specific shock scales; `sigma_tau_Y` is common across sectors within country | Maps unit shocks to tax-wedge movements. | Replace with empirical residual standard deviations after tax-rate series are constructed. |
| Sectoral production-tax dimensionality | Steady-state subsidies vary by markup; dynamic fiscal rules are country-specific and sector-common | Keeps sectoral markup correction while avoiding unidentified 176-rule dynamics. | Move to sector groups only if the experiment needs heterogeneous fiscal reaction functions. |
| Production-tax incidence | Implemented as marginal-cost wedge `mc_k_i + tau_Y_k_i` | Incorrect for sales taxes, input taxes, payroll taxes, carbon taxes, or subsidies changing production functions. | Keep only if the intended policy taxes the marginal-cost production base; otherwise modify demand or cost-minimization equations. |
| VAT incidence and CPI target | VAT is uniform and monetary policy still targets pre-tax `pi_C_k` | A tax-inclusive CPI target would change Taylor-rule behavior. | Keep pre-tax target for fiscal-wedge experiments; or add `pi_C_tax_k = pi_C_k + tau_C_k - tau_C_k(-1)` and target it. |
| Tariff revenue steady state | Linearized around zero steady-state tariffs | Nonzero tariff rates require revenue-base movement terms. | Keep zero-steady-state interpretation; or reconstruct bilateral consumption/intermediate bases and add base-movement terms. |
| Government spending/transfers | Not modeled | Current block is revenue/debt accounting only, not a full fiscal resource allocation model. | Add public consumption, transfers, or spending rules if the policy experiment requires resource-use effects. |
| Fiscal rule timing | Uses contemporaneous `y_k` | Creates within-period feedback and real-time information assumptions. | Use `y_k(-1)` for implementation lags; use output gaps for stabilization-rule interpretation. |

Minimum checks before quantitative use:

1. Restore or rebuild the missing price-rigidity MAT artifact.
2. Run the full Julia `solve_scenario` path and verify equation/variable counts, parser success, and Blanchard-Kahn determinacy.
3. Inspect debt IRFs under multiple `phi_tau_N_b_k` and `psi_bgov_spread_k` values.
4. Compare tax shock IRFs for VAT, labour tax, and representative sectoral production-tax shocks.
5. Decide whether the sectoral production-tax rules should remain fully disaggregated or be tied by sector groups.
