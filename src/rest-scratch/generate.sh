docker run --rm \
  -u $(id -u):$(id -g) \
  -v "${PWD}:/local" \
  openapitools/openapi-generator-cli:latest generate \
  -i /local/openapi/openapi.yaml \
  -g python-flask \
  -o /local/python