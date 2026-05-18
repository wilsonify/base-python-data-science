// Metrics and loss functions for deep learning framework
// Ported from Python metrics module

import { Tensor, tensorCombine, tensorSum, zerosLike, is1d } from './index';
import { Layer } from './layer';

function copyTensor(source: Tensor, target: Tensor): void {
    if (is1d(source)) {
        for (let i = 0; i < (source as number[]).length; i++) {
            (target as number[])[i] = (source as number[])[i];
        }
    } else {
        for (let i = 0; i < (source as Tensor[]).length; i++) {
            copyTensor((source as Tensor[])[i], (target as Tensor[])[i]);
        }
    }
}

export function softmax(tensor: Tensor): Tensor {
    if (is1d(tensor)) {
        // Subtract largest value for numerical stability
        const largest = Math.max(...(tensor as number[]));
        const exps = (tensor as number[]).map(x => Math.exp(x - largest));
        const sumOfExps = exps.reduce((sum, exp) => sum + exp, 0);
        return exps.map(exp => exp / sumOfExps);
    } else {
        return (tensor as Tensor[]).map(tensor_i => softmax(tensor_i));
    }
}

export abstract class Loss {
    abstract loss(predicted: Tensor, actual: Tensor): number;
    abstract gradient(predicted: Tensor, actual: Tensor): Tensor;
}

export class SSE extends Loss {
    loss(predicted: Tensor, actual: Tensor): number {
        const squaredErrors = tensorCombine(
            (pred, act) => Math.pow(pred - act, 2),
            predicted,
            actual
        );
        return tensorSum(squaredErrors);
    }

    gradient(predicted: Tensor, actual: Tensor): Tensor {
        return tensorCombine(
            (pred, act) => 2 * (pred - act),
            predicted,
            actual
        );
    }
}

export abstract class Optimizer {
    abstract step(layer: Layer): void;
}

export class GradientDescent extends Optimizer {
    private readonly learningRate: number;

    constructor(learningRate: number = 0.1) {
        super();
        this.learningRate = learningRate;
    }

    step(layer: Layer): void {
        const params = layer.params();
        const grads = layer.grads();

        for (let i = 0; i < params.length; i++) {
            const param = params[i];
            const grad = grads[i];

            // Update param using gradient step
            const updatedParam = tensorCombine(
                (p, g) => p - g * this.learningRate,
                param,
                grad
            );

            // Copy updated values back to param (in-place update)
            copyTensor(updatedParam, param);
        }
    }
}

export class Momentum extends Optimizer {
    private readonly learningRate: number;
    private readonly momentum: number;
    private updates: Tensor[] = [];

    constructor(learningRate: number, momentum: number = 0.9) {
        super();
        this.learningRate = learningRate;
        this.momentum = momentum;
    }

    step(layer: Layer): void {
        const params = layer.params();
        const grads = layer.grads();

        // If we have no previous updates, start with all zeros
        if (this.updates.length === 0) {
            this.updates = grads.map(grad => zerosLike(grad));
        }

        for (let i = 0; i < this.updates.length; i++) {
            const update = this.updates[i];
            const param = params[i];
            const grad = grads[i];

            // Apply momentum
            const newUpdate = tensorCombine(
                (u, g) => this.momentum * u + (1 - this.momentum) * g,
                update,
                grad
            );

            // Copy new update back
            copyTensor(newUpdate, update);

            // Then take a gradient step
            const updatedParam = tensorCombine(
                (p, u) => p - this.learningRate * u,
                param,
                update
            );

            // Copy updated values back to param
            copyTensor(updatedParam, param);
        }
    }
}
export class SoftmaxCrossEntropy extends Loss {
    loss(predicted: Tensor, actual: Tensor): number {
        // Apply softmax to get probabilities
        const probabilities = softmax(predicted);
        
        // Compute likelihoods
        const likelihoods = tensorCombine(
            (p, act) => Math.log(p + 1e-30) * act,
            probabilities,
            actual
        );
        
        // Return negative sum
        return -tensorSum(likelihoods);
    }

    gradient(predicted: Tensor, actual: Tensor): Tensor {
        const probabilities = softmax(predicted);
        return tensorCombine(
            (p, act) => p - act,
            probabilities,
            actual
        );
    }
}
