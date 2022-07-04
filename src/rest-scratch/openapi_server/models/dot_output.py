# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class DotOutput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, x=None, result=None):  # noqa: E501
        """DotOutput - a model defined in OpenAPI

        :param x: The x of this DotOutput.  # noqa: E501
        :type x: float
        :param result: The result of this DotOutput.  # noqa: E501
        :type result: float
        """
        self.openapi_types = {
            'x': float,
            'result': float
        }

        self.attribute_map = {
            'x': 'x',
            'result': 'result'
        }

        self._x = x
        self._result = result

    @classmethod
    def from_dict(cls, dikt) -> 'DotOutput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The dot-output of this DotOutput.  # noqa: E501
        :rtype: DotOutput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def x(self):
        """Gets the x of this DotOutput.


        :return: The x of this DotOutput.
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this DotOutput.


        :param x: The x of this DotOutput.
        :type x: float
        """

        self._x = x

    @property
    def result(self):
        """Gets the result of this DotOutput.


        :return: The result of this DotOutput.
        :rtype: float
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this DotOutput.


        :param result: The result of this DotOutput.
        :type result: float
        """

        self._result = result