import logging
from typing import Tuple

from openapi_server.models import StrengthInput, StrengthOutput
from openapi_server.rpc import rpc_call


def sqrt(body: dict) -> Tuple[dict, int]:  # noqa: E501
    """square root"""
    response_body, status_code = rpc_call(
        body_dict=body, routing_key="dsfs", strategy_str="sqrt"
    )
    logging.debug(f"response_body= {response_body}")
    logging.debug(f"status_code= {status_code}")
    return response_body, int(status_code)


def strength(body: dict) -> Tuple[dict, int]:  # noqa: E501
    """signal strength"""
    body_in = StrengthInput().from_dict(body)
    body_in_dict = body_in.to_dict()
    actual = body_in.actual
    expected = body_in.expected
    response_body, status_code = rpc_call(
        body_dict=body_in_dict, routing_key="dsfs", strategy_str="strength"
    )
    strength_response = response_body["strength"]
    out_so = StrengthOutput(
        actual=actual, expected=expected, strength=strength_response
    )
    return out_so.to_dict(), int(status_code)


def echo(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(
        body_dict=body, routing_key="dsfs", strategy_str="echo"
    )
    return response_body, status_code


def difference_quotient(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "difference_quotient")
    out_dict = response_body
    return out_dict, status_code


def distance(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "distance")
    out_dict = response_body
    return out_dict, status_code


def estimate_gradient(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "estimate_gradient")
    out_dict = response_body
    return out_dict, status_code


def in_random_order(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "in_random_order")
    out_dict = response_body
    return out_dict, status_code


def maximize_batch(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "maximize_batch")
    out_dict = response_body
    return out_dict, status_code


def maximize_stochastic(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "maximize_stochastic")
    out_dict = response_body
    return out_dict, status_code


def minimize_batch(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "minimize_batch")
    out_dict = response_body
    return out_dict, status_code


def minimize_stochastic(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "minimize_stochastic")
    out_dict = response_body
    return out_dict, status_code


def partial_difference_quotient(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "partial_difference_quotient")
    out_dict = response_body
    return out_dict, status_code


def dot(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "dot")

    out_dict = response_body
    return out_dict, status_code


def get_column(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "get_column")

    out_dict = response_body
    return out_dict, status_code


def get_row(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "get_row")

    out_dict = response_body
    return out_dict, status_code


def magnitude(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "magnitude")

    out_dict = response_body
    return out_dict, status_code


def matrix_add(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "matrix_add")

    out_dict = response_body
    return out_dict, status_code


def scalar_multiply(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "scalar_multiply")

    out_dict = response_body
    return out_dict, status_code


def shape(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "shape")

    out_dict = response_body
    return out_dict, status_code


def squared_distance(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "squared_distance")

    out_dict = response_body
    return out_dict, status_code


def sum_of_squares(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "sum_of_squares")

    out_dict = response_body
    return out_dict, status_code


def vector_add(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "vector_add")

    out_dict = response_body
    return out_dict, status_code


def vector_mean(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "vector_mean")

    out_dict = response_body
    return out_dict, status_code


def vector_subtract(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "vector_subtract")

    out_dict = response_body
    return out_dict, status_code


def vector_sum(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "vector_sum")

    out_dict = response_body
    return out_dict, status_code


def accuracy(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "accuracy")
    status_code = 200

    out_dict = response_body
    return out_dict, status_code


def f1_score(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "f1_score")

    out_dict = response_body
    return out_dict, status_code


def precision(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "precision")

    out_dict = response_body
    return out_dict, status_code


def recall(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "recall")

    out_dict = response_body
    return out_dict, status_code


def split_data(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "split_data")

    out_dict = response_body
    return out_dict, status_code


def train_test_split(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "train_test_split")
    out_dict = response_body
    return out_dict, status_code


def mysqrt_strategy(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "mysqrt_strategy")
    out_dict = response_body
    return out_dict, status_code


def mystrength_strategy(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "mystrength_strategy")
    out_dict = response_body
    return out_dict, status_code


def bernoulli_trial(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "bernoulli_trial")
    out_dict = response_body
    return out_dict, status_code


def binomial(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "binomial")
    out_dict = response_body
    return out_dict, status_code


def inverse_normal_cdf(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "inverse_normal_cdf")
    return response_body, status_code


def normal_cdf(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "normal_cdf")
    out_dict = response_body
    return out_dict, status_code


def normal_pdf(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "normal_pdf")
    out_dict = response_body
    return out_dict, status_code


def random_kid(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "random_kid")
    out_dict = response_body
    return out_dict, status_code


def uniform_cdf(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "uniform_cdf")
    out_dict = response_body
    return out_dict, status_code


def uniform_pdf(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "uniform_pdf")
    return response_body, status_code


def bucketize(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "bucketize")
    out_dict = response_body
    return out_dict, status_code


def correlation(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "correlation")
    out_dict = response_body
    return out_dict, status_code


def correlation_matrix(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "correlation_matrix")
    out_dict = response_body
    return out_dict, status_code


def covariance(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "covariance")
    out_dict = response_body
    return out_dict, status_code


def data_range(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "data_range")
    out_dict = response_body
    return out_dict, status_code


def de_mean(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "de_mean")
    out_dict = response_body
    return out_dict, status_code


def interquartile_range(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "interquartile_range")
    out_dict = response_body
    return out_dict, status_code


def mean(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "mean")
    out_dict = response_body
    return out_dict, status_code


def median(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "median")
    out_dict = response_body
    return out_dict, status_code


def mode(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "mode")
    out_dict = response_body
    return out_dict, status_code


def quantile(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "quantile")
    out_dict = response_body
    return out_dict, status_code


def standard_deviation(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "standard_deviation")
    out_dict = response_body
    return out_dict, status_code


def variance(body: dict) -> Tuple[dict, int]:  # noqa: E501
    response_body, status_code = rpc_call(body, "dsfs", "variance")
    out_dict = response_body
    return out_dict, status_code
