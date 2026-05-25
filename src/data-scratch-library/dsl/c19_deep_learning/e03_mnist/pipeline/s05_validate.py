"""
Evaluate one or multiple models using dsl.c19_deep_learning 2.20
Loads model weights from NPZ files and logs structured metrics."""

import logging
import os
import tempfile
from logging.config import dictConfig
from pprint import pprint
from typing import List, Optional, Set

from dsl import (
    BUCKET,
    MLFLOW_MODEL_ARTIFACT_PATH,
    S04_INPUT_DATA_PREFIX,
    S04_INPUT_MODEL_PREFIX,
    S04_OUTPUT_PREFIX,
    S05_INPUT_MODEL_PREFIX,
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


def load_validation_data():
    """Load validation data from S3."""
    x_val_dict = download_npz(
        BUCKET, f"{S04_INPUT_DATA_PREFIX}/validation/x_validation.npz"
    )
    y_val_dict = download_npz(
        BUCKET, f"{S04_INPUT_DATA_PREFIX}/validation/y_validation.npz"
    )

    x_val_nda = x_val_dict.get("arr_0")
    y_val_nda = y_val_dict.get("arr_0")
    if x_val_nda is None or y_val_nda is None:
        raise ValueError("Failed to load validation data from NPZ files")

    x_val_tensor = get_nda_to_tensor(x_val_nda)
    y_val_tensor = get_nda_to_tensor(y_val_nda)
    logging.info(
        f"Loaded validation data: x_val={x_val_tensor.shape}, y_val={y_val_tensor.shape}"
    )
    return x_val_tensor, y_val_tensor


def evaluate_model(model, x_val_tensor, y_val_tensor, run_id: str):
    """Evaluate a model and save validation metrics."""
    preds_nda = model.predict(x_val_tensor)

    scores = ClassificationScores.from_compute_scores(
        predicted_nda=preds_nda, actual_nda=y_val_tensor.numpy(), dataset_name="val"
    )
    metrics_dict = scores.to_dict()

    log_metrics(
        metrics_dict,
        bucket=BUCKET,
        key=f"{S04_OUTPUT_PREFIX}/{run_id}/metrics_val.json",
    )
    logging.info(f"Logged validation metrics for run_id={run_id}: {metrics_dict}")

    log_model(
        model_obj=model,
        signature_dict={
            "inputs": model.input_shape[1:],
            "outputs": model.output_shape[1:],
        },
        bucket=BUCKET,
        prefix=f"{S04_OUTPUT_PREFIX}/{run_id}/{MLFLOW_MODEL_ARTIFACT_PATH}",
        local_dir=os.path.join(
            tempfile.mkdtemp(prefix="mlflow_valid_"), run_id, MLFLOW_MODEL_ARTIFACT_PATH
        ),
    )


def load_model_config(run_id: str) -> Optional[Config]:
    """Load model configuration from S3."""
    try:
        config = Config.from_json_s3(
            bucket=BUCKET, key=f"{S04_INPUT_MODEL_PREFIX}/{run_id}/config.json"
        )
        return config
    except Exception as e:
        logging.warning(f"Failed to load config for run {run_id}: {e}")
        return None


def check_weights_exist(run_id: str, objects: List[str]) -> bool:
    """Check if model weights exist in S3."""
    weights_prefix = (
        f"{S04_INPUT_MODEL_PREFIX}/{run_id}/{MLFLOW_MODEL_ARTIFACT_PATH}/weights"
    )
    return any(obj.startswith(weights_prefix) for obj in objects)


def is_valid_run(run_id: str, objects: List[str]) -> bool:
    """Determine if a run is valid based on config and weights."""
    config = load_model_config(run_id)
    if config is None:
        return False
    if not check_weights_exist(run_id, objects):
        logging.warning(f"Weights missing for run {run_id}")
        return False
    return True


def extract_run_id(obj: str) -> Optional[str]:
    """Extract run ID from an S3 object key."""
    if not obj.endswith("config.json"):
        return None
    parts = obj.replace(S04_INPUT_MODEL_PREFIX + "/", "").split("/")
    return parts[0] if parts else None


def find_valid_runs(objects: List[str]) -> Set[str]:
    """Return all valid run IDs from S3 objects."""
    return {
        run_id
        for obj in objects
        if (run_id := extract_run_id(obj)) and is_valid_run(run_id, objects)
    }


def main_eval_one(run_id: str):
    """Evaluate a single model run."""
    logging.info(f"Evaluating run_id={run_id}")
    cfg = load_model_config(run_id)
    assert cfg is not None, f"Invalid configuration for run {run_id}"
    pprint(cfg)

    model_prefix = (
        f"{S04_INPUT_MODEL_PREFIX}/{run_id}/{MLFLOW_MODEL_ARTIFACT_PATH}/weights"
    )

    model = read_saved_weights_from_s3(
        BUCKET, model_prefix, model_fn=create_empty_model
    )

    x_val_tensor, y_val_tensor = load_validation_data()

    evaluate_model(model, x_val_tensor, y_val_tensor, run_id)


def main_eval_all():
    """Evaluate all valid model runs in S3."""
    objects = list_objects_s3(
        bucket=BUCKET, prefix=S05_INPUT_MODEL_PREFIX, glob_pattern="*"
    )
    logging.info(f"Found {len(objects)} objects in S3 under {S05_INPUT_MODEL_PREFIX}")

    valid_runs = find_valid_runs(objects)
    run_ids = sorted(valid_runs)
    logging.info(f"Found {len(run_ids)} valid runs to evaluate")

    for i, run_id in enumerate(run_ids):
        try:
            logging.info(f"Evaluating {i + 1}/{len(run_ids)}: {run_id}")
            main_eval_one(run_id)
        except Exception as e:
            logging.exception(f"Error evaluating run {run_id}")
            continue


if __name__ == "__main__":
    dictConfig(logging_config_dict)
    logging.getLogger().setLevel(logging.INFO)
    main_eval_all()
