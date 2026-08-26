# Curated daily bike-sharing data

These files are derived from `resources/day.csv`, the daily portion of the UCI Bike Sharing dataset. They retain five columns:

- `dteday` — observation date, included as an identifier rather than a predictor
- `temp` — normalized temperature; predictor
- `hum` — normalized humidity; predictor
- `windspeed` — normalized wind speed; predictor
- `cnt` — total daily bike rentals; outcome

## Random split

The 731 daily observations were shuffled with random seed `42` and divided approximately 60/20/20:

| File | Purpose | Rows | Share |
|---|---|---:|---:|
| `training.csv` | Estimate model coefficients | 439 | 60.1% |
| `validation.csv` | Compare methods or experimental choices | 146 | 20.0% |
| `testing.csv` | Final evaluation | 146 | 20.0% |

Every source observation appears in exactly one split. This random split supports a regression-methods exercise; it should not be interpreted as a realistic future-demand forecasting design.

Validation is not strictly necessary when fitting only the four specified models with no tuning. It is included to support classroom discussion about model selection, experimentation, and when a separate validation set is useful.

## Regression exercise

Estimate the intercept and weights in:

```text
predicted cnt = intercept + b_temp × temp + b_hum × hum + b_windspeed × windspeed
```

Compare:

1. Least Squares (LS)
2. Least Absolute Deviation (LAD)
3. Nonnegative Least Squares (NNLS)
4. Nonnegative Least Absolute Deviation (NNLAD)

For NNLS and NNLAD, constrain the three predictor weights to be nonnegative while leaving the intercept unrestricted.

Source: Fanaee-T, H. (2013). *Bike Sharing* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894. Licensed CC BY 4.0.
