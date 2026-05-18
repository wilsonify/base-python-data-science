// FizzBuzz example using the deep learning framework
// Ported from Python e02_fizzbuzz_revisited

import { Sequential, Linear, Tanh, Sigmoid } from '../layer';
import { Momentum, SSE, SoftmaxCrossEntropy } from '../metrics';

// Helper functions
function binaryEncode(n: number): number[] {
    const result: number[] = [];
    for (let i = 0; i < 10; i++) {
        result.push((n >> i) & 1);
    }
    return result;
}

function fizzBuzzEncode(n: number): number[] {
    if (n % 15 === 0) return [0, 0, 0, 1];
    if (n % 5 === 0) return [0, 0, 1, 0];
    if (n % 3 === 0) return [0, 1, 0, 0];
    return [1, 0, 0, 0];
}

function argmax(tensor: number[]): number {
    let maxIndex = 0;
    let maxValue = tensor[0];
    for (let i = 1; i < tensor.length; i++) {
        if (tensor[i] > maxValue) {
            maxValue = tensor[i];
            maxIndex = i;
        }
    }
    return maxIndex;
}

// Training data
const xs: number[][] = [];
const ys: number[][] = [];

for (let n = 101; n < 1024; n++) {
    xs.push(binaryEncode(n));
    ys.push(fizzBuzzEncode(n));
}

// Network setup
const NUM_HIDDEN = 25;
const net = new Sequential([
    new Linear(10, NUM_HIDDEN),
    new Tanh(),
    new Linear(NUM_HIDDEN, 4),
    new Sigmoid()
]);

// Accuracy function
function fizzBuzzAccuracy(low: number, hi: number, network: Sequential): number {
    let numCorrect = 0;
    for (let n = low; n < hi; n++) {
        const x = binaryEncode(n);
        const predicted = argmax(network.forward(x) as number[]);
        const actual = argmax(fizzBuzzEncode(n));
        if (predicted === actual) {
            numCorrect++;
        }
    }
    return numCorrect / (hi - low);
}

// Training with SSE loss
function trainWithSSE(epochs: number): void {
    const optimizer = new Momentum(0.1, 0.9);
    const loss = new SSE();

    console.log('Training with SSE loss...');
    for (let epoch = 0; epoch < epochs; epoch++) {
        let epochLoss = 0;
        
        for (let i = 0; i < xs.length; i++) {
            const predicted = net.forward(xs[i]);
            epochLoss += loss.loss(predicted, ys[i]);
            const gradient = loss.gradient(predicted, ys[i]);
            net.backward(gradient);
            optimizer.step(net);
        }
        
        const accuracy = fizzBuzzAccuracy(101, 1024, net);
        if (epoch % 100 === 0) {
            console.log(`fb loss: ${epochLoss.toFixed(2)} acc: ${accuracy.toFixed(2)}`);
        }
    }
}

// Training with SoftmaxCrossEntropy loss
function trainWithSoftmaxCrossEntropy(epochs: number): void {
    const net2 = new Sequential([
        new Linear(10, NUM_HIDDEN),
        new Tanh(),
        new Linear(NUM_HIDDEN, 4)
        // No final sigmoid layer
    ]);

    const optimizer = new Momentum(0.1, 0.9);
    const loss = new SoftmaxCrossEntropy();

    console.log(String.raw`\nTraining with SoftmaxCrossEntropy loss...`);
    for (let epoch = 0; epoch < epochs; epoch++) {
        let epochLoss = 0;

        for (let i = 0; i < xs.length; i++) {
            const predicted = net2.forward(xs[i]);
            epochLoss += loss.loss(predicted, ys[i]);
            const gradient = loss.gradient(predicted, ys[i]);
            net2.backward(gradient);
            optimizer.step(net2);
        }

        const accuracy = fizzBuzzAccuracy(101, 1024, net2);
        if (epoch % 20 === 0) {
            console.log(`fb loss: ${epochLoss.toFixed(3)} acc: ${accuracy.toFixed(2)}`);
        }
    }

    // Test results
    console.log(String.raw`\nTest results (SSE): ${fizzBuzzAccuracy(1, 101, net).toFixed(2)}`);
    console.log(`Test results (SoftmaxCrossEntropy): ${fizzBuzzAccuracy(1, 101, net2).toFixed(2)}`);
}

// Run training
trainWithSSE(1000);
trainWithSoftmaxCrossEntropy(100);
