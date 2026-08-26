# Regression Methods Report

This file is the report template for the activity. Complete it using results from your own analysis; do not include unsupported claims or results copied from another group.

## Deliverables

Submit:

1. This completed `REPORT.md` file.
2. The completed `output/submission.csv` coefficient file.
3. Any figure files referenced by the report, stored in a `figures/` folder.

Keep the report concise: approximately 800 words or fewer, excluding tables and figure captions. Use one coefficient table, one performance table, and at least one meaningful figure.

## 1. Question and experimental design

<!-- State the prediction question, outcome, three predictors, regression equation, and how the training and testing sets were used. Mention that this is a random-split methods exercise rather than a genuine future forecast. -->

## 2. Methods

Describe each method in your own words. Explain both its loss function and when its assumptions would be appropriate.

| Method | What it minimizes | Coefficient constraints | When it may be appropriate |
|---|---|---|---|
| LS |  |  |  |
| LAD |  |  |  |
| NNLS |  |  |  |
| NNLAD |  |  |  |

Also explain why changing the loss function is different from constraining the coefficients.

## 3. Estimated coefficients

Report the coefficients estimated from `data/training.csv`.

| Method | `b_0` | `b_1_temp` | `b_2_hum` | `b_3_windspeed` |
|---|---:|---:|---:|---:|
| LS |  |  |  |  |
| LAD |  |  |  |  |
| NNLS |  |  |  |  |
| NNLAD |  |  |  |  |

<!-- Interpret important signs, differences, and coefficients that are zero or close to zero. Do not assume that a constrained zero means the predictor is irrelevant. -->

## 4. Test-set performance

Evaluate predictions on `data/testing.csv` using coefficients learned from the training set. Report mean absolute error as the L1-based measure and root mean squared error as the L2-based measure.

| Method | Test MAE | Test RMSE |
|---|---:|---:|
| LS |  |  |
| LAD |  |  |
| NNLS |  |  |
| NNLAD |  |  |

<!-- Compare the methods without treating a small numerical difference as automatically important. Report errors in rentals per day. -->

## 5. Graphical evidence

Include at least one graph that helps compare the methods. Good choices include actual versus predicted test values, a coefficient comparison, or residual distributions.

<!-- Insert the figure using Markdown, for example: ![Concise description](figures/your-figure.png) -->

Provide a caption and explain what the graph contributes beyond the tables.

## 6. Recommended method

<!-- Determine which method makes the most sense in this context. Support the recommendation with test performance, coefficient behavior, and whether the nonnegative constraint is plausible. Distinguish predictive association from causation. -->

## 7. Was validation needed?

<!-- Discuss whether `data/validation.csv` was necessary for this fixed four-method exercise. Explain how the answer would change if validation results were used to select predictors, transformations, tuning parameters, or a preferred model. -->

## 8. Something interesting

<!-- Add one evidence-based observation or question of your choice. Examples of directions—not answers—include an unusual residual, coefficient stability, nonlinearity, omitted variables, seasonal errors, or random versus chronological splitting. -->

## Reproducibility note

<!-- Identify the software or packages used and any numerical tolerances or solver settings needed to reproduce the results. -->

