from flask import Blueprint, request, jsonify
import random
import logging

from dsl.c04_linear_algebra.e0401_vectors import distance, squared_distance
from dsl.c05_statistics.e0501_central_tendancy import mean

logger = logging.getLogger(__name__)

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


def _compute_cluster_error(cluster_points, mean):
    """Compute total squared error for a cluster given its points and mean."""
    return sum(squared_distance(point, mean) for point in cluster_points)


def _run_k_multiple_times(points, k, runs_per_k):
    """Run k-means multiple times and return (avg_error, min_error, max_error)."""
    k_errors = []
    for _ in range(runs_per_k):
        assignments, means = k_means(points, k)
        error = squared_clustering_errors(points, assignments, means)
        k_errors.append(error)

    if not k_errors:
        return float('inf'), 0, 0

    avg_error = sum(k_errors) / len(k_errors)
    return avg_error, min(k_errors), max(k_errors)

def k_means(data, k, initial_assignments=None, max_iterations=100):
    """K-means clustering algorithm."""
    if not data or k <= 0:
        return [], []

    # Initialize assignments and means
    assignments, means = _k_means_initialize(data, k, initial_assignments)

    # Run k-means iterations
    assignments, means = _k_means_iterate(data, k, assignments, means, max_iterations)

    return assignments, means


def _k_means_initialize(data, k, initial_assignments):
    """Initialize assignments and means for k-means."""
    n = len(data)
    if initial_assignments is None:
        assignments = [random.randrange(k) for _ in range(n)]
    else:
        assignments = initial_assignments.copy()

    means = cluster_means(data, assignments, k)
    return assignments, means


def _k_means_iterate(data, k, assignments, means, max_iterations):
    """Run the k-means main loop and return final assignments and means."""
    for _ in range(max_iterations):
        # Assign points to nearest mean
        new_assignments = [classify(point, means) for point in data]

        # Check for convergence
        if new_assignments == assignments:
            break

        # Update means and assignments
        means = cluster_means(data, new_assignments, k)
        assignments = new_assignments

    return assignments, means


def _build_clusters_dict(points, assignments):
    """Organize results by cluster into a dict: {cluster_id: [{index, point}, ...]}"""
    clusters = {}
    for i, (point, assignment) in enumerate(zip(points, assignments)):
        clusters.setdefault(assignment, []).append({"index": i, "point": point})
    return clusters


def _parse_analyze_payload(data):
    """Validate and parse payload for clustering analysis.

    Returns (points, assignments, means) or raises ValueError.
    """
    if not data:
        raise ValueError(ERR_NO_JSON)

    missing = [f for f in ('data', 'assignments', 'means') if f not in data]
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")

    points = data['data']
    assignments = data['assignments']
    means = data['means']

    if not isinstance(points, list):
        raise ValueError(ERR_DATA_MUST_BE_LIST)

    if not isinstance(assignments, list):
        raise ValueError('assignments must be a list')

    if not isinstance(means, list):
        raise ValueError('means must be a list')

    if len(points) != len(assignments):
        raise ValueError('data and assignments must have the same length')

    return points, assignments, means

clustering_bp = Blueprint('clustering', __name__)

# Common response messages
ERR_NO_JSON = 'No JSON data provided'
ERR_DATA_MUST_BE_LIST = 'data must be a list of points'
ERR_ALL_POINTS_LISTS = 'All points must be lists of numbers'
ERR_SAME_DIMENSION = 'All points must have the same dimensionality'
ERR_K_GT_POINTS = 'k cannot be greater than the number of data points'


# Request helpers
def _get_json_or_error():
    data = request.get_json(silent=True)
    if not data:
        return None, (jsonify({'error': ERR_NO_JSON}), 400)
    return data, None


def _ensure_list_field(data, name, error_message=None, required=True):
    if name not in data:
        if required:
            return None, (jsonify({'error': f'Missing required field: {name}'}), 400)
        return None, None

    value = data[name]
    if not isinstance(value, list):
        return None, (jsonify({'error': error_message or f'{name} must be a list'}), 400)
    return value, None


def _ensure_int_field(value, name, min_value=1):
    if not isinstance(value, int) or value < min_value:
        return None, (jsonify({'error': f'{name} must be an integer >= {min_value}'}), 400)
    return value, None


def _parse_kmeans_payload(data):
    """Validate and parse kmeans request payload; raise ValueError on problems."""
    if not data:
        raise ValueError(ERR_NO_JSON)

    if 'data' not in data or 'k' not in data:
        raise ValueError('Missing required fields: data, k')

    points = data['data']
    if not isinstance(points, list):
        raise ValueError(ERR_DATA_MUST_BE_LIST)

    k = data['k']
    if not isinstance(k, int) or k < 1:
        raise ValueError('k must be an integer >= 1')

    max_iterations = data.get('max_iterations', 100)
    if not isinstance(max_iterations, int) or max_iterations <= 0:
        raise ValueError('max_iterations must be a positive integer')

    initial_assignments = data.get('initial_assignments')
    if initial_assignments is not None and not isinstance(initial_assignments, list):
        raise ValueError('initial_assignments must be a list')

    return points, k, max_iterations, initial_assignments

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
    # Thin wrapper: parse request, delegate to core route logic and map exceptions to HTTP responses
    data = request.get_json(silent=True)
    try:
        result = _perform_kmeans_route(data)
        return jsonify(result)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.exception('K-means clustering failed')
        return jsonify({'error': 'K-means clustering failed due to an internal error'}), 500


def _perform_kmeans_route(data):
    """Route-level core for kmeans: validate payload and compute results.

    Raises ValueError for client errors.
    """
    if not data:
        raise ValueError(ERR_NO_JSON)

    points, k, max_iterations, initial_assignments = _parse_kmeans_payload(data)

    _validate_points_list(points)

    if k > len(points):
        raise ValueError(ERR_K_GT_POINTS)

    return _perform_kmeans_core(points, k, max_iterations, initial_assignments)


def _perform_kmeans_core(points, k, max_iterations, initial_assignments):
    """Core k-means computation extracted from the route handler.

    Returns a plain dictionary with results (suitable for jsonify).
    """
    assignments, means = k_means(points, k, initial_assignments, max_iterations)

    return _format_kmeans_result(points, k, max_iterations, assignments, means)


def _format_kmeans_result(points, k, max_iterations, assignments, means):
    """Format the k-means computation results into a serializable dict."""
    total_error = squared_clustering_errors(points, assignments, means)
    clusters = _build_clusters_dict(points, assignments)

    return {
        'clusters': clusters,
        'assignments': assignments,
        'means': means,
        'k': k,
        'total_squared_error': total_error,
        'iterations_used': max_iterations,
        'data_points': len(points)
    }


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
        data, err = _get_json_or_error()
        if err:
            return err

        try:
            points, assignments, means = _parse_analyze_payload(data)
        except ValueError as e:
            return jsonify({'error': str(e)}), 400

        result = _analyze_clustering_core(points, assignments, means)
        return jsonify(result)
        
    except Exception as e:
        logger.exception('Clustering analysis failed')
        return jsonify({'error': 'Clustering analysis failed due to an internal error'}), 500


def _analyze_clustering_core(points, assignments, means):
    """Core computation for clustering analysis.

    Returns a dict suitable for jsonify.
    """
    total_error = squared_clustering_errors(points, assignments, means)

    from collections import Counter
    cluster_sizes = dict(Counter(assignments))

    cluster_errors = {}
    cluster_errors = _compute_cluster_errors_dict(points, assignments, means, cluster_sizes)

    return {
        'total_squared_error': total_error,
        'average_squared_error': total_error / len(points) if points else 0,
        'cluster_sizes': cluster_sizes,
        'cluster_errors': cluster_errors,
        'num_clusters': len(means),
        'data_points': len(points)
    }


def _compute_cluster_errors_dict(points, assignments, means, cluster_sizes):
    """Return a dict of cluster_id -> {total_error, average_error, size}."""
    out = {}
    for cluster_id, size in cluster_sizes.items():
        if cluster_id < len(means):
            cluster_points = [p for p, a in zip(points, assignments) if a == cluster_id]
            if cluster_points:
                cluster_error = _compute_cluster_error(cluster_points, means[cluster_id])
                out[cluster_id] = {
                    'total_error': cluster_error,
                    'average_error': cluster_error / len(cluster_points),
                    'size': len(cluster_points)
                }
    return out


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
    data = request.get_json(silent=True)
    try:
        result = _find_optimal_k_route(data)
        return jsonify(result)
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.exception('Optimal k analysis failed')
        return jsonify({'error': 'Optimal k analysis failed due to an internal error'}), 500


def _find_optimal_k_route(data):
    """Route-level core for finding optimal k: validate payload and call core computation."""
    if not data:
        raise ValueError(ERR_NO_JSON)

    if 'data' not in data:
        raise ValueError('Missing required field: data')

    points = data['data']
    max_k = data.get('max_k', min(10, len(points)))
    runs_per_k = data.get('runs_per_k', 3)

    if not isinstance(points, list):
        raise ValueError(ERR_DATA_MUST_BE_LIST)

    if not isinstance(max_k, int) or max_k <= 1:
        raise ValueError('max_k must be an integer greater than 1')

    if not isinstance(runs_per_k, int) or runs_per_k <= 0:
        raise ValueError('runs_per_k must be a positive integer')

    if max_k > len(points):
        raise ValueError('max_k cannot be greater than the number of data points')

    return _find_optimal_k_core(points, max_k, runs_per_k)


def _find_optimal_k_core(points, max_k, runs_per_k):
    """Core elbow-method computation for finding optimal k."""
    results = []
    for k in range(1, max_k + 1):
        avg_error, min_err, max_err = _run_k_multiple_times(points, k, runs_per_k)
        results.append({
            'k': k,
            'average_squared_error': avg_error,
            'min_error': min_err,
            'max_error': max_err
        })

    elbow_k = 1
    max_decrease = 0
    for i in range(1, len(results)):
        decrease = results[i-1]['average_squared_error'] - results[i]['average_squared_error']
        if decrease > max_decrease:
            max_decrease = decrease
            elbow_k = results[i]['k']

    return {
        'results': results,
        'recommended_k': elbow_k,
        'max_k_tested': max_k,
        'runs_per_k': runs_per_k,
        'data_points': len(points)
    }


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
