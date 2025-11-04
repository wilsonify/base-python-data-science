// Type definitions
export type DataPoint = { features: Record<string, any>; label: boolean };
export type TreeNode = {
    attribute?: string;
    value?: any;
    trueBranch?: TreeNode;
    falseBranch?: TreeNode;
    prediction?: boolean;
};

// Helper function to partition data based on an attribute
function partition<T>(
    data: T[],
    attribute: string,
    value: any
): { true: T[]; false: T[] } {
    const truePartition: T[] = [];
    const falsePartition: T[] = [];

    for (const item of data) {
        if ((item as any)[attribute] === value) {
            truePartition.push(item);
        } else {
            falsePartition.push(item);
        }
    }

    return { true: truePartition, false: falsePartition };
}

// Calculate entropy of a boolean list
function entropy(labels: boolean[]): number {
    const n = labels.length;
    if (n === 0) return 0;

    // Count true and false labels
    let trueCount = 0;
    for (const label of labels) {
        if (label) trueCount++;
    }

    const falseCount = n - trueCount;

    // Calculate probabilities
    const pTrue = trueCount / n;
    const pFalse = falseCount / n;

    // Calculate entropy
    let entropy = 0;
    if (pTrue > 0) entropy -= pTrue * Math.log2(pTrue);
    if (pFalse > 0) entropy -= pFalse * Math.log2(pFalse);

    return entropy;
}

// Calculate information gain from splitting on an attribute
function informationGain(
    data: DataPoint[],
    attribute: string,
    value: any
): number {
    const { true: truePartition, false: falsePartition } = partition(data, attribute, value);
    const n = data.length;
    const nTrue = truePartition.length;
    const nFalse = falsePartition.length;

    if (nTrue === 0 || nFalse === 0) return 0;

    // Calculate entropy before split
    const initialEntropy = entropy(data.map(d => d.label));

    // Calculate weighted entropy after split
    const trueEntropy = entropy(truePartition.map(d => d.label));
    const falseEntropy = entropy(falsePartition.map(d => d.label));

    const weightedEntropy = (nTrue / n) * trueEntropy + (nFalse / n) * falseEntropy;

    return initialEntropy - weightedEntropy;
}

// Find the best attribute to split on
function findBestSplit(
    data: DataPoint[],
    attributes: string[]
): { attribute: string; value: any; gain: number } | null {
    let bestSplit: { attribute: string; value: any; gain: number } | null = null;
    let maxGain = 0;

    for (const attribute of attributes) {
        // Get unique values for this attribute
        const values = new Set<any>();
        for (const point of data) {
            values.add(point.features[attribute]);
        }

        for (const value of values) {
            const gain = informationGain(data, attribute, value);
            if (gain > maxGain) {
                maxGain = gain;
                bestSplit = { attribute, value, gain };
            }
        }
    }

    return bestSplit;
}

// Build a decision tree using ID3 algorithm
function buildTree(
    data: DataPoint[],
    attributes: string[],
    depth: number = 0,
    maxDepth: number = 10
): TreeNode {
    // Base cases
    if (data.length === 0) {
        return { prediction: false }; // Default prediction
    }

    const labels = data.map(d => d.label);
    const uniqueLabels = new Set(labels);

    // If all labels are the same, return a leaf node
    if (uniqueLabels.size === 1) {
        return { prediction: labels[0] };
    }

    // If no attributes left or max depth reached, return majority vote
    if (attributes.length === 0 || depth >= maxDepth) {
        let trueCount = 0;
        for (const label of labels) {
            if (label) trueCount++;
        }
        return { prediction: trueCount > labels.length / 2 };
    }

    // Find the best split
    const bestSplit = findBestSplit(data, attributes);
    if (!bestSplit || bestSplit.gain === 0) {
        // No good split found, return majority vote
        let trueCount = 0;
        for (const label of labels) {
            if (label) trueCount++;
        }
        return { prediction: trueCount > labels.length / 2 };
    }

    // Create the tree node
    const { attribute, value } = bestSplit;
    const { true: truePartition, false: falsePartition } = partition(data, attribute, value);

    // Remaining attributes (remove the one we just used)
    const remainingAttributes = attributes.filter(attr => attr !== attribute);

    // Recursively build subtrees
    const trueBranch = buildTree(truePartition, remainingAttributes, depth + 1, maxDepth);
    const falseBranch = buildTree(falsePartition, remainingAttributes, depth + 1, maxDepth);

    return {
        attribute,
        value,
        trueBranch,
        falseBranch
    };
}

// Classify a data point using a decision tree
export function classify(tree: TreeNode, dataPoint: Record<string, any>): boolean {
    // If we're at a leaf node, return the prediction
    if (tree.prediction !== undefined) {
        return tree.prediction;
    }

    // If we're at an internal node, traverse the tree
    if (tree.attribute !== undefined && tree.value !== undefined) {
        const attributeValue = dataPoint[tree.attribute];
        
        if (attributeValue === tree.value && tree.trueBranch) {
            return classify(tree.trueBranch, dataPoint);
        } else if (tree.falseBranch) {
            return classify(tree.falseBranch, dataPoint);
        }
    }

    // Fallback (shouldn't happen with proper tree construction)
    return false;
}

// Build a decision tree from training data
export function buildDecisionTree(
    data: DataPoint[],
    attributes: string[],
    maxDepth: number = 10
): TreeNode {
    return buildTree(data, attributes, 0, maxDepth);
}

// Print the decision tree (for debugging/visualization)
export function printTree(tree: TreeNode, indent: string = ''): void {
    if (tree.prediction !== undefined) {
        console.log(`${indent}Predict: ${tree.prediction}`);
        return;
    }

    if (tree.attribute !== undefined && tree.value !== undefined) {
        console.log(`${indent}If ${tree.attribute} = ${tree.value}`);
        if (tree.trueBranch) {
            console.log(`${indent}  → True:`);
            printTree(tree.trueBranch, indent + '    ');
        }
        if (tree.falseBranch) {
            console.log(`${indent}  → False:`);
            printTree(tree.falseBranch, indent + '    ');
        }
    }
}

// Calculate tree accuracy
export function treeAccuracy(tree: TreeNode, testData: DataPoint[]): number {
    let correct = 0;
    for (const point of testData) {
        const prediction = classify(tree, point.features);
        if (prediction === point.label) {
            correct++;
        }
    }
    return correct / testData.length;
}

// Random Forest implementation
export class RandomForest {
    private trees: TreeNode[] = [];
    private attributes: string[] = [];
    private numTrees: number = 0;
    private sampleSize: number = 0;

    constructor(numTrees: number = 10, sampleSize: number = 0.7) {
        this.numTrees = numTrees;
        this.sampleSize = sampleSize;
    }

    // Train the random forest
    train(data: DataPoint[], attributes: string[]): void {
        this.attributes = attributes;
        this.trees = [];

        const actualSampleSize = Math.floor(data.length * this.sampleSize);

        for (let i = 0; i < this.numTrees; i++) {
            // Bootstrap sample (sample with replacement)
            const bootstrapSample: DataPoint[] = [];
            for (let j = 0; j < actualSampleSize; j++) {
                const randomIndex = Math.floor(Math.random() * data.length);
                bootstrapSample.push(data[randomIndex]);
            }

            // Random subset of attributes (sqrt(n) for classification)
            const numAttributes = Math.floor(Math.sqrt(attributes.length));
            const shuffledAttributes = [...attributes].sort(() => Math.random() - 0.5);
            const selectedAttributes = shuffledAttributes.slice(0, numAttributes);

            // Build tree
            const tree = buildTree(bootstrapSample, selectedAttributes);
            this.trees.push(tree);
        }
    }

    // Classify using majority vote from all trees
    classify(dataPoint: Record<string, any>): boolean {
        if (this.trees.length === 0) {
            throw new Error('Forest must be trained before classification');
        }

        const votes = this.trees.map(tree => classify(tree, dataPoint));
        const trueVotes = votes.filter(vote => vote).length;
        return trueVotes > votes.length / 2;
    }

    // Get forest information
    getInfo(): { numTrees: number; attributes: string[]; isTrained: boolean } {
        return {
            numTrees: this.trees.length,
            attributes: this.attributes,
            isTrained: this.trees.length > 0
        };
    }
}

// Example usage data
export const exampleData: DataPoint[] = [
    { features: { level: 'Senior', lang: 'Java', tweets: 'no', phd: 'no' }, label: true },
    { features: { level: 'Senior', lang: 'Java', tweets: 'no', phd: 'yes' }, label: false },
    { features: { level: 'Mid', lang: 'Java', tweets: 'no', phd: 'no' }, label: true },
    { features: { level: 'Junior', lang: 'Python', tweets: 'no', phd: 'no' }, label: false },
    { features: { level: 'Junior', lang: 'R', tweets: 'yes', phd: 'no' }, label: true },
    { features: { level: 'Junior', lang: 'R', tweets: 'yes', phd: 'yes' }, label: false },
    { features: { level: 'Mid', lang: 'R', tweets: 'yes', phd: 'yes' }, label: true },
    { features: { level: 'Senior', lang: 'Python', tweets: 'no', phd: 'no' }, label: false },
    { features: { level: 'Senior', lang: 'R', tweets: 'yes', phd: 'no' }, label: true },
    { features: { level: 'Junior', lang: 'Python', tweets: 'yes', phd: 'no' }, label: true },
    { features: { level: 'Senior', lang: 'Python', tweets: 'yes', phd: 'yes' }, label: true },
    { features: { level: 'Mid', lang: 'Python', tweets: 'no', phd: 'yes' }, label: true },
    { features: { level: 'Mid', lang: 'Java', tweets: 'yes', phd: 'no' }, label: true },
    { features: { level: 'Junior', lang: 'Python', tweets: 'no', phd: 'yes' }, label: false }
];

export const candidateAttributes = ['level', 'lang', 'tweets', 'phd'];

// Example usage
export function exampleUsage(): void {
    console.log('Decision Tree Example:');
    
    // Build and test a decision tree
    const tree = buildDecisionTree(exampleData, candidateAttributes);
    console.log('\nDecision Tree Structure:');
    printTree(tree);

    // Test classification
    const testCases = [
        { level: 'Junior', lang: 'Java', tweets: 'yes', phd: 'no' },
        { level: 'Senior', lang: 'Python', tweets: 'no', phd: 'yes' }
    ];

    console.log('\nClassification Results:');
    for (const testCase of testCases) {
        const prediction = classify(tree, testCase);
        console.log(`${JSON.stringify(testCase)} -> ${prediction ? 'YES' : 'NO'}`);
    }

    // Random Forest example
    console.log('\nRandom Forest Example:');
    const forest = new RandomForest(5, 0.8);
    forest.train(exampleData, candidateAttributes);
    
    console.log('Forest Info:', forest.getInfo());
    
    for (const testCase of testCases) {
        const prediction = forest.classify(testCase);
        console.log(`${JSON.stringify(testCase)} -> ${prediction ? 'YES' : 'NO'}`);
    }
}
