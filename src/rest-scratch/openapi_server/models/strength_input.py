# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class StrengthInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, actual=None, expected=None):  # noqa: E501
        """StrengthInput - a model defined in OpenAPI

        :param actual: The actual of this StrengthInput.  # noqa: E501
        :type actual: int
        :param expected: The expected of this StrengthInput.  # noqa: E501
        :type expected: int
        """
        self.openapi_types = {
            'actual': int,
            'expected': int
        }

        self.attribute_map = {
            'actual': 'actual',
            'expected': 'expected'
        }

        self._actual = actual
        self._expected = expected

    @classmethod
    def from_dict(cls, dikt) -> 'StrengthInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The strength-input of this StrengthInput.  # noqa: E501
        :rtype: StrengthInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def actual(self):
        """Gets the actual of this StrengthInput.


        :return: The actual of this StrengthInput.
        :rtype: int
        """
        return self._actual

    @actual.setter
    def actual(self, actual):
        """Sets the actual of this StrengthInput.


        :param actual: The actual of this StrengthInput.
        :type actual: int
        """

        self._actual = actual

    @property
    def expected(self):
        """Gets the expected of this StrengthInput.


        :return: The expected of this StrengthInput.
        :rtype: int
        """
        return self._expected

    @expected.setter
    def expected(self, expected):
        """Sets the expected of this StrengthInput.


        :param expected: The expected of this StrengthInput.
        :type expected: int
        """

        self._expected = expected
