#!/usr/bin/env python3
import logging
import os
from logging.config import dictConfig

import connexion
from json_ref_dict import RefDict, materialize

from openapi_server import controllers
from openapi_server import encoder
from openapi_server import models
from openapi_server.controllers import (
    math_controller,
    pet_controller,
    security_controller_,
    store_controller,
    user_controller
)

# hidden imports
assert dir(controllers)
assert dir(math_controller)
assert dir(pet_controller)
assert dir(security_controller_)
assert dir(store_controller)
assert dir(user_controller)
assert dir(models)

path_to_here = os.path.abspath(os.path.dirname(__file__))

logging_config_dict = dict(
    version=1,
    formatters={
        "simple": {
            "format": """%(asctime)s | %(filename)s | %(lineno)d | %(levelname)s | %(message)s"""
        }
    },
    handlers={"console": {"class": "logging.StreamHandler", "formatter": "simple"}},
    root={"handlers": ["console"], "level": logging.DEBUG},
)


def main():
    openapi_refdict = RefDict(f"{path_to_here}/openapi/openapi.yaml")
    openapi_dict = materialize(openapi_refdict)
    app = connexion.App(__name__)
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api(
        specification=openapi_dict,
        arguments={"title": "Swagger Petstore"},
        pythonic_params=True
    )

    app.run(port=8080)


if __name__ == "__main__":
    dictConfig(logging_config_dict)
    main()
