import {
    mean,
    median,
    mode,
    variance,
    standard_deviation,
    range,
    quantile,
    interquartile_range,
    skewness,
    kurtosis,
    correlation,
    covariance
} from '../ts-data-scratch/stats';

describe('Statistics', () => {
    describe('Central Tendency', () => {
        test('mean should calculate arithmetic mean', () => {
            expect(mean([1, 2, 3, 4, 5])).toBe(3);
            expect(mean([0, 0, 0])).toBe(0);
            expect(mean([-1, 1])).toBe(0);
            expect(mean([2.5, 3.5])).toBe(3);
        });

        test('mean should handle empty array', () => {
            expect(mean([])).toBeNaN();
        });

        test('mean should handle single element', () => {
            expect(mean([5])).toBe(5);
            expect(mean([-3])).toBe(-3);
        });

        test('median should calculate median correctly', () => {
            expect(median([1, 2, 3, 4, 5])).toBe(3);
            expect(median([1, 2, 3, 4])).toBe(2.5);
            expect(median([5, 1, 3, 2, 4])).toBe(3); // Unsorted
            expect(median([4, 2, 1, 3])).toBe(2.5); // Unsorted even
        });

        test('median should handle empty array', () => {
            expect(median([])).toBeNaN();
        });

        test('median should handle single element', () => {
            expect(median([5])).toBe(5);
        });

        test('mode should return most frequent value', () => {
            expect(mode([1, 2, 2, 3, 3, 3, 4])).toBe(3);
            expect(mode([5, 5, 5, 5])).toBe(5);
            expect(mode([1, 2, 3, 4])).toBe(1); // First in case of tie
        });

        test('mode should handle empty array', () => {
            expect(mode([])).toBeNaN();
        });

        test('mode should handle single element', () => {
            expect(mode([5])).toBe(5);
        });

        test('mode should handle all same values', () => {
            expect(mode([7, 7, 7, 7])).toBe(7);
        });
    });

    describe('Dispersion', () => {
        test('variance should calculate sample variance', () => {
            const data = [1, 2, 3, 4, 5];
            expect(variance(data)).toBeCloseTo(2.5, 4);
            
            const data2 = [2, 4, 4, 4, 5, 5, 7, 9];
            expect(variance(data2)).toBeCloseTo(4.5714, 3);
        });

        test('variance should handle empty array', () => {
            expect(variance([])).toBeNaN();
        });

        test('variance should handle single element', () => {
            expect(variance([5])).toBeNaN(); // Sample variance requires at least 2 elements
        });

        test('standard_deviation should calculate sample standard deviation', () => {
            const data = [1, 2, 3, 4, 5];
            expect(standard_deviation(data)).toBeCloseTo(1.5811, 4);
            
            const data2 = [2, 4, 4, 4, 5, 5, 7, 9];
            expect(standard_deviation(data2)).toBeCloseTo(2.1381, 3);
        });

        test('standard_deviation should handle empty array', () => {
            expect(standard_deviation([])).toBeNaN();
        });

        test('range should calculate range', () => {
            expect(range([1, 2, 3, 4, 5])).toBe(4);
            expect(range([10, 5, 15])).toBe(10);
            expect(range([-5, -1, -3])).toBe(4);
        });

        test('range should handle empty array', () => {
            expect(range([])).toBeNaN();
        });

        test('range should handle single element', () => {
            expect(range([5])).toBe(0);
        });

        test('quantile should calculate quantiles correctly', () => {
            const data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
            
            expect(quantile(data, 0.25)).toBe(3.25); // Q1
            expect(quantile(data, 0.5)).toBe(5.5);   // Median
            expect(quantile(data, 0.75)).toBe(7.75); // Q3
            expect(quantile(data, 0)).toBe(1);
            expect(quantile(data, 1)).toBe(10);
        });

        test('quantile should handle empty array', () => {
            expect(quantile([], 0.5)).toBeNaN();
        });

        test('quantile should handle invalid p values', () => {
            const data = [1, 2, 3, 4, 5];
            expect(quantile(data, -0.1)).toBeNaN();
            expect(quantile(data, 1.1)).toBeNaN();
        });

        test('interquartile_range should calculate IQR', () => {
            const data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
            expect(interquartile_range(data)).toBeCloseTo(4.5, 4); // Q3 - Q1 = 7.75 - 3.25
        });

        test('interquartile_range should handle empty array', () => {
            expect(interquartile_range([])).toBeNaN();
        });
    });

    describe('Shape Measures', () => {
        test('skewness should calculate skewness', () => {
            // Symmetric data should have skewness near 0
            const symmetric = [1, 2, 3, 4, 5];
            expect(skewness(symmetric)).toBeCloseTo(0, 4);
            
            // Right-skewed data should have positive skewness
            const rightSkewed = [1, 2, 3, 4, 10];
            expect(skewness(rightSkewed)).toBeGreaterThan(0);
            
            // Left-skewed data should have negative skewness
            const leftSkewed = [1, 6, 7, 8, 9];
            expect(skewness(leftSkewed)).toBeLessThan(0);
        });

        test('skewness should handle empty array', () => {
            expect(skewness([])).toBeNaN();
        });

        test('skewness should handle insufficient data', () => {
            expect(skewness([1, 2])).toBeNaN();
        });

        test('kurtosis should calculate kurtosis', () => {
            // Normal-like data should have kurtosis near 0 (excess kurtosis)
            const normal = [1, 2, 3, 4, 5, 6, 7, 8];
            expect(Math.abs(kurtosis(normal))).toBeLessThan(2);
        });

        test('kurtosis should handle empty array', () => {
            expect(kurtosis([])).toBeNaN();
        });

        test('kurtosis should handle insufficient data', () => {
            expect(kurtosis([1, 2, 3])).toBeNaN();
        });
    });

    describe('Correlation and Covariance', () => {
        test('correlation should calculate Pearson correlation', () => {
            // Perfect positive correlation
            const perfectPositive = [1, 2, 3, 4, 5];
            expect(correlation(perfectPositive, perfectPositive)).toBeCloseTo(1, 4);
            
            // Perfect negative correlation
            const perfectNegative = [1, 2, 3, 4, 5];
            const negative = [5, 4, 3, 2, 1];
            expect(correlation(perfectNegative, negative)).toBeCloseTo(-1, 4);
            
            // No correlation (zero variance in second array, epsilon prevents NaN)
            const noCorr1 = [1, 2, 3, 4, 5];
            const noCorr2 = [1, 1, 1, 1, 1];
            expect(correlation(noCorr1, noCorr2)).toBeCloseTo(0, 4);
        });

        test('correlation should handle different length arrays', () => {
            const arr1 = [1, 2, 3];
            const arr2 = [1, 2, 3, 4];
            expect(correlation(arr1, arr2)).toBeNaN();
        });

        test('correlation should handle empty arrays', () => {
            expect(correlation([], [])).toBeNaN();
        });

        test('correlation should handle single element arrays', () => {
            expect(correlation([1], [2])).toBeNaN();
        });

        test('covariance should calculate covariance', () => {
            const arr1 = [1, 2, 3, 4, 5];
            const arr2 = [2, 4, 6, 8, 10]; // 2 * arr1
            
            const cov = covariance(arr1, arr2);
            expect(cov).toBeGreaterThan(0);
        });

        test('covariance should handle different length arrays', () => {
            const arr1 = [1, 2, 3];
            const arr2 = [1, 2, 3, 4];
            expect(covariance(arr1, arr2)).toBeNaN();
        });

        test('covariance should handle empty arrays', () => {
            expect(covariance([], [])).toBeNaN();
        });

        test('covariance should handle single element arrays', () => {
            expect(covariance([1], [2])).toBeNaN();
        });
    });

    describe('Edge Cases', () => {
        test('should handle large numbers', () => {
            const largeNumbers = [1e6, 2e6, 3e6, 4e6, 5e6];
            expect(mean(largeNumbers)).toBe(3e6);
            expect(variance(largeNumbers)).toBeCloseTo(2.5e12, 4);
        });

        test('should handle very small numbers', () => {
            const smallNumbers = [1e-6, 2e-6, 3e-6, 4e-6, 5e-6];
            expect(mean(smallNumbers)).toBeCloseTo(3e-6, 10);
            expect(variance(smallNumbers)).toBeCloseTo(2.5e-12, 4);
        });

        test('should handle negative numbers', () => {
            const negatives = [-5, -4, -3, -2, -1];
            expect(mean(negatives)).toBe(-3);
            expect(median(negatives)).toBe(-3);
            expect(range(negatives)).toBe(4);
        });

        test('should handle mixed positive and negative', () => {
            const mixed = [-10, -5, 0, 5, 10];
            expect(mean(mixed)).toBe(0);
            expect(median(mixed)).toBe(0);
            expect(range(mixed)).toBe(20);
        });

        test('should handle decimal numbers', () => {
            const decimals = [1.1, 2.2, 3.3, 4.4, 5.5];
            expect(mean(decimals)).toBeCloseTo(3.3, 4);
            expect(median(decimals)).toBe(3.3);
        });

        test('should handle identical values', () => {
            const identical = [5, 5, 5, 5, 5];
            expect(mean(identical)).toBe(5);
            expect(median(identical)).toBe(5);
            expect(mode(identical)).toBe(5);
            expect(variance(identical)).toBeCloseTo(0, 4);
            expect(standard_deviation(identical)).toBeCloseTo(0, 4);
            expect(range(identical)).toBe(0);
        });

        test('should handle arrays with NaN values', () => {
            const withNaN = [1, 2, NaN, 4, 5];
            expect(mean(withNaN)).toBeNaN();
            expect(median(withNaN)).toBeNaN();
        });

        test('should handle arrays with Infinity values', () => {
            const withInf = [1, 2, Infinity, 4, 5];
            expect(mean(withInf)).toBe(Infinity);
        });
    });

    describe('Performance Tests', () => {
        test('should handle large arrays efficiently', () => {
            const largeArray = [];
            for (let i = 0; i < 10000; i++) {
                largeArray.push(Math.random() * 100);
            }
            
            const start = Date.now();
            const result = mean(largeArray);
            const duration = Date.now() - start;
            
            expect(typeof result).toBe('number');
            expect(duration).toBeLessThan(1000); // Should complete within 1 second
        });

        test('should handle multiple calculations efficiently', () => {
            const data = [];
            for (let i = 0; i < 1000; i++) {
                data.push(Math.random() * 100);
            }
            
            const start = Date.now();
            mean(data);
            median(data);
            mode(data);
            variance(data);
            standard_deviation(data);
            const duration = Date.now() - start;
            
            expect(duration).toBeLessThan(500); // Should complete within 500ms
        });
    });

    describe('Statistical Properties', () => {
        test('mean should be between min and max', () => {
            const data = [10, 20, 30, 40, 50];
            const avg = mean(data);
            expect(avg).toBeGreaterThanOrEqual(Math.min(...data));
            expect(avg).toBeLessThanOrEqual(Math.max(...data));
        });

        test('standard deviation should be non-negative', () => {
            const data = [1, 2, 3, 4, 5];
            expect(standard_deviation(data)).toBeGreaterThanOrEqual(0);
        });

        test('variance should be non-negative', () => {
            const data = [1, 2, 3, 4, 5];
            expect(variance(data)).toBeGreaterThanOrEqual(0);
        });

        test('range should be non-negative', () => {
            const data = [1, 2, 3, 4, 5];
            expect(range(data)).toBeGreaterThanOrEqual(0);
        });

        test('correlation should be between -1 and 1', () => {
            const x = [1, 2, 3, 4, 5];
            const y = [2, 4, 6, 8, 10];
            const corr = correlation(x, y);
            
            if (!isNaN(corr)) {
                expect(corr).toBeGreaterThanOrEqual(-1);
                expect(corr).toBeLessThanOrEqual(1);
            }
        });
    });

    describe('Special Cases', () => {
        test('should handle mathematical constants', () => {
            const pi = [3.14159, 3.14159, 3.14159];
            expect(mean(pi)).toBeCloseTo(3.14159, 5);
            expect(variance(pi)).toBeCloseTo(0, 5);
        });

        test('should handle binary data', () => {
            const binary = [0, 1, 0, 1, 0, 1, 0, 1];
            expect(mean(binary)).toBe(0.5);
            expect(mode(binary)).toBe(0); // First occurrence in tie
        });

        test('should handle ordinal data as numbers', () => {
            const ordinal = [1, 2, 2, 3, 3, 3, 4, 5]; // Likert scale
            expect(mean(ordinal)).toBeCloseTo(2.875, 3);
            expect(median(ordinal)).toBe(3); // Average of 4th and 5th elements: (3+3)/2
            expect(mode(ordinal)).toBe(3);
        });
    });
});
