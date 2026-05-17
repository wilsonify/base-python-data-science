# Chapter 18 – Neural Networks

From-scratch implementation of feed-forward neural networks trained with backpropagation.

---

## Key Concepts

### Perceptrons

A perceptron computes a weighted sum of its inputs plus a bias and fires
(returns 1) if the result is non-negative:

$$\text{output} = \begin{cases} 1 & \text{if } \mathbf{w} \cdot \mathbf{x} + b \geq 0 \\ 0 & \text{otherwise} \end{cases}$$

Single perceptrons can represent AND, OR, and NOT gates but **cannot** represent
XOR — motivating multi-layer networks.

### Feed-Forward Networks

A feed-forward network stacks layers of neurons. Each neuron applies
`sigmoid(dot(weights, inputs))` and passes its output to the next layer.
The network is represented as a list of layers, where each layer is a list of
weight vectors.

### Backpropagation

Training uses gradient descent on the squared-error loss:

1. **Forward pass** — compute all neuron outputs.
2. **Compute loss** — sum of squared errors vs. target.
3. **Backward pass** — propagate gradients from output to hidden layers.
4. **Update weights** — take a gradient-descent step.

---

## Module API

| Function | Signature | Description |
|---|---|---|
| `step_function` | `(x: float) → int` | Returns 1 if x ≥ 0, else 0 |
| `perceptron_output` | `(weights, bias, x) → int` | Single-perceptron classification |
| `sigmoid` | `(t: float) → float` | Logistic sigmoid: $1/(1+e^{-t})$ |
| `neuron_output` | `(weights, inputs) → float` | Sigmoid of the dot product (includes bias input) |
| `feed_forward` | `(network, input_vector) → List[Vector]` | Run input through all layers; returns every layer's output |
| `backpropagation` | `(network, input_vector, targets) → List[List[Vector]]` | Compute weight gradients via backpropagation |

### Typical Usage

```python
network = [
    [[random() for _ in range(3)] for _ in range(2)],  # hidden layer
    [[random() for _ in range(3)]]                       # output layer
]
for epoch in range(20000):
    for x, y in zip(xs, ys):
        gradients = backpropagation(network, x, y)
        network = [[gradient_step(n, g, -lr)
                     for n, g in zip(layer, layer_grad)]
                    for layer, layer_grad in zip(network, gradients)]
```

---

## Example

See [`e01_neural_networks.py`](e01_neural_networks.py) for XOR learning and
Fizz Buzz solved with a neural network.

---

## Further Reading

- [Backpropagation – Wikipedia](https://en.wikipedia.org/wiki/Backpropagation)
- [Universal approximation theorem](https://en.wikipedia.org/wiki/Universal_approximation_theorem)
- *Data Science from Scratch*, Chapter 18
