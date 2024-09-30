import random

from dsl.c04_linear_algebra import Vector
from dsl.c04_linear_algebra.e0401_vectors import scalar_multiply, vector_add, distance


def gradient_step(v: Vector, gradient: Vector, step_size: float) -> Vector:
    """
    Moves `step_size` in the `gradient` direction from `v`
    """
    assert len(v) == len(gradient)
    step = scalar_multiply(step_size, gradient)
    return vector_add(v, step)


def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]


def main():
    # pick a random starting point
    v = [random.uniform(-10, 10) for i in range(3)]

    for epoch in range(1000):
        grad = sum_of_squares_gradient(v)
        v = gradient_step(v, grad, -0.01)  # take a negative gradient step
        print(epoch, v)  # compute the gradient at v

    assert distance(v, [0, 0, 0]) < 0.001  # v should be close to 0


if __name__ == "__main__":
    main()
