# Long-Run Monitoring

Use `scripts/run_state.py` for long jobs so status is explicit and recoverable.

## Commands

Start a run:

```powershell
python scripts/run_state.py start --name "benchmark-irfs" --command "matlab -batch a0_launch" --run-card quality_reports/run_cards/2026-04-30_benchmark-irfs.md --expected-output master_supporting_docs/MCMS/results/benchmark.mat
```

Update progress:

```powershell
python scripts/run_state.py update --stage "solving model" --message "Dynare finished preprocessing"
```

Show status:

```powershell
python scripts/run_state.py status
```

Finish:

```powershell
python scripts/run_state.py finish --status succeeded --message "Outputs regenerated"
```

## State File

Runtime state is written to ignored `quality_reports/run_state/current.json`.
Long-run logs and generated outputs remain governed by the run card.
