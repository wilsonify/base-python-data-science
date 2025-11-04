# TypeScript Data Science Library

A comprehensive TypeScript implementation of machine learning algorithms from scratch. This library provides the core functionality of the data-scratch-library ported to vanilla TypeScript with full type safety and modern JavaScript features.

## Features

### 🤖 Machine Learning Algorithms
- **K-Nearest Neighbors (KNN)**: Classification with distance-based voting
- **Naive Bayes**: Spam detection and text classification
- **Decision Trees**: ID3 algorithm with random forest support
- **Clustering**: K-means with quality analysis and optimal k detection
- **Neural Networks**: Feed-forward networks with backpropagation

### 📊 Mathematical Foundations
- **Linear Algebra**: Vector operations, matrices, dot products
- **Statistics**: Mean, median, standard deviation, correlation
- **Probability**: Probability distributions and calculations
- **Gradient Descent**: Optimization algorithms

### 🔧 Utilities
- **Type Safety**: Full TypeScript support with comprehensive types
- **Cross-Validation**: Model evaluation and validation
- **Data Splitting**: Train/test split utilities
- **Performance Metrics**: Accuracy, precision, recall, F1-score

## Installation

```bash
npm install ts-data-scratch
```

## Quick Start

```typescript
import { 
    knnClassify, 
    NaiveBayesClassifier, 
    kMeans, 
    trainSimpleNetwork,
    classify,
    predict 
} from 'ts-data-scratch';

// K-Nearest Neighbors
const labeledPoints = [
    { point: [1, 2], label: 'A' },
    { point: [3, 4], label: 'B' },
    { point: [1.1, 2.1], label: 'A' }
];

const prediction = knnClassify(3, labeledPoints, [1.5, 2.5]);
console.log(prediction); // 'A'

// Naive Bayes for spam detection
const classifier = new NaiveBayesClassifier();
classifier.train([
    { message: "buy viagra now", isSpam: true },
    { message: "hello friend", isSpam: false }
]);

const result = classifier.classify("cheap pills online");
console.log(result.isSpam); // true
console.log(result.spamProbability); // 0.95

// K-means clustering
const points = [[1, 2], [3, 4], [5, 6], [1.1, 2.1]];
const clusters = kMeans(points, 2);
console.log(clusters.assignments); // [0, 1, 1, 0]

// Neural Networks
const trainingData = [
    { inputs: [0, 0], target: [0] },
    { inputs: [0, 1], target: [1] },
    { inputs: [1, 0], target: [1] },
    { inputs: [1, 1], target: [0] }
];

const { network } = trainSimpleNetwork(trainingData, 2, 0.1, 1000);
const output = predict(network, [1, 0]);
console.log(output); // [0.98] (approximately 1)
```

## API Reference

### K-Nearest Neighbors

```typescript
// Basic classification
knnClassify(k, labeledPoints, newPoint): T

// With distance information
knnClassifyWithDistance(k, labeledPoints, newPoint): {
    prediction: T;
    distances: number[];
    neighbors: LabeledPoint<T>[];
}

// Weighted KNN
weightedKnnClassify(k, labeledPoints, newPoint): T

// Cross-validation
knnCrossValidate(k, labeledPoints, folds?): number

// Find optimal k
findOptimalK(labeledPoints, maxK?, folds?): {
    optimalK: number;
    accuracies: number[];
}
```

### Naive Bayes

```typescript
// Classifier class
class NaiveBayesClassifier {
    constructor(smoothing?: number)
    train(messages: LabeledMessage[]): void
    classify(message: string): ClassificationResult
    getTrainingInfo(): TrainingInfo
    getWordProbabilities(): WordProbabilities
}

// Convenience functions
trainNaiveBayesClassifier(messages, smoothing?): NaiveBayesClassifier
classifyMessage(message, trainingMessages, smoothing?): ClassificationResult
naiveBayesCrossValidate(messages, folds?, smoothing?): number
```

### Decision Trees

```typescript
// Build and classify
buildDecisionTree(data, attributes, maxDepth?): TreeNode
classify(tree, dataPoint): boolean
printTree(tree, indent?): void
treeAccuracy(tree, testData): number

// Random Forest
class RandomForest {
    constructor(numTrees?, sampleSize?)
    train(data, attributes): void
    classify(dataPoint): boolean
    getInfo(): ForestInfo
}
```

### Clustering

```typescript
// K-means clustering
kMeans(points, k, maxIterations?, initialAssignments?): KMeansResult
kMeansMultipleRuns(points, k, numRuns?, maxIterations?): KMeansResult

// Analysis utilities
findOptimalK(points, maxK?, runsPerK?): OptimalKResult
silhouetteScore(points, assignments, means): number
analyzeClustering(result): ClusterAnalysis
```

### Neural Networks

```typescript
// Activation functions
sigmoid(x): number
stepFunction(x): number
tanh(x): number
relu(x): number

// Network operations
perceptron(weights, bias, inputs): number
neuron(weights, inputs): number
feedForward(network, inputs): FeedForwardResult
backpropagation(network, inputs, target): BackpropResult

// Training
trainSimpleNetwork(trainingData, hiddenNeurons?, learningRate?, epochs?): TrainingResult
createNetwork(layerSizes): NeuralNetwork
predict(network, inputs): number[]
```

## Examples

### Complete KNN Example

```typescript
import { knnClassify, findOptimalK, knnCrossValidate } from 'ts-data-scratch';

// Training data
const cities = [
    { point: [-86.75, 33.57], label: "Python" },
    { point: [-88.25, 30.68], label: "Python" },
    { point: [-112.02, 33.43], label: "Java" },
    { point: [-110.93, 32.12], label: "Java" }
];

// Find optimal k
const { optimalK } = findOptimalK(cities, 10);
console.log(`Optimal k: ${optimalK}`);

// Classify new city
const newCity = [-87.68, 41.83]; // Chicago
const prediction = knnClassify(optimalK, cities, newCity);
console.log(`Chicago prefers: ${prediction}`);

// Cross-validation
const accuracy = knnCrossValidate(optimalK, cities);
console.log(`Cross-validation accuracy: ${(accuracy * 100).toFixed(2)}%`);
```

### Spam Detection with Naive Bayes

```typescript
import { NaiveBayesClassifier } from 'ts-data-scratch';

const messages = [
    { message: "buy viagra now cheap pills", isSpam: true },
    { message: "hello friend how are you", isSpam: false },
    { message: "limited time offer free money", isSpam: true },
    { message: "meeting tomorrow at 3pm", isSpam: false }
];

const classifier = new NaiveBayesClassifier(0.5);
classifier.train(messages);

const testMessages = [
    "buy cheap pills online",
    "hello my dear friend",
    "free money click here",
    "project deadline next week"
];

testMessages.forEach(msg => {
    const result = classifier.classify(msg);
    console.log(`"${msg}" -> ${result.isSpam ? 'SPAM' : 'HAM'}`);
    console.log(`  Spam prob: ${result.spamProbability.toFixed(4)}`);
    console.log(`  Ham prob: ${result.hamProbability.toFixed(4)}`);
});
```

### Clustering Analysis

```typescript
import { kMeans, findOptimalK, analyzeClustering } from 'ts-data-scratch';

const points = [
    [1, 2], [1, 4], [1, 0],  // Cluster 1
    [10, 2], [10, 4], [10, 0], // Cluster 2
    [5, 8], [5, 10], [5, 6]    // Cluster 3
];

// Find optimal number of clusters
const { optimalK, errors } = findOptimalK(points, 6);
console.log(`Optimal k: ${optimalK}`);
console.log(`Errors: ${errors.map(e => e.toFixed(2)).join(', ')}`);

// Perform clustering
const result = kMeans(points, optimalK);

// Analyze results
const analysis = analyzeClustering(result);
console.log(`Cluster sizes: ${analysis.clusterSizes.join(', ')}`);
console.log(`Silhouette score: ${analysis.silhouetteScore.toFixed(4)}`);

result.clusters.forEach((cluster, i) => {
    console.log(`Cluster ${i}: ${cluster.points.length} points`);
    console.log(`  Centroid: [${cluster.centroid.map(v => v.toFixed(2)).join(', ')}]`);
});
```

### Neural Network for XOR

```typescript
import { trainSimpleNetwork, predict, sigmoid } from 'ts-data-scratch';

// XOR training data
const trainingData = [
    { inputs: [0, 0], target: [0] },
    { inputs: [0, 1], target: [1] },
    { inputs: [1, 0], target: [1] },
    { inputs: [1, 1], target: [0] }
];

// Train network
const { network, finalError } = trainSimpleNetwork(trainingData, 2, 0.1, 5000);
console.log(`Final error: ${finalError.toFixed(6)}`);

// Test predictions
const testCases = [
    [0, 0], [0, 1], [1, 0], [1, 1]
];

testCases.forEach(inputs => {
    const output = predict(network, inputs);
    const prediction = output[0] > 0.5 ? 1 : 0;
    console.log(`XOR(${inputs.join(', ')}) = ${prediction} (${output[0].toFixed(4)})`);
});
```

## Development

### Building

```bash
npm run build
```

### Testing

```bash
npm test
```

### Development Mode

```bash
npm run dev
```

## Type Safety

This library is written entirely in TypeScript with comprehensive type definitions:

```typescript
// All functions have proper type annotations
knnClassify<T>(k: number, labeledPoints: LabeledPoint<T>[], newPoint: number[]): T

// Classes are fully typed
class NaiveBayesClassifier {
    train(messages: LabeledMessage[]): void
    classify(message: string): ClassificationResult
}

// Complex return types are properly defined
type KMeansResult = {
    clusters: Cluster[];
    assignments: number[];
    means: Point[];
    totalSquaredError: number;
    iterations: number;
};
```

## Performance

- **No external dependencies** for core algorithms
- **Optimized implementations** with efficient data structures
- **TypeScript optimizations** with proper type inference
- **Memory efficient** algorithms with minimal overhead

## Algorithms Implemented

### Classification
- ✅ K-Nearest Neighbors (with weighted voting)
- ✅ Naive Bayes (with Laplace smoothing)
- ✅ Decision Trees (ID3 algorithm)
- ✅ Random Forest (ensemble method)
- ✅ Neural Networks (backpropagation)

### Clustering
- ✅ K-means (with multiple initialization)
- ✅ Elbow method for optimal k
- ✅ Silhouette score analysis
- ✅ Cluster quality metrics

### Mathematics
- ✅ Linear algebra (vectors, matrices)
- ✅ Statistics (descriptive statistics)
- ✅ Probability (distributions, Bayes)
- ✅ Optimization (gradient descent)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your algorithm with TypeScript types
4. Include comprehensive tests
5. Update documentation
6. Submit a pull request

## License

MIT License - see LICENSE file for details.

## Acknowledgments

Based on the "Data Science from Scratch" book and Python implementation, adapted for modern TypeScript with enhanced type safety and additional features.
