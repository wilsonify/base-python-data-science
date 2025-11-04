import random

from dsl.c08_gradient_descent import negate, negate_all
from dsl.c08_gradient_descent.e0805_stochastic_gd import maximize_stochastic
from dsl.c15_multiple_regression.multiple_regression import squared_error, squared_error_gradient


def test_maximize_stochastic_squared_error():
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
    maximize_stochastic(
        target_fn=negate(squared_error),
        gradient_fn=negate_all(squared_error_gradient),
        x=x,
        y=y,
        theta_0=[random.random() for _ in x[0]],
        alpha_0=0.01
    )
