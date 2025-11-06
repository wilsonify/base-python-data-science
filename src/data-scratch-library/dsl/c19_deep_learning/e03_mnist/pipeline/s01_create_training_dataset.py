"""
Step 1: Download original MNIST data and split into training/validation/evaluation sets.

Source:
https://storage.googleapis.com/dsl.c19_deep_learning/tf-keras-datasets/mnist.npz
"""

import logging
import os

import numpy as np
import dsl.c19_deep_learning as tf

from dsl.utils.io.labels_np_to_json import labels_np_to_json
from dsl.utils.io.upload_npz import upload_npz

# S3 bucket configuration
BUCKET = "064592191516-mlflow"
S3_PREFIX = "mnist/s01_create_training_dataset"


def save_npz(filepath, data):
    """Save numpy array to npz file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    np.savez_compressed(filepath, data=data)


def save_labels_json(filepath, labels):
    """Save labels to JSON file."""
    import json

    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(labels.tolist(), f)


def main():
    # Load configuration
    import json

    with open("config.json", encoding="utf-8") as f:
        cfg = json.load(f)

    logging.info("Loading MNIST data from Keras...")
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    logging.info(f"Initial train set: {x_train.shape}, test set: {x_test.shape}")

    # Create a random number generator with a fixed seed
    rng = np.random.default_rng(cfg["SEED"])

    # Create validation split using the Generator instance
    num_val = int(cfg["VALIDATION_SPLIT"] * len(x_train))
    val_idx = rng.choice(len(x_train), num_val, replace=False)
    x_val, y_val = x_train[val_idx], y_train[val_idx]
    x_train, y_train = np.delete(x_train, val_idx, axis=0), np.delete(
        y_train, val_idx, axis=0
    )

    logging.info(f"Split {num_val} samples for validation.")

    # Save datasets locally and to S3
    datasets = {
        "train": (x_train, y_train),
        "test": (x_test, y_test),
        "val": (x_val, y_val),
    }

    output_dir = "data/mnist/raw"
    for split, (x, y) in datasets.items():
        logging.info(f"Processing {split} dataset ({x.shape})...")

        # Save locally (as cache)
        local_x_path = f"{output_dir}/{split}/x_{split}.npz"
        local_y_path = f"{output_dir}/{split}/y_{split}.npz"
        local_y_json_path = f"{output_dir}/{split}/y_{split}.json"

        save_npz(local_x_path, x)
        save_npz(local_y_path, y)
        save_labels_json(local_y_json_path, y)

        # Upload to S3
        logging.info(f"Uploading {split} dataset to S3...")
        s3_x_path = f"{S3_PREFIX}/{split}/x_{split}.npz"
        s3_y_path = f"{S3_PREFIX}/{split}/y_{split}.npz"
        s3_y_json_path = f"{S3_PREFIX}/{split}/y_{split}.json"

        upload_npz(BUCKET, s3_x_path, x)
        upload_npz(BUCKET, s3_y_path, y)
        labels_np_to_json(BUCKET, s3_y_json_path, y)

    logging.info("Step 1 completed successfully.")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    main()
