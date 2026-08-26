# Instructions for coding agents

## Purpose

Help a participant complete the bike-sharing regression activity and its report. Perform the analysis only when the participant explicitly asks. Do not insert reference answers, precomputed coefficients, performance values, or completed interpretations into the starter project in advance.

## Read first

Before working, read:

1. `README.md` for the activity and submission requirements.
2. `data/README.md` for the curated columns and split procedure.
3. `output/README.md` for the coefficient submission schema.
4. `REPORT.md` for the required report structure.

## Data boundaries

- Fit models using only `data/training.csv`.
- Use only `temp`, `hum`, and `windspeed` as predictors and `cnt` as the outcome.
- Treat `dteday` as an identifier, not a predictor.
- Do not use `casual`, `registered`, `atemp`, or other columns from the raw resources.
- Do not modify files in `resources/` or `data/`.
- Do not change the random splits or move observations between them.
- Validation is optional for the fixed exercise. If it is used to make modeling choices, say so in the report.
- Use `data/testing.csv` only for final evaluation after analysis choices are complete.

## Model specification

Use the same linear form for all methods:

```text
predicted cnt = b_0 + b_1(temp) + b_2(hum) + b_3(windspeed)
```

The intercept `b_0` is unrestricted in every method.

Implement and fit:

1. **LS:** minimize the sum of squared residuals with unrestricted slopes.
2. **LAD:** minimize the sum of absolute residuals with unrestricted slopes.
3. **NNLS:** minimize the sum of squared residuals subject to `b_1`, `b_2`, and `b_3 >= 0`.
4. **NNLAD:** minimize the sum of absolute residuals subject to `b_1`, `b_2`, and `b_3 >= 0`.

Use a suitable numerical solver for each objective. Do not obtain LAD by merely changing the reporting metric after fitting LS. Do not obtain a nonnegative solution by clipping negative coefficients after fitting an unconstrained model.

## Required outputs

When asked to complete the activity:

1. Write the fitted coefficients into `output/submission.csv` without changing its header, method names, row order, or adding an index column.
2. Calculate test MAE and test RMSE from predictions made with the training-derived coefficients.
3. Create at least one informative comparison figure and store it under `figures/`.
4. Complete the sections in `REPORT.md` using computed evidence.
5. Keep the report within its stated length and do not fabricate interpretation. Make the participant's judgment visible when the recommendation is subjective.

## Verification

Before declaring the task complete, verify that:

- All coefficient and metric values are finite numbers.
- Predictions use the exact equation and column order specified above.
- NNLS and NNLAD slopes satisfy the nonnegative constraint within a documented numerical tolerance.
- The intercept was not accidentally constrained.
- MAE and RMSE were computed on the testing set, not the training set.
- No target leakage or extra predictors were introduced.
- `submission.csv` parses as CSV and retains exactly five columns and four method rows.
- Every number and claim in `REPORT.md` agrees with the generated results.
- Figure labels, units, legends, and captions are readable and accurate.

Run relevant code or checks and report what was verified. Do not alter unrelated project files.
