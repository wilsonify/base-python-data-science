import os

from dsl import linear_algebra

current_dir = os.path.dirname(__file__)
parent_dir = os.path.join(current_dir, os.pardir)


def distance(self, body):
    v = body["v"]
    w = body["w"]
    result = linear_algebra.distance(v, w)
    self.publish(result)


def dot(self, body):
    v = body["v"]
    w = body["w"]
    result = linear_algebra.dot(v, w)
    self.publish(result)


def get_column(self, body):
    mat = body["mat"]
    col = body["col"]
    result = linear_algebra.get_column(mat, col)
    self.publish(result)


def get_row(self, body):
    mat = body["mat"]
    row = body["row"]
    result = linear_algebra.get_row(mat, row)
    self.publish(result)


def magnitude(self, body):
    v = body["v"]
    result = linear_algebra.magnitude(v)
    self.publish(result)


def matrix_add(self, body):
    mat1 = body["mat1"]
    mat2 = body["mat2"]
    result = linear_algebra.matrix_add(mat1, mat2)
    self.publish(result)


def scalar_multiply(self, body):
    c = body["c"]
    v = body["v"]
    result = linear_algebra.scalar_multiply(c, v)
    self.publish(result)


def shape(self, body):
    mat = body["mat"]
    result = linear_algebra.shape(mat)
    self.publish(result)


def squared_distance(self, body):
    v = body["v"]
    w = body["w"]
    result = linear_algebra.squared_distance(v, w)
    self.publish(result)


def sum_of_squares(self, body):
    v = body["v"]
    result = linear_algebra.sum_of_squares(v)
    self.publish(result)


def vector_add(self, body):
    v = body["v"]
    w = body["w"]
    result = linear_algebra.vector_add(v, w)
    self.publish(result)


def vector_mean(self, body):
    vectors = body["vectors"]
    result = linear_algebra.vector_mean(vectors)
    self.publish(result)


def vector_subtract(self, body):
    v = body["v"]
    w = body["w"]
    result = linear_algebra.vector_subtract(v, w)
    self.publish(result)


def vector_sum(self, body):
    vectors = body["vectors"]
    result = linear_algebra.vector_sum(vectors)
    self.publish(result)
