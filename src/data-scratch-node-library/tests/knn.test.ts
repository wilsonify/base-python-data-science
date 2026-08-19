import {
    rawMajorityVote,
    majorityVote,
    knnClassify,
    knnClassifyWithDistance,
    weightedKnnClassify,
    knnCrossValidate,
    findOptimalK,
    predictLanguageForCity,
    cities
} from '../ts-data-scratch/knn';

describe('K-Nearest Neighbors', () => {
    describe('Voting Functions', () => {
        test('rawMajorityVote should return most common label', () => {
            expect(rawMajorityVote(['A', 'A', 'B'])).toBe('A');
            expect(rawMajorityVote(['A', 'B', 'C', 'B'])).toBe('B');
            expect(rawMajorityVote(['X', 'Y', 'Z'])).toBe('X'); // First in case of tie
        });

        test('majorityVote should handle ties correctly', () => {
            // Should recursively remove farthest until tie is broken
            expect(majorityVote(['A', 'B', 'A', 'B'])).toBe('A'); // Removes last B
            expect(majorityVote(['A', 'A', 'B', 'B', 'C'])).toBe('A'); // Removes C, then tie
        });

        test('majorityVote should handle single label', () => {
            expect(majorityVote(['A'])).toBe('A');
            expect(majorityVote(['B', 'B', 'B'])).toBe('B');
        });
    });

    describe('Classification Functions', () => {
        const labeledPoints = [
            { point: [1, 1], label: 'A' },
            { point: [2, 2], label: 'A' },
            { point: [10, 10], label: 'B' },
            { point: [11, 11], label: 'B' }
        ];

        test('knnClassify should classify correctly', () => {
            expect(knnClassify(1, labeledPoints, [1.5, 1.5])).toBe('A');
            expect(knnClassify(1, labeledPoints, [10.5, 10.5])).toBe('B');
            expect(knnClassify(3, labeledPoints, [1.5, 1.5])).toBe('A');
        });

        test('knnClassify should handle k larger than dataset', () => {
            expect(() => knnClassify(5, labeledPoints, [1, 1])).toThrow();
        });

        test('knnClassifyWithDistance should return detailed info', () => {
            const result = knnClassifyWithDistance(3, labeledPoints, [1.5, 1.5]);
            
            expect(result).toHaveProperty('prediction');
            expect(result).toHaveProperty('distances');
            expect(result).toHaveProperty('neighbors');
            
            expect(result.prediction).toBe('A');
            expect(result.distances).toHaveLength(3);
            expect(result.neighbors).toHaveLength(3);
            
            // Distances should be sorted (closest first)
            expect(result.distances[0]).toBeLessThanOrEqual(result.distances[1]);
            expect(result.distances[1]).toBeLessThanOrEqual(result.distances[2]);
        });

        test('weightedKnnClassify should use distance weighting', () => {
            const result = weightedKnnClassify(3, labeledPoints, [1.5, 1.5]);
            expect(typeof result).toBe('string');
            expect(['A', 'B']).toContain(result);
        });
    });

    describe('Cross-Validation', () => {
        const labeledPoints = [
            { point: [1, 1], label: 'A' },
            { point: [2, 2], label: 'A' },
            { point: [3, 3], label: 'A' },
            { point: [10, 10], label: 'B' },
            { point: [11, 11], label: 'B' },
            { point: [12, 12], label: 'B' }
        ];

        test('knnCrossValidate should return accuracy between 0 and 1', () => {
            const accuracy = knnCrossValidate(3, labeledPoints, 3);
            expect(accuracy).toBeGreaterThanOrEqual(0);
            expect(accuracy).toBeLessThanOrEqual(1);
        });

        test('knnCrossValidate should work with different fold counts', () => {
            const acc3 = knnCrossValidate(3, labeledPoints, 3);
            const acc5 = knnCrossValidate(3, labeledPoints, 5);
            
            expect(typeof acc3).toBe('number');
            expect(typeof acc5).toBe('number');
        });

        test('knnCrossValidate should handle small datasets', () => {
            const smallData = [
                { point: [1, 1], label: 'A' },
                { point: [2, 2], label: 'B' }
            ];
            
            const accuracy = knnCrossValidate(1, smallData, 2);
            expect(typeof accuracy).toBe('number');
        });
    });

    describe('Optimal K Finding', () => {
        const labeledPoints = [
            { point: [1, 1], label: 'A' },
            { point: [2, 2], label: 'A' },
            { point: [3, 3], label: 'A' },
            { point: [10, 10], label: 'B' },
            { point: [11, 11], label: 'B' },
            { point: [12, 12], label: 'B' }
        ];

        test('findOptimalK should return valid results', () => {
            const result = findOptimalK(labeledPoints, 3, 3);
            
            expect(result).toHaveProperty('optimalK');
            expect(result).toHaveProperty('accuracies');
            
            expect(typeof result.optimalK).toBe('number');
            expect(Array.isArray(result.accuracies)).toBe(true);
            expect(result.accuracies).toHaveLength(3);
            expect(result.optimalK).toBeGreaterThanOrEqual(1);
            expect(result.optimalK).toBeLessThanOrEqual(3);
        });

        test('findOptimalK should handle small maxK', () => {
            const result = findOptimalK(labeledPoints, 3, 2);
            expect(result.optimalK).toBeGreaterThanOrEqual(1);
            expect(result.optimalK).toBeLessThanOrEqual(3);
        });
    });

    describe('Example Functions', () => {
        test('predictLanguageForCity should return valid language', () => {
            const prediction = predictLanguageForCity(-87.68, 41.83); // Chicago
            expect(['Python', 'Java', 'R']).toContain(prediction);
            expect(typeof prediction).toBe('string');
        });

        test('cities data should be properly formatted', () => {
            expect(cities).toHaveLength(20);
            expect(cities[0]).toHaveProperty('point');
            expect(cities[0]).toHaveProperty('label');
            expect(Array.isArray(cities[0].point)).toBe(true);
            expect(cities[0].point).toHaveLength(2);
        });
    });

    describe('Edge Cases', () => {
        test('should handle identical points', () => {
            const data = [
                { point: [1, 1], label: 'A' },
                { point: [1, 1], label: 'B' }
            ];
            
            const result = knnClassify(1, data, [1, 1]);
            expect(['A', 'B']).toContain(result);
        });

        test('should handle high dimensional data', () => {
            const highDimData = [
                { point: [1, 2, 3, 4, 5], label: 'A' },
                { point: [2, 3, 4, 5, 6], label: 'A' },
                { point: [10, 11, 12, 13, 14], label: 'B' }
            ];
            
            const result = knnClassify(1, highDimData, [1.5, 2.5, 3.5, 4.5, 5.5]);
            expect(result).toBe('A');
        });

        test('should handle negative coordinates', () => {
            const data = [
                { point: [-1, -1], label: 'A' },
                { point: [1, 1], label: 'B' }
            ];
            
            expect(knnClassify(1, data, [-0.5, -0.5])).toBe('A');
            expect(knnClassify(1, data, [0.5, 0.5])).toBe('B');
        });

        test('should handle zero distance case', () => {
            const data = [
                { point: [1, 1], label: 'A' },
                { point: [2, 2], label: 'B' }
            ];
            
            const result = knnClassify(1, data, [1, 1]); // Exact match with first point
            expect(result).toBe('A');
        });
    });

    describe('Performance Tests', () => {
        test('should handle moderately large datasets', () => {
            const largeData = [];
            for (let i = 0; i < 100; i++) {
                largeData.push({
                    point: [Math.random(), Math.random()],
                    label: i < 50 ? 'A' : 'B'
                });
            }
            
            const start = Date.now();
            const result = knnClassify(5, largeData, [0.5, 0.5]);
            const duration = Date.now() - start;
            
            expect(['A', 'B']).toContain(result);
            expect(duration).toBeLessThan(1000); // Should complete within 1 second
        });
    });
});
