"""
Model serialization utilities for saving and loading neural network weights.

These models take a long time to train, so it would be nice if we could save them so
that we don't have to train them every time. Luckily, we can use the json module to
easily serialize model weights to a file.
For saving, we can use Layer.params to collect the weights, stick them in a list, and
use json.dump to save that list to a file.
"""

import json
from typing import List, Union
from .layer import Layer
from .deep_learning import Tensor, shape

def save_weights(model: Layer, filename: str) -> None:
    """
    Save model weights to a JSON file.
    
    Args:
        model: The neural network layer to save
        filename: Path to the JSON file to save weights to
    """
    weights = list(model.params())
    with open(filename, 'w') as f:
        json.dump(weights, f)

def load_weights(model: Layer, filename: str) -> None:
    """
    Load model weights from a JSON file.
    
    Args:
        model: The neural network layer to load weights into
        filename: Path to the JSON file to load weights from
    
    Raises:
        ValueError: If the shapes of loaded weights don't match model parameters
    """
    with open(filename) as f:
        weights = json.load(f)
    # Check for consistency
    for param, weight in zip(model.params(), weights):
        if shape(param) != shape(weight):
            raise ValueError(f"Shape mismatch: expected {shape(param)}, got {shape(weight)}")
    # Then load using slice assignment
    for param, weight in zip(model.params(), weights):
        param[:] = weight