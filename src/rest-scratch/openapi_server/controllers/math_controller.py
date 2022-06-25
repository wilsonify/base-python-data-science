import math

import connexion
import six
from openapi_server import util
from openapi_server.models.api_response import ApiResponse  # noqa: E501
from openapi_server.models.sqrt_input import SqrtInput
from openapi_server.models.strength_input import StrengthInput


def mysqrt(body):  # noqa: E501
    """ square root """
    if connexion.request.is_json:
        body = SqrtInput.from_dict(connexion.request.get_json())  # noqa: E501

    return dict(
        x=body['x'],
        result=math.sqrt()
    )


def mystrength(body):  # noqa: E501
    """ signal strength """
    if connexion.request.is_json:
        body = StrengthInput.from_dict(connexion.request.get_json())  # noqa: E501
    actual = body['actual']
    expected = body['expected']
    result = actual / expected
    return dict(
        actual=actual,
        expected=expected,
        result=result
    )
