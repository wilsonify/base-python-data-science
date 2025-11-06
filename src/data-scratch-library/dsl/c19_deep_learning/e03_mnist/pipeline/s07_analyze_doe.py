"""
Analyze Reinforcement DOE results from S3.
Loads hyperparameters and ClassificationScores for each run.
Generates descriptive plots and summarizes the best performing model.
"""

import logging
import os
from logging.config import dictConfig
from pprint import pprint
from typing import Any, Dict

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from dsl import BUCKET, S06_OUTPUT_PREFIX, logging_config_dict
from dsl.io_library.ConfigDataClass import Config
from dsl.io_library.list_objects_s3 import list_objects_s3
from dsl.metrics_library.compute_scores import ClassificationScores

path_to_here = os.path.abspath(os.path.dirname(__file__))
PLOTS_DIR = os.path.join(path_to_here, "doe_analysis_plots")
os.makedirs(PLOTS_DIR, exist_ok=True)


def get_completed_runs() -> Dict[str, Dict[str, Any]]:
    """Returns run_id -> {config, metrics} loaded from S3 results."""
    runs: Dict[str, Dict[str, Any]] = {}
    objects = list_objects_s3(BUCKET, S06_OUTPUT_PREFIX)

    # all run directories: prefix/run_id/
    prefixes = sorted({os.path.dirname(o) for o in objects})

    for prefix in prefixes:
        run_id = prefix.split("/")[-1]
        cfg_key = f"{prefix}/config.json"
        metrics_key = f"{prefix}/metrics_train.json"

        if cfg_key not in objects or metrics_key not in objects:
            continue

        try:
            cfg = Config.from_json_s3(BUCKET, cfg_key)
            metrics = ClassificationScores.from_json_s3(BUCKET, metrics_key)
            runs[run_id] = {
                "config": cfg,
                "metrics": metrics,
            }
        except Exception as e:
            logging.warning(f"Failed to load data for run {run_id}: {e}")

    logging.info(f"Discovered {len(runs)} completed runs.")
    return runs


def build_dataframe(runs: Dict[str, Dict[str, Any]]) -> pd.DataFrame:
    """Flatten config + metrics into a single tidy DataFrame."""
    rows = []
    for run_id, data in runs.items():
        row = {"run_id": run_id}
        row.update(data["config"])
        row.update(data["metrics"])
        rows.append(row)
    return pd.DataFrame(rows)


def rank_and_summarize(df: pd.DataFrame):
    """Print best model and key stat summaries."""
    metric = (
        "train_cross_entropy_loss"
        if "train_cross_entropy_loss" in df.columns
        else df.columns[-1]
    )
    best = df.sort_values(metric, ascending=True).iloc[0]

    print("\n=== Best Model Summary ===")
    print(f"Minimizing metric: {metric}")
    print(f"Best run_id: {best['run_id']}")
    print(f"Score: {best[metric]:.5f}")
    print("\nHyperparameters:")
    hp_cols = [c for c in df.columns if c not in ["run_id", metric]]
    pprint({c: best[c] for c in hp_cols})


def plot_metric_history(df: pd.DataFrame):
    metric_cols = [c for c in df.columns if "loss" in c or "acc" in c]
    if not metric_cols:
        logging.warning("No recognizable metric columns found.")
        return

    metric = metric_cols[0]
    df_sorted = df.sort_values(metric)

    plt.figure(figsize=(8, 5))
    plt.plot(df_sorted[metric].values, marker="o")
    plt.xlabel("Rank index")
    plt.ylabel(metric)
    plt.title("Optimization History (sorted by performance)")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "optimization_history.png"))
    plt.close()


def plot_param_relationships(df: pd.DataFrame):
    # Select only numeric columns for plotting
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    plot_cols = [c for c in numeric_cols if c not in ["run_id"]]

    if len(plot_cols) > 1:  # Need at least 2 columns for a pair plot
        plt.figure(figsize=(10, 6))
        sns.pairplot(df, vars=plot_cols, diag_kind="kde")
        plt.savefig(os.path.join(PLOTS_DIR, "param_relationships.png"))
        plt.close()
    else:
        logging.warning("Not enough numeric columns for pair plot")


def compute_param_importance(df: pd.DataFrame):
    from sklearn.ensemble import RandomForestRegressor

    invalid_predictors = [
        "train_cross_entropy_loss",
        "train_cross_loss",
        "train_accuracy_keras",
        "train_accuracy_numpy",
        "train_auc",
        "run_id",
    ]
    metric = (
        "train_cross_entropy_loss"
        if "train_cross_entropy_loss" in df.columns
        else df.columns[-1]
    )

    # Select only numeric columns and simple categorical columns
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
    hp_cols = [c for c in numeric_cols if c not in invalid_predictors]

    if len(hp_cols) < 2:
        logging.warning("Not enough numeric hyperparameters for importance analysis")
        return

    # Create feature matrix with only numeric columns
    X = df[hp_cols].copy()
    y = df[metric]

    rf = RandomForestRegressor(
        n_estimators=200, random_state=42, min_samples_leaf=1, max_features=20
    )
    rf.fit(X, y)
    importances = pd.DataFrame(
        {"Hyperparameter": hp_cols, "Importance": rf.feature_importances_}
    ).sort_values("Importance", ascending=False)

    plt.figure(figsize=(8, 6))
    sns.barplot(data=importances, x="Importance", y="Hyperparameter", palette="viridis")
    plt.title("Estimated Hyperparameter Importance (RF)")
    plt.tight_layout()
    plt.savefig(os.path.join(PLOTS_DIR, "hyperparameter_importance.png"))
    plt.close()


def main():
    dictConfig(logging_config_dict)
    logging.getLogger().setLevel(logging.INFO)

    runs = get_completed_runs()
    if not runs:
        raise RuntimeError("No completed runs found in S3.")

    df = build_dataframe(runs)

    rank_and_summarize(df)
    plot_metric_history(df)
    plot_param_relationships(df)
    compute_param_importance(df)

    print(f"\nAll plots saved to: {PLOTS_DIR}")


if __name__ == "__main__":
    main()
