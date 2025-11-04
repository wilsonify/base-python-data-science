# OpenAPI Documentation Guide

## Overview

The Data Scratch Library REST API is now fully documented using OpenAPI 3.0 specification. This provides standardized, machine-readable API documentation that can be used with various tools and clients.

## Documentation Features

### 1. OpenAPI 3.0 Specification
- **File**: `openapi.yaml`
- **Standard**: OpenAPI 3.0.3
- **Format**: YAML
- **Location**: `/openapi.yaml` endpoint

### 2. Interactive Swagger UI
- **URL**: `/docs` (when flask-swagger-ui is installed)
- **Features**: 
  - Interactive API exploration
  - Try-it-out functionality
  - Request/response examples
  - Schema validation

### 3. Comprehensive Coverage
- **5 ML Algorithm Categories**: KNN, Naive Bayes, Decision Trees, Clustering, Neural Networks
- **25+ Endpoints**: Classification, training, analysis, and information endpoints
- **Complete Schemas**: Request/response models with validation
- **Error Handling**: Standardized error responses

## Accessing Documentation

### 1. OpenAPI Specification
```bash
# Get the raw OpenAPI spec
curl http://127.0.0.1:5000/openapi.yaml

# Or view in browser
http://127.0.0.1:5000/openapi.yaml
```

### 2. Interactive Swagger UI
```bash
# Install optional dependency
pip install flask-swagger-ui

# Start the server
python run.py

# Visit interactive documentation
http://127.0.0.1:5000/docs
```

### 3. API Information Endpoint
```bash
curl http://127.0.0.1:5000/
```

## Documentation Structure

### API Categories
1. **Base Endpoints**
   - Health check (`/health`)
   - API information (`/`)
   - OpenAPI spec (`/openapi.yaml`)

2. **K-Nearest Neighbors** (`/api/knn`)
   - Single point classification
   - Batch classification
   - Algorithm information

3. **Naive Bayes** (`/api/naive-bayes`)
   - Spam classifier training
   - Message classification
   - Batch classification
   - Algorithm information

4. **Decision Trees** (`/api/decision-trees`)
   - Tree training
   - Instance classification
   - Batch classification
   - Random forest classification
   - Algorithm information

5. **Clustering** (`/api/clustering`)
   - K-means clustering
   - Quality analysis
   - Optimal k detection
   - Algorithm information

6. **Neural Networks** (`/api/neural-networks`)
   - Activation functions
   - Perceptron and neuron operations
   - Feed-forward propagation
   - Backpropagation
   - Training demonstration
   - Algorithm information

### Schema Documentation
Each endpoint includes:
- **Request schemas**: Complete input validation
- **Response schemas**: Expected output formats
- **Examples**: Sample requests and responses
- **Error schemas**: Standardized error handling
- **Parameters**: Detailed parameter descriptions

## Using the Documentation

### 1. With Swagger UI
1. Navigate to `/docs`
2. Browse endpoints by category
3. Expand endpoints to see details
4. Use "Try it out" to test APIs
5. View generated requests/responses

### 2. With OpenAPI Tools
```bash
# Generate client code
openapi-generator-cli generate -i openapi.yaml -g python -o ./client

# Validate specification
swagger-codegen validate -i openapi.yaml

# Convert to other formats
swagger-codegen generate -i openapi.yaml -l html2 -o ./docs-html
```

### 3. Programmatic Access
```python
import requests
import yaml

# Fetch OpenAPI spec
response = requests.get('http://127.0.0.1:5000/openapi.yaml')
spec = yaml.safe_load(response.text)

# List all endpoints
for path, methods in spec['paths'].items():
    for method, details in methods.items():
        print(f"{method.upper()} {path}: {details['summary']}")
```

## Documentation Examples

### Example: KNN Classification
```yaml
# From openapi.yaml
/api/knn/classify:
  post:
    summary: Classify a point using KNN
    requestBody:
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/KnnClassifyRequest'
          example:
            k: 3
            point: [1.0, 2.0]
            training_data:
              - point: [1.1, 2.1]
                label: "A"
              - point: [3.0, 4.0]
                label: "B"
    responses:
      '200':
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/KnnClassifyResponse'
```

### Example: Response Schema
```yaml
KnnClassifyResponse:
  type: object
  properties:
    prediction:
      description: Predicted label
      example: "A"
    k:
      type: integer
      example: 3
    point:
      type: array
      items:
        type: number
      example: [1.0, 2.0]
    training_points_count:
      type: integer
      example: 10
```

## Integration with Tools

### 1. API Testing Tools
- **Postman**: Import OpenAPI spec for automated requests
- **Insomnia**: Use OpenAPI plugin for endpoint discovery
- **Swagger Editor**: Online validation and editing

### 2. Code Generation
```bash
# Generate Python client
openapi-generator-cli generate -i openapi.yaml -g python -o ./python-client

# Generate JavaScript client
openapi-generator-cli generate -i openapi.yaml -g javascript -o ./js-client

# Generate TypeScript types
openapi-generator-cli generate -i openapi.yaml -g typescript-axios -o ./ts-client
```

### 3. Documentation Generation
```bash
# Generate HTML documentation
swagger-codegen generate -i openapi.yaml -l html2 -o ./html-docs

# Generate Markdown documentation
swagger-codegen generate -i openapi.yaml -l markdown -o ./markdown-docs
```

## Best Practices

### 1. Schema Design
- Use descriptive property names
- Include meaningful examples
- Define proper data types and constraints
- Document all required fields

### 2. Endpoint Documentation
- Clear, concise summaries
- Detailed descriptions with usage examples
- Complete parameter documentation
- Error response documentation

### 3. Version Management
- Include version in API paths
- Document breaking changes
- Maintain backward compatibility
- Use semantic versioning

### 4. Validation
- Use schema validation for all requests
- Return appropriate HTTP status codes
- Provide meaningful error messages
- Include error response schemas

## Updating Documentation

### 1. Adding New Endpoints
1. Update route implementation
2. Add endpoint to `openapi.yaml`
3. Define request/response schemas
4. Include examples and descriptions
5. Test with Swagger UI

### 2. Modifying Existing Endpoints
1. Update implementation
2. Update OpenAPI schemas
3. Review breaking changes
4. Update version if needed
5. Regenerate client documentation

### 3. Schema Updates
1. Modify component schemas
2. Update all references
3. Validate specification
4. Test with examples
5. Update documentation

## Quality Assurance

### 1. Validation
```bash
# Validate OpenAPI spec
swagger-codegen validate -i openapi.yaml

# Check for common issues
speccy lint openapi.yaml
```

### 2. Testing
```bash
# Test all documented endpoints
python -m pytest tests/test_api.py

# Test OpenAPI compliance
dredd openapi.yaml http://127.0.0.1:5000
```

### 3. Coverage
- All endpoints documented
- All schemas defined
- All examples tested
- Error cases covered

## Troubleshooting

### Common Issues
1. **Missing Schemas**: Ensure all referenced schemas are defined
2. **Invalid YAML**: Check YAML syntax and indentation
3. **Missing Examples**: Add examples for all request/response schemas
4. **Validation Errors**: Use OpenAPI validator to identify issues

### Debug Tips
1. Use Swagger UI to test endpoints interactively
2. Check browser console for JavaScript errors
3. Validate YAML syntax with online tools
4. Review server logs for implementation errors

## Conclusion

The OpenAPI documentation provides a comprehensive, standardized description of the Data Scratch Library REST API. It enables:
- **Interactive exploration** with Swagger UI
- **Code generation** for multiple languages
- **Automated testing** with OpenAPI tools
- **Easy integration** with third-party services
- **Consistent documentation** across all endpoints

For the best experience, install the optional dependencies and use the interactive Swagger UI at `/docs`.
