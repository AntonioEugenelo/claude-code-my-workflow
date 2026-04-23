# Session Log: Horse-Race Appendix Replication

Date: 2026-04-20

## Scope

- Replicated the deleted horse-race appendix that had previously been included in the paper.
- Avoided modifying the live manuscript and wrote all regenerated artifacts to scratch space.

## Actions

- Confirmed the relevant deleted source was `a_appendix_horse_race.tex`, not `a_appendix_horse_race_revised.tex`.
- Recovered the deleted source into `quality_reports/recovered/2026-04-20_horse_race_appendix_recovered.tex`.
- Ran `run_horse_race_appendix.py` in isolation with output redirected to `quality_reports/tmp/horse_race_replication_2026-04-20/current_run/`.
- Compared narrative claims in the recovered appendix against regenerated CSV / JSON outputs and direct `.mat` extraction.

## Outcome

- Most appendix claims replicate.
- The aggregate consumption / CPI subsection is internally inconsistent because the runner mixes:
  - cached benchmark CSV data for heterogeneous-DCP aggregate blocks
  - direct `.mat` data for the role-based benchmark analysis
- The mismatch matters for benchmark CPI, especially the euro-area benchmark CPI claim.

## Artifacts

- Review report:
  `quality_reports/reviews/2026-04-20_horse-race-appendix-replication.md`
- Scratch rerun outputs:
  `quality_reports/tmp/horse_race_replication_2026-04-20/current_run/`
