# 90-minute compressed integrated mock (synthetic)

**Not official.** Do not inspect any answer key; none is bundled.

## Scenario
A manufacturing team has production and equipment maintenance records. Create a command-line quality decision tool, fix the unsafe legacy code, and design a reproducible fault-risk ML experiment.

## Inputs
- `production.csv`: lot, equipment, units, defects, customer, event_time, temperature
- `maintenance.csv`: equipment and last inspection date
- `customers.json`: inclusive/exclusive rate and inspection recency requirements
- `starter.py`: intentionally incomplete and insecure

## Required deliverables
1. `practice/solution.py` CLI accepting `--data-dir` and `--output`.
2. Join production to maintenance by equipment. Reject duplicate maintenance IDs; handle missing joins explicitly.
3. Validate counts and timestamps. Produce one row per lot with `PASS/FAIL/REVIEW`, reasons, and customer.
4. For customer A, max defect rate <= 1%; inspection <= 30 days as of 2026-10-25. For B, defect rate strictly < 2%; inspection <= 14 days. Interpret exactly as in `customers.json`.
5. Generate `results.csv` and `summary.json` with weighted overall defect rate; do not average lot percentages.
6. Replace unsafe `eval` in `starter.py` with safe JSON parsing and clear errors.
7. Add >= 5 automated tests covering equality boundary, strict boundary, missing maintenance, duplicate equipment, zero production, and invalid path (at least five of these).
8. Write `ML_PLAN.md` describing how you would train and compare a baseline and a neural network on sensor time series: prediction horizon, label definition, time/group split, leakage checks, imbalance, metrics, threshold selection, final test. You do not need to train a network in this compressed mock.
9. Run tests and report commands/results in `RUN_LOG.md`; document any reused public tools and their license.

## Suggested time
0–10 min inspect/plan; 10–55 min implement; 55–75 min tests; 75–90 min report/review.

## Scoring (100, practice only)
Requirements/plan 10; data integration/validation 20; correct decisions/output 25; security/refactor 10; tests 15; ML plan 15; documentation 5.

## Follow-up written questions (30 min, 5 min each; practice without AI)
1. Why use a unique equipment key and how detect duplicate joins?
2. Why is missing maintenance REVIEW rather than PASS?
3. Explain difference between <= and < with a boundary example.
4. How did you remove unsafe evaluation and verify behavior?
5. How would you prevent temporal leakage when predicting failure 24h ahead?
6. Which public libraries did you use, and how did you verify compliance with restrictions?
