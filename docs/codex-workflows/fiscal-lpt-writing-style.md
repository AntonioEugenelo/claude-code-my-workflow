# Fiscal-LPT Writing Style

Use this workflow whenever drafting or revising text for the Fiscal-LPT paper.
It combines the Harvard economics writing guide in `docs/supporting_docs/Writing-guide.pdf`
with a high-level style profile extracted from the Cochrane papers in the same
folder. It should guide structure, rhythm, and review standards without copying
phrasing from the source papers.

## Source Corpus

- `Writing-guide.pdf`: economics-writing principles, paper organization,
  clarity, evidence, results exposition, citation discipline, and revision.
- `320201.email.pdf`: Cochrane, stable quiet inflation at the zero bound.
- `steppingonarake.pdf`: Cochrane, fiscal theory of monetary policy.
- `zero_bound_elsarticle-revised.pdf`: Cochrane, New-Keynesian liquidity trap.

## Extracted Metrics

Measured from local PDF text extraction on 2026-05-12.

| Source | Pages | Mean sentence words | Median | Short sentences <=10 words | Long sentences >=30 words | Questions | Semicolon sentences |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Cochrane zero-bound chapter | 114 | 20.3 | 18 | 20% | 18% | 62 | 36 |
| Cochrane fiscal-theory paper | 55 | 20.3 | 18 | 21% | 18% | 7 | 15 |
| Cochrane liquidity-trap paper | 43 | 18.3 | 15 | 30% | 15% | 9 | 6 |
| Harvard writing guide | 41 | 19.9 | 18 | 23% | 18% | 48 | 30 |

Target range for Fiscal-LPT prose:

- Average sentence length: 17-22 words in non-technical prose.
- Median sentence length: 15-19 words.
- Short anchor sentences: roughly one fifth to one third of sentences.
- Long technical sentences: acceptable, but keep them under one fifth of the
  paragraph unless an equation or mechanism requires it.
- Paragraphs: normally 120-300 words; split earlier when the claim changes.
- Questions: use sparingly to name a puzzle or tension, not as decoration.
- Semicolons: allowed when they compress a tight logical relation; avoid serial
  semicolon chains.

## Writing-Guide Principles

1. State the research question early and plainly.
2. Organize the paper around an argument, not around a chronology of work done.
3. Build every section from claim, model or evidence, interpretation, and payoff.
4. Use an outline before drafting; each paragraph should have one job.
5. Prefer clear, direct prose over ornate academic phrasing.
6. Use active verbs and concrete subjects where possible.
7. Omit needless words and revise until the point is carried by the fewest words
   that do not sacrifice precision.
8. Present only results that speak to the paper's question.
9. When discussing tables, figures, or simulations, guide the reader to the key
   comparison first; do not narrate every number.
10. Be honest about mixed evidence. If results are partial, say which margin
    works, which does not, and why that is still informative.
11. Keep citations consistent and attached to claims they actually support.
12. In theory sections, pair mathematical objects with plain economic intuition.

## Cochrane-Informed Style Profile

Use this as a high-level model of argument and rhythm.

### Argument Order

- Start from a fact, puzzle, or paradox.
- Name what standard theory predicts.
- State what the fact does or does not do to that prediction.
- Present the mechanism in a stripped-down model before adding details.
- Return to the empirical or policy puzzle after the equations.
- Make the reader see why the sign, timing, or equilibrium selection matters.

### Paragraph Shape

Default paragraph pattern:

1. Short claim or puzzle.
2. Mechanism in one or two sentences.
3. Equation, model implication, or calibrated result.
4. Interpretation in plain language.
5. Link to the next step.

Results paragraph pattern:

1. Big-picture statement of what the result shows.
2. The one comparison that matters.
3. Magnitudes only after the comparison is named.
4. Explanation of the economic force.
5. Caveat or implication.

### Sentence Rhythm

- Mix short declarative sentences with longer mechanism sentences.
- Let short sentences carry reversals, conclusions, and puzzles.
- Use `But` and `Thus` when they do real argumentative work.
- Avoid strings of uniformly medium-length sentences.
- Do not bury the verb behind nominalizations.

### Syntax Preferences

- Prefer subject-verb-object order.
- Prefer named actors: model, household, government, firm, central bank, tariff,
  subsidy, fiscal rule.
- Use first person sparingly in the paper; it can appear in framing passages, but
  most Fiscal-LPT text should use the paper, model, or mechanism as the subject.
- Put equations after the verbal question they answer.
- Keep definitions close to first use.

### Lexical Preferences

Prefer:

- `show`, `ask`, `rule out`, `pin down`, `raise`, `lower`, `move`, `break`,
  `fit`, `fail`, `matter`, `channel`, `mechanism`, `puzzle`, `force`, `sign`,
  `timing`, `selection`

Avoid unless technically needed:

- `utilize`, `facilitate`, `undertake`, `operationalize`, `substantially`,
  `primarily`, `notably`, `interestingly`, `it is important to note`, `the
  analysis proceeds by`

## Fiscal-LPT Adaptation

The paper is about adding fiscal variables and fiscal-rule steps to the MCMS
model. Therefore every prose pass must preserve three boundaries:

- The paper repo `../Fiscal-LPT` holds only Overleaf/paper source.
- The model repo `../MCMS-private` holds code, calibration, runtime artifacts,
  and generated model outputs.
- This workflow repo holds writing guides, style sources, review prompts,
  planning notes, and writing-direction materials.

Paper prose should frame the project as a model extension:

- Start with the economic problem fiscal variables solve in MCMS.
- Explain why the current MCMS model needs explicit taxes, subsidies, debt, and
  fiscal feedback rules.
- Introduce fiscal variables by economic role before notation.
- Tie each added block to a model step: declaration, calibration, equation
  construction, scenario run, and output interpretation.
- Separate implementation facts from paper claims. A code change is not itself a
  contribution unless the paper explains the economic mechanism it enables.

## Review Checklist

Before accepting paper text, check:

- Does the opening paragraph state the puzzle and contribution without throat
  clearing?
- Does every paragraph lead with a claim, not a figure/table reference?
- Are model variables introduced by role before symbol?
- Are fiscal rules explained through budget logic and incentives, not just
  equations?
- Are results ordered by economic mechanism rather than by file, script, or panel?
- Are sentence lengths varied enough to avoid a flat 20-word rhythm?
- Are any Cochrane-like moves used at the level of structure only, without
  copied sentences or verbal imitation?
- Are claims traceable to `../MCMS-private` code, generated outputs, or cited
  papers?
