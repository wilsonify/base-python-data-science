# Data Scratch MQTT

A simplified MQTT-based data science strategy service that dynamically loads and executes mathematical and statistical functions.

## Overview

This system provides an MQTT consumer that can execute various data science strategies (linear algebra, statistics, probability, machine learning, etc.) on demand. It uses a dynamic strategy loading system that gracefully handles missing dependencies.

## Features

- **91+ Dynamic Strategies**: Automatically loads strategies from the data science library
- **Graceful Degradation**: Works even when optional dependencies are missing
- **MQTT-based**: Uses MQTT for communication and request/response pattern
- **Error Handling**: Comprehensive error handling and reporting
- **Zero Configuration**: Uses sensible defaults with environment variable overrides

## Installation

### Core Dependencies
```bash
pip install python-dateutil paho-mqtt
```

### Optional Dependencies (for full functionality)
```bash
pip install dsl  # Data Science Library
```

### Development Dependencies
```bash
pip install pyinstaller pytest pytest-cov
```

## Usage

### Start the MQTT Consumer
```bash
python -m data_scratch_mqtt
```

### Send Requests via MQTT
Publish a JSON message to the configured topic (default: `dsfs`):

```json
{
  "strategy": "mean",
  "xs": [1, 2, 3, 4, 5]
}
```

### Available Strategies

#### Core Strategies (always available)
- `echo` - Echoes the input payload

#### Dynamic Strategies (requires `dsl` library)
- **Linear Algebra**: `vector_add`, `dot`, `magnitude`, `matrix_add`, etc.
- **Statistics**: `mean`, `median`, `variance`, `correlation`, etc.
- **Probability**: `normal_cdf`, `binomial`, `bernoulli_trial`, etc.
- **Machine Learning**: `accuracy`, `precision`, `recall`, `split_data`, etc.
- **Gradient Descent**: `minimize_batch`, `estimate_gradient`, etc.

## Configuration

Environment variables:
- `MQMQ_HOST` - MQTT broker host (default: `localhost`)
- `mqtt_PORT` - MQTT broker port (default: `1883`)
- `mqtt_KEEPALIVE` - MQTT keepalive interval (default: `60`)
- `mqtt_USER` - MQTT username (default: `thom`)
- `mqtt_PASS` - MQTT password (default: `examplepassword`)
- `mqtt_TOPIC` - MQTT topic to subscribe to (default: `dsfs`)

## Response Format

Responses are published to `{topic}_reply` with the following format:

### Success Response
```json
{
  "result": 3.0
}
```

### Error Response
```json
{
  "error": "No module named 'dsl'",
  "function": "vector_add",
  "module": "dsl.c04_linear_algebra.e0401_vectors"
}
```

## Testing

Run the test suite:
```bash
pytest -v
```

The tests use mocks and don't require a running MQTT broker.

## Architecture

The system uses a dynamic strategy pattern:

1. **Strategy Discovery**: Automatically discovers available functions
2. **Dynamic Wrapping**: Wraps library functions as MQTT strategies
3. **Graceful Handling**: Handles missing dependencies without crashing
4. **Parameter Extraction**: Automatically extracts parameters from JSON requests

## Development

### Adding New Strategies

Simply add the function to the module mapping in `strategies_library/dynamic_strategy.py`:

```python
'my_new_function': 'dsl.module.path',
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=data_scratch_mqtt --cov-report=term-missing
```

## Simplification History

This project was simplified from:
- **8 individual strategy files** → **1 dynamic strategy system**
- **55+ hardcoded imports** → **6 core imports**
- **Manual strategy registration** → **Automatic discovery**

Resulting in a 90%+ reduction in code complexity while maintaining full functionality.
