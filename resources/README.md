# UCI Bike Sharing dataset: original resources

These files are the original hourly and daily data distributed with the [UCI Bike Sharing dataset](https://doi.org/10.24432/C5W894):

- `day.csv` — bike rentals aggregated by day; 731 observations
- `hour.csv` — bike rentals aggregated by hour; 17,379 observations

The records cover the Capital Bikeshare system in Washington, D.C., during 2011 and 2012. UCI combined rental counts with corresponding weather, calendar, and seasonal information. The dataset supports regression and event or anomaly-detection exercises.

## Columns

Both CSV files contain the following columns. `hr` appears only in `hour.csv`.

| Column | Description |
|---|---|
| `instant` | Sequential record index |
| `dteday` | Date |
| `season` | 1 = spring, 2 = summer, 3 = fall, 4 = winter |
| `yr` | 0 = 2011, 1 = 2012 |
| `mnth` | Month, 1–12 |
| `hr` | Hour, 0–23; hourly file only |
| `holiday` | 1 if the date is a holiday; otherwise 0 |
| `weekday` | Day of the week |
| `workingday` | 1 if the date is neither a weekend nor a holiday |
| `weathersit` | Encoded weather situation, described below |
| `temp` | Normalized temperature in Celsius; divided by 41 |
| `atemp` | Normalized apparent temperature in Celsius; divided by 50 |
| `hum` | Normalized humidity; divided by 100 |
| `windspeed` | Normalized wind speed; divided by 67 |
| `casual` | Count of casual-user rentals |
| `registered` | Count of registered-user rentals |
| `cnt` | Total rentals: `casual + registered` |

### Weather codes

| `weathersit` | Conditions |
|---:|---|
| 1 | Clear, few clouds, or partly cloudy |
| 2 | Mist and/or cloudy |
| 3 | Light snow or light rain, possibly with thunderstorms |
| 4 | Heavy rain, ice pellets, snow, fog, or similarly severe weather |

## Attribution and license

Creator: Hadi Fanaee-T, Laboratory of Artificial Intelligence and Decision Support, University of Porto.

Dataset citation:

> Fanaee-T, H. (2013). *Bike Sharing* [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5W894

Associated publication:

> Fanaee-T, H., & Gama, J. (2013). Event labeling combining ensemble detectors and background knowledge. *Progress in Artificial Intelligence*. https://doi.org/10.1007/s13748-013-0040-3

The UCI repository distributes this dataset under the [Creative Commons Attribution 4.0 International license](https://creativecommons.org/licenses/by/4.0/).
