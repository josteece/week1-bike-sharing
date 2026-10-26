"""Fit LS, LAD, NNLS, and NNLAD models of cnt ~ temp + hum + windspeed.

Uses only data/training.csv to estimate coefficients (per AGENTS.md), then
evaluates the four fitted models on data/testing.csv. Writes
output/submission.csv and a comparison figure to figures/.
"""

from __future__ import annotations

import csv
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import linprog, lsq_linear

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUTPUT = ROOT / "output"
FIGURES = ROOT / "figures"

PREDICTORS = ["temp", "hum", "windspeed"]
OUTCOME = "cnt"


def design_matrix(df: pd.DataFrame) -> np.ndarray:
    X = df[PREDICTORS].to_numpy(dtype=float)
    ones = np.ones((len(df), 1))
    return np.hstack([ones, X])


def fit_ls(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    return coef


def fit_nnls(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    # Intercept (column 0) unrestricted; slopes (columns 1..3) nonnegative.
    lower = [-np.inf, 0.0, 0.0, 0.0]
    upper = [np.inf, np.inf, np.inf, np.inf]
    result = lsq_linear(X, y, bounds=(lower, upper), method="trf", tol=1e-12, max_iter=10000)
    return result.x


def fit_lad(X: np.ndarray, y: np.ndarray, nonneg_slopes: bool) -> np.ndarray:
    """Minimize sum|residual| via linear programming.

    Variables: [b0, b1, b2, b3, u_1..u_n] where u_i >= |residual_i|.
    Minimize sum(u). Constraints per observation i, with pred_i = X_i . b:
      pred_i - u_i <= y_i
      -pred_i - u_i <= -y_i
    """
    n, p = X.shape  # p == 4 (intercept + 3 predictors)
    n_vars = p + n

    c = np.concatenate([np.zeros(p), np.ones(n)])

    A_ub = np.zeros((2 * n, n_vars))
    b_ub = np.zeros(2 * n)
    A_ub[:n, :p] = X
    A_ub[:n, p:] = -np.eye(n)
    b_ub[:n] = y
    A_ub[n:, :p] = -X
    A_ub[n:, p:] = -np.eye(n)
    b_ub[n:] = -y

    bounds = [(None, None)]  # intercept
    slope_bound = (0.0, None) if nonneg_slopes else (None, None)
    bounds += [slope_bound] * (p - 1)
    bounds += [(0.0, None)] * n  # u_i

    result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")
    if not result.success:
        raise RuntimeError(f"LAD linprog failed: {result.message}")
    return result.x[:p]


def predict(coef: np.ndarray, df: pd.DataFrame) -> np.ndarray:
    X = design_matrix(df)
    return X @ coef


def mae(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.mean(np.abs(y_true - y_pred)))


def rmse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))


def main() -> None:
    train = pd.read_csv(DATA / "training.csv")
    test = pd.read_csv(DATA / "testing.csv")

    X_train = design_matrix(train)
    y_train = train[OUTCOME].to_numpy(dtype=float)

    coefs = {
        "LS": fit_ls(X_train, y_train),
        "LAD": fit_lad(X_train, y_train, nonneg_slopes=False),
        "NNLS": fit_nnls(X_train, y_train),
        "NNLAD": fit_lad(X_train, y_train, nonneg_slopes=True),
    }

    # Verification: nonnegativity, finiteness.
    tol = 1e-8
    for name in ["NNLS", "NNLAD"]:
        slopes = coefs[name][1:]
        assert np.all(slopes >= -tol), f"{name} violated nonnegativity: {slopes}"
    for name, c in coefs.items():
        assert np.all(np.isfinite(c)), f"{name} produced non-finite coefficients: {c}"

    y_test = test[OUTCOME].to_numpy(dtype=float)
    metrics = {}
    for name, c in coefs.items():
        y_pred = predict(c, test)
        metrics[name] = {"MAE": mae(y_test, y_pred), "RMSE": rmse(y_test, y_pred)}

    OUTPUT.mkdir(exist_ok=True)
    with (OUTPUT / "submission.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["method", "b_0", "b_1_temp", "b_2_hum", "b_3_windspeed"])
        for name in ["LS", "LAD", "NNLS", "NNLAD"]:
            c = coefs[name]
            writer.writerow([name, *[f"{v:.6f}" for v in c]])

    print("Coefficients (b_0, b_1_temp, b_2_hum, b_3_windspeed):")
    for name, c in coefs.items():
        print(f"  {name:6s} {c}")
    print("\nTest-set metrics:")
    for name, m in metrics.items():
        print(f"  {name:6s} MAE={m['MAE']:.2f}  RMSE={m['RMSE']:.2f}")

    make_figure(coefs, test, metrics)


def make_figure(coefs: dict[str, np.ndarray], test: pd.DataFrame, metrics: dict[str, dict[str, float]]) -> None:
    import matplotlib.pyplot as plt

    FIGURES.mkdir(exist_ok=True)
    y_test = test[OUTCOME].to_numpy(dtype=float)

    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5))

    # Panel 1: actual vs predicted on the test set, one color per method.
    ax = axes[0]
    colors = {"LS": "#4C72B0", "LAD": "#DD8452", "NNLS": "#55A868", "NNLAD": "#C44E52"}
    for name, c in coefs.items():
        y_pred = predict(c, test)
        ax.scatter(y_test, y_pred, s=14, alpha=0.6, label=name, color=colors[name])
    lims = [min(y_test.min(), 0), y_test.max() * 1.05]
    ax.plot(lims, lims, color="gray", linestyle="--", linewidth=1, label="y = x")
    ax.set_xlabel("Actual daily rentals (test set)")
    ax.set_ylabel("Predicted daily rentals")
    ax.set_title("Actual vs. predicted, test set")
    ax.legend(fontsize=8)

    # Panel 2: test RMSE/MAE bar comparison.
    ax = axes[1]
    names = list(metrics.keys())
    x = np.arange(len(names))
    width = 0.35
    mae_vals = [metrics[n]["MAE"] for n in names]
    rmse_vals = [metrics[n]["RMSE"] for n in names]
    ax.bar(x - width / 2, mae_vals, width, label="MAE")
    ax.bar(x + width / 2, rmse_vals, width, label="RMSE")
    ax.set_xticks(x)
    ax.set_xticklabels(names)
    ax.set_ylabel("Rentals per day")
    ax.set_title("Test-set error by method")
    ax.legend(fontsize=8)

    fig.tight_layout()
    fig.savefig(FIGURES / "method_comparison.png", dpi=150)
    print(f"\nWrote {FIGURES / 'method_comparison.png'}")


if __name__ == "__main__":
    main()
