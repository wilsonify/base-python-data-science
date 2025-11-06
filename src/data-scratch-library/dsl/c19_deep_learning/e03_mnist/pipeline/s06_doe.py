"""
DOE optimization using Optuna.
"""

import logging
import os
from logging.config import dictConfig
from time import sleep

import optuna
from optuna.trial import Trial

from dsl import (
    BUCKET,
    S02_INPUT_PREFIX,
    S03_OUTPUT_PREFIX,
    S06_INPUT_PREFIX,
    S06_OUTPUT_PREFIX,
    logging_config_dict,
)
from dsl.io_library.ConfigDataClass import Config
from dsl.io_library.download_npz import download_npz
from dsl.io_library.log_to_s3 import log_params
from dsl.s03_train_sans_mlflow import train_one_model
from dsl.utils.features.generate_guid import generate_guid
from dsl.utils.features.get_nda_to_tensor import get_nda_to_tensor
from dsl.utils.features.get_signature_from_data import get_signature_from_data

path_to_here = os.path.abspath(os.path.dirname(__file__))
CONFIG_PATH = os.path.join(path_to_here, "config.json")


def validate_environment():
    logging.info("Validating environment...")
    logging.info(
        f"S06_INPUT_PREFIX: {S06_INPUT_PREFIX}, S06_OUTPUT_PREFIX: {S06_OUTPUT_PREFIX}, BUCKET: {BUCKET}"
    )
    logging.info(f"Config path: {CONFIG_PATH}, Working directory: {os.getcwd()}")


def verify_s3_training_data():
    required_files = [
        f"{S06_INPUT_PREFIX}/training/x_training.npz",
        f"{S06_INPUT_PREFIX}/training/y_training.npz",
    ]
    from dsl.io_library.list_objects_s3 import list_objects_s3

    objects = list_objects_s3(BUCKET, S06_INPUT_PREFIX)
    for file in required_files:
        if file not in objects:
            raise FileNotFoundError(f"Missing S3 file: s3://{BUCKET}/{file}")


def load_training_data():
    x_train_np = download_npz(BUCKET, f"{S06_INPUT_PREFIX}/training/x_training.npz")[
        "arr_0"
    ]
    y_train_np = download_npz(BUCKET, f"{S06_INPUT_PREFIX}/training/y_training.npz")[
        "arr_0"
    ]
    logging.info(
        f"x_train shape: {x_train_np.shape}, y_train shape: {y_train_np.shape}"
    )

    x_tensor = get_nda_to_tensor(x_train_np)
    y_tensor = get_nda_to_tensor(y_train_np)

    signature = get_signature_from_data(x_train_np, y_train_np)
    logging.info(f"Inferred data signature: {signature}")
    return x_tensor, y_tensor


def objective(trial: Trial, base_config: Config, study_id: str) -> float:
    """Optuna objective function to minimize validation loss."""
    batch_size = trial.suggest_categorical("BATCH_SIZE", [128, 256])
    epochs = trial.suggest_categorical("EPOCHS", [10, 50, 100])
    validation_split = trial.suggest_float("VALIDATION_SPLIT", 0.0, 0.5)
    shuffle = trial.suggest_categorical("SHUFFLE", [True, False])
    class_weight_option = trial.suggest_categorical(
        "CLASS_WEIGHT", [None, {0: 0.1, 1: 0.9}]
    )
    steps_per_epoch = trial.suggest_categorical("STEPS_PER_EPOCHS", [None, 1])

    run_id = generate_guid()

    cfg = Config(
        SEED=base_config.SEED,
        SHUFFLE_BUFFER_SIZE=100,
        BATCH_SIZE=batch_size,
        EPOCHS=epochs,
        VALIDATION_SPLIT=validation_split,
        SHUFFLE=shuffle,
        CLASS_WEIGHT=class_weight_option,
        STEPS_PER_EPOCHS=steps_per_epoch,
    )

    trial_prefix = f"{S06_OUTPUT_PREFIX}/{study_id}/{run_id}"

    log_params(
        {
            "STUDY_ID": study_id,
            "RUN_ID": run_id,
            **cfg.__dict__,
        },
        bucket=BUCKET,
        prefix=trial_prefix,
    )

    sleep(2)

    try:
        train_one_model(run_id)
        metrics_key = f"{trial_prefix}/metrics_train.json"
        metrics_obj = download_npz(BUCKET, metrics_key)
        val_loss = metrics_obj.get("train_cross_loss", 1.0)
        return val_loss
    except Exception as e:
        logging.error(f"Trial failed [{run_id}]: {e}")
        return float("inf")


def main():
    dictConfig(logging_config_dict)
    logging.getLogger().setLevel(logging.DEBUG)

    validate_environment()
    verify_s3_training_data()

    base_config = Config.from_json(CONFIG_PATH)

    study_id = generate_guid()
    logging.info(f"StudyID: {study_id}")

    log_params(
        {"STUDY_ID": study_id}, bucket=BUCKET, prefix=f"{S06_OUTPUT_PREFIX}/{study_id}"
    )
    sleep(1)

    study = optuna.create_study(
        direction="minimize",
        study_name=f"DOE_Optuna_{study_id}",
    )

    study.optimize(
        lambda trial: objective(trial, base_config, study_id),
        timeout=3600,
    )

    best_trial = study.best_trial
    logging.info(f"Best hyperparameters: {best_trial.params}")
    logging.info(f"Best objective value (train loss): {best_trial.value}")

    best_prefix = f"{S06_OUTPUT_PREFIX}/{study_id}/best_trial"
    log_params(
        {
            "BEST_STUDY_TRIAL_PARAMS": best_trial.params,
            "BEST_STUDY_VALUE": best_trial.value,
        },
        bucket=BUCKET,
        prefix=best_prefix,
    )


if __name__ == "__main__":
    main()
