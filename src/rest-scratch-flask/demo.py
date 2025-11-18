#!/usr/bin/env python3
"""
Demo script for Data Scratch Library REST API.
This script demonstrates the API functionality without requiring external dependencies.
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask app
from app import create_app, SWAGGER_AVAILABLE

def demo_api():
    """Demonstrate API functionality."""
    print("=== Data Scratch Library REST API Demo ===\n")
    
    # Create the Flask app
    app = create_app()
    
    print("Available Routes:")
    for rule in app.url_map.iter_rules():
        if rule.endpoint != 'static':
            print(f"  {rule.methods} {rule.rule}")
    
    print("\n=== API Information:")
    with app.test_client() as client:
        # Test health check
        response = client.get('/health')
        print(f"Health Check: {response.status_code} - {response.get_json()}")
        
        # Test OpenAPI spec
        response = client.get('/openapi.yaml')
        print(f"OpenAPI Spec: {response.status_code} - Available at /openapi.yaml")
        
        # Test API info
        response = client.get('/')
        api_info = response.get_json()
        print(f"API Info: {response.status_code}")
        print(f"  - CORS Enabled: {api_info.get('cors_enabled', False)}")
        print(f"  - Swagger UI Enabled: {api_info.get('swagger_ui_enabled', False)}")
        if api_info.get('swagger_ui_enabled'):
            print(f"  - Swagger UI: {api_info['endpoints']['swagger_ui']}")
        print(f"  - OpenAPI Spec: {api_info['endpoints']['openapi_spec']}")
        
        print("\nAvailable Routes:")
        for rule in app.url_map.iter_rules():
            if rule.endpoint != 'static':
                print(f"  {rule.methods} {rule.rule}")
        
        print("\n=== Testing ML Endpoints:")
        
        # Test KNN classification
        knn_data = {
            "k": 3,
            "point": [1.0, 2.0],
            "training_data": [
                {"point": [1.1, 2.1], "label": "A"},
                {"point": [3.0, 4.0], "label": "B"},
                {"point": [1.2, 2.2], "label": "A"}
            ]
        }
        
        response = client.post('/api/knn/classify', 
                             json=knn_data)
        print(f"KNN Classification: {response.status_code} - {response.get_json()}")
        
        # Test Naive Bayes classification
        nb_data = {
            "message": "buy viagra now cheap pills",
            "training_data": [
                {"message": "buy viagra now", "is_spam": True},
                {"message": "hello friend", "is_spam": False},
                {"message": "cheap pills online", "is_spam": True}
            ]
        }
        
        response = client.post('/api/naive-bayes/classify', 
                             json=nb_data)
        print(f"Naive Bayes Classification: {response.status_code} - {response.get_json()}")
        
        # Test Decision Tree classification
        dt_data = {
            "instance": {"level": "Senior", "lang": "Java"},
            "training_data": [
                {"features": {"level": "Senior", "lang": "Java"}, "label": True},
                {"features": {"level": "Junior", "lang": "Python"}, "label": False}
            ]
        }
        
        response = client.post('/api/decision-trees/classify', 
                             json=dt_data)
        print(f"Decision Tree Classification: {response.status_code} - {response.get_json()}")
        
        # Test Clustering
        cluster_data = {
            "data": [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0], [1.1, 2.1]],
            "k": 2
        }
        
        response = client.post('/api/clustering/kmeans', 
                             json=cluster_data)
        print(f"K-Means Clustering: {response.status_code} - Cluster assignments found")
        
        # Test Neural Networks
        nn_data = {"x": 1.0}
        
        response = client.post('/api/neural-networks/sigmoid', 
                             json=nn_data)
        print(f"Neural Network Sigmoid: {response.status_code} - {response.get_json()}")
    
    print("\n=== Demo Complete ===")
    print("To run the API server:")
    print("  python run.py")
    print("Then visit:")
    print("  - API Root: http://127.0.0.1:5000")
    print("  - OpenAPI Spec: http://127.0.0.1:5000/openapi.yaml")
    if SWAGGER_AVAILABLE:
        print("  - Swagger UI: http://127.0.0.1:5000/docs")
    print("\nOptional dependencies for full features:")
    print("  pip install Flask-CORS  # For cross-origin support")
    print("  pip install flask-swagger-ui  # For interactive API documentation")

if __name__ == '__main__':
    demo_api()
