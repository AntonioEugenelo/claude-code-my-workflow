# Adversarial Review Loop — Round 1 Report
**Date:** 2026-02-18
**File:** `MacroWorkshop_v2.tex` (post-fix, lines 265 + 283 corrected)
**Reviewers:** Tightened proofreader + domain-reviewer

---

## PROOFREADER (Tightened)

### Beamer-Specific Pitfalls

| Check | Result |
|-------|--------|
| Stray `\\` inside itemize | ✅ None found (lines 265+283 fixed) |
| `\\$` patterns | ✅ None found |
| `\begingroup`/`\endgroup` balance | ✅ 3/3 matched (L202↔206, L209↔213, L472↔484) |
| Orphaned hyperlinks | ✅ 2 links → 2 targets found (production-network, tariff-propagation) |
| Equation display consistency | ✅ All equations use `\[...\]` consistently |

### Cross-Slide Consistency

#### Issue P-R1.1: Shock terms omitted without note
- **Location:** Slide 5 (lines 204, 211) vs. Appendix A10 (line 625) / A11 (line 646)
- **Current:** Main slide PCs end with `+ \beta\mathbb{E}_t\pi_{wk,t+1}` — no shock term
- **Appendix:** Same equations include `+ u^w_{k,t}` / `+ u^p_{ki,t}`
- **Category:** Cross-slide consistency (Beamer pitfall #3)
- **Severity:** Medium (-2)
- **Fix:** Either add shock terms to main slide, or add footnote "shock terms omitted"

#### Issue P-R1.2: Cox et al. (2024) not disambiguated on slide 2
- **Location:** Slide 2, lines 98–104
- **Current:** `Cox et al.\ (2024)` — refers to the fiscal divine coincidence paper
- **Problem:** Slide 6 also cites `Cox et al.\ (2024, "Big G")` — a different paper. Slide 2 gives no label.
- **Category:** Disambiguation (new check #5.7)
- **Severity:** Major (-5)
- **Fix:** Add descriptor, e.g., `Cox, Erceg \& Leist (2024)` or `Cox et al.\ (2024, ``Optimal FP'')`

### Grammar / Typos / Academic Quality
- No further issues found.

---

## DOMAIN REVIEWER (Tightened)

### Lens 1: Assumption Stress Test
- All assumptions correctly stated. ✅

### Lens 2: Derivation Verification
- Equations correct. ✅
- Cross-slide shock term omission noted (same as P-R1.1). ⚠️

### Lens 3: Citation Fidelity

#### Issue D-R1.1: Cox et al. (2024) disambiguation (same as P-R1.2)
- **Severity:** Major (-5)
- **Problem:** Two distinct papers cited as "Cox et al. (2024)". Need clear labelling.

#### Issue D-R1.2: Welfare numbers lack table reference
- **Slide:** 2, lines 102–103
- **Current:** "welfare 3.1 vs. 2.8", "6.3 vs. 4.7"
- **Problem:** Numbers from Table 3 of Cox et al. (2024, fiscal paper) but the table is not referenced on the main slide.
- **Severity:** Minor (-1)
- **Recommendation:** Add "(Table 3)" or "(welfare loss × 10⁴)" for unit clarity. The appendix slide (A3, line 426) does say "Table 3" — but the main slide should too.

### Lens 5: Backward Logic Check
- Summary → earlier slides: all 4 items trace back. ✅
- No circular arguments. ✅

---

## SCORING

| Category | Issue | Deduction |
|----------|-------|-----------|
| Major | Cox disambiguation (P-R1.2 / D-R1.1) | -5 |
| Medium | Shock terms omitted without note (P-R1.1) | -2 |
| Minor | Welfare numbers lack table ref (D-R1.2) | -1 |

**Round 1 Score: 100 - 5 - 2 - 1 = 92/100**

**Verdict: PASS ≥ 90** — but two issues should be fixed to reach 97+.

---

## FIXES REQUIRED FOR ROUND 2

1. **[MAJOR] Disambiguate Cox et al. on slide 2** — add descriptive label
2. **[MEDIUM] Add footnote to slide 5 PCs** — note shock term omission
3. **[MINOR] Add "(Table 3)" to welfare numbers on slide 2** — traceability
