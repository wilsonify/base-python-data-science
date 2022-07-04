# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class DataRangeInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, x=None):  # noqa: E501
        """DataRangeInput - a model defined in OpenAPI

        :param x: The x of this DataRangeInput.  # noqa: E501
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
    def from_dict(cls, dikt) -> 'DataRangeInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The data_range-input of this DataRangeInput.  # noqa: E501
        :rtype: DataRangeInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def x(self):
        """Gets the x of this DataRangeInput.


        :return: The x of this DataRangeInput.
        :rtype: List[float]
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this DataRangeInput.


        :param x: The x of this DataRangeInput.
        :type x: List[float]
        """

        self._x = x
