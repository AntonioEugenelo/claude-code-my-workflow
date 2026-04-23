# Benchmark Transmission Flowchart Plan

Date: 2026-04-14
Repo: `C:\CustomTools\claude-code-my-workflow`
Project: `master_supporting_docs/MCMS` and `master_supporting_docs/Tariffs_ECB`

## Goal

Recompute the benchmark IRF with intermediate-demand responses and assess or implement a figure that shows tariff transmission as a two-sided flow:

- top: tariff shock into final-demand reallocation
- bottom: tariff shock into intermediate-demand / cross-sector production transmission

The aim is an almost causal visualization that makes the propagation path legible sector by sector.

## Working Assumptions

- The benchmark object is the aggregate 10 pp reciprocal US-China tariff shock already used in the paper.
- The relevant state-space objects may need to be recovered from the full Dynare results rather than the light IRF export.
- A strict causal graph is not available from the model solution; the best feasible object may be an impact accounting decomposition using exact final-demand responses and intermediate-demand responses derived from saved decision rules and IO shares.

## Plan

1. Inspect the existing benchmark figure pipeline in `new_process.py` and identify where benchmark IRFs are loaded and plotted.
2. Inspect available Dynare output to determine whether source-specific final demand and intermediate-demand responses are saved directly or need to be reconstructed from the decision rules.
3. Implement a benchmark transmission extractor in `new_process.py` that saves a tidy table for:
   - sector
   - country
   - own output/value added response
   - final-demand contribution
   - intermediate-demand contribution
   - if feasible, key source/buyer breakdowns
4. Design and generate a new figure. Preferred target is a readable two-sided transmission chart. Fall back to the clearest valid alternative if a true flowchart becomes too noisy for 44 sectors.
5. Regenerate outputs and verify whether the resulting chart is informative enough for manuscript use.

## Verification

- Run `python new_process.py`
- Inspect the generated benchmark transmission data and figure files
- If the figure is wired into the paper, recompile `0_main.tex`
