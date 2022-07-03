# coding: utf-8

from __future__ import absolute_import

import math
import unittest

import pytest
from flask import json

from openapi_server.controllers.math_controller import (
    sqrt,
    variance,
    standard_deviation,
    quantile,
    mode,
    median,
    mean,
    interquartile_range,
    de_mean,
    data_range,
    covariance,
    correlation_matrix,
    correlation,
    bucketize,
    uniform_pdf,
    uniform_cdf,
    echo, distance, in_random_order, random_kid, difference_quotient, estimate_gradient, maximize_batch,
    maximize_stochastic, minimize_batch, minimize_stochastic, partial_difference_quotient, get_column, dot, get_row,
    magnitude, matrix_add, scalar_multiply, shape, squared_distance, sum_of_squares, vector_mean, vector_add,
    vector_subtract, vector_sum, f1_score, accuracy, precision, recall, split_data, train_test_split,
    bernoulli_trial, binomial, inverse_normal_cdf, normal_cdf, normal_pdf
)
from openapi_server.models.sqrt_input import SqrtInput
from openapi_server.models.strength_input import StrengthInput
from openapi_server.test import BaseTestCase


def test_smoke():
    print('fire?')


def test_sqrt():
    body = dict(x=10)
    result = sqrt(body)
    assert result[1] == 200
    assert result[0] == {'result': pytest.approx(3.16, abs=0.1), 'x': 10}


def test_strength():
    body = dict(expected=10, actual=6)
    result = mystrength(body)
    assert result[1] == "200"
    assert result[0] == []


def test_echo():
    body = dict(expected=10, actual=6)
    result = echo(body)
    assert result[1] == "200"
    assert result[0] == dict(expected=10, actual=6, strategy="echo")


def test_difference_quotient():
    body = dict(x=5, h=1)
    result = difference_quotient(body)
    assert result[1] == "200"
    assert result[0] == pytest.approx(11.0, abs=0.1)


@pytest.mark.parametrize(
    ("vec1", "vec2", "expected"), (
            ([0, 0, 0], [10, 10, 10], math.sqrt(300)),
            ([0, 0, 0], [-10, -10, -10], math.sqrt(300)))
)
def test_distance(vec1, vec2, expected):
    body = dict(v=vec1, w=vec2)
    result = distance(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_estimate_gradient():
    body = dict(v=[10.0, 2.0], h=1)
    result = estimate_gradient(body)
    assert result[1] == "200"
    assert result[0] == [[21.0, 0.0], [0.0, 5.0]]


def test_in_random_order():
    body = dict(data=[1, 2, 3, 4, 5, 6])
    result = in_random_order(body)
    assert result[1] == "200"
    assert len(result[0]) == 6


def test_maximize_batch():
    body = dict(x=[[1, 2, 3], [2, 3, 4], [5, 6, 7]])
    result = maximize_batch(body)
    assert result[1] == "200"
    assert result[0] == []


def test_maximize_stochastic():
    body = dict(
        x=[[1, 49, 4, 0], [1, 41, 9, 0], [1, 40, 8, 0], [1, 25, 6, 0], [1, 21, 1, 0], [1, 21, 0, 0], [1, 19, 3, 0],
           [1, 19, 0, 0], [1, 18, 9, 0], [1, 18, 8, 0]],
        y=[68.77, 51.25, 52.08, 38.36, 44.54, 57.13, 51.4, 41.42, 31.22, 34.76, ]
    )
    result = maximize_stochastic(body)
    assert result[1] == "200"
    assert len(result[0]) == 4


def test_minimize_batch():
    body = dict(
        x=[[1, 49, 4, 0], [1, 41, 9, 0], [1, 40, 8, 0], [1, 25, 6, 0], [1, 21, 1, 0], [1, 21, 0, 0], [1, 19, 3, 0],
           [1, 19, 0, 0], [1, 18, 9, 0], [1, 18, 8, 0]],
        y=[68.77, 51.25, 52.08, 38.36, 44.54, 57.13, 51.4, 41.42, 31.22, 34.76, ]
    )
    result = minimize_batch(body)
    assert result[1] == "200"
    assert len(result[0]) == 4


def test_minimize_stochastic():
    body = dict(x=[
        [1, 49, 4, 0], [1, 41, 9, 0], [1, 40, 8, 0],
        [1, 25, 6, 0], [1, 21, 1, 0], [1, 21, 0, 0],
        [1, 19, 3, 0], [1, 19, 0, 0], [1, 18, 9, 0], [1, 18, 8, 0]
    ],
        y=[
            68.77, 51.25, 52.08,
            38.36, 44.54, 57.13,
            51.4, 41.42, 31.22, 34.76,
        ])
    result = minimize_stochastic(body)
    assert result[1] == "200"
    assert result[0] == []


def test_partial_difference_quotient():
    body = dict(expected=10, actual=6)
    result = partial_difference_quotient(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("vec1", "vec2", "expected"), (
            ([1, 1, 1], [10, 10, 10], 30),
            ([1, 1, 1], [-10, -10, -10], -30))
)
def test_dot(vec1, vec2, expected):
    body = dict(v=vec1, w=vec2)
    result = dot(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("mat1", "col", "expected"), (
            ([[1, 2, 3]], 0, [1]),
            ([[1, 2, 3]], 2, [3]))
)
def test_get_column(mat1, col, expected):
    body = dict(mat=mat1, col=col)
    result = get_column(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("mat1", "row", "expected"), (
            ([[1], [2], [3]], 0, [1]),
            ([[1], [2], [3]], 2, [3]))
)
def test_get_row(mat1, row, expected):
    body = dict(mat=mat1, row=row)
    result = get_row(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_magnitude():
    body = dict(expected=10, actual=6)
    result = magnitude(body)
    assert result[1] == "200"
    assert result[0] == []


def test_matrix_add():
    body = dict(expected=10, actual=6)
    result = matrix_add(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_scalar_multiply():
    body = dict(expected=10, actual=6)
    result = scalar_multiply(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_shape():
    body = dict(expected=10, actual=6)
    result = shape(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_squared_distance():
    body = dict(expected=10, actual=6)
    result = squared_distance(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_sum_of_squares():
    body = dict(expected=10, actual=6)
    result = sum_of_squares(body)
    assert result[1] == "200"
    assert result[0] == []


def test_vector_add():
    body = dict(expected=10, actual=6)
    result = vector_add(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_vector_mean():
    body = dict(expected=10, actual=6)
    result = vector_mean(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1], [1], [0]),
            ([1, 0, 0, 1], [1, 2, 3, 4], [0, -2, -3, -3])
    ))
def test_vector_subtract(v1, v2, expected):
    body = dict(expected=10, actual=6)
    result = vector_subtract(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("v1", "v2", "expected"), (
            ([1], [1], [2]),
            ([1, 0, 0, 1], [1, 2, 3, 4], [2, 2, 3, 5])
    ))
def test_vector_sum(v1, v2, expected):
    body = dict(vectors=[v1, v2])
    result = vector_sum(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("tp", "fp", "fn", "tn", "expected"), (
            (100, 120, 200, 303, pytest.approx(0.55, abs=0.01)),
            (100, 1, 200, 303, pytest.approx(0.66, abs=0.01)),
            (0, 120, 200, 303, pytest.approx(0.48, abs=0.01))
    ))
def test_accuracy(tp, fp, fn, tn, expected):
    body = dict(expected=10, actual=6)
    result = accuracy(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_f1_score():
    body = dict(expected=10, actual=6)
    result = f1_score(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_precision():
    body = dict(expected=10, actual=6)
    result = precision(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_recall():
    body = dict(expected=10, actual=6)
    result = recall(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_split_data():
    body = dict(expected=10, actual=6)
    result = split_data(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_train_test_split():
    body = dict(expected=10, actual=6)
    result = train_test_split(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_bernoulli_trial():
    body = dict(expected=10, actual=6)
    result = bernoulli_trial(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_binomial():
    body = dict(expected=10, actual=6)
    result = binomial(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("p", "mu", "sigma", "expected"), (
            (0.01, 100, 5, pytest.approx(88.36, abs=0.01)),
            (0.10, 100, 5, pytest.approx(93.59, abs=0.01)),
            (0.5, 100, 5, pytest.approx(100, abs=0.01)),
            (0.95, 100, 5, pytest.approx(108, abs=1))
    ))
def test_inverse_normal_cdf(p, mu, sigma, expected):
    body = dict(p=p, mu=mu, sigma=sigma)
    result = inverse_normal_cdf(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "mu", "sigma", "expected"), (
            (0.1, 100, 5, pytest.approx(0, abs=0.01)),
            (95, 100, 5, pytest.approx(0.16, abs=0.01)),
            (100, 100, 5, pytest.approx(0.5, abs=0.01)),
            (105, 100, 5, pytest.approx(0.84, abs=1))
    ))
def test_normal_cdf(x, mu, sigma, expected):
    body = dict(x=x, mu=mu, sigma=sigma)
    result = normal_cdf(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_normal_pdf():
    body = dict(expected=10, actual=6)
    result = normal_pdf(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_random_kid():
    body = dict()
    result = random_kid(body)
    assert result[1] == "200"
    assert result[0] in ["Boy", "Girl"]


@pytest.mark.parametrize(
    ("x", "expected"), (
            (0.1, pytest.approx(0.1, abs=0.01)),
            (0.5, pytest.approx(0.5, abs=0.01)),
            (0.9, pytest.approx(0.9, abs=0.01)),
            (2, pytest.approx(1, abs=0.1))
    ))
def test_uniform_cdf(x, expected):
    body = dict(x=x)
    result = uniform_cdf(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            (-0.1, pytest.approx(0, abs=0.01)),
            (0.5, pytest.approx(1, abs=0.01)),
            (0.9, pytest.approx(1, abs=0.01)),
            (2, pytest.approx(0, abs=0.1))
    ))
def test_uniform_pdf(x, expected):
    body = dict(x=x)
    result = uniform_pdf(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_bucketize():
    body = dict(expected=10, actual=6)
    result = bucketize(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_correlation():
    body = dict(expected=10, actual=6)
    result = correlation(body)
    assert result[1] == "200"
    assert result[0] == []


def test_correlation_matrix():
    body = dict(expected=10, actual=6)
    result = correlation_matrix(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_covariance():
    body = dict(expected=10, actual=6)
    result = covariance(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2], pytest.approx(1, abs=0.01)),
            ([1, 2, 10], pytest.approx(9, abs=0.01)),
            ([1, 2, 3, 4, 5], pytest.approx(4, abs=0.1)),
            ([1, 0, 0, 1], pytest.approx(1, abs=0.01))
    ))
def test_data_range(x, expected):
    body = dict(x=x)
    result = data_range(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2], [-0.5, 0.5]),
            ([1, 2, 12], [-4.0, -3.0, 7.0]),
            ([1, 2, 3, 4, 5], [-2.0, -1.0, 0.0, 1.0, 2.0]),
            ([1, 0, 0, 1], [0.5, -0.5, -0.5, 0.5])
    ))
def test_de_mean(x, expected):
    body = dict(x=x)
    result = de_mean(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5),
            ([1, 2, 3, 4, 5, 100, 123], 98),
            ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 3),
            ([1, 0, 0, 1], pytest.approx(1, abs=0.01))
    ))
def test_interquartile_range(x, expected):
    body = dict(expected=10, actual=6)
    result = interquartile_range(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_mean():
    body = dict(expected=10, actual=6)
    result = mean(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5.5),
            ([1, 2, 3, 4, 5, 100, 123], 4),
            ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 4),
            ([1, 0, 0, 1], 0.5)
    ))
def test_median(x, expected):
    body = dict(x=x)
    result = median(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10], [5]),
            ([1, 2, 3, 4, 5, 100, 123, 98, 98], [98]),
            ([1, 4, 6, 5, 4, 3, 3, 15, 4, 3, 6, 7, 3], [3]),
            ([1, 0, 0, 1], [1, 0])
    ))
def test_mode(x, expected):
    body = dict(x=x)
    result = mode(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("p", "x", "expected"), (
            (0.1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2),
            (0.5, [1, 2, 3, 4, 5, 100, 123], 4),
            (0.75, [1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], 6),
            (0.99, [1, 0, 0, 1], 1)
    ))
def test_quantile(p, x, expected):
    body = dict(x=x, p=p)
    result = quantile(body)
    assert result[1] == "200"
    assert result[0] == expected


@pytest.mark.parametrize(
    ("x", "expected"), (
            ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], pytest.approx(3.03, abs=0.01)),
            ([1, 2, 3, 4, 5, 100, 123], pytest.approx(53.37, abs=0.01)),
            ([1, 4, 6, 5, 4, 3, 15, 4, 3, 6, 7], pytest.approx(3.64, abs=0.01)),
            ([1, 0, 0, 1], pytest.approx(0.577, abs=0.01))
    ))
def test_standard_deviation(x, expected):
    body = dict(x=x)
    result = standard_deviation(body)
    assert result[1] == "200"
    assert result[0] == expected


def test_variance():
    body = dict(x=[1, 2, 3, 4])
    result = variance(body)
    assert result[1] == "200"
    assert result[0] == pytest.approx(1.67, abs=0.1)


class TestMathController(BaseTestCase):
    """MathController integration test stubs"""

    def test_mysqrt(self):
        """Test case for mysqrt"""
        sqrt_input = SqrtInput(x=10)
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/v2/sqrt',
            method='POST',
            headers=headers,
            data=json.dumps(sqrt_input),
            content_type='application/json')
        self.assert200(
            response=response,
            message='Response body is : ' + response.data.decode('utf-8')
        )

    def test_mystrength(self):
        """Test case for mystrength"""
        strength_input = StrengthInput(expected=10, actual=6)
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/v2/strength',
            method='POST',
            headers=headers,
            data=json.dumps(strength_input),
            content_type='application/json')
        self.assert200(
            response=response,
            message='Response body is : ' + response.data.decode('utf-8')
        )


if __name__ == '__main__':
    unittest.main()
