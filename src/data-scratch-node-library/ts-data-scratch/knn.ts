import { distance } from './linear_algebra';

// Type definitions
type LabeledPoint<T> = { point: number[], label: T };
type VoteCounter<T> = Map<T, number>;

// Helper function to count votes
function countVotes<T>(labels: T[]): VoteCounter<T> {
    const votes: VoteCounter<T> = new Map();
    
    for (const label of labels) {
        const count = votes.get(label) || 0;
        votes.set(label, count + 1);
    }
    
    return votes;
}

// Raw majority vote - returns the label with the most votes
export function rawMajorityVote<T>(labels: T[]): T {
    const votes = countVotes(labels);
    let winner: T | undefined;
    let maxCount = 0;
    
    for (const [label, count] of votes.entries()) {
        if (count > maxCount) {
            maxCount = count;
            winner = label;
        }
    }
    
    return winner!;
}

// Majority vote with tie-breaking
export function majorityVote<T>(labels: T[]): T {
    // assumes that labels are ordered from nearest to farthest
    const voteCounts = countVotes(labels);
    
    // Find the label(s) with the highest vote count
    let maxCount = 0;
    for (const count of voteCounts.values()) {
        if (count > maxCount) {
            maxCount = count;
        }
    }
    
    // Count how many labels have the max count
    const winners: T[] = [];
    for (const [label, count] of voteCounts.entries()) {
        if (count === maxCount) {
            winners.push(label);
        }
    }
    
    if (winners.length === 1) {
        return winners[0]; // unique winner
    } else {
        // try again without the farthest (recursive tie-breaking)
        return majorityVote(labels.slice(0, -1));
    }
}

// K-Nearest Neighbors classification
export function knnClassify<T>(
    k: number,
    labeledPoints: LabeledPoint<T>[],
    newPoint: number[]
): T {
    // each labeled point should be a pair (point, label)
    
    // order the labeled points from nearest to farthest
    const byDistance = [...labeledPoints].sort((a, b) => 
        distance(a.point, newPoint) - distance(b.point, newPoint)
    );
    
    // find the labels for the k closest
    const kNearestLabels = byDistance
        .slice(0, k)
        .map(labeledPoint => labeledPoint.label);
    
    // and let them vote
    return majorityVote(kNearestLabels);
}

// Enhanced KNN with distance information
export function knnClassifyWithDistance<T>(
    k: number,
    labeledPoints: LabeledPoint<T>[],
    newPoint: number[]
): { prediction: T; distances: number[]; neighbors: LabeledPoint<T>[] } {
    // order the labeled points from nearest to farthest
    const byDistance = [...labeledPoints].sort((a, b) => 
        distance(a.point, newPoint) - distance(b.point, newPoint)
    );
    
    // get the k closest neighbors
    const kNearestNeighbors = byDistance.slice(0, k);
    const distances = kNearestNeighbors.map(neighbor => 
        distance(neighbor.point, newPoint)
    );
    const kNearestLabels = kNearestNeighbors.map(neighbor => neighbor.label);
    
    return {
        prediction: majorityVote(kNearestLabels),
        distances,
        neighbors: kNearestNeighbors
    };
}

// Weighted KNN (closer neighbors have more influence)
export function weightedKnnClassify<T>(
    k: number,
    labeledPoints: LabeledPoint<T>[],
    newPoint: number[]
): T {
    // order the labeled points from nearest to farthest
    const byDistance = [...labeledPoints].sort((a, b) => 
        distance(a.point, newPoint) - distance(b.point, newPoint)
    );
    
    // get the k closest neighbors
    const kNearestNeighbors = byDistance.slice(0, k);
    
    // calculate weighted votes (inverse distance weighting)
    const weightedVotes: VoteCounter<T> = new Map();
    
    for (const neighbor of kNearestNeighbors) {
        const dist = distance(neighbor.point, newPoint);
        // Avoid division by zero
        const weight = dist === 0 ? 1 : 1 / (dist + 1e-10);
        const currentWeight = weightedVotes.get(neighbor.label) || 0;
        weightedVotes.set(neighbor.label, currentWeight + weight);
    }
    
    // Find the label with the highest total weight
    let winner: T | undefined;
    let maxWeight = 0;
    
    for (const [label, weight] of weightedVotes.entries()) {
        if (weight > maxWeight) {
            maxWeight = weight;
            winner = label;
        }
    }
    
    return winner!;
}

// Cross-validation for KNN
export function knnCrossValidate<T>(
    k: number,
    labeledPoints: LabeledPoint<T>[],
    folds: number = 5
): number {
    // Shuffle the data
    const shuffled = [...labeledPoints].sort(() => Math.random() - 0.5);
    const foldSize = Math.floor(shuffled.length / folds);
    let correctPredictions = 0;
    
    for (let i = 0; i < folds; i++) {
        // Create train/test split for this fold
        const testStart = i * foldSize;
        const testEnd = (i + 1) * foldSize;
        
        const testSet = shuffled.slice(testStart, testEnd);
        const trainSet = [
            ...shuffled.slice(0, testStart),
            ...shuffled.slice(testEnd)
        ];
        
        // Test on this fold
        for (const testPoint of testSet) {
            const prediction = knnClassify(k, trainSet, testPoint.point);
            if (prediction === testPoint.label) {
                correctPredictions++;
            }
        }
    }
    
    return correctPredictions / shuffled.length;
}

// Find optimal k using cross-validation
export function findOptimalK<T>(
    labeledPoints: LabeledPoint<T>[],
    maxK: number = 20,
    folds: number = 5
): { optimalK: number; accuracies: number[] } {
    const accuracies: number[] = [];
    
    for (let k = 1; k <= maxK; k++) {
        const accuracy = knnCrossValidate(k, labeledPoints, folds);
        accuracies.push(accuracy);
    }
    
    // Find k with highest accuracy
    let optimalK = 1;
    let maxAccuracy = accuracies[0];
    
    for (let i = 1; i < accuracies.length; i++) {
        if (accuracies[i] > maxAccuracy) {
            maxAccuracy = accuracies[i];
            optimalK = i + 1; // k = i + 1 because we start from k=1
        }
    }
    
    return { optimalK, accuracies };
}

// Example usage with cities data
export const cities = [
    { point: [-86.75, 33.5666666666667], label: "Python" },
    { point: [-88.25, 30.6833333333333], label: "Python" },
    { point: [-112.016666666667, 33.4333333333333], label: "Java" },
    { point: [-110.933333333333, 32.1166666666667], label: "Java" },
    { point: [-92.2333333333333, 34.7333333333333], label: "R" },
    { point: [-121.95, 37.7], label: "R" },
    { point: [-118.15, 33.8166666666667], label: "Python" },
    { point: [-118.233333333333, 34.05], label: "Python" },
    { point: [-122.416666666667, 37.7833333333333], label: "R" },
    { point: [-87.6833333333333, 41.8333333333333], label: "Java" },
    { point: [-84.4333333333333, 33.65], label: "Python" },
    { point: [-116.216666666667, 43.6166666666667], label: "Java" },
    { point: [-95.9333333333333, 36.1166666666667], label: "R" },
    { point: [-96.7833333333333, 32.7833333333333], label: "Python" },
    { point: [-89.6333333333333, 41.85], label: "Java" },
    { point: [-104.716666666667, 38.8166666666667], label: "Python" },
    { point: [-94.6, 39.1166666666667], label: "Java" },
    { point: [-96.7, 32.7833333333333], label: "Python" },
    { point: [-122.35, 47.6166666666667], label: "Python" },
    { point: [-95.35, 29.9666666666667], label: "Java" }
];

// Predict which language a new city might prefer
export function predictLanguageForCity(longitude: number, latitude: number): string {
    return knnClassify(3, cities, [longitude, latitude]);
}
