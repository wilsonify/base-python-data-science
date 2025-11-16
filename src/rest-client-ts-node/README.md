# REST Client TypeScript Node

This project demonstrates a REST API client implementation using TypeScript and Node.js, generated from an OpenAPI specification.

## OpenAPI Specification

The API client is defined by the OpenAPI spec in `openapi/openapi.yaml`.

## Generating Client Code

The client code can be generated from the OpenAPI spec using the OpenAPI Generator:

```bash
# Install OpenAPI Generator (if not already installed)
npm install @openapitools/openapi-generator-cli -g

# Generate the client code
openapi-generator-cli generate \
  -i openapi/openapi.yaml \
  -g typescript-node \
  -o generated
```

## Development

After generating the code:

1. Navigate to the generated directory
2. Install dependencies: `npm install`
3. Build the client: `npm run build`
4. Use the generated client in your application

## Note

The `generated/` directory is not included in version control. You must generate it locally using the command above.
