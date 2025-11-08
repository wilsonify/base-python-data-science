"""
Local utility functions to replace external DSL dependencies.
Pure Python implementations for data processing and model operations.
"""

import json
import logging
import os
from typing import Any, Dict, List, Tuple
import random


class Config:
    """Local configuration class."""
    
    def __init__(self, config_dict: Dict[str, Any]):
        self.config = config_dict
        for key, value in config_dict.items():
            setattr(self, key.lower(), value)
    
    @classmethod
    def from_json(cls, config_path: str) -> 'Config':
        """Load config from JSON file."""
        with open(config_path, 'r') as f:
            config_dict = json.load(f)
        return cls(config_dict)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert config to dictionary."""
        return self.config
    
    def __getattr__(self, name: str) -> Any:
        """Get attribute with case-insensitive access."""
        return self.config.get(name.upper())


def save_local_file(data: Any, filepath: str) -> None:
    """Save data to local JSON file."""
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    
    if filepath.endswith('.json'):
        with open(filepath, 'w') as f:
            json.dump(data, f)
    else:
        raise ValueError(f"Unsupported file format: {filepath}")


def load_local_file(filepath: str) -> Any:
    """Load data from local JSON file."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    
    if filepath.endswith('.json'):
        with open(filepath, 'r') as f:
            return json.load(f)
    else:
        raise ValueError(f"Unsupported file format: {filepath}")


def normalize_image(image: List[List[int]], mean: float = 127.5, std: float = 127.5) -> List[List[float]]:
    """Normalize image values to [-1, 1] range."""
    normalized = []
    for row in image:
        normalized_row = [(pixel - mean) / std for pixel in row]
        normalized.append(normalized_row)
    return normalized


def flatten_images(images: List[List[List[int]]]) -> List[List[float]]:
    """Flatten 2D images to 1D vectors."""
    flattened = []
    for image in images:
        flat_image = [pixel for row in image for pixel in row]
        flattened.append(flat_image)
    return flattened


def one_hot_encode(labels: List[int], num_classes: int = 10) -> List[List[float]]:
    """Convert labels to one-hot encoding."""
    one_hot = []
    for label in labels:
        encoding = [0.0] * num_classes
        encoding[label] = 1.0
        one_hot.append(encoding)
    return one_hot


def split_train_validation(x_data: List, y_data: List, validation_split: float, seed: int = 42) -> Tuple[List, List, List, List]:
    """Split training data into train and validation sets."""
    random.seed(seed)
    
    num_val = int(validation_split * len(x_data))
    val_indices = random.sample(range(len(x_data)), num_val)
    
    x_val = [x_data[i] for i in val_indices]
    y_val = [y_data[i] for i in val_indices]
    
    x_train = [x_data[i] for i in range(len(x_data)) if i not in val_indices]
    y_train = [y_data[i] for i in range(len(y_data)) if i not in val_indices]
    
    return x_train, x_val, y_train, y_val


def calculate_accuracy(y_true: List[int], y_pred: List[int]) -> float:
    """Calculate classification accuracy."""
    if len(y_true) != len(y_pred):
        raise ValueError("True and predicted labels must have same length")
    
    correct = sum(1 for t, p in zip(y_true, y_pred) if t == p)
    return correct / len(y_true)


def simple_neural_forward(x: List[float], weights: List[List[float]], biases: List[float]) -> List[float]:
    """Simple forward pass through a neural network layer."""
    # Simple matrix multiplication
    output = []
    for i in range(len(weights)):
        weighted_sum = biases[i]
        for j in range(len(x)):
            weighted_sum += x[j] * weights[i][j]
        # Simple ReLU activation
        output.append(max(0, weighted_sum))
    return output


def create_simple_model(input_size: int = 784, hidden_size: int = 128, output_size: int = 10, seed: int = 42) -> Dict[str, Any]:
    """Create a simple neural network model."""
    random.seed(seed)
    
    # Initialize weights and biases randomly
    weights1 = [[random.uniform(-0.1, 0.1) for _ in range(input_size)] for _ in range(hidden_size)]
    biases1 = [0.0] * hidden_size
    
    weights2 = [[random.uniform(-0.1, 0.1) for _ in range(hidden_size)] for _ in range(output_size)]
    biases2 = [0.0] * output_size
    
    model = {
        'weights1': weights1,
        'biases1': biases1,
        'weights2': weights2,
        'biases2': biases2,
        'input_size': input_size,
        'hidden_size': hidden_size,
        'output_size': output_size
    }
    
    return model


def predict_simple(model: Dict[str, Any], x: List[float]) -> int:
    """Make prediction with simple neural network."""
    # Forward pass through first layer
    hidden = simple_neural_forward(x, model['weights1'], model['biases1'])
    
    # Forward pass through output layer
    output = simple_neural_forward(hidden, model['weights2'], model['biases2'])
    
    # Return argmax
    return output.index(max(output))


def train_simple_model(model: Dict[str, Any], x_train: List[List[float]], y_train: List[int], 
                      epochs: int = 5, learning_rate: float = 0.01) -> Dict[str, List[float]]:
    """Train the simple neural network."""
    history = {'loss': [], 'accuracy': []}
    
    for epoch in range(epochs):
        correct_predictions = 0
        total_loss = 0
        
        # Simple training loop (one sample at a time)
        for i, (x, y_true) in enumerate(zip(x_train, y_train)):
            # Forward pass
            hidden = simple_neural_forward(x, model['weights1'], model['biases1'])
            output = simple_neural_forward(hidden, model['weights2'], model['biases2'])
            
            # Calculate loss (simple MSE)
            y_one_hot = [0.0] * model['output_size']
            y_one_hot[y_true] = 1.0
            loss = sum((pred - true) ** 2 for pred, true in zip(output, y_one_hot))
            total_loss += loss
            
            # Simple prediction for accuracy
            y_pred = output.index(max(output))
            if y_pred == y_true:
                correct_predictions += 1
            
            # Very simple weight update (gradient approximation)
            if i % 100 == 0:  # Update every 100 samples for speed
                for j in range(len(model['weights2'])):
                    for k in range(len(model['weights2'][j])):
                        # Simple gradient approximation
                        gradient = (output[j] - y_one_hot[j]) * hidden[k] * learning_rate
                        model['weights2'][j][k] -= gradient
        
        # Calculate metrics
        accuracy = correct_predictions / len(x_train)
        avg_loss = total_loss / len(x_train)
        
        history['loss'].append(avg_loss)
        history['accuracy'].append(accuracy)
        
        logging.info(f"Epoch {epoch + 1}/{epochs} - Loss: {avg_loss:.4f}, Accuracy: {accuracy:.4f}")
    
    return history


def save_model(model: Dict[str, Any], filepath: str) -> None:
    """Save model to local file."""
    save_local_file(model, filepath)


def load_model(filepath: str) -> Dict[str, Any]:
    """Load model from local file."""
    return load_local_file(filepath)


def evaluate_model(model: Dict[str, Any], x_test: List[List[float]], y_test: List[int]) -> Dict[str, Any]:
    """Evaluate model on test data."""
    predictions = []
    
    for x in x_test:
        pred = predict_simple(model, x)
        predictions.append(pred)
    
    accuracy = calculate_accuracy(y_test, predictions)
    
    return {
        'accuracy': accuracy,
        'predictions': predictions,
        'true_labels': y_test
    }
