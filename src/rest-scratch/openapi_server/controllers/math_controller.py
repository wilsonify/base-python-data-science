import connexion
import six

from openapi_server.models.api_response import ApiResponse  # noqa: E501
from openapi_server.models.pet import Pet  # noqa: E501
from openapi_server import util
import math


def mysqrt(body):  # noqa: E501
    """ square root """
    if connexion.request.is_json:
        body = Pet.from_dict(connexion.request.get_json())  # noqa: E501

    return dict(
        x=body['x'],
        result=math.sqrt()
    )


def mystrength(body):  # noqa: E501
    """ signal strength """
    if connexion.request.is_json:
        body = Pet.from_dict(connexion.request.get_json())  # noqa: E501
    actual = body['actual']
    expected = body['expected']
    result = actual / expected
    return dict(
        actual=actual,
        expected=expected,
        result=result
    )
