---
description: Always verify the logic and accuracy of user requests before executing. Surface incongruences and ask for clarification rather than proceeding with flawed assumptions.
---

# Verify Before Executing

**Before acting on any user instruction, verify that the request is internally consistent and factually accurate.**

## What to Check

1. **Logical consistency** — Does the request contradict itself? Do the stated goals conflict with the stated approach?
2. **Factual accuracy** — Are the papers, theorems, equations, or methods the user references real and correctly described?
3. **Codebase consistency** — Does the request match the actual state of the files? (e.g., "modify function X in file Y" — does X exist in Y?)
4. **Mathematical correctness** — Are the derivations, assumptions, or formulas the user provides correct?
5. **Feasibility** — Can the request actually be accomplished as described, or does it require steps the user may not have considered?

## When You Find Issues

**Do NOT silently proceed with your best guess.** Instead:

1. State what you found: the specific incongruence, error, or ambiguity
2. Show the conflicting evidence (e.g., "You referenced Proposition 3 of Smith (2020), but that proposition states X, not Y")
3. Propose a clarification question or suggest the most likely intended meaning
4. Wait for the user to confirm before proceeding

## Examples

- User says "log-linearize the Euler equation from slide 5" but slide 5 has a budget constraint → flag it
- User references a paper's result incorrectly → show the actual result and ask which version to use
- User asks to modify a function that doesn't exist in the specified file → report what's actually there
- User provides an equation with a sign error or missing term → point it out before building on it

## Exceptions

- **Trivial/obvious requests** (e.g., "fix the typo on line 12") do not need pre-verification
- **Exploratory requests** (e.g., "try approach X and see if it works") can proceed without full verification, but note concerns upfront
