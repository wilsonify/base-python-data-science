# coding: utf-8

from __future__ import absolute_import

import unittest

from flask import json

from openapi_server.test import BaseTestCase


class TestPetController(BaseTestCase):
    """PetController integration test stubs"""

    @unittest.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
    def test_add_pet(self):
        """Test case for add_pet

        Add a new pet to the store
        """
        body = {
  "photoUrls" : [ "photoUrls", "photoUrls" ],
  "name" : "doggie",
  "id" : 0,
  "category" : {
    "name" : "name",
    "id" : 6
  },
  "tags" : [ {
    "name" : "name",
    "id" : 1
  }, {
    "name" : "name",
    "id" : 1
  } ],
  "status" : "available"
}
        headers = { 
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/v2/pet',
            method='POST',
            headers=headers,
            data=json.dumps(body),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
