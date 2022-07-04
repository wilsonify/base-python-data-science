# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class MinimizeStochasticInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, x=None, y=None):  # noqa: E501
        """MinimizeStochasticInput - a model defined in OpenAPI

        :param x: The x of this MinimizeStochasticInput.  # noqa: E501
        :type x: List[List[float]]
        :param y: The y of this MinimizeStochasticInput.  # noqa: E501
        :type y: List[float]
        """
        self.openapi_types = {
            'x': List[List[float]],
            'y': List[float]
        }

        self.attribute_map = {
            'x': 'x',
            'y': 'y'
        }

        self._x = x
        self._y = y

    @classmethod
    def from_dict(cls, dikt) -> 'MinimizeStochasticInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The minimize_stochastic-input of this MinimizeStochasticInput.  # noqa: E501
        :rtype: MinimizeStochasticInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def x(self):
        """Gets the x of this MinimizeStochasticInput.


        :return: The x of this MinimizeStochasticInput.
        :rtype: List[List[float]]
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this MinimizeStochasticInput.


        :param x: The x of this MinimizeStochasticInput.
        :type x: List[List[float]]
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this MinimizeStochasticInput.


        :return: The y of this MinimizeStochasticInput.
        :rtype: List[float]
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this MinimizeStochasticInput.


        :param y: The y of this MinimizeStochasticInput.
        :type y: List[float]
        """

        self._y = y