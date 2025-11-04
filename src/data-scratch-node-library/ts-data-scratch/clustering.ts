import { vector_mean, distance, squared_distance } from './linear_algebra';

// Type definitions
export type Point = number[];
export type Cluster = {
    centroid: Point;
    points: Point[];
    id: number;
};
export type KMeansResult = {
    clusters: Cluster[];
    assignments: number[];
    means: Point[];
    totalSquaredError: number;
    iterations: number;
};

// Assign each point to the nearest cluster centroid
function assignPointsToClusters(points: Point[], means: Point[]): number[] {
    const assignments: number[] = [];
    
    for (const point of points) {
        let minDistance = Infinity;
        let closestCluster = 0;
        
        for (let i = 0; i < means.length; i++) {
            const dist = distance(point, means[i]);
            if (dist < minDistance) {
                minDistance = dist;
                closestCluster = i;
            }
        }
        
        assignments.push(closestCluster);
    }
    
    return assignments;
}

// Calculate new cluster means based on current assignments
function calculateNewMeans(points: Point[], assignments: number[], k: number): Point[] {
    const clusters: Point[][] = Array(k).fill(null).map(() => []);
    
    // Group points by cluster assignment
    for (let i = 0; i < points.length; i++) {
        const clusterId = assignments[i];
        clusters[clusterId].push(points[i]);
    }
    
    // Calculate mean for each cluster
    const newMeans: Point[] = [];
    for (let i = 0; i < k; i++) {
        if (clusters[i].length > 0) {
            const mean = vector_mean(clusters[i]);
            newMeans.push(mean);
        } else {
            // If no points assigned to cluster, keep the old mean or reinitialize
            newMeans.push(Array(points[0].length).fill(0));
        }
    }
    
    return newMeans;
}

// Calculate total squared error for clustering
function calculateTotalSquaredError(points: Point[], assignments: number[], means: Point[]): number {
    let totalError = 0;
    
    for (let i = 0; i < points.length; i++) {
        const clusterId = assignments[i];
        totalError += squared_distance(points[i], means[clusterId]);
    }
    
    return totalError;
}

// K-means clustering algorithm
export function kMeans(
    points: Point[],
    k: number,
    maxIterations: number = 100,
    initialAssignments?: number[]
): KMeansResult {
    if (points.length === 0) {
        throw new Error('Cannot cluster empty dataset');
    }
    
    if (k <= 0) {
        throw new Error('Number of clusters must be positive');
    }
    
    if (k > points.length) {
        throw new Error('Number of clusters cannot exceed number of points');
    }
    
    const dimensions = points[0].length;
    
    // Initialize means (randomly select k points as initial centroids)
    let means: Point[] = [];
    const usedIndices = new Set<number>();
    
    while (means.length < k) {
        const randomIndex = Math.floor(Math.random() * points.length);
        if (!usedIndices.has(randomIndex)) {
            means.push([...points[randomIndex]]);
            usedIndices.add(randomIndex);
        }
    }
    
    // Initialize assignments if provided, otherwise assign to nearest
    let assignments = initialAssignments || assignPointsToClusters(points, means);
    
    let iterations = 0;
    let converged = false;
    
    while (!converged && iterations < maxIterations) {
        // Calculate new means based on current assignments
        const newMeans = calculateNewMeans(points, assignments, k);
        
        // Check for convergence (means don't change significantly)
        let meansChanged = false;
        for (let i = 0; i < k; i++) {
            const dist = distance(means[i], newMeans[i]);
            if (dist > 0.0001) { // Threshold for convergence
                meansChanged = true;
                break;
            }
        }
        
        if (!meansChanged) {
            converged = true;
        } else {
            means = newMeans;
            assignments = assignPointsToClusters(points, means);
            iterations++;
        }
    }
    
    // Calculate final error
    const totalSquaredError = calculateTotalSquaredError(points, assignments, means);
    
    // Organize results into clusters
    const clusters: Cluster[] = Array(k).fill(null).map((_, i) => ({
        centroid: means[i],
        points: [],
        id: i
    }));
    
    for (let i = 0; i < points.length; i++) {
        const clusterId = assignments[i];
        clusters[clusterId].points.push(points[i]);
    }
    
    return {
        clusters,
        assignments,
        means,
        totalSquaredError,
        iterations
    };
}

// Run k-means multiple times and return the best result
export function kMeansMultipleRuns(
    points: Point[],
    k: number,
    numRuns: number = 10,
    maxIterations: number = 100
): KMeansResult {
    let bestResult: KMeansResult | null = null;
    let minError = Infinity;
    
    for (let run = 0; run < numRuns; run++) {
        const result = kMeans(points, k, maxIterations);
        if (result.totalSquaredError < minError) {
            minError = result.totalSquaredError;
            bestResult = result;
        }
    }
    
    return bestResult!;
}

// Find optimal number of clusters using elbow method
export function findOptimalK(
    points: Point[],
    maxK: number = 10,
    runsPerK: number = 5
): {
    optimalK: number;
    errors: number[];
    elbowPoint: number;
} {
    const errors: number[] = [];
    
    for (let k = 1; k <= maxK; k++) {
        let minError = Infinity;
        
        // Run k-means multiple times and take the best error
        for (let run = 0; run < runsPerK; run++) {
            const result = kMeans(points, k);
            if (result.totalSquaredError < minError) {
                minError = result.totalSquaredError;
            }
        }
        
        errors.push(minError);
    }
    
    // Find elbow point using simple heuristic
    let elbowPoint = 1;
    let maxImprovement = 0;
    
    for (let i = 1; i < errors.length - 1; i++) {
        const improvement1 = errors[i - 1] - errors[i];
        const improvement2 = errors[i] - errors[i + 1];
        const relativeImprovement = improvement1 / improvement2;
        
        if (relativeImprovement > maxImprovement) {
            maxImprovement = relativeImprovement;
            elbowPoint = i + 1; // +1 because k starts at 1
        }
    }
    
    return {
        optimalK: elbowPoint,
        errors,
        elbowPoint
    };
}

// Calculate silhouette score for clustering quality
export function silhouetteScore(points: Point[], assignments: number[], means: Point[]): number {
    let totalScore = 0;
    
    for (let i = 0; i < points.length; i++) {
        const point = points[i];
        const clusterId = assignments[i];
        
        // Calculate a: average distance to points in same cluster
        let sameClusterDistances = 0;
        let sameClusterCount = 0;
        
        for (let j = 0; j < points.length; j++) {
            if (i !== j && assignments[j] === clusterId) {
                sameClusterDistances += distance(point, points[j]);
                sameClusterCount++;
            }
        }
        
        const a = sameClusterCount > 0 ? sameClusterDistances / sameClusterCount : 0;
        
        // Calculate b: minimum average distance to points in other clusters
        let minOtherClusterDistance = Infinity;
        
        for (let k = 0; k < means.length; k++) {
            if (k !== clusterId) {
                let otherClusterDistances = 0;
                let otherClusterCount = 0;
                
                for (let j = 0; j < points.length; j++) {
                    if (assignments[j] === k) {
                        otherClusterDistances += distance(point, points[j]);
                        otherClusterCount++;
                    }
                }
                
                if (otherClusterCount > 0) {
                    const avgDistance = otherClusterDistances / otherClusterCount;
                    if (avgDistance < minOtherClusterDistance) {
                        minOtherClusterDistance = avgDistance;
                    }
                }
            }
        }
        
        const b = minOtherClusterDistance;
        
        // Calculate silhouette score for this point
        const silhouette = b > a ? (b - a) / Math.max(a, b) : 0;
        totalScore += silhouette;
    }
    
    return totalScore / points.length;
}

// Cluster analysis utilities
export function analyzeClustering(result: KMeansResult): {
    clusterSizes: number[];
    averageClusterSize: number;
    clusterErrors: number[];
    silhouetteScore: number;
} {
    const clusterSizes = result.clusters.map(cluster => cluster.points.length);
    const averageClusterSize = clusterSizes.reduce((a, b) => a + b, 0) / clusterSizes.length;
    
    // Calculate error for each cluster
    const clusterErrors: number[] = [];
    for (let i = 0; i < result.clusters.length; i++) {
        const cluster = result.clusters[i];
        let clusterError = 0;
        
        for (const point of cluster.points) {
            clusterError += squared_distance(point, cluster.centroid);
        }
        
        clusterErrors.push(clusterError);
    }
    
    // Calculate all points for silhouette score
    const allPoints: Point[] = [];
    for (const cluster of result.clusters) {
        allPoints.push(...cluster.points);
    }
    
    const silhouetteValue = silhouetteScore(allPoints, result.assignments, result.means);
    
    return {
        clusterSizes,
        averageClusterSize,
        clusterErrors,
        silhouetteScore: silhouetteValue
    };
}

// Example usage data
export const examplePoints: Point[] = [
    [1, 2], [1, 4], [1, 0],
    [10, 2], [10, 4], [10, 0],
    [5, 8], [5, 10], [5, 6]
];

// Example usage
export function exampleUsage(): void {
    console.log('K-Means Clustering Example:');
    
    // Basic k-means
    const result = kMeans(examplePoints, 3);
    console.log('\nClustering Results:');
    console.log(`Total Squared Error: ${result.totalSquaredError.toFixed(4)}`);
    console.log(`Iterations: ${result.iterations}`);
    
    result.clusters.forEach((cluster, i) => {
        console.log(`\nCluster ${i}:`);
        console.log(`  Centroid: [${cluster.centroid.map(v => v.toFixed(2)).join(', ')}]`);
        console.log(`  Size: ${cluster.points.length}`);
        console.log(`  Points: [${cluster.points.map(p => `[${p.join(', ')}]`).join(', ')}]`);
    });
    
    // Find optimal k
    console.log('\nFinding Optimal K:');
    const optimalKResult = findOptimalK(examplePoints, 6, 3);
    console.log(`Optimal K: ${optimalKResult.optimalK}`);
    console.log(`Errors by K: ${optimalKResult.errors.map(e => e.toFixed(2)).join(', ')}`);
    
    // Cluster analysis
    console.log('\nCluster Analysis:');
    const analysis = analyzeClustering(result);
    console.log(`Cluster Sizes: ${analysis.clusterSizes.join(', ')}`);
    console.log(`Average Cluster Size: ${analysis.averageClusterSize.toFixed(2)}`);
    console.log(`Silhouette Score: ${analysis.silhouetteScore.toFixed(4)}`);
}
