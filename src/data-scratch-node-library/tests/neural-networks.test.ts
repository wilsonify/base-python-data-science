import {
    sigmoid,
    sigmoidDerivative,
    stepFunction,
    tanh,
    tanhDerivative,
    relu,
    reluDerivative,
    perceptron,
    neuron,
    feedForward,
    backpropagation,
    updateWeights,
    trainSimpleNetwork,
    predict,
    xorExample,
    createNetwork,
    getNetworkInfo,
    type NeuralNetwork
} from '../ts-data-scratch/neural_networks';

describe('Neural Networks', () => {
    describe('Activation Functions', () => {
        test('sigmoid should return values between 0 and 1', () => {
            expect(sigmoid(0)).toBeCloseTo(0.5, 4);
            expect(sigmoid(1)).toBeCloseTo(0.7311, 4);
            expect(sigmoid(-1)).toBeCloseTo(0.2689, 4);
            expect(sigmoid(10)).toBeGreaterThan(0.999);
            expect(sigmoid(-10)).toBeLessThan(0.001);
        });

        test('sigmoidDerivative should compute correct derivative', () => {
            const s0 = sigmoid(0);
            expect(sigmoidDerivative(0)).toBeCloseTo(s0 * (1 - s0), 6);
            
            const s1 = sigmoid(1);
            expect(sigmoidDerivative(1)).toBeCloseTo(s1 * (1 - s1), 6);
        });

        test('stepFunction should return binary output', () => {
            expect(stepFunction(1)).toBe(1);
            expect(stepFunction(0.1)).toBe(1);
            expect(stepFunction(0)).toBe(0);
            expect(stepFunction(-0.1)).toBe(0);
            expect(stepFunction(-1)).toBe(0);
        });

        test('tanh should return values between -1 and 1', () => {
            expect(tanh(0)).toBeCloseTo(0, 4);
            expect(tanh(1)).toBeCloseTo(0.7616, 4);
            expect(tanh(-1)).toBeCloseTo(-0.7616, 4);
            expect(tanh(10)).toBeGreaterThan(0.999);
            expect(tanh(-10)).toBeLessThan(-0.999);
        });

        test('tanhDerivative should compute correct derivative', () => {
            const t0 = tanh(0);
            expect(tanhDerivative(0)).toBeCloseTo(1 - t0 * t0, 6);
            
            const t1 = tanh(1);
            expect(tanhDerivative(1)).toBeCloseTo(1 - t1 * t1, 6);
        });

        test('relu should return correct values', () => {
            expect(relu(1)).toBe(1);
            expect(relu(0.5)).toBe(0.5);
            expect(relu(0)).toBe(0);
            expect(relu(-0.5)).toBe(0);
            expect(relu(-1)).toBe(0);
        });

        test('reluDerivative should return correct derivative', () => {
            expect(reluDerivative(1)).toBe(1);
            expect(reluDerivative(0.5)).toBe(1);
            expect(reluDerivative(0)).toBe(0);
            expect(reluDerivative(-0.5)).toBe(0);
            expect(reluDerivative(-1)).toBe(0);
        });
    });

    describe('Simple Neural Components', () => {
        test('perceptron should classify linearly separable data', () => {
            // AND gate
            const weights = [0.5, 0.5];
            const bias = -0.7;
            
            expect(perceptron(weights, bias, [0, 0])).toBe(0);
            expect(perceptron(weights, bias, [0, 1])).toBe(0);
            expect(perceptron(weights, bias, [1, 0])).toBe(0);
            expect(perceptron(weights, bias, [1, 1])).toBe(1);
        });

        test('neuron should compute weighted sum with activation', () => {
            const weights = [0.5, 0.5];
            
            // With sigmoid activation
            const result = neuron(weights, [1, 1]);
            expect(result).toBeCloseTo(sigmoid(1), 6); // 0.5*1 + 0.5*1 = 1
        });

        test('neuron should work with different activation functions', () => {
            const weights = [1, 1];
            
            const sigmoidResult = neuron(weights, [1, 1]);
            expect(sigmoidResult).toBeCloseTo(sigmoid(2), 6);
        });
    });

    describe('Feed Forward Network', () => {
        test('feedForward should propagate through network correctly', () => {
            const network = createNetwork([2, 1, 1]);
            
            const result = feedForward(network, [1, 1]);
            
            expect(result).toHaveProperty('outputs');
            expect(result).toHaveProperty('finalOutput');
            
            expect(result.outputs).toHaveLength(3); // Input + hidden + output
            expect(result.finalOutput).toHaveLength(1);
            
            expect(result.outputs[0]).toEqual([1, 1]); // Input should be preserved
        });

        test('feedForward should handle different network sizes', () => {
            const singleLayer = createNetwork([2, 1]);
            const result = feedForward(singleLayer, [1, 1]);
            
            expect(result.outputs).toHaveLength(2);
            expect(result.finalOutput).toHaveLength(1);
        });

        test('feedForward should handle single input', () => {
            const network = createNetwork([1, 1, 1]);
            
            const result = feedForward(network, [1]);
            expect(result.finalOutput).toHaveLength(1);
            expect(typeof result.finalOutput[0]).toBe('number');
        });
    });

    describe('Backpropagation', () => {
        test('backpropagation should compute gradients', () => {
            const network = [
                [[0.15, 0.20], 0.35], // Input to hidden
                [[0.25, 0.30], 0.35]  // Hidden to output
            ] as NeuralNetwork;
            
            const inputs = [0.05, 0.10];
            const targets = [0.01, 0.99]; // For 2 outputs (need to adjust network)
            
            // For this test, let's use a simpler case
            const simpleNetwork = [
                [[0.15, 0.20], 0.35], // 2 inputs to 1 hidden
                [[0.25], 0.35]        // 1 hidden to 1 output
            ] as NeuralNetwork;
            
            const simpleTargets = [0.01];
            
            const result = backpropagation(simpleNetwork, inputs, simpleTargets);
            
            expect(result).toHaveProperty('gradients');
            expect(Array.isArray(result.gradients)).toBe(true);
            expect(result.gradients).toHaveLength(2);
        });

        test('backpropagation should handle different network architectures', () => {
            const network = [
                [[0.1, 0.1], 0.1], // 2 inputs to 1 hidden
                [[0.1], 0.1]       // 1 hidden to 1 output
            ] as NeuralNetwork;
            
            const result = backpropagation(network, [1, 1], [0]);
            expect(result.gradients).toHaveLength(2);
        });
    });

    describe('Weight Updates', () => {
        test('updateWeights should modify network weights', () => {
            const network = createNetwork([2, 1, 1]);
            
            const gradients = [
                [[0.1, 0.1], 0.1],
                [[0.1], 0.1]
            ] as unknown as NeuralNetwork;
            
            const learningRate = 0.1;
            const updatedNetwork = updateWeights(network as any, gradients, learningRate);
            
            expect(updatedNetwork).toHaveLength(2);
            expect(updatedNetwork[0]).toHaveLength(2);
            expect(updatedNetwork[1]).toHaveLength(2);
            
            // Weights should have changed
            expect(updatedNetwork[0][0][0]).not.toBe(network[0][0][0]);
        });

        test('updateWeights should handle different learning rates', () => {
            const network = createNetwork([2, 1, 1]);
            
            const gradients = [
                [[0.1, 0.1], 0.1],
                [[0.1], 0.1]
            ] as unknown as NeuralNetwork;
            
            const updated1 = updateWeights(network as any, gradients, 0.1);
            const updated2 = updateWeights(network as any, gradients, 0.5);
            
            // Different learning rates should produce different results
            expect(updated1[0][0][0]).not.toBe(updated2[0][0][0]);
        });
    });

    describe('Network Training', () => {
        test('trainSimpleNetwork should train XOR problem', () => {
            const trainingData = [
                { inputs: [0, 0], target: [0] },
                { inputs: [0, 1], target: [1] },
                { inputs: [1, 0], target: [1] },
                { inputs: [1, 1], target: [0] }
            ];
            
            const result = trainSimpleNetwork(trainingData, 2, 0.5, 100);
            
            expect(result).toHaveProperty('network');
            expect(result).toHaveProperty('finalError');
            expect(result).toHaveProperty('epochs');
            
            expect(Array.isArray(result.network)).toBe(true);
            expect(typeof result.finalError).toBe('number');
            expect(typeof result.epochs).toBe('number');
            
            expect(result.finalError).toBeLessThan(1); // Should reduce error
            expect(result.epochs).toBeLessThanOrEqual(100);
        });

        test('trainSimpleNetwork should handle different hidden sizes', () => {
            const trainingData = [
                { inputs: [0, 0], target: [0] },
                { inputs: [1, 1], target: [0] }
            ];
            
            const result1 = trainSimpleNetwork(trainingData, 2, 0.1, 50);
            const result2 = trainSimpleNetwork(trainingData, 4, 0.1, 50);
            
            expect(result1.network).toHaveLength(2); // Hidden + Output
            expect(result2.network).toHaveLength(2);
        });

        test('trainSimpleNetwork should handle different learning rates', () => {
            const trainingData = [
                { inputs: [0, 0], target: [0] },
                { inputs: [1, 1], target: [1] }
            ];
            
            const result1 = trainSimpleNetwork(trainingData, 2, 0.01, 50);
            const result2 = trainSimpleNetwork(trainingData, 2, 0.5, 50);
            
            expect(typeof result1.finalError).toBe('number');
            expect(typeof result2.finalError).toBe('number');
        });

        test('trainSimpleNetwork should converge for simple problems', () => {
            // Simple identity function
            const trainingData = [
                { inputs: [0], target: [0] },
                { inputs: [1], target: [1] }
            ];
            
            const result = trainSimpleNetwork(trainingData, 2, 0.5, 200);
            
            expect(result.finalError).toBeLessThan(0.1);
        });
    });

    describe('Prediction', () => {
        test('predict should make predictions with trained network', () => {
            const trainingData = [
                { inputs: [0, 0], target: [0] },
                { inputs: [1, 1], target: [1] }
            ];
            
            const { network } = trainSimpleNetwork(trainingData, 2, 0.5, 100);
            
            const prediction1 = predict(network, [0, 0]);
            const prediction2 = predict(network, [1, 1]);
            
            expect(prediction1).toHaveLength(1);
            expect(prediction2).toHaveLength(1);
            expect(typeof prediction1[0]).toBe('number');
            expect(typeof prediction2[0]).toBe('number');
            
            // Should predict closer to targets
            expect(prediction1[0]).toBeLessThan(0.5);
            expect(prediction2[0]).toBeGreaterThan(0.5);
        });

        test('predict should handle multiple outputs', () => {
            // Create a simple multi-output network manually
            const network: NeuralNetwork = [
                [[0.5, 0.5], 0], // 2 inputs to 2 hidden
                [[0.5, 0.5], 0]  // 2 hidden to 2 outputs
            ];
            
            const prediction = predict(network, [1, 1]);
            expect(prediction).toHaveLength(2);
        });
    });

    describe('Network Creation and Info', () => {
        test('createNetwork should create network with specified architecture', () => {
            const network = createNetwork([2, 3, 1]);
            
            expect(network).toHaveLength(2); // Input->Hidden + Hidden->Output layers
            
            // Check dimensions (flattened: inputSize * outputSize)
            expect(network[0][0]).toHaveLength(6); // 2 inputs * 3 hidden = 6
            expect(network[1][0]).toHaveLength(3); // 3 hidden * 1 output = 3
            
            // Check types
            expect(typeof network[0][1]).toBe('number'); // Bias
            expect(typeof network[1][1]).toBe('number');
        });

        test('createNetwork should handle different architectures', () => {
            const network1 = createNetwork([1, 2, 1]);
            const network2 = createNetwork([3, 5, 2]);
            
            expect(network1[0][0]).toHaveLength(2);  // 1 * 2 = 2
            expect(network2[0][0]).toHaveLength(15); // 3 * 5 = 15
        });

        test('getNetworkInfo should return network information', () => {
            const network = createNetwork([2, 3, 1]);
            const info = getNetworkInfo(network);
            
            expect(info).toHaveProperty('layers');
            expect(info).toHaveProperty('neuronsPerLayer');
            expect(info).toHaveProperty('totalWeights');
            expect(info).toHaveProperty('totalParameters');
            
            expect(info.layers).toBe(2);
            expect(info.neuronsPerLayer).toEqual([6, 3]); // Flat weight counts: 2*3=6, 3*1=3
            expect(typeof info.totalWeights).toBe('number');
            expect(typeof info.totalParameters).toBe('number');
        });
    });

    describe('XOR Example', () => {
        test('xorExample should run without errors', () => {
            expect(() => xorExample()).not.toThrow();
        });

        test('xorExample should return valid results', () => {
            const result = xorExample();
            
            expect(result).toHaveProperty('network');
            expect(result).toHaveProperty('predictions');
            
            expect(Array.isArray(result.network)).toBe(true);
            expect(Array.isArray(result.predictions)).toBe(true);
            expect(result.predictions).toHaveLength(4);
            
            // Check prediction structure
            result.predictions.forEach(pred => {
                expect(pred).toHaveProperty('inputs');
                expect(pred).toHaveProperty('output');
                expect(pred).toHaveProperty('target');
                expect(Array.isArray(pred.inputs)).toBe(true);
                expect(Array.isArray(pred.output)).toBe(true);
                expect(Array.isArray(pred.target)).toBe(true);
            });
        });
    });

    describe('Edge Cases', () => {
        test('should handle zero weights', () => {
            const network: NeuralNetwork = [
                [[0, 0], 0],
                [[0], 0]
            ];
            
            const result = feedForward(network, [1, 1]);
            expect(result.finalOutput[0]).toBeCloseTo(0.5, 6); // sigmoid(0)
        });

        test('should handle very large weights', () => {
            const network: NeuralNetwork = [
                [[100, 100], 0],
                [[100], 0]
            ];
            
            const result = feedForward(network, [1, 1]);
            expect(result.finalOutput[0]).toBeGreaterThan(0.999);
        });

        test('should handle very negative weights', () => {
            const network: NeuralNetwork = [
                [[-100, -100, -100, -100], 0],  // 2 inputs -> 2 hidden (4 flat weights)
                [[-100, -100], -100]             // 2 hidden -> 1 output with strong negative bias
            ];
            
            const result = feedForward(network, [1, 1]);
            expect(result.finalOutput[0]).toBeLessThan(0.001);
        });

        test('should handle single input neuron', () => {
            const network: NeuralNetwork = [
                [[0.5], 0],
                [[0.5], 0]
            ];
            
            const result = feedForward(network, [1]);
            expect(result.finalOutput).toHaveLength(1);
        });

        test('should handle empty training data gracefully', () => {
            expect(() => {
                trainSimpleNetwork([], 2, 0.1, 10);
            }).toThrow();
        });
    });

    describe('Performance Tests', () => {
        test('should handle reasonable training times', () => {
            const trainingData = [];
            for (let i = 0; i < 50; i++) {
                trainingData.push({
                    inputs: [Math.random(), Math.random()],
                    target: [Math.random() > 0.5 ? 1 : 0]
                });
            }
            
            const start = Date.now();
            const result = trainSimpleNetwork(trainingData, 4, 0.1, 100);
            const duration = Date.now() - start;
            
            expect(result.finalError).toBeLessThan(1);
            expect(duration).toBeLessThan(5000); // Should complete within 5 seconds
        });

        test('should handle larger networks efficiently', () => {
            const network = createNetwork([10, 20, 5]);
            const inputs = Array(10).fill(0).map(() => Math.random());
            
            const start = Date.now();
            const result = feedForward(network, inputs);
            const duration = Date.now() - start;
            
            expect(result.finalOutput).toHaveLength(5);
            expect(duration).toBeLessThan(1000); // Should complete within 1 second
        });
    });

    describe('Numerical Stability', () => {
        test('should handle deterministic behavior', () => {
            const testInputs = [1, 1];
            
            const network = createNetwork([2, 2, 1]);
            const pred1 = predict(network, testInputs);
            const pred2 = predict(network, testInputs);
            
            expect(pred1).toEqual(pred2); // Same network and inputs should give same output
        });

        test('should handle extreme input values', () => {
            const network = createNetwork([2, 2, 1]);
            
            const extremeInputs = [1000, -1000];
            const result = feedForward(network, extremeInputs);
            
            expect(result.finalOutput[0]).toBeGreaterThanOrEqual(0);
            expect(result.finalOutput[0]).toBeLessThanOrEqual(1);
            expect(isFinite(result.finalOutput[0])).toBe(true);
        });

        test('should maintain numerical precision', () => {
            const network = createNetwork([2, 2, 1]);
            
            const result1 = feedForward(network, [1, 1]);
            const result2 = feedForward(network, [1, 1]);
            
            // Results should be identical for same inputs
            expect(result1.finalOutput[0]).toBe(result2.finalOutput[0]);
        });
    });
});
