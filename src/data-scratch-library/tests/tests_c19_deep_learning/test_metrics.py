"""
Test cases for metrics module in metrics.py.
"""

import random
import math
import pytest
from dsl.c19_deep_learning.metrics import (
    softmax, SSE, SoftmaxCrossEntropy, GradientDescent, Momentum
)
from dsl.c19_deep_learning.layer import Linear


def test_slice_assignment():
    """Test slice assignment vs regular assignment"""
    tensor = [[1, 2], [3, 4]]

    for row in tensor:
        row = [0, 0]
    assert tensor == [[1, 2], [3, 4]], "assignment doesn't update a list"

    for row in tensor:
        row[:] = [0, 0]
    assert tensor == [[0, 0], [0, 0]], "but slice assignment does"


class TestSoftmax:
    """Test the softmax function."""

    def test_sums_to_one(self):
        result = softmax([1.0, 2.0, 3.0])
        assert sum(result) == pytest.approx(1.0)

    def test_all_equal(self):
        result = softmax([0.0, 0.0, 0.0])
        for val in result:
            assert val == pytest.approx(1.0 / 3.0)

    def test_2d_tensor(self):
        result = softmax([[1.0, 2.0], [3.0, 4.0]])
        assert len(result) == 2
        assert sum(result[0]) == pytest.approx(1.0)
        assert sum(result[1]) == pytest.approx(1.0)

    def test_numerical_stability(self):
        result = softmax([1000.0, 1001.0, 1002.0])
        assert sum(result) == pytest.approx(1.0)


class TestSSE:
    """Test Sum of Squared Errors loss."""

    def test_loss_zero(self):
        sse = SSE()
        assert sse.loss([1.0, 2.0], [1.0, 2.0]) == pytest.approx(0.0)

    def test_loss_value(self):
        sse = SSE()
        # (1-0)^2 + (2-0)^2 = 1 + 4 = 5
        assert sse.loss([1.0, 2.0], [0.0, 0.0]) == pytest.approx(5.0)

    def test_gradient(self):
        sse = SSE()
        grad = sse.gradient([3.0, 1.0], [1.0, 1.0])
        # 2*(3-1)=4, 2*(1-1)=0
        assert grad[0] == pytest.approx(4.0)
        assert grad[1] == pytest.approx(0.0)


class TestSoftmaxCrossEntropy:
    """Test SoftmaxCrossEntropy loss."""

    def test_loss_positive(self):
        sce = SoftmaxCrossEntropy()
        loss = sce.loss([2.0, 0.0], [1, 0])
        assert loss > 0

    def test_gradient_shape(self):
        sce = SoftmaxCrossEntropy()
        grad = sce.gradient([1.0, 2.0, 3.0], [0, 0, 1])
        assert len(grad) == 3

    def test_gradient_direction(self):
        sce = SoftmaxCrossEntropy()
        # One-hot for class 2 (index 2)
        grad = sce.gradient([1.0, 2.0, 3.0], [0, 0, 1])
        # For the actual class, gradient = p - 1 (should be negative)
        assert grad[2] < 0


class TestGradientDescent:
    """Test GradientDescent optimizer."""

    def test_step_updates_params(self):
        random.seed(0)
        layer = Linear(2, 2)
        inp = [1.0, 1.0]
        layer.forward(inp)
        layer.backward([1.0, 1.0])

        w_before = [row[:] for row in layer.w]
        b_before = layer.b[:]

        opt = GradientDescent(learning_rate=0.1)
        opt.step(layer)

        # Params should have changed
        changed = False
        for i in range(len(layer.w)):
            for j in range(len(layer.w[i])):
                if layer.w[i][j] != w_before[i][j]:
                    changed = True
        assert changed


class TestMomentum:
    """Test Momentum optimizer."""

    def test_step_updates_params(self):
        random.seed(0)
        layer = Linear(2, 2)
        inp = [1.0, 1.0]
        layer.forward(inp)
        layer.backward([1.0, 1.0])

        w_before = [row[:] for row in layer.w]

        opt = Momentum(learning_rate=0.1, momentum=0.9)
        opt.step(layer)

        changed = False
        for i in range(len(layer.w)):
            for j in range(len(layer.w[i])):
                if layer.w[i][j] != w_before[i][j]:
                    changed = True
        assert changed

    def test_momentum_accumulates(self):
        random.seed(0)
        layer = Linear(2, 2)

        opt = Momentum(learning_rate=0.01, momentum=0.9)

        # Two steps with same gradient
        for _ in range(2):
            layer.forward([1.0, 1.0])
            layer.backward([1.0, 1.0])
            opt.step(layer)

        # updates list should be populated
        assert len(opt.updates) == 2


if __name__ == "__main__":
    from test_runner import TestRunner
    runner = TestRunner()
    runner.run_file(__file__)
