# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class SplitDataInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data=None):  # noqa: E501
        """SplitDataInput - a model defined in OpenAPI

        :param data: The data of this SplitDataInput.  # noqa: E501
        :type data: List[List[float]]
        """
        self.openapi_types = {
            'data': List[List[float]]
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt) -> 'SplitDataInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The split_data-input of this SplitDataInput.  # noqa: E501
        :rtype: SplitDataInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this SplitDataInput.


        :return: The data of this SplitDataInput.
        :rtype: List[List[float]]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this SplitDataInput.


        :param data: The data of this SplitDataInput.
        :type data: List[List[float]]
        """

        self._data = data