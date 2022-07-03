# coding: utf-8

from __future__ import absolute_import

import os
import unittest

import pytest
from flask import json


from openapi_server.controllers.math_controller import mysqrt, mystrength
from openapi_server.models.sqrt_input import SqrtInput  # noqa: E501
from openapi_server.models.strength_input import StrengthInput  # noqa: E501
from openapi_server.test import BaseTestCase


def test_smoke():
    import shutil
    from data_science_from_scratch.__main__ import available_strategies
    for k in available_strategies:
        if k=="sqrt":
            continue
        if k=="strength":
            continue
        os.makedirs(
            f"/home/thom/repos/base-python-data-science/src/rest-scratch/openapi_server/openapi/paths/{k}",
            exist_ok=True
        )
        shutil.copy2(
            src=f"/home/thom/repos/base-python-data-science/src/rest-scratch/openapi_server/openapi/paths/sqrt/sqrt.yaml",
            dst=f"/home/thom/repos/base-python-data-science/src/rest-scratch/openapi_server/openapi/paths/{k}/{k}.yaml"
        )
        shutil.copy2(
            src=f"/home/thom/repos/base-python-data-science/src/rest-scratch/openapi_server/openapi/paths/sqrt/sqrt-input.yaml",
            dst=f"/home/thom/repos/base-python-data-science/src/rest-scratch/openapi_server/openapi/paths/{k}/{k}-input.yaml"
        )
        shutil.copy2(
            src=f"/home/thom/repos/base-python-data-science/src/rest-scratch/openapi_server/openapi/paths/sqrt/sqrt-output.yaml",
            dst=f"/home/thom/repos/base-python-data-science/src/rest-scratch/openapi_server/openapi/paths/{k}/{k}-output.yaml"
        )






def test_mysqrt():
    body = dict(x=10)
    result = mysqrt(body)
    assert result[1] == 200
    assert result[0] == {'result': pytest.approx(3.16, abs=0.1), 'x': 10}


def test_mystrength():
    body = dict(expected=10, actual=6)
    result = mystrength(body)
    assert result[1] == 200
    assert result[0] == {'actual': 6, 'expected': 10, 'strength': pytest.approx(0.6, abs=0.1)}


class TestMathController(BaseTestCase):
    """MathController integration test stubs"""

    def test_mysqrt(self):
        """Test case for mysqrt"""
        sqrt_input = SqrtInput(x=10)
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
        self.assert200(
            response=response,
            message='Response body is : ' + response.data.decode('utf-8')
        )

    def test_mystrength(self):
        """Test case for mystrength"""
        strength_input = StrengthInput(expected=10, actual=6)
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
        self.assert200(
            response=response,
            message='Response body is : ' + response.data.decode('utf-8')
        )


if __name__ == '__main__':
    unittest.main()
