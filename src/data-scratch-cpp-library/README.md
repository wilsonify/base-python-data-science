# C++ Data Science Library

A comprehensive C++ implementation of machine learning algorithms from scratch. This library provides the core functionality of the data-scratch-library ported to modern C++ with full type safety and performance optimization.

## Features

### 🤖 Machine Learning Algorithms
- **K-Nearest Neighbors (KNN)**: Classification with distance-based voting, weighted voting, and cross-validation
- **Naive Bayes**: Spam detection and text classification (coming soon)
- **Decision Trees**: ID3 algorithm with random forest support (coming soon)
- **Clustering**: K-means with quality analysis and optimal k detection (coming soon)
- **Neural Networks**: Feed-forward networks with backpropagation (coming soon)

### 📊 Mathematical Foundations
- **Linear Algebra**: Vector operations, matrices, dot products, distance calculations
- **Statistics**: Mean, median, standard deviation, correlation, histograms
- **Probability**: Probability distributions, error function, normal distribution calculations
- **Machine Learning Utilities**: Data splitting, performance metrics (accuracy, precision, recall, F1-score)

### 🔧 Key Features
- **Type Safety**: Full C++ template support with strong typing
- **Performance**: Optimized C++ implementations with modern C++ features
- **Modular Design**: Clean separation of concerns with well-defined interfaces
- **Cross-Platform**: Standard C++11 compatible code

## Building the Library

### Prerequisites
- C++11 compatible compiler (GCC 4.8+, Clang 3.4+, MSVC 2015+)
- CMake 3.14 or higher
- Make (or your preferred build system)

### Build Instructions

```bash
# Clone the repository
git clone <repository-url>
cd data-scratch-cpp-library

# Create build directory
mkdir build
cd build

# Configure with CMake
cmake ..

# Build the library
make

# The shared library will be created as libdata-scratch-cpp-library.so
```

## Usage Examples

### Linear Algebra

```cpp
#include "dscpp.h"

int main() {
    // Vector operations
    std::vector<double> v1 = {1.0, 2.0, 3.0};
    std::vector<double> v2 = {4.0, 5.0, 6.0};
    
    auto sum = vector_add(v1, v2);        // {5.0, 7.0, 9.0}
    auto diff = vector_subtract(v1, v2);  // {-3.0, -3.0, -3.0}
    auto mag = magnitude(v1);             // sqrt(14)
    
    // Matrix operations
    std::vector<std::vector<double>> matrix = {
        {1.0, 2.0},
        {3.0, 4.0}
    };
    
    auto shape_info = shape(matrix);      // {2, 2}
    auto row = get_row(matrix, 0);        // {1.0, 2.0}
    auto col = get_column(matrix, 1);     // {2.0, 4.0}
    
    return 0;
}
```

### Statistics

```cpp
#include "dscpp.h"

int main() {
    std::vector<double> data = {1.0, 2.0, 3.0, 4.0, 5.0};
    
    double avg = mean(data);              // 3.0
    double med = median(data);            // 3.0
    double std_dev = standard_deviation(data);  // ~1.58
    double var = variance(data);          // ~2.5
    
    // Histogram
    auto histogram = make_histogram(data, 1.0);
    
    // Correlation matrix
    std::vector<std::vector<double>> matrix = {
        {1.0, 2.0, 3.0},
        {4.0, 5.0, 6.0},
        {7.0, 8.0, 9.0}
    };
    auto corr_matrix = correlation_matrix(matrix);
    
    return 0;
}
```

### K-Nearest Neighbors

```cpp
#include "dscpp.h"

int main() {
    // Create labeled data points
    std::vector<LabeledPoint<std::string>> training_data = {
        {{1.0, 2.0}, "ClassA"},
        {{2.0, 3.0}, "ClassA"},
        {{3.0, 4.0}, "ClassB"},
        {{4.0, 5.0}, "ClassB"}
    };
    
    // New point to classify
    std::vector<double> new_point = {2.5, 3.5};
    
    // Classify using k=3
    std::string prediction = knnClassify(3, training_data, new_point);
    
    // Get detailed information with distances
    auto result = knnClassifyWithDistance(3, training_data, new_point);
    std::cout << "Prediction: " << result.prediction << std::endl;
    std::cout << "Distances: ";
    for (double dist : result.distances) {
        std::cout << dist << " ";
    }
    std::cout << std::endl;
    
    // Weighted KNN (closer neighbors have more influence)
    std::string weighted_prediction = weightedKnnClassify(3, training_data, new_point);
    
    // Cross-validation to find optimal k
    auto optimal_k = findOptimalK(training_data, 10, 5);
    std::cout << "Optimal k: " << optimal_k.optimalK << std::endl;
    
    return 0;
}
```

### Probability

```cpp
#include "dscpp.h"

int main() {
    // Normal distribution
    double x = 1.96;
    double pdf = normal_pdf(x, 0.0, 1.0);     // Standard normal PDF
    double cdf = normal_cdf(x, 0.0, 1.0);     // Standard normal CDF
    double inv_cdf = inverse_normal_cdf(0.975, 0.0, 1.0);  // Inverse CDF
    
    // Uniform distribution
    double uniform_pdf_val = uniform_pdf(0.5, 0.0, 1.0);
    double uniform_cdf_val = uniform_cdf(0.5, 0.0, 1.0);
    
    // Random sampling
    double random_normal_sample = random_normal();
    std::string random_kid_sample = random_kid();
    
    // Binomial distribution
    int binomial_sample = binomial(0.5, 10);  // 10 trials, p=0.5
    
    return 0;
}
```

### Machine Learning Utilities

```cpp
#include "dscpp.h"

int main() {
    // Data splitting
    std::vector<std::vector<double>> features = {
        {1.0, 2.0},
        {3.0, 4.0},
        {5.0, 6.0},
        {7.0, 8.0}
    };
    std::vector<double> labels = {0.0, 1.0, 0.0, 1.0};
    
    // Split data for training/testing
    auto split_result = train_test_split(features, labels, 0.25);
    
    // Performance metrics
    double tp = 50, fp = 10, fn = 5, tn = 35;
    double acc = accuracy(tp, fp, fn, tn);        // 0.85
    double prec = precision(tp, fp, fn, tn);      // 0.833
    double rec = recall(tp, fp, fn, tn);          // 0.909
    double f1 = f1_score(tp, fp, fn, tn);         // ~0.869
    
    return 0;
}
```

## Library Structure

```
dscpp/
├── c04_linear_algebra/     # Vector and matrix operations
├── c05_statistics/         # Statistical functions
├── c06_probability/        # Probability distributions
├── c11_machine_learning/   # ML utilities and metrics
├── c12_k_nearest_neighbors/ # KNN algorithm implementation
├── c13_naive_bayes/       # Naive Bayes classifier (coming soon)
├── c17_decision_trees/    # Decision tree algorithms (coming soon)
├── c18_neural_networks/   # Neural network implementation (coming soon)
└── c20_clustering/        # Clustering algorithms (coming soon)
```

## API Reference

### Linear Algebra
- `vector_add(v, w)` - Add two vectors
- `vector_subtract(v, w)` - Subtract two vectors
- `scalar_multiply(c, v)` - Multiply vector by scalar
- `dot(v, w)` - Dot product
- `magnitude(v)` - Vector magnitude
- `distance(v, w)` - Euclidean distance
- `shape(matrix)` - Get matrix dimensions
- `get_row(matrix, i)` - Get matrix row
- `get_column(matrix, j)` - Get matrix column

### Statistics
- `mean(data)` - Arithmetic mean
- `median(data)` - Median value
- `variance(data)` - Sample variance
- `standard_deviation(data)` - Standard deviation
- `correlation(x, y)` - Pearson correlation
- `make_histogram(data, bucket_size)` - Create histogram

### KNN
- `knnClassify(k, data, point)` - Basic KNN classification
- `knnClassifyWithDistance(k, data, point)` - Classification with distance info
- `weightedKnnClassify(k, data, point)` - Distance-weighted classification
- `knnCrossValidate(k, data, folds)` - Cross-validation
- `findOptimalK(data, max_k, folds)` - Find optimal k value

### Probability
- `normal_pdf(x, mu, sigma)` - Normal distribution PDF
- `normal_cdf(x, mu, sigma)` - Normal distribution CDF
- `inverse_normal_cdf(p, mu, sigma)` - Inverse normal CDF
- `random_normal()` - Sample from standard normal
- `binomial(p, n)` - Binomial distribution sample

## Performance

The library is designed for performance:
- **Zero-copy operations** where possible
- **Template-based design** for compile-time optimization
- **Efficient memory management** with RAII
- **SIMD-friendly** data structures

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Roadmap

- [ ] Complete Naive Bayes implementation
- [ ] Decision Trees and Random Forest
- [ ] K-Means clustering
- [ ] Neural Networks with backpropagation
- [ ] Comprehensive test suite
- [ ] Performance benchmarks
- [ ] Documentation improvements
- [ ] Python bindings for interoperability
