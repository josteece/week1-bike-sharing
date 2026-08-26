# Output submission

`submission.csv` is a Kaggle-style submission template for the regression exercise. It uses one header row, one row per method, and no extra index column.

Each participant should replace the blank fields with the fitted coefficients from:

```text
predicted cnt = b_0 + b_1_temp(temp) + b_2_hum(hum) + b_3_windspeed(windspeed)
```

Keep the column names, method names, and row order unchanged. Enter plain numeric values only. The intercept `b_0` is unrestricted; the three predictor coefficients must be nonnegative for NNLS and NNLAD.

Kaggle competitions normally define their exact required schema in a provided `sample_submission.csv`. For this classroom exercise, `submission.csv` is the authoritative schema.
