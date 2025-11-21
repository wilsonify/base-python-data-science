#!/usr/bin/env python3
"""
Flask application runner for Data Scratch Library REST API.
"""

import os
from app import create_app

# Create and configure the Flask app
app = create_app()

if __name__ == '__main__':
    # Get configuration from environment variables
    host = os.environ.get('FLASK_HOST', '127.0.0.1')
    port = int(os.environ.get('FLASK_PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    print("Starting Data Scratch Library REST API...")
    print(f"Server: http://{host}:{port}")
    print(f"Debug mode: {debug}")
    print("API endpoints available at:")
    print(f"  - KNN: http://{host}:{port}/api/knn")
    print(f"  - Naive Bayes: http://{host}:{port}/api/naive-bayes")
    print(f"  - Decision Trees: http://{host}:{port}/api/decision-trees")
    print(f"  - Clustering: http://{host}:{port}/api/clustering")
    print(f"  - Neural Networks: http://{host}:{port}/api/neural-networks")
    print(f"  - Health check: http://{host}:{port}/health")
    
    app.run(host=host, port=port, debug=debug)
