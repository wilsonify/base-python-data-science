import {
    kMeans,
    kMeansMultipleRuns,
    findOptimalK,
    silhouetteScore,
    analyzeClustering,
    examplePoints,
    exampleUsage
} from '../ts-data-scratch/clustering';

describe('K-Means Clustering', () => {
    describe('Basic K-Means', () => {
        const points = [
            [1, 2], [1, 4], [1, 0],  // Cluster 1
            [10, 2], [10, 4], [10, 0], // Cluster 2
            [5, 8], [5, 10], [5, 6]    // Cluster 3
        ];

        test('kMeans should cluster points correctly', () => {
            const result = kMeans(points, 3);
            
            expect(result).toHaveProperty('clusters');
            expect(result).toHaveProperty('assignments');
            expect(result).toHaveProperty('means');
            expect(result).toHaveProperty('totalSquaredError');
            expect(result).toHaveProperty('iterations');
            
            expect(result.clusters).toHaveLength(3);
            expect(result.assignments).toHaveLength(points.length);
            expect(result.means).toHaveLength(3);
            expect(typeof result.totalSquaredError).toBe('number');
            expect(typeof result.iterations).toBe('number');
            
            // All points should be assigned to a cluster
            result.assignments.forEach(assignment => {
                expect(assignment).toBeGreaterThanOrEqual(0);
                expect(assignment).toBeLessThan(3);
            });
            
            // Total points in clusters should equal input points
            const totalClusterPoints = result.clusters.reduce(
                (sum, cluster) => sum + cluster.points.length, 0
            );
            expect(totalClusterPoints).toBe(points.length);
        });

        test('kMeans should handle k=1', () => {
            const result = kMeans(points, 1);
            
            expect(result.clusters).toHaveLength(1);
            expect(result.assignments.every(a => a === 0)).toBe(true);
        });

        test('kMeans should handle k equal to number of points', () => {
            const smallPoints = [[1, 1], [2, 2], [3, 3]];
            const result = kMeans(smallPoints, 3);
            
            expect(result.clusters).toHaveLength(3);
            // Each point should be in its own cluster (or some distribution)
            expect(result.assignments).toHaveLength(3);
        });

        test('kMeans should handle empty input', () => {
            expect(() => kMeans([], 2)).toThrow('Cannot cluster empty dataset');
        });

        test('kMeans should handle invalid k values', () => {
            expect(() => kMeans(points, 0)).toThrow('Number of clusters must be positive');
            expect(() => kMeans(points, -1)).toThrow('Number of clusters must be positive');
            expect(() => kMeans(points, points.length + 1)).toThrow('Number of clusters cannot exceed number of points');
        });

        test('kMeans should handle different maxIterations', () => {
            const result1 = kMeans(points, 3, 10);
            const result2 = kMeans(points, 3, 100);
            
            expect(result1.iterations).toBeLessThanOrEqual(10);
            expect(result2.iterations).toBeLessThanOrEqual(100);
        });

        test('kMeans should handle initial assignments', () => {
            const initialAssignments = [0, 0, 0, 1, 1, 1, 2, 2, 2];
            const result = kMeans(points, 3, 100, initialAssignments);
            
            expect(result.assignments).toHaveLength(points.length);
        });
    });

    describe('Multiple Runs', () => {
        const points = [
            [1, 1], [2, 2], [8, 8], [9, 9]
        ];

        test('kMeansMultipleRuns should return best result', () => {
            const result = kMeansMultipleRuns(points, 2, 5, 50);
            
            expect(result).toHaveProperty('clusters');
            expect(result).toHaveProperty('totalSquaredError');
            
            expect(result.clusters).toHaveLength(2);
            expect(typeof result.totalSquaredError).toBe('number');
        });

        test('kMeansMultipleRuns should handle different run counts', () => {
            const result1 = kMeansMultipleRuns(points, 2, 3, 50);
            const result2 = kMeansMultipleRuns(points, 2, 10, 50);
            
            expect(result1.clusters).toHaveLength(2);
            expect(result2.clusters).toHaveLength(2);
        });
    });

    describe('Optimal K Finding', () => {
        const points = [
            [1, 1], [2, 2], [1.5, 1.5],  // Cluster 1
            [8, 8], [9, 9], [8.5, 8.5],  // Cluster 2
            [15, 15], [16, 16], [15.5, 15.5] // Cluster 3
        ];

        test('findOptimalK should return valid results', () => {
            const result = findOptimalK(points, 5, 3);
            
            expect(result).toHaveProperty('optimalK');
            expect(result).toHaveProperty('errors');
            expect(result).toHaveProperty('elbowPoint');
            
            expect(typeof result.optimalK).toBe('number');
            expect(Array.isArray(result.errors)).toBe(true);
            expect(result.errors).toHaveLength(5);
            expect(result.optimalK).toBeGreaterThanOrEqual(1);
            expect(result.optimalK).toBeLessThanOrEqual(5);
            
            // Errors should generally decrease (but not always strictly)
            expect(result.errors[0]).toBeGreaterThan(result.errors[4]);
        });

        test('findOptimalK should handle small datasets', () => {
            const smallPoints = [[1, 1], [2, 2], [8, 8]];
            const result = findOptimalK(smallPoints, 3, 2);
            
            expect(result.optimalK).toBeGreaterThanOrEqual(1);
            expect(result.optimalK).toBeLessThanOrEqual(3);
        });

        test('findOptimalK should handle different runs per K', () => {
            const result1 = findOptimalK(points, 3, 2);
            const result2 = findOptimalK(points, 3, 5);
            
            expect(result1.optimalK).toBeGreaterThanOrEqual(1);
            expect(result2.optimalK).toBeGreaterThanOrEqual(1);
        });
    });

    describe('Silhouette Score', () => {
        test('silhouetteScore should return value between -1 and 1', () => {
            const points = [
                [1, 1], [2, 2], [1.5, 1.5],  // Cluster 1
                [8, 8], [9, 9], [8.5, 8.5]   // Cluster 2
            ];
            
            const assignments = [0, 0, 0, 1, 1, 1];
            const means = [[1.5, 1.5], [8.5, 8.5]];
            
            const score = silhouetteScore(points, assignments, means);
            
            expect(typeof score).toBe('number');
            expect(score).toBeGreaterThanOrEqual(-1);
            expect(score).toBeLessThanOrEqual(1);
        });

        test('silhouetteScore should handle perfect clustering', () => {
            const points = [
                [1, 1], [1, 2], [2, 1],  // Perfect cluster 1
                [10, 10], [10, 11], [11, 10]  // Perfect cluster 2
            ];
            
            const assignments = [0, 0, 0, 1, 1, 1];
            const means = [[1.33, 1.33], [10.33, 10.33]];
            
            const score = silhouetteScore(points, assignments, means);
            
            // Should be high for good clustering
            expect(score).toBeGreaterThan(0.5);
        });

        test('silhouetteScore should handle single cluster', () => {
            const points = [[1, 1], [2, 2], [3, 3]];
            const assignments = [0, 0, 0];
            const means = [[2, 2]];
            
            const score = silhouetteScore(points, assignments, means);
            expect(typeof score).toBe('number');
        });
    });

    describe('Cluster Analysis', () => {
        test('analyzeClustering should return comprehensive analysis', () => {
            const points = [
                [1, 1], [2, 2], [3, 3],  // Cluster 1
                [10, 10], [11, 11]       // Cluster 2
            ];
            
            const result = kMeans(points, 2);
            const analysis = analyzeClustering(result);
            
            expect(analysis).toHaveProperty('clusterSizes');
            expect(analysis).toHaveProperty('averageClusterSize');
            expect(analysis).toHaveProperty('clusterErrors');
            expect(analysis).toHaveProperty('silhouetteScore');
            
            expect(Array.isArray(analysis.clusterSizes)).toBe(true);
            expect(typeof analysis.averageClusterSize).toBe('number');
            expect(Array.isArray(analysis.clusterErrors)).toBe(true);
            expect(typeof analysis.silhouetteScore).toBe('number');
            
            expect(analysis.clusterSizes).toHaveLength(2);
            expect(analysis.clusterErrors).toHaveLength(2);
            
            const totalSize = analysis.clusterSizes.reduce((sum, size) => sum + size, 0);
            expect(totalSize).toBe(points.length);
        });
    });

    describe('Example Functions', () => {
        test('examplePoints should be properly formatted', () => {
            expect(examplePoints).toHaveLength(9);
            expect(examplePoints[0]).toHaveLength(2);
            expect(typeof examplePoints[0][0]).toBe('number');
            expect(typeof examplePoints[0][1]).toBe('number');
        });

        test('exampleUsage should run without errors', () => {
            expect(() => exampleUsage()).not.toThrow();
        });
    });

    describe('Edge Cases', () => {
        test('should handle identical points', () => {
            const identicalPoints = [
                [1, 1], [1, 1], [1, 1],
                [5, 5], [5, 5]
            ];
            
            const result = kMeans(identicalPoints, 2);
            expect(result.clusters).toHaveLength(2);
            expect(result.assignments).toHaveLength(5);
        });

        test('should handle high dimensional data', () => {
            const highDimPoints = [
                [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [1.5, 2.5, 3.5, 4.5, 5.5],
                [10, 11, 12, 13, 14], [11, 12, 13, 14, 15]
            ];
            
            const result = kMeans(highDimPoints, 2);
            expect(result.clusters).toHaveLength(2);
            expect(result.assignments).toHaveLength(5);
        });

        test('should handle negative coordinates', () => {
            const negativePoints = [
                [-1, -1], [-2, -2], [-1.5, -1.5],
                [5, 5], [6, 6]
            ];
            
            const result = kMeans(negativePoints, 2);
            expect(result.clusters).toHaveLength(2);
            expect(result.assignments).toHaveLength(5);
        });

        test('should handle very large coordinate values', () => {
            const largePoints = [
                [1e6, 1e6], [1.1e6, 1.1e6],
                [2e6, 2e6], [2.1e6, 2.1e6]
            ];
            
            const result = kMeans(largePoints, 2);
            expect(result.clusters).toHaveLength(2);
            expect(typeof result.totalSquaredError).toBe('number');
        });

        test('should handle single point', () => {
            const singlePoint = [[1, 1]];
            const result = kMeans(singlePoint, 1);
            
            expect(result.clusters).toHaveLength(1);
            expect(result.clusters[0].points).toHaveLength(1);
            expect(result.assignments).toEqual([0]);
        });
    });

    describe('Performance Tests', () => {
        test('should handle moderately large datasets efficiently', () => {
            const largePoints = [];
            for (let i = 0; i < 200; i++) {
                if (i < 100) {
                    largePoints.push([Math.random() * 5, Math.random() * 5]);
                } else {
                    largePoints.push([10 + Math.random() * 5, 10 + Math.random() * 5]);
                }
            }
            
            const start = Date.now();
            const result = kMeans(largePoints, 2, 50);
            const duration = Date.now() - start;
            
            expect(result.clusters).toHaveLength(2);
            expect(result.assignments).toHaveLength(200);
            expect(duration).toBeLessThan(3000); // Should complete within 3 seconds
        });

        test('should converge within reasonable iterations', () => {
            const points = [
                [1, 1], [2, 2], [1.5, 1.5],
                [10, 10], [11, 11], [10.5, 10.5]
            ];
            
            const result = kMeans(points, 2, 100);
            expect(result.iterations).toBeLessThan(50);
        });
    });

    describe('Convergence Tests', () => {
        test('should converge to stable solution', () => {
            const points = [
                [1, 1], [2, 2], [1.5, 1.5],
                [8, 8], [9, 9], [8.5, 8.5]
            ];
            
            const result1 = kMeans(points, 2, 100);
            const result2 = kMeans(points, 2, 100);
            
            // Results should be similar (may differ due to random initialization)
            expect(result1.clusters).toHaveLength(2);
            expect(result2.clusters).toHaveLength(2);
            
            // Total squared error should be similar
            const errorDiff = Math.abs(result1.totalSquaredError - result2.totalSquaredError);
            expect(errorDiff).toBeLessThan(result1.totalSquaredError * 0.1); // Within 10%
        });
    });
});
