import { dot } from './linear_algebra';

// Type definitions
export type Layer = [number[], number]; // [weights, bias]
export type NeuralNetwork = Layer[];
export type TrainingData = { inputs: number[]; target: number[] }[];

// Activation functions
export function sigmoid(x: number): number {
    return 1 / (1 + Math.exp(-x));
}

export function sigmoidDerivative(x: number): number {
    const s = sigmoid(x);
    return s * (1 - s);
}

export function stepFunction(x: number): number {
    return x >= 0 ? 1 : 0;
}

export function tanh(x: number): number {
    return Math.tanh(x);
}

export function tanhDerivative(x: number): number {
    const t = tanh(x);
    return 1 - t * t;
}

export function relu(x: number): number {
    return Math.max(0, x);
}

export function reluDerivative(x: number): number {
    return x > 0 ? 1 : 0;
}

// Perceptron
export function perceptron(weights: number[], bias: number, inputs: number[]): number {
    const weightedSum = dot(weights, inputs) + bias;
    return stepFunction(weightedSum);
}

// Single neuron with sigmoid activation
export function neuron(weights: number[], inputs: number[]): number {
    const weightedSum = dot(weights, inputs);
    return sigmoid(weightedSum);
}

// Feed-forward propagation
export function feedForward(network: NeuralNetwork, inputs: number[]): {
    outputs: number[][];
    finalOutput: number[];
} {
    const outputs: number[][] = [inputs];
    let currentInput = inputs;

    for (const [weights, bias] of network) {
        const weightedSum = dot(weights, currentInput) + bias;
        const output = sigmoid(weightedSum);
        outputs.push([output]); // Store as array to maintain consistency
        currentInput = [output]; // Pass as array to next layer
    }

    return {
        outputs,
        finalOutput: currentInput
    };
}

// Backpropagation algorithm
export function backpropagation(
    network: NeuralNetwork,
    inputs: number[],
    target: number[]
): {
    gradients: NeuralNetwork;
    output: number[];
    error: number;
} {
    // Forward pass
    const { outputs, finalOutput } = feedForward(network, inputs);
    
    // Calculate output layer error (delta)
    const outputLayer = network[network.length - 1];
    const outputDelta: number[] = [];
    
    for (let i = 0; i < finalOutput.length; i++) {
        const error = target[i] - finalOutput[i];
        const delta = error * sigmoidDerivative(finalOutput[i]);
        outputDelta.push(delta);
    }
    
    // Initialize gradients
    const gradients: NeuralNetwork = [];
    
    // Calculate output layer gradients
    const outputWeightsGradient: number[] = [];
    const prevOutput = outputs[outputs.length - 2];
    
    for (let i = 0; i < outputLayer[0].length; i++) {
        let weightGradient = 0;
        for (let j = 0; j < outputDelta.length; j++) {
            weightGradient += outputDelta[j] * prevOutput[i];
        }
        outputWeightsGradient.push(weightGradient);
    }
    
    const outputBiasGradient = outputDelta.reduce((sum, delta) => sum + delta, 0);
    gradients.push([outputWeightsGradient, outputBiasGradient]);
    
    // Backpropagate through hidden layers
    let currentDelta = outputDelta;
    
    for (let layerIdx = network.length - 2; layerIdx >= 0; layerIdx--) {
        const layer = network[layerIdx];
        const layerOutput = outputs[layerIdx + 1];
        const prevOutput = outputs[layerIdx];
        
        // Calculate delta for this layer
        const nextLayerWeights = network[layerIdx + 1][0];
        const layerDelta: number[] = [];
        
        for (let i = 0; i < layerOutput.length; i++) {
            let error = 0;
            for (let j = 0; j < currentDelta.length; j++) {
                error += currentDelta[j] * nextLayerWeights[j];
            }
            const delta = error * sigmoidDerivative(layerOutput[i]);
            layerDelta.push(delta);
        }
        
        // Calculate weight gradients for this layer
        const weightsGradient: number[] = [];
        for (let i = 0; i < layer[0].length; i++) {
            let weightGradient = 0;
            for (let j = 0; j < layerDelta.length; j++) {
                weightGradient += layerDelta[j] * prevOutput[i];
            }
            weightsGradient.push(weightGradient);
        }
        
        const biasGradient = layerDelta.reduce((sum, delta) => sum + delta, 0);
        gradients.unshift([weightsGradient, biasGradient]);
        
        currentDelta = layerDelta;
    }
    
    // Calculate total error
    const error = target.reduce((sum, targetVal, i) => {
        return sum + Math.pow(targetVal - finalOutput[i], 2);
    }, 0) / 2;
    
    return {
        gradients,
        output: finalOutput,
        error
    };
}

// Update network weights using gradients
export function updateWeights(
    network: NeuralNetwork,
    gradients: NeuralNetwork,
    learningRate: number
): NeuralNetwork {
    const updatedNetwork: NeuralNetwork = [];
    
    for (let i = 0; i < network.length; i++) {
        const [weights, bias] = network[i];
        const [weightGradients, biasGradient] = gradients[i];
        
        const updatedWeights = weights.map((weight, j) => 
            weight + learningRate * weightGradients[j]
        );
        
        const updatedBias = bias + learningRate * biasGradient;
        
        updatedNetwork.push([updatedWeights, updatedBias]);
    }
    
    return updatedNetwork;
}

// Simple neural network training
export function trainSimpleNetwork(
    trainingData: TrainingData,
    hiddenNeurons: number = 2,
    learningRate: number = 0.1,
    epochs: number = 1000
): {
    network: NeuralNetwork;
    finalError: number;
    errors: number[];
} {
    if (trainingData.length === 0) {
        throw new Error('Training data cannot be empty');
    }
    
    const inputSize = trainingData[0].inputs.length;
    const outputSize = trainingData[0].target.length;
    
    // Initialize network with random weights
    const network: NeuralNetwork = [
        [
            Array(hiddenNeurons).fill(0).map(() => Math.random() * 2 - 1),
            Math.random() * 2 - 1
        ],
        [
            Array(outputSize).fill(0).map(() => Math.random() * 2 - 1),
            Math.random() * 2 - 1
        ]
    ];
    
    const errors: number[] = [];
    let currentNetwork = network;
    
    // Training loop
    for (let epoch = 0; epoch < epochs; epoch++) {
        let totalError = 0;
        
        // Train on each example
        for (const example of trainingData) {
            const { gradients, error } = backpropagation(
                currentNetwork,
                example.inputs,
                example.target
            );
            
            currentNetwork = updateWeights(currentNetwork, gradients, learningRate);
            totalError += error;
        }
        
        const averageError = totalError / trainingData.length;
        errors.push(averageError);
        
        // Early stopping if error is very small
        if (averageError < 0.001) {
            break;
        }
    }
    
    return {
        network: currentNetwork,
        finalError: errors[errors.length - 1],
        errors
    };
}

// Predict using trained network
export function predict(network: NeuralNetwork, inputs: number[]): number[] {
    const { finalOutput } = feedForward(network, inputs);
    return finalOutput;
}

// XOR problem example
export function xorExample(): {
    network: NeuralNetwork;
    predictions: { inputs: number[]; output: number[]; target: number[] }[];
} {
    const trainingData: TrainingData = [
        { inputs: [0, 0], target: [0] },
        { inputs: [0, 1], target: [1] },
        { inputs: [1, 0], target: [1] },
        { inputs: [1, 1], target: [0] }
    ];
    
    const { network } = trainSimpleNetwork(trainingData, 2, 0.1, 5000);
    
    const predictions = trainingData.map(example => ({
        inputs: example.inputs,
        output: predict(network, example.inputs),
        target: example.target
    }));
    
    return { network, predictions };
}

// Multi-layer network creation
export function createNetwork(layerSizes: number[]): NeuralNetwork {
    const network: NeuralNetwork = [];
    
    for (let i = 1; i < layerSizes.length; i++) {
        const inputSize = layerSizes[i - 1];
        const outputSize = layerSizes[i];
        
        const weights = Array(outputSize).fill(0).map(() =>
            Array(inputSize).fill(0).map(() => Math.random() * 2 - 1)
        );
        
        // Flatten weights array for our network format
        const flattenedWeights: number[] = [];
        for (let j = 0; j < outputSize; j++) {
            for (let k = 0; k < inputSize; k++) {
                flattenedWeights.push(weights[j][k]);
            }
        }
        
        const bias = Math.random() * 2 - 1;
        network.push([flattenedWeights, bias]);
    }
    
    return network;
}

// Network information
export function getNetworkInfo(network: NeuralNetwork): {
    layers: number;
    neuronsPerLayer: number[];
    totalWeights: number;
    totalParameters: number;
} {
    const neuronsPerLayer = network.map(layer => layer[0].length);
    const totalWeights = network.reduce((sum, layer) => sum + layer[0].length, 0);
    const totalParameters = totalWeights + network.length; // weights + biases
    
    return {
        layers: network.length,
        neuronsPerLayer,
        totalWeights,
        totalParameters
    };
}

// Example usage
export function exampleUsage(): void {
    console.log('Neural Networks Example:');
    
    // Activation functions
    console.log('\nActivation Functions:');
    console.log(`sigmoid(0) = ${sigmoid(0).toFixed(4)}`);
    console.log(`sigmoid(1) = ${sigmoid(1).toFixed(4)}`);
    console.log(`step(-1) = ${stepFunction(-1)}`);
    console.log(`step(1) = ${stepFunction(1)}`);
    
    // Perceptron
    console.log('\nPerceptron:');
    const perceptronWeights = [0.5, -0.5];
    const perceptronBias = -0.1;
    const perceptronInputs = [1, 0.5];
    const perceptronOutput = perceptron(perceptronWeights, perceptronBias, perceptronInputs);
    console.log(`Perceptron output: ${perceptronOutput}`);
    
    // Single neuron
    console.log('\nSingle Neuron:');
    const neuronWeights = [0.5, -0.5];
    const neuronInputs = [1, 0.5];
    const neuronOutput = neuron(neuronWeights, neuronInputs);
    console.log(`Neuron output: ${neuronOutput.toFixed(4)}`);
    
    // Feed-forward network
    console.log('\nFeed-Forward Network:');
    const network: NeuralNetwork = [
        [[0.5, -0.5], 0.0], // Hidden layer
        [[1.0, 1.0], 0.0]   // Output layer
    ];
    const ffResult = feedForward(network, [1, 1]);
    console.log(`Network output: [${ffResult.finalOutput.map(v => v.toFixed(4)).join(', ')}]`);
    
    // Backpropagation
    console.log('\nBackpropagation:');
    const bpResult = backpropagation(network, [1, 1], [1]);
    console.log(`Error: ${bpResult.error.toFixed(4)}`);
    console.log(`Output: [${bpResult.output.map(v => v.toFixed(4)).join(', ')}]`);
    
    // XOR problem
    console.log('\nXOR Problem:');
    const xorResult = xorExample();
    console.log('XOR Predictions:');
    xorResult.predictions.forEach(pred => {
        console.log(`  [${pred.inputs.join(', ')}] -> ${pred.output[0].toFixed(4)} (target: ${pred.target[0]})`);
    });
    
    // Network info
    console.log('\nNetwork Information:');
    const networkInfo = getNetworkInfo(xorResult.network);
    console.log(`Layers: ${networkInfo.layers}`);
    console.log(`Neurons per layer: [${networkInfo.neuronsPerLayer.join(', ')}]`);
    console.log(`Total weights: ${networkInfo.totalWeights}`);
    console.log(`Total parameters: ${networkInfo.totalParameters}`);
}
