# Session Log: Main-Text MCMS Audit

Date: 2026-04-19

Scope:
- active main text only
- appendix excluded by user instruction

Key commands:
- `./scripts/sync-overleaf.sh status`
- `git status --short`
- `latexmk -pdf -interaction=nonstopmode -halt-on-error 0_main.tex`
- `python explorations/full_paper_mcms_audit/scripts/extract_active_claims.py`
- `python master_supporting_docs/MCMS/extract_paper_numbers.py`
- `python master_supporting_docs/MCMS/new_process.py`
- `python explorations/full_paper_mcms_audit/scripts/build_maintext_evidence.py`

Key evidence files:
- [active_claim_inventory.md](C:/CustomTools/claude-code-my-workflow/explorations/full_paper_mcms_audit/output/active_claim_inventory.md)
- [maintext_mcms_evidence.json](C:/CustomTools/claude-code-my-workflow/explorations/full_paper_mcms_audit/output/maintext_mcms_evidence.json)
  Includes generation timestamp plus SHA256 and mtime fingerprints for the key CSV and MAT artifacts used in the audit.
- [2026-04-19_main-text-mcms-audit_adversarial.md](C:/CustomTools/claude-code-my-workflow/quality_reports/reviews/2026-04-19_main-text-mcms-audit_adversarial.md)
- [2026-04-19_mcms-maintext-code-adversarial.md](C:/CustomTools/claude-code-my-workflow/quality_reports/reviews/2026-04-19_mcms-maintext-code-adversarial.md)

Main findings logged:
- Figure 4 prose/caption still describe `delta = 1, mu = 2`, while the current MCMS export is `delta = mu = 1`
- robustness captions in Section 55a repeatedly say `bilateral tariff` although the corresponding MCMS jobs use `shock_pair = (4, 2)`
- `python new_process.py` currently fails on unreadable `irf_Het_DCP_Baseline.mat`, then fails again in the MATLAB fallback
- sector IDs are inconsistent across generator outputs, and that inconsistency propagates into single-shock transmission exports
