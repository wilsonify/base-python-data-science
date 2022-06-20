import connexion
import six
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.sqrt_input import SqrtInput  # noqa: E501
from openapi_server.models.sqrt_output import SqrtOutput  # noqa: E501
from openapi_server.models.strength_input import StrengthInput  # noqa: E501
from openapi_server.models.strength_output import StrengthOutput  # noqa: E501
from openapi_server import util


def mysqrt(sqrt_input=None):  # noqa: E501
    """mysqrt

    Description of the endpoint # noqa: E501

    :param sqrt_input: 
    :type sqrt_input: dict | bytes

    :rtype: Union[SqrtOutput, Tuple[SqrtOutput, int], Tuple[SqrtOutput, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        sqrt_input = SqrtInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def mystrength(strength_input=None):  # noqa: E501
    """mystrength

    Description of the endpoint # noqa: E501

    :param strength_input: 
    :type strength_input: dict | bytes

    :rtype: Union[StrengthOutput, Tuple[StrengthOutput, int], Tuple[StrengthOutput, int, Dict[str, str]]
    """
    if connexion.request.is_json:
        strength_input = StrengthInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
