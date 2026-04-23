# Review Routing

Use these routes to choose the right read-only review agents for each document type.

## Routing Table

| Document Type | Path Pattern | Read-Only Review Agents | Default Tier |
| --- | --- | --- | --- |
| Cover letter / proposal | `Letters/**/*.tex` | `proofreader || domain-reviewer || narrative-reviewer -> cover-letter-reviewer` | Standard |
| Beamer slides | `Slides/**/*.tex` | `proofreader || narrative-reviewer -> domain-reviewer` | Standard |
| Quarto slides | `Quarto/**/*.qmd` | `proofreader || narrative-reviewer -> domain-reviewer` | Standard |
| Research paper | `master_supporting_docs/**/*.tex` | `proofreader || derivation-auditor || figure-reviewer -> theory-critic || pedagogical-reviewer || narrative-reviewer` | Deep |
| Journal review / notes | `**/*review*.md`, `**/*review*.xml` | `proofreader -> narrative-reviewer` | Light |
| Exams / problem sets | `**/*exam*.*`, `**/*PSet*.*`, `**/*tutorial*.*` | `proofreader -> domain-reviewer` | Light |
| Documentation | `*.md`, `quality_reports/**/*.md`, `docs/**/*.md` | `proofreader` plus local command/link checks | Quick |
| Code and analysis | `**/*.py`, `**/*.m`, `**/*.R` | `code-critic || code-structurer` | Standard |

## Agent Mapping

- `proofreader`: grammar, typos, terminology consistency, likely overflow
- `domain-reviewer`: factual correctness, substantive assumptions, citation fidelity
- `narrative-reviewer`: flow, framing, transitions, emphasis, audience fit
- `pedagogical-reviewer`: teaching order, signposting, reader burden, one-pass comprehensibility
- `cover-letter-reviewer`: recipient fit, strategic quality, tone, concision
- `derivation-auditor`: mathematical correctness and propagation of assumptions
- `figure-reviewer`: match between code, figure, caption, and manuscript claim
- `theory-critic`: interpretation, assumptions, robustness, literature positioning
- `code-critic`: logic, runtime safety, failure modes, scaling/index risks
- `code-structurer`: organization, naming, cohesion, replication readiness
- `devils-advocate`: adversarial challenge pass for framing, omissions, and weak argument steps

## Review Tier Guidance

- Quick: use only the narrowest relevant review agents.
- Standard: run the full set from the table.
- Deep: run the full set and also compare outputs against supporting source material.
- Adversarial: run the baseline route, then add `devils-advocate` via `adversarial-review.md`.

## Early Stop Rules

- Stop qualitative review if compilation or execution is failing.
- Stop theory review if derivation issues invalidate the argument.
- Stop narrative polish if factual or citation errors remain unresolved.

## Optional Tracking Helper

For multi-pass review work:

- `scripts/review_plan.py` computes the required review agents and waves.
- `scripts/review-mode.sh` records the active review round and completed review agents in `.codex/state/`.

All review agents are read-only and should be spawned as Codex `explorer` agents.
