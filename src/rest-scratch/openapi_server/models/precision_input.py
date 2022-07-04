# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model_ import Model
from openapi_server import util


class PrecisionInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, tp=None, fp=None, fn=None, tn=None):  # noqa: E501
        """PrecisionInput - a model defined in OpenAPI

        :param tp: The tp of this PrecisionInput.  # noqa: E501
        :type tp: float
        :param fp: The fp of this PrecisionInput.  # noqa: E501
        :type fp: float
        :param fn: The fn of this PrecisionInput.  # noqa: E501
        :type fn: float
        :param tn: The tn of this PrecisionInput.  # noqa: E501
        :type tn: float
        """
        self.openapi_types = {
            'tp': float,
            'fp': float,
            'fn': float,
            'tn': float
        }

        self.attribute_map = {
            'tp': 'tp',
            'fp': 'fp',
            'fn': 'fn',
            'tn': 'tn'
        }

        self._tp = tp
        self._fp = fp
        self._fn = fn
        self._tn = tn

    @classmethod
    def from_dict(cls, dikt) -> 'PrecisionInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The precision-input of this PrecisionInput.  # noqa: E501
        :rtype: PrecisionInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def tp(self):
        """Gets the tp of this PrecisionInput.

        number of True Positives  # noqa: E501

        :return: The tp of this PrecisionInput.
        :rtype: float
        """
        return self._tp

    @tp.setter
    def tp(self, tp):
        """Sets the tp of this PrecisionInput.

        number of True Positives  # noqa: E501

        :param tp: The tp of this PrecisionInput.
        :type tp: float
        """

        self._tp = tp

    @property
    def fp(self):
        """Gets the fp of this PrecisionInput.

        number of False Positives  # noqa: E501

        :return: The fp of this PrecisionInput.
        :rtype: float
        """
        return self._fp

    @fp.setter
    def fp(self, fp):
        """Sets the fp of this PrecisionInput.

        number of False Positives  # noqa: E501

        :param fp: The fp of this PrecisionInput.
        :type fp: float
        """

        self._fp = fp

    @property
    def fn(self):
        """Gets the fn of this PrecisionInput.

        number of False Negatives  # noqa: E501

        :return: The fn of this PrecisionInput.
        :rtype: float
        """
        return self._fn

    @fn.setter
    def fn(self, fn):
        """Sets the fn of this PrecisionInput.

        number of False Negatives  # noqa: E501

        :param fn: The fn of this PrecisionInput.
        :type fn: float
        """

        self._fn = fn

    @property
    def tn(self):
        """Gets the tn of this PrecisionInput.

        number of True Negatives  # noqa: E501

        :return: The tn of this PrecisionInput.
        :rtype: float
        """
        return self._tn

    @tn.setter
    def tn(self, tn):
        """Sets the tn of this PrecisionInput.

        number of True Negatives  # noqa: E501

        :param tn: The tn of this PrecisionInput.
        :type tn: float
        """

        self._tn = tn
