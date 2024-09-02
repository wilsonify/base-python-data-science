import logging
import os

import connexion
from flask_testing import TestCase
from json_ref_dict import RefDict, materialize

from openapi_server.encoder import JSONEncoder


class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('DEBUG')
        path_to_here = os.path.abspath(os.path.dirname(__file__))
        path_to_parent = os.path.abspath(os.path.join(path_to_here, os.pardir))
        path_to_openapi = os.path.abspath(f"{path_to_parent}/openapi/openapi.yaml")
        openapi_refdict = RefDict(path_to_openapi)
        openapi_dict = materialize(openapi_refdict)
        app = connexion.App(__name__)
        app.app.json_encoder = JSONEncoder
        app.add_api(
            specification=openapi_dict,
            arguments={"title": "Swagger Petstore"},
            pythonic_params=True
        )
        return app.app
