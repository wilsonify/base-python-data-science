# REST Scratch Pistache

This project demonstrates a REST API implementation using C++ and Pistache, generated from an OpenAPI specification.

## OpenAPI Specification

The API is defined in `openapi/openapi.yaml`. This specification describes all the available endpoints, request/response schemas, and other API details.

## Generating Server Code

The server code can be generated from the OpenAPI spec using the OpenAPI Generator:

```bash
# Install OpenAPI Generator (if not already installed)
# Using Docker:
docker pull openapitools/openapi-generator-cli

# Generate the server code
docker run --rm -v "${PWD}:/local" openapitools/openapi-generator-cli generate \
  -i /local/openapi/openapi.yaml \
  -g cpp-pistache-server \
  -o /local/generated

# Or using Java JAR:
openapi-generator-cli generate \
  -i openapi/openapi.yaml \
  -g cpp-pistache-server \
  -o generated
```

## Development

After generating the code:

1. Navigate to the generated directory
2. Build using CMake: `mkdir build && cd build && cmake .. && make`
3. Implement the API handlers
4. Run the server

## Note

The `generated/` directory is not included in version control. You must generate it locally using the command above.
