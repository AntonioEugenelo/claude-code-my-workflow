# MCMS Main-Text Generator Audit

Scope: only code paths needed for main-text numbers and figures. Appendix-only generators are excluded.

Files reviewed:
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py)
- [extract_paper_numbers.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/extract_paper_numbers.py)
- [a1_calibration.m](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/a1_calibration.m)

Evidence:
- [maintext_mcms_evidence.json](C:/CustomTools/claude-code-my-workflow/explorations/full_paper_mcms_audit/output/maintext_mcms_evidence.json)
- direct execution of `python new_process.py`

## Findings

1. High: the active transmission-decomposition path can compute the wrong shock while keeping a plausible sector label.
Location:
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:748)
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3369)
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3417)
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:3896)

What it does:
- `export_standard_jobs_from_mat()` writes `SectorID = 1..20` for tradeable rows
- `extract_benchmark_transmission_decomposition()` renames that local row id to `shock_sector_id`
- `_impact_from_irfs(... shock_sector_id)` then uses that local row id as if it were the global shock id in `varepsilon_tau_*`

Observed emitted evidence:
- `Figure_SingleShock_Transmission_Shocks.csv` contains `shock_sector_id = 6` with `shock_sector = Textiles`
- in the global sector map, global sector `6` is `Metal ores`, while `Textiles` is global sector `9`

What it should do:
- remap the stored row id back to the global tariff-sector id before any shock-key lookup
- keep the display label and the shock identifier as separate fields

Impact:
- active benchmark transmission figures can be computed for the wrong shock while still carrying the expected-looking sector label
- this is a figure-data correspondence bug, not just a naming issue

2. High: the active pipeline has a MATLAB fallback, but it still has no CSV-layer fallback and can abort before the active-paper pass completes.
Location:
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:5031)
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:5039)
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:5466)

What the code does:
- tries direct MAT regeneration
- on failure, tries MATLAB preprocessing
- if both fail, raises and aborts before the final sync/publish stage
- there is no fallback that rebuilds from the already-readable CSV layer

Observed execution result:
- `python new_process.py` fails on `irf_Het_DCP_Baseline.mat`
- the MATLAB fallback also fails on this machine
 
What it should do:
- add a CSV-layer fallback for the active-paper subset, or fail much earlier with a clearer contract about required inputs

Impact:
- the script has a recovery attempt, but not a successful end-to-end recovery path
- active-paper regeneration remains operationally brittle

3. Medium: the active build can silently leave stale or partial paper figures in place.
Location:
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:983)
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:5031)
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:5357)

What the code does:
- `refresh_preprocessed_csvs()` does not verify that the full active-manuscript manifest was rebuilt
- `sync_paper_figures()` copies only sources that exist and logs `[SKIP] Missing paper figure source` for the rest

What it should do:
- fail fast on missing required active outputs
- or explicitly invalidate stale destination files when a required source is missing

Impact:
- the manuscript tree can retain old figures from a previous successful run after a partial failure
- that is a silent reproducibility risk

4. Medium: the pipeline is not anchored to a single project root and mixes replication with publishing side effects.
Location:
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:24)
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:983)
- [new_process.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/new_process.py:5468)

What it does:
- uses cwd-relative core paths such as `OUTPUT_BASE_DIR`, `MAT_DIR`, and `FULL_RESULTS_MAT`
- mixes local regeneration, paper sync, and `upload_to_google_drive()` in one `main()` path

What it should do:
- anchor all file paths to a single project root or script root
- separate replication and publishing into explicit entry points

Impact:
- replication depends too much on the current working directory
- a normal run can unintentionally include network/auth side effects

5. Medium-low: `a1_calibration.m` does not hard-fail after internal consistency violations.
Location:
- [a1_calibration.m](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/a1_calibration.m:105)
- [a1_calibration.m](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/a1_calibration.m:800)

What it does:
- prints `ERROR` messages for failed normalization checks
- still proceeds to save `calib.mat`

Impact:
- downstream code can consume an apparently valid calibration artifact after a failed consistency check

6. Medium-low: `extract_paper_numbers.py` is useful as a scratch audit tool but not as a scoped main-text validator.
Location:
- [extract_paper_numbers.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/extract_paper_numbers.py:1)
- [extract_paper_numbers.py](C:/CustomTools/claude-code-my-workflow/master_supporting_docs/MCMS/extract_paper_numbers.py:132)

What it does:
- prints many relevant benchmark and robustness numbers from the readable CSV layer
- still contains inactive scenario and appendix branches
- computes `top3` for GDP but prints `nsmallest(3, col)` regardless of sign

Impact:
- the helper is fine for manual exploration
- its printed GDP ranking check is unreliable and it is not a clean main-text validation entry point

## Good Practices Worth Preserving

- `get_standard_job_specs()` gives a single visible mapping from figure IDs to MAT inputs and shock pairs
- `create_sectoral_spillover_matrix()` performs internal consistency checks against the benchmark cross-section before exporting the reproducibility CSV
- the readable CSV layer is rich enough to audit most headline main-text numbers even when the benchmark MAT is broken
- `IRFStore` is a good compatibility layer for HDF5 versus classic MAT access
- `cleanup_stale_active_manuscript_outputs()` plus `sync_paper_figures()` gives the pipeline a deliberate publish step

## Overall Code Status

The main-text MCMS layer is analytically rich but operationally fragile. The most serious bug is the local-ID/global-ID confusion in the transmission path. After that, the main risks are brittle recovery behavior, stale-output risk, and replication side effects tied to cwd and publishing hooks.
