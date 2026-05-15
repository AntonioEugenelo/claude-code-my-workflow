# Fiscal LPT Data Requirements and Source Audit

Date checked: 2026-05-08

Branch: `govt-julia`

This note audits the data still needed to make the fiscal LPT extension quantitatively operational in the Julia runtime. It covers the new fiscal objects currently calibrated with placeholders in `src/calibration.jl`, checks plausible data sources, and records whether the source actually solves the model need or only gives a partial proxy.

The restored EA price-rigidity input is no longer a data gap:
`input_data/Price_Rigidities_Countries_EA/theta_es_de_fr_it.mat` is present.

Current runtime calibration update:

- Country order is EA, China, ROW, USA.
- `Tbar_C = [0.18, 0.12, 0.14, 0.05]`.
- `Tbar_N = [0.38, 0.25, 0.25, 0.28]`.
- `S_C = [0.5141, 0.3993, 0.5523, 0.6839]`, using household-consumption/GDP benchmarks.
- `Bgov_ss = [0.878, 0.8833, 0.94, 1.2079]`.
- `Psi_bgov_spread = 0`.
- `Tbar_Y[k,i] = 1/M[k,i] - 1`, a markup-offsetting production-subsidy benchmark.
- Dynamic production-tax/subsidy rules are country-specific but common across all sectors within a country.

## Source Checks

| Source | What I checked | Availability | Does it solve a current need? | Caveat |
| --- | --- | --- | --- | --- |
| IMF WoRLD, 2026 update, https://www.imf.org/en/topics/fiscal-policies/world-revenue-longitudinal-database | Official page and download links. PowerShell GET returned 403, browser/web access works. | Available through IMF page with Excel/Stata downloads and IMF Data portal. 2026 update covers revenue trends since the early 1980s, 195 countries, time coverage to 2024. | Yes for broad tax revenue components needed to construct effective consumption/labour tax rates. | It gives revenue categories, not ready-made DSGE wedges; we still need national-account tax bases and a mapping from revenue categories to `tau_C` and `tau_N`. |
| World Bank WDI API, `NE.CON.TOTL.ZS`, https://data.worldbank.org/indicator/NE.CON.TOTL.ZS | API spot checks for final consumption/GDP. US 2024 returned 82.893; China 2024 returned 56.560. Euro-area aggregate was reachable but first-page values were null. | API available and machine-readable. | Yes for `S_C_k` for US, China, and many individual countries/ROW weights. | Euro-area aggregate should come from Eurostat or member-country aggregation rather than the WDI aggregate endpoint. |
| World Bank WDI API, `GC.DOD.TOTL.GD.ZS`, https://data.worldbank.org/indicator/GC.DOD.TOTL.GD.ZS | API/page spot check. US 2024 returned 117.973. | Available and machine-readable. | Partial for `Bgov_ss_k`. | This is central-government debt, while the model budget block is closer to general-government debt. Use IMF WEO or Eurostat for baseline when available. |
| Eurostat government debt, https://ec.europa.eu/eurostat/web/products-euro-indicators/w/2-22042026-bp | Direct GET returned 200. Page reports euro-area Q4 2025 debt/GDP and source dataset `gov_10q_ggdebt`. | Available. | Yes for euro-area `Bgov_ss`. | EA aggregate debt is available; country/member weighted construction may be needed if the model's EA block is not exactly EA20/EA21. |
| European Commission VAT rates, https://taxation-customs.ec.europa.eu/taxation/vat/vat-rates_en | Direct GET returned 200. | Available. | Partial for `Tbar_C_k` in EU countries. | Statutory VAT rates do not equal the effective consumption tax wedge; reduced rates/exemptions and base erosion matter. Use only for scenarios or cross-checks. |
| OECD Consumption Tax Trends 2024, https://doi.org/10.1787/dcd4dd36-en | Official page accessible in browser; PowerShell GET returned 403. | Available through OECD page/report. | Partial for VAT/GST rates and OECD consumption-tax structure. | OECD member coverage is good for US/EU but not sufficient for China/ROW and not a ready effective tax wedge. |
| OECD Tax Wedge, https://www.oecd.org/en/data/indicators/tax-wedge.html | Official page accessible in browser; PowerShell GET returned 403. | Available in OECD Data Explorer. | Partial for labour tax wedge in OECD countries. | Indicator is for an average single worker and is not a general equilibrium effective labour-income tax rate. Weak for China/ROW. |
| OECD GDP and Non-financial Accounts, https://www.oecd.org/en/data/datasets/gdp-and-non-financial-accounts.html | Official page accessible in browser. | Available in OECD Data Explorer. | Yes for GDP components, income-side accounts, and compensation-of-employees bases for OECD/partners. | Coverage and aggregation must be reconciled with the 4-country model blocks. |
| OECD employee compensation by activity, https://www.oecd.org/en/data/indicators/employee-compensation-by-activity.html | Official page accessible in browser. | Available in OECD Data Explorer. | Partial/validation source for `S_L_k`, especially by broad sector. | It reports compensation as percent of gross value added by broad activities, not directly the exact labour tax base/GDP for the model's 44 sectors. |
| OECD Input-Output tables, https://www.oecd.org/en/data/datasets/input-output-tables.html | Official page accessible in browser. | Available; 2025 release covers 1995-2022 and includes value-added components, including net taxes on production, compensation, fixed capital consumption, and operating surplus. | Good validation source for `S_MCY_k_i`, `S_L_k`, and production-tax bases for OECD/G20 countries. | It does not directly observe marginal cost; `S_MCY` remains partly model-implied. |
| OECD ICIO, https://www.oecd.org/en/data/datasets/inter-country-input-output-tables.html | Official page accessible in browser. | Available; 2025 ICIO includes 80 economies plus Rest of World, 1995-2022. | Useful for country-sector base validation and ROW construction. | Still not a sector-specific production tax wedge. |
| Eurostat SUT/FIGARO, https://ec.europa.eu/eurostat/web/esa-supply-use-input-tables/information-data | Direct GET returned 200. | Available. FIGARO links EU inter-country SUT/IOT with 27 EU countries, candidate countries, major trading partners including China and the US, and Rest of World. | Good for EU/EA sectoral bases and a consistency check against OECD ICIO. | Useful for IO bases, less direct for tax-rate wedges. |
| Tax Foundation state/local sales tax rates, https://taxfoundation.org/data/all/state/sales-tax-rates/ | Browser source checked. | Available. | Scenario/cross-check only for US statutory retail sales taxes. | Not official government data and not a national effective consumption tax wedge. Prefer revenue-based effective rates for calibration. |
| Literature: Mendoza, Razin, and Tesar (1994), NBER w4864, https://www.nber.org/papers/w4864 | Checked paper abstract and method. | Available. | Yes, gives the main way to avoid relying on statutory tax rates: construct effective consumption and factor-income tax rates from national accounts and revenue statistics. | The method must be implemented for the current model countries and updated data. |
| Literature: Leeper, Plante, and Traum (2009/2010), NBER w15160, https://www.nber.org/papers/w15160 | Checked paper abstract. | Available. | Yes for fiscal-rule closure logic and debt feedback priors. | US-focused; should not be copied mechanically to EA/China/ROW without sensitivity checks. |
| Literature: Trabandt and Uhlig (2009/2011), NBER w15343, https://www.nber.org/papers/w15343 | Checked paper abstract. | Available. | Useful cross-check for US/EU labour and consumption tax rates in DSGE settings. | Does not identify the sectoral production-tax block or country-specific fiscal rules for China/ROW. |

## Data Still Needed

| Runtime object | Needed data | Best available source path | Availability verdict | Does it fully solve it? | Recommended fix |
| --- | --- | --- | --- | --- | --- |
| `Tbar_C[k]` | Steady-state effective consumption tax/VAT wedge by model country block: EA, US, China, ROW. | Construct effective rates using IMF WoRLD/OECD Revenue Statistics tax revenue categories plus final consumption bases from WDI, OECD national accounts, Eurostat. Use EC/OECD statutory VAT only as cross-checks. | Available, but requires construction. | Mostly yes for EA/US/China; ROW needs weighted aggregation. | Implement Mendoza-Razin-Tesar-style effective consumption tax rates. For US, do not use VAT; use goods-and-services tax revenue relative to consumption. For China, use revenue-based effective tax if statutory VAT schedules are hard to reconcile. |
| `Tbar_N[k]` | Steady-state effective labour-income tax wedge by country block. | OECD Tax Wedge for OECD/EA/US cross-check; OECD national accounts and IMF/OECD revenue categories for constructed effective labour tax rates; WDI/official accounts for China where OECD coverage is weak. | Partly available. | Not fully from any one source. | Use effective-tax-rate construction from Mendoza-Razin-Tesar: allocate personal income taxes/social contributions to labour, divide by a labour-income base from compensation of employees and mixed-income treatment. Report China/ROW as lower-confidence unless official national accounts and revenue splits are added. |
| `S_C[k]` | Final consumption base divided by GDP. | WDI `NE.CON.TOTL.ZS`; Eurostat national accounts for EA; OECD expenditure accounts for OECD/EA/US; model-country aggregation weights for ROW. | Available. WDI API confirmed for US and China. | Yes, except EA/ROW aggregation choices. | Replace placeholder `1.00` with final consumption/GDP. Use Eurostat for EA, WDI/OECD for US and China, and construct ROW as GDP-weighted residual or model-weighted aggregate. |
| `S_L[k]` | Labour-income tax base/GDP. | OECD income-side national accounts; OECD employee compensation by activity; Eurostat national accounts; WDI/official national accounts for non-OECD. | Partly available. | Mostly, if compensation of employees is accepted as the base. | Replace current model proxy only after constructing compensation/GDP. If mixed income is important, apply the Mendoza-Razin-Tesar adjustment; otherwise document compensation-only as a conservative base. |
| `Bgov_ss[k]` | General-government debt/GDP by model country block. | Eurostat `gov_10q_ggdebt` for EA; IMF WEO general-government gross debt for US/China/ROW; WDI central-government debt as fallback only. | Available for EA; available through IMF/WDI alternatives for others. | Yes, with definition choice. | Use general-government gross debt/GDP as baseline. Avoid WDI central-government debt except as fallback because it is narrower than the budget block. |
| `Tbar_Y[k,i]` | Steady-state production tax/subsidy wedge by country-sector. | OECD IOT value-added components include net taxes on production; Eurostat/FIGARO SUT/IOT can validate EU sector bases; GTAP-like sectoral tax wedges may exist but are licensed and not ideal for reproducible work. | Sector base data available; true sector tax wedge not fully available. | No. | Literature/model workaround: keep `Tbar_Y = 0` in baseline and interpret `tau_Y` as a marginal-cost policy wedge around a neutral steady state. For quantitative production-tax experiments, estimate only grouped sector wedges or use OECD net taxes on production/value added as a validation proxy, not a clean wedge. |
| `S_MCY[k,i]` | Production-tax base/GDP by country-sector, currently `Lambda ./ M`. | Existing MCMS IO calibration is internally consistent; OECD IOT and ICIO; Eurostat FIGARO for EU/global IO cross-checks. | Available for validation. | Partly: marginal cost is not directly observed. | Keep model-implied `S_MCY` as baseline because `mc*y` is a model object. Validate sector magnitudes against gross output/value added and net-tax-base data from OECD/Eurostat. |
| `Rho_tau_C[k]`, `Rho_tau_N[k]`, `Rho_tau_Y[k,i]` | Persistence of fiscal instruments. | Estimate AR components from constructed tax-rate series; Leeper-Plante-Traum for fiscal-rule priors; LPT fiscal files for intended coefficients if they contain estimates. | Aggregate estimates possible; sectoral estimates weak. | No for full 4 x 44 sectoral production-tax persistence. | Estimate country-level `rho` for consumption/labour rates. Tie `rho_tau_Y` across sectors or sector groups; do not attempt 176 unconstrained AR rules without a strong sectoral tax-rate panel. |
| `Phi_tau_*_y` | Output/current-cycle response of fiscal instruments. | Estimate fiscal reaction functions using constructed tax-rate series and GDP/output gaps; literature priors from Leeper-Plante-Traum. | Possible for aggregates. | Not fully for China/ROW/sectoral production taxes. | Use aggregate country-level fiscal reaction rules; use lagged output or output gap to avoid contemporaneous-information assumptions. For sectoral `tau_Y`, set common or zero output feedback unless the policy experiment requires it. |
| `Phi_tau_*_b` | Debt feedback/stabilization coefficients. | Estimate with debt/GDP and tax-rate series; Leeper-Plante-Traum priors; debt-stability/determinacy grid. | Possible but fragile. | No single source identifies the exact model feedback coefficients. | Calibrate debt feedback to ensure bounded debt IRFs and run sensitivity over closures: labour-tax closure, VAT closure, production-tax closure, or mixed closure. |
| `Sigma_tau_C[k]`, `Sigma_tau_N[k]`, `Sigma_tau_Y[k,i]` | Shock scaling/innovation standard whatdeviations. | Standard deviations from constructed tax-rate residuals; or scenario shocks of one percentage point in tax wedges. | Available after tax-rate series are constructed. | Yes for aggregate tax shocks; no for full sectoral production shocks. | Define shock unit explicitly. Baseline recommendation: one percentage-point tax-wedge shock for transparent IRFs; empirical scaling as a secondary calibration. |
| `Psi_bgov_spread[k]` | Sovereign debt-spread elasticity. | Public market data can provide spreads for some countries, but not uniformly for EA/US/China/ROW. Literature on sovereign risk can provide priors, but this model does not otherwise have a sovereign default block. | Partial and conceptually mismatched. | No. | Set `Psi_bgov_spread = 0` in baseline unless sovereign-risk transmission is an intended mechanism. Add small positive values only as robustness, with debt-stability checks. |
| `rev_tariff` steady-state terms | Bilateral tariff revenue bases if nonzero steady-state tariffs are desired. | Existing trade IO data can provide trade bases; tariff schedules would require WTO/WITS/TRAINS or policy-specific tariff data. | Trade bases available; tariff schedules not checked in this audit. | Not needed for current zero-steady-state tariff interpretation. | Avoid adding this data need unless the fiscal experiment uses nonzero steady-state tariffs. Keep current zero-steady-state tariff interpretation for now. |
| Government spending/transfers | Spending or transfer paths if fiscal policy changes real resource use rather than only revenue/debt accounting. | IMF GFS/WEO, OECD government accounts, Eurostat COFOG/GFS. | Available. | Not needed by the current implemented block. | Avoid unless the experiment explicitly needs public consumption, transfers, or spending multipliers. Current block can remain revenue/debt accounting. |

## Gaps That Remain After Source Checks

1. Sector-level production tax wedges (`Tbar_Y[k,i]` and full sectoral fiscal rules) are not cleanly identified from the plausible public sources. OECD/Eurostat IO data can validate bases and net taxes, but they do not give the model's marginal-cost wedge by country-sector.

2. China and ROW effective labour tax rates require more construction than EA/US. OECD Tax Wedge is not enough and is OECD-centered; the right approach is revenue/national-account construction, with China-specific official revenue splits if we want high confidence.

3. Debt-spread elasticities are not a normal fiscal-calibration datum for this model. They would add a sovereign-risk mechanism without the rest of a sovereign-risk block.

4. Full fiscal reaction functions for every country and 44 sectors are over-parameterized relative to available data. The literature supports aggregate fiscal instruments responding to debt/output, but not an unrestricted country-sector rule matrix.

## Literature Workarounds

The most defensible way to avoid missing statutory and country-specific tax-rate data is to use effective average tax rates constructed from national accounts and revenue statistics. Mendoza, Razin, and Tesar (1994) explicitly propose this approach for consumption and factor-income taxes, and the method is aligned with representative-agent DSGE wedges.

For fiscal rules, Leeper, Plante, and Traum (2009/2010) support using rich but aggregate fiscal-instrument rules and show that debt stabilization can come from multiple fiscal instruments. This argues for estimating or calibrating a small set of country-level rules, not 176 independent sectoral rules.

For US/EU tax wedge magnitudes, Trabandt and Uhlig (2009/2011) provide DSGE-relevant cross-checks for labour and consumption tax rates. This is useful as a sanity check, not as the primary data source for China or ROW.

## Recommended Operational Path

1. Baseline data build:
   - `Tbar_C`: construct effective consumption tax rates from tax revenue and final-consumption bases.
   - `Tbar_N`: construct effective labour tax wedges using revenue categories, compensation of employees, and a documented mixed-income assumption.
   - `S_C`: WDI/OECD/Eurostat final consumption over GDP.
   - `S_L`: compensation of employees over GDP, with optional mixed-income adjustment.
   - `Bgov_ss`: general-government debt/GDP from Eurostat/IMF WEO; WDI only as fallback.
   - `S_MCY`: keep current model-implied base, validate against OECD/Eurostat IO data.

2. Baseline closure:
   - Use the markup-offsetting steady-state production subsidy, `Tbar_Y[k,i] = 1/M[k,i] - 1`.
   - Keep `Psi_bgov_spread = 0`.
   - Estimate or calibrate country-level fiscal-rule parameters for `tau_C` and `tau_N`.
   - Keep `tau_Y` rule parameters common across sectors within each country, unless sector groups are explicitly required.

3. Sensitivity checks:
   - VAT-financed, labour-tax-financed, and mixed fiscal closures.
   - Debt feedback grid sufficient to keep debt IRFs bounded.
   - One-percentage-point tax wedge shocks vs empirical residual-standard-deviation shocks.

4. Do not add more data unless the experiment needs it:
   - Nonzero steady-state tariffs require WTO/WITS/TRAINS tariff schedules and bilateral bases.
   - Spending/transfers require GFS/WEO/OECD/Eurostat spending data and a real-resource-use block.
   - Sovereign spreads require a sovereign-risk interpretation and should not be hidden inside a fiscal accounting closure.
