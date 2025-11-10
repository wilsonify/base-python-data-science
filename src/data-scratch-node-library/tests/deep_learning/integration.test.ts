// Integration test for the complete deep learning framework
// Tests a simple neural network training workflow

import { Sequential, Linear, Tanh, Sigmoid } from '../../ts-data-scratch/deep_learning/layer';
import { GradientDescent, SSE } from '../../ts-data-scratch/deep_learning/metrics';
import { Tensor } from '../../ts-data-scratch/deep_learning/index';

describe('Deep Learning Integration Tests', () => {
    test('Complete training workflow for simple classification', () => {
        // Create a simple dataset for AND-like classification
        const trainingData: { input: number[], output: number[] }[] = [
            { input: [0, 0], output: [0] },
            { input: [0, 1], output: [0] },
            { input: [1, 0], output: [0] },
            { input: [1, 1], output: [1] }
        ];

        // Create a neural network
        const network = new Sequential([
            new Linear(2, 4),
            new Tanh(),
            new Linear(4, 1),
            new Sigmoid()
        ]);

        // Setup optimizer and loss function
        const optimizer = new GradientDescent(0.5);
        const lossFunction = new SSE();

        // Get initial loss
        let initialLoss = 0;
        for (const data of trainingData) {
            const predicted = network.forward(data.input);
            initialLoss += lossFunction.loss(predicted, data.output);
        }

        // Train the network
        const epochs = 1000;
        for (let epoch = 0; epoch < epochs; epoch++) {
            for (const data of trainingData) {
                // Forward pass
                const predicted = network.forward(data.input);
                
                // Compute loss and gradient
                const loss = lossFunction.loss(predicted, data.output);
                const gradient = lossFunction.gradient(predicted, data.output);
                
                // Backward pass
                network.backward(gradient);
                
                // Update weights
                optimizer.step(network);
            }
        }

        // Get final loss
        let finalLoss = 0;
        for (const data of trainingData) {
            const predicted = network.forward(data.input);
            finalLoss += lossFunction.loss(predicted, data.output);
        }

        // Verify that the network learned (loss decreased significantly)
        expect(finalLoss).toBeLessThan(initialLoss * 0.1);
        
        // Test predictions
        const predictions = trainingData.map(data => {
            const predicted = network.forward(data.input);
            return {
                input: data.input,
                predicted: (predicted[0] as number),
                actual: data.output[0]
            };
        });

        // Verify predictions are reasonable (close to actual values)
        predictions.forEach(pred => {
            const roundedPred = Math.round(pred.predicted);
            expect(roundedPred).toBe(pred.actual);
        });
    });

    test('Multi-layer network with different activation functions', () => {
        // Create a more complex network
        const network = new Sequential([
            new Linear(3, 5),
            new Tanh(),
            new Linear(5, 3),
            new Sigmoid(),
            new Linear(3, 1)
        ]);

        // Test forward pass
        const input: Tensor = [1, 2, 3];
        const output = network.forward(input);
        
        expect(output).toHaveLength(1);
        expect(typeof (output[0] as number)).toBe('number');
        expect(isFinite(output[0] as number)).toBe(true);

        // Test backward pass
        const gradient: Tensor = [0.1];
        const inputGradient = network.backward(gradient);
        
        expect(inputGradient).toHaveLength(3);
        inputGradient.forEach(val => {
            expect(typeof val).toBe('number');
            expect(isFinite(val as number)).toBe(true);
        });

        // Test that params and grads are available
        expect(network.params().length).toBeGreaterThan(0);
        expect(network.grads().length).toBeGreaterThan(0);
        expect(network.params().length).toBe(network.grads().length);
    });

    test('Network parameter and gradient consistency', () => {
        const layer = new Linear(2, 3);
        
        // Test initial parameters
        const params = layer.params();
        expect(params).toHaveLength(2); // weights and biases
        expect(tensorShape(params[0])).toEqual([3, 2]); // weight matrix
        expect(tensorShape(params[1])).toEqual([3]); // bias vector

        // Test gradients are initially zero or empty
        const grads = layer.grads();
        expect(grads).toHaveLength(2);

        // Forward and backward pass to generate gradients
        const input: Tensor = [1, 2];
        layer.forward(input);
        const gradient: Tensor = [0.1, 0.2, 0.3];
        layer.backward(gradient);

        // Check that gradients are computed
        const newGrads = layer.grads();
        expect(newGrads).toHaveLength(2);
        
        // Verify gradient shapes match parameter shapes
        expect(tensorShape(newGrads[0])).toEqual(tensorShape(params[0]));
        expect(tensorShape(newGrads[1])).toEqual(tensorShape(params[1]));
    });
});

// Helper function
function tensorShape(tensor: Tensor): number[] {
    const sizes: number[] = [];
    while (Array.isArray(tensor) && tensor.length > 0 && typeof tensor[0] !== 'number') {
        sizes.push(tensor.length);
        tensor = tensor[0] as Tensor;
    }
    if (Array.isArray(tensor) && typeof tensor[0] === 'number') {
        sizes.push(tensor.length);
    }
    return sizes;
}
