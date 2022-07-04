# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class ScalarMultiplyInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, c=None, mat=None):  # noqa: E501
        """ScalarMultiplyInput - a model defined in OpenAPI

        :param c: The c of this ScalarMultiplyInput.  # noqa: E501
        :type c: float
        :param mat: The mat of this ScalarMultiplyInput.  # noqa: E501
        :type mat: List[List[float]]
        """
        self.openapi_types = {
            'c': float,
            'mat': List[List[float]]
        }

        self.attribute_map = {
            'c': 'c',
            'mat': 'mat'
        }

        self._c = c
        self._mat = mat

    @classmethod
    def from_dict(cls, dikt) -> 'ScalarMultiplyInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The scalar_multiply-input of this ScalarMultiplyInput.  # noqa: E501
        :rtype: ScalarMultiplyInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def c(self):
        """Gets the c of this ScalarMultiplyInput.


        :return: The c of this ScalarMultiplyInput.
        :rtype: float
        """
        return self._c

    @c.setter
    def c(self, c):
        """Sets the c of this ScalarMultiplyInput.


        :param c: The c of this ScalarMultiplyInput.
        :type c: float
        """

        self._c = c

    @property
    def mat(self):
        """Gets the mat of this ScalarMultiplyInput.


        :return: The mat of this ScalarMultiplyInput.
        :rtype: List[List[float]]
        """
        return self._mat

    @mat.setter
    def mat(self, mat):
        """Sets the mat of this ScalarMultiplyInput.


        :param mat: The mat of this ScalarMultiplyInput.
        :type mat: List[List[float]]
        """

        self._mat = mat
