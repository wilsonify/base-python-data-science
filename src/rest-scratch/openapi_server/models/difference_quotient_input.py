# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class DifferenceQuotientInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, x=None, h=None):  # noqa: E501
        """DifferenceQuotientInput - a model defined in OpenAPI

        :param x: The x of this DifferenceQuotientInput.  # noqa: E501
        :type x: float
        :param h: The h of this DifferenceQuotientInput.  # noqa: E501
        :type h: float
        """
        self.openapi_types = {
            'x': float,
            'h': float
        }

        self.attribute_map = {
            'x': 'x',
            'h': 'h'
        }

        self._x = x
        self._h = h

    @classmethod
    def from_dict(cls, dikt) -> 'DifferenceQuotientInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The difference_quotient-input of this DifferenceQuotientInput.  # noqa: E501
        :rtype: DifferenceQuotientInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def x(self):
        """Gets the x of this DifferenceQuotientInput.


        :return: The x of this DifferenceQuotientInput.
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this DifferenceQuotientInput.


        :param x: The x of this DifferenceQuotientInput.
        :type x: float
        """

        self._x = x

    @property
    def h(self):
        """Gets the h of this DifferenceQuotientInput.


        :return: The h of this DifferenceQuotientInput.
        :rtype: float
        """
        return self._h

    @h.setter
    def h(self, h):
        """Sets the h of this DifferenceQuotientInput.


        :param h: The h of this DifferenceQuotientInput.
        :type h: float
        """

        self._h = h
