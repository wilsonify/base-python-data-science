# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.models.sqrt_input import SqrtInput  # noqa: E501
from openapi_server.models.sqrt_output import SqrtOutput  # noqa: E501
from openapi_server.models.strength_input import StrengthInput  # noqa: E501
from openapi_server.models.strength_output import StrengthOutput  # noqa: E501
from openapi_server.test import BaseTestCase


class TestMathController(BaseTestCase):
    """MathController integration test stubs"""

    def test_mysqrt(self):
        """Test case for mysqrt

        
        """
        sqrt_input = openapi_server.SqrtInput()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/v2/sqrt',
            method='POST',
            headers=headers,
            data=json.dumps(sqrt_input),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mystrength(self):
        """Test case for mystrength

        
        """
        strength_input = openapi_server.StrengthInput()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/v2/strength',
            method='POST',
            headers=headers,
            data=json.dumps(strength_input),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
