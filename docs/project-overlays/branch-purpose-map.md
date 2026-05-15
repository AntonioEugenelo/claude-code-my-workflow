# Branch Purpose Map

This checkout is tailored to the Fiscal-LPT / MCMS fiscal-extension project while preserving reusable workflow machinery from the prior purpose-agnostic branch.

## Known Branch Uses

| Branch or family | Primary use | Activate overlays |
| --- | --- | --- |
| `main`, `codex-upstream-purpose-agnostic-migration` | Codex-first workflow infrastructure and Claude compatibility | `workflow-infrastructure.md` |
| Fiscal-LPT / MCMS fiscal extension | Fiscal variables and fiscal-rule steps in MCMS, with a paper-only Overleaf repo | `fiscal-lpt-mcms.md`, `mcms.md` |
| MCMS-related work | model runs, calibration, generated results | `mcms.md` |
| `cox-replication-*`, `preserve-cox-replication-before-codex-migration` | Cox replication and government-spending model/paper work | `cox-replication.md` |
| `cover-letters` | Cover letters, statements, fellowship/exchange applications | `cover-letters.md` |
| `cv-editing` | CV editing, CV consistency checks, application packages | `cv-editing.md`, `antonio-eugenelo.md` |
| `ISOF-reviews` | Referee/review forms and paper assessment | `referee-review.md`, optionally `academic-research.md` |
| `Monetary_Economics` | Teaching, lecture notes, problem sets, Beamer/Quarto slides | `teaching-slides.md`, optionally `academic-research.md` |
| `Slides---Antigravity` | Slide/application prototype and visual presentation work | `slide-prototype.md`, optionally `academic-research.md` |
| Upstream workflow branches | Importing reusable hooks, agents, skills, docs, and repo hygiene | `workflow-infrastructure.md` |

## Boundary Rule

Represent repeatable project behavior as an overlay, workflow doc, template,
script, skill, agent, or rule. Keep model code in `../MCMS-private`, paper source
in `../Fiscal-LPT`, and writing-direction material in this workflow repo.

## Independence Rule

The default branch must work with only Git and Python available. Tools such as MATLAB, Dynare, Quarto, LaTeX, R, GitHub CLI, Overleaf credentials, and project datasets are optional requirements of selected overlays.
