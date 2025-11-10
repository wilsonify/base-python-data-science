// Layer implementations for deep learning framework
// Ported from Python layer module

import { Tensor, randomTensorWithInit, tensorApply, tensorCombine, Sigmoid as BaseSigmoid } from './index';
import { dot } from '../linear_algebra';

export abstract class Layer {
    abstract forward(input: Tensor): Tensor;
    abstract backward(gradient: Tensor): Tensor;
    
    params(): Tensor[] {
        return [];
    }
    
    grads(): Tensor[] {
        return [];
    }
}

export class Linear extends Layer {
    private inputDim: number;
    private outputDim: number;
    public w: Tensor;
    public b: Tensor;
    private input: Tensor = [];
    private wGrad: number[][] = [];
    private bGrad: number[] = [];

    constructor(inputDim: number, outputDim: number, init: string = 'xavier') {
        super();
        this.inputDim = inputDim;
        this.outputDim = outputDim;
        
        // Initialize weights and biases
        this.w = randomTensorWithInit(outputDim, inputDim, init);
        this.b = randomTensorWithInit(outputDim, init);
    }

    forward(input: Tensor): Tensor {
        this.input = input;
        // Return vector of neuron outputs
        const result: number[] = [];
        for (let o = 0; o < this.outputDim; o++) {
            const weightedSum = dot(input as number[], (this.w as Tensor[])[o] as number[]) + 
                               (this.b as number[])[o];
            result.push(weightedSum);
        }
        return result;
    }

    backward(gradient: Tensor): Tensor {
        // Bias gradients are the same as output gradients
        this.bGrad = gradient as number[];
        
        // Weight gradients
        this.wGrad = [];
        for (let o = 0; o < this.outputDim; o++) {
            const wGradRow: number[] = [];
            for (let i = 0; i < this.inputDim; i++) {
                wGradRow.push((this.input as number[])[i] * (gradient as number[])[o]);
            }
            this.wGrad.push(wGradRow);
        }
        
        // Input gradients
        const inputGrad: number[] = [];
        for (let i = 0; i < this.inputDim; i++) {
            let sum = 0;
            for (let o = 0; o < this.outputDim; o++) {
                sum += ((this.w as Tensor[])[o] as number[])[i] * (gradient as number[])[o];
            }
            inputGrad.push(sum);
        }
        return inputGrad;
    }

    params(): Tensor[] {
        return [this.w, this.b];
    }
    
    grads(): Tensor[] {
        return [this.wGrad, this.bGrad];
    }
}

export class Sequential extends Layer {
    private layers: Layer[];

    constructor(layers: Layer[]) {
        super();
        this.layers = layers;
    }

    forward(input: Tensor): Tensor {
        let output = input;
        for (const layer of this.layers) {
            output = layer.forward(output);
        }
        return output;
    }

    backward(gradient: Tensor): Tensor {
        let grad = gradient;
        for (let i = this.layers.length - 1; i >= 0; i--) {
            grad = this.layers[i].backward(grad);
        }
        return grad;
    }

    params(): Tensor[] {
        const allParams: Tensor[] = [];
        for (const layer of this.layers) {
            allParams.push(...layer.params());
        }
        return allParams;
    }

    grads(): Tensor[] {
        const allGrads: Tensor[] = [];
        for (const layer of this.layers) {
            allGrads.push(...layer.grads());
        }
        return allGrads;
    }
}

export function tanh(x: number): number {
    if (x < -100) return -1;
    if (x > 100) return 1;
    const em2x = Math.exp(-2 * x);
    return (1 - em2x) / (1 + em2x);
}

export class Tanh extends Layer {
    private tanhOutput: Tensor = [];

    forward(input: Tensor): Tensor {
        this.tanhOutput = tensorApply(tanh, input);
        return this.tanhOutput;
    }

    backward(gradient: Tensor): Tensor {
        return tensorCombine(
            (tanhVal, grad) => (1 - tanhVal * tanhVal) * grad,
            this.tanhOutput,
            gradient
        );
    }
}

export class Relu extends Layer {
    private input: Tensor = [];

    forward(input: Tensor): Tensor {
        this.input = input;
        return tensorApply(x => Math.max(x, 0), input);
    }

    backward(gradient: Tensor): Tensor {
        return tensorCombine(
            (x, grad) => x > 0 ? grad : 0,
            this.input,
            gradient
        );
    }
}

export class Dropout extends Layer {
    private p: number;
    private train: boolean = true;
    private mask: Tensor = [];

    constructor(p: number) {
        super();
        this.p = p;
    }

    setTrainingMode(train: boolean): void {
        this.train = train;
    }

    forward(input: Tensor): Tensor {
        if (this.train) {
            // Create mask using the specified probability
            this.mask = tensorApply(() => Math.random() < this.p ? 0 : 1, input);
            // Multiply by mask to dropout inputs
            return tensorCombine((x, m) => x * m, input, this.mask);
        } else {
            // During evaluation, scale down outputs uniformly
            return tensorApply(x => x * (1 - this.p), input);
        }
    }

    backward(gradient: Tensor): Tensor {
        if (this.train) {
            // Only propagate gradients where mask == 1
            return tensorCombine((g, m) => g * m, gradient, this.mask);
        } else {
            throw new Error("don't call backward when not in train mode");
        }
    }
}

// Re-export Sigmoid from index module for convenience
export { BaseSigmoid as Sigmoid };
