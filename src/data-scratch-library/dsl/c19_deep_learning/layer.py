"""
Neural-network layer abstractions: Layer, Linear, Sequential, and
activation layers (Sigmoid, Tanh, Relu, Dropout).
"""

import math
import operator
import random
from typing import Iterable, List

from dsl.c04_linear_algebra.e0401_vectors import dot
from .deep_learning import Tensor, random_tensor, tensor_apply, tensor_combine


class Layer:
    """Base class for all layers."""

    def forward(self, input: Tensor) -> Tensor:
        raise NotImplementedError

    def backward(self, gradient: Tensor) -> Tensor:
        raise NotImplementedError

    def params(self) -> Iterable[Tensor]:
        return ()

    def grads(self) -> Iterable[Tensor]:
        return ()


class Linear(Layer):
    """Fully-connected layer."""

    def __init__(self, input_dim: int, output_dim: int, init: str = "xavier") -> None:
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.w = random_tensor(output_dim, input_dim, init=init)
        self.b = random_tensor(output_dim, init=init)

    def forward(self, input: Tensor) -> Tensor:
        self.input = input
        return [dot(input, self.w[o]) + self.b[o] for o in range(self.output_dim)]

    def backward(self, gradient: Tensor) -> Tensor:
        self.b_grad = gradient
        self.w_grad = [
            [self.input[i] * gradient[o] for i in range(self.input_dim)]
            for o in range(self.output_dim)
        ]
        return [
            sum(self.w[o][i] * gradient[o] for o in range(self.output_dim))
            for i in range(self.input_dim)
        ]

    def params(self) -> Iterable[Tensor]:
        return [self.w, self.b]

    def grads(self) -> Iterable[Tensor]:
        return [self.w_grad, self.b_grad]


class Sequential(Layer):
    """A sequence of layers applied in order."""

    def __init__(self, layers: List[Layer]) -> None:
        self.layers = layers

    def forward(self, inputs: Tensor) -> Tensor:
        output = inputs
        for layer in self.layers:
            output = layer.forward(output)
        return output

    def backward(self, gradient: Tensor) -> Tensor:
        for layer in reversed(self.layers):
            gradient = layer.backward(gradient)
        return gradient

    def params(self) -> Iterable[Tensor]:
        return (p for layer in self.layers for p in layer.params())

    def grads(self) -> Iterable[Tensor]:
        return (g for layer in self.layers for g in layer.grads())


# -- Activation layers ----------------------------------------------------------

def tanh(x: float) -> float:
    """Numerically stable tanh."""
    if x < -100:
        return -1.0
    if x > 100:
        return 1.0
    em2x = math.exp(-2 * x)
    return (1 - em2x) / (1 + em2x)


class Sigmoid(Layer):
    """Element-wise sigmoid activation."""

    def forward(self, input: Tensor) -> Tensor:
        from dsl.c18_neural_networks.neural_networks import sigmoid
        self.sigmoids = tensor_apply(sigmoid, input)
        return self.sigmoids

    def backward(self, gradient: Tensor) -> Tensor:
        return tensor_combine(
            lambda sig, grad: sig * (1 - sig) * grad,
            self.sigmoids,
            gradient,
        )


class Tanh(Layer):
    """Element-wise tanh activation."""

    def forward(self, input: Tensor) -> Tensor:
        self.tanh = tensor_apply(tanh, input)
        return self.tanh

    def backward(self, gradient: Tensor) -> Tensor:
        return tensor_combine(
            lambda t, g: (1 - t ** 2) * g, self.tanh, gradient
        )


class Relu(Layer):
    """Element-wise ReLU activation."""

    def forward(self, input: Tensor) -> Tensor:
        self.input = input
        return tensor_apply(lambda x: max(x, 0), input)

    def backward(self, gradient: Tensor) -> Tensor:
        return tensor_combine(
            lambda x, g: g if x > 0 else 0, self.input, gradient
        )


class Dropout(Layer):
    """Inverted dropout layer."""

    def __init__(self, p: float) -> None:
        self.p = p
        self.train = True

    def forward(self, input: Tensor) -> Tensor:
        if self.train:
            self.mask = tensor_apply(
                lambda _: 0 if random.random() < self.p else 1, input
            )
            return tensor_combine(operator.mul, input, self.mask)
        return tensor_apply(lambda x: x * (1 - self.p), input)

    def backward(self, gradient: Tensor) -> Tensor:
        if self.train:
            return tensor_combine(operator.mul, gradient, self.mask)
        raise RuntimeError("don't call backward when not in train mode")
