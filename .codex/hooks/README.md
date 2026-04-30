# Active Hook Parity

Claude Code hooks remain under `.claude/hooks/` and are preserved as the
canonical legacy reference. Codex hook commands are actively registered in
`.codex/config.toml` for the Codex events supported by the installed runtime.

## Active Codex Hooks

| Claude behavior | Codex event | Codex handler | Status |
| --- | --- | --- | --- |
| `PostToolUse[Bash|Task]` context monitor | `PostToolUse` | `.codex/hooks/context-monitor.py` | Active, broadened to all Codex tools |
| `PostToolUse[Write|Edit]` verify reminder | `PostToolUse` | `.codex/hooks/verify-reminder.py` | Active, extracts direct file paths and Codex apply-patch paths |
| `SessionStart[resume]` context restore | `SessionStart[resume]` | `.codex/hooks/post-compact-restore.py` | Active for resume |
| `Stop` session-log reminder | `Stop` | `.codex/hooks/log-reminder.py` | Active |
| Workflow-drift reminders | `Stop` | `.codex/hooks/log-reminder.py` | Active for missing decision locks, missing source authority, and running jobs without run cards |

## Unsupported Exact Events

The installed Codex runtime exposes `PreToolUse`, `PermissionRequest`,
`PostToolUse`, `SessionStart`, `UserPromptSubmit`, and `Stop`. It does not
expose exact equivalents for Claude's `Notification` or `PreCompact` events.

Because of that:

- notification behavior remains a Claude-only hook unless Codex adds a matching event;
- pre-compact state capture remains an explicit checkpoint/session-log workflow in Codex;
- post-compact restore is only active on Codex `SessionStart` with `source = "resume"`;
- verification and session-log reminders still remain explicit obligations in `AGENTS.md`.

The Python hook scripts use shared helpers that tolerate `CLAUDE_PROJECT_DIR`, `CODEX_PROJECT_DIR`, or the current working directory. Codex runtime state is written to ignored files under `quality_reports/hook_state/`.
