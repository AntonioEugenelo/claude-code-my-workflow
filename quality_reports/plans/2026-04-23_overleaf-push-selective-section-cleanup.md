## Objective

Push the current paper changes to Overleaf while keeping Section 4 text unchanged, carrying over the current Section 6 manuscript state, and removing the duplicate section-draft files created during the earlier numbering detour.

## Scope

- Confirm the active manuscript inputs and Overleaf sync status.
- Remove the duplicate local section-draft files that should no longer survive in the working tree.
- Prepare a selective nested-repo commit that includes:
  - Section 4 figure binaries only
  - the current live Section 6 source (`56_sectoral_channels.tex`)
  - the active Section 6 figure exports it references
- Exclude unrelated manuscript edits and exclude the current Section 4 text diff.
- Recompile the manuscript from the paper repo before pushing.
- Push the resulting nested-paper commit to Overleaf.

## Likely Files To Change

- `quality_reports/plans/2026-04-23_overleaf-push-selective-section-cleanup.md`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/55b_sectoral_transmission_decomposition.tex` (delete)
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/56_sectoral_channels_recovered_ae2e56d.tex` (delete)
- `quality_reports/session_logs/2026-04-23_overleaf-push-selective-section-cleanup.md`

## Assumptions

- “The only change in section 4 should be in figures” means the current text diff in `55a_benchmark_and_robustness.tex` should not be committed or pushed.
- “Remove the duplicate old section 5 and section 7” refers to the extra local section-draft files created during the temporary section-renumbering workflow, not to the broader set of historical dead section files still tracked in the paper repo.
- The live Section 6 content to preserve is the current `0_clean/sections/56_sectoral_channels.tex` version already used by `0_main.tex`.

## Verification

- Recompile `master_supporting_docs/Tariffs_ECB/0_clean/0_main.tex` with `latexmk -g -pdf -outdir=build_verify -interaction=nonstopmode -halt-on-error 0_main.tex`.
- Check the staged nested-repo diff to confirm Section 4 contributes figure changes only.
- Check `./scripts/sync-overleaf.sh status` before and after the push.
