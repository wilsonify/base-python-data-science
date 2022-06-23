#!/usr/bin/env python3

import os
import connexion
from json_ref_dict import RefDict, materialize
from openapi_server import encoder

path_to_here = os.path.abspath(os.path.dirname(__file__))

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
    main()
