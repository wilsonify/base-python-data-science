import os

from data_science_from_scratch.library import linear_algebra

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def distance(self, payload):
    result = linear_algebra.distance(vec1, vec2)
    self.publish(payload)


def dot(self, payload):
    result = linear_algebra.dot(vec1, vec2)
    self.publish(payload)


def get_column(self, payload):
    result = linear_algebra.get_column(mat1, col)
    self.publish(payload)


def get_row(mat1, row, expected):
    result = linear_algebra.get_row(mat1, row)
    self.publish(payload)


def is_diagonal(i, j, expected):
    result = linear_algebra.is_diagonal(i, j)
    self.publish(payload)


def magnitude(vec1, expected):
    result = linear_algebra.magnitude(vec1)
    self.publish(payload)


def make_matrix(n, m, expected):
    result = linear_algebra.make_matrix(n, m, linear_algebra.is_diagonal)
    self.publish(payload)


def matrix_add(mat1, mat2, expected):
    result = linear_algebra.matrix_add(mat1, mat2)
    self.publish(payload)


def scalar_multiply(v, c, expected):
    result = linear_algebra.scalar_multiply(c, v)
    self.publish(payload)


def shape(random_matrix):
    num_rows, num_columns = linear_algebra.shape(random_matrix)
    assert num_rows == 100
    assert num_columns == 4


def squared_distance(v1, v2, expected):
    result = linear_algebra.squared_distance(v1, v2)
    self.publish(payload)


def sum_of_squares(v1, expected):
    result = linear_algebra.sum_of_squares(v1)
    self.publish(payload)


def vector_add(v1, v2, expected):
    result = linear_algebra.vector_add(v1, v2)
    self.publish(payload)


def vector_mean(v1, v2, expected):
    result = linear_algebra.vector_mean([v1, v2])
    self.publish(payload)


def vector_subtract(v1, v2, expected):
    result = linear_algebra.vector_subtract(v1, v2)
    self.publish(payload)


def vector_sum(v1, v2, expected):
    result = linear_algebra.vector_sum([v1, v2])
    self.publish(payload)
