// Tests for metrics and loss functions
// Ported from Python metrics tests

import {
    softmax,
    SSE,
    GradientDescent,
    Momentum,
    SoftmaxCrossEntropy
} from '../../ts-data-scratch/deep_learning/metrics';
import { Linear, Sequential } from '../../ts-data-scratch/deep_learning/layer';
import { Tensor } from '../../ts-data-scratch/deep_learning/index';

describe('Metrics and Loss Functions', () => {
    test('softmax function', () => {
        const tensor: Tensor = [1, 2, 3];
        const result = softmax(tensor);
        
        expect(result).toHaveLength(3);
        
        // Check that probabilities sum to 1
        const sum = (result as number[]).reduce((a, b) => a + b, 0);
        expect(Math.abs(sum - 1)).toBeLessThan(0.001);
        
        // Check that all values are positive
        (result as number[]).forEach(val => {
            expect(val).toBeGreaterThan(0);
        });
        
        // Check that larger input gets larger probability
        expect((result as number[])[2]).toBeGreaterThan((result as number[])[1]);
        expect((result as number[])[1]).toBeGreaterThan((result as number[])[0]);
    });

    test('SSE loss', () => {
        const loss = new SSE();
        const predicted: Tensor = [1, 2, 3];
        const actual: Tensor = [1, 2, 4];
        
        const lossValue = loss.loss(predicted, actual);
        expect(lossValue).toBe(1); // (3-4)^2 = 1
        
        const gradient = loss.gradient(predicted, actual);
        expect(gradient).toEqual([0, 0, -2]); // 2 * (3-4) = -2
    });

    test('SoftmaxCrossEntropy loss', () => {
        const loss = new SoftmaxCrossEntropy();
        const predicted: Tensor = [2, 1, 0.1]; // logits
        const actual: Tensor = [1, 0, 0]; // one-hot encoded
        
        const lossValue = loss.loss(predicted, actual);
        expect(lossValue).toBeGreaterThan(0);
        
        const gradient = loss.gradient(predicted, actual);
        expect(gradient).toHaveLength(3);
        
        // Gradient should be (softmax - actual)
        const soft = softmax(predicted);
        const expectedGrad = (soft as number[]).map((s, i) => s - (actual as number[])[i]);
        
        (gradient as number[]).forEach((g, i) => {
            expect(Math.abs(g - expectedGrad[i])).toBeLessThan(0.001);
        });
    });

    test('GradientDescent optimizer', () => {
        const layer = new Linear(2, 3);
        const optimizer = new GradientDescent(0.1);
        
        // Get initial parameters
        const initialParams = layer.params().map(param => 
            JSON.parse(JSON.stringify(param))
        );
        
        // Simulate a forward and backward pass to generate gradients
        const input: Tensor = [1, 2];
        layer.forward(input);
        const gradient: Tensor = [0.1, 0.2, 0.3];
        layer.backward(gradient);
        
        // Apply optimizer step
        optimizer.step(layer);
        
        // Check that parameters changed
        const newParams = layer.params();
        newParams.forEach((param, i) => {
            expect(JSON.stringify(param)).not.toEqual(JSON.stringify(initialParams[i]));
        });
    });

    test('Momentum optimizer', () => {
        const layer = new Linear(2, 3);
        const optimizer = new Momentum(0.1, 0.9);
        
        // Get initial parameters
        const initialParams = layer.params().map(param => 
            JSON.parse(JSON.stringify(param))
        );
        
        // Simulate a forward and backward pass to generate gradients
        const input: Tensor = [1, 2];
        layer.forward(input);
        const gradient: Tensor = [0.1, 0.2, 0.3];
        layer.backward(gradient);
        
        // Apply first optimizer step
        optimizer.step(layer);
        
        // Check that parameters changed
        const newParams = layer.params();
        newParams.forEach((param, i) => {
            expect(JSON.stringify(param)).not.toEqual(JSON.stringify(initialParams[i]));
        });
        
        // Apply second step to test momentum accumulation
        const paramsAfterFirstStep = layer.params().map(param => 
            JSON.parse(JSON.stringify(param))
        );
        
        // Need another forward/backward pass to generate new gradients
        layer.forward(input);
        layer.backward(gradient);
        optimizer.step(layer);
        
        const paramsAfterSecondStep = layer.params();
        paramsAfterSecondStep.forEach((param, i) => {
            expect(JSON.stringify(param)).not.toEqual(JSON.stringify(paramsAfterFirstStep[i]));
        });
    });
});
