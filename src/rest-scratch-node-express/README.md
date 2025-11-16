# REST Scratch Node Express

This project demonstrates a REST API implementation using Node.js and Express, generated from an OpenAPI specification.

## OpenAPI Specification

The API is defined in `openapi/openapi.yaml`. This specification describes all the available endpoints, request/response schemas, and other API details.

## Generating Server Code

The server code can be generated from the OpenAPI spec using the OpenAPI Generator:

```bash
# Install OpenAPI Generator (if not already installed)
npm install @openapitools/openapi-generator-cli -g

# Generate the server code
openapi-generator-cli generate \
  -i openapi/openapi.yaml \
  -g nodejs-express-server \
  -o generated
```

## Development

After generating the code:

1. Navigate to the generated directory
2. Install dependencies: `npm install`
3. Implement the business logic in the service files
4. Run the server: `npm start`

## Note

The `generated/` directory is not included in version control. You must generate it locally using the command above.
