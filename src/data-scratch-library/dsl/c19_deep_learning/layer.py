"""
In the previous chapter we built a simple neural net that allowed us to stack two lay‐
ers of neurons, each of which computed sigmoid(dot(weights, inputs)).
Although that’s perhaps an idealized representation of what an actual neuron does, in
practice we’d like to allow a wider variety of things. Perhaps we’d like the neurons to
remember something about their previous inputs. Perhaps we’d like to use a different
activation function than sigmoid. And frequently we’d like to use more than two lay‐
ers. (Our feed_forward function actually handled any number of layers, but our gra‐
dient computations did not.)
In this chapter we’ll build machinery for implementing such a variety of neural net‐
works. Our fundamental abstraction will be the Layer, something that knows how to
apply some function to its inputs and that knows how to backpropagate gradients.
One way of thinking about the neural networks we built in Chapter 18 is as a “linear”
layer, followed by a “sigmoid” layer, then another linear layer and another sigmoid
layer. We didn’t distinguish them in these terms, but doing so will allow us to experi‐
ment with much more general structures:
"""

from typing import Iterable, Tuple, List, Union, Any
from .deep_learning import Tensor, random_tensor, tensor_apply, tensor_combine
from scratch.linear_algebra import dot
import random
import operator
import math
class Layer:
    """
    Our neural networks will be composed of Layers, each of which
    knows how to do some computation on its inputs in the "forward"
    direction and propagate gradients in the "backward" direction.
    """
    def forward(self, input: Tensor) -> Tensor:
        """
        Note the lack of types. We're not going to be prescriptive
        about what kinds of inputs layers can take and what kinds
        of outputs they can return.
        """
        raise NotImplementedError
    
    def backward(self, gradient: Tensor) -> Tensor:
        """
        Similarly, we're not going to be prescriptive about what the
        gradient looks like. It's up to you the user to make sure
        that you're doing things sensibly.
        """
        raise NotImplementedError
    
    def params(self) -> Iterable[Tensor]:
        """
        Returns the parameters of this layer. The default implementation
        returns nothing, so that if you have a layer with no parameters
        you don't have to implement this.
        """
        return ()
    
    def grads(self) -> Iterable[Tensor]:
        """
        Returns the gradients, in the same order as params().
        """
        return ()


from scratch.linear_algebra import dot
class Linear(Layer):
    def __init__(self,
                 input_dim: int,
                 output_dim: int,
                 init: str = 'xavier') -> None:
        """
        A layer of output_dim neurons, each with input_dim weights
        (and a bias).
        """
        self.input_dim = input_dim
        self.output_dim = output_dim
        # self.w[o] is the weights for the oth neuron
        self.w = random_tensor(output_dim, input_dim, init=init)
        # self.b[o] is the bias term for the oth neuron
        self.b = random_tensor(output_dim, init=init)

    def forward(self, input: Tensor) -> Tensor:
        # Save the input to use in the backward pass.
        self.input = input
        # Return the vector of neuron outputs.
        return [dot(input, self.w[o]) + self.b[o]
                for o in range(self.output_dim)]

    def backward(self, gradient: Tensor) -> Tensor:
        # Each b[o] gets added to output[o], which means
        # the gradient of b is the same as the output gradient.
        self.b_grad = gradient
        # Each w[o][i] multiplies input[i] and gets added to output[o].
        # So its gradient is input[i] * gradient[o].
        self.w_grad = [[self.input[i] * gradient[o]
                        for i in range(self.input_dim)]
                       for o in range(self.output_dim)]
        # Each input[i] multiplies every w[o][i] and gets added to every
        # output[o]. So its gradient is the sum of w[o][i] * gradient[o]
        # across all the outputs.
        return [sum(self.w[o][i] * gradient[o] for o in range(self.output_dim))
                for i in range(self.input_dim)]

    def params(self) -> Iterable[Tensor]:
        return [self.w, self.b]
    
    def grads(self) -> Iterable[Tensor]:
        return [self.w_grad, self.b_grad]


from typing import List
class Sequential(Layer):
    """
    A layer consisting of a sequence of other layers.
    It's up to you to make sure that the output of each layer
    makes sense as the input to the next layer.
    """
    def __init__(self, layers: List[Layer]) -> None:
        self.layers = layers
    
    def forward(self, input: Tensor) -> Tensor:
        """Just forward the input through the layers in order."""
        for layer in self.layers:
            input = layer.forward(input)
        return input
    
    def backward(self, gradient: Tensor) -> Tensor:
        """Just backpropagate the gradient through the layers in reverse."""
        for layer in reversed(self.layers):
            gradient = layer.backward(gradient)
        return gradient
    
    def params(self) -> Iterable[Tensor]:
        """Just return the params from each layer."""
        return (param for layer in self.layers for param in layer.params())
    
    def grads(self) -> Iterable[Tensor]:
        """Just return the grads from each layer."""
        return (grad for layer in self.layers for grad in layer.grads())



def tanh(x: float) -> float:
    # If x is very large or very small, tanh is (essentially) 1 or -1.
    # We check for this because, e.g., math.exp(1000) raises an error.
    if x < -100: 
        return -1
    elif x > 100: 
        return 1
    em2x = math.exp(-2 * x)
    return (1 - em2x) / (1 + em2x)

class Tanh(Layer):
    def forward(self, input: Tensor) -> Tensor:
        # Save tanh output to use in backward pass.
        self.tanh = tensor_apply(tanh, input)
        return self.tanh
    
    def backward(self, gradient: Tensor) -> Tensor:
        return tensor_combine(
            lambda tanh_val, grad: (1 - tanh_val ** 2) * grad,
            self.tanh,
            gradient)


class Relu(Layer):
    def forward(self, input: Tensor) -> Tensor:
        self.input = input
        return tensor_apply(lambda x: max(x, 0), input)
    
    def backward(self, gradient: Tensor) -> Tensor:
        return tensor_combine(lambda x, grad: grad if x > 0 else 0,
                             self.input,
                             gradient)

class Dropout(Layer):
    def __init__(self, p: float) -> None:
        self.p = p
        self.train = True
    
    def forward(self, input: Tensor) -> Tensor:
        if self.train:
            # Create a mask of 0s and 1s shaped like the input
            # using the specified probability.
            self.mask = tensor_apply(
                lambda _: 0 if random.random() < self.p else 1,
                input)
            # Multiply by the mask to dropout inputs.
            return tensor_combine(operator.mul, input, self.mask)
        else:
            # During evaluation just scale down the outputs uniformly.
            return tensor_apply(lambda x: x * (1 - self.p), input)
    
    def backward(self, gradient: Tensor) -> Tensor:
        if self.train:
            # Only propagate the gradients where mask == 1.
            return tensor_combine(operator.mul, gradient, self.mask)
        else:
            raise RuntimeError("don't call backward when not in train mode")