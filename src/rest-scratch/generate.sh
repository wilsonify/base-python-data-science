docker run --rm \
  -u $(id -u):$(id -g) \
  -v "${PWD}:/local" \
  openapitools/openapi-generator-cli:latest generate \
  -i /local/openapi_server/openapi/openapi.yaml \
  -g python-flask \
  -o /local/rest_scratch