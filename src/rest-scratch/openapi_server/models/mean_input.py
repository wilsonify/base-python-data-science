# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class MeanInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, x=None):  # noqa: E501
        """MeanInput - a model defined in OpenAPI

        :param x: The x of this MeanInput.  # noqa: E501
        :type x: List[float]
        """
        self.openapi_types = {
            'x': List[float]
        }

        self.attribute_map = {
            'x': 'x'
        }

        self._x = x

    @classmethod
    def from_dict(cls, dikt) -> 'MeanInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The mean-input of this MeanInput.  # noqa: E501
        :rtype: MeanInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def x(self):
        """Gets the x of this MeanInput.


        :return: The x of this MeanInput.
        :rtype: List[float]
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this MeanInput.


        :param x: The x of this MeanInput.
        :type x: List[float]
        """

        self._x = x
