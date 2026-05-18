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

// Helper: initialize means by choosing k distinct random points
function initializeRandomMeans(points: Point[], k: number): Point[] {
    const out: Point[] = [];
    const used = new Set<number>();
    while (out.length < k) {
        const idx = Math.floor(Math.random() * points.length);
        if (!used.has(idx)) {
            out.push([...points[idx]]);
            used.add(idx);
        }
    }
    return out;
}

// Helper: check convergence between two mean sets
function hasConverged(oldMeans: Point[], newMeans: Point[], tol = 0.0001): boolean {
    for (let i = 0; i < oldMeans.length; i++) {
        if (distance(oldMeans[i], newMeans[i]) > tol) return false;
    }
    return true;
}

// Helpers for silhouette computations moved to top-level to reduce nesting
function averageDistanceToCluster(point: Point, clusterId: number, points: Point[], assignments: number[]): number {
    let total = 0;
    let count = 0;
    for (let j = 0; j < points.length; j++) {
        if (assignments[j] === clusterId) {
            total += distance(point, points[j]);
            count++;
        }
    }
    return count > 0 ? total / count : 0;
}

function minAverageDistanceToOtherClusters(point: Point, clusterId: number, points: Point[], assignments: number[], means: Point[]): number {
    let minAvg = Infinity;
    for (let k = 0; k < means.length; k++) {
        if (k === clusterId) continue;
        const avg = averageDistanceToCluster(point, k, points, assignments);
        if (avg < minAvg) minAvg = avg;
    }
    return minAvg;
}

// Assign each point to the nearest cluster centroid
function assignPointsToClusters(points: Point[], means: Point[]): number[] {
    const assignments: number[] = [];
    
    for (const point of points) {
        assignments.push(_closestClusterIndex(point, means));
    }
    
    return assignments;
}


// Helper: return index of closest mean for a single point
function _closestClusterIndex(point: Point, means: Point[]): number {
    let minDistance = Infinity;
    let closestCluster = 0;
    for (let i = 0; i < means.length; i++) {
        const dist = distance(point, means[i]);
        if (dist < minDistance) {
            minDistance = dist;
            closestCluster = i;
        }
    }
    return closestCluster;
}

// Calculate new cluster means based on current assignments
// Group points by cluster assignment
function buildClusters(points: Point[], assignments: number[], k: number): Point[][] {
    const clusters: Point[][] = new Array(k).fill(null).map(() => []);
    for (let i = 0; i < points.length; i++) {
        const clusterId = assignments[i];
        clusters[clusterId].push(points[i]);
    }
    return clusters;
}

// Calculate new cluster means based on current assignments. If a cluster has no
// points assigned, preserve the old mean when provided (reduces oscillation and
// keeps behaviour predictable while avoiding large nested conditionals).
function calculateNewMeans(points: Point[], assignments: number[], k: number, oldMeans?: Point[]): Point[] {
    const clusters = buildClusters(points, assignments, k);
    const newMeans: Point[] = [];

    for (let i = 0; i < k; i++) {
        if (clusters[i].length > 0) {
            newMeans.push(vector_mean(clusters[i]));
        } else if (oldMeans?.[i]) {
            newMeans.push(oldMeans[i]);
        } else {
            newMeans.push(new Array(points[0].length).fill(0));
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
    
    // Initialize means (randomly select k points as initial centroids)
    let means: Point[] = initializeRandomMeans(points, k);

    // Initialize assignments if provided, otherwise assign to nearest
    let assignments = initialAssignments || assignPointsToClusters(points, means);

    // Run k-means iterations in a helper to reduce cognitive complexity of kMeans
    const loopResult = runKMeansLoop(points, k, maxIterations, means, assignments);
    assignments = loopResult.assignments;
    means = loopResult.means;
    const iterations = loopResult.iterations;
    
    // Calculate final error
    const totalSquaredError = calculateTotalSquaredError(points, assignments, means);
    
    // Organize results into clusters
    const clusters = _buildResultClusters(points, assignments, means);
    
    return {
        clusters,
        assignments,
        means,
        totalSquaredError,
        iterations
    };
}

// Helper: build Cluster[] from points, assignments and means (used by kMeans)
function _buildResultClusters(points: Point[], assignments: number[], means: Point[]): Cluster[] {
    const k = means.length;
    const clusters: Cluster[] = new Array(k).fill(null).map((_, i) => ({
        centroid: means[i],
        points: [],
        id: i
    }));

    for (let i = 0; i < points.length; i++) {
        const clusterId = assignments[i];
        clusters[clusterId].points.push(points[i]);
    }

    return clusters;
}


// Run the main K-means iteration loop. Extracted to keep `kMeans` small.
function runKMeansLoop(points: Point[], k: number, maxIterations: number, means: Point[], assignments: number[]) {
    let iterations = 0;
    for (let iter = 0; iter < maxIterations; iter++) {
        const step = _kMeansIterationStep(points, k, means, assignments);
        means = step.means;
        assignments = step.assignments;
        iterations = step.iterations;

        if (step.converged) break;
    }

    return { assignments, means, iterations };
}


// Helper: perform one iteration step for k-means (compute new means, assignments and whether converged)
function _kMeansIterationStep(points: Point[], k: number, means: Point[], assignments: number[]) {
    const newMeans = calculateNewMeans(points, assignments, k, means);
    const newAssignments = assignPointsToClusters(points, newMeans);
    const converged = hasConverged(means, newMeans);
    const iterations = converged ? 0 : 1; // single-step iteration indicator; caller accumulates
    return { means: newMeans, assignments: newAssignments, converged, iterations };
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
        const minError = _runKAndReturnBestError(points, k, runsPerK);
        errors.push(minError);
    }

    const elbowPoint = _detectElbowPoint(errors);

    return {
        optimalK: elbowPoint,
        errors,
        elbowPoint
    };
}


// Helper: run k-means multiple times for a single k and return the best (minimum) error
function _runKAndReturnBestError(points: Point[], k: number, runsPerK: number): number {
    let minError = Infinity;
    for (let run = 0; run < runsPerK; run++) {
        const result = kMeans(points, k);
        if (result.totalSquaredError < minError) {
            minError = result.totalSquaredError;
        }
    }
    return minError === Infinity ? 0 : minError;
}


// Helper: detect elbow point from errors array using the existing heuristic
function _detectElbowPoint(errors: number[]): number {
    if (errors.length === 0) return 1;
    let elbowPoint = 1;
    let maxImprovement = 0;

    for (let i = 1; i < errors.length - 1; i++) {
        const improvement1 = errors[i - 1] - errors[i];
        const improvement2 = errors[i] - errors[i + 1];
        // protect against division by zero
        const relativeImprovement = improvement2 === 0 ? improvement1 : improvement1 / improvement2;

        if (relativeImprovement > maxImprovement) {
            maxImprovement = relativeImprovement;
            elbowPoint = i + 1; // +1 because k starts at 1
        }
    }

    return elbowPoint;
}

// Calculate silhouette score for clustering quality
export function silhouetteScore(points: Point[], assignments: number[], means: Point[]): number {
    let totalScore = 0;
    for (let i = 0; i < points.length; i++) {
        const point = points[i];
        const clusterId = assignments[i];

        const a = averageDistanceToCluster(point, clusterId, points, assignments);
        const b = minAverageDistanceToOtherClusters(point, clusterId, points, assignments, means);

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
    const clusterErrors = _computeAllClusterErrors(result);

    // Calculate all points for silhouette score
    const allPoints = _flattenClusterPoints(result);

    const silhouetteValue = silhouetteScore(allPoints, result.assignments, result.means);
    
    return {
        clusterSizes,
        averageClusterSize,
        clusterErrors,
        silhouetteScore: silhouetteValue
    };
}


// Helper: compute total squared error for a single cluster
function _computeClusterError(cluster: Cluster): number {
    let clusterError = 0;
    for (const point of cluster.points) {
        clusterError += squared_distance(point, cluster.centroid);
    }
    return clusterError;
}

// Helper: compute errors for all clusters in a result
function _computeAllClusterErrors(result: KMeansResult): number[] {
    const errors: number[] = [];
    for (const cluster of result.clusters) {
        errors.push(_computeClusterError(cluster));
    }
    return errors;
}

// Helper: flatten cluster points into a single array (preserves order)
function _flattenClusterPoints(result: KMeansResult): Point[] {
    const allPoints: Point[] = [];
    for (const cluster of result.clusters) {
        allPoints.push(...cluster.points);
    }
    return allPoints;
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
    printBasicClusteringResults(result);

    // Find optimal k
    console.log('\nFinding Optimal K:');
    const optimalKResult = findOptimalK(examplePoints, 6, 3);
    printOptimalKResults(optimalKResult);

    // Cluster analysis
    console.log('\nCluster Analysis:');
    const analysis = analyzeClustering(result);
    printAnalysisResults(analysis);
}

// Printing helpers to keep exampleUsage small and reduce complexity
function printBasicClusteringResults(result: KMeansResult): void {
    console.log(`Total Squared Error: ${result.totalSquaredError.toFixed(4)}`);
    console.log(`Iterations: ${result.iterations}`);
    
    result.clusters.forEach((cluster, i) => {
        console.log(`\nCluster ${i}:`);
        console.log(`  Centroid: [${cluster.centroid.map(v => v.toFixed(2)).join(', ')}]`);
        console.log(`  Size: ${cluster.points.length}`);
        console.log(`  Points: [${cluster.points.map(p => `[${p.join(', ')}]`).join(', ')}]`);
    });
}

function printOptimalKResults(opt: { optimalK: number; errors: number[]; elbowPoint: number; }): void {
    console.log(`Optimal K: ${opt.optimalK}`);
    console.log(`Errors by K: ${opt.errors.map(e => e.toFixed(2)).join(', ')}`);
}

function printAnalysisResults(analysis: { clusterSizes: number[]; averageClusterSize: number; clusterErrors: number[]; silhouetteScore: number; }): void {
    console.log(`Cluster Sizes: ${analysis.clusterSizes.join(', ')}`);
    console.log(`Average Cluster Size: ${analysis.averageClusterSize.toFixed(2)}`);
    console.log(`Silhouette Score: ${analysis.silhouetteScore.toFixed(4)}`);
}
