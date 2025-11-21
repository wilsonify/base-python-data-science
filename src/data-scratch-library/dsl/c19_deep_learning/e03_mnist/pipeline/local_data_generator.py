"""
Local data generator for MNIST-like dataset.
Creates synthetic digit images without external dependencies.
"""

import json
import logging
import os
from typing import Tuple, Dict, Any
import random


def _rand_bright() -> int:
    """Return a bright pixel value for synthetic digit strokes."""
    return random.randint(180, 255)


def create_digit_image(digit: int, size: Tuple[int, int]) -> list:
    """Create a simple synthetic digit image."""
    height, width = size
    image = [[0 for _ in range(width)] for _ in range(height)]
    center_h, center_w = height // 2, width // 2

    # Dispatch to per-digit drawing helpers to keep this function simple
    digit_drawers = {
        0: _draw_digit_0,
        1: _draw_digit_1,
        2: _draw_digit_2,
        3: _draw_digit_3,
        4: _draw_digit_4,
        5: _draw_digit_5,
        6: _draw_digit_6,
        7: _draw_digit_7,
        8: _draw_digit_8,
        9: _draw_digit_9,
    }

    drawer = digit_drawers.get(digit)
    if drawer:
        drawer(image, height, width, center_h, center_w)

    _add_noise(image, height, width)
    return image


def _add_noise(image: list, height: int, width: int) -> None:
    """Apply small random noise to an image in-place."""
    for i in range(height):
        for j in range(width):
            if image[i][j] > 0:
                image[i][j] = max(0, image[i][j] + random.randint(-30, 30))
            else:
                if random.random() < 0.05:  # 5% noise
                    image[i][j] = random.randint(0, 50)


def _draw_digit_0(image: list, height: int, width: int, center_h: int, center_w: int) -> None:
    for i in range(height):
        for j in range(width):
            if 6 <= i <= 21 and 6 <= j <= 21:
                dist = ((i - center_h) ** 2 + (j - center_w) ** 2) ** 0.5
                if 6 <= dist <= 8:
                    image[i][j] = _rand_bright()


def _draw_digit_1(image: list, height: int, width: int, center_h: int, center_w: int) -> None:
    for i in range(5, 23):
        for j in range(center_w - 2, center_w + 3):
            if 0 <= i < height and 0 <= j < width:
                image[i][j] = _rand_bright()


def _draw_digit_2(image: list, height: int, width: int, center_h: int, center_w: int) -> None:
    for j in range(6, 22):
        image[6][j] = _rand_bright()
        image[21][j] = _rand_bright()
    for i in range(6, 14):
        image[i][21] = _rand_bright()
    for i in range(14, 22):
        image[i][6] = _rand_bright()


def _draw_digit_3(image: list, height: int, width: int, center_h: int, center_w: int) -> None:
    for j in range(6, 22):
        image[6][j] = _rand_bright()
        image[14][j] = _rand_bright()
        image[21][j] = _rand_bright()
    for i in range(6, 22):
        image[i][21] = _rand_bright()


def _draw_digit_4(image: list, height: int, width: int, center_h: int, center_w: int) -> None:
    for i in range(6, 14):
        for j in range(6, 22):
            if j == center_w or j == 21:
                image[i][j] = _rand_bright()
    for j in range(6, 22):
        image[14][j] = _rand_bright()


def _draw_digit_5(image: list, height: int, width: int, center_h: int, center_w: int) -> None:
    for j in range(6, 22):
        image[6][j] = _rand_bright()
        image[14][j] = _rand_bright()
        image[21][j] = _rand_bright()
    for i in range(6, 14):
        image[i][6] = _rand_bright()
    for i in range(14, 22):
        image[i][21] = _rand_bright()


def _draw_digit_6(image: list, height: int, width: int, center_h: int, center_w: int) -> None:
    for j in range(6, 22):
        image[14][j] = _rand_bright()
        image[21][j] = _rand_bright()
    for i in range(6, 22):
        image[i][6] = _rand_bright()
    for i in range(14, 22):
        image[i][21] = _rand_bright()


def _draw_digit_7(image: list, height: int, width: int, center_h: int, center_w: int) -> None:
    for j in range(6, 22):
        image[6][j] = _rand_bright()
    for i in range(6, 22):
        col = i - 6 + 6
        if col < width:
            image[i][col] = _rand_bright()


def _draw_digit_8(image: list, height: int, width: int, center_h: int, center_w: int) -> None:
    for i in range(6, 14):
        for j in range(6, 22):
            dist1 = ((i - 10) ** 2 + ((j - center_w) ** 2)) ** 0.5
            dist2 = ((i - 18) ** 2 + ((j - center_w) ** 2)) ** 0.5
            if 3 <= dist1 <= 5 or 3 <= dist2 <= 5:
                image[i][j] = _rand_bright()
    for j in range(6, 22):
        image[14][j] = _rand_bright()


def _draw_digit_9(image: list, height: int, width: int, center_h: int, center_w: int) -> None:
    for j in range(6, 22):
        image[6][j] = _rand_bright()
        image[14][j] = _rand_bright()
    for i in range(6, 22):
        image[i][21] = _rand_bright()
    for i in range(6, 14):
        image[i][6] = _rand_bright()

def generate_synthetic_mnist(num_train: int = 60000, num_test: int = 10000, 
                           img_size: Tuple[int, int] = (28, 28), 
                           num_classes: int = 10, seed: int = 42) -> Dict[str, Any]:
    """
    Generate synthetic MNIST-like dataset.
    
    Args:
        num_train: Number of training samples
        num_test: Number of test samples  
        img_size: Image dimensions (height, width)
        num_classes: Number of digit classes (0-9)
        seed: Random seed for reproducibility
        
    Returns:
        Dictionary containing train and test data/labels
    """
    random.seed(seed)

    def _generate_split(n: int):
        x = []
        y = []
        for _ in range(n):
            digit = random.randint(0, num_classes - 1)
            image = create_digit_image(digit, img_size)
            x.append(image)
            y.append(digit)
        return x, y

    x_train, y_train = _generate_split(num_train)
    x_test, y_test = _generate_split(num_test)
    
    return {
        'x_train': x_train,
        'y_train': y_train,
        'x_test': x_test,
        'y_test': y_test
    }


def save_local_data(data: Dict[str, Any], output_dir: str) -> None:
    """Save generated data to local JSON files."""
    os.makedirs(output_dir, exist_ok=True)
    
    for split in ['train', 'test']:
        x_key = f'x_{split}'
        y_key = f'y_{split}'
        
        if x_key in data and y_key in data:
            # Save images as JSON
            x_path = os.path.join(output_dir, split, f'x_{split}.json')
            os.makedirs(os.path.dirname(x_path), exist_ok=True)
            with open(x_path, 'w') as f:
                json.dump(data[x_key], f)
            
            # Save labels as JSON
            y_path = os.path.join(output_dir, split, f'y_{split}.json')
            with open(y_path, 'w') as f:
                json.dump(data[y_key], f)
            
            logging.info(f"Saved {split} data: {len(data[x_key])} samples")


def load_local_data(data_dir: str, split: str) -> Tuple[list, list]:
    """Load data from local JSON files."""
    x_path = os.path.join(data_dir, split, f'x_{split}.json')
    y_path = os.path.join(data_dir, split, f'y_{split}.json')
    
    if not os.path.exists(x_path) or not os.path.exists(y_path):
        raise FileNotFoundError(f"Data files not found for split: {split}")
    
    with open(x_path, 'r') as f:
        x_data = json.load(f)
    
    with open(y_path, 'r') as f:
        y_data = json.load(f)
    
    return x_data, y_data


def main():
    """Generate and save synthetic MNIST data."""
    logging.basicConfig(level=logging.INFO)
    
    # Generate synthetic data
    logging.info("Generating synthetic MNIST data...")
    data = generate_synthetic_mnist(num_train=1000, num_test=200, seed=42)  # Smaller for testing
    
    # Save locally
    output_dir = "data/mnist/raw"
    save_local_data(data, output_dir)
    
    logging.info("Data generation completed successfully!")


if __name__ == "__main__":
    main()
