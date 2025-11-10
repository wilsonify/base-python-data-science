// Model serialization utilities for deep learning framework
// Ported from Python io module

import { readFileSync, writeFileSync } from 'fs';
import { Layer } from './layer';
import { Tensor, tensorShape } from './index';

export function saveWeights(model: Layer, filename: string): void {
    const weights = model.params();
    const jsonData = JSON.stringify(weights, null, 2);
    writeFileSync(filename, jsonData, 'utf8');
}

export function loadWeights(model: Layer, filename: string): void {
    const jsonData = readFileSync(filename, 'utf8');
    const weights: Tensor[] = JSON.parse(jsonData);
    
    // Check for consistency
    const params = model.params();
    for (let i = 0; i < params.length; i++) {
        const param = params[i];
        const weight = weights[i];
        
        if (JSON.stringify(tensorShape(param)) !== JSON.stringify(tensorShape(weight))) {
            throw new Error(`Shape mismatch: expected ${JSON.stringify(tensorShape(param))}, got ${JSON.stringify(tensorShape(weight))}`);
        }
    }
    
    // Load weights using slice assignment equivalent
    for (let i = 0; i < params.length; i++) {
        copyTensor(weights[i], params[i]);
    }
}

function copyTensor(source: Tensor, target: Tensor): void {
    if (Array.isArray(source) && source.length > 0 && typeof source[0] === 'number') {
        // 1D tensor
        for (let i = 0; i < source.length; i++) {
            (target as number[])[i] = (source as number[])[i];
        }
    } else if (Array.isArray(source) && source.length > 0 && Array.isArray(source[0])) {
        // Multi-dimensional tensor
        for (let i = 0; i < source.length; i++) {
            copyTensor((source as Tensor[])[i], (target as Tensor[])[i]);
        }
    }
}
