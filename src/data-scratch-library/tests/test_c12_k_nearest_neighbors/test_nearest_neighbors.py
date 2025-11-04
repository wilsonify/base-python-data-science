import pytest
from collections import Counter

from dsl.c12_k_nearest_neighbors.nearest_neighbors import (
    knn_classify, majority_vote, raw_majority_vote, get_distances, try_several_k
)
from dsl.c04_linear_algebra.e0401_vectors import distance


def test_majority_vote():
    """Test the majority_vote function."""
    # Test with clear majority
    labels = ['A', 'A', 'B']  # A should win
    result = majority_vote(labels)
    assert result == 'A'
    
    # Test with tie (should recursively remove last element)
    labels_tie = ['A', 'B']
    result_tie = majority_vote(labels_tie)
    assert result_tie in ['A', 'B']  # Either is acceptable with tie


def test_raw_majority_vote():
    """Test the raw_majority_vote function."""
    labels = ['A', 'A', 'B', 'A']
    result = raw_majority_vote(labels)
    assert result == 'A'
    
    # Test with tie (raw majority vote picks first most common)
    labels_tie = ['A', 'B', 'A', 'B']
    result_tie = raw_majority_vote(labels_tie)
    assert result_tie in ['A', 'B']


def test_knn_classify():
    """Test the knn_classify function."""
    # Test data: points with labels
    labeled_points = [
        ([1, 0], 'A'), ([0, 1], 'A'),  # A points
        ([3, 3], 'B'), ([4, 4], 'B')   # B points
    ]
    
    new_point = [0, 0]  # Should be closer to A points
    
    # Test with k=1
    result = knn_classify(1, labeled_points, new_point)
    assert result == 'A'
    
    # Test with k=3
    result_k3 = knn_classify(3, labeled_points, new_point)
    assert result_k3 == 'A'  # 2 A's vs 1 B among 3 nearest


def test_knn_classify_k2():
    """Test knn_classify with k=2."""
    labeled_points = [
        ([1, 0], 'A'), ([0, 1], 'A'),
        ([3, 3], 'B'), ([4, 4], 'B')
    ]
    
    new_point = [2, 2]  # Somewhere in the middle
    
    result = knn_classify(2, labeled_points, new_point)
    assert result in ['A', 'B']  # Should be one of them


def test_knn_classify_edge_cases():
    """Test knn_classify edge cases."""
    labeled_points = [([1, 1], 'A')]
    
    # Test with k larger than dataset
    result = knn_classify(5, labeled_points, [0, 0])
    assert result == 'A'  # Only choice available
    
    # Test with single point
    result_single = knn_classify(1, labeled_points, [1, 1])
    assert result_single == 'A'


def test_distance_calculation():
    """Test that distance calculations work correctly in KNN context."""
    # Test points forming a right triangle
    labeled_points = [
        ([3, 4], 'far'), ([1, 0], 'close1'), ([0, 1], 'close2')
    ]
    
    new_point = [0, 0]
    
    # With k=1, should pick the closest point
    result = knn_classify(1, labeled_points, new_point)
    
    # Distance to [3,4] is 5, to [1,0] is 1, to [0,1] is 1
    # Should pick either 'close1' or 'close2' (both distance 1)
    assert result in ['close1', 'close2']


def test_try_several_k():
    """Test the try_several_k function."""
    # Use the cities data from the module
    from dsl.c12_k_nearest_neighbors.nearest_neighbors import cities
    
    # This function logs results, so we just test it runs without error
    try:
        try_several_k(cities)
        assert True  # If it runs without error, test passes
    except Exception as e:
        pytest.fail(f"try_several_k raised an exception: {e}")


def test_get_distances():
    """Test the get_distances function."""
    # This function generates random distances and logs results
    # We just test it runs without error
    try:
        get_distances()
        assert True  # If it runs without error, test passes
    except Exception as e:
        pytest.fail(f"get_distances raised an exception: {e}")


def test_knn_with_higher_dimensions():
    """Test KNN with higher dimensional data."""
    labeled_points = [
        ([1, 2, 3, 4], 'A'), ([2, 3, 4, 5], 'A'),
        ([10, 20, 30, 40], 'B'), ([11, 21, 31, 41], 'B')
    ]
    
    new_point = [1, 2, 3, 5]  # Close to A points
    
    result = knn_classify(1, labeled_points, new_point)
    assert result == 'A'


def test_knn_consistency():
    """Test that KNN gives consistent results."""
    labeled_points = [
        ([0, 0], 'A'), ([1, 1], 'A'), 
        ([10, 10], 'B'), ([11, 11], 'B')
    ]
    
    new_point = [0.5, 0.5]
    
    # Should give same result multiple times
    result1 = knn_classify(1, labeled_points, new_point)
    result2 = knn_classify(1, labeled_points, new_point)
    
    assert result1 == result2
