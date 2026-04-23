Date: 2026-04-18

Status: In Progress

## Goal

Draft a standalone evidence-backed memo that explains how to address the current Tariffs ECB action points, with every substantive claim tied to numerical evidence or concrete file-level support, then run a full adversarial review loop on that memo.

## Scope

Primary targets:

- one new standalone memo file
- review artifacts under `quality_reports/reviews/`
- session log for this task

Evidence sources:

- `quality_reports/session_logs/2026-04-18_overleaf-jose-elias-action-points.md`
- `master_supporting_docs/Tariffs_ECB/0_clean/sections/*.tex`
- `master_supporting_docs/MCMS/new_process.py`
- `master_supporting_docs/MCMS/a1_calibration.m`
- existing generated appendix/table outputs where relevant

## Non-Goals

- No manuscript text changes in the paper itself.
- No figure regeneration or design edits to the active manuscript outputs.
- No resolution of the underlying benchmark IRF corruption unless it blocks the memo.

## Assumptions

- “All the action points” means the previously enumerated Jose Elias follow-ups plus the three additional user-specified action points about Figure 1, Sections 4.1.1/4.1.2, and the EA/household dynamics narrative.
- A markdown memo is acceptable as the requested separate file.
- The adversarial review should follow the repo’s review-agent workflow, with read-only agents and on-disk review artifacts.

## Planned Changes

1. Collect the exact action-point list and map each item to concrete source files.
2. Gather numerical/documentary evidence for each item from manuscript sections, code, and generated outputs.
3. Draft the memo with numbered action points, recommended fixes, evidence, and explicit support for every claim.
4. Run the adversarial review loop on the memo using review agents and save findings to `quality_reports/reviews/`.
5. Fix any issues identified by the review agents and rerun the required agents if needed.

## Verification

- The memo exists on disk and covers each action point explicitly.
- Every substantive claim in the memo cites a file, line, count, or numerical value.
- Review artifacts from the adversarial loop are saved on disk.
- The final memo reflects any material review findings that needed correction.
