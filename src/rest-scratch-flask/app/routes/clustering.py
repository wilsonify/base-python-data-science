from flask import Blueprint, request, jsonify
import sys
import os
import random

# Add the data-scratch-library to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), '../../..', 'data-scratch-library'))

from dsl.c04_linear_algebra.e0401_vectors import distance, squared_distance
from dsl.c05_statistics.e0501_central_tendancy import mean

# Helper functions for clustering
def vector_mean(vectors):
    """Calculate the mean of vectors."""
    if not vectors:
        return []
    
    num_components = len(vectors[0])
    return [sum(vector[i] for vector in vectors) / len(vectors) for i in range(num_components)]

def classify(point, means):
    """Classify a point to the nearest mean."""
    if not means:
        return 0
    
    distances = [squared_distance(point, mean) for mean in means]
    return distances.index(min(distances))


def _validate_points_list(points):
    """Validate that 'points' is a non-empty list of lists with consistent dimensionality."""
    if not isinstance(points, list):
        raise ValueError(ERR_DATA_MUST_BE_LIST)

    if not points:
        raise ValueError('data cannot be empty')

    for point in points:
        if not isinstance(point, list):
            raise ValueError(ERR_ALL_POINTS_LISTS)

        if len(point) != len(points[0]):
            raise ValueError(ERR_SAME_DIMENSION)



def cluster_means(data, assignments, k):
    """Calculate cluster means."""
    clusters = [[] for _ in range(k)]
    for point, assignment in zip(data, assignments):
        clusters[assignment].append(point)
    
    means = []
    for cluster in clusters:
        if cluster:
            means.append(vector_mean(cluster))
        else:
            # Empty cluster - use a random point or zero vector
            means.append([0] * len(data[0]) if data else [])
    
    return means

def squared_clustering_errors(data, assignments, means):
    """Calculate total squared error."""
    total_error = 0
    for point, assignment in zip(data, assignments):
        mean = means[assignment]
        total_error += squared_distance(point, mean)
    return total_error

def k_means(data, k, initial_assignments=None, max_iterations=100):
    """K-means clustering algorithm."""
    if not data or k <= 0:
        return [], []
    
    n = len(data)
    
    # Initialize assignments
    if initial_assignments is None:
        assignments = [random.randrange(k) for _ in range(n)]
    else:
        assignments = initial_assignments.copy()
    
    # Initialize means
    means = cluster_means(data, assignments, k)
    
    # Run k-means iterations
    for iteration in range(max_iterations):
        # Assign points to nearest mean
        new_assignments = [classify(point, means) for point in data]
        
        # Check for convergence
        if new_assignments == assignments:
            break
        
        # Update means
        means = cluster_means(data, new_assignments, k)
        assignments = new_assignments
    
    return assignments, means

clustering_bp = Blueprint('clustering', __name__)

# Common response messages
ERR_NO_JSON = 'No JSON data provided'
ERR_DATA_MUST_BE_LIST = 'data must be a list of points'
ERR_ALL_POINTS_LISTS = 'All points must be lists of numbers'
ERR_SAME_DIMENSION = 'All points must have the same dimensionality'
ERR_K_GT_POINTS = 'k cannot be greater than the number of data points'

@clustering_bp.route('/kmeans', methods=['POST'])
def perform_kmeans():
    """
    Perform K-means clustering on data points.
    
    Request body:
    {
        "data": [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],
        "k": 2,
        "max_iterations": 100,
        "initial_assignments": [0, 1, 0]
    }
    """
    try:
        data = request.get_json(silent=True)
        
        # Validate required fields
        if not data:
            return jsonify({'error': ERR_NO_JSON}), 400
        
        if 'data' not in data or 'k' not in data:
            return jsonify({'error': 'Missing required fields: data, k'}), 400
        
        points = data['data']
        k = data['k']
        max_iterations = data.get('max_iterations', 100)
        initial_assignments = data.get('initial_assignments')
        
        # Validate data types
        if not isinstance(points, list):
            return jsonify({'error': ERR_DATA_MUST_BE_LIST}), 400
        
        if not isinstance(k, int) or k <= 0:
            return jsonify({'error': 'k must be a positive integer'}), 400
        
        if not isinstance(max_iterations, int) or max_iterations <= 0:
            return jsonify({'error': 'max_iterations must be a positive integer'}), 400
        
        if initial_assignments is not None and not isinstance(initial_assignments, list):
            return jsonify({'error': 'initial_assignments must be a list'}), 400
        
        # Validate types and content
        try:
            _validate_points_list(points)
        except ValueError as e:
            return jsonify({'error': str(e)}), 400

        if not isinstance(k, int) or k <= 0:
            return jsonify({'error': 'k must be a positive integer'}), 400

        if not isinstance(max_iterations, int) or max_iterations <= 0:
            return jsonify({'error': 'max_iterations must be a positive integer'}), 400

        if initial_assignments is not None and not isinstance(initial_assignments, list):
            return jsonify({'error': 'initial_assignments must be a list'}), 400

        if k > len(points):
            return jsonify({'error': ERR_K_GT_POINTS}), 400

        # Perform K-means clustering
        assignments, means = k_means(points, k, initial_assignments, max_iterations)

        # Calculate error metrics
        total_error = squared_clustering_errors(points, assignments, means)

        # Organize results by cluster
        clusters = {}
        for i, (point, assignment) in enumerate(zip(points, assignments)):
            if assignment not in clusters:
                clusters[assignment] = []
            clusters[assignment].append({
                'index': i,
                'point': point
            })
        
        return jsonify({
            'clusters': clusters,
            'assignments': assignments,
            'means': means,
            'k': k,
            'total_squared_error': total_error,
            'iterations_used': max_iterations,  # This would be actual iterations in a more complete implementation
            'data_points': len(points)
        })
        
    except Exception as e:
        return jsonify({'error': f'K-means clustering failed: {str(e)}'}), 500


@clustering_bp.route('/analyze', methods=['POST'])
def analyze_clustering():
    """
    Analyze clustering quality and provide metrics.
    
    Request body:
    {
        "data": [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],
        "assignments": [0, 1, 0],
        "means": [[1.5, 2.5], [4.0, 5.0]]
    }
    """
    try:
        data = request.get_json(silent=True)
        
        # Validate required fields
        if not data:
            return jsonify({'error': ERR_NO_JSON}), 400
        
        if 'data' not in data or 'assignments' not in data or 'means' not in data:
            return jsonify({'error': 'Missing required fields: data, assignments, means'}), 400
        
        points = data['data']
        assignments = data['assignments']
        means = data['means']
        
        # Validate data types
        if not isinstance(points, list):
            return jsonify({'error': ERR_DATA_MUST_BE_LIST}), 400
        
        if not isinstance(assignments, list):
            return jsonify({'error': 'assignments must be a list'}), 400
        
        if not isinstance(means, list):
            return jsonify({'error': 'means must be a list'}), 400
        
        # Validate lengths
        if len(points) != len(assignments):
            return jsonify({'error': 'data and assignments must have the same length'}), 400
        
        # Calculate metrics
        total_error = squared_clustering_errors(points, assignments, means)
        
        # Calculate cluster sizes
        cluster_sizes = {}
        for assignment in assignments:
            cluster_sizes[assignment] = cluster_sizes.get(assignment, 0) + 1
        
        # Calculate average distance to cluster center for each cluster
        cluster_errors = {}
        for cluster_id in cluster_sizes:
            cluster_points = []
            for point, assignment in zip(points, assignments):
                if assignment == cluster_id:
                    cluster_points.append(point)
            
            if cluster_points and cluster_id < len(means):
                cluster_error = sum(squared_distance(point, means[cluster_id]) for point in cluster_points)
                cluster_errors[cluster_id] = {
                    'total_error': cluster_error,
                    'average_error': cluster_error / len(cluster_points),
                    'size': len(cluster_points)
                }
        
        return jsonify({
            'total_squared_error': total_error,
            'average_squared_error': total_error / len(points),
            'cluster_sizes': cluster_sizes,
            'cluster_errors': cluster_errors,
            'num_clusters': len(means),
            'data_points': len(points)
        })
        
    except Exception as e:
        return jsonify({'error': f'Clustering analysis failed: {str(e)}'}), 500


@clustering_bp.route('/optimal_k', methods=['POST'])
def find_optimal_k():
    """
    Find optimal number of clusters using elbow method.
    
    Request body:
    {
        "data": [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],
        "max_k": 5,
        "runs_per_k": 3
    }
    """
    try:
        data = request.get_json(silent=True)
        
        # Validate required fields
        if not data:
            return jsonify({'error': ERR_NO_JSON}), 400
        
        if 'data' not in data:
            return jsonify({'error': 'Missing required field: data'}), 400
        
        points = data['data']
        max_k = data.get('max_k', min(10, len(points)))
        runs_per_k = data.get('runs_per_k', 3)
        
        # Validate data types
        if not isinstance(points, list):
            return jsonify({'error': ERR_DATA_MUST_BE_LIST}), 400
        
        if not isinstance(max_k, int) or max_k <= 1:
            return jsonify({'error': 'max_k must be an integer greater than 1'}), 400
        
        if not isinstance(runs_per_k, int) or runs_per_k <= 0:
            return jsonify({'error': 'runs_per_k must be a positive integer'}), 400
        
        if max_k > len(points):
            return jsonify({'error': 'max_k cannot be greater than the number of data points'}), 400
        
        # Test different values of k
        results = []
        for k in range(1, max_k + 1):
            k_errors = []
            
            for _ in range(runs_per_k):
                assignments, means = k_means(points, k)
                error = squared_clustering_errors(points, assignments, means)
                k_errors.append(error)
            
            avg_error = sum(k_errors) / len(k_errors)
            results.append({
                'k': k,
                'average_squared_error': avg_error,
                'min_error': min(k_errors),
                'max_error': max(k_errors)
            })
        
        # Simple elbow detection (find point with maximum decrease)
        elbow_k = 1
        max_decrease = 0
        for i in range(1, len(results)):
            decrease = results[i-1]['average_squared_error'] - results[i]['average_squared_error']
            if decrease > max_decrease:
                max_decrease = decrease
                elbow_k = results[i]['k']
        
        return jsonify({
            'results': results,
            'recommended_k': elbow_k,
            'max_k_tested': max_k,
            'runs_per_k': runs_per_k,
            'data_points': len(points)
        })
        
    except Exception as e:
        return jsonify({'error': f'Optimal k analysis failed: {str(e)}'}), 500


@clustering_bp.route('/info', methods=['GET'])
def clustering_info():
    """Get information about clustering algorithms and parameters."""
    return jsonify({
        'algorithms': ['K-means'],
        'description': 'Partition data into k clusters based on feature similarity',
        'parameters': {
            'data': {
                'type': 'array',
                'description': 'List of data points to cluster',
                'example': '[[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]]'
            },
            'k': {
                'type': 'integer',
                'description': 'Number of clusters to create',
                'recommended': 'Use elbow method or domain knowledge'
            },
            'max_iterations': {
                'type': 'integer',
                'description': 'Maximum number of iterations for convergence',
                'default': 100
            },
            'initial_assignments': {
                'type': 'array',
                'description': 'Optional initial cluster assignments',
                'example': '[0, 1, 0]'
            }
        },
        'output': {
            'clusters': 'object with cluster assignments',
            'means': 'array of cluster centroids',
            'total_squared_error': 'float measuring clustering quality'
        },
        'endpoints': {
            'kmeans': 'POST /api/clustering/kmeans - Perform K-means clustering',
            'analyze': 'POST /api/clustering/analyze - Analyze clustering quality',
            'optimal_k': 'POST /api/clustering/optimal_k - Find optimal number of clusters'
        },
        'notes': [
            'All points must have the same dimensionality',
            'K-means converges to local optima - multiple runs may give different results',
            'Lower squared error generally indicates better clustering',
            'Elbow method helps determine optimal k value'
        ]
    })
