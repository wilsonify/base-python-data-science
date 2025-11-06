"""
FizzBuzz example using the deep learning framework.

This demonstrates how to train a neural network to solve the FizzBuzz problem
using our layer-based architecture.
"""

import random
import tqdm
import math
from typing import List
from .layer import Sequential, Linear, Tanh, Sigmoid
from .metrics import Momentum, SSE, SoftmaxCrossEntropy
from .deep_learning import Tensor

# Import helper functions from scratch
from scratch.neural_networks import binary_encode, fizz_buzz_encode, argmax

"""
We can now use our "deep learning" framework to reproduce our solution from
"Example: Fizz Buzz" on page 229. Let's set up the data:
"""
xs = [binary_encode(n) for n in range(101, 1024)]
ys = [fizz_buzz_encode(n) for n in range(101, 1024)]

"""
and create the network:
"""
NUM_HIDDEN = 25
random.seed(0)
net = Sequential([
    Linear(input_dim=10, output_dim=NUM_HIDDEN, init='uniform'),
    Tanh(),
    Linear(input_dim=NUM_HIDDEN, output_dim=4, init='uniform'),
    Sigmoid()
])

"""
As we're training, let's also track our accuracy on the training set:
"""
def fizzbuzz_accuracy(low: int, hi: int, net) -> float:
    num_correct = 0
    for n in range(low, hi):
        x = binary_encode(n)
        predicted = argmax(net.forward(x))
        actual = argmax(fizz_buzz_encode(n))
        if predicted == actual:
            num_correct += 1
    return num_correct / (hi - low)

optimizer = Momentum(learning_rate=0.1, momentum=0.9)
loss = SSE()

with tqdm.trange(1000) as t:
    for epoch in t:
        epoch_loss = 0.0
        for x, y in zip(xs, ys):
            predicted = net.forward(x)
            epoch_loss += loss.loss(predicted, y)
            gradient = loss.gradient(predicted, y)
            net.backward(gradient)
            optimizer.step(net)
        accuracy = fizzbuzz_accuracy(101, 1024, net)
        t.set_description(f"fb loss: {epoch_loss:.2f} acc: {accuracy:.2f}")

# Now check results on the test set
print("test results", fizzbuzz_accuracy(1, 101, net))

"""
Now let's try using softmax cross-entropy loss instead, which should work better
for classification tasks:
"""
def softmax(tensor: Tensor) -> Tensor:
    """Softmax along the last dimension"""
    from .deep_learning import is_1d
    if is_1d(tensor):
        # Subtract largest value for numerical stability.
        largest = max(tensor)
        exps = [math.exp(x - largest) for x in tensor]
        sum_of_exps = sum(exps)
        # This is the total "weight."
        return [exp_i / sum_of_exps
                # Probability is the fraction
                for exp_i in exps]
    # of the total weight.
    else:
        return [softmax(tensor_i) for tensor_i in tensor]

random.seed(0)
net = Sequential([
    Linear(input_dim=10, output_dim=NUM_HIDDEN, init='uniform'),
    Tanh(),
    Linear(input_dim=NUM_HIDDEN, output_dim=4, init='uniform')
    # No final sigmoid layer now
])

optimizer = Momentum(learning_rate=0.1, momentum=0.9)
loss = SoftmaxCrossEntropy()

with tqdm.trange(100) as t:
    for epoch in t:
        epoch_loss = 0.0
        for x, y in zip(xs, ys):
            predicted = net.forward(x)
            epoch_loss += loss.loss(predicted, y)
            gradient = loss.gradient(predicted, y)
            net.backward(gradient)
            optimizer.step(net)
        accuracy = fizzbuzz_accuracy(101, 1024, net)
        t.set_description(f"fb loss: {epoch_loss:.3f} acc: {accuracy:.2f}")

# Again check results on the test set
print("test results", fizzbuzz_accuracy(1, 101, net))