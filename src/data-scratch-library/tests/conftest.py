"""
Shared pytest fixtures for data-scratch-library tests
"""
import math
import random
import pytest


@pytest.fixture
def seed_random():
    """Fixture to seed random for deterministic tests"""
    random.seed(42)
    yield
    

@pytest.fixture
def zero_vector():
    """Common zero vector for tests"""
    return [0, 0, 0]


@pytest.fixture
def unit_vectors():
    """Common unit vectors"""
    return {
        'x': [1, 0, 0],
        'y': [0, 1, 0],
        'z': [0, 0, 1]
    }


@pytest.fixture
def sample_vectors():
    """Sample vectors for testing"""
    return {
        'v1': [1, 2, 3],
        'v2': [4, 5, 6],
        'v3': [-1, -2, -3]
    }


@pytest.fixture
def sample_matrix():
    """Sample 3x3 matrix"""
    return [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]


@pytest.fixture
def identity_matrix_2x2():
    """2x2 identity matrix"""
    return [
        [1, 0],
        [0, 1]
    ]


@pytest.fixture
def identity_matrix_3x3():
    """3x3 identity matrix"""
    return [
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]


@pytest.fixture
def sample_data():
    """Sample statistical data"""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


@pytest.fixture
def small_dataset():
    """Small dataset for statistics"""
    return [2.0, 4.0, 6.0, 8.0]


@pytest.fixture
def constant_list():
    """List with all same values"""
    return [5, 5, 5, 5, 5]


@pytest.fixture
def bimodal_data():
    """Data with two modes"""
    return [1, 1, 2, 2, 3, 4, 5]


@pytest.fixture
def tolerance():
    """Standard tolerance for floating point comparisons"""
    return 1e-9


@pytest.fixture
def relaxed_tolerance():
    """Relaxed tolerance for floating point comparisons"""
    return 1e-6
