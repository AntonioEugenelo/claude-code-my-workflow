Repository-local Codex support files live here.

- `.codex/state/` is created by helper scripts for local machine state such as Overleaf sync credentials and sync logs.
- `quality_reports/tmp/review_state/` holds writable local review-round enforcement state used by `review-mode.sh` and the Stop hook.
- `.codex/review_agents/` contains the active read-only review-agent prompt cards.
- `.codex/hooks.json` and `.codex/hooks/` contain repo-local Codex hook configuration and hook scripts.
- `.codex/config.toml` enables repo-local Codex features for this repository.
- `.codex/state/` is gitignored.
- `.claude/` remains archived legacy material for migration reference only.
