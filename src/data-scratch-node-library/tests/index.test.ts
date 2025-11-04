// Main test suite runner
// This file imports all test modules to ensure they run

// Import all test modules to ensure they are executed
import './linear-algebra.test';
import './knn.test';
import './naive-bayes.test';
import './clustering.test';
import './neural-networks.test';
import './decision-trees.test';
import './stats.test';
import './probability.test';
import './machine-learning.test';

describe('TypeScript Data Science Library - Integration Tests', () => {
    test('Library should be importable and functional', () => {
        // Test that we can import the main library
        const lib = require('../ts-data-scratch/index');
        
        expect(lib).toBeDefined();
        
        // Test that key functions are available
        expect(typeof lib.knnClassify).toBe('function');
        expect(typeof lib.NaiveBayesClassifier).toBe('function');
        expect(typeof lib.kMeans).toBe('function');
        expect(typeof lib.sigmoid).toBe('function');
        expect(typeof lib.buildDecisionTree).toBe('function');
        expect(typeof lib.distance).toBe('function');
        expect(typeof lib.mean).toBe('function');
    });

    test('Basic functionality should work end-to-end', () => {
        const {
            knnClassify,
            NaiveBayesClassifier,
            kMeans,
            sigmoid,
            distance,
            vector_add
        } = require('../ts-data-scratch/index');

        // Test KNN
        const cities = [
            { point: [-86.75, 33.57], label: 'Python' },
            { point: [-112.02, 33.43], label: 'Java' }
        ];
        const prediction = knnClassify(1, cities, [-87.68, 41.83]);
        expect(['Python', 'Java']).toContain(prediction);

        // Test Naive Bayes
        const classifier = new NaiveBayesClassifier();
        classifier.train([
            { message: 'spam message', isSpam: true },
            { message: 'ham message', isSpam: false }
        ]);
        const result = classifier.classify('test message');
        expect(typeof result.isSpam).toBe('boolean');

        // Test Clustering
        const points = [[1, 2], [10, 4], [1, 0], [10, 2]];
        const clusters = kMeans(points, 2);
        expect(clusters.clusters).toHaveLength(2);

        // Test Neural Networks
        const sigmoidResult = sigmoid(0);
        expect(sigmoidResult).toBeCloseTo(0.5, 4);

        // Test Linear Algebra
        const sum = vector_add([1, 2], [3, 4]);
        expect(sum).toEqual([4, 6]);

        const dist = distance([1, 2], [4, 6]);
        expect(dist).toBeCloseTo(5, 4);
    });

    test('Library should handle edge cases gracefully', () => {
        const {
            knnClassify,
            distance,
            mean,
            NaiveBayesClassifier
        } = require('../ts-data-scratch/index');

        // Test empty inputs
        expect(() => mean([])).not.toThrow();
        expect(mean([])).toBeNaN();

        // Test distance with same points
        expect(distance([1, 1], [1, 1])).toBe(0);

        // Test KNN with minimal data
        const minimalData = [{ point: [0, 0], label: 'A' }];
        expect(knnClassify(1, minimalData, [0, 0])).toBe('A');

        // Test Naive Bayes with minimal training
        const nb = new NaiveBayesClassifier();
        nb.train([{ message: 'test', isSpam: true }]);
        const nbResult = nb.classify('test');
        expect(typeof nbResult.isSpam).toBe('boolean');
    });

    test('Library should maintain type safety', () => {
        // This test ensures that the TypeScript types are working correctly
        const lib = require('../ts-data-scratch/index');

        // All exported functions should be of correct type
        const functionExports = [
            'knnClassify', 'knnClassifyWithDistance', 'weightedKnnClassify',
            'knnCrossValidate', 'findOptimalK', 'predictLanguageForCity',
            'classifyMessage', 'naiveBayesCrossValidate',
            'kMeans', 'kMeansMultipleRuns', 'findOptimalK', 'silhouetteScore',
            'analyzeClustering',
            'sigmoid', 'sigmoidDerivative', 'stepFunction', 'tanh', 'tanhDerivative',
            'relu', 'reluDerivative', 'perceptron', 'neuron',
            'feedForward', 'backpropagation', 'updateWeights',
            'trainSimpleNetwork', 'predict', 'xorExample',
            'createNetwork', 'getNetworkInfo',
            'buildDecisionTree', 'classify', 'treeAccuracy',
            'scalar_add', 'vector_add', 'vector_subtract', 'vector_sum',
            'scalar_multiply', 'vector_mean', 'dot', 'sum_of_squares',
            'magnitude', 'squared_distance', 'distance',
            'shape', 'get_row', 'get_column', 'make_matrix',
            'is_diagonal', 'matrix_add',
            'mean', 'median', 'mode', 'variance', 'standard_deviation',
            'range', 'quantile', 'interquartile_range', 'skewness', 'kurtosis',
            'correlation', 'covariance',
            'erf', 'normal_cdf', 'inverse_normal_cdf',
            'bernoulli_trial', 'binomial', 'binomial_distribution',
            'normal_probability_below', 'normal_probability_above',
            'normal_probability_between', 'normal_upper_bound',
            'normal_lower_bound', 'normal_two_sided_bounds',
            'split_data', 'train_test_split',
            'accuracy', 'precision', 'recall', 'f1_score'
        ];

        functionExports.forEach(funcName => {
            expect(typeof lib[funcName]).toBe('function');
        });

        // Classes should be constructors
        expect(typeof lib.NaiveBayesClassifier).toBe('function');
        expect(typeof lib.RandomForest).toBe('function');
    });

    test('Library should be performant', () => {
        const {
            knnClassify,
            kMeans,
            mean,
            distance
        } = require('../ts-data-scratch/index');

        // Performance test - should complete reasonable operations quickly
        const start = Date.now();

        // Test KNN with moderate dataset
        const knnData = [];
        for (let i = 0; i < 100; i++) {
            knnData.push({
                point: [Math.random(), Math.random()],
                label: i < 50 ? 'A' : 'B'
            });
        }
        knnClassify(5, knnData, [0.5, 0.5]);

        // Test clustering
        const clusterPoints = [];
        for (let i = 0; i < 50; i++) {
            clusterPoints.push([Math.random() * 10, Math.random() * 10]);
        }
        kMeans(clusterPoints, 3, 10);

        // Test statistics
        const statsData = [];
        for (let i = 0; i < 1000; i++) {
            statsData.push(Math.random() * 100);
        }
        mean(statsData);

        const duration = Date.now() - start;
        expect(duration).toBeLessThan(2000); // Should complete within 2 seconds
    });
});
