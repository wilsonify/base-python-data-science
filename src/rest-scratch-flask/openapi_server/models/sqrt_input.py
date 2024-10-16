# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SqrtInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, x=None):  # noqa: E501
        """SqrtInput - a model defined in OpenAPI

        :param x: The x of this SqrtInput.  # noqa: E501
        :type x: float
        """
        self.openapi_types = {
            'x': float
        }

        self.attribute_map = {
            'x': 'x'
        }

        self._x = x

    @classmethod
    def from_dict(cls, dikt) -> 'SqrtInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The sqrt-input of this SqrtInput.  # noqa: E501
        :rtype: SqrtInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def x(self):
        """Gets the x of this SqrtInput.


        :return: The x of this SqrtInput.
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this SqrtInput.


        :param x: The x of this SqrtInput.
        :type x: float
        """

        self._x = x
