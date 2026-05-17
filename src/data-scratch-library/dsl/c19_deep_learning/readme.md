# Chapter 19 – Deep Learning

A modular deep-learning framework built from scratch with composable layers,
loss functions, and optimisers.

---

## Key Concepts

### Tensors

A `Tensor` is a recursive list of floats (i.e. an n-dimensional array). Helper
functions operate on tensors element-wise or recursively:

| Function | Description |
|---|---|
| `shape` | Returns dimensions as a list of ints |
| `is_1d` | True if the tensor is a flat vector |
| `tensor_sum` | Sum of all elements |
| `tensor_apply` | Apply a scalar function element-wise |
| `zeros_like` | Zero tensor with the same shape |
| `tensor_combine` | Apply a binary function to two tensors element-wise |

### The Layer Abstraction

Every building block implements the `Layer` interface:

- `forward(input)` — compute output from input.
- `backward(gradient)` — propagate gradient back; return gradient w.r.t. input.
- `params()` / `grads()` — expose learnable parameters and their gradients.

### Built-in Layers

| Layer | Purpose |
|---|---|
| `Linear` | Fully-connected layer: `dot(weights, input) + bias` |
| `Sequential` | Chain multiple layers into a single network |
| `Sigmoid` | Element-wise sigmoid activation |
| `Tanh` | Element-wise tanh activation |
| `Relu` | Element-wise ReLU activation |
| `Dropout` | Randomly zero activations during training (regularisation) |

### Loss Functions

| Class | Description |
|---|---|
| `SSE` | Sum of squared errors |
| `SoftmaxCrossEntropy` | Softmax + cross-entropy (for classification) |

### Optimisers

| Class | Description |
|---|---|
| `GradientDescent` | Vanilla SGD with a fixed learning rate |
| `Momentum` | SGD with exponential moving-average velocity |

### Weight Initialisation

| Init | Strategy |
|---|---|
| `'normal'` | Standard normal distribution (default) |
| `'uniform'` | Uniform on [0, 1] |
| `'xavier'` | Normal with variance = ndims / sum(dims) |

Generated via `random_tensor(*dims, init='normal')`.

---

## Module Structure

| File | Contents |
|---|---|
| `deep_learning.py` | Tensor utilities, random initialisers |
| `layer.py` | `Layer`, `Linear`, `Sequential`, activations, `Dropout` |
| `metrics.py` | `softmax`, loss classes, optimiser classes |
| `io.py` | I/O helpers |

---

## Examples

| Script | Description |
|---|---|
| [`e01_xor_revisited.py`](e01_xor_revisited.py) | Learn XOR with the modular framework |
| [`e02_fizzbuzz_revisited.py`](e02_fizzbuzz_revisited.py) | Fizz Buzz with a deeper network |
| [`e03_mnist/`](e03_mnist/) | MNIST digit recognition |

---

## Further Reading

- [Deep learning – Wikipedia](https://en.wikipedia.org/wiki/Deep_learning)
- [Xavier initialisation](https://proceedings.mlr.press/v9/glorot10a.html)
- *Data Science from Scratch*, Chapter 19
