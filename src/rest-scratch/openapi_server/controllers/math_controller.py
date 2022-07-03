import logging
from typing import Tuple

from openapi_server.models import StrengthInput, StrengthOutput
from openapi_server.rpc import RemoteProcedure


def sqrt(body: dict) -> Tuple[dict, int]:  # noqa: E501
    """ square root """
    body['strategy'] = "sqrt"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)
    logging.debug(f"response_body= {response_body}")
    logging.debug(f"status_code= {status_code}")
    return response_body, int(status_code)


def strength(body: dict) -> Tuple[dict, int]:  # noqa: E501
    """ signal strength """
    body_in = StrengthInput().from_dict(body)
    body_in_dict = body_in.to_dict()
    body_in_dict['strategy'] = "strength"
    actual = body_in.actual
    expected = body_in.expected
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body_in_dict)
    strength_response = response_body["strength"]
    out_so = StrengthOutput(
        actual=actual,
        expected=expected,
        strength=strength_response
    )
    return out_so.to_dict(), int(status_code)


def echo(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "echo"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)
    return response_body, status_code


def difference_quotient(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "difference_quotient"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)
    out_dict = response_body
    return out_dict, status_code


def distance(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "distance"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def estimate_gradient(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "estimate_gradient"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def in_random_order(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "in_random_order"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def maximize_batch(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "maximize_batch"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def maximize_stochastic(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "maximize_stochastic"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def minimize_batch(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "minimize_batch"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def minimize_stochastic(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "minimize_stochastic"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def partial_difference_quotient(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "partial_difference_quotient"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def dot(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "dot"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def get_column(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "get_column"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def get_row(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "get_row"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def magnitude(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "magnitude"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def matrix_add(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "matrix_add"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def scalar_multiply(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "scalar_multiply"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def shape(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "shape"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def squared_distance(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "squared_distance"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def sum_of_squares(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "sum_of_squares"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def vector_add(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "vector_add"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def vector_mean(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "vector_mean"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def vector_subtract(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "vector_subtract"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def vector_sum(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "vector_sum"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)
    out_dict = response_body
    return out_dict, status_code


def accuracy(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "accuracy"
    status_code = 200
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)
    out_dict = response_body
    return out_dict, status_code


def f1_score(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "f1_score"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def precision(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "precision"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def recall(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "recall"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def split_data(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "split_data"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def train_test_split(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "train_test_split"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def mysqrt_strategy(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "mysqrt_strategy"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def mystrength_strategy(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "mystrength_strategy"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def bernoulli_trial(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "bernoulli_trial"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def binomial(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "binomial"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def inverse_normal_cdf(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "inverse_normal_cdf"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def normal_cdf(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "normal_cdf"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def normal_pdf(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "normal_pdf"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def random_kid(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "random_kid"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)
    out_dict = response_body
    return out_dict, status_code


def uniform_cdf(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "uniform_cdf"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def uniform_pdf(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "uniform_pdf"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def bucketize(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "bucketize"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def correlation(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "correlation"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def correlation_matrix(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "correlation_matrix"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def covariance(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "covariance"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def data_range(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "data_range"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def de_mean(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "de_mean"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def interquartile_range(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "interquartile_range"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def mean(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "mean"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def median(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "median"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def mode(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "mode"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def quantile(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "quantile"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def standard_deviation(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "standard_deviation"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code


def variance(body: dict) -> Tuple[dict, int]:  # noqa: E501
    body['strategy'] = "variance"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body, status_code = rpc.call(body)

    out_dict = response_body
    return out_dict, status_code
