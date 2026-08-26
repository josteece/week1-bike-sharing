# Week 1: Bike Sharing

This project uses the [UCI Bike Sharing dataset](https://doi.org/10.24432/C5W894), created by Hadi Fanaee-T. It contains hourly and daily counts of rental bikes from the Capital Bikeshare system during 2011 and 2012, together with weather, seasonal, and calendar information. The dataset is suitable for regression questions such as predicting bike demand from temperature, humidity, wind speed, and whether a day is a working day.

## Suggested first regression

For this introductory exercise, predict total bike rentals using three weather measurements:

- Outcome: `cnt` — total number of bike rentals
- Predictor: `temp` — normalized temperature
- Predictor: `hum` — normalized humidity
- Predictor: `windspeed` — normalized wind speed

Do not use `casual` or `registered` as predictors of `cnt`: those two columns add up exactly to `cnt`, so they would reveal the outcome rather than provide a meaningful prediction. It is also sensible to leave out `atemp` initially because it measures something very similar to `temp`.

## Participant task

Your task is to estimate four versions of this linear model:

```text
predicted cnt = b_0 + b_1(temp) + b_2(hum) + b_3(windspeed)
```

Use `data/training.csv` to find `b_0`, `b_1`, `b_2`, and `b_3` for each method:

1. **Least Squares (LS):** minimize the sum of squared residuals.
2. **Least Absolute Deviation (LAD):** minimize the sum of absolute residuals.
3. **Nonnegative Least Squares (NNLS):** minimize the sum of squared residuals while requiring `b_1`, `b_2`, and `b_3` to be nonnegative.
4. **Nonnegative Least Absolute Deviation (NNLAD):** minimize the sum of absolute residuals while requiring `b_1`, `b_2`, and `b_3` to be nonnegative.

The intercept `b_0` is unrestricted in all four methods. The date column `dteday` identifies an observation but is not a predictor.

### Steps

1. Inspect `data/training.csv` and confirm the meanings and ranges of the variables.
2. Fit all four methods using only the training data.
3. Compare their coefficients and explain why some coefficients change or become zero under the nonnegative constraint.
4. Optionally use `data/validation.csv` to compare out-of-sample errors. Discuss whether a validation set is actually needed when there are no tuning choices.
5. Use `data/testing.csv` only for a final evaluation after your analysis choices are complete.
6. Enter your four sets of coefficients in `output/submission.csv`.

The completed submission should retain this exact structure:

```csv
method,b_0,b_1_temp,b_2_hum,b_3_windspeed
LS,...,...,...,...
LAD,...,...,...,...
NNLS,...,...,...,...
NNLAD,...,...,...,...
```

Replace each `...` with a numeric coefficient. Do not change the header, method names, or row order, and do not add an index column. Your coding agent may help you implement and test the methods, but you should be able to explain the loss function, constraints, and resulting coefficients.

The original files are stored in `resources/`:

- `day.csv` — daily observations
- `hour.csv` — hourly observations
- `README.md` — the UCI data dictionary, attribution, and license information in Markdown

The dataset is distributed by the UCI Machine Learning Repository under the [Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/).

Citation: Fanaee-T, H. (2013). *Bike Sharing* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894
