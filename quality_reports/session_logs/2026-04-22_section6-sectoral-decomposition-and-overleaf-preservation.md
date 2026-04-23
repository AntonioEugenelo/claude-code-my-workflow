# Session Log: Section 6 Sectoral Decomposition and Overleaf Preservation

## Objective

Preserve the current Overleaf-synced `Sectoral Channels of US--China Tariff Transmission` section, add a new preceding analytical section that improves on it, verify every substantive claim against the generated sectoral and horse-race outputs, and compile `0_main.tex`.

## Overleaf / Repo State

- Overleaf sync status checked first via `./scripts/sync-overleaf.sh status`.
- Result: all in sync at nested-paper commit `bc1454ed5651bf1348a45f82cbc05294f87370aa`.
- `0_clean/sections/56_sectoral_channels.tex` already matched the Overleaf-synced version, so it was preserved rather than reconstructed manually.

## Files Changed

- Added `master_supporting_docs/Tariffs_ECB/0_clean/sections/55b_sectoral_transmission_decomposition.tex`
- Updated `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex`

## Manuscript Structure Change

- Inserted a new analytical section before the preserved Overleaf sectoral section.
- New numbering in `0_main.tex`:
  - Section 5: new analytical sectoral decomposition section
  - Section 6: preserved Overleaf `Sectoral Channels` section
  - Section 7: conclusions

## Claim Audit Inputs

The new section's claims were checked against:

- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_6_Baseline_Bars_CrossSection.csv`
- `master_supporting_docs/MCMS/output_python/extra_charts/Figure_SectoralSpillover_Matrix.csv`
- `master_supporting_docs/Tariffs_ECB/0_clean/generated/horse_race_univariate.csv`
- `master_supporting_docs/Tariffs_ECB/0_clean/generated/horse_race_alpha_mu_aggregate.csv`
- `master_supporting_docs/Tariffs_ECB/0_clean/generated/horse_race_aggregate_outcomes.csv`
- `master_supporting_docs/Tariffs_ECB/0_clean/generated/horse_race_role_grid.csv` and generated tables where needed indirectly through `run_horse_race_appendix.py`

## Key Verified Claims Used in the New Section

- US aggregate GDP top drags: Textiles `-0.0285%`, Electronics `-0.0095%`, Other Manufacturing `-0.0069%`.
- China aggregate GDP top drags: Textiles `-0.0562%`, Electronics `-0.0495%`, Other Manufacturing `-0.0395%`.
- US aggregate GDP top positives: Fabricated Metals `+0.0026%`, Rubber and Plastic `+0.0022%`, Chemicals `+0.0019%`.
- US CPI top contributors: Textiles `+0.046 pp`, Electronics `+0.033 pp`, Other Manufacturing `+0.026 pp`.
- China CPI top contributors: Electronics `+0.0017 pp`, Textiles `+0.0012 pp`.
- China horse-race GDP fit:
  - bilateral trade `R^2 = 0.931`
  - broad sector-weight margin `R^2 = 0.041`
  - import-penetration margin `R^2 = 0.872`
  - value-added size proxy `R^2 = 0.000`
- US horse-race GDP fit:
  - bilateral trade `R^2 = 0.907`
  - broad sector-weight margin `R^2 = 0.014`
  - import-penetration margin `R^2 = 0.789`
- US own-sector value added: all 20 positive.
- China own-sector value added: all 20 negative.
- EA own-sector value added: all 20 non-negative.
- EA aggregate GDP contributions: 12 negative, 8 positive.
- US spillover decomposition:
  - absolute cross-sector share `0.6119`
  - cross term dominates own term in `9/20` shocked sectors
  - services share of absolute cross-sector mass `0.7747`
- China spillover decomposition:
  - absolute cross-sector share `0.5998`
  - cross term dominates own term in `18/20` shocked sectors
  - services share of absolute cross-sector mass `0.5087`
- EA regime result:
  - heterogeneous DCP GDP `R^2 = 0.068`
  - heterogeneous DCP CPI `R^2 = 0.924`
  - PCP GDP `R^2 = 0.930`

## Source Regeneration

### 1. Sectoral figure pipeline

Command:

```powershell
python new_process.py
```

Working directory:

```text
master_supporting_docs/MCMS
```

Notes:

- First run failed with Windows `OSError: [Errno 22] Invalid argument` on `Fig_Sectoral_Bars_GDP.png`.
- Diagnosis showed `master_supporting_docs/MCMS/output_python/extra_charts` was marked read-only.
- Cleared the attribute with:

```powershell
attrib -R "C:\CustomTools\claude-code-my-workflow\master_supporting_docs\MCMS\output_python\extra_charts"
attrib -R "C:\CustomTools\claude-code-my-workflow\master_supporting_docs\MCMS\output_python\extra_charts\*" /S
```

- Second run succeeded.
- The generator refreshed the manuscript CSVs and synced figure outputs back into `master_supporting_docs/Tariffs_ECB/0_clean/figures`.

### 2. Horse-race appendix pipeline

Command:

```powershell
python run_horse_race_appendix.py
```

Working directory:

```text
master_supporting_docs/Tariffs_ECB/0_clean
```

Result:

- Succeeded.
- Printed the same headline `R^2` values used in the new prose for China, the US, and the EA.

## Figure Differences After Regeneration

Relative to the nested-paper git baseline, the rerun changed these sectoral PNG binaries:

- `0_clean/figures/Fig_CHN_Structural_Scatter_3x4.png`
- `0_clean/figures/Fig_CN_Sectoral_Heatmap.png`
- `0_clean/figures/Fig_EA_Structural_Scatter_3x4.png`
- `0_clean/figures/Fig_SectoralSpillover_CHN.png`
- `0_clean/figures/Fig_SectoralSpillover_USA.png`
- `0_clean/figures/Fig_US_Structural_Scatter_3x4.png`

`git diff --stat` showed byte-size changes only in those files among the sectoral figures checked. The regenerated bar charts and EA sectoral heatmap did not show git diffs in the targeted comparison.

## Compile Verification

Command:

```powershell
latexmk -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex
```

Working directory:

```text
master_supporting_docs/Tariffs_ECB/0_clean
```

Result:

- Compile succeeded.
- Output PDF: `master_supporting_docs/Tariffs_ECB/0_clean/build_verify/0_main.pdf`

## Residual Warnings

These remained after the successful build and appear to be pre-existing or outside the new section:

- Multiply defined labels:
  - `eq:general_model_price_setting_foreign`
  - `eq:budget_constraint`
  - `eq:calvo_inflation_dynamics_2`
- Undefined references:
  - `sec:benchmark`
  - `sec:analytical_insights`
  - `eq:general_model_budget_constraint`
  - one additional log-reported item in the existing manuscript outside the new section cluster
- TinyTeX / latexmk environment warnings about duplicate fontmap entries and `quotemeta` noise

No new duplicate labels or undefined references were introduced by the `55b_sectoral_transmission_decomposition.tex` labels.

## Review Pass

- Manual consistency review performed on the new section after regeneration and compile.
- Checked for:
  - label collisions
  - claim / number mismatches
  - broken subsection references
  - unsupported statements about sign patterns and counts
- No substantive mismatches found in the new section.
- No delegated review-agent pass was run in this session because the user did not request or authorize delegation.

## Follow-up Rewrite to Match the Analogous Instruction Set

After the initial insertion, `55b_sectoral_transmission_decomposition.tex` was rewritten again to align more closely with `quality_reports/specs/2026-04-22_section6-analogous-rewrite-instruction-set.md`.

### Main rewrite changes

- Renamed the section from a generic decomposition label to the more phenomenon-centered title:
  - `Sectoral incidence and propagation of a US tariff on Chinese imports`
- Tightened the opening into a clearer three-paragraph scaffold:
  - questions
  - preview asymmetries
  - roadmap
- Recast subsection titles into claim-bearing analytical roles:
  - `Benchmark Sectoral Incidence`
  - `Direct Exposure and the Sectoral Ranking`
  - `Direct Incidence Inside the Tariffed Sector`
  - `Cross-Sector Propagation in the United States and China`
  - `The Euro Area as an Offsetting-Margins Object`
- Shifted the prose away from figure-order narration toward:
  - benchmark incidence first
  - then what sorts the ranking
  - then why own and aggregate incidence differ
  - then the special euro-area object
- Made the euro-area framing explicit using the netting / offsetting-margins logic required by the spec.
- Added a clearer bridge sentence into the preserved Overleaf section that follows.

### Verification after the follow-up rewrite

Claim check command:

```powershell
python - <<'PY'
import pandas as pd
bars = pd.read_csv(r'master_supporting_docs/MCMS/output_python/extra_charts/Figure_6_Baseline_Bars_CrossSection.csv')
alpha = pd.read_csv(r'master_supporting_docs/Tariffs_ECB/0_clean/generated/horse_race_alpha_mu_aggregate.csv')
agg = pd.read_csv(r'master_supporting_docs/Tariffs_ECB/0_clean/generated/horse_race_aggregate_outcomes.csv')
assert round(float(bars.loc[bars.Description=='Textiles','GDP_USA_Benchmark'].iloc[0]), 4) == round(-0.02853247407518051, 4)
assert round(float(bars.loc[bars.Description=='Electronics','GDP_CHN_Benchmark'].iloc[0]), 4) == round(-0.04948408816478089, 4)
assert int((bars['Sec_VA_USA_Benchmark']>0).sum()) == 20
assert int((bars['Sec_VA_CHN_Benchmark']<0).sum()) == 20
assert int((bars['GDP_EA_Benchmark']<0).sum()) == 12
assert round(float(alpha[(alpha.country=='CHN')&(alpha.outcome=='GDP')&(alpha.predictor=='trade')]['r2'].iloc[0]),3) == 0.931
assert round(float(alpha[(alpha.country=='USA')&(alpha.outcome=='GDP')&(alpha.predictor=='trade')]['r2'].iloc[0]),3) == 0.907
assert round(float(agg[(agg.regime=='Heterogeneous DCP')&(agg.country=='EA')&(agg.outcome=='GDP')]['r2'].iloc[0]),3) == 0.068
assert round(float(agg[(agg.regime=='Heterogeneous DCP')&(agg.country=='EA')&(agg.outcome=='CPI')]['r2'].iloc[0]),3) == 0.924
assert round(float(agg[(agg.regime=='PCP')&(agg.country=='EA')&(agg.outcome=='GDP')]['r2'].iloc[0]),3) == 0.930
print('rewrite claim check: OK')
PY
```

Result:

- Passed.

Compile command:

```powershell
latexmk -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex
```

Result:

- Passed after the follow-up rewrite.
- Output remained `master_supporting_docs/Tariffs_ECB/0_clean/build_verify/0_main.pdf`.
