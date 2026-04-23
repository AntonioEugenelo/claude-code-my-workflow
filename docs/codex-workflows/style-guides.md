# Style Guides

Use these conventions when the task calls for the repo's established prose voice or analysis/figure style.

## Eugenelo Prose Voice

Apply this voice when the user asks for Eugenelo style, "my writing style", or when revising prose that should sound like Antonio Eugenelo.

Core rules:

- Lead with the claim, not with setup.
- Prefer concrete Anglo-Saxon wording over abstract Latinate phrasing.
- Cut hedges and false intensifiers.
- Put `I` or the true actor in subject position when the prose is personal.
- Vary sentence length; use short anchor sentences to control rhythm.
- Trust the reader; use short transitions and avoid scaffolding.
- Keep the tone formal but warm, closer to seminar prose than to bureaucratic prose.
- Prefer compact possessive attribution (`Kortum's result`, not `the result of Kortum`).

Anti-patterns:

- long preambles before the point
- passive constructions that hide the actor
- uniform sentence length
- doubled connectors and over-signposting
- procedural verbs such as `utilise`, `facilitate`, `undertake` where simple verbs are stronger

Do not force this voice onto technical derivations, code comments, or neutral institutional boilerplate unless the user explicitly asks for it.

## R and Figure Conventions

For `.R` analysis and repo-native figures:

- load packages at the top with `library()`
- call `set.seed()` once when randomness matters
- keep paths relative to the repo root
- create output directories with `dir.create(..., recursive = TRUE)`
- document functions and use clear `snake_case` names
- keep comments focused on why, not what

Preferred palette:

```r
primary_blue   <- "#003299"
primary_gold   <- "#FFD700"
accent_orange  <- "#FF6600"
positive_green <- "#009900"
negative_red   <- "#B91C1C"
```

Figure defaults:

- use transparent backgrounds when figures are meant for slides
- set explicit export dimensions
- save heavy intermediate objects as `.rds` rather than recomputing silently
- keep style choices consistent across manuscript, slides, and analysis outputs
