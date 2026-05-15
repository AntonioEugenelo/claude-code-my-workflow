# Writing Style: Fiscal-LPT Cochrane-Informed Economics Prose

Activate this rule for all Fiscal-LPT paper drafting and revision. It is a
project-specific style rule derived from `docs/codex-workflows/fiscal-lpt-writing-style.md`.

## Core Rule

Write Fiscal-LPT paper text as clear economics prose: puzzle first, mechanism
second, result third, implication last. Use Cochrane's papers as evidence for
high-level rhythm and argumentative structure, not for sentence copying or
verbal imitation.

## Targets

- Average sentence length in non-technical prose: 17-22 words.
- Median sentence length: 15-19 words.
- Short anchor sentences: one fifth to one third of sentences.
- Long sentences: reserve for mechanisms; split if they carry more than one
  claim and one caveat.
- Paragraphs: one claim each, usually 120-300 words.

## Required Paragraph Order

1. Claim, puzzle, or friction.
2. Mechanism.
3. Model object, equation, calibration fact, or result.
4. Economic interpretation.
5. Link to the next step.

## Fiscal-LPT Content Order

- State the economic problem before notation.
- Introduce taxes, subsidies, public debt, and fiscal feedback rules by role.
- Tie each new fiscal object to the MCMS implementation step that makes it run.
- Use generated outputs only after the relevant mechanism is clear.
- Do not present code changes as contributions unless the paper states the
  economic claim they make testable.

## Diction

Prefer: `show`, `ask`, `rule out`, `pin down`, `raise`, `lower`, `move`,
`fit`, `fail`, `matter`, `channel`, `mechanism`, `puzzle`, `force`, `sign`,
`timing`.

Avoid: `utilize`, `facilitate`, `undertake`, `operationalize`, `substantially`,
`primarily`, `notably`, `interestingly`, `it is important to note`, `the
analysis proceeds by`.

## Non-Negotiables

- Do not narrate figures or scripts panel by panel.
- Do not overclaim beyond MCMS code, calibration, or generated outputs.
- Do not copy phrases from the supporting Cochrane PDFs.
- Do not add paper-facing material to `../MCMS-private`; keep paper source in
  `../Fiscal-LPT` and writing-direction material in this workflow repo.
