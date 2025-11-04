import {
    scalar_add,
    vector_add,
    vector_subtract,
    vector_sum,
    scalar_multiply,
    vector_mean,
    dot,
    sum_of_squares,
    magnitude,
    squared_distance,
    distance,
    shape,
    get_row,
    get_column,
    make_matrix,
    is_diagonal,
    matrix_add
} from '../ts-data-scratch/linear_algebra';

describe('Linear Algebra', () => {
    describe('Scalar Operations', () => {
        test('scalar_add should add two numbers', () => {
            expect(scalar_add(2, 3)).toBe(5);
            expect(scalar_add(-1, 1)).toBe(0);
            expect(scalar_add(0, 0)).toBe(0);
        });
    });

    describe('Vector Operations', () => {
        test('vector_add should add two vectors componentwise', () => {
            expect(vector_add([1, 2, 3], [4, 5, 6])).toEqual([5, 7, 9]);
            expect(vector_add([-1, 1], [1, -1])).toEqual([0, 0]);
        });

        test('vector_subtract should subtract two vectors componentwise', () => {
            expect(vector_subtract([5, 7, 9], [1, 2, 3])).toEqual([4, 5, 6]);
            expect(vector_subtract([1, 1], [1, 1])).toEqual([0, 0]);
        });

        test('vector_sum should sum multiple vectors', () => {
            const vectors = [[1, 2], [3, 4], [5, 6]];
            expect(vector_sum(vectors)).toEqual([9, 12]);
        });

        test('vector_sum should handle empty array', () => {
            expect(vector_sum([])).toEqual([]);
        });

        test('vector_sum should handle single vector', () => {
            expect(vector_sum([[1, 2, 3]])).toEqual([1, 2, 3]);
        });

        test('scalar_multiply should multiply vector by scalar', () => {
            expect(scalar_multiply(2, [1, 2, 3])).toEqual([2, 4, 6]);
            expect(scalar_multiply(0, [1, 2, 3])).toEqual([0, 0, 0]);
            expect(scalar_multiply(-1, [1, 2, 3])).toEqual([-1, -2, -3]);
        });

        test('vector_mean should compute mean of vectors', () => {
            const vectors = [[1, 2], [3, 4], [5, 6]];
            expect(vector_mean(vectors)).toEqual([3, 4]);
        });

        test('dot should compute dot product', () => {
            expect(dot([1, 2, 3], [4, 5, 6])).toBe(32);
            expect(dot([1, 0], [0, 1])).toBe(0);
        });

        test('sum_of_squares should compute sum of squares', () => {
            expect(sum_of_squares([1, 2, 3])).toBe(14);
            expect(sum_of_squares([0, 0, 0])).toBe(0);
        });

        test('magnitude should compute vector magnitude', () => {
            expect(magnitude([3, 4])).toBe(5);
            expect(magnitude([0, 0])).toBe(0);
        });

        test('squared_distance should compute squared distance', () => {
            expect(squared_distance([1, 2], [4, 6])).toBe(25);
            expect(squared_distance([0, 0], [0, 0])).toBe(0);
        });

        test('distance should compute euclidean distance', () => {
            expect(distance([1, 2], [4, 6])).toBe(5);
            expect(distance([0, 0], [0, 0])).toBe(0);
        });
    });

    describe('Matrix Operations', () => {
        const matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ];

        test('shape should return matrix dimensions', () => {
            expect(shape(matrix)).toEqual([3, 3]);
            expect(shape([[1, 2], [3, 4]])).toEqual([2, 2]);
            expect(shape([])).toEqual([0, 0]);
        });

        test('get_row should return specified row', () => {
            expect(get_row(matrix, 0)).toEqual([1, 2, 3]);
            expect(get_row(matrix, 1)).toEqual([4, 5, 6]);
        });

        test('get_column should return specified column', () => {
            expect(get_column(matrix, 0)).toEqual([1, 4, 7]);
            expect(get_column(matrix, 1)).toEqual([2, 5, 8]);
            expect(get_column(matrix, 2)).toEqual([3, 6, 9]);
        });

        test('make_matrix should create matrix with entry function', () => {
            const matrix2x2 = make_matrix(2, 2, (i, j) => i + j);
            expect(matrix2x2).toEqual([[0, 1], [1, 2]]);
        });

        test('is_diagonal should create identity matrix pattern', () => {
            expect(is_diagonal(0, 0)).toBe(1);
            expect(is_diagonal(1, 1)).toBe(1);
            expect(is_diagonal(0, 1)).toBe(0);
            expect(is_diagonal(1, 0)).toBe(0);
        });

        test('matrix_add should add matrices of same shape', () => {
            const matrixA = [[1, 2], [3, 4]];
            const matrixB = [[5, 6], [7, 8]];
            const result = matrix_add(matrixA, matrixB);
            expect(result).toEqual([[6, 8], [10, 12]]);
        });

        test('matrix_add should throw error for different shapes', () => {
            const matrixA = [[1, 2], [3, 4]];
            const matrixB = [[1, 2, 3], [4, 5, 6]];
            expect(() => matrix_add(matrixA, matrixB)).toThrow('cannot add matrices with different shapes');
        });
    });

    describe('Edge Cases', () => {
        test('should handle zero-length vectors', () => {
            expect(vector_add([], [])).toEqual([]);
            expect(vector_subtract([], [])).toEqual([]);
            expect(dot([], [])).toBe(0);
            expect(magnitude([])).toBe(0);
        });

        test('should handle large numbers', () => {
            const largeVector = [1e6, 1e6];
            expect(magnitude(largeVector)).toBeCloseTo(1.414213562e6, 5);
        });

        test('should handle negative numbers', () => {
            expect(vector_add([-1, -2], [-3, -4])).toEqual([-4, -6]);
            expect(magnitude([-3, -4])).toBe(5);
        });
    });
});
