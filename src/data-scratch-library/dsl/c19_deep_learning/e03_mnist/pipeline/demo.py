"""
Demo script showing the local MNIST pipeline in action.
Pure Python, no external dependencies.
"""

import os

from local_pipeline import run_complete_pipeline
from local_utils import load_model, load_local_file
from local_data_generator import load_local_data


def demo_single_prediction():
    """Demo making a single prediction with the trained model."""
    print("\n" + "="*50)
    print("SINGLE PREDICTION DEMO")
    print("="*50)
    
    # Load the trained model
    model_path = "data/mnist/models/mnist_model.json"
    if not os.path.exists(model_path):
        print("No trained model found. Run the pipeline first!")
        return
    
    model = load_model(model_path)
    
    # Load a test sample
    try:
        _, y_test = load_local_data("data/mnist/raw", "test")
        x_test_processed = load_local_file("data/mnist/processed/test/x_test_processed.json")
        
        # Make prediction on first test sample
        sample_input = x_test_processed[0]
        true_label = y_test[0]
        
        # Simple prediction (using our local utils function)
        from local_utils import predict_simple
        predicted_label = predict_simple(model, sample_input)
        
        print(f"True label: {true_label}")
        print(f"Predicted label: {predicted_label}")
        print(f"Correct: {'✅' if predicted_label == true_label else '❌'}")
        
    except Exception as e:
        print(f"Error during prediction demo: {e}")


def demo_data_inspection():
    """Demo inspecting the generated synthetic data."""
    print("\n" + "="*50)
    print("DATA INSPECTION DEMO")
    print("="*50)
    
    try:
        # Load some sample data
        x_train, y_train = load_local_data("data/mnist/raw", "train")
        
        print(f"Training samples: {len(x_train)}")
        print(f"Image dimensions: {len(x_train[0])}x{len(x_train[0][0])}")
        print(f"Sample labels: {y_train[:10]}")
        
        # Show pixel value distribution for first image
        first_image = x_train[0]
        flat_pixels = [pixel for row in first_image for pixel in row]
        non_zero_pixels = [p for p in flat_pixels if p > 0]
        
        print("First image stats:")
        print(f"  - Non-zero pixels: {len(non_zero_pixels)}")
        print(f"  - Min pixel value: {min(flat_pixels)}")
        print(f"  - Max pixel value: {max(flat_pixels)}")
        print(f"  - Average non-zero value: {sum(non_zero_pixels)/len(non_zero_pixels):.1f}")
        
    except Exception as e:
        print(f"Error during data inspection: {e}")


def main():
    """Run the complete demo."""
    print("LOCAL MNIST PIPELINE DEMO")
    print("Pure Python - No external dependencies")
    print("="*50)
    
    # Check if pipeline has been run
    if not os.path.exists("data/mnist/models/mnist_model.json"):
        print("Running pipeline first...")
        results = run_complete_pipeline()
        print(f"Pipeline completed with test accuracy: {results['test_accuracy']:.4f}")
    else:
        print("Using existing trained model...")
    
    # Run demos
    demo_data_inspection()
    demo_single_prediction()
    
    print("\n" + "="*50)
    print("DEMO COMPLETED")
    print("="*50)
    print("All files are stored locally in the 'data/mnist/' directory")
    print("No external dependencies or cloud services were used!")


if __name__ == "__main__":
    main()
