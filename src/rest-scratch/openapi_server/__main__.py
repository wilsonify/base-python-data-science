#!/usr/bin/env python3

import os
import connexion
from json_ref_dict import RefDict, materialize
from openapi_server import encoder

path_to_here = os.path.abspath(os.path.dirname(__file__))

def main():
    openapi_dict = RefDict(f"{path_to_here}/openapi/openapi.yaml")
    app = connexion.App(__name__, specification_dir="./openapi/")
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api(
        openapi_dict,
        arguments={"title": "Swagger Petstore"}, 
        pythonic_params=True
    )

    app.run(port=8080)


if __name__ == "__main__":
    main()
