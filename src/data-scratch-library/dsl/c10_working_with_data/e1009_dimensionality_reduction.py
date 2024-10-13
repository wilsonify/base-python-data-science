import sys
from typing import List

from dsl.c04_linear_algebra import Vector
from dsl.c04_linear_algebra.e0401_vectors import vector_mean, vector_subtract, magnitude, dot, scalar_multiply
from dsl.c08_gradient_descent.e0802_using_gradient import gradient_step


def simple_trange(n, width=30):
    """A simple replacement for tqdm.trange that shows a progress bar."""
    for i in range(n):
        percent_complete = (i + 1) / n
        num_blocks = int(width * percent_complete)
        progress_bar = f"[{'#' * num_blocks}{'.' * (width - num_blocks)}]"
        sys.stdout.write(f"\r{progress_bar} {percent_complete:.1%}")
        sys.stdout.flush()
        yield i

    print()  # Newline at the end


def de_mean(data: List[Vector]) -> List[Vector]:
    """Recenters the data to have mean 0 in every dimension"""
    mean = vector_mean(data)
    return [vector_subtract(vector, mean) for vector in data]


def direction(w: Vector) -> Vector:
    mag = magnitude(w)
    return [w_i / mag for w_i in w]


def directional_variance(data: List[Vector], w: Vector) -> float:
    """Returns the variance of x in the direction of w"""
    w_dir = direction(w)
    return sum(dot(v, w_dir) ** 2 for v in data)


def directional_variance_gradient(data: List[Vector], w: Vector) -> Vector:
    """The gradient of directional variance with respect to w"""
    w_dir = direction(w)
    return [sum(2 * dot(v, w_dir) * v[i] for v in data)
            for i in range(len(w))]


def first_principal_component(data: List[Vector], n: int = 100, step_size: float = 0.1) -> Vector:
    """Computes the first principal component using gradient descent."""
    guess = [1.0 for _ in data[0]]
    for _ in simple_trange(n):
        gradient = directional_variance_gradient(data, guess)
        guess = gradient_step(guess, gradient, step_size)
    return direction(guess)


def project(v: Vector, w: Vector) -> Vector:
    """Returns the projection of v onto the direction w"""
    projection_length = dot(v, w)
    return scalar_multiply(projection_length, w)


def remove_projection_from_vector(v: Vector, w: Vector) -> Vector:
    """Projects v onto w and subtracts the result from v"""
    return vector_subtract(v, project(v, w))


def remove_projection(data: List[Vector], w: Vector) -> List[Vector]:
    """Removes the projection from all vectors in the data."""
    return [remove_projection_from_vector(v, w) for v in data]
