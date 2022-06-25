import logging
from typing import Tuple

from openapi_server.models import SqrtInput, SqrtOutput, StrengthInput, StrengthOutput
from openapi_server.rpc import RemoteProcedure


def mysqrt(body: dict) -> Tuple[dict, int]:  # noqa: E501
    """ square root """
    logging.debug(f"body = {body}")
    logging.debug(f"type(body) = {type(body)}")
    body_in = SqrtInput().from_dict(body)
    body_in_dict = body_in.to_dict()
    body_in_dict['strategy'] = "mysqrt"
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body = rpc.call(body_in_dict)
    status_code = response_body['status_code']
    sqrt_output = SqrtOutput().from_dict(response_body)
    body_out = sqrt_output.to_dict()
    return body_out, status_code


def mystrength(body: dict) -> Tuple[dict, int]:  # noqa: E501
    """ signal strength """
    body_in = StrengthInput().from_dict(body)
    body_in_dict = body_in.to_dict()
    body_in_dict['strategy'] = "mystrength"
    actual = body_in.actual
    expected = body_in.expected
    rpc = RemoteProcedure(routing_key='dsfs')
    response_body = rpc.call(body_in_dict)
    status_code = response_body['status_code']
    strength = response_body["strength"]
    out_so = StrengthOutput(
        actual=actual,
        expected=expected,
        strength=strength
    )
    out_dict = out_so.to_dict()
    return out_dict, status_code
