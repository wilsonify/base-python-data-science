from functools import partial

from dsl.c08_gradient_descent.e0804_minibatch_gd import maximize_batch
from dsl.c10_working_with_data.e1009_dimensionality_reduction import directional_variance, directional_variance_gradient


def test_maximize_batch_directional_variance():
    x = [[1, 2, 3], [2, 3, 4], [5, 6, 7]]
    maximize_batch(
        target_fn=partial(directional_variance, x),
        gradient_fn=partial(directional_variance_gradient, x),
        theta_0=[1 for _ in x[0]],
        tolerance=0.000001
    )
