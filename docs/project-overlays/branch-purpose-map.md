# Branch Purpose Map

This branch is the purpose-agnostic overset branch. It should contain the reusable workflow machinery for every known project branch, but it should not make any project overlay active by default.

## Known Branch Uses

| Branch or family | Primary use | Activate overlays |
| --- | --- | --- |
| `main`, `codex-upstream-purpose-agnostic-migration` | Codex-first workflow infrastructure and Claude compatibility | `workflow-infrastructure.md` |
| `Tariffs_ECB_paper`, `codex-ecb-tariffs` | Tariffs/ECB paper, Overleaf sync, academic writing, review, compilation | `academic-research.md`, `antonio-eugenelo.md`, `tariffs-overleaf.md` |
| MCMS-related work | MATLAB/Dynare model runs, calibration, generated results | `mcms.md`, optionally `academic-research.md` |
| `cox-replication-*`, `preserve-cox-replication-before-codex-migration` | Cox replication and government-spending model/paper work | `cox-replication.md`, `government-spending.md`, optionally `academic-research.md` |
| `antonio-main-mixed-archive` | Antonio/Oxford local academic context and mixed legacy material | `antonio-eugenelo.md`, then task-specific overlays |
| `cover-letters` | Cover letters, statements, fellowship/exchange applications | `cover-letters.md`, `antonio-eugenelo.md` |
| `cv-editing` | CV editing, CV consistency checks, application packages | `cv-editing.md`, `antonio-eugenelo.md` |
| `ISOF-reviews` | Referee/review forms and paper assessment | `referee-review.md`, optionally `academic-research.md` |
| `Monetary_Economics` | Teaching, lecture notes, problem sets, Beamer/Quarto slides | `teaching-slides.md`, optionally `academic-research.md` |
| `Slides---Antigravity` | Slide/application prototype and visual presentation work | `slide-prototype.md`, optionally `academic-research.md` |
| Upstream workflow branches | Importing reusable hooks, agents, skills, docs, and repo hygiene | `workflow-infrastructure.md` |

## Overset Rule

If a branch has a distinct repeatable use, represent that use as an overlay, workflow doc, template, script, skill, agent, or rule in this branch. Do not copy large project assets into the generic branch just to prove support exists.

## Independence Rule

The default branch must work with only Git and Python available. Tools such as MATLAB, Dynare, Quarto, LaTeX, R, GitHub CLI, Overleaf credentials, and project datasets are optional requirements of selected overlays.
