import { BivaritateFunction } from "./type-helpers"

export function scalar_add(a: number, b: number): number {
  return a + b
}

// functions for working with vectors

export function vector_add(v: Array<number>, w: Array<number>) {
  //"""adds two vectors componentwise"""

  var v_i: number;
  var w_i: number;
  var result = [];

  for (var i = 0; i < v.length; i += 1) {
    v_i = v[i];
    w_i = w[i];
    result.push(v_i + w_i);
  }

  return result;
}

export function vector_subtract(v: Array<number>, w: Array<number>) {
  //"""subtracts two vectors componentwise"""
  var v_i: number;
  var w_i: number;
  var result = [];
  for (var i = 0; i < v.length; i += 1) {
    v_i = v[i];
    w_i = w[i];
    result.push(v_i - w_i);
  }
  return result;
}

export function vector_sum(vectors: Array<Array<number>>) {
  return vector_add(vectors[0], vectors[1]);
}

export function scalar_multiply(c: number, v: Array<number>) {
  var v_i: number;
  var result = [];
  for (var i = 0; i < v.length; i += 1) {
    v_i = v[i];
    result.push(c * v_i);
  }

  return result;
}

export function vector_mean(vectors: Array<Array<number>>) {
  //"""compute the vector whose i-th element is the mean of the i-th elements of the input vectors"""
  var n = vectors.length
  return scalar_multiply(1 / n, vector_sum(vectors))
}

export function dot(v: Array<number>, w: Array<number>): number {
  //"""v_1 * w_1 + ... + v_n * w_n"""
  var result = 0;
  for (var i = 0; i < v.length; i += 1) {
    var v_i = v[i];
    var w_i = w[i];
    result += v_i * w_i;
  }
  return result;
}

export function sum_of_squares(v: Array<number>) {
  //"""v_1 * v_1 + ... + v_n * v_n"""
  return dot(v, v)
}

export function magnitude(v: Array<number>) {
  return Math.sqrt(sum_of_squares(v))
}

export function squared_distance(v: Array<number>, w: Array<number>) {
  return sum_of_squares(vector_subtract(v, w))
}


export function distance(v: Array<number>, w: Array<number>) {
  return Math.sqrt(squared_distance(v, w))
}


//functions for working with matrices

export function shape(a_matrix: Array<Array<number>>) {
  var num_cols, num_rows;
  num_rows = a_matrix.length;
  num_cols = a_matrix ? a_matrix[0].length : 0;
  return [num_rows, num_cols];
}

export function get_row(a_matrix: Array<Array<number>>, i: number) {
  return a_matrix[i]
}

export function get_column(a_matrix: Array<Array<number>>, j: number) {
  var result = [];
  for (var i = 0; i < a_matrix.length; i += 1) {
    var A_i = a_matrix[i]
    result.push(A_i[j])
  }
  return result
}


export function make_matrix(num_rows: number, num_cols: number, entry_fn: BivaritateFunction) {
  //"""returns a num_rows x num_cols matrix whose (i,j)-th entry is entry_fn(i, j)"""
  var result = [];
  for (var i = 0, _pj_a = num_rows; i < _pj_a; i += 1) {
    var row = [];
    for (var j = 0, _pj_b = num_cols; j < _pj_b; j += 1) {
      row.push(entry_fn(i, j));
    }
    result.push(row);
  }
  return result;
}



export function is_diagonal(i: number, j: number) {
  //"""1's on the 'diagonal', 0's everywhere else"""
  return i === j ? 1 : 0;
}

const identity_matrix = make_matrix(5, 5, is_diagonal)

export function matrix_add(a_matrix: Array<Array<number>>, b_matrix: Array<Array<number>>): Array<Array<number>> {
  var num_cols, num_rows;
  if (shape(a_matrix) !== shape(b_matrix)) {
    throw new Error("cannot add matrices with different shapes");
  }
  [num_rows, num_cols] = shape(a_matrix);
  function entry_fn(i: number, j: number) {
    return a_matrix[i][j] + b_matrix[i][j];
  }
  return make_matrix(num_rows, num_cols, entry_fn);
}

