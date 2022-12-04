docker run --rm \
  -u $(id -u):$(id -g) \
  -v "${PWD}:/local" \
  openapitools/openapi-generator-cli:latest generate \
  -i /local/openapi/openapi.yaml \
  -g cpp-pistache-server \
  -o /local/generated