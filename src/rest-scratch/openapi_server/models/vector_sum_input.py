# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class VectorSumInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, v=None, w=None):  # noqa: E501
        """VectorSumInput - a model defined in OpenAPI

        :param v: The v of this VectorSumInput.  # noqa: E501
        :type v: List[float]
        :param w: The w of this VectorSumInput.  # noqa: E501
        :type w: List[float]
        """
        self.openapi_types = {
            'v': List[float],
            'w': List[float]
        }

        self.attribute_map = {
            'v': 'v',
            'w': 'w'
        }

        self._v = v
        self._w = w

    @classmethod
    def from_dict(cls, dikt) -> 'VectorSumInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The vector_sum-input of this VectorSumInput.  # noqa: E501
        :rtype: VectorSumInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def v(self):
        """Gets the v of this VectorSumInput.


        :return: The v of this VectorSumInput.
        :rtype: List[float]
        """
        return self._v

    @v.setter
    def v(self, v):
        """Sets the v of this VectorSumInput.


        :param v: The v of this VectorSumInput.
        :type v: List[float]
        """

        self._v = v

    @property
    def w(self):
        """Gets the w of this VectorSumInput.


        :return: The w of this VectorSumInput.
        :rtype: List[float]
        """
        return self._w

    @w.setter
    def w(self, w):
        """Sets the w of this VectorSumInput.


        :param w: The w of this VectorSumInput.
        :type w: List[float]
        """

        self._w = w