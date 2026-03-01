"""
Core tensor operations and random tensor generation.
"""

import random
from typing import Callable, List, Union

from dsl.c06_probability.e0603_normal import inverse_normal_cdf

Tensor = Union[List[float], List["Tensor"]]


def shape(tensor: Tensor) -> List[int]:
    """Return the shape of a (nested-list) tensor."""
    sizes: List[int] = []
    while isinstance(tensor, list):
        sizes.append(len(tensor))
        tensor = tensor[0]
    return sizes


def is_1d(tensor: Tensor) -> bool:
    """True if *tensor* is a 1-D list of scalars."""
    return not isinstance(tensor[0], list)


def tensor_sum(tensor: Tensor) -> float:
    """Sum all values in the tensor."""
    if is_1d(tensor):
        return sum(tensor)
    return sum(tensor_sum(t) for t in tensor)


def tensor_apply(f: Callable[[float], float], tensor: Tensor) -> Tensor:
    """Apply *f* element-wise to *tensor*."""
    if is_1d(tensor):
        return [f(x) for x in tensor]
    return [tensor_apply(f, t) for t in tensor]


def zeros_like(tensor: Tensor) -> Tensor:
    """Return a tensor of zeros with the same shape as *tensor*."""
    return tensor_apply(lambda _: 0.0, tensor)


def tensor_combine(
    f: Callable[[float, float], float], t1: Tensor, t2: Tensor
) -> Tensor:
    """Apply *f* to corresponding elements of *t1* and *t2*."""
    if is_1d(t1):
        return [f(x, y) for x, y in zip(t1, t2)]
    return [tensor_combine(f, a, b) for a, b in zip(t1, t2)]


# -- Random tensor constructors ------------------------------------------------

def random_uniform(*dims: int) -> Tensor:
    """Uniform random tensor in [0, 1)."""
    if len(dims) == 1:
        return [random.random() for _ in range(dims[0])]
    return [random_uniform(*dims[1:]) for _ in range(dims[0])]


def random_normal(
    *dims: int, mean: float = 0.0, variance: float = 1.0
) -> Tensor:
    """Normal random tensor via the inverse-CDF method."""
    if len(dims) == 1:
        return [
            mean + variance * inverse_normal_cdf(random.random())
            for _ in range(dims[0])
        ]
    return [
        random_normal(*dims[1:], mean=mean, variance=variance)
        for _ in range(dims[0])
    ]


def random_tensor(*dims: int, init: str = "normal") -> Tensor:
    """Create a random tensor with the given initialisation scheme."""
    if init == "normal":
        return random_normal(*dims)
    if init == "uniform":
        return random_uniform(*dims)
    if init == "xavier":
        variance = len(dims) / sum(dims)
        return random_normal(*dims, variance=variance)
    raise ValueError(f"unknown init: {init}")
