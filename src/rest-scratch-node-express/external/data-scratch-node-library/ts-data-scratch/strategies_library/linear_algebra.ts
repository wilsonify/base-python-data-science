import {
    distance,
    dot,
    get_column,
    get_row,
    magnitude,
    matrix_add,
    scalar_multiply,
    shape,
    squared_distance,
    sum_of_squares,
    vector_add,
    vector_mean,
    vector_subtract,
    vector_sum
} from "../linear_algebra";
import { NumericArray } from "../type-helpers";

interface Idistance { v: NumericArray, w: NumericArray }

const distance_strategy = (body: Idistance) => new Promise(
    async (resolve, reject) => {
        try {
            var v = body.v
            var w = body.w
            var result = distance(v, w)
            resolve(console.log(result));
        } catch (e) {
            reject(
                console.log(`unable to resolve distance ${e}`)
            );
        }

    })

interface Idot { v: NumericArray, w: NumericArray }
const dot_strategy = (body: Idot) => new Promise(
    async (resolve, reject) => {
        try {
            var v = body.v
            var w = body.w
            var result = dot(v, w)
            resolve(console.log(result));
        } catch (e) {
            reject(
                console.log(`unable to resolve dot ${e}`)
            );
        }
    }
)

interface Iget_column { mat: number[][], col: number }
const get_column_strategy = (body: Iget_column) => new Promise(
    async (resolve, reject) => {
        try {
            var mat = body.mat
            var col = body.col
            var result = get_column(mat, col)
            resolve(console.log(result));
        } catch (e) {
            reject(
                console.log(`unable to resolve get_column ${e}`)
            );
        }
    }
)

interface Iget_row { mat: number[][], row: number }
const get_row_strategy = (body: Iget_row) => new Promise(
    async (resolve, reject) => {
        try {
            var mat = body.mat
            var row = body.row
            var result = get_row(mat, row)
            resolve(console.log(result));
        } catch (e) {
            reject(
                console.log(`unable to resolve get_row ${e}`)
            );
        }
    }
)

interface Imagnitude { v: any; }
const magnitude_strategy = (body: Imagnitude) => new Promise(
    async (resolve, reject) => {
        try {
            var v = body.v
            var result = magnitude(v)
            resolve(console.log(result));
        } catch (e) {
            reject(
                console.log(`unable to resolve magnitude ${e}`)
            );
        }
    }
)

interface Imatrix_add { mat1: number[][]; mat2: number[][]; }
const matrix_add_strategy = (body: Imatrix_add) => new Promise(
    async (resolve, reject) => {
        try {
            var mat1 = body.mat1
            var mat2 = body.mat2
            var result = matrix_add(mat1, mat2)
            resolve(console.log(result));
        } catch (e) {
            reject(
                console.log(`unable to resolve matrix_add ${e}`)
            );
        }
    }
)

interface Iscalar_multiply { c: any; v: any; }
const scalar_multiply_strategy = (body: Iscalar_multiply) => new Promise(
    async (resolve, reject) => {
        try {
            var c = body.c
            var v = body.v
            var result = scalar_multiply(c, v)
            resolve(console.log(result));
        } catch (e) {
            reject(
                console.log(`unable to resolve scalar_multiply ${e}`)
            );
        }
    }
)

interface Ishape { mat: any; }
const shape_strategy = (body: Ishape) => new Promise(
    async (resolve, reject) => {
        try {
            var mat = body.mat
            var result = shape(mat)
            resolve(console.log(result));
        } catch (e) {
            reject(
                console.log(`unable to resolve shape ${e}`)
            );
        }
    }
)

interface Isquared_distance { v: any; w: any; }
const squared_distance_strategy = (body: Isquared_distance) => new Promise(
    async (resolve, reject) => {
        try {
            var v = body.v
            var w = body.w
            var result = squared_distance(v, w)
            resolve(console.log(result));
        } catch (e) {
            reject(
                console.log(`unable to resolve squared_distance ${e}`)
            );
        }
    }
)

interface Isum_of_squares { v: any; }
const sum_of_squares_strategy = (body: Isum_of_squares) => new Promise(
    async (resolve, reject) => {
        try {
            var v = body.v
            var result = sum_of_squares(v)
            resolve(console.log(result));
        } catch (e) {
            reject(
                console.log(`unable to resolve sum_of_squares ${e}`)
            );
        }
    }
)

interface Ivector_add { v: any; w: any; }
const vector_add_strategy = (body: Ivector_add) => new Promise(
    async (resolve, reject) => {
        try {
            var v = body.v
            var w = body.w
            var result = vector_add(v, w)
            resolve(console.log(result));
        } catch (e) {
            reject(
                console.log(`unable to resolve vector_add ${e}`)
            );
        }
    }
)

interface Ivector_mean { vectors: any; }
const vector_mean_strategy = (body: Ivector_mean) => new Promise(
    async (resolve, reject) => {
        try {
            var vectors = body.vectors
            var result = vector_mean(vectors)
            resolve(console.log(result));
        } catch (e) {
            reject(
                console.log(`unable to resolve vector_mean ${e}`)
            );
        }
    }
)

interface Ivector_subtract { v: any; w: any; }
const vector_subtract_strategy = (body: Ivector_subtract) => new Promise(
    async (resolve, reject) => {
        try {
            var v = body.v
            var w = body.w
            var result = vector_subtract(v, w)
            resolve(console.log(result));
        } catch (e) {
            reject(
                console.log(`unable to resolve vector_subtract ${e}`)
            );
        }
    }
)

interface Ivector_sum { vectors: any; }
const vector_sum_strategy = (body: Ivector_sum) => new Promise(
    async (resolve, reject) => {
        try {
            var vectors = body.vectors
            var result = vector_sum(vectors)
            resolve(console.log(result));
        } catch (e) {
            reject(
                console.log(`unable to resolve vector_sum ${e}`)
            );
        }
    }
)