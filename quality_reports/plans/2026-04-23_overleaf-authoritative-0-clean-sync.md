# Plan: Overleaf-Authoritative 0 Clean Sync

**Date:** 2026-04-23
**Status:** IN PROGRESS

## Objective

Make the local `master_supporting_docs/Tariffs_ECB/0_clean/` match Overleaf exactly, treating Overleaf as authoritative over the local copy.

## Scope

- Inspect the current local `Tariffs_ECB` repo state and Overleaf sync state.
- Fetch the latest Overleaf commit.
- Replace the local `0_clean/` tree with the Overleaf version.
- Verify that local `0_clean/` matches Overleaf exactly after the replacement.

## Constraints

- Trust Overleaf over local for `0_clean/`.
- Avoid touching unrelated paths in `master_supporting_docs/Tariffs_ECB/` unless required by the sync mechanics.
- Preserve visibility into what changed by checking diffs/status before and after the replacement.

## Likely Files

- `master_supporting_docs/Tariffs_ECB/0_clean/**`
- `quality_reports/plans/2026-04-23_overleaf-authoritative-0-clean-sync.md`
- `quality_reports/session_logs/2026-04-23_overleaf-authoritative-0-clean-sync.md`

## Work Plan

1. Inspect local `Tariffs_ECB` status and Overleaf sync status.
2. Fetch the Overleaf remote state without merging local edits back in.
3. Compare local `0_clean/` against Overleaf `0_clean/`.
4. Replace local `0_clean/` with the Overleaf tree.
5. Verify path-level equality by checking git diff/status against the fetched Overleaf commit.

## Verification

- Successful fetch from Overleaf.
- `git diff --name-status FETCH_HEAD -- 0_clean` or equivalent shows no remaining differences after replacement.
- Local filesystem and git status confirm the local `0_clean/` tree now reflects the Overleaf state.

## Assumptions

- The desired outcome is local alignment to the current Overleaf manuscript, not a bidirectional merge.
- If local-only edits exist inside `0_clean/`, they should be discarded in favor of Overleaf because the user explicitly made Overleaf authoritative.
