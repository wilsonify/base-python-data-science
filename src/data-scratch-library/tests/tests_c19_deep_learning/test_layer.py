"""
Test cases for layer module classes.
"""

import random
import pytest
from dsl.c19_deep_learning.layer import (
    Layer, Linear, Sequential, Tanh, Relu, Dropout, tanh
)


class TestLayerBase:
    """Test the Layer base class raises NotImplementedError."""

    def test_forward_not_implemented(self):
        layer = Layer()
        with pytest.raises(NotImplementedError):
            layer.forward([1.0])

    def test_backward_not_implemented(self):
        layer = Layer()
        with pytest.raises(NotImplementedError):
            layer.backward([1.0])

    def test_params_empty(self):
        layer = Layer()
        assert list(layer.params()) == []

    def test_grads_empty(self):
        layer = Layer()
        assert list(layer.grads()) == []


class TestTanhFunction:
    """Test the standalone tanh helper function."""

    def test_tanh_zero(self):
        assert tanh(0.0) == pytest.approx(0.0, abs=1e-7)

    def test_tanh_overflow_positive(self):
        assert tanh(200) == 1

    def test_tanh_overflow_negative(self):
        assert tanh(-200) == -1

    def test_tanh_normal_value(self):
        assert tanh(1.0) == pytest.approx(0.7615941559, abs=1e-5)


class TestLinear:
    """Test the Linear layer."""

    def test_forward_output_length(self):
        random.seed(0)
        layer = Linear(3, 5)
        output = layer.forward([1.0, 2.0, 3.0])
        assert len(output) == 5

    def test_backward_gradient_length(self):
        random.seed(0)
        layer = Linear(3, 5)
        layer.forward([1.0, 2.0, 3.0])
        grad = layer.backward([1.0] * 5)
        assert len(grad) == 3

    def test_params_count(self):
        random.seed(0)
        layer = Linear(3, 5)
        params = list(layer.params())
        # Should return [weights, biases]
        assert len(params) == 2

    def test_grads_after_backward(self):
        random.seed(0)
        layer = Linear(3, 5)
        layer.forward([1.0, 2.0, 3.0])
        layer.backward([1.0] * 5)
        grads = list(layer.grads())
        assert len(grads) == 2


class TestTanhLayer:
    """Test the Tanh activation layer."""

    def test_forward(self):
        layer = Tanh()
        result = layer.forward([0.0, 1.0, -1.0])
        assert result[0] == pytest.approx(0.0, abs=1e-7)
        assert result[1] > 0
        assert result[2] < 0

    def test_backward(self):
        layer = Tanh()
        layer.forward([0.0])
        grad = layer.backward([1.0])
        # tanh(0)=0, derivative = 1 - 0^2 = 1
        assert grad[0] == pytest.approx(1.0, abs=1e-7)


class TestReluLayer:
    """Test the Relu activation layer."""

    def test_forward_positive(self):
        layer = Relu()
        result = layer.forward([1.0, -2.0, 3.0])
        assert result == [1.0, 0, 3.0]

    def test_backward(self):
        layer = Relu()
        layer.forward([1.0, -2.0, 3.0])
        grad = layer.backward([1.0, 1.0, 1.0])
        assert grad == [1.0, 0, 1.0]


class TestSequential:
    """Test the Sequential layer."""

    def test_forward(self):
        random.seed(0)
        net = Sequential([Linear(3, 2), Tanh()])
        output = net.forward([1.0, 2.0, 3.0])
        assert len(output) == 2
        for val in output:
            assert -1.0 <= val <= 1.0

    def test_backward(self):
        random.seed(0)
        net = Sequential([Linear(3, 2), Tanh()])
        net.forward([1.0, 2.0, 3.0])
        grad = net.backward([1.0, 1.0])
        assert len(grad) == 3

    def test_params(self):
        random.seed(0)
        net = Sequential([Linear(3, 2), Tanh()])
        params = list(net.params())
        # Linear has 2 params (w, b), Tanh has 0
        assert len(params) == 2

    def test_grads(self):
        random.seed(0)
        net = Sequential([Linear(3, 2), Tanh()])
        net.forward([1.0, 2.0, 3.0])
        net.backward([1.0, 1.0])
        grads = list(net.grads())
        assert len(grads) == 2


class TestDropout:
    """Test the Dropout layer."""

    def test_train_mode_drops_values(self):
        random.seed(0)
        layer = Dropout(p=0.5)
        layer.train = True
        inp = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
        result = layer.forward(inp)
        # Some values should be zeroed out
        assert 0 in result or 0.0 in result

    def test_eval_mode_scales(self):
        layer = Dropout(p=0.5)
        layer.train = False
        result = layer.forward([2.0, 4.0])
        assert result[0] == pytest.approx(1.0)
        assert result[1] == pytest.approx(2.0)

    def test_backward_train(self):
        random.seed(0)
        layer = Dropout(p=0.5)
        layer.train = True
        layer.forward([1.0, 1.0, 1.0, 1.0])
        grad = layer.backward([1.0, 1.0, 1.0, 1.0])
        assert len(grad) == 4

    def test_backward_eval_raises(self):
        layer = Dropout(p=0.5)
        layer.train = False
        layer.forward([1.0])
        with pytest.raises(RuntimeError):
            layer.backward([1.0])


if __name__ == "__main__":
    from test_runner import TestRunner
    runner = TestRunner()
    runner.run_file(__file__)
