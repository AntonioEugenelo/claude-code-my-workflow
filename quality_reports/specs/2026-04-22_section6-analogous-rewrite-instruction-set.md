# Requirements Specification: Section 6 Analogous Rewrite Instruction Set

**Date:** 2026-04-22
**Status:** ACTIVE

---

## Objective

Produce an analogous rewrite of active Section 6 by imitating the structural transformation that Jose-Elias Gallegos applied when rewriting the old Section 4 into the new Section 4.

This document is designed as a standalone handoff artifact for another Codex session. It should be sufficient even if that later session has no access to the original search path or chat context.

---

## Source Basis

The instruction set below is derived from the following concrete manuscript evidence:

- Nested paper repo: `master_supporting_docs/Tariffs_ECB`
- Key Jose commit: `bc1454ed5651bf1348a45f82cbc05294f87370aa` dated 2026-04-21
- Main transformed file: `0_clean/sections/55a_benchmark_and_robustness.tex`
- Comparison baseline: the old Section 4 text preserved inside that same committed file under `\section{old}`
- Companion file check: `0_clean/sections/56_sectoral_channels.tex` changed only trivially in the same commit, so the rewrite logic comes overwhelmingly from `55a_benchmark_and_robustness.tex`

Interpretation: the reusable pattern is not "move lots of text across files." The reusable pattern is "reframe one section from panel-by-panel descriptive prose into a claim-driven economic argument."

---

## Core Diagnosis

Old Section 4 had these traits:

- Generic section title: `Quantitative results`
- Organization around figure panels and variable blocks
- Heavy use of point estimates early in paragraphs
- Mixed explanatory levels: results, accounting, institutional assumptions, and caveats interleaved
- EA discussion treated mainly as another result paragraph

New Section 4 had these traits:

- Section title names the economic object: `Aggregate transmission of a US--China tariff war`
- Opening triad: motivating questions, preview facts, roadmap
- Main body organized by economic logic rather than by figure panel order
- Clear separation between "what happens" and "why it happens"
- Near-zero EA result reframed as an offsetting-margins problem
- Robustness used to reinforce the main thesis rather than generate a parallel thesis
- End-of-section bridge explicitly motivates the next section

---

## Non-Negotiable Rewrite Rules

### 1. Rename the section around the phenomenon, not around generic output

Do not use titles like `Results`, `Quantitative Results`, `Additional Evidence`, or similar placeholders.

The title of Section 6 should identify the actual economic object being interpreted.

Model example from Jose:

- Old: `\section{Quantitative results}`
- New: `\section{Aggregate transmission of a US--China tariff war}`

Rule for Section 6:

- Name Section 6 after the mechanism, transmission object, decomposition object, or comparison object it actually studies.

### 2. Begin with an opening scaffold before any deep detail

The first three paragraphs should do three distinct jobs:

1. State the question set the section answers.
2. State the main preview facts or asymmetries.
3. State the roadmap of the section.

Do not open with raw numbers or by walking the reader straight into a figure.

Model example from Jose:

- Paragraph 1: three questions
- Paragraph 2: three broad facts
- Paragraph 3: section roadmap

### 3. Reorganize by economic logic, not by panel order

If the current Section 6 is structured as CPI paragraph, GDP paragraph, consumption paragraph, then figure-by-figure commentary, rewrite it.

The top-level section structure should follow conceptual work, not the visual order of panels.

Jose's transformation:

- Old structure: CPI -> GDP -> consumption -> tariff revenue -> trade balance -> REER
- New structure: benchmark dynamics -> mechanisms -> third-country interpretation -> robustness

Rule for Section 6:

- Build subsections whose titles encode explanatory roles.
- Each subsection should have one analytical job.

### 4. Lead with claims, then support them with numbers

Do not begin paragraphs with magnitudes unless the magnitude itself is the argument.

Preferred pattern:

1. State the economic claim.
2. Name the contrast or asymmetry.
3. Use figure evidence and magnitudes as support.
4. Close with interpretation.

Jose pattern:

- New prose starts with claims like `the targeted country experiences the larger output contraction`
- Old prose starts with values like `US CPI inflation rises 0.13 pp on impact`

### 5. Separate "what happens" from "why it happens"

Make an explicit distinction between descriptive dynamics and mechanism explanation.

Required implementation pattern:

- First subsection: benchmark or baseline dynamics
- Second subsection: mechanism decomposition

Do not blend these two tasks inside the same local block unless the passage is very short and the distinction remains obvious.

### 6. Translate variable-level narration into asymmetry-level narration

Readers should leave each subsection with one durable contrast.

Good contrast patterns, modeled on Jose:

- price incidence vs quantity incidence
- tariff-imposing country vs targeted country
- small aggregate response vs offsetting gross margins
- direct effect vs propagated effect
- benchmark mechanism vs robustness magnitude shift

Rule for Section 6:

- Every major subsection should be organized around one named contrast or asymmetry.
- If a paragraph cannot be summarized by a contrast, it is probably still too descriptive.

### 7. Reframe near-zero or ambiguous aggregate results as decomposition problems

If Section 6 contains a result that looks small, flat, mixed, or unstable, do not present it as "little happens."

Jose's EA rewrite shows the preferred move:

- Wrong framing: small response means little effect
- Right framing: small net response reflects multiple large margins with opposite signs

Required wording logic for analogous cases:

- `This is not a small-effect object; it is an offsetting-margins object.`

The exact sentence need not be copied, but the conceptual move should be copied.

### 8. Fold standalone tangents into the main analytical wedge

If the current section contains isolated paragraphs on accounting details, institutional assumptions, or side implications, do not necessarily preserve them as standalone blocks.

Jose example:

- Old section had a standalone paragraph on tariff revenue and its disposition.
- New section absorbed that material into the GDP-consumption wedge argument.

Rule for Section 6:

- A side mechanism should remain standalone only if it carries independent explanatory weight.
- Otherwise integrate it into the main paragraph where it sharpens the core claim.

### 9. Anchor prose claims in explicit model objects when needed

If the rewritten argument needs an accounting identity or model equation to carry credibility, cite the exact object.

Jose example:

- Added appendix label `app:eq:ulsilon_k` so the GDP-consumption wedge could be referenced cleanly.

Rule for Section 6:

- If a major claim depends on an accounting identity, label and cite the identity.
- Do not rely on vague phrases like "by the model accounting" if a precise citation is possible.

### 10. Keep robustness subordinate to the main narrative

Robustness exercises should test whether the main interpretation survives, not start an unrelated interpretation track.

Jose pattern:

- Robustness is introduced only after the benchmark and mechanisms are already established.
- The closing conclusion explicitly says robustness changes magnitudes but not the ordering of the main results.

Rule for Section 6:

- Put robustness late.
- Introduce it as a stress test of the central claims.
- End the robustness section by restating what survives.

### 11. End by motivating the next section

The end of Section 6 should make the next section feel necessary.

Jose example:

- After reframing the EA as a net object, he ends by motivating sectoral analysis.

Rule for Section 6:

- Final paragraph should explicitly state what unresolved decomposition, cross-section, extension, or application naturally follows.

### 12. Preserve one level of granularity per local block

Do not mix all of the following in one paragraph:

- figure reading
- mechanism theory
- accounting identity
- literature placement
- caveat
- forward link

Jose's rewrite became much cleaner because each block had a single scale of explanation.

Rule for Section 6:

- One paragraph, one main analytical function.

---

## Executable Rewrite Protocol

Another Codex session should apply the following sequence directly.

### Step 1. Diagnose the current Section 6 draft

Before writing, inventory:

- current title
- current subsection titles
- whether the prose is figure-panel-driven
- the main facts the section needs to preserve
- any existing accounting identities or equations that support the intended claims
- whether there is an ambiguous or near-zero outcome that should be reframed as offsetting margins

### Step 2. Write the opening triad

Create three opening paragraphs with fixed roles:

1. Questions the section answers
2. Preview facts or asymmetries
3. Roadmap

If the first paragraph starts with a figure reference or a number, rewrite it.

### Step 3. Build a "baseline dynamics" subsection

This subsection should answer:

- What are the main qualitative patterns?
- Which actors or margins move most?
- Which asymmetry is central?

Numbers are allowed, but the subsection should read as an interpreted baseline, not as an annotated spreadsheet.

### Step 4. Build a "mechanisms" subsection

Create 2 to 4 mechanism blocks, each with a named economic role.

For each mechanism block, use this order:

1. Define the mechanism
2. State how it enters the model
3. Explain what pattern it helps explain
4. Tie it back to a figure, equation, or comparison

Do not let the mechanism subsection become a second descriptive walk through the same figure.

### Step 5. Isolate the tricky object

If Section 6 has a third-country result, mixed-sign result, or weak aggregate result, give it its own interpretive subsection.

The job of this subsection is:

- to explain why the object is hard to read naively
- to decompose the gross forces
- to state the correct interpretation cleanly

### Step 6. Move robustness late and discipline its role

For each robustness block:

- state what margin is being stressed
- state the expected directional implication
- report whether the benchmark ranking survives

Avoid robustness prose that merely restates all the numbers from the figure.

### Step 7. Write a bridge ending

End the section with a short paragraph that says:

- what the current section established
- what remains unresolved at the current level of aggregation
- why the next section is needed

---

## Concrete Before/After Mapping From Jose's Rewrite

Use these as model moves.

### Move A. Generic title -> analytical title

- Before: `Quantitative results`
- After: `Aggregate transmission of a US--China tariff war`

### Move B. Panel walk-through -> thesis-first benchmark subsection

- Before: separate paragraphs for CPI, GDP, consumption, tariff revenue, trade balance, REER
- After: `Benchmark aggregate dynamics` with two opening asymmetries before detailed interpretation

### Move C. Country description -> incidence framing

- Before: "US CPI rises... China CPI rises less..."
- After: `price incidence` versus `quantity incidence`

### Move D. Small EA result -> net-object framing

- Before: dense paragraph with bilateral numbers
- After: dedicated subsection treating the EA as an offsetting-margins object

### Move E. Mechanism list buried in text -> explicit mechanism subsection

- Before: mechanisms scattered across results prose
- After: `Mechanisms behind the benchmark` with named blocks:
  `Direct incidence and expenditure switching`
  `Production-network amplification`
  `Currency invoicing and exchange-rate pass-through`

### Move F. Robustness as extra material -> robustness as confirmation

- Before: long robustness blocks living next to the main exposition
- After: `Additional robustness` explicitly framed as quantitative variation around the same core ranking

### Move G. Standalone tangent -> embedded accounting support

- Before: tariff revenue had its own paragraph
- After: tariff revenue supports the GDP-consumption wedge within the main benchmark interpretation

---

## Section 6 Template To Imitate

This is the preferred skeleton, adapted from Jose's rewrite pattern.

```text
\section{[Phenomenon-centered title]}

Opening paragraph 1: section questions
Opening paragraph 2: preview facts / asymmetries
Opening paragraph 3: roadmap

\subsection{[Baseline or benchmark dynamics]}
  \subsubsection{[Main incidence / main contrast]}
  \subsubsection{[Special object or third-country object if needed]}

\subsection{[Mechanisms behind the baseline]}
  \subsubsection{[Mechanism 1]}
  \subsubsection{[Mechanism 2]}
  \subsubsection{[Mechanism 3, only if truly needed]}

\subsection{[Interpretive payoff for the ambiguous object]}
  Explain why the aggregate object is small/mixed only in net terms

\subsection{[Additional robustness]}
  \subsubsection{[Robustness 1]}
  \subsubsection{[Robustness 2]}

Closing bridge paragraph to next section
```

Do not treat this skeleton as mandatory line-for-line LaTeX. Treat it as the preferred reasoning order.

---

## Style Constraints

The rewriting agent should preserve these style constraints:

- Use clear analytic prose, not ornate prose.
- Prefer claim-first sentences.
- Use numbers selectively and always in service of an interpretation.
- Avoid long runs of raw magnitudes.
- Avoid repeating the same mechanism in multiple subsections.
- Avoid over-claiming identification when the available object is only descriptive or accounting-based.
- State explicitly when a passage is interpretive rather than formally identified.

---

## Red Flags

If any of the following remain in the rewritten Section 6, the rewrite is probably incomplete:

- The section still reads in the order of the figure panels.
- The first substantive paragraph starts with point estimates.
- A near-zero result is described as simply small rather than decomposed.
- Mechanisms appear only as afterthoughts inside results paragraphs.
- Robustness changes the subject rather than testing the existing subject.
- The section ends without making the next section feel necessary.
- Long paragraphs mix descriptive reading, mechanism, caveat, and literature all at once.

---

## Success Criteria

The Section 6 rewrite is successful if all of the following are true:

- The title names the economic object of the section.
- The opening triad exists and is functional.
- The section is organized by claims and mechanisms, not by panel order.
- At least one core asymmetry or contrast structures the exposition.
- Any near-zero or ambiguous result is reframed as an offsetting-margins object.
- Robustness confirms or disciplines the main thesis rather than competing with it.
- The final paragraph creates a natural bridge into the following section.

---

## Important Caveat

Do not mechanically copy Jose's exact wording, placeholder text, or artifacts from commit `bc1454e`.

That commit preserved the old draft under `\section{old}` and still contained open placeholders such as:

- `[REVISAR CUANDO SE ACTUALICE LA FIGURA]`
- `[INCLUDE FIGURE HERE, AND I WILL ADAPT THE TEXT]`

Copy the transformation logic, not the unfinished residue.
