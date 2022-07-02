import os
import random
from functools import partial

from data_science_from_scratch import multiple_regression
from data_science_from_scratch.library import gradient_descent
from data_science_from_scratch.library.gradient_descent import negate, negate_all
from data_science_from_scratch.library.manipulation import directional_variance, directional_variance_gradient

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def difference_quotient(self, body: dict):
    x = 5
    h = 1
    naive_square = body["naive_square"]
    result = gradient_descent.difference_quotient(
        f=naive_square,
        x=x,
        h=h
    )
    


def partial_difference_quotient(self, body: dict):
    naive_square_comprehension = body["naive_square_comprehension"]
    output = gradient_descent.partial_difference_quotient(
        f=naive_square_comprehension,
        v=[10.0, 2.0],
        i=0,
        h=1
    )
    


def distance(self, body: dict):
    v = body["v"]
    w = body["w"]
    result = gradient_descent.distance(v=v, w=w)
    

def estimate_gradient(self, body: dict):
    naive_square_comprehension = body["naive_square_comprehension"]
    output = gradient_descent.estimate_gradient(
        f=naive_square_comprehension,
        v=[10.0, 2.0],
        h=1
    )
    


def in_random_order(self, body: dict):
    random.seed(0)
    output = gradient_descent.in_random_order(data=[1, 2, 3, 4, 5, 6])
    


def maximize_batch(self, body: dict):
    x = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]
    gradient_descent.maximize_batch(
        target_fn=partial(directional_variance, x),
        gradient_fn=partial(directional_variance_gradient, x),
        theta_0=[1 for _ in x[0]],
        tolerance=0.000001
    )


def maximize_stochastic(self, body: dict):
    x = [
        [1, 49, 4, 0], [1, 41, 9, 0], [1, 40, 8, 0],
        [1, 25, 6, 0], [1, 21, 1, 0], [1, 21, 0, 0],
        [1, 19, 3, 0], [1, 19, 0, 0], [1, 18, 9, 0], [1, 18, 8, 0]
    ]
    y = [
        68.77, 51.25, 52.08,
        38.36, 44.54, 57.13,
        51.4, 41.42, 31.22, 34.76,
    ]
    gradient_descent.maximize_stochastic(
        target_fn=negate(multiple_regression.squared_error),
        gradient_fn=negate_all(multiple_regression.squared_error_gradient),
        x=x,
        y=y,
        theta_0=[random.random() for _ in x[0]],
        alpha_0=0.01
    )
