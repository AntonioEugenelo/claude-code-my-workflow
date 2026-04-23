# Implement-Verify-Review Loop

Codex still relies primarily on an explicit operating procedure. This repository now also includes a narrow layer of repo-local Codex hook enforcement for supported events, but that layer does not replace the main workflow.

## Main Loop

1. Implement the planned changes.
2. Verify the result.
3. Review the changed files using the correct review agents or checks.
4. Fix findings in severity order.
5. Re-verify.
6. Re-review if fixes were material.
7. Report outcome, residual risks, and next steps.

When the user asks for a harsh or adversarial review loop, use the read-only review agents in `review-agents.md` and the procedure in `adversarial-review.md`.

## Verification Requirements

- LaTeX: compile the relevant target and inspect for blocking warnings or obvious output regressions.
- Quarto: render the document or run the relevant render/check command.
- Code: run the relevant script, test, or validation command.
- Data/analysis: confirm that outputs regenerate from source code rather than by hand.
- Documentation-only edits: verify links, commands, and filenames against the repo.

## Review Gates

The authoritative thresholds live in `quality-gates.md`.

- `90/100`: commit-ready production work
- `95/100`: ready for supervisor, collaborator, or peer review
- `98/100`: ready to send, publish, or deploy
- `60/100`: exploratory work in `explorations/`

## Non-Negotiable Rules

- Do not self-score after fixes. Re-run the current review checklist on the current files.
- Do not claim verification without actually running the relevant command or check.
- Do not substitute a prose promise for a compilation, render, or execution check when one is available.
- If verification fails twice for the same reason, stop and report the blocker clearly.
- Review agents are read-only. Spawn them as Codex `explorer` agents only and keep all file edits in the main thread.
- If review-agent sets produce materially incompatible directions, stop and ask the user to choose before implementing more fixes. Do not silently arbitrate between theory, narrative, pedagogy, derivation, or figure priorities when the choice changes the work.
- If review tracking is active, keep the tracking state current. When supported by the client, the Stop hook can enforce missing review passes and unresolved reviewer-conflict state.

## Review Loop Limits

- Use at most 5 fix-review rounds before escalating unresolved issues to the user.
- If a compilation-blocking issue appears, fix that before continuing with qualitative review.
- Use user escalation immediately, not after 5 rounds, when the current blocker is reviewer disagreement rather than implementation difficulty.

## Review Modes

- Quick: typo fix, formatting-only change, or under 5 changed lines. Use a narrow review pass.
- Standard: default for most edits. Review with all relevant review agents or checks for the file type.
- Deep: before submission, external review, or publication. Re-check source fidelity, citations, and generated artifacts.

## Hook Limits

- Repo-local Codex hooks currently provide useful enforcement only for supported runtime events.
- In the current Codex docs, `PreToolUse` and `PermissionRequest` are practical for `Bash`, while `Stop` can enforce end-of-turn workflow state.
- Edit-time enforcement for `Write`, `Edit`, MCP, and other non-shell tools still remains procedural until Codex exposes broader hook coverage.
- The current Codex hook docs also state that Windows support is temporarily disabled, so this repo can be hook-ready before every local Codex client is able to execute the hooks.
