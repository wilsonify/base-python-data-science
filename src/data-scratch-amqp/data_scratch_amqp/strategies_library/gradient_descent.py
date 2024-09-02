import os
import random
from functools import partial

from dsl.c10_working_with_data.manipulation import directional_variance, directional_variance_gradient
from dsl.c08_gradient_descent.gradient_descent import negate, negate_all
from dsl.c14_simple_linear_regression.simple_linear_regression import squared_error_gradient
from dsl.c15_multiple_regression.multiple_regression import squared_error

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def difference_quotient(self, body: dict):
    x = body["x"]
    h = body["h"]
    result = difference_quotient(
        f=lambda xi: xi * xi,
        x=x,
        h=h
    )
    self.publish(result)


def partial_difference_quotient(self, body: dict):
    v = body["v"]
    i = body["i"]
    h = body["h"]
    output = partial_difference_quotient(
        f=lambda xi: [_ * _ for _ in xi],
        v=v,
        i=i,
        h=h
    )
    self.publish(output)


def estimate_gradient(self, body: dict):
    v = body["v"]
    h = body["h"]
    output = estimate_gradient(
        f=lambda xi: [_ * _ for _ in xi],
        v=v,
        h=h
    )
    self.publish(output)


def in_random_order(self, body: dict):
    data = body["data"]
    output = [_ for _ in in_random_order(data)]
    self.publish(output)


def maximize_batch(self, body: dict):
    x = body["x"]
    result = maximize_batch(
        target_fn=partial(directional_variance, x),
        gradient_fn=partial(directional_variance_gradient, x),
        theta_0=[1 for _ in x[0]],
        tolerance=0.000001
    )
    self.publish(result)


def maximize_stochastic(self, body: dict):
    x = body["x"]
    y = body["y"]
    result = maximize_stochastic(
        target_fn=negate(squared_error),
        gradient_fn=negate_all(squared_error_gradient),
        x=x,
        y=y,
        theta_0=[random.random() for _ in x[0]],
        alpha_0=0.01
    )
    self.publish(result)


def minimize_batch(self, body: dict):
    x = body["x"]
    result = minimize_batch(
        target_fn=partial(directional_variance, x),
        gradient_fn=partial(directional_variance_gradient, x),
        theta_0=[1 for _ in x[0]],
        tolerance=0.000001
    )
    self.publish(result)


def minimize_stochastic(self, body: dict):
    x = body["x"]
    y = body["y"]
    result = minimize_stochastic(
        target_fn=negate(squared_error),
        gradient_fn=negate_all(squared_error_gradient),
        x=x,
        y=y,
        theta_0=[random.random() for _ in x[0]],
        alpha_0=0.01
    )
    self.publish(result)
