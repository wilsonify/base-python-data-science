"""
Loss functions (SSE, SoftmaxCrossEntropy) and optimizers
(GradientDescent, Momentum).
"""

import math
from typing import List

from .deep_learning import Tensor, tensor_combine, tensor_sum, zeros_like, is_1d
from .layer import Layer


def softmax(tensor: Tensor) -> Tensor:
    """Softmax along the last dimension (numerically stable)."""
    if is_1d(tensor):
        largest = max(tensor)
        exps = [math.exp(x - largest) for x in tensor]
        total = sum(exps)
        return [e / total for e in exps]
    return [softmax(t) for t in tensor]


# -- Loss functions -------------------------------------------------------------

class Loss:
    """Abstract loss function."""

    def loss(self, predicted: Tensor, actual: Tensor) -> float:
        raise NotImplementedError

    def gradient(self, predicted: Tensor, actual: Tensor) -> Tensor:
        raise NotImplementedError


class SSE(Loss):
    """Sum of squared errors."""

    def loss(self, predicted: Tensor, actual: Tensor) -> float:
        sq = tensor_combine(lambda p, a: (p - a) ** 2, predicted, actual)
        return tensor_sum(sq)

    def gradient(self, predicted: Tensor, actual: Tensor) -> Tensor:
        return tensor_combine(lambda p, a: 2 * (p - a), predicted, actual)


class SoftmaxCrossEntropy(Loss):
    """Negative log-likelihood with softmax."""

    def loss(self, predicted: Tensor, actual: Tensor) -> float:
        probs = softmax(predicted)
        ll = tensor_combine(lambda p, a: math.log(p + 1e-30) * a, probs, actual)
        return -tensor_sum(ll)

    def gradient(self, predicted: Tensor, actual: Tensor) -> Tensor:
        probs = softmax(predicted)
        return tensor_combine(lambda p, a: p - a, probs, actual)


# -- Optimizers -----------------------------------------------------------------

class Optimizer:
    """Abstract optimizer."""

    def step(self, layer: Layer) -> None:
        raise NotImplementedError


class GradientDescent(Optimizer):
    """Vanilla SGD."""

    def __init__(self, learning_rate: float = 0.1) -> None:
        self.lr = learning_rate

    def step(self, layer: Layer) -> None:
        for param, grad in zip(layer.params(), layer.grads()):
            param[:] = tensor_combine(
                lambda p, g: p - g * self.lr, param, grad
            )


class Momentum(Optimizer):
    """SGD with momentum."""

    def __init__(self, learning_rate: float, momentum: float = 0.9) -> None:
        self.lr = learning_rate
        self.mo = momentum
        self.updates: List[Tensor] = []

    def step(self, layer: Layer) -> None:
        if not self.updates:
            self.updates = [zeros_like(g) for g in layer.grads()]
        for update, param, grad in zip(self.updates, layer.params(), layer.grads()):
            update[:] = tensor_combine(
                lambda u, g: self.mo * u + (1 - self.mo) * g, update, grad
            )
            param[:] = tensor_combine(
                lambda p, u: p - self.lr * u, param, update
            )
