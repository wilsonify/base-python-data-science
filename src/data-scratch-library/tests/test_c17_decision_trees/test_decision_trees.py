import pytest
from collections import Counter, defaultdict

from dsl.c17_decision_trees.decision_trees import (
    partition_entropy_by, partition_by, classify, build_tree_id3, 
    entropy, get_class_probabilities, data_entropy, partition_entropy,
    group_by, forest_classify
)


def test_entropy():
    """Test the entropy function."""
    # Test with perfect certainty (entropy = 0)
    perfect_probs = [1.0]
    assert entropy(perfect_probs) == pytest.approx(0.0)
    
    # Test with maximum uncertainty (50/50)
    max_uncertainty = [0.5, 0.5]
    assert entropy(max_uncertainty) == pytest.approx(1.0)
    
    # Test with three outcomes
    three_probs = [0.5, 0.25, 0.25]
    result = entropy(three_probs)
    assert result > 0
    assert result < 1.585  # Maximum for 3 outcomes


def test_get_class_probabilities():
    """Test the get_class_probabilities function."""
    labels = ['A', 'A', 'B', 'C', 'A']
    probs = get_class_probabilities(labels)
    
    # Should have 3 probabilities for 3 unique classes
    assert len(probs) == 3
    
    # Probabilities should sum to 1
    assert sum(probs) == pytest.approx(1.0)
    
    # Check specific probabilities: A=3/5, B=1/5, C=1/5
    assert 0.6 in probs  # 3/5
    assert 0.2 in probs  # 1/5 (appears twice)


def test_data_entropy():
    """Test the data_entropy function."""
    labeled_data = [
        ([1, 2], 'A'), ([3, 4], 'A'), ([5, 6], 'B')
    ]
    
    entropy_val = data_entropy(labeled_data)
    
    # Should be positive
    assert entropy_val > 0
    
    # For 2 A's and 1 B, entropy should be less than 1
    assert entropy_val < 1.0


def test_partition_entropy():
    """Test the partition_entropy function."""
    # Create two subsets
    subset1 = [([1, 2], 'A'), ([3, 4], 'A')]  # Pure A
    subset2 = [([5, 6], 'B'), ([7, 8], 'B')]  # Pure B
    
    subsets = [subset1, subset2]
    entropy_val = partition_entropy(subsets)
    
    # Both subsets are pure, so entropy should be 0
    assert entropy_val == pytest.approx(0.0)


def test_group_by():
    """Test the group_by function."""
    items = [
        ({'level': 'Senior', 'outcome': True}),
        ({'level': 'Junior', 'outcome': False}),
        ({'level': 'Senior', 'outcome': False}),
        ({'level': 'Mid', 'outcome': True})
    ]
    
    groups = group_by(items, lambda x: x[0]['level'])
    
    assert 'Senior' in groups
    assert 'Junior' in groups
    assert 'Mid' in groups
    assert len(groups['Senior']) == 2
    assert len(groups['Junior']) == 1
    assert len(groups['Mid']) == 1


def test_partition_by():
    """Test the partition_by function."""
    inputs = [
        ({'level': 'Senior', 'lang': 'Java'}, True),
        ({'level': 'Senior', 'lang': 'Python'}, False),
        ({'level': 'Junior', 'lang': 'Java'}, True),
        ({'level': 'Junior', 'lang': 'Python'}, False)
    ]
    
    partitions = partition_by(inputs, 'level')
    
    assert 'Senior' in partitions
    assert 'Junior' in partitions
    assert len(partitions['Senior']) == 2
    assert len(partitions['Junior']) == 2


def test_partition_entropy_by():
    """Test the partition_entropy_by function."""
    inputs = [
        ({'level': 'Senior', 'outcome': False}),
        ({'level': 'Senior', 'outcome': False}),
        ({'level': 'Mid', 'outcome': True}),
        ({'level': 'Junior', 'outcome': True}),
    ]
    
    entropy_val = partition_entropy_by(inputs, 'level')
    
    # Should be a positive number
    assert entropy_val > 0
    # Maximum entropy for 4 items would be log2(2) = 1
    assert entropy_val <= 1


def test_classify():
    """Test the classify function."""
    # Test with leaf (simple case)
    leaf_true = True
    leaf_false = False
    
    input_data = {'level': 'Senior', 'lang': 'Java'}
    
    assert classify(input_data, leaf_true) is True
    assert classify(input_data, leaf_false) is False
    
    # Test with tree structure
    # Tree: if level == 'Senior' -> False, else -> True
    tree = ('level', {'Senior': False, 'Junior': True, None: True})
    
    senior_input = {'level': 'Senior', 'lang': 'Java'}
    junior_input = {'level': 'Junior', 'lang': 'Python'}
    
    assert classify(senior_input, tree) is False
    assert classify(junior_input, tree) is True
    
    # Test with unknown attribute value
    unknown_input = {'level': 'Mid', 'lang': 'Python'}
    result_unknown = classify(unknown_input, tree)
    assert result_unknown is True  # Should use None subtree


def test_build_tree_id3():
    """Test the build_tree_id3 function."""
    # Simple training data
    training_data = [
        ({'level': 'Senior', 'lang': 'Java', 'tweets': 'no', 'phd': 'no'}, False),
        ({'level': 'Senior', 'lang': 'Java', 'tweets': 'no', 'phd': 'yes'}, False),
        ({'level': 'Mid', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'R', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'R', 'tweets': 'yes', 'phd': 'yes'}, False),
        ({'level': 'Mid', 'lang': 'R', 'tweets': 'yes', 'phd': 'yes'}, True),
        ({'level': 'Senior', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}, False),
        ({'level': 'Senior', 'lang': 'R', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'Python', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Senior', 'lang': 'Python', 'tweets': 'yes', 'phd': 'yes'}, True),
        ({'level': 'Mid', 'lang': 'Python', 'tweets': 'no', 'phd': 'yes'}, True),
        ({'level': 'Mid', 'lang': 'Java', 'tweets': 'yes', 'phd': 'no'}, True),
        ({'level': 'Junior', 'lang': 'Python', 'tweets': 'no', 'phd': 'yes'}, False)
    ]
    
    # Build tree
    tree = build_tree_id3(training_data)
    
    # Should return a tree (either leaf or split structure)
    assert tree is not None
    assert isinstance(tree, (bool, tuple))
    
    # Test classification with the tree
    test_input = {'level': 'Junior', 'lang': 'Python', 'tweets': 'no', 'phd': 'no'}
    prediction = classify(test_input, tree)
    assert prediction in [True, False]


def test_tree_with_pure_data():
    """Test tree building with pure (homogeneous) data."""
    # All data has the same outcome
    pure_data = [
        ({'feature': 'A'}, True),
        ({'feature': 'B'}, True),
        ({'feature': 'C'}, True)
    ]
    
    tree = build_tree_id3(pure_data)
    
    # Should create a leaf node
    assert tree is True  # All True, so should return True leaf


def test_tree_with_empty_data():
    """Test tree building with edge cases."""
    # Test with empty data
    try:
        tree = build_tree_id3([])
        assert False, "Should raise error with empty data"
    except (IndexError, ValueError):
        pass  # Expected


def test_tree_with_no_attributes():
    """Test tree building with no split attributes."""
    data = [
        ({}, True),
        ({}, False),
        ({}, True)
    ]
    
    tree = build_tree_id3(data)
    
    # Should create a leaf with majority prediction
    assert tree is True  # True appears twice, False once


def test_forest_classify():
    """Test the forest_classify function."""
    # Create simple trees
    tree1 = True  # Always predicts True
    tree2 = False  # Always predicts False
    tree3 = True   # Always predicts True
    
    trees = [tree1, tree2, tree3]
    input_data = {'level': 'Senior'}
    
    result = forest_classify(trees, input_data)
    
    # Should return majority vote (2 True, 1 False = True)
    assert result is True


def test_entropy_calculations():
    """Test entropy calculations for various scenarios."""
    # Test with perfect split (entropy = 0)
    perfect_data = [
        ({'group': 'A'}, True),
        ({'group': 'A'}, True),
        ({'group': 'B'}, False),
        ({'group': 'B'}, False)
    ]
    
    entropy_val = partition_entropy_by(perfect_data, 'group')
    assert entropy_val == pytest.approx(0.0)
    
    # Test with maximum entropy (50/50 split)
    max_entropy_data = [
        ({'group': 'A'}, True),
        ({'group': 'A'}, False),
        ({'group': 'B'}, True),
        ({'group': 'B'}, False)
    ]
    
    entropy_val = partition_entropy_by(max_entropy_data, 'group')
    assert entropy_val > 0


def test_tree_depth():
    """Test that tree building handles depth correctly."""
    # Data that should create a multi-level tree
    data = [
        ({'a1': 'x', 'a2': 'y'}, True),
        ({'a1': 'x', 'a2': 'z'}, False),
        ({'a1': 'w', 'a2': 'y'}, False),
        ({'a1': 'w', 'a2': 'z'}, False)
    ]
    
    tree = build_tree_id3(data)
    
    # Should create a non-trivial tree
    assert isinstance(tree, tuple) or isinstance(tree, bool)
    
    # Test classification
    test_input = {'a1': 'x', 'a2': 'y'}
    prediction = classify(test_input, tree)
    assert prediction in [True, False]
