"""
Test cases for deep_learning module tensor operations.
"""

import operator
from dsl.c19_deep_learning.deep_learning import (
    shape, is_1d, tensor_sum, tensor_apply, zeros_like, 
    tensor_combine, random_uniform, random_normal
)

def test_shape():
    """Test tensor shape function"""
    assert shape([1, 2, 3]) == [3]
    assert shape([[1, 2], [3, 4], [5, 6]]) == [3, 2]

def test_is_1d():
    """Test 1D tensor detection"""
    assert is_1d([1, 2, 3])
    assert not is_1d([[1, 2], [3, 4]])

def test_tensor_sum():
    """Test tensor sum function"""
    assert tensor_sum([1, 2, 3]) == 6
    assert tensor_sum([[1, 2], [3, 4]]) == 10

def test_tensor_apply():
    """Test element-wise tensor operations"""
    assert tensor_apply(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]
    assert tensor_apply(lambda x: 2 * x, [[1, 2], [3, 4]]) == [[2, 4], [6, 8]]

def test_zeros_like():
    """Test zeros tensor creation"""
    assert zeros_like([1, 2, 3]) == [0, 0, 0]
    assert zeros_like([[1, 2], [3, 4]]) == [[0, 0], [0, 0]]

def test_tensor_combine():
    """Test tensor combination operations"""
    assert tensor_combine(operator.add, [1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert tensor_combine(operator.mul, [1, 2, 3], [4, 5, 6]) == [4, 10, 18]

def test_random_tensors():
    """Test random tensor generation"""
    assert shape(random_uniform(2, 3, 4)) == [2, 3, 4]
    assert shape(random_normal(5, 6, mean=10)) == [5, 6]

if __name__ == "__main__":
    test_shape()
    test_is_1d()
    test_tensor_sum()
    test_tensor_apply()
    test_zeros_like()
    test_tensor_combine()
    test_random_tensors()
    print("All deep learning tests passed!")
