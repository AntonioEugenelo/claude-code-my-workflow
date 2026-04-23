## Objective

Identify why the sectoral transmission matrices in the active paper changed materially, tracing the change from manuscript figures back through the MCMS generator, exported matrix CSVs, and recent git/Overleaf history.

## Scope

- Audit only; do not change source files unless a clear bug is found and the user asks for a fix.
- Inspect:
  - `master_supporting_docs/MCMS/new_process.py`
  - `master_supporting_docs/MCMS/output_python/extra_charts/Figure_SectoralSpillover_Matrix.csv`
  - `master_supporting_docs/Tariffs_ECB/0_clean/figures/Fig_SectoralSpillover_USA.png`
  - `master_supporting_docs/Tariffs_ECB/0_clean/figures/Fig_SectoralSpillover_CHN.png`
  - `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels.tex`
  - recent git history in both `MCMS` and `Tariffs_ECB`

## Working Hypotheses

1. The main change may be the deliberate shift from on-impact / short-horizon objects to 12-quarter cumulative GDP and CPI objects.
2. A second change may be a switch in the GDP object itself, for example from output-style sector responses to value-added contributions.
3. The apparent change may also reflect figure-refresh timing: regenerated matrices may now match a newer export path while the user is comparing against an older compiled artifact or earlier branch state.

## Planned Steps

1. Read the recent plan and session-log trail for the matrix refresh.
2. Diff the relevant MCMS generator blocks across recent commits.
3. Diff the exported matrix CSV across recent commits where possible.
4. Compare the current manuscript caption/text against the current generator semantics.
5. Summarize the exact reasons for the visual change, separating intended changes from any possible unintended drift.

## Verification

- Confirm the exact commit(s) where the matrix logic changed.
- Confirm whether the current paper figure matches the current MCMS export.
- Confirm whether the caption/text matches the generator semantics.
- Report whether the change was intentional, accidental, or mixed.
