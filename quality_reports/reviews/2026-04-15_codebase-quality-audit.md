# Codebase Quality Audit

Date: 2026-04-15

## Scope

Audit across the root repository plus nested `master_supporting_docs/MCMS` and `master_supporting_docs/Tariffs_ECB`, excluding `.tex` and `.mod` files. Focus was narrowed to maintained source:

- `scripts/`
- `.claude/hooks/`
- `guide/workflow-guide.qmd`
- `guide/custom.scss`
- `master_supporting_docs/MCMS` top-level `.m` / `.py`
- `master_supporting_docs/MCMS/functions/solve_fixed_point.m`
- `master_supporting_docs/MCMS/run_benchmark_irf_export.m`
- `master_supporting_docs/Tariffs_ECB/0_clean/run_horse_race_appendix.py`
- `master_supporting_docs/Tariffs_ECB/0_clean/run_stacked_regressions.py`

Generated/runtime surfaces such as `.git/`, `__pycache__/`, `build_verify/`, `output_*`, Dynare-generated `dynare_files/+b0_main`, and bytecode outputs were treated as noise unless needed as evidence.

## Agent Coverage

1. Deduplication / DRY
2. Type definition consolidation
3. Unused code
4. Circular dependencies
5. Weak typing
6. Try/catch and defensive programming
7. Deprecated / legacy / fallback code
8. AI slop / stubs / low-value comments

## High-Confidence Findings

### 1. Deduplication / DRY

- High: MCMS MATLAB runners duplicate the same scenario-run skeleton across `a0_launch.m`, `a0_launch_missing.m`, `a0_rerun_DCP.m`, `a0_rerun_remaining.m`, and `run_benchmark_irf_export.m`.
- High: `master_supporting_docs/MCMS/new_process.py` carries overlapping orchestration in `legacy_main()` and `main()`.
- High: `master_supporting_docs/Tariffs_ECB/0_clean/run_horse_race_appendix.py` substantially duplicates and supersedes `run_stacked_regressions.py`.
- Medium-high: review-routing state and logic are duplicated across `scripts/review_plan.py`, `scripts/review-mode.sh`, `.claude/hooks/review-completeness-check.py`, and `.claude/hooks/review-agent-tracker.py`.
- Medium: `.claude/hooks/*` repeats session/cache path helpers across multiple files.
- Medium: Overleaf sync logic is split across `scripts/sync-overleaf.sh`, `scripts/sync_to_overleaf.sh`, and `.claude/hooks/overleaf-first-edit-sync.py`.

### 2. Type Definition Consolidation

- High: figure-job and scenario-job manifests are duplicated in both MATLAB and Python: `a2_preprocessing.m` and `new_process.py`.
- High: model run/config shapes recur across `a0_launch.m`, `a0_rerun_DCP.m`, `a0_rerun_remaining.m`, and `run_benchmark_irf_export.m`.
- High: economic registries are redefined across repos with drift (`ROW` vs `RoW`, sector lists, structural indices) in `new_process.py`, `run_horse_race_appendix.py`, `run_stacked_regressions.py`, and `a2_ecb.m`.
- High: benchmark cross-section and regression dataset schemas are only implicit, but are reused across `new_process.py`, `run_horse_race_appendix.py`, and `extract_paper_numbers.py`.
- Medium-high: review/routing/threshold contracts are duplicated between active scripts and legacy hooks.

### 3. Unused / Dead / Orphaned Code

- High: `master_supporting_docs/Tariffs_ECB/0_clean/run_stacked_regressions.py` appears dead/superseded.
- High: `master_supporting_docs/MCMS/a2_ecb.m` appears archival rather than active pipeline code.
- High: `master_supporting_docs/MCMS/a0_rerun_DCP.m`, `a0_rerun_nomonpol.m`, and `a0_rerun_remaining.m` look like one-off rerun helpers.
- Medium-high: `master_supporting_docs/MCMS/a0_launch_missing.m` appears to be a recovery-only launcher.
- Medium: `scripts/extract_citations.py` and `scripts/find_bib_entries.py` appear orphaned and undocumented.

### 4. Circular Dependencies

- Medium: one real cross-repo data loop exists around `horse_race_stacked_160.csv`.
  - `run_horse_race_appendix.py` reads MCMS outputs and writes the CSV.
  - `new_process.py` reads that CSV back into MCMS figures.
- Low: `.claude` review hooks and compaction hooks form benign event/state loops, not harmful architectural cycles.
- Low: no important Python import cycles were found in maintained source.
- Low: no meaningful MATLAB call cycles were found; the main issue there is hidden workspace coupling, not cyclic calls.

### 5. Weak Types

- High: `new_process.py` passes major payloads as anonymous nested dicts rather than typed contracts.
- High: standard/scenario jobs in `new_process.py` are raw list-of-dict specs.
- High: `run_horse_race_appendix.py` uses surface annotations but still returns many stable result payloads as plain dicts.
- High: MATLAB equivalents of weak typing appear in partial config structs, dynamic field access, and cell-wrapped tuple-ish values across `a0_launch.m`, `run_benchmark_irf_export.m`, and `a2_preprocessing.m`.
- Medium: `scripts/quality_score.py` and `scripts/review_plan.py` use generic `dict` for stable orchestration payloads.
- Medium: `.claude/hooks/*` deserialize state JSON into plain dicts with known shapes.

### 6. Defensive Programming / Try-Catch

- High: `.claude/hooks/review-agent-tracker.py` uses `try/except Exception: pass`.
- High: `.claude/hooks/log-reminder.py` fail-opens with broad `except Exception: sys.exit(0)`.
- High: `.claude/hooks/overleaf-first-edit-sync.py` suppresses broad failures and may mark a session as synced before success.
- Medium-high: `scripts/sync_to_docs.sh` suppresses Quarto render failures with `|| echo`.
- Medium-high: `master_supporting_docs/MCMS/a2_preprocessing.m` has three broad `catch` blocks around structural reshaping and then continues.
- Medium: several MCMS launcher/rerun scripts catch any `ME`, log it, and continue, which risks incomplete result sets.
- Preserve: `run_benchmark_irf_export.m` uses boundary-guard `try/catch` with `rethrow(ME)`, which is justified.

### 7. Deprecated / Legacy / Fallback Code

- High: `.claude/hooks` review path conflicts with the Codex-first review path.
- High: `scripts/sync_to_overleaf.sh` and `.claude/hooks/overleaf-first-edit-sync.py` look like older redundant sync paths beside `scripts/sync-overleaf.sh`.
- High: `new_process.py` explicitly carries `legacy_main()`.
- High: `run_stacked_regressions.py` appears superseded by `run_horse_race_appendix.py`.
- Medium-high: the MCMS launcher family is partly redundant and likely mixes active vs legacy responsibilities.

### 8. AI Slop / Stubs / Comment Noise

- High: `guide/workflow-guide.qmd` still carries a lot of migration narrative that belongs in `docs/codex-migration.md`.
- High: `guide/custom.scss` contains a diary-style WIP banner.
- High: `.claude/hooks/*` docstrings still contain legacy vendor/runtime chatter rather than concise behavioral documentation.
- High: `new_process.py` still exposes `legacy`, `fallback`, and `[DEPRECATED]` narration in the active pipeline.
- Medium: `a0_rerun_nomonpol.m` begins with timestamped work-log commentary that belongs in git/session logs, not durable source.

## Cross-Cutting Assessment

The repository’s largest quality problem is not syntax or explicit type misuse. It is duplicated orchestration and duplicated contracts:

- duplicated run manifests and scenario specs
- duplicated review/sync control planes (`.claude` vs Codex-first scripts)
- duplicated regression and figure-generation paths across MCMS and Tariffs_ECB
- implicit, schema-less data contracts reused across repos

The second-largest problem is legacy retention:

- `legacy_main()` in active MCMS code
- superseded `run_stacked_regressions.py`
- extra rerun/recovery scripts left in the main source surface
- migration narrative left in guide/style files

The third-largest problem is fail-open operational code in the legacy hook layer.

## Recommended Cleanup Order

1. Decide whether `.claude/` is archived or still live. If archived, remove or quarantine its hooks and make `.codex` + `scripts/` authoritative.
2. Collapse Overleaf/review orchestration to one path each.
3. Remove or wrap `legacy_main()` and superseded `run_stacked_regressions.py`.
4. Break the MCMS <-> Tariffs_ECB data cycle around `horse_race_stacked_160.csv`.
5. Introduce a small shared contracts layer:
   - `economic_registry`
   - `run_config` / `scenario_spec`
   - benchmark CSV / cross-section schemas
6. Refactor MCMS MATLAB runners to a single scenario runner with thin entry scripts.
7. Replace fail-open catches with explicit, boundary-aware error handling.
8. Strip migration/work-log narration from guide/style/comments after the architecture is simplified.

## Suggested Implementation Workstreams

- Workstream A: control-plane cleanup
  - retire `.claude` review/sync hooks or migrate the useful pieces
  - make `scripts/review_plan.py`, `scripts/review-mode.sh`, and `scripts/sync-overleaf.sh` canonical

- Workstream B: MCMS pipeline cleanup
  - factor shared MATLAB runner logic
  - remove or archive one-off rerun launchers
  - collapse `legacy_main()` / `main()`
  - formalize typed payloads and job specs in `new_process.py`

- Workstream C: Tariffs_ECB analysis cleanup
  - retire `run_stacked_regressions.py`
  - extract shared regression helpers from `run_horse_race_appendix.py`
  - formalize result types / schema checks

- Workstream D: docs/comment cleanup
  - move migration narrative out of `guide/workflow-guide.qmd`
  - remove WIP diary comments and stale work-log notes

## Confidence / Limitations

- High confidence on duplication, superseded scripts, and weak-contract findings.
- Medium confidence on dead-code candidates that may still be used manually outside tracked references.
- Tool-style checks (`knip`, `madge`) were approximated with static repo inspection because this workspace does not expose a native Node tooling surface.
- No code changes were made in this audit pass.
