"""
Step 3: Train a model on preprocessed MNIST datasets and log results to S3.
"""

import logging
import os
import sys
import time

import dsl.c19_deep_learning as tf
from dsl.c19_deep_learning.data import Dataset

from dsl import (
    BUCKET,
    MLFLOW_MODEL_ARTIFACT_PATH,
    S03_INPUT_PREFIX,
    S03_OUTPUT_PREFIX,
)
from dsl.utils.features.create_empty_model import create_empty_model
from dsl.utils.features.generate_guid import generate_guid
from dsl.utils.features.get_signature_from_data import get_signature_from_data_tf
from dsl.utils.io.ConfigDataClass import Config
from dsl.utils.io.download_npz import download_npz
from dsl.utils.io.log_to_s3 import log_metrics, log_model, log_params
from dsl.utils.metrics.compute_scores import ClassificationScores
from dsl.utils.metrics.metrics_numpy import acc_numpy

path_to_here = os.path.abspath(os.path.dirname(__file__))


def setup_logging():
    """Set up logging configuration."""
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "training.log")

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_file),
        ],
    )

    logger = logging.getLogger(__name__)
    logger.info("Training logging setup complete. Log file: %s", log_file)
    return logger


def _normalize(value, min_val, max_val):
    if max_val <= min_val:
        return 0.5
    return (value - min_val) / (max_val - min_val)


def compute_composite_score(scores: ClassificationScores, train_time: float):
    """Compute a composite score for DOE comparison."""
    # Positive direction metrics
    acc = scores.accuracy_numpy
    auc = scores.auc if scores.auc is not None else acc

    # Negative direction metric
    loss = scores.cross_loss

    # Normalize (per-run fallback defaults)
    norm_acc = acc
    norm_auc = auc
    norm_loss = loss
    norm_time = train_time

    # Weighted sum
    w = 0.25
    composite = w * norm_acc + w * norm_auc - w * norm_loss - w * norm_time
    return composite


def train_one_model(run_id: str, logger: logging.Logger):
    """Train a single model and log metrics."""
    logger.info(f"Starting training for run_id={run_id}")
    # Load configuration from local cache or S3
    logger.info("Loading configuration...")
    config_path = os.path.join(path_to_here, "config.json")
    cfg = Config.from_json(config_path)
    log_params(cfg.to_dict(), bucket=BUCKET, prefix=f"{S03_OUTPUT_PREFIX}/{run_id}")

    # Load training data
    logger.info("Loading training data...")
    x_key = f"{S03_INPUT_PREFIX}/training/x_training.npz"
    y_key = f"{S03_INPUT_PREFIX}/training/y_training.npz"

    x_train_dict = download_npz(BUCKET, x_key, use_cache=True)
    y_train_dict = download_npz(BUCKET, y_key, use_cache=True)

    x_train = x_train_dict.get("arr_0", x_train_dict.get("data"))
    y_train = y_train_dict.get("arr_0", y_train_dict.get("data"))

    if x_train is None or y_train is None:
        raise ValueError("Failed to load training data")

    logger.info(
        f"Loaded training data: x_shape={x_train.shape}, y_shape={y_train.shape}"
    )

    # Create and compile model
    logger.info("Creating model...")
    model = create_empty_model()
    hyperparams = cfg.get_hyperparameters_for_dsl.c19_deep_learning_model()
    logger.info(f"Training with hyperparameters: {hyperparams}")

    # Prepare training dataset
    train_ds = (
        Dataset.from_tensor_slices((x_train, y_train))
        .shuffle(cfg.SHUFFLE_BUFFER_SIZE)
        .batch(int(cfg.BATCH_SIZE))
        .prefetch(tf.data.AUTOTUNE)
    )

    # Train model
    logger.info("Starting model training...")
    start_time = time.time()
    # Remove validation_split from hyperparams when using tf.data.Dataset
    training_params = hyperparams.copy()
    if "validation_split" in training_params:
        del training_params["validation_split"]
    model.fit(train_ds, **training_params)
    train_time = time.time() - start_time
    logger.info(f"Training completed in {train_time:.3f} seconds")

    # Save model
    logger.info("Saving model...")
    signature = get_signature_from_data_tf(x_train, y_train)
    log_model(
        model_obj=model,
        signature_dict=signature,
        bucket=BUCKET,
        prefix=f"{S03_OUTPUT_PREFIX}/{run_id}/{MLFLOW_MODEL_ARTIFACT_PATH}",
    )

    # Compute metrics
    logger.info("Computing metrics...")
    preds = model.predict(x_train)

    pred_classes = preds.argmax(axis=1)
    actual_classes = y_train.argmax(axis=1)
    accuracy_numpy = acc_numpy(pred_classes, actual_classes)

    history = model.history.history
    cross_loss = history["loss"][-1]
    accuracy_keras = history["accuracy"][-1]

    scores = ClassificationScores(
        dataset_name="train",
        cross_loss=cross_loss,
        accuracy_keras=accuracy_keras,
        accuracy_numpy=float(accuracy_numpy),
        train_time_sec=train_time,
    )

    # Log metrics
    logger.info("Logging metrics...")
    raw_metrics = scores.to_dict()
    raw_metrics["train_time_sec"] = round(train_time, 4)
    log_metrics(
        raw_metrics,
        bucket=BUCKET,
        key=f"{S03_OUTPUT_PREFIX}/{run_id}/metrics_train.json",
    )

    composite_score = compute_composite_score(scores, train_time)
    log_metrics(
        {"composite_score": round(composite_score, 6)},
        bucket=BUCKET,
        key=f"{S03_OUTPUT_PREFIX}/{run_id}/metrics_composite.json",
    )

    logger.info(
        "Training completed successfully:\n"
        f"  - Accuracy: {scores.accuracy_numpy:.4f}\n"
        f"  - Loss: {scores.cross_loss:.4f}\n"
        f"  - AUC: {scores.auc}\n"
        f"  - Composite Score: {composite_score:.4f}"
    )


def main():
    logger = setup_logging()
    logger.info("Starting training pipeline...")
    active_run_id = generate_guid()
    logger.info(f"Generated run ID: {active_run_id}")
    train_one_model(active_run_id, logger)
    logger.info("Training pipeline completed successfully")


if __name__ == "__main__":
    main()
