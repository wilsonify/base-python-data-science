// Data Science Library in TypeScript
// Main export file for all functionality

// Linear Algebra
export * from './linear_algebra';

// Statistics
export * from './stats';

// Probability
export * from './probability';

// Machine Learning Utilities
export * from './machine_learning';

// K-Nearest Neighbors
export * from './knn';

// Naive Bayes
export * from './naive_bayes';

// Decision Trees
export { 
    buildDecisionTree, 
    classify, 
    printTree, 
    treeAccuracy, 
    RandomForest,
    exampleData,
    candidateAttributes,
    type DataPoint,
    type TreeNode
} from './decision_trees';

// Clustering
export { 
    kMeans, 
    kMeansMultipleRuns, 
    findOptimalK as findOptimalKClustering,
    silhouetteScore,
    analyzeClustering,
    examplePoints,
    exampleUsage as clusteringExampleUsage,
    type Point,
    type Cluster,
    type KMeansResult
} from './clustering';

// Neural Networks
export { 
    sigmoid,
    sigmoidDerivative,
    stepFunction,
    tanh,
    tanhDerivative,
    relu,
    reluDerivative,
    perceptron,
    neuron,
    feedForward,
    backpropagation,
    updateWeights,
    trainSimpleNetwork,
    predict,
    xorExample,
    createNetwork,
    getNetworkInfo,
    exampleUsage as neuralNetworksExampleUsage,
    type Layer,
    type NeuralNetwork,
    type TrainingData
} from './neural_networks';

// Type Helpers
export * from './type-helpers';

// Default Map
export * from './defaultmap';

// Deep Learning
export * from './deep_learning/index';
export * from './deep_learning/layer';
export * from './deep_learning/metrics';
export * from './deep_learning/io';
