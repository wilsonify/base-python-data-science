from flask import Blueprint, request, jsonify
import sys
import os

# Add the data-scratch-library to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..', 'data-scratch-library'))

from dsl.c12_k_nearest_neighbors.nearest_neighbors import knn_classify

knn_bp = Blueprint('knn', __name__)

# Common response messages (reduce duplicated string literals)
ERR_NO_JSON = 'No JSON data provided'

@knn_bp.route('/classify', methods=['POST'])
def classify_point():
    """
    Classify a point using K-Nearest Neighbors algorithm.
    
    Request body:
    {
        "k": 3,
        "point": [1.0, 2.0],
        "training_data": [
            {"point": [1.1, 2.1], "label": "A"},
            {"point": [3.0, 4.0], "label": "B"}
        ]
    }
    """
    try:
        data = request.get_json(silent=True)
        
        # Validate required fields
        if not data:
            return jsonify({'error': ERR_NO_JSON}), 400
        
        if 'k' not in data or 'point' not in data or 'training_data' not in data:
            return jsonify({'error': 'Missing required fields: k, point, training_data'}), 400
        
        k = data['k']
        point = data['point']
        training_data = data['training_data']
        
        # Validate data types
        if not isinstance(k, int) or k <= 0:
            return jsonify({'error': 'k must be a positive integer'}), 400
        
        if not isinstance(point, list):
            return jsonify({'error': 'point must be a list of numbers'}), 400
        
        if not isinstance(training_data, list):
            return jsonify({'error': 'training_data must be a list'}), 400
        
        # Convert training data to the format expected by knn_classify
        labeled_points = []
        for item in training_data:
            if 'point' not in item or 'label' not in item:
                return jsonify({'error': 'Each training item must have point and label'}), 400
            
            if not isinstance(item['point'], list):
                return jsonify({'error': 'Training points must be lists of numbers'}), 400
            
            labeled_points.append((item['point'], item['label']))
        
        # Perform KNN classification
        prediction = knn_classify(k, labeled_points, point)
        
        return jsonify({
            'prediction': prediction,
            'k': k,
            'point': point,
            'training_points_count': len(labeled_points)
        })
        
    except Exception as e:
        return jsonify({'error': f'Classification failed: {str(e)}'}), 500


@knn_bp.route('/batch_classify', methods=['POST'])
def batch_classify():
    """
    Classify multiple points using K-Nearest Neighbors algorithm.
    
    Request body:
    {
        "k": 3,
        "points": [[1.0, 2.0], [3.0, 4.0]],
        "training_data": [
            {"point": [1.1, 2.1], "label": "A"},
            {"point": [3.0, 4.0], "label": "B"}
        ]
    }
    """
    try:
        data = request.get_json(silent=True)
        
        # Validate required fields
        if not data:
            return jsonify({'error': ERR_NO_JSON}), 400
        
        if 'k' not in data or 'points' not in data or 'training_data' not in data:
            return jsonify({'error': 'Missing required fields: k, points, training_data'}), 400
        
        k = data['k']
        points = data['points']
        training_data = data['training_data']
        
        # Validate data types
        if not isinstance(k, int) or k <= 0:
            return jsonify({'error': 'k must be a positive integer'}), 400
        
        if not isinstance(points, list):
            return jsonify({'error': 'points must be a list of point arrays'}), 400
        
        # Convert training data to the format expected by knn_classify
        labeled_points = []
        for item in training_data:
            if 'point' not in item or 'label' not in item:
                return jsonify({'error': 'Each training item must have point and label'}), 400
            
            labeled_points.append((item['point'], item['label']))
        
        # Perform batch classification
        predictions = []
        for point in points:
            prediction = knn_classify(k, labeled_points, point)
            predictions.append(prediction)
        
        return jsonify({
            'predictions': predictions,
            'k': k,
            'points_count': len(points),
            'training_points_count': len(labeled_points)
        })
        
    except Exception as e:
        return jsonify({'error': f'Batch classification failed: {str(e)}'}), 500


@knn_bp.route('/info', methods=['GET'])
def knn_info():
    """Get information about the KNN algorithm and parameters."""
    return jsonify({
        'algorithm': 'K-Nearest Neighbors',
        'description': 'Classifies a point based on the majority class of its k nearest neighbors',
        'parameters': {
            'k': {
                'type': 'integer',
                'description': 'Number of nearest neighbors to consider',
                'recommended': 'Odd numbers to avoid ties, typically 1, 3, or 5'
            },
            'point': {
                'type': 'array',
                'description': 'The point to classify',
                'example': '[1.0, 2.0, 3.0]'
            },
            'training_data': {
                'type': 'array',
                'description': 'Labeled training points',
                'example': '[{"point": [1.0, 2.0], "label": "A"}]'
            }
        },
        'notes': [
            'All points should have the same dimensionality',
            'Labels can be any hashable type (string, number, etc.)',
            'Higher k values can reduce noise but may blur decision boundaries'
        ]
    })
