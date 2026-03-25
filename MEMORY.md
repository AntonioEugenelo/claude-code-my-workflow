# Project Memory

Corrections and learned facts that persist across sessions.
When a mistake is corrected, append a `[LEARN:category]` entry below.

---

<!-- Append new entries below. Most recent at bottom. -->

## Workflow Patterns

[LEARN:workflow] Requirements specification phase catches ambiguity before planning → reduces rework 30-50%. Use spec-then-plan for complex/ambiguous tasks (>1 hour or >3 files).

[LEARN:workflow] Spec-then-plan protocol: AskUserQuestion (3-5 questions) → create `quality_reports/specs/YYYY-MM-DD_description.md` with MUST/SHOULD/MAY requirements → declare clarity status (CLEAR/ASSUMED/BLOCKED) → get approval → then draft plan.

[LEARN:workflow] Context survival before compression: (1) Update MEMORY.md with [LEARN] entries, (2) Ensure session log current (last 10 min), (3) Active plan saved to disk, (4) Open questions documented. The pre-compact hook displays checklist.

[LEARN:workflow] Plans, specs, and session logs must live on disk (not just in conversation) to survive compression and session boundaries. Quality reports only at merge time.

## Documentation Standards

[LEARN:documentation] When adding new features, update BOTH README and guide immediately to prevent documentation drift. Stale docs break user trust.

[LEARN:documentation] Always document new templates in README's "What's Included" section with purpose description. Template inventory must be complete and accurate.

[LEARN:documentation] Guide must be generic (framework-oriented) not prescriptive. Provide templates with examples for multiple workflows (LaTeX, R, Python, Jupyter), let users customize. No "thou shalt" rules.

[LEARN:documentation] Date fields in frontmatter and README must reflect latest significant changes. Users check dates to assess currency.

## Design Philosophy

[LEARN:design] Framework-oriented > Prescriptive rules. Constitutional governance works as a TEMPLATE with examples users customize to their domain. Same for requirements specs.

[LEARN:design] Quality standard for guide additions: useful + pedagogically strong + drives usage + leaves great impression + improves upon starting fresh + no redundancy + not slow. All 7 criteria must hold.

[LEARN:design] Generic means working for any academic workflow: pure LaTeX (no Quarto), pure R (no LaTeX), Python/Jupyter, any domain (not just econometrics). Test recommendations across use cases.

## File Organization

[LEARN:files] Specifications go in `quality_reports/specs/YYYY-MM-DD_description.md`, not scattered in root or other directories. Maintains structure.

[LEARN:files] Templates belong in `templates/` directory with descriptive names. Currently have: session-log.md, quality-report.md, exploration-readme.md, archive-readme.md, requirements-spec.md, constitutional-governance.md.

## Constitutional Governance

[LEARN:governance] Constitutional articles distinguish immutable principles (non-negotiable for quality/reproducibility) from flexible user preferences. Keep to 3-7 articles max.

[LEARN:governance] Example articles: Primary Artifact (which file is authoritative), Plan-First Threshold (when to plan), Quality Gate (minimum score), Verification Standard (what must pass), File Organization (where files live).

[LEARN:governance] Amendment process: Ask user if deviating from article is "amending Article X (permanent)" or "overriding for this task (one-time exception)". Preserves institutional memory.

## Skill Creation

[LEARN:skills] Effective skill descriptions use trigger phrases users actually say: "check citations", "format results", "validate protocol" → Claude knows when to load skill.

[LEARN:skills] Skills need 3 sections minimum: Instructions (step-by-step), Examples (concrete scenarios), Troubleshooting (common errors) → users can debug independently.

[LEARN:skills] Domain-specific examples beat generic ones: citation checker (psychology), protocol validator (biology), regression formatter (economics) → shows adaptability.

## Memory System

[LEARN:memory] Two-tier memory solves template vs working project tension: MEMORY.md (generic patterns, committed), personal-memory.md (machine-specific, gitignored) → cross-machine sync + local privacy.

[LEARN:memory] Post-merge hooks prompt reflection, don't auto-append → user maintains control while building habit.

## PDF & Reference Processing

[LEARN:pdf] On Windows, use PyMuPDF (`import fitz`) for PDF text extraction — the Read tool's built-in PDF reader requires `pdftoppm` which is not installed. Always set `sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')` to handle academic Unicode.

[LEARN:pdf] Use `glob.glob()` for filenames with special characters (umlauts, accents) — Python string literals may not match the filesystem encoding.

[LEARN:references] ALWAYS check `master_supporting_docs/` BEFORE going online. The local folder contains authoritative paper copies. Only use WebSearch/WebFetch if the paper is not available locally or supplementary info is needed.

## Meta-Governance

[LEARN:meta] Repository dual nature requires explicit governance: what's generic (commit) vs specific (gitignore) → prevents template pollution.

[LEARN:meta] Dogfooding principles must be enforced: plan-first, spec-then-plan, quality gates, session logs → we follow our own guide.

[LEARN:meta] Template development work (building infrastructure, docs) doesn't create session logs in quality_reports/ → those are for user work (slides, analysis), not meta-work. Keeps template clean for users who fork.

## Tariffs ECB Paper — Project Knowledge

[LEARN:project] MCMS model: `master_supporting_docs/MCMS/` (branch: Paper). 4 countries (EA, CHN, ROW, USA), 44 sectors (3 energy + 41 non-energy). MATLAB/Dynare. Entry: `a0_launch.m`. Core equations: `dynare_files/b4_declare_model.mod`. Calibration: `a1_calibration.m`.

[LEARN:project] Tariffs_ECB paper: `master_supporting_docs/Tariffs_ECB/0_clean/`. Overleaf-synced via `scripts/sync_to_overleaf.sh`. Paper sections in `sections/`, figures in `figures/`. Preliminary sections: 51 (macro effects), 52 (sectoral shocks), 60 (conclusions).

[LEARN:model] IO matrix convention: Omega_X(buyer-country, seller-country, buyer-sector, seller-sector). Country reordering: data (EA=1, USA=2, CHI=3, ROW=4) → model (EA=1, CHN=2, ROW=3, USA=4). Knum=4=USA is hardcoded as dollar anchor.

[LEARN:model] Only tariff shocks active (varepsilon_tau). Other shocks (TFP, demand, cost-push) are calibrated in a1_calibration.m but not fired in b5_declare_variance.mod. Tariff persistence rho=0.96.

[LEARN:model] 18 scenario runs: 9 structural (Baseline, 5 IO decompositions, CnPeg, Arm1, Arm2) × 2 invoicing (Het_DCP, PCP). Post-processing via new_process.py → PDFs.

[LEARN:workflow] ECB colour palette: #003299 (blue), #FFD700 (gold), #FF6600 (orange), #009900 (green). Applied to R figures, Python plots, and any presentation materials.

## LaTeX / TinyTeX

[LEARN:latex] TinyTeX 2025 install has broken `updmap`/`pdftex.map` (generated on CI runner). Cannot use `tlmgr install` against 2026 repos. Workaround: download packages from CTAN manually, install files into texmf-dist, run `mktexlsr`.

[LEARN:latex] `mathastext` with `eulergreek` option requires the `eulervm` package (font family `zeur*`), NOT just the base Euler fonts (`eur*`). The `eulervm` virtual fonts (zeur*.vf + zeur*.tfm) bridge mathastext to Euler Type1 glyphs. Without eulervm, Greek letters render as T1 ligatures (β→fi, δ→ffi, γ→fl).

[LEARN:latex] Edit tool fails with EEXIST on git submodule paths. Use Python scripts via Bash tool for all file modifications inside `master_supporting_docs/Tariffs_ECB/` and `master_supporting_docs/MCMS/`.

## User Preferences

[LEARN:preference] NEVER run reviews yourself — always delegate to the domain-reviewer, proofreader, or other specialist agents. If agents stall or fail, restart them or notify the user. Do not substitute manual review for agent-based review.

[LEARN:project] Antonio Eugenelo is University of Oxford (RA), NOT ECB. The other authors (Aguilar, Chankova, Darracq, Dieppe, Dominguez-Diaz, Gallegos, Quintana) are ECB.
