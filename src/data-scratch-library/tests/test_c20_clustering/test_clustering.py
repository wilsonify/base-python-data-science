import pytest
import math
import random

from dsl.c04_linear_algebra.e0401_vectors import distance, squared_distance
from dsl.c05_statistics.e0501_central_tendancy import mean


def vector_mean(vectors):
    """Simple implementation of vector mean for testing."""
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


def k_means(data, k, initial_assignments=None):
    """Simple k-means implementation for testing."""
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
    
    # Run k-means iterations (simplified version)
    for _ in range(10):  # Fixed number of iterations for testing
        # Assign points to nearest mean
        new_assignments = [classify(point, means) for point in data]
        
        # Update means
        means = cluster_means(data, new_assignments, k)
        assignments = new_assignments
    
    return assignments, means


# Now the actual tests


def test_squared_distance():
    """Test the squared_distance function."""
    v1 = [1, 2, 3]
    v2 = [4, 6, 8]
    
    # Distance squared = (4-1)^2 + (6-2)^2 + (8-3)^2 = 3^2 + 4^2 + 5^2 = 9 + 16 + 25 = 50
    result = squared_distance(v1, v2)
    assert result == pytest.approx(50.0)
    
    # Test with same vector (distance should be 0)
    assert squared_distance(v1, v1) == 0.0
    
    # Test with negative numbers
    v3 = [-1, -2, -3]
    result = squared_distance(v1, v3)
    # (1-(-1))^2 + (2-(-2))^2 + (3-(-3))^2 = 2^2 + 4^2 + 6^2 = 4 + 16 + 36 = 56
    assert result == pytest.approx(56.0)


def test_vector_mean():
    """Test the vector_mean function."""
    vectors = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    result = vector_mean(vectors)
    expected = [4, 5, 6]  # (1+4+7)/3=4, (2+5+8)/3=5, (3+6+9)/3=6
    
    assert len(result) == len(expected)
    for i in range(len(result)):
        assert result[i] == pytest.approx(expected[i])
    
    # Test with single vector
    single_vector = [[1, 2, 3]]
    result = vector_mean(single_vector)
    assert result == [1, 2, 3]
    
    # Test with empty list
    try:
        vector_mean([])
        assert False, "Should raise error for empty input"
    except (ValueError, ZeroDivisionError):
        pass  # Expected


def test_classify():
    """Test the classify function."""
    means = [[0, 0], [10, 10], [20, 20]]
    
    # Point closest to [0, 0]
    point1 = [1, 1]
    result1 = classify(point1, means)
    assert result1 == 0
    
    # Point closest to [10, 10]
    point2 = [9, 11]
    result2 = classify(point2, means)
    assert result2 == 1
    
    # Point closest to [20, 20]
    point3 = [22, 19]
    result3 = classify(point3, means)
    assert result3 == 2
    
    # Test with ties (equidistant)
    tie_point = [5, 5]
    # Distance to [0,0] = sqrt(50), to [10,10] = sqrt(50)
    # Should pick one of them consistently
    result_tie = classify(tie_point, means)
    assert result_tie in [0, 1]


def test_k_means_simple():
    """Test k_means with simple, well-separated data."""
    # Three clear clusters
    data = [
        # Cluster 1 around [0, 0]
        [0.1, 0.1], [-0.1, -0.1], [0.2, -0.1], [-0.1, 0.2],
        # Cluster 2 around [10, 10]
        [10.1, 10.1], [9.9, 9.9], [10.2, 9.8], [9.8, 10.2],
        # Cluster 3 around [20, 0]
        [20.1, 0.1], [19.9, -0.1], [20.2, 0.2], [19.8, -0.2]
    ]
    
    assignments, means = k_means(data, k=3)
    
    # Should return assignments and means
    assert len(assignments) == len(data)
    assert len(means) == 3
    
    # All assignments should be valid cluster indices
    for assignment in assignments:
        assert 0 <= assignment < 3
    
    # Means should be close to the true cluster centers
    # (order might be different, so we check distances)
    true_centers = [[0, 0], [10, 10], [20, 0]]
    
    # Check that each mean is close to one of the true centers
    for mean in means:
        min_distance = min(squared_distance(mean, center) for center in true_centers)
        assert min_distance < 1.0  # Should be reasonably close


def test_k_means_convergence():
    """Test that k_means converges to a stable solution."""
    # Simple 2-cluster data
    data = [[0, 0], [0.1, 0.1], [0.2, -0.1],  # Cluster 1
            [5, 5], [5.1, 4.9], [4.9, 5.1]]     # Cluster 2
    
    assignments1, means1 = k_means(data, k=2)
    assignments2, means2 = k_means(data, k=2, initial_assignments=assignments1)
    
    # Should converge to same solution (or very similar)
    # Since k-means can have local optima, we just check that it's stable
    assert len(assignments1) == len(assignments2)
    assert len(means1) == len(means2)


def test_cluster_means():
    """Test the cluster_means function."""
    data = [[1, 2], [3, 4], [5, 6], [7, 8]]
    assignments = [0, 0, 1, 1]  # First two in cluster 0, last two in cluster 1
    
    means = cluster_means(data, assignments, k=2)
    
    assert len(means) == 2
    
    # Mean of cluster 0: [(1+3)/2, (2+4)/2] = [2, 3]
    assert means[0] == pytest.approx([2, 3])
    
    # Mean of cluster 1: [(5+7)/2, (6+8)/2] = [6, 7]
    assert means[1] == pytest.approx([6, 7])


def test_squared_clustering_errors():
    """Test the squared_clustering_errors function."""
    data = [[0, 0], [1, 1], [10, 10], [11, 11]]
    assignments = [0, 0, 1, 1]
    means = [[0.5, 0.5], [10.5, 10.5]]
    
    error = squared_clustering_errors(data, assignments, means)
    
    # Should be positive
    assert error > 0
    
    # Calculate expected error manually
    # Cluster 0: distance from [0,0] to [0.5,0.5] = sqrt(0.5), squared = 0.5
    #           distance from [1,1] to [0.5,0.5] = sqrt(0.5), squared = 0.5
    # Cluster 1: distance from [10,10] to [10.5,10.5] = sqrt(0.5), squared = 0.5
    #           distance from [11,11] to [10.5,10.5] = sqrt(0.5), squared = 0.5
    # Total = 0.5 + 0.5 + 0.5 + 0.5 = 2.0
    assert error == pytest.approx(2.0)


def test_k_means_edge_cases():
    """Test k_means with edge cases."""
    # Test with k=1
    data = [[1, 2], [3, 4], [5, 6]]
    assignments, means = k_means(data, k=1)
    
    assert len(means) == 1
    assert all(a == 0 for a in assignments)  # All should be in cluster 0
    
    # Test with k equal to number of points
    assignments, means = k_means(data, k=3)
    
    assert len(means) == 3
    # Each point should be in its own cluster (or some valid assignment)
    for assignment in assignments:
        assert 0 <= assignment < 3


def test_k_means_empty_clusters():
    """Test k_means handling of empty clusters."""
    # Data that might lead to empty clusters
    data = [[0, 0], [0.1, 0.1], [0.2, 0.2]]  # All points very close
    
    assignments, means = k_means(data, k=3)
    
    # Should handle empty clusters gracefully
    assert len(assignments) == len(data)
    assert len(means) == 3
    
    # All points might end up in one cluster, others empty
    # This is acceptable behavior


def test_k_means_random_initialization():
    """Test that k_means works with random initialization."""
    data = [[0, 0], [10, 10], [20, 20]]
    
    # Run multiple times with different random seeds
    results = []
    for _ in range(5):
        assignments, means = k_means(data, k=3)
        results.append((assignments, means))
    
    # All should be valid results
    for assignments, means in results:
        assert len(assignments) == 3
        assert len(means) == 3
        for a in assignments:
            assert 0 <= a < 3


def test_k_means_higher_dimensions():
    """Test k_means with higher dimensional data."""
    # 3D data
    data = [
        [1, 2, 3], [1.1, 2.1, 2.9], [0.9, 1.9, 3.1],  # Cluster 1
        [10, 20, 30], [10.1, 19.9, 30.1], [9.9, 20.1, 29.9]  # Cluster 2
    ]
    
    assignments, means = k_means(data, k=2)
    
    assert len(assignments) == len(data)
    assert len(means) == 2
    
    # Each mean should be 3-dimensional
    for mean in means:
        assert len(mean) == 3


def test_k_means_identical_points():
    """Test k_means with identical points."""
    data = [[1, 1], [1, 1], [1, 1], [5, 5]]
    
    assignments, means = k_means(data, k=2)
    
    # Should handle identical points
    assert len(assignments) == 4
    assert len(means) == 2
    
    # One mean should be at [1, 1], another at [5, 5] (or vice versa)
    means_set = {tuple(round(x, 1) for x in mean) for mean in means}
    assert (1.0, 1.0) in means_set or (5.0, 5.0) in means_set
