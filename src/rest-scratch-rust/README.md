# REST Scratch Rust

This project demonstrates a REST API implementation using Rust, generated from an OpenAPI specification.

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
  -g rust-server \
  -o /local/generated

# Or using Java JAR:
openapi-generator-cli generate \
  -i openapi/openapi.yaml \
  -g rust-server \
  -o generated
```

## Development

After generating the code:

1. Navigate to the generated directory
2. Build the project: `cargo build`
3. Implement the API trait in your handler
4. Run the server: `cargo run`

## Note

The `generated/` directory is not included in version control. You must generate it locally using the command above.
