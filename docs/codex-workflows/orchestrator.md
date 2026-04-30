# Implement-Verify-Review Loop

This repository uses active Codex hooks where the installed Codex runtime supports them, but the orchestrator remains an explicit operating procedure. Hooks are reminders and mechanical checks; they do not replace verification, review, or session logging.

## Main Loop

1. Implement the planned changes.
2. Verify the result.
3. Review the changed files using the correct lenses.
4. Fix findings in severity order.
5. Re-verify.
6. Re-review if fixes were material.
7. Report outcome, residual risks, and next steps.

## Verification Requirements

- LaTeX: compile the relevant target and inspect for blocking warnings or obvious output regressions.
- Quarto: render the document or run the relevant render/check command.
- Code: run the relevant script, test, or validation command.
- Data/analysis: confirm that outputs regenerate from source code rather than by hand.
- Documentation-only edits: verify links, commands, and filenames against the repo.
- Long or output-overwriting runs: apply `docs/codex-workflows/rerun-gate.md` and create/update a run card first.
- Result audits: use a claim ledger from `quality_reports/claim_ledgers/` rather than global memory.

## Review Gates

- `90/100`: commit-ready production work
- `95/100`: ready for supervisor, collaborator, or peer review
- `98/100`: ready to send, publish, or deploy
- `60/100`: exploratory work in `explorations/`

## Non-Negotiable Rules

- Do not self-score after fixes. Re-run the current review checklist on the current files.
- Do not claim verification without actually running the relevant command or check.
- Do not substitute a prose promise for a compilation, render, or execution check when one is available.
- If verification fails twice for the same reason, stop and report the blocker clearly.

## Active Hook Support

- `PostToolUse`: context monitoring and verification reminders.
- `SessionStart[resume]`: context restore from recent plans/session logs.
- `Stop`: session-log reminder.
- `Stop`: workflow-drift reminders for missing decision locks, missing source authority, and running jobs without run cards.
- No exact Codex equivalent is currently wired for Claude `Notification` or `PreCompact`; use explicit checkpointing before compaction-sensitive handoffs.

## Review Loop Limits

- Use at most 5 fix-review rounds before escalating unresolved issues to the user.
- If a compilation-blocking issue appears, fix that before continuing with qualitative review.

## Review Modes

- Quick: typo fix, formatting-only change, or under 5 changed lines. Use a narrow review pass.
- Standard: default for most edits. Review with all relevant lenses for the file type.
- Deep: before submission, external review, or publication. Re-check source fidelity, citations, and generated artifacts.
