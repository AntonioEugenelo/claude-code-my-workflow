# Review Routing

Use these lenses to choose the right review pass for each document type. In Codex, these are review roles and checklists, not runtime-bound subagents.

## Routing Table

| Document Type | Path Pattern | Review Lenses | Default Tier |
| --- | --- | --- | --- |
| Cover letter / proposal | `Letters/**/*.tex` | proofreader, domain, narrative, letter-quality | Standard |
| Beamer slides | `Slides/**/*.tex` | proofreader, narrative, domain, layout | Standard |
| Quarto slides | `Quarto/**/*.qmd` | proofreader, narrative, domain, layout | Standard |
| Research paper | `master_supporting_docs/**/*.tex` | proofreader, derivation, figure-consistency, theory, narrative | Deep |
| Journal review / notes | `**/*review*.md`, `**/*review*.xml` | proofreader, narrative | Light |
| Exams / problem sets | `**/*exam*.*`, `**/*PSet*.*`, `**/*tutorial*.*` | proofreader, domain | Light |
| Documentation | `*.md`, `quality_reports/**/*.md`, `docs/**/*.md` | proofreader, command-check, link-check | Quick |
| Code and analysis | `**/*.py`, `**/*.m`, `**/*.R` | correctness, structure, reproducibility | Standard |

## Lens Definitions

- `proofreader`: grammar, typos, terminology consistency, missing words
- `domain`: factual correctness, notation, citations, field-specific claims
- `narrative`: flow, framing, transitions, emphasis, audience fit
- `letter-quality`: recipient-specific fit, credibility, tone, missing evidence
- `layout`: overflow, spacing, density, readability, visual consistency
- `derivation`: mathematical correctness and propagation of assumptions
- `figure-consistency`: match between code, figure, caption, and manuscript claim
- `theory`: interpretation, assumptions, robustness, literature positioning
- `command-check`: commands in docs match the repo and current filenames
- `link-check`: internal references and paths resolve
- `correctness`: logic, runtime safety, failure modes
- `structure`: organization, naming, cohesion, maintainability
- `reproducibility`: paths, seeds, generated outputs, dependency assumptions

## Review Tier Guidance

- Quick: use only the narrowest relevant lenses.
- Standard: run the full set from the table.
- Deep: run the full set and also compare outputs against supporting source material.

## Early Stop Rules

- Stop qualitative review if compilation or execution is failing.
- Stop theory review if derivation issues invalidate the argument.
- Stop narrative polish if factual or citation errors remain unresolved.
