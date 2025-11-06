"""
XOR example using the deep learning framework.

This demonstrates how to train a neural network to solve the XOR problem
using our layer-based architecture.
"""

import random
import tqdm
from typing import List
from .layer import Sequential, Linear, Sigmoid
from .metrics import GradientDescent, SSE
from .deep_learning import Tensor

# Create the network architecture
xor_net = Sequential([
    Linear(input_dim=2, output_dim=2),
    Sigmoid(),
    Linear(input_dim=2, output_dim=1),
    Sigmoid()
])

"""
Let's see how easy it is to use our new framework to train a network that can compute
XOR. We start by re-creating the training data:
"""
# training data
xs: List[List[float]] = [[0., 0], [0., 1], [1., 0], [1., 1]]
ys: List[List[float]] = [[0.], [1.], [1.], [0.]]

"""
and then we define the network, although now we can leave off the last sigmoid layer:
"""
random.seed(0)
net = Sequential([
    Linear(input_dim=2, output_dim=2),
    Sigmoid(),
    Linear(input_dim=2, output_dim=1)
])

"""
We can now write a simple training loop, except that now we can use the abstractions
of Optimizer and Loss. This allows us to easily try different ones:
"""
optimizer = GradientDescent(learning_rate=0.1)
loss = SSE()

with tqdm.trange(3000) as t:
    for epoch in t:
        epoch_loss = 0.0
        for x, y in zip(xs, ys):
            predicted = net.forward(x)
            epoch_loss += loss.loss(predicted, y)
            gradient = loss.gradient(predicted, y)
            net.backward(gradient)
            optimizer.step(net)
        t.set_description(f"xor loss {epoch_loss:.3f}")

"""
This should train quickly, and you should see the loss go down. And now we can
inspect the weights:
"""
for param in net.params():
    print(param)

"""
For my network I find roughly:
hidden1 = -2.6 * x1 + -2.7 * x2 + 0.2 # NOR
hidden2 = 2.1 * x1 + 2.1 * x2 - 3.4 # AND
output = -3.1 * h1 + -2.6 * h2 + 1.8 # NOR
So hidden1 activates if neither input is 1. hidden2 activates if both inputs are 1. And
output activates if neither hidden output is 1—that is, if it's not the case that neither
input is 1 and it's also not the case that both inputs are 1. Indeed, this is exactly the
logic of XOR.
Notice that this network learned different features than the one we trained in Chap‐
ter 18, but it still manages to do the same thing.
"""