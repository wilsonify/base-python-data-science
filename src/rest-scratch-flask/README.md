# Data Scratch Library REST API

A Flask-based REST API that exposes the functionality of the data-scratch-library, providing endpoints for various machine learning algorithms including K-Nearest Neighbors, Naive Bayes, Decision Trees, Clustering, and Neural Networks.

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the API server:
```bash
python run.py
```

The API will be available at `http://127.0.0.1:5000`

## API Endpoints

### Base Endpoints

- `GET /` - API information and available endpoints
- `GET /health` - Health check endpoint

### K-Nearest Neighbors (`/api/knn`)

#### Classify a Single Point
```http
POST /api/knn/classify
Content-Type: application/json

{
    "k": 3,
    "point": [1.0, 2.0],
    "training_data": [
        {"point": [1.1, 2.1], "label": "A"},
        {"point": [3.0, 4.0], "label": "B"}
    ]
}
```

#### Batch Classification
```http
POST /api/knn/batch_classify
Content-Type: application/json

{
    "k": 3,
    "points": [[1.0, 2.0], [3.0, 4.0]],
    "training_data": [
        {"point": [1.1, 2.1], "label": "A"},
        {"point": [3.0, 4.0], "label": "B"}
    ]
}
```

#### Algorithm Information
```http
GET /api/knn/info
```

### Naive Bayes (`/api/naive-bayes`)

#### Train Classifier
```http
POST /api/naive-bayes/train
Content-Type: application/json

{
    "training_data": [
        {"message": "buy viagra now", "is_spam": true},
        {"message": "hello friend", "is_spam": false}
    ],
    "smoothing": 0.5
}
```

#### Classify Message
```http
POST /api/naive-bayes/classify
Content-Type: application/json

{
    "message": "buy viagra now",
    "training_data": [
        {"message": "buy viagra now", "is_spam": true},
        {"message": "hello friend", "is_spam": false}
    ],
    "smoothing": 0.5
}
```

#### Batch Classification
```http
POST /api/naive-bayes/batch_classify
Content-Type: application/json

{
    "messages": ["buy viagra now", "hello friend"],
    "training_data": [
        {"message": "buy viagra now", "is_spam": true},
        {"message": "hello friend", "is_spam": false}
    ],
    "smoothing": 0.5
}
```

#### Algorithm Information
```http
GET /api/naive-bayes/info
```

### Decision Trees (`/api/decision-trees`)

#### Train Tree
```http
POST /api/decision-trees/train
Content-Type: application/json

{
    "training_data": [
        {"features": {"level": "Senior", "lang": "Java"}, "label": true},
        {"features": {"level": "Junior", "lang": "Python"}, "label": false}
    ],
    "split_candidates": ["level", "lang"]
}
```

#### Classify Instance
```http
POST /api/decision-trees/classify
Content-Type: application/json

{
    "instance": {"level": "Senior", "lang": "Java"},
    "training_data": [
        {"features": {"level": "Senior", "lang": "Java"}, "label": true},
        {"features": {"level": "Junior", "lang": "Python"}, "label": false}
    ],
    "split_candidates": ["level", "lang"]
}
```

#### Random Forest Classification
```http
POST /api/decision-trees/forest_classify
Content-Type: application/json

{
    "instance": {"level": "Senior", "lang": "Java"},
    "num_trees": 5,
    "training_data": [
        {"features": {"level": "Senior", "lang": "Java"}, "label": true},
        {"features": {"level": "Junior", "lang": "Python"}, "label": false}
    ]
}
```

#### Algorithm Information
```http
GET /api/decision-trees/info
```

### Clustering (`/api/clustering`)

#### K-Means Clustering
```http
POST /api/clustering/kmeans
Content-Type: application/json

{
    "data": [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],
    "k": 2,
    "max_iterations": 100,
    "initial_assignments": [0, 1, 0]
}
```

#### Analyze Clustering Quality
```http
POST /api/clustering/analyze
Content-Type: application/json

{
    "data": [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],
    "assignments": [0, 1, 0],
    "means": [[1.5, 2.5], [4.0, 5.0]]
}
```

#### Find Optimal K (Elbow Method)
```http
POST /api/clustering/optimal_k
Content-Type: application/json

{
    "data": [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]],
    "max_k": 5,
    "runs_per_k": 3
}
```

#### Algorithm Information
```http
GET /api/clustering/info
```

### Neural Networks (`/api/neural-networks`)

#### Sigmoid Activation
```http
POST /api/neural-networks/sigmoid
Content-Type: application/json

{
    "x": 1.0
}
```

#### Step Function
```http
POST /api/neural-networks/step
Content-Type: application/json

{
    "x": 1.0
}
```

#### Perceptron Prediction
```http
POST /api/neural-networks/perceptron
Content-Type: application/json

{
    "weights": [0.5, -0.5],
    "bias": -0.1,
    "inputs": [1.0, 0.5]
}
```

#### Neuron Activation
```http
POST /api/neural-networks/neuron
Content-Type: application/json

{
    "weights": [0.5, -0.5],
    "inputs": [1.0, 0.5]
}
```

#### Feed Forward Propagation
```http
POST /api/neural-networks/feed_forward
Content-Type: application/json

{
    "network": [
        [[0.5, -0.5], 0.0],  # Hidden layer: [weights, bias]
        [[1.0, 1.0], 0.0]    # Output layer: [weights, bias]
    ],
    "inputs": [1.0, 1.0]
}
```

#### Backpropagation
```http
POST /api/neural-networks/backpropagation
Content-Type: application/json

{
    "network": [
        [[0.5, -0.5], 0.0],
        [[1.0, 1.0], 0.0]
    ],
    "inputs": [1.0, 1.0],
    "target": [1.0]
}
```

#### Simple Training Demo
```http
POST /api/neural-networks/simple_train
Content-Type: application/json

{
    "training_data": [
        {"inputs": [0, 0], "target": [0]},
        {"inputs": [0, 1], "target": [1]},
        {"inputs": [1, 0], "target": [1]},
        {"inputs": [1, 1], "target": [0]}
    ],
    "hidden_neurons": 2,
    "learning_rate": 0.1,
    "epochs": 100
}
```

#### Algorithm Information
```http
GET /api/neural-networks/info
```

## Response Format

All endpoints return JSON responses with the following structure:

### Success Response
```json
{
    "data": { ... },
    "message": "Operation completed successfully"
}
```

### Error Response
```json
{
    "error": "Error description",
    "status_code": 400
}
```

## Usage Examples

### Python Example with requests
```python
import requests

# KNN Classification
knn_data = {
    "k": 3,
    "point": [1.0, 2.0],
    "training_data": [
        {"point": [1.1, 2.1], "label": "A"},
        {"point": [3.0, 4.0], "label": "B"}
    ]
}

response = requests.post('http://127.0.0.1:5000/api/knn/classify', json=knn_data)
print(response.json())

# Naive Bayes Spam Detection
spam_data = {
    "message": "buy viagra now cheap pills",
    "training_data": [
        {"message": "buy viagra now", "is_spam": True},
        {"message": "hello friend", "is_spam": False}
    ]
}

response = requests.post('http://127.0.0.1:5000/api/naive-bayes/classify', json=spam_data)
print(response.json())
```

### JavaScript Example with fetch
```javascript
// KNN Classification
const knnData = {
    k: 3,
    point: [1.0, 2.0],
    training_data: [
        {point: [1.1, 2.1], label: "A"},
        {point: [3.0, 4.0], label: "B"}
    ]
};

fetch('http://127.0.0.1:5000/api/knn/classify', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify(knnData)
})
.then(response => response.json())
.then(data => console.log(data));
```

## Configuration

Environment variables:
- `FLASK_HOST`: Server host (default: 127.0.0.1)
- `FLASK_PORT`: Server port (default: 5000)
- `FLASK_DEBUG`: Enable debug mode (default: False)

## Error Handling

The API includes comprehensive error handling for:
- Invalid JSON data
- Missing required fields
- Invalid data types
- Algorithm-specific errors
- Server errors (500)

All errors include descriptive messages to help with debugging.

## Testing

Run the test suite:
```bash
python -m pytest tests/
```

## License

This API is part of the data-scratch-library project.


# Data Scratch Library REST API - Summary

## Overview
A comprehensive Flask-based REST API that exposes the core machine learning functionality of the data-scratch-library. The API provides endpoints for classification, clustering, and neural network operations with full error handling and validation.

## Project Structure
```
rest-scratch-flask/
├── app/
│   ├── __init__.py              # Flask app factory
│   └── routes/
│       ├── knn.py              # K-Nearest Neighbors endpoints
│       ├── naive_bayes.py      # Naive Bayes classification
│       ├── decision_trees.py   # Decision tree algorithms
│       ├── clustering.py       # K-means clustering
│       └── neural_networks.py  # Neural network functions
├── tests/
│   ├── __init__.py
│   └── test_api.py             # Comprehensive API tests
├── requirements.txt            # Python dependencies
├── setup.py                    # Package setup
├── run.py                      # Application runner
├── demo.py                     # Demo script
├── README.md                   # Full documentation
└── API_SUMMARY.md             # This summary
```

## Available Endpoints

### Base Endpoints
- `GET /` - API overview and available endpoints
- `GET /health` - Health check

### K-Nearest Neighbors (`/api/knn`)
- `POST /api/knn/classify` - Classify a single point
- `POST /api/knn/batch_classify` - Classify multiple points
- `GET /api/knn/info` - Algorithm information

### Naive Bayes (`/api/naive-bayes`)
- `POST /api/naive-bayes/train` - Train spam classifier
- `POST /api/naive-bayes/classify` - Classify single message
- `POST /api/naive-bayes/batch_classify` - Classify multiple messages
- `GET /api/naive-bayes/info` - Algorithm information

### Decision Trees (`/api/decision-trees`)
- `POST /api/decision-trees/train` - Train decision tree
- `POST /api/decision-trees/classify` - Classify single instance
- `POST /api/decision-trees/batch_classify` - Classify multiple instances
- `POST /api/decision-trees/forest_classify` - Random forest classification
- `GET /api/decision-trees/info` - Algorithm information

### Clustering (`/api/clustering`)
- `POST /api/clustering/kmeans` - Perform K-means clustering
- `POST /api/clustering/analyze` - Analyze clustering quality
- `POST /api/clustering/optimal_k` - Find optimal k using elbow method
- `GET /api/clustering/info` - Algorithm information

### Neural Networks (`/api/neural-networks`)
- `POST /api/neural-networks/sigmoid` - Calculate sigmoid activation
- `POST /api/neural-networks/step` - Calculate step function
- `POST /api/neural-networks/perceptron` - Perceptron prediction
- `POST /api/neural-networks/neuron` - Neuron activation
- `POST /api/neural-networks/feed_forward` - Feed forward propagation
- `POST /api/neural-networks/backpropagation` - Calculate gradients
- `POST /api/neural-networks/simple_train` - Training demonstration
- `GET /api/neural-networks/info` - Algorithm information

## Key Features

### Data Validation
- Comprehensive input validation for all endpoints
- Type checking and format validation
- Clear error messages with status codes

### Error Handling
- 400: Bad Request (invalid data, missing fields)
- 500: Internal Server Error (algorithm failures)
- Structured error responses with descriptive messages

### CORS Support
- Cross-Origin Resource Sharing enabled
- Accessible from web applications

### Testing
- Comprehensive test suite with pytest
- Tests for all endpoints and error conditions
- Mock data for reliable testing

## Quick Start

1. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run the API:**
```bash
python run.py
```

3. **Test with Demo:**
```bash
python demo.py
```

4. **Run Tests:**
```bash
python -m pytest tests/
```

## Example Usage

### KNN Classification
```python
import requests

response = requests.post('http://127.0.0.1:5000/api/knn/classify', json={
    "k": 3,
    "point": [1.0, 2.0],
    "training_data": [
        {"point": [1.1, 2.1], "label": "A"},
        {"point": [3.0, 4.0], "label": "B"}
    ]
})

result = response.json()
print(f"Prediction: {result['prediction']}")
```

### Spam Detection
```python
response = requests.post('http://127.0.0.1:5000/api/naive-bayes/classify', json={
    "message": "buy viagra now cheap pills",
    "training_data": [
        {"message": "buy viagra now", "is_spam": True},
        {"message": "hello friend", "is_spam": False}
    ]
})

result = response.json()
print(f"Is spam: {result['is_spam']}")
print(f"Spam probability: {result['spam_probability']}")
```

### Clustering
```python
response = requests.post('http://127.0.0.1:5000/api/clustering/kmeans', json={
    "data": [[1.0, 2.0], [3.0, 4.0], [5.0, 6.0], [1.1, 2.1]],
    "k": 2
})

result = response.json()
print(f"Cluster assignments: {result['assignments']}")
print(f"Cluster means: {result['means']}")
```

## Configuration

Environment variables:
- `FLASK_HOST`: Server host (default: 127.0.0.1)
- `FLASK_PORT`: Server port (default: 5000)
- `FLASK_DEBUG`: Enable debug mode (default: False)

## Implementation Details

### Architecture
- **Flask Blueprint Pattern**: Modular route organization
- **Factory Pattern**: Configurable app creation
- **Error Handling**: Centralized error responses
- **Data Validation**: Input validation for all endpoints

### Security
- Input sanitization and validation
- Error message sanitization
- CORS configuration
- No persistent storage (stateless API)

### Performance
- Stateless design for scalability
- Efficient data processing
- Minimal memory footprint
- Fast response times

## Dependencies

### Core Dependencies
- **Flask 2.3.3**: Web framework
- **Flask-CORS 4.0.0**: Cross-origin support
- **marshmallow 3.20.1**: Data serialization

### Development Dependencies
- **pytest 7.4.2**: Testing framework
- **pytest-flask 1.2.0**: Flask testing utilities

## Future Enhancements

### Potential Improvements
1. **Authentication**: API key or JWT authentication
2. **Rate Limiting**: Prevent abuse
3. **Caching**: Improve response times
4. **Async Support**: Handle concurrent requests
5. **Database Integration**: Persistent model storage
6. **Model Persistence**: Save and load trained models
7. **Batch Processing**: Handle large datasets efficiently
8. **WebSocket Support**: Real-time predictions

### Additional Algorithms
1. **Linear Regression**: Regression endpoints
2. **PCA**: Dimensionality reduction
3. **SVM**: Support vector machines
4. **Random Forest**: Enhanced tree methods
5. **Gradient Boosting**: Advanced ensemble methods

## Contributing

### Development Setup
1. Clone the repository
2. Install development dependencies: `pip install -r requirements.txt`
3. Run tests: `python -m pytest tests/`
4. Make changes and test thoroughly

### Adding New Endpoints
1. Create new route file in `app/routes/`
2. Register blueprint in `app/__init__.py`
3. Add comprehensive tests in `tests/test_api.py`
4. Update documentation

## License

This REST API is part of the data-scratch-library project and follows the same licensing terms.
