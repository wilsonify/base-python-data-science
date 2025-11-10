// XOR example using the deep learning framework
// Ported from Python e01_xor_revisited

import { Sequential, Linear, Sigmoid } from '../layer';
import { GradientDescent, SSE } from '../metrics';
import { Tensor } from '../index';

// Training data
const xs: number[][] = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
];

const ys: number[][] = [
    [0],
    [1],
    [1],
    [0]
];

// Create the network
const net = new Sequential([
    new Linear(2, 2),
    new Sigmoid(),
    new Linear(2, 1)
]);

// Training setup
const optimizer = new GradientDescent(0.1);
const loss = new SSE();

// Training loop
function train(epochs: number): void {
    for (let epoch = 0; epoch < epochs; epoch++) {
        let epochLoss = 0.0;
        
        for (let i = 0; i < xs.length; i++) {
            const predicted = net.forward(xs[i]);
            epochLoss += loss.loss(predicted, ys[i]);
            const gradient = loss.gradient(predicted, ys[i]);
            net.backward(gradient);
            optimizer.step(net);
        }
        
        if (epoch % 500 === 0) {
            console.log(`xor loss ${epochLoss.toFixed(3)}`);
        }
    }
}

// Test the trained network
function test(): void {
    console.log('\\nTesting XOR network:');
    for (let i = 0; i < xs.length; i++) {
        const predicted = net.forward(xs[i]);
        console.log(`Input: [${xs[i]}], Predicted: ${(predicted[0] as number).toFixed(3)}, Actual: ${ys[i][0]}`);
    }
}

// Run training and testing
console.log('Training XOR network...');
train(3000);
test();

// Print final weights
console.log('\\nFinal weights:');
const params = net.params();
for (let i = 0; i < params.length; i++) {
    console.log(`Parameter ${i}:`, params[i]);
}
