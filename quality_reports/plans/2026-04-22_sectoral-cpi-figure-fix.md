## Objective

Replace the current non-additive sectoral inflation object in the active-manuscript figure pipeline with the exact sector-bundle CPI decomposition implied by the first-order Dynare solution, then regenerate the affected inflation figures and verify that the new sectoral outputs sum to aggregate CPI.

## Scope

- Update `master_supporting_docs/MCMS/new_process.py`.
- Regenerate the section-5 inflation-related CSV and PNG artifacts.
- Verify exact additivity numerically against aggregate CPI for the affected outputs.

## Steps

1. Add helpers to load CPI-sector weights and compute sector-bundle CPI contributions from the full Dynare solution.
2. Route the benchmark cross-section, spillover matrix, and own-sector inflation scatter through the new CPI-sector object.
3. Regenerate the affected CSV and figure outputs.
4. Run a numerical verification pass showing that the revised sectoral CPI contributions sum to aggregate CPI.
