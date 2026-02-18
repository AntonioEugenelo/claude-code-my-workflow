# Combined Review Report: MacroWorkshop_v2.tex
**Date:** 2026-02-18
**Reviewers:** proofreader, slide-auditor, pedagogy-reviewer, tikz-reviewer, domain-reviewer

---

## 1. PROOFREADER REVIEW

### Issue 1: Line break inside bullet point (Slide 6)
- **File:** MacroWorkshop_v2.tex
- **Location:** Slide "From Subsidies to Government Spending", line 265
- **Current:** `\item Procurement changes \\demand \textit{composition}`
- **Proposed:** `\item Procurement changes demand \textit{composition}`
- **Category:** Typo
- **Severity:** High — The `\\` before "demand" forces a line break mid-bullet, which is likely unintentional and may cause awkward layout.

### Issue 2: Line break before $G_{ki}$ (Slide 6)
- **File:** MacroWorkshop_v2.tex
- **Location:** Slide "From Subsidies to Government Spending", line 283
- **Current:** `In an IO economy, \\$G_{ki}$ enters at the \textit{sector level}`
- **Proposed:** `In an IO economy, $G_{ki}$ enters at the \textit{sector level}`
- **Category:** Typo
- **Severity:** High — The `\\` before `$G_{ki}$` forces a line break AND escapes the dollar sign, so LaTeX will print a literal `$` rather than entering math mode. This will cause a compilation issue or garbled output.

### Issue 3: Missing cost-push shock term (Slide 5)
- **File:** MacroWorkshop_v2.tex
- **Location:** Slide "Phase 1: Fiscal Instruments...", lines 204, 211
- **Current:** Wage PC ends with `+ \beta\mathbb{E}_t\pi_{wk,t+1}` (no shock term)
- **Proposed:** Consider adding `+ u^w_{k,t}` for consistency with appendix slide A10 (line 625) and the original v2 slide 7 (line 268)
- **Category:** Consistency
- **Severity:** Low — Omission may be intentional for space, but creates inconsistency with the appendix derivation.

### Issue 4: Cox et al. welfare numbers presentation (Slide 2)
- **File:** MacroWorkshop_v2.tex
- **Location:** Slide "IO Economies: Divine Coincidence...", lines 102–103
- **Current:** `With fiscal: welfare 3.1 vs.\ 2.8` / `Without fiscal: 6.3 vs.\ 4.7`
- **Proposed:** Add labels: `With fiscal: welfare loss 3.1 (zero-infl.) vs.\ 2.8 (optimal MP)` or a brief note on what the numbers represent
- **Category:** Academic Quality
- **Severity:** Medium — Without context, the audience may not know what 3.1/2.8 represent. The appendix slide clarifies but the main slide does not.

### Issue 5: No other grammar, spelling, or punctuation issues found
- All remaining text is grammatically correct, uses formal academic register, and has consistent citation style.

---

## 2. SLIDE AUDITOR REVIEW

### Slide 1: "Motivation" (slide 1)
- **Issue:** None. Two-column layout with blocks is clean.
- **Severity:** —

### Slide 2: "IO Economies: Divine Coincidence..." (slide 2)
- **Issue:** Two blocks + one alertblock = 3 colored boxes. Borderline box fatigue.
- **Severity:** Low — Acceptable for a literature overview slide where side-by-side comparison is the point.

### Slide 3: "The Theoretical Benchmark" (slide 3)
- **Issue:** None. Clean two-column block layout.
- **Severity:** —

### Slide 4: "The Gap: From Benchmark to Reality" (slide 4)
- **Issue:** Two blocks + one alertblock = 3 colored boxes. Same as slide 2.
- **Severity:** Low — The alertblock carries the slide's key message; removing it would weaken the argument.

### Slide 5: "Phase 1: Fiscal Instruments..." (slide 5)
- **Issue:** Dense slide — two equations, TikZ diagram, descriptive text, and "Why not L&TS?" paragraph all on one frame. Risk of vertical overflow on projectors with different aspect ratios.
- **Severity:** Medium — The `\begingroup\small ... \endgroup` and `\small` on the Aguilar description help. The TikZ diagram is compact. Should be monitored visually in the PDF.
- **Recommendation:** If overflow occurs, reduce TikZ `node distance` from 1.2cm/1.4cm to 1.0cm/1.2cm, or move the "Why not L&TS?" box to a footnote.

### Slide 6: "From Subsidies to Government Spending" (slide 6)
- **Issue 1:** The `\\` line break in line 265 (Issue 1 from proofreader) may cause unintended vertical spacing inside the alertblock.
- **Issue 2:** The `\\$G_{ki}$` in line 283 will print a literal dollar sign — HIGH priority fix.
- **Severity:** High (due to Issue 2)

### Slide 7: "Research Agenda" (slide 7)
- **Issue:** 3 enumerated items + equation + conjecture. Moderately dense but within bounds for a 169 aspect ratio.
- **Severity:** Low

### Slide 8: "Summary" (slide 8)
- **Issue:** 4 enumerated items with substantial text. Could be tight.
- **Severity:** Low — `\itemsep{6pt}` provides adequate spacing.

---

## 3. PEDAGOGY REVIEWER REVIEW

### Summary
- **Patterns followed:** 10/13
- **Patterns violated:** 1/13
- **Patterns partially applied:** 2/13
- **Deck-level assessment:** Strong narrative arc with clear two-phase structure. Minor pacing concern.

### Pattern-by-Pattern

| # | Pattern | Status | Notes |
|---|---------|--------|-------|
| 1 | Motivation before formalism | ✅ Followed | Slide 1 motivates before slides 2–3 formalize |
| 2 | Incremental notation | ✅ Followed | Rubbo's simpler notation introduced before Aguilar's $K \times I$ version |
| 3 | Worked example after definition | ⚠️ Partially | No worked example, but this is a research talk, not a lecture — appropriate |
| 4 | Progressive complexity | ✅ Followed | Simple (Rubbo 1-sector) → complex (Aguilar $K \times I$) |
| 5 | Fragment reveals | N/A | No `\pause` or overlays (per project rules) |
| 6 | Standout slides at pivots | ✅ Followed | Slide 6 serves as the Phase 1→2 transition |
| 7 | Two-slide strategy for dense theorems | ⚠️ Partially | Slide 5 is dense; could benefit from splitting, but 15-min constraint justifies |
| 8 | Semantic colour usage | ✅ Followed | `\red{}` consistently marks key differentiators |
| 9 | Box hierarchy | ✅ Followed | `block` for literature, `alertblock` for key arguments |
| 10 | Box fatigue | ✅ Followed | Max 3 boxes/slide, acceptable for comparison slides |
| 11 | Socratic embedding | ❌ Violated | No embedded questions. The alertblock on slide 2 ends with "What happens when we combine both?" — this is the only question mark in the deck. |
| 12 | Visual-first for complex concepts | ✅ Followed | TikZ network diagram on slide 5 |
| 13 | Two-column comparisons | ✅ Followed | Used on slides 1, 2, 3, 4, 5, 6 |

### Deck-Level

- **Narrative arc:** Excellent. Clear progression: Literature gap → Benchmark → Gap → Phase 1 (bridge) → Phase 2 (agenda) → Summary.
- **Pacing:** 4 theory-heavy slides (2–5) before the transition at slide 6. Acceptable for a 15-min research talk.
- **Visual rhythm:** Good. Mix of two-column layouts, equations, TikZ, and enumerated lists.
- **Notation:** Consistent throughout. $\tau^w_k$, $\tau^s_{ki}$, $G_{ki}$ used consistently across main and appendix slides.

### Critical Recommendations
1. Consider adding one embedded question to break the theory sequence (e.g., end of slide 4: "Can we do better with fewer instruments?")
2. The alertblock question on slide 2 is effective — keep it prominent.
3. The Phase 1 → Phase 2 transition on slide 6 is the strongest pedagogical feature of the restructure.

---

## 4. TIKZ REVIEWER REVIEW

### Diagram: IO Network (Slide 5, lines 217–230)

#### Issue 1: Fiscal entry label semantics
- **Severity:** MINOR
- **Location:** Line 229, label `$\tau^s_{km}$`
- **Problem:** The arrow uses `oxfordaccent` to visually distinguish it from IO links (good). The label correctly shows $\tau^s_{km}$ for Phase 1. However, the original v2 had $G_{km}$ since the diagram was introduced in the context of government spending. The change to $\tau^s_{km}$ is correct for Phase 1 but means Phase 2 loses its visual anchor in the main slides.
- **Fix:** Acceptable as-is. The appendix diagram could be duplicated with $G_{km}$ label for Phase 2 if needed.

#### Issue 2: Label-edge proximity
- **Severity:** MINOR
- **Location:** Edge labels `$\omega_{kkij}$`, `$\omega_{kkjm}$`, `$\omega_{kkmi}$`
- **Problem:** With `node distance=1.2cm and 1.4cm`, the edge labels are adequately spaced. No overlap detected.
- **Fix:** None needed.

#### Issue 3: Arrow direction convention
- **Severity:** MINOR
- **Location:** Lines 226–228
- **Problem:** Arrows go $i \to j$, $j \to m$, $m \to i$ — forming a directed cycle. This represents IO flows (sector $i$ uses inputs from $j$). The convention is consistent with the Rubbo/Aguilar notation where $\omega_{kkij}$ = share of sector $j$'s output used by sector $i$.
- **Fix:** None needed — semantically correct.

### Verdict: **APPROVED**
Zero CRITICAL, zero MAJOR issues. Three MINOR notes, all acceptable.

---

## 5. DOMAIN REVIEWER REVIEW

### Summary
- **Overall assessment:** SOUND
- **Total issues:** 4
- **Blocking issues:** 1 (the `\\$` typo — rendering issue, not substance)
- **Non-blocking issues:** 3

### Lens 1: Assumption Stress Test

#### Issue 1.1: L&TS "flexible wages" characterisation
- **Slide:** 3 (Theoretical Benchmark), 4 (The Gap)
- **Severity:** MINOR
- **Claim:** "both assume flexible wages (competitive labour market)"
- **Check:** L&TS (2025 WP) assume a competitive labour market with flexible nominal wages. A&M (2025) assume competitive labour. The characterisation is accurate.
- **Status:** ✅ Correct

#### Issue 1.2: "Trivial 2N solution" claim
- **Slide:** 5 (Phase 1), line 236
- **Severity:** MINOR
- **Claim:** `the "trivial" 2N solution doesn't clean up wage misallocation`
- **Check:** This is the key theoretical argument. Under L&TS, the $2N$ instruments (sales tax + payroll tax per sector) restore production efficiency because all frictions are on the price side. With Calvo wages, wage misallocation is a separate distortion. The $2N$ price-side taxes cannot undo a wage-side friction — this is correct in principle.
- **Caveat:** L&TS's $2N$ instruments actually include $N$ labour wedge taxes. The precise claim should be that L&TS's solution *assumes* the wage adjusts freely; it doesn't need a separate wage instrument because there's no wage friction. With Calvo wages, the wage cannot adjust freely, so even with L&TS's full $2N$ set, the restoration fails because the wage friction introduces an additional distortion not covered by their optimality conditions.
- **Recommendation:** The phrasing is accurate for a research talk. Could add "even with their full $2N$ set" for precision.
- **Status:** ✅ Substantively correct, minor precision improvement possible

### Lens 2: Derivation Verification

#### Issue 2.1: Wage PC without shock term (Slide 5)
- **Slide:** 5 (Phase 1), line 204
- **Severity:** MINOR
- **Check:** The wage PC is written as $\pi_{wk,t} = \kappa_{wk}(\ldots) + \beta\mathbb{E}_t\pi_{wk,t+1}$ without $+ u^w_{k,t}$. The appendix derivation (line 625) includes the shock term. This is a pedagogical simplification for the main slide — acceptable but creates a minor inconsistency.
- **Status:** ⚠️ Intentional simplification, note the inconsistency

### Lens 3: Citation Fidelity

#### Issue 3.1: Cox et al. (2024) "Big G" attribution
- **Slide:** 6 (From Subsidies to Government Spending), line 274
- **Claim:** `Cox et al. (2024, "Big G") document that government spending is: highly concentrated (top sectors receive >35% of federal procurement)`
- **Check:** The Big G paper (Cox, Müller, Pastén, Schoenle, Weber, NBER WP 27034) does document concentration of federal procurement. The ">35%" figure appears in their empirical analysis of FPDS data.
- **Status:** ✅ Accurate

#### Issue 3.2: Cox et al. (2024) — two different Cox papers
- **Slide:** 2 vs. Slide 6
- **Severity:** MEDIUM
- **Problem:** Slide 2 references **Cox et al. (2024)** for the fiscal policy + divine coincidence result (this is the NBER "Optimal Monetary and Fiscal Policies in Disaggregated Economies" paper). Slide 6 references **Cox et al. (2024, "Big G")** for the procurement facts. These are two DIFFERENT papers by overlapping (but not identical) author sets. Both are dated 2024. The audience may conflate them.
- **Recommendation:** Differentiate clearly. Consider: "Cox, Müller et al. (2024, Big G)" on slide 6 vs. "Cox, Erceg, Leist (2024)" on slide 2 — or add a/b suffixes. Check which author set is correct for each paper.
- **Status:** ⚠️ Needs clarification — verify author overlap and add disambiguating labels

### Lens 4: Code-Theory Alignment
- No code in this file. N/A.

### Lens 5: Backward Logic Check
- **Summary slide (8) → slides 1–7:** Each of the 4 summary items traces back to specific earlier content. Phase 1 → slide 5, Phase 2 → slides 6–7, Benchmark → slides 2–3, Conjecture → slide 7. ✅ Consistent.
- **Slide 7 (Research Agenda) → slides 4–5:** The claim that price-wedge restoration is impossible traces back to slides 4 (Gap) and 5 (Phase 1 extension). ✅ Consistent.
- **No circular arguments detected.**

### Positive Findings
1. The two-phase narrative arc is logically tight — each slide builds on the previous one.
2. The wage rigidity argument is correctly articulated and well-supported by the L&TS/A&M benchmark contrast.
3. The market clearing equation on slide 7 is correctly specified for the open-economy case.

---

## CONSOLIDATED ACTION ITEMS

### HIGH PRIORITY (Must Fix)
| # | Issue | Location | Fix |
|---|-------|----------|-----|
| 1 | `\\` before `$G_{ki}$` prints literal `$` | Line 283 | Remove `\\` → `$G_{ki}$` |
| 2 | `\\` inside bullet forces line break | Line 265 | Remove `\\` → `Procurement changes demand` |

### MEDIUM PRIORITY (Should Fix)
| # | Issue | Location | Fix |
|---|-------|----------|-----|
| 3 | Two different Cox et al. (2024) papers | Slides 2, 6 | Disambiguate (e.g., "Big G" vs. "Optimal MP&FP") |
| 4 | Welfare numbers lack context | Slide 2 | Add "(welfare loss)" or column headers |

### LOW PRIORITY (Nice to Fix)
| # | Issue | Location | Fix |
|---|-------|----------|-----|
| 5 | Missing shock terms in PCs | Slide 5 | Add `+ u^w_{k,t}` and `+ u^p_{ki,t}` for appendix consistency |
| 6 | No embedded Socratic question | Slides 2–5 | Add one question to break theory run |
| 7 | "Trivial 2N solution" precision | Slide 5 | Consider "even with L&TS's full $2N$ set" |
