# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from openapi_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_pet_find_by_status_get(self):
        """Test case for pet_find_by_status_get

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/pet/findByStatus',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pet_find_by_tags_get(self):
        """Test case for pet_find_by_tags_get

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/pet/findByTags',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pet_pet_id_delete(self):
        """Test case for pet_pet_id_delete

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/pet/{pet_id}',
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pet_pet_id_get(self):
        """Test case for pet_pet_id_get

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/pet/{pet_id}',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pet_pet_id_post(self):
        """Test case for pet_pet_id_post

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/pet/{pet_id}',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pet_pet_id_upload_image_post(self):
        """Test case for pet_pet_id_upload_image_post

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/pet/{pet_id}/uploadImage',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pet_post(self):
        """Test case for pet_post

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/pet',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_pet_put(self):
        """Test case for pet_put

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/pet',
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_store_inventory_get(self):
        """Test case for store_inventory_get

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/store/inventory',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_store_order_order_id_delete(self):
        """Test case for store_order_order_id_delete

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/store/order/{order_id}',
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_store_order_order_id_get(self):
        """Test case for store_order_order_id_get

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/store/order/{order_id}',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_store_order_post(self):
        """Test case for store_order_post

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/store/order',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_create_with_array_post(self):
        """Test case for user_create_with_array_post

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/user/createWithArray',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_create_with_list_post(self):
        """Test case for user_create_with_list_post

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/user/createWithList',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_login_get(self):
        """Test case for user_login_get

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/user/login',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_logout_get(self):
        """Test case for user_logout_get

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/user/logout',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_post(self):
        """Test case for user_post

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/user',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_username_delete(self):
        """Test case for user_username_delete

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/user/{username}',
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_username_get(self):
        """Test case for user_username_get

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/user/{username}',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_user_username_put(self):
        """Test case for user_username_put

        
        """
        headers = { 
        }
        response = self.client.open(
            '/v2/user/{username}',
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
