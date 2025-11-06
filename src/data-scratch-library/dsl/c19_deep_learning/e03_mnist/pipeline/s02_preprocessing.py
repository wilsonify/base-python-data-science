"""
Step 2: Preprocess MNIST datasets (train, validation, evaluation)
using shared preprocessing functions.
"""

import logging
import os
import sys

import dsl.c19_deep_learning as tf

from dsl import BUCKET, S02_INPUT_PREFIX, S02_OUTPUT_PREFIX
from dsl.utils.features.get_nda_to_tensor import get_dataset_to_nda
from dsl.utils.features.shared_preprocess_data import (
    shared_preprocess_data_numpy,
    shared_preprocess_data_tf,
)
from dsl.utils.io.ConfigDataClass import Config
from dsl.utils.io.download_npz import download_npz
from dsl.utils.io.labels_np_to_json import labels_np_to_json
from dsl.utils.io.upload_npz import upload_npz

path_to_here = os.path.abspath(os.path.dirname(__file__))


def setup_logging():
    """Set up logging configuration."""
    # Ensure the log directory exists
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "preprocessing.log")

    # Configure root logger
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),  # Log to stdout
            logging.FileHandler(log_file),  # Log to file
        ],
    )

    # Create a logger for this module
    logger = logging.getLogger(__name__)
    logger.info("Logging setup complete. Logging to: %s", log_file)
    return logger


def process_split(cfg: Config, local_name: str) -> None:
    """Download, preprocess, and upload one dataset split."""
    logger = logging.getLogger(__name__)

    logger.info(f"Processing {local_name} split")

    # Try to load from local cache first, then S3
    x_key = f"{S02_INPUT_PREFIX}/{local_name}/x_{local_name}.npz"
    y_key = f"{S02_INPUT_PREFIX}/{local_name}/y_{local_name}.npz"

    logger.info(f"Loading {local_name} data...")
    x_dict = download_npz(BUCKET, x_key, use_cache=True)
    y_dict = download_npz(BUCKET, y_key, use_cache=True)

    x = x_dict.get("data", x_dict.get("arr_0"))
    y = y_dict.get("data", y_dict.get("arr_0"))

    assert x is not None, f"Failed to load data for {local_name} split x"
    assert y is not None, f"Failed to load data for {local_name} split y"

    logger.info(f"Loaded {local_name} data: x_shape={x.shape}, y_shape={y.shape}")

    # Apply preprocessing
    logger.info(f"Preprocessing {local_name} split...")
    x, y = shared_preprocess_data_numpy(x, y, cfg)
    ds = tf.data.Dataset.from_tensor_slices((x, y))
    ds = shared_preprocess_data_tf(ds, cfg)
    x_proc, y_proc = get_dataset_to_nda(ds)

    logger.info(f"Preprocessed {local_name} shapes: x={x_proc.shape}, y={y_proc.shape}")

    # Upload with S3 standard names
    output_x_key = f"{S02_OUTPUT_PREFIX}/{local_name}/x_{local_name}.npz"
    output_y_key = f"{S02_OUTPUT_PREFIX}/{local_name}/y_{local_name}.npz"
    output_y_json_key = f"{S02_OUTPUT_PREFIX}/{local_name}/y_{local_name}.json"

    logger.info(f"Saving processed {local_name} data...")
    upload_npz(BUCKET, output_x_key, x_proc, use_cache=True)
    upload_npz(BUCKET, output_y_key, y_proc, use_cache=True)
    labels_np_to_json(BUCKET, output_y_json_key, y_proc)

    logger.info(f"Completed {local_name} split processing")


def main():
    logger = setup_logging()
    logger.info("Starting preprocessing pipeline...")
    config_path = os.path.join(path_to_here, "config.json")
    assert os.path.exists(config_path), f"Configuration file not found: {config_path}"

    cfg_default = Config.from_json(config_path)
    logger.info(f"Loaded configuration: {cfg_default.__dict__}")

    for local_name in ["train", "test", "val"]:
        process_split(cfg_default, local_name)

    logger.info("Preprocessing pipeline completed successfully")


if __name__ == "__main__":
    main()
