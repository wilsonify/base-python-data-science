// Tests for tensor operations
// Ported from Python deep learning tests

import {
    Tensor,
    tensorShape,
    is1d,
    tensorSum,
    tensorApply,
    tensorCombine,
    zerosLike,
    randomTensor
} from '../../ts-data-scratch/deep_learning/index';

describe('Tensor Operations', () => {
    test('tensorShape function', () => {
        const tensor1d: Tensor = [1, 2, 3];
        expect(tensorShape(tensor1d)).toEqual([3]);

        const tensor2d: Tensor = [[1, 2], [3, 4]];
        expect(tensorShape(tensor2d)).toEqual([2, 2]);

        const tensor3d: Tensor = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]];
        expect(tensorShape(tensor3d)).toEqual([2, 2, 2]);
    });

    test('is1d function', () => {
        const tensor1d: Tensor = [1, 2, 3];
        expect(is1d(tensor1d)).toBe(true);

        const tensor2d: Tensor = [[1, 2], [3, 4]];
        expect(is1d(tensor2d)).toBe(false);

        const empty: Tensor = [];
        expect(is1d(empty)).toBe(true);
    });

    test('tensorSum function', () => {
        const tensor1d: Tensor = [1, 2, 3];
        expect(tensorSum(tensor1d)).toBe(6);

        const tensor2d: Tensor = [[1, 2], [3, 4]];
        expect(tensorSum(tensor2d)).toBe(10);

        const tensor3d: Tensor = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]];
        expect(tensorSum(tensor3d)).toBe(36);
    });

    test('tensorApply function', () => {
        const tensor1d: Tensor = [1, 2, 3];
        const result1d = tensorApply(x => x * 2, tensor1d);
        expect(result1d).toEqual([2, 4, 6]);

        const tensor2d: Tensor = [[1, 2], [3, 4]];
        const result2d = tensorApply(x => x * 2, tensor2d);
        expect(result2d).toEqual([[2, 4], [6, 8]]);
    });

    test('tensorCombine function', () => {
        const t1: Tensor = [1, 2, 3];
        const t2: Tensor = [4, 5, 6];
        const result = tensorCombine((a, b) => a + b, t1, t2);
        expect(result).toEqual([5, 7, 9]);

        const t1_2d: Tensor = [[1, 2], [3, 4]];
        const t2_2d: Tensor = [[5, 6], [7, 8]];
        const result2d = tensorCombine((a, b) => a + b, t1_2d, t2_2d);
        expect(result2d).toEqual([[6, 8], [10, 12]]);
    });

    test('zerosLike function', () => {
        const tensor1d: Tensor = [1, 2, 3];
        const zeros1d = zerosLike(tensor1d);
        expect(zeros1d).toEqual([0, 0, 0]);

        const tensor2d: Tensor = [[1, 2], [3, 4]];
        const zeros2d = zerosLike(tensor2d);
        expect(zeros2d).toEqual([[0, 0], [0, 0]]);
    });

    test('randomTensor function', () => {
        const tensor1d = randomTensor(5);
        expect(tensor1d).toHaveLength(5);
        expect(is1d(tensor1d)).toBe(true);

        const tensor2d = randomTensor(3, 4);
        expect(tensorShape(tensor2d)).toEqual([3, 4]);
        expect(is1d(tensor2d)).toBe(false);
    });
});
