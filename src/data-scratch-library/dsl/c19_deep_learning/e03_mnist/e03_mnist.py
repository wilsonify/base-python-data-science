"""
MNIST digit classification using the deep learning framework.

This demonstrates how to train a neural network to classify handwritten digits
using our layer-based architecture.
"""

import random
import tqdm
import matplotlib.pyplot as plt
import mnist
from typing import List, Tuple
from .layer import Sequential, Linear, Tanh, Dropout
from .metrics import Momentum, SoftmaxCrossEntropy
from .deep_learning import Tensor, shape, tensor_sum

# Import helper functions from scratch
from dsl.c10_working_with_data.e01_working_with_data import argmax

# MNIST is a dataset of handwritten digits that everyone uses to learn deep learning.

# This will download the data; change this to where you want it.
# (Yes, it's a 0-argument function, that's what the library expects.)
# (Yes, I'm assigning a lambda to a variable, like I said never to do.)
mnist.temporary_dir = lambda: '/tmp'

# Each of these functions first downloads the data and returns a numpy array.
# We call .tolist() because our "tensors" are just lists.
train_images = mnist.train_images().tolist()
train_labels = mnist.train_labels().tolist()

"""
Let's plot the first 100 training images to see what they look like (Figure 19-1):
"""
fig, ax = plt.subplots(10, 10)
for i in range(10):
    for j in range(10):
        # Plot each image in black and white and hide the axes.
        ax[i][j].imshow(train_images[10 * i + j], cmap='Greys')
        ax[i][j].xaxis.set_visible(False)
        ax[i][j].yaxis.set_visible(False)
plt.show()

test_images = mnist.test_images().tolist()
test_labels = mnist.test_labels().tolist()

# Compute the average pixel value
avg = tensor_sum(train_images) / 60000 / 28 / 28
# Recenter, rescale, and flatten
train_images = [[(pixel - avg) / 256 for row in image for pixel in row]
                for image in train_images]
test_images = [[(pixel - avg) / 256 for row in image for pixel in row]
               for image in test_images]
# After centering, average pixel should be very close to 0

"""
We also want to one-hot-encode the targets, since we have 10 outputs. First let's write
a one_hot_encode function:
"""
def one_hot_encode(i: int, num_labels: int = 10) -> List[float]:
    return [1.0 if j == i else 0.0 for j in range(num_labels)]


"""
and then apply it to our data:
"""
train_labels = [one_hot_encode(label) for label in train_labels]
test_labels = [one_hot_encode(label) for label in test_labels]

"""
One of the strengths of our abstractions is that we can use the same training/evalua‐
tion loop with a variety of models. So let's write that first. We'll pass it our model, the
data, a loss function, and (if we're training) an optimizer.
It will make a pass through our data, track performance, and (if we passed in an opti‐
mizer) update our parameters:
"""
def loop(model,
         images: List[Tensor],
         labels: List[Tensor],
         loss,
         optimizer=None) -> None:
    correct = 0     # Track number of correct predictions.
    total_loss = 0.0  # Track total loss.
    
    with tqdm.trange(len(images)) as t:
        for i in t:
            predicted = model.forward(images[i])
            if argmax(predicted) == argmax(labels[i]):
                correct += 1
            total_loss += loss.loss(predicted, labels[i])
            # Predict.
            # Check for
            # correctness.
            # Compute loss.
            # If we're training, backpropagate gradient and update weights.
            if optimizer is not None:
                gradient = loss.gradient(predicted, labels[i])
                model.backward(gradient)
                optimizer.step(model)
            # And update our metrics in the progress bar.
            avg_loss = total_loss / (i + 1)
            acc = correct / (i + 1)
            t.set_description(f"mnist loss: {avg_loss:.3f} acc: {acc:.3f}")

"""
One pass through our 60,000 training examples should be enough to learn the model:
"""
random.seed(0)
# Logistic regression is just a linear layer followed by softmax
model = Linear(784, 10)
loss = SoftmaxCrossEntropy()
# This optimizer seems to work
optimizer = Momentum(learning_rate=0.01, momentum=0.99)
# Train on the training data
loop(model, train_images, train_labels, loss, optimizer)
# Test on the test data (no optimizer means just evaluate)
loop(model, test_images, test_labels, loss)

"""
Now let's try a deeper network with dropout:
"""
random.seed(0)
# Name them so we can turn train on and off
dropout1 = Dropout(0.1)
dropout2 = Dropout(0.1)
model = Sequential([
    Linear(784, 30),  # Hidden layer 1: size 30
    dropout1,
    Tanh(),
    Linear(30, 10),   # Hidden layer 2: size 10
    dropout2,
    Tanh(),
    Linear(10, 10)    # Output layer: size 10
])

optimizer = Momentum(learning_rate=0.01, momentum=0.99)
loss = SoftmaxCrossEntropy()
# Enable dropout and train (takes > 20 minutes on my laptop!)
dropout1.train = dropout2.train = True
loop(model, train_images, train_labels, loss, optimizer)
# Disable dropout and evaluate
dropout1.train = dropout2.train = False
loop(model, test_images, test_labels, loss)