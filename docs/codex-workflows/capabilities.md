# Capability Map

This file replaces Claude slash commands with Codex-native task recipes. Users can ask for these in plain language.

## Common Requests

| User Intent | Codex Procedure |
| --- | --- |
| Tailor a new project branch | Apply `branch-tailoring.md`, select overlays from `project-overlays/branch-purpose-map.md`, and update `quality_reports/decisions/ACTIVE.md`. |
| Compile LaTeX | Identify the target `.tex`, run the appropriate LaTeX command, inspect log/output, and report blocking warnings and generated artifacts. |
| Proofread a file | Run the `proofreader` lens from `review-routing.md`, save findings to `quality_reports/`, and avoid editing unless the user asked for fixes. |
| Review a letter | Use proofreader, domain, narrative, and letter-quality lenses. Verify recipient facts and one-page constraints. |
| Review a paper | Use proofreader, derivation, figure-consistency, theory, and narrative lenses. Prefer findings-first output. |
| Review code or analysis | Use correctness, structure, and reproducibility lenses. Focus on bugs, regressions, and missing checks. |
| Translate Beamer to Quarto | Preserve source-of-truth in Beamer, translate slide-by-slide, convert citations and environments, then render and proofread the Quarto output. |
| Validate bibliography or citations | Cross-check citation keys against the bibliography files and flag missing, stale, or incorrect references. |
| Draft or revise a cover letter | Gather target context, fit evidence, and constraints; draft in LaTeX; then verify tone, facts, and page length. |
| Edit a CV | Use `cv-editing.md`, preserve factual claims, edit the CV source, and compare against target application constraints. |
| Draft a referee report | Use `referee-review.md`, separate major and minor concerns, and satisfy any fixed review-form fields exactly. |
| Create lecture material | Plan first, establish structure, draft source slides, compile, then run narrative/domain/layout review. |
| Build a slide prototype | Use `slide-prototype.md`, render or screenshot the result when possible, and keep frontend dependencies project-local. |
| Run Cox replication work | Use `cox-replication.md`, apply the rerun gate, and use a claim ledger for broad numeric or figure audits. |
| Run data analysis | Inspect inputs, confirm assumptions, run the analysis code, regenerate outputs, and summarize reproducibility status. |
| Deploy docs or rendered outputs | Render first, verify artifacts, then run the repo-specific sync or publish script if applicable. |
| Challenge an argument | Use `adversarial-review.md` and the `devils-advocate` review agent after the baseline route. |
| Brainstorm research ideas | Read relevant supporting material, synthesize literature constraints, and propose testable questions with empirical strategies. |
| Conduct an interview-style elicitation | Ask a short sequence of targeted questions, summarize the answers, and turn them into a concrete brief or research plan. |
| Create a checkpoint | Summarize active branch, plan, open files, decisions, blockers, verification state, and next actions in `quality_reports/checkpoints/`. |
| Preregister a study | Use `templates/preregistration-template.md` and the `.codex/skills/preregister/` workflow to convert a research spec into a preregistration draft. |
| Run a deep audit | Use the audit/reproducibility lenses, compare source files to outputs, and save findings under `quality_reports/`. |
| Respond to referees | Map each referee point to manuscript changes, evidence, and response text; verify source/output consistency before drafting final prose. |
| Verify claims | Trace claims to source files, data, code, tables, figures, and bibliography entries; flag unsupported statements. |
| Commit work | Confirm the diff, summarize what changed, and use non-interactive git commands. Do not stage secrets or unrelated local state. |

## Output Expectations

- For reviews, default to findings-first.
- For implementation tasks, default to execute rather than merely propose.
- For verification-heavy tasks, include the command or method used and whether it passed.
- For exploratory tasks, distinguish provisional results from production-ready outputs.
