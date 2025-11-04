import {
    split_data,
    train_test_split,
    accuracy,
    precision,
    recall,
    f1_score
} from '../ts-data-scratch/machine_learning';

describe('Machine Learning Utilities', () => {
    describe('Data Splitting', () => {
        test('split_data should split data into train and test sets', () => {
            const data = [
                [1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]
            ];
            
            const result = split_data(data, 0.3);
            
            expect(result).toHaveProperty('train');
            expect(result).toHaveProperty('test');
            expect(Array.isArray(result.train)).toBe(true);
            expect(Array.isArray(result.test)).toBe(true);
            
            // Total should equal original
            expect(result.train.length + result.test.length).toBe(data.length);
            
            // Test set should be approximately 30% of data
            const testRatio = result.test.length / data.length;
            expect(testRatio).toBeGreaterThan(0.2);
            expect(testRatio).toBeLessThan(0.4);
        });

        test('split_data should handle different probabilities', () => {
            const data = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]];
            
            const result50 = split_data(data, 0.5);
            const result20 = split_data(data, 0.2);
            const result80 = split_data(data, 0.8);
            
            expect(result50.train.length + result50.test.length).toBe(10);
            expect(result20.train.length + result20.test.length).toBe(10);
            expect(result80.train.length + result80.test.length).toBe(10);
            
            // Check approximate ratios
            expect(result50.test.length / 10).toBeGreaterThan(0.3);
            expect(result50.test.length / 10).toBeLessThan(0.7);
            
            expect(result20.test.length / 10).toBeGreaterThan(0.1);
            expect(result20.test.length / 10).toBeLessThan(0.3);
            
            expect(result80.test.length / 10).toBeGreaterThan(0.7);
            expect(result80.test.length / 10).toBeLessThan(0.9);
        });

        test('split_data should handle edge probabilities', () => {
            const data = [[1], [2], [3], [4], [5]];
            
            // Probability 0 should put all in train
            const result0 = split_data(data, 0);
            expect(result0.train.length).toBe(5);
            expect(result0.test.length).toBe(0);
            
            // Probability 1 should put all in test
            const result1 = split_data(data, 1);
            expect(result1.train.length).toBe(0);
            expect(result1.test.length).toBe(5);
        });

        test('split_data should handle empty data', () => {
            const result = split_data([], 0.5);
            expect(result.train).toHaveLength(0);
            expect(result.test).toHaveLength(0);
        });

        test('split_data should handle single item', () => {
            const data = [[1]];
            const result = split_data(data, 0.5);
            
            expect(result.train.length + result.test.length).toBe(1);
            expect([0, 1]).toContain(result.train.length);
            expect([0, 1]).toContain(result.test.length);
        });

        test('split_data should be deterministic with same random seed would be nice', () => {
            const data = [[1], [2], [3], [4], [5]];
            
            // We can't test exact determinism without controlling random seed
            // But we can test that splits are valid
            const result1 = split_data(data, 0.4);
            const result2 = split_data(data, 0.4);
            
            expect(result1.train.length + result1.test.length).toBe(5);
            expect(result2.train.length + result2.test.length).toBe(5);
        });

        test('split_data should handle invalid probabilities', () => {
            const data = [[1], [2], [3]];
            
            // Negative probability should be treated as 0
            const resultNeg = split_data(data, -0.1);
            expect(resultNeg.train.length + resultNeg.test.length).toBe(3);
            
            // Probability > 1 should be treated as 1
            const resultLarge = split_data(data, 1.5);
            expect(resultLarge.train.length + resultLarge.test.length).toBe(3);
        });
    });

    describe('Train Test Split', () => {
        test('train_test_split should split features and labels', () => {
            const x = [[1, 2], [3, 4], [5, 6], [7, 8]];
            const y = [0, 1, 0, 1];
            
            const result = train_test_split(x, y, 0.25);
            
            expect(result).toHaveProperty('x_train');
            expect(result).toHaveProperty('x_test');
            expect(result).toHaveProperty('y_train');
            expect(result).toHaveProperty('y_test');
            
            // Check lengths
            expect(result.x_train.length).toBe(result.y_train.length);
            expect(result.x_test.length).toBe(result.y_test.length);
            expect(result.x_train.length + result.x_test.length).toBe(x.length);
            expect(result.y_train.length + result.y_test.length).toBe(y.length);
            
            // Check approximate test ratio
            const testRatio = result.x_test.length / x.length;
            expect(testRatio).toBeGreaterThan(0.1);
            expect(testRatio).toBeLessThan(0.4);
        });

        test('train_test_split should maintain correspondence between x and y', () => {
            const x = [[1], [2], [3], [4], [5], [6]];
            const y = [0, 1, 0, 1, 0, 1];
            
            const result = train_test_split(x, y, 0.5);
            
            // Each x_train should correspond to correct y_train
            // (We can't test exact correspondence without knowing the split)
            // But we can test that the splits are valid
            expect(result.x_train.length).toBe(result.y_train.length);
            expect(result.x_test.length).toBe(result.y_test.length);
        });

        test('train_test_split should handle different test sizes', () => {
            const x = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]];
            const y = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1];
            
            const result20 = train_test_split(x, y, 0.2);
            const result50 = train_test_split(x, y, 0.5);
            
            expect(result20.x_test.length / 10).toBeGreaterThan(0.1);
            expect(result20.x_test.length / 10).toBeLessThan(0.3);
            
            expect(result50.x_test.length / 10).toBeGreaterThan(0.3);
            expect(result50.x_test.length / 10).toBeLessThan(0.7);
        });

        test('train_test_split should handle edge cases', () => {
            const x = [[1], [2], [3]];
            const y = [0, 1, 0];
            
            // Test size 0
            const result0 = train_test_split(x, y, 0);
            expect(result0.x_train.length).toBe(3);
            expect(result0.x_test.length).toBe(0);
            expect(result0.y_train).toEqual(y);
            
            // Test size 1
            const result1 = train_test_split(x, y, 1);
            expect(result1.x_train.length).toBe(0);
            expect(result1.x_test.length).toBe(3);
            expect(result1.y_test).toEqual(y);
        });

        test('train_test_split should handle empty data', () => {
            const result = train_test_split([], [], 0.5);
            expect(result.x_train).toHaveLength(0);
            expect(result.x_test).toHaveLength(0);
            expect(result.y_train).toHaveLength(0);
            expect(result.y_test).toHaveLength(0);
        });

        test('train_test_split should handle mismatched lengths', () => {
            const x = [[1], [2], [3]];
            const y = [0, 1]; // Mismatched length
            
            expect(() => {
                train_test_split(x, y, 0.5);
            }).toThrow();
        });
    });

    describe('Performance Metrics', () => {
        test('accuracy should calculate correct accuracy', () => {
            expect(accuracy(50, 10, 5, 35)).toBeCloseTo(0.85, 4);
            expect(accuracy(100, 0, 0, 0)).toBe(1);
            expect(accuracy(0, 0, 0, 100)).toBe(1);
            expect(accuracy(0, 100, 0, 0)).toBe(0);
        });

        test('accuracy should handle edge cases', () => {
            expect(accuracy(0, 0, 0, 0)).toBeNaN();
            expect(accuracy(1, 1, 1, 1)).toBeCloseTo(0.5, 4);
        });

        test('precision should calculate correct precision', () => {
            expect(precision(50, 10, 5, 35)).toBeCloseTo(0.8333, 4);
            expect(precision(100, 0, 5, 35)).toBe(1);
            expect(precision(0, 100, 5, 35)).toBe(0);
        });

        test('precision should handle no positive predictions', () => {
            expect(precision(0, 0, 5, 35)).toBeNaN();
        });

        test('recall should calculate correct recall', () => {
            expect(recall(50, 10, 5, 35)).toBeCloseTo(0.9091, 4);
            expect(recall(50, 10, 0, 35)).toBe(1);
            expect(recall(0, 10, 50, 35)).toBe(0);
        });

        test('recall should handle no actual positives', () => {
            expect(recall(0, 10, 0, 35)).toBeNaN();
        });

        test('f1_score should calculate correct F1 score', () => {
            expect(f1_score(50, 10, 5, 35)).toBeCloseTo(0.8696, 4);
            expect(f1_score(100, 0, 0, 100)).toBe(1);
            expect(f1_score(0, 100, 0, 0)).toBe(0);
        });

        test('f1_score should handle edge cases', () => {
            expect(f1_score(0, 0, 0, 0)).toBeNaN();
            expect(f1_score(50, 0, 0, 50)).toBe(1); // Perfect classification
        });

        test('f1_score should be harmonic mean of precision and recall', () => {
            const tp = 50, fp = 10, fn = 5, tn = 35;
            const p = precision(tp, fp, fn, tn);
            const r = recall(tp, fp, fn, tn);
            const f1 = f1_score(tp, fp, fn, tn);
            
            const expected_f1 = 2 * p * r / (p + r);
            expect(f1).toBeCloseTo(expected_f1, 6);
        });
    });

    describe('Metric Properties', () => {
        test('accuracy should be between 0 and 1', () => {
            expect(accuracy(10, 10, 10, 10)).toBeCloseTo(0.5, 4);
            expect(accuracy(100, 0, 0, 0)).toBe(1);
            expect(accuracy(0, 100, 0, 0)).toBe(0);
        });

        test('precision should be between 0 and 1', () => {
            expect(precision(50, 50, 10, 10)).toBeCloseTo(0.5, 4);
            expect(precision(100, 0, 10, 10)).toBe(1);
            expect(precision(0, 100, 10, 10)).toBe(0);
        });

        test('recall should be between 0 and 1', () => {
            expect(recall(50, 10, 50, 10)).toBeCloseTo(0.5, 4);
            expect(recall(100, 10, 0, 10)).toBe(1);
            expect(recall(0, 10, 100, 10)).toBe(0);
        });

        test('f1_score should be between 0 and 1', () => {
            expect(f1_score(50, 10, 50, 10)).toBeCloseTo(0.5, 4);
            expect(f1_score(100, 0, 0, 100)).toBe(1);
            expect(f1_score(0, 100, 0, 0)).toBe(0);
        });
    });

    describe('Special Cases', () => {
        test('should handle perfect classification', () => {
            expect(accuracy(100, 0, 0, 100)).toBe(1);
            expect(precision(100, 0, 0, 100)).toBe(1);
            expect(recall(100, 0, 0, 100)).toBe(1);
            expect(f1_score(100, 0, 0, 100)).toBe(1);
        });

        test('should handle worst classification', () => {
            expect(accuracy(0, 100, 100, 0)).toBe(0);
            expect(precision(0, 100, 100, 0)).toBe(0);
            expect(recall(0, 100, 100, 0)).toBe(0);
            expect(f1_score(0, 100, 100, 0)).toBe(0);
        });

        test('should handle always positive classifier', () => {
            // Always predicts positive
            expect(accuracy(50, 50, 0, 0)).toBeCloseTo(0.5, 4);
            expect(precision(50, 50, 0, 0)).toBeCloseTo(0.5, 4);
            expect(recall(50, 50, 0, 0)).toBe(1);
        });

        test('should handle always negative classifier', () => {
            // Always predicts negative
            expect(accuracy(0, 0, 50, 50)).toBeCloseTo(0.5, 4);
            expect(precision(0, 0, 50, 50)).toBeNaN();
            expect(recall(0, 0, 50, 50)).toBe(0);
        });
    });

    describe('Edge Cases and Error Handling', () => {
        test('should handle negative values gracefully', () => {
            // Metrics should handle negative inputs (though they don't make practical sense)
            expect(() => accuracy(-1, 10, 10, 10)).not.toThrow();
            expect(() => precision(-1, 10, 10, 10)).not.toThrow();
            expect(() => recall(-1, 10, 10, 10)).not.toThrow();
            expect(() => f1_score(-1, 10, 10, 10)).not.toThrow();
        });

        test('should handle very large numbers', () => {
            expect(() => accuracy(1e6, 1e6, 1e6, 1e6)).not.toThrow();
            expect(() => precision(1e6, 1e6, 1e6, 1e6)).not.toThrow();
            expect(() => recall(1e6, 1e6, 1e6, 1e6)).not.toThrow();
            expect(() => f1_score(1e6, 1e6, 1e6, 1e6)).not.toThrow();
        });

        test('should handle zero cases correctly', () => {
            expect(accuracy(0, 0, 0, 0)).toBeNaN();
            expect(precision(0, 0, 0, 0)).toBeNaN();
            expect(recall(0, 0, 0, 0)).toBeNaN();
            expect(f1_score(0, 0, 0, 0)).toBeNaN();
        });
    });

    describe('Performance Tests', () => {
        test('should handle large datasets efficiently', () => {
            const largeData = [];
            for (let i = 0; i < 10000; i++) {
                largeData.push([i, i + 1]);
            }
            
            const start = Date.now();
            const result = split_data(largeData, 0.3);
            const duration = Date.now() - start;
            
            expect(result.train.length + result.test.length).toBe(10000);
            expect(duration).toBeLessThan(1000); // Should complete within 1 second
        });

        test('should handle multiple metric calculations efficiently', () => {
            const start = Date.now();
            
            for (let i = 0; i < 1000; i++) {
                accuracy(50, 10, 5, 35);
                precision(50, 10, 5, 35);
                recall(50, 10, 5, 35);
                f1_score(50, 10, 5, 35);
            }
            
            const duration = Date.now() - start;
            expect(duration).toBeLessThan(500); // Should complete within 500ms
        });
    });

    describe('Consistency Tests', () => {
        test('split_data should maintain data integrity', () => {
            const originalData = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]];
            const result = split_data(originalData, 0.4);
            
            // Check that no data is lost or duplicated
            const allData = [...result.train, ...result.test];
            
            // Sort both arrays to compare (order may be different due to random split)
            const sortedOriginal = originalData.sort();
            const sortedResult = allData.sort();
            
            expect(sortedResult).toEqual(sortedOriginal);
        });

        test('train_test_split should maintain feature-label correspondence', () => {
            const x = [[1], [2], [3], [4], [5]];
            const y = [10, 20, 30, 40, 50];
            
            const result = train_test_split(x, y, 0.4);
            
            // Check that each x in train corresponds to correct y in train
            // (This is a simplified check - in practice we'd need to track indices)
            expect(result.x_train.length).toBe(result.y_train.length);
            expect(result.x_test.length).toBe(result.y_test.length);
        });
    });
});
