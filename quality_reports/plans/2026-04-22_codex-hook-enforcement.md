# Plan: Codex Hook Enforcement

**Date:** 2026-04-22
**Status:** COMPLETED

## Objective

Add real Codex-native hook enforcement for the repository where the current Codex runtime supports it.

Initial enforcement scope:

1. repo-local Codex hook activation via `.codex/config.toml` and `.codex/hooks.json`
2. a `PreToolUse` Bash guardrail for clearly dangerous shell commands
3. a `Stop` hook that enforces active review completeness and unresolved review-conflict state
4. workflow/script updates so reviewer disagreement can be marked and cleared explicitly
5. documentation updates to replace the now-stale "no hook enforcement" claim

## Constraints

- Current Codex hook support is partial.
- Official Codex docs currently say `PreToolUse` and `PostToolUse` only emit `Bash`, while `Write`, `Edit`, MCP, and other tools are not yet intercepted.
- Therefore this change can enforce shell and stop-time workflow policy, but not full Claude-style edit-time enforcement.

## Planned Files

- `.codex/config.toml`
- `.codex/hooks.json`
- `.codex/hooks/pre_tool_use_guard.py`
- `.codex/hooks/stop_review_enforcer.py`
- `scripts/review-mode.sh`
- `docs/codex-workflows/adversarial-review.md`
- `docs/codex-workflows/orchestrator.md`
- `docs/codex-migration.md`
- `README.md`
- `quality_reports/session_logs/2026-04-22_codex-hook-enforcement.md`

## Planned Steps

1. Add repo-local Codex hook config and hook registration.
2. Implement a Bash pre-tool guard that blocks obviously destructive commands.
3. Implement a stop hook that:
   - blocks turn completion when a tracked review round is incomplete
   - blocks turn completion when a tracked reviewer conflict is unresolved
4. Extend `scripts/review-mode.sh` to mark and clear reviewer conflicts.
5. Update workflow docs to explain what is now enforced by hooks versus what remains procedural.
6. Verify by reading back the hook files and running the shell scripts / syntax checks where possible.

## Verification

- Read back `.codex/config.toml` and `.codex/hooks.json`
- Run the Python hook files directly with representative JSON payloads
- Run `bash ./scripts/review-mode.sh` commands for the new conflict state
- Confirm docs no longer claim that Codex has no hook-driven enforcement at all

## Risks

- Hook support in Codex is still marked under development, so the implementation should stay narrow and fail open on internal errors.
- Stop-hook enforcement can become annoying if the continuation prompt loops; the messaging must be targeted and actionable.
- Bash interception is a guardrail, not a perfect containment boundary, because the current runtime does not intercept all shell or non-shell tools.
