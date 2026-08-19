// Deep Learning Framework for TypeScript
// Ported from Python deep learning module

export type Tensor = number[] | Tensor[];

export function tensorShape(tensor: Tensor): number[] {
    const sizes: number[] = [];
    while (Array.isArray(tensor) && tensor.length > 0 && typeof tensor[0] !== 'number') {
        sizes.push(tensor.length);
        tensor = tensor[0];
    }
    if (Array.isArray(tensor) && typeof tensor[0] === 'number') {
        sizes.push(tensor.length);
    }
    return sizes;
}

export function is1d(tensor: Tensor): boolean {
    if (!Array.isArray(tensor) || tensor.length === 0) {
        return true;
    }
    return typeof tensor[0] === 'number';
}

export function tensorSum(tensor: Tensor): number {
    if (is1d(tensor)) {
        return (tensor as number[]).reduce((sum, x) => sum + x, 0);
    } else {
        return (tensor as Tensor[]).reduce((sum, tensor_i) => sum + tensorSum(tensor_i), 0);
    }
}

export function tensorApply(f: (x: number) => number, tensor: Tensor): Tensor {
    if (is1d(tensor)) {
        return (tensor as number[]).map(x => f(x));
    } else {
        return (tensor as Tensor[]).map(tensor_i => tensorApply(f, tensor_i));
    }
}

export function zerosLike(tensor: Tensor): Tensor {
    return tensorApply(() => 0.0, tensor);
}

export function tensorCombine(
    f: (x: number, y: number) => number,
    t1: Tensor,
    t2: Tensor
): Tensor {
    if (is1d(t1)) {
        return (t1 as number[]).map((x, i) => f(x, (t2 as number[])[i]));
    } else {
        return (t1 as Tensor[]).map((t1_i, i) => 
            tensorCombine(f, t1_i, (t2 as Tensor[])[i])
        );
    }
}

export function sigmoid(x: number): number {
    return 1 / (1 + Math.exp(-x));
}

export class Sigmoid {
    private sigmoids: Tensor = [];

    forward(input: Tensor): Tensor {
        this.sigmoids = tensorApply(sigmoid, input);
        return this.sigmoids;
    }
    
    backward(gradient: Tensor): Tensor {
        return tensorCombine(
            (sig, grad) => sig * (1 - sig) * grad,
            this.sigmoids,
            gradient
        );
    }

    params(): Tensor[] {
        return [];
    }

    grads(): Tensor[] {
        return [];
    }
}

export function randomUniform(...dims: number[]): Tensor {
    if (dims.length === 1) {
        return Array.from({ length: dims[0] }, () => Math.random());
    } else {
        return Array.from({ length: dims[0] }, () => 
            randomUniform(...dims.slice(1))
        );
    }
}

// Box-Muller transform for normal distribution
function boxMuller(): number {
    const u1 = Math.random();
    const u2 = Math.random();
    return Math.sqrt(-2 * Math.log(u1)) * Math.cos(2 * Math.PI * u2);
}

export function randomNormal(
    dims: number[],
    mean: number = 0,
    variance: number = 1
): Tensor {
    if (dims.length === 1) {
        return Array.from({ length: dims[0] }, () => 
            mean + variance * boxMuller()
        );
    } else {
        return Array.from({ length: dims[0] }, () => 
            randomNormal(dims.slice(1), mean, variance)
        );
    }
}

export function randomTensor(...dims: number[]): Tensor {
    const init = 'normal'; // Default initialization
    if (init === 'normal') {
        return randomNormal(dims);
    } else if (init === 'uniform') {
        return randomUniform(...dims);
    } else if (init === 'xavier') {
        const variance = dims.length / dims.reduce((sum, dim) => sum + dim, 0);
        return randomNormal(dims, 0, variance);
    } else {
        throw new Error(`unknown init: ${init}`);
    }
}

export function randomTensorWithInit(...dimsAndInit: [...number[], string]): Tensor {
    const init = dimsAndInit[dimsAndInit.length - 1] as string;
    const dims = dimsAndInit.slice(0, -1) as number[];
    
    if (init === 'normal') {
        return randomNormal(dims);
    } else if (init === 'uniform') {
        return randomUniform(...dims);
    } else if (init === 'xavier') {
        const variance = dims.length / dims.reduce((sum, dim) => sum + dim, 0);
        return randomNormal(dims, 0, variance);
    } else {
        throw new Error(`unknown init: ${init}`);
    }
}
