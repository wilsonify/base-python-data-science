import logging
import math
from typing import Tuple

from openapi_server.models import SqrtInput, SqrtOutput, StrengthInput, StrengthOutput


def mysqrt(body: dict) -> Tuple[dict, int]:  # noqa: E501
    """ square root """
    logging.debug(f"body = {body}")
    logging.debug(f"type(body) = {type(body)}")
    body_in = SqrtInput().from_dict(body)
    x = body_in.x
    sqrt_output = SqrtOutput(
        x=x,
        result=math.sqrt(x)
    )
    body_out = sqrt_output.to_dict()
    return body_out, 200


def mystrength(body: dict) -> Tuple[dict, int]:  # noqa: E501
    """ signal strength """
    body_in = StrengthInput().from_dict(body)
    actual = body_in.actual
    expected = body_in.expected
    strength = actual / expected
    out_so = StrengthOutput(
        actual=actual,
        expected=expected,
        strength=strength
    )
    out_dict = out_so.to_dict()
    return out_dict, 200
