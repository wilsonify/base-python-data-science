"""
Evaluate one or multiple models using dsl.c19_deep_learning 2.20
Loads model weights from NPZ files and computes structured metrics."""

import logging
import os
import tempfile
from logging.config import dictConfig
from pprint import pprint

from dsl import (
    BUCKET,
    MLFLOW_MODEL_ARTIFACT_PATH,
    S03_OUTPUT_PREFIX,
    S04_INPUT_DATA_PREFIX,
    S04_INPUT_MODEL_PREFIX,
    S04_OUTPUT_PREFIX,
    logging_config_dict,
)
from dsl.utils.features.create_empty_model import create_empty_model
from dsl.utils.features.get_nda_to_tensor import get_nda_to_tensor
from dsl.utils.io import Config, download_npz
from dsl.utils.io.list_objects_s3 import list_objects_s3
from dsl.utils.io.log_to_s3 import (
    log_metrics,
    log_model,
    read_saved_weights_from_s3,
)
from dsl.utils.metrics import ClassificationScores


def evaluate_run(run_id: str):
    """Evaluate a single run and log metrics to S3."""
    logging.info(f"Evaluating run_id={run_id}")

    logging.info("Loading configuration for reference")
    cfg = Config.from_json_s3(
        bucket=BUCKET, key=f"{S04_INPUT_MODEL_PREFIX}/{run_id}/config.json"
    )
    pprint(cfg)

    logging.info("Loading model and weights from S3")
    model_prefix = (
        f"{S04_INPUT_MODEL_PREFIX}/{run_id}/{MLFLOW_MODEL_ARTIFACT_PATH}/weights"
    )
    model = read_saved_weights_from_s3(
        BUCKET, model_prefix, model_fn=create_empty_model
    )

    logging.info("Loading evaluation data")
    x_test_dict = download_npz(
        BUCKET, f"{S04_INPUT_DATA_PREFIX}/evaluation/x_evaluation.npz"
    )
    y_test_dict = download_npz(
        BUCKET, f"{S04_INPUT_DATA_PREFIX}/evaluation/y_evaluation.npz"
    )

    x_test_nda = x_test_dict.get("arr_0")
    y_test_nda = y_test_dict.get("arr_0")
    assert (
        x_test_nda is not None
    ), "Failed to load evaluation data from NPZ files for x_test"
    assert (
        y_test_nda is not None
    ), "Failed to load evaluation data from NPZ files for y_test"

    x_test_tensor = get_nda_to_tensor(x_test_nda)
    y_test_tensor = get_nda_to_tensor(y_test_nda)

    logging.info(
        f"x_test shape: {x_test_tensor.shape}, y_test shape: {y_test_tensor.shape}"
    )

    logging.info("Making predictions")
    preds_nda = model.predict(x_test_tensor)

    logging.info("Computing metrics using ClassificationScores")
    scores = ClassificationScores.from_compute_scores(
        predicted_nda=preds_nda, actual_nda=y_test_nda, dataset_name="test"
    )
    metrics_dict = scores.to_dict()

    logging.info("Logging metrics to S3")
    log_metrics(
        metrics_dict,
        bucket=BUCKET,
        key=f"{S04_OUTPUT_PREFIX}/{run_id}/metrics_test.json",
    )
    logging.info(f"Logged metrics for run_id={run_id}: {metrics_dict}")

    logging.info("Optionally logging the model again for reference")
    log_model(
        model_obj=model,
        signature_dict={
            "inputs": model.input_shape[1:],
            "outputs": model.output_shape[1:],
        },
        bucket=BUCKET,
        prefix=f"{S04_OUTPUT_PREFIX}/{run_id}/{MLFLOW_MODEL_ARTIFACT_PATH}",
        local_dir=os.path.join(
            tempfile.mkdtemp(prefix="mlflow_eval_"), run_id, MLFLOW_MODEL_ARTIFACT_PATH
        ),
    )


def extract_run_id_from_s3_key(s3_key: str):
    """Extract run_id from a given S3 key."""
    return s3_key.replace(S03_OUTPUT_PREFIX + "/", "").split("/")[0]


def evaluate_all_runs():
    """Evaluate all models stored under the input model prefix."""
    logging.info("Listing all run IDs to evaluate from S3...")
    s3_objects = list_objects_s3(
        bucket=BUCKET, prefix=S04_INPUT_MODEL_PREFIX, glob_pattern="*"
    )
    unique_run_ids = sorted({extract_run_id_from_s3_key(obj) for obj in s3_objects})

    logging.info(f"Found {len(unique_run_ids)} unique run IDs: {unique_run_ids}")

    for run_id in unique_run_ids:
        try:
            evaluate_run(run_id)
        except Exception:
            logging.exception(f"Evaluation failed for run_id={run_id}")
            continue


if __name__ == "__main__":
    dictConfig(logging_config_dict)
    logging.getLogger().setLevel(logging.INFO)
    evaluate_all_runs()
