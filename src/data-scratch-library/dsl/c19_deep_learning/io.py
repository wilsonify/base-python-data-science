"""
Model serialization: save / load neural-network weights as JSON.
"""

import json
from typing import List

from .deep_learning import Tensor, shape
from .layer import Layer


def save_weights(model: Layer, filename: str) -> None:
    """Save model parameters to a JSON file."""
    weights = list(model.params())
    with open(filename, "w") as f:
        json.dump(weights, f)


def load_weights(model: Layer, filename: str) -> None:
    """Load model parameters from a JSON file (in-place)."""
    with open(filename) as f:
        weights = json.load(f)
    for param, weight in zip(model.params(), weights):
        if shape(param) != shape(weight):
            raise ValueError(
                f"Shape mismatch: expected {shape(param)}, got {shape(weight)}"
            )
    for param, weight in zip(model.params(), weights):
        param[:] = weight
