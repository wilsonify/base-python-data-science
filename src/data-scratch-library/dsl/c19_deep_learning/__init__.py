"""
Chapter 19: Deep Learning

Layer-based deep learning framework with tensor operations, optimizers,
and loss functions.
"""

from .deep_learning import (
    Tensor,
    shape,
    is_1d,
    tensor_sum,
    tensor_apply,
    zeros_like,
    tensor_combine,
    random_uniform,
    random_normal,
    random_tensor,
)
from .layer import (
    Layer,
    Linear,
    Sequential,
    Tanh,
    Relu,
    Dropout,
    Sigmoid,
    tanh,
)
from .metrics import (
    softmax,
    Loss,
    SSE,
    Optimizer,
    GradientDescent,
    Momentum,
    SoftmaxCrossEntropy,
)
from .io import save_weights, load_weights
