# Rerun Gate

Use this workflow before any expensive rerun, regeneration, compilation, or
simulation.

## Required Questions

Answer these before running:

1. Did model code, preprocessing, calibration, source text, or input data change?
2. Are existing outputs stale relative to those inputs?
3. Can the question be answered from existing `.mat`, `.csv`, `.log`, figure, PDF, or HTML outputs?
4. What exact command will run, from which directory?
5. What files should change if the run succeeds?
6. What is the stop condition if the run takes too long?

## Run Card Requirement

Create or update a file under `quality_reports/run_cards/` when the run:

- is expected to take more than 5 minutes,
- overwrites model outputs, figures, PDFs, or tables,
- affects manuscript claims,
- is needed to decide whether a result changed.

## Default Decision

Do not rerun by default. Reuse existing verified outputs unless inputs changed,
outputs are stale, or the user explicitly says to run anyway after the gate is
reported.

## Report Format

Before running, report:

- `rerun_needed`: yes/no/unclear,
- `reason`,
- `command`,
- `expected_outputs`,
- `run_card`,
- `risk`.
