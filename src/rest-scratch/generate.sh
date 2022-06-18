docker run --rm \
  -v "${PWD}:/local" \
  openapitools/openapi-generator-cli:v4.1.2 generate \
  -i /local/openapi_server/openapi/openapi.yaml \
  -g python-flask \
  -o /local/python

sudo chown -R $USER .
