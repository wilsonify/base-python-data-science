from math import sqrt
from typing import List, Tuple

from dsl.c04_linear_algebra import Vector


def vector_mean(vectors: List[Vector]) -> Vector:
    """Calculate the mean of each dimension in the list of vectors."""
    n = len(vectors)
    return [sum(vector[i] for vector in vectors) / n for i in range(len(vectors[0]))]


def standard_deviation(data: List[float]) -> float:
    """Compute the standard deviation of a list of numbers."""
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)
    return sqrt(variance)


def scale(data: List[Vector]) -> Tuple[Vector, Vector]:
    """Returns the mean and standard deviation for each position in the data."""
    dim = len(data[0])
    means = vector_mean(data)
    stdevs = [standard_deviation([vector[i] for vector in data]) for i in range(dim)]
    return means, stdevs


def rescale(data: List[Vector]) -> List[Vector]:
    """
    Rescales the input data so that each position has
    mean 0 and standard deviation 1.
    (Leaves a position as is if its standard deviation is 0.)
    """
    dim = len(data[0])
    means, stdevs = scale(data)
    # Rescale each vector
    rescaled = [
        [(v[i] - means[i]) / stdevs[i] if stdevs[i] > 0 else v[i] for i in range(dim)]
        for v in data
    ]
    return rescaled
