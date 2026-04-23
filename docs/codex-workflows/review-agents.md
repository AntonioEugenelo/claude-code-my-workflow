# Review Agents

The active Codex branch uses explicit review agents again, not just abstract lenses.

These agents are the closest Codex-native replacement for the old Claude review subagents.

## Non-Negotiable Rule

Every review agent is read-only.

- Spawn review agents as Codex `explorer` agents only.
- Do not assign a write scope.
- Do not ask review agents to patch files.
- The main agent performs fixes after integrating the findings.
- Reviewer scores come from the review agents. The main agent does not self-score the work.

## Active Prompt Cards

The active prompt cards live under `.codex/review_agents/`.

| Review Agent | Active Prompt Card | Primary Job |
| --- | --- | --- |
| `proofreader` | `.codex/review_agents/proofreader.md` | language, typos, consistency, likely overflow |
| `narrative-reviewer` | `.codex/review_agents/narrative-reviewer.md` | story, flow, audience, confusion points |
| `pedagogical-reviewer` | `.codex/review_agents/pedagogical-reviewer.md` | teaching order, signposting, reader burden, one-pass comprehensibility |
| `theory-critic` | `.codex/review_agents/theory-critic.md` | hostile theory ref report |
| `derivation-auditor` | `.codex/review_agents/derivation-auditor.md` | line-by-line mathematical verification |
| `figure-reviewer` | `.codex/review_agents/figure-reviewer.md` | figure/text/data consistency |
| `domain-reviewer` | `.codex/review_agents/domain-reviewer.md` | substantive correctness |
| `cover-letter-reviewer` | `.codex/review_agents/cover-letter-reviewer.md` | strategic letter quality |
| `code-critic` | `.codex/review_agents/code-critic.md` | adversarial computational audit |
| `code-structurer` | `.codex/review_agents/code-structurer.md` | replication-package clarity |
| `devils-advocate` | `.codex/review_agents/devils-advocate.md` | targeted adversarial challenge pass |

## Lens Mapping

The older Claude names are preserved because they remain useful shorthand:

| Lens | Review Agent |
| --- | --- |
| `proofreader` | `proofreader` |
| `domain` | `domain-reviewer` |
| `narrative` | `narrative-reviewer` |
| `pedagogy` | `pedagogical-reviewer` |
| `letter-quality` | `cover-letter-reviewer` |
| `derivation` | `derivation-auditor` |
| `figure-consistency` | `figure-reviewer` |
| `theory` | `theory-critic` |
| `correctness` | `code-critic` |
| `structure` | `code-structurer` |

## Conflict Signaling

Review agents should surface material cross-agent conflicts explicitly rather than assuming their own lens takes priority.

Examples:

- `narrative-reviewer` wants a shorter, cleaner exposition but `theory-critic` requires caveats that materially change the framing
- `pedagogical-reviewer` wants more setup while `narrative-reviewer` wants compression that would remove it
- `figure-reviewer` or `derivation-auditor` objects to a simplification that a prose-focused reviewer prefers

When those conflicts would change implementation direction, the main agent should stop the review loop and ask the user to choose which direction to privilege before editing further.

## Execution Rule

Use `scripts/review_plan.py` to determine the required review agents, execution waves, and round-one-only reviewers for a given target.

Use `scripts/review-mode.sh` to track which review agents have been completed in the current round.
