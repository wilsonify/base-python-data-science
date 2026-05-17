import math
import random

from dsl.c08_gradient_descent.decorators import safe, negate, negate_all
from dsl.c08_gradient_descent.e0801_estimating_gradient import partial_difference_quotient
from dsl.c08_gradient_descent.e0802_using_gradient import main as e0802_main
from dsl.c08_gradient_descent.e0804_minibatch_gd import (
    e0804_minibatch_sgd_main,
    e0805_minibatch_sgd_main,
)


def test_negate():
    f = lambda x: x * 2
    neg_f = negate(f)
    assert neg_f(3) == -6
    assert neg_f(-4) == 8


def test_negate_all():
    f = lambda x: [x, x * 2, x * 3]
    neg_f = negate_all(f)
    assert neg_f(2) == [-2, -4, -6]


def test_safe_catches_exceptions():
    def raises_value_error(x):
        raise ValueError("test")

    safe_fn = safe(raises_value_error)
    assert safe_fn(1) == float("inf")

    def raises_zero_div(x):
        return 1 / 0

    safe_fn = safe(raises_zero_div)
    assert safe_fn(1) == float("inf")


def test_partial_difference_quotient_vector_valued():
    """Test the except TypeError branch where f returns a list."""
    def f(v):
        return [v[0] ** 2, v[1] ** 2]

    result = partial_difference_quotient(f, [3.0, 4.0], 0, h=1e-5)
    # Partial wrt v[0]: [2*3, 0] = [6.0, 0.0]
    assert math.isclose(result[0], 6.0, rel_tol=1e-3)
    assert math.isclose(result[1], 0.0, abs_tol=1e-3)


def test_e0802_main(capsys):
    random.seed(42)
    e0802_main()


def test_e0804_minibatch_sgd_main(capsys):
    random.seed(42)
    e0804_minibatch_sgd_main()


def test_e0805_minibatch_sgd_main(capsys):
    random.seed(42)
    e0805_minibatch_sgd_main()
