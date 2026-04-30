Active Codex review-agent prompt cards live here.

- These files are the active replacement for the old `.claude/agents/` review layer.
- Spawn every review agent as a read-only Codex `explorer` agent.
- Review agents never edit files and never own a write scope.
- Their only output is findings, questions, and report text saved by the main agent.
- Active cards currently include `proofreader`, `derivation-auditor`, `figure-reviewer`, `theory-critic`, `pedagogical-reviewer`, `narrative-reviewer`, `devils-advocate`, and the specialized domain/code reviewers.
