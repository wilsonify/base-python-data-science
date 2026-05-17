"""
Test cases for deep_learning module tensor operations.
"""

import operator
import random
import pytest
from dsl.c19_deep_learning.deep_learning import (
    shape, is_1d, tensor_sum, tensor_apply, zeros_like,
    tensor_combine, random_uniform, random_normal, random_tensor,
    Sigmoid
)

def test_shape():
    """Test tensor shape function"""
    assert shape([1, 2, 3]) == [3]
    assert shape([[1, 2], [3, 4], [5, 6]]) == [3, 2]

def test_shape_multidimensional():
    """Test shape with 3D tensor"""
    t = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    assert shape(t) == [2, 2, 2]

def test_is_1d():
    """Test 1D tensor detection"""
    assert is_1d([1, 2, 3])
    assert not is_1d([[1, 2], [3, 4]])

def test_tensor_sum():
    """Test tensor sum function"""
    assert tensor_sum([1, 2, 3]) == 6
    assert tensor_sum([[1, 2], [3, 4]]) == 10

def test_tensor_sum_3d():
    """Test tensor sum with 3D tensor"""
    t = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    assert tensor_sum(t) == 36

def test_tensor_apply():
    """Test element-wise tensor operations"""
    assert tensor_apply(lambda x: x + 1, [1, 2, 3]) == [2, 3, 4]
    assert tensor_apply(lambda x: 2 * x, [[1, 2], [3, 4]]) == [[2, 4], [6, 8]]

def test_tensor_apply_3d():
    """Test tensor_apply on 3D tensor"""
    t = [[[1, 2], [3, 4]]]
    result = tensor_apply(lambda x: x * 0, t)
    assert result == [[[0, 0], [0, 0]]]

def test_zeros_like():
    """Test zeros tensor creation"""
    assert zeros_like([1, 2, 3]) == [0, 0, 0]
    assert zeros_like([[1, 2], [3, 4]]) == [[0, 0], [0, 0]]

def test_tensor_combine():
    """Test tensor combination operations"""
    assert tensor_combine(operator.add, [1, 2, 3], [4, 5, 6]) == [5, 7, 9]
    assert tensor_combine(operator.mul, [1, 2, 3], [4, 5, 6]) == [4, 10, 18]

def test_tensor_combine_2d():
    """Test tensor_combine on 2D tensors"""
    result = tensor_combine(operator.add, [[1, 2], [3, 4]], [[10, 20], [30, 40]])
    assert result == [[11, 22], [33, 44]]

def test_random_tensors():
    """Test random tensor generation"""
    assert shape(random_uniform(2, 3, 4)) == [2, 3, 4]
    assert shape(random_normal(5, 6, mean=10)) == [5, 6]

def test_sigmoid_forward():
    """Test Sigmoid forward pass"""
    sig = Sigmoid()
    result = sig.forward([0.0])
    assert abs(result[0] - 0.5) < 1e-7

def test_sigmoid_backward():
    """Test Sigmoid backward pass computes sig*(1-sig)*grad"""
    sig = Sigmoid()
    sig.forward([0.0])
    grad = sig.backward([1.0])
    # sigmoid(0)=0.5, derivative = 0.5*0.5 = 0.25
    assert abs(grad[0] - 0.25) < 1e-7

def test_sigmoid_2d():
    """Test Sigmoid on 2D tensor"""
    sig = Sigmoid()
    result = sig.forward([[0.0, 0.0], [0.0, 0.0]])
    assert abs(result[0][0] - 0.5) < 1e-7
    assert abs(result[1][1] - 0.5) < 1e-7

def test_random_tensor_normal():
    """Test random_tensor with init='normal'"""
    random.seed(42)
    t = random_tensor(3, 4, init='normal')
    assert shape(t) == [3, 4]

def test_random_tensor_uniform():
    """Test random_tensor with init='uniform'"""
    random.seed(42)
    t = random_tensor(2, 5, init='uniform')
    assert shape(t) == [2, 5]
    # All values should be in [0, 1)
    for row in t:
        for val in row:
            assert 0.0 <= val < 1.0

def test_random_tensor_xavier():
    """Test random_tensor with init='xavier'"""
    random.seed(42)
    t = random_tensor(3, 4, init='xavier')
    assert shape(t) == [3, 4]

def test_random_tensor_invalid():
    """Test random_tensor raises on invalid init"""
    with pytest.raises(ValueError, match="unknown init"):
        random_tensor(2, 3, init='bad')

if __name__ == "__main__":
    from test_runner import TestRunner
    runner = TestRunner()
    runner.run_file(__file__)
