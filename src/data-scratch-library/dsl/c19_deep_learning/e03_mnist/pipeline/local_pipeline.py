"""
Complete local MNIST pipeline - pure Python, no external dependencies.
Replaces all S3, external DSL, and cloud dependencies with local file operations.
"""

import logging
import os
import sys
from pathlib import Path
from typing import Dict, Any, List, Tuple

# Import our local utilities
from local_data_generator import generate_synthetic_mnist, save_local_data, load_local_data
from local_utils import (
    Config, save_local_file, load_local_file, normalize_image, flatten_images,
    one_hot_encode, split_train_validation, create_simple_model, train_simple_model,
    evaluate_model, save_model, load_model
)


def setup_logging(log_dir: str = "logs") -> logging.Logger:
    """Set up logging configuration."""
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "local_pipeline.log")
    
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(log_file),
        ],
    )
    
    logger = logging.getLogger(__name__)
    logger.info(f"Logging setup complete. Log file: {log_file}")
    return logger


def step1_create_dataset(config: Config, logger: logging.Logger) -> Dict[str, str]:
    """Step 1: Generate synthetic MNIST dataset."""
    logger.info("Step 1: Creating synthetic MNIST dataset...")
    
    # Generate synthetic data
    data = generate_synthetic_mnist(
        num_train=1000,  # Smaller for local testing
        num_test=200,
        seed=config.seed
    )
    
    # Save to local directory
    output_dir = "data/mnist/raw"
    save_local_data(data, output_dir)
    
    # Split training data into train/validation
    x_train, x_val, y_train, y_val = split_train_validation(
        data['x_train'], data['y_train'], 
        validation_split=config.validation_split, 
        seed=config.seed
    )
    
    # Save validation split
    save_local_file(x_val, f"{output_dir}/val/x_val.json")
    save_local_file(y_val, f"{output_dir}/val/y_val.json")
    
    # Update training data without validation samples
    save_local_file(x_train, f"{output_dir}/train/x_train.json")
    save_local_file(y_train, f"{output_dir}/train/y_train.json")
    
    # Save test data
    save_local_file(data['x_test'], f"{output_dir}/test/x_test.json")
    save_local_file(data['y_test'], f"{output_dir}/test/y_test.json")
    
    logger.info("Step 1 completed successfully")
    return {"data_dir": output_dir}


def step2_preprocess_data(config: Config, data_dir: str, logger: logging.Logger) -> Dict[str, str]:
    """Step 2: Preprocess the data."""
    logger.info("Step 2: Preprocessing data...")
    
    # Create processed data directory
    processed_dir = "data/mnist/processed"
    os.makedirs(processed_dir, exist_ok=True)
    
    for split in ['train', 'val', 'test']:
        logger.info(f"Processing {split} split...")
        
        # Load raw data
        x_data, y_data = load_local_data(data_dir, split)
        
        # Normalize images
        x_normalized = [normalize_image(img, config.normalize_mean, config.normalize_std) for img in x_data]
        
        # Flatten images
        x_flattened = flatten_images(x_normalized)
        
        # One-hot encode labels
        y_one_hot = one_hot_encode(y_data, config.num_classes)
        
        # Save processed data
        x_path = f"{processed_dir}/{split}/x_{split}_processed.json"
        y_path = f"{processed_dir}/{split}/y_{split}_processed.json"
        
        save_local_file(x_flattened, x_path)
        save_local_file(y_one_hot, y_path)
        
        logger.info(f"Processed {split}: {len(x_flattened)} samples")
    
    logger.info("Step 2 completed successfully")
    return {"processed_dir": processed_dir}


def step3_train_model(config: Config, processed_dir: str, logger: logging.Logger) -> Dict[str, str]:
    """Step 3: Train the model."""
    logger.info("Step 3: Training model...")
    
    # Load training data
    x_train_path = f"{processed_dir}/train/x_train_processed.json"
    y_train_path = f"{processed_dir}/train/y_train_processed.json"
    
    x_train = load_local_file(x_train_path)
    y_train_one_hot = load_local_file(y_train_path)
    
    # Convert one-hot back to labels for training
    y_train = [labels.index(max(labels)) for labels in y_train_one_hot]
    
    # Create model
    model = create_simple_model(
        input_size=784,  # 28x28 flattened
        hidden_size=64,   # Smaller for faster training
        output_size=config.num_classes,
        seed=config.seed
    )
    
    # Train model
    logger.info("Starting training...")
    history = train_simple_model(
        model, x_train, y_train,
        epochs=config.epochs,
        learning_rate=0.01
    )
    
    # Save model and training history
    models_dir = "data/mnist/models"
    os.makedirs(models_dir, exist_ok=True)
    
    model_path = f"{models_dir}/mnist_model.json"
    save_model(model, model_path)
    
    history_path = f"{models_dir}/training_history.json"
    save_local_file(history, history_path)
    
    logger.info("Step 3 completed successfully")
    return {"model_path": model_path, "history_path": history_path}


def step4_evaluate_model(processed_dir: str, model_path: str, logger: logging.Logger) -> Dict[str, Any]:
    """Step 4: Evaluate the model."""
    logger.info("Step 4: Evaluating model...")
    
    # Load test data
    x_test_path = f"{processed_dir}/test/x_test_processed.json"
    y_test_path = f"{processed_dir}/test/y_test_processed.json"
    
    x_test = load_local_file(x_test_path)
    y_test_one_hot = load_local_file(y_test_path)
    
    # Convert one-hot back to labels
    y_test = [labels.index(max(labels)) for labels in y_test_one_hot]
    
    # Load model
    model = load_model(model_path)
    
    # Evaluate
    results = evaluate_model(model, x_test, y_test)
    
    # Save results
    results_dir = "data/mnist/results"
    os.makedirs(results_dir, exist_ok=True)
    
    results_path = f"{results_dir}/evaluation_results.json"
    save_local_file(results, results_path)
    
    logger.info(f"Test Accuracy: {results['accuracy']:.4f}")
    logger.info("Step 4 completed successfully")
    
    return results


def run_complete_pipeline(config_path: str = "config.json") -> Dict[str, Any]:
    """Run the complete local pipeline."""
    logger = setup_logging()
    logger.info("Starting complete local MNIST pipeline...")
    
    try:
        # Load configuration
        config = Config.from_json(config_path)
        logger.info(f"Loaded configuration: {config.to_dict()}")
        
        # Step 1: Create dataset
        step1_result = step1_create_dataset(config, logger)
        
        # Step 2: Preprocess data
        step2_result = step2_preprocess_data(config, step1_result['data_dir'], logger)

        # Step 3: Train model
        step3_result = step3_train_model(config, step2_result['processed_dir'], logger)

        # Step 4: Evaluate model
        step4_result = step4_evaluate_model(step2_result['processed_dir'],
                                            step3_result['model_path'], logger)

        # Final results
        final_results = {
            'pipeline_status': 'completed',
            'test_accuracy': step4_result['accuracy'],
            'model_path': step3_result['model_path'],
            'results_path': "data/mnist/results/evaluation_results.json"
        }
        
        logger.info("Pipeline completed successfully!")
        logger.info(f"Final test accuracy: {final_results['test_accuracy']:.4f}")
        
        return final_results
        
    except Exception as e:
        logger.error(f"Pipeline failed with error: {e}")
        raise


def main():
    """Main function to run the pipeline."""
    # Change to pipeline directory
    pipeline_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(pipeline_dir)
    
    # Run pipeline
    results = run_complete_pipeline()
    
    print("\n" + "="*50)
    print("PIPELINE RESULTS")
    print("="*50)
    print(f"Status: {results['pipeline_status']}")
    print(f"Test Accuracy: {results['test_accuracy']:.4f}")
    print(f"Model saved to: {results['model_path']}")
    print(f"Results saved to: {results['results_path']}")
    print("="*50)


if __name__ == "__main__":
    main()
