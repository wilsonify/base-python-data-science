import os
import random
from functools import partial

import dsl.c08_gradient_descent.e0801_estimating_gradient
import dsl.c08_gradient_descent.e0805_stochastic_gd
from dsl.c10_working_with_data.manipulation import directional_variance, directional_variance_gradient
from dsl.c08_gradient_descent import gradient_descent
from dsl.c08_gradient_descent.gradient_descent import negate, negate_all
from dsl.c15_multiple_regression import multiple_regression

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def difference_quotient(self, body: dict):
    x = body["x"]
    h = body["h"]
    result = dsl.c08_gradient_descent.e0801_estimating_gradient.difference_quotient(
        f=lambda xi: xi * xi,
        x=x,
        h=h
    )
    self.publish(result)


def partial_difference_quotient(self, body: dict):
    v = body["v"]
    i = body["i"]
    h = body["h"]
    output = dsl.c08_gradient_descent.e0801_estimating_gradient.partial_difference_quotient(
        f=lambda xi: [_ * _ for _ in xi],
        v=v,
        i=i,
        h=h
    )
    self.publish(output)


def estimate_gradient(self, body: dict):
    v = body["v"]
    h = body["h"]
    output = dsl.c08_gradient_descent.e0801_estimating_gradient.estimate_gradient(
        f=lambda xi: [_ * _ for _ in xi],
        v=v,
        h=h
    )
    self.publish(output)


def in_random_order(self, body: dict):
    data = body["data"]
    output = [_ for _ in dsl.c08_gradient_descent.e0805_stochastic_gd.in_random_order(data)]
    self.publish(output)


def maximize_batch(self, body: dict):
    x = body["x"]
    result = gradient_descent.maximize_batch(
        target_fn=partial(directional_variance, x),
        gradient_fn=partial(directional_variance_gradient, x),
        theta_0=[1 for _ in x[0]],
        tolerance=0.000001
    )
    self.publish(result)


def maximize_stochastic(self, body: dict):
    x = body["x"]
    y = body["y"]
    result = dsl.c08_gradient_descent.e0805_stochastic_gd.maximize_stochastic(
        target_fn=negate(multiple_regression.squared_error),
        gradient_fn=negate_all(multiple_regression.squared_error_gradient),
        x=x,
        y=y,
        theta_0=[random.random() for _ in x[0]],
        alpha_0=0.01
    )
    self.publish(result)


def minimize_batch(self, body: dict):
    x = body["x"]
    result = gradient_descent.minimize_batch(
        target_fn=partial(directional_variance, x),
        gradient_fn=partial(directional_variance_gradient, x),
        theta_0=[1 for _ in x[0]],
        tolerance=0.000001
    )
    self.publish(result)


def minimize_stochastic(self, body: dict):
    x = body["x"]
    y = body["y"]
    result = dsl.c08_gradient_descent.e0805_stochastic_gd.minimize_stochastic(
        target_fn=negate(multiple_regression.squared_error),
        gradient_fn=negate_all(multiple_regression.squared_error_gradient),
        x=x,
        y=y,
        theta_0=[random.random() for _ in x[0]],
        alpha_0=0.01
    )
    self.publish(result)
