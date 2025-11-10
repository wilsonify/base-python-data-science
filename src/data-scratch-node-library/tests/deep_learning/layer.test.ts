// Tests for layer implementations
// Ported from Python layer tests

import {
    Linear,
    Sequential,
    Tanh,
    Relu,
    Dropout
} from '../../ts-data-scratch/deep_learning/layer';
import { Tensor } from '../../ts-data-scratch/deep_learning/index';

describe('Layer Tests', () => {
    test('Linear layer forward pass', () => {
        const layer = new Linear(3, 2);
        const input: Tensor = [1, 2, 3];
        const output = layer.forward(input);
        
        expect(output).toHaveLength(2);
        expect(is1d(output)).toBe(true);
        
        // Check that output is computed correctly
        const params = layer.params();
        const weights = params[0] as Tensor[]; // 2x3 weight matrix
        const biases = params[1] as number[]; // 2-element bias vector
        
        for (let i = 0; i < 2; i++) {
            const expected = (input as number[]).reduce((sum, x, j) => 
                sum + x * (weights[i] as number[])[j], 0) + biases[i];
            expect(Math.abs((output as number[])[i] - expected)).toBeLessThan(0.001);
        }
    });

    test('Linear layer backward pass', () => {
        const layer = new Linear(2, 3);
        const input: Tensor = [1, 2];
        
        // Forward pass
        const output = layer.forward(input);
        
        // Backward pass
        const gradient: Tensor = [0.1, 0.2, 0.3];
        const inputGrad = layer.backward(gradient);
        
        expect(inputGrad).toHaveLength(2);
        expect(is1d(inputGrad)).toBe(true);
        
        // Check gradients
        const grads = layer.grads();
        expect(grads).toHaveLength(2); // weight grad and bias grad
    });

    test('Sequential layer', () => {
        const layers = [
            new Linear(2, 3),
            new Tanh(),
            new Linear(3, 1)
        ];
        const sequential = new Sequential(layers);
        
        const input: Tensor = [1, 2];
        const output = sequential.forward(input);
        
        expect(output).toHaveLength(1);
        expect(is1d(output)).toBe(true);
        
        // Test backward pass
        const gradient: Tensor = [0.5];
        const inputGrad = sequential.backward(gradient);
        
        expect(inputGrad).toHaveLength(2);
        expect(is1d(inputGrad)).toBe(true);
        
        // Test params and grads
        expect(sequential.params().length).toBeGreaterThan(0);
        expect(sequential.grads().length).toBeGreaterThan(0);
    });

    test('Tanh layer', () => {
        const layer = new Tanh();
        const input: Tensor = [-1, 0, 1];
        const output = layer.forward(input);
        
        expect(output).toHaveLength(3);
        expect(is1d(output)).toBe(true);
        
        // Check tanh values are in [-1, 1]
        (output as number[]).forEach(val => {
            expect(val).toBeGreaterThanOrEqual(-1);
            expect(val).toBeLessThanOrEqual(1);
        });
        
        // Test backward pass
        const gradient: Tensor = [0.1, 0.2, 0.3];
        const inputGrad = layer.backward(gradient);
        
        expect(inputGrad).toHaveLength(3);
        expect(is1d(inputGrad)).toBe(true);
    });

    test('Relu layer', () => {
        const layer = new Relu();
        const input: Tensor = [-1, 0, 1];
        const output = layer.forward(input);
        
        expect(output).toEqual([0, 0, 1]);
        
        // Test backward pass
        const gradient: Tensor = [0.1, 0.2, 0.3];
        const inputGrad = layer.backward(gradient);
        
        expect(inputGrad).toEqual([0, 0, 0.3]);
    });

    test('Dropout layer', () => {
        const layer = new Dropout(0.5);
        layer.setTrainingMode(true);
        
        const input: Tensor = [1, 2, 3, 4];
        const output = layer.forward(input);
        
        expect(output).toHaveLength(4);
        
        // During training, some values should be zeroed out
        // (though with probability, we can't guarantee which ones)
        
        // Test backward pass
        const gradient: Tensor = [0.1, 0.2, 0.3, 0.4];
        const inputGrad = layer.backward(gradient);
        
        expect(inputGrad).toHaveLength(4);
        
        // Test evaluation mode
        layer.setTrainingMode(false);
        const evalOutput = layer.forward(input);
        
        // During evaluation, outputs should be scaled
        evalOutput.forEach((val, i) => {
            expect(val).toBe((input as number[])[i] * 0.5);
        });
    });
});

// Helper function
function is1d(tensor: Tensor): boolean {
    if (!Array.isArray(tensor) || tensor.length === 0) {
        return true;
    }
    return typeof tensor[0] === 'number';
}
