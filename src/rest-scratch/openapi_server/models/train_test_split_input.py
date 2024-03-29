# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class TrainTestSplitInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, x=None, y=None, p=None):  # noqa: E501
        """TrainTestSplitInput - a model defined in OpenAPI

        :param x: The x of this TrainTestSplitInput.  # noqa: E501
        :type x: List[List[float]]
        :param y: The y of this TrainTestSplitInput.  # noqa: E501
        :type y: List[List[float]]
        :param p: The p of this TrainTestSplitInput.  # noqa: E501
        :type p: float
        """
        self.openapi_types = {
            'x': List[List[float]],
            'y': List[List[float]],
            'p': float
        }

        self.attribute_map = {
            'x': 'x',
            'y': 'y',
            'p': 'p'
        }

        self._x = x
        self._y = y
        self._p = p

    @classmethod
    def from_dict(cls, dikt) -> 'TrainTestSplitInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The train_test_split-input of this TrainTestSplitInput.  # noqa: E501
        :rtype: TrainTestSplitInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def x(self):
        """Gets the x of this TrainTestSplitInput.


        :return: The x of this TrainTestSplitInput.
        :rtype: List[List[float]]
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this TrainTestSplitInput.


        :param x: The x of this TrainTestSplitInput.
        :type x: List[List[float]]
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this TrainTestSplitInput.


        :return: The y of this TrainTestSplitInput.
        :rtype: List[List[float]]
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this TrainTestSplitInput.


        :param y: The y of this TrainTestSplitInput.
        :type y: List[List[float]]
        """

        self._y = y

    @property
    def p(self):
        """Gets the p of this TrainTestSplitInput.


        :return: The p of this TrainTestSplitInput.
        :rtype: float
        """
        return self._p

    @p.setter
    def p(self, p):
        """Sets the p of this TrainTestSplitInput.


        :param p: The p of this TrainTestSplitInput.
        :type p: float
        """

        self._p = p
