/**
 * The MathController file is a very simple one, which does not need to be changed manually,
 * unless there's a case where business logic routes the request to an entity which is not
 * the service.
 * The heavy lifting of the Controller item is done in Request.js - that is where request
 * parameters are extracted and sent to the service, and where response is handled.
 */

const Controller = require('./Controller');
const service = require('../services/MathService');
const accuracy = async (request, response) => {
  await Controller.handleRequest(request, response, service.accuracy);
};

const bucketize = async (request, response) => {
  await Controller.handleRequest(request, response, service.bucketize);
};

const correlation = async (request, response) => {
  await Controller.handleRequest(request, response, service.correlation);
};

const correlation_matrix = async (request, response) => {
  await Controller.handleRequest(request, response, service.correlation_matrix);
};

const covariance = async (request, response) => {
  await Controller.handleRequest(request, response, service.covariance);
};

const data_range = async (request, response) => {
  await Controller.handleRequest(request, response, service.data_range);
};

const de_mean = async (request, response) => {
  await Controller.handleRequest(request, response, service.de_mean);
};

const difference_quotient = async (request, response) => {
  await Controller.handleRequest(request, response, service.difference_quotient);
};

const distance = async (request, response) => {
  await Controller.handleRequest(request, response, service.distance);
};

const dot = async (request, response) => {
  await Controller.handleRequest(request, response, service.dot);
};

const echo = async (request, response) => {
  await Controller.handleRequest(request, response, service.echo);
};

const estimate_gradient = async (request, response) => {
  await Controller.handleRequest(request, response, service.estimate_gradient);
};

const f1_score = async (request, response) => {
  await Controller.handleRequest(request, response, service.f1_score);
};

const get_column = async (request, response) => {
  await Controller.handleRequest(request, response, service.get_column);
};

const get_row = async (request, response) => {
  await Controller.handleRequest(request, response, service.get_row);
};

const in_random_order = async (request, response) => {
  await Controller.handleRequest(request, response, service.in_random_order);
};

const interquartile_range = async (request, response) => {
  await Controller.handleRequest(request, response, service.interquartile_range);
};

const magnitude = async (request, response) => {
  await Controller.handleRequest(request, response, service.magnitude);
};

const matrix_add = async (request, response) => {
  await Controller.handleRequest(request, response, service.matrix_add);
};

const maximize_batch = async (request, response) => {
  await Controller.handleRequest(request, response, service.maximize_batch);
};

const maximize_stochastic = async (request, response) => {
  await Controller.handleRequest(request, response, service.maximize_stochastic);
};

const mean = async (request, response) => {
  await Controller.handleRequest(request, response, service.mean);
};

const median = async (request, response) => {
  await Controller.handleRequest(request, response, service.median);
};

const minimize_batch = async (request, response) => {
  await Controller.handleRequest(request, response, service.minimize_batch);
};

const minimize_stochastic = async (request, response) => {
  await Controller.handleRequest(request, response, service.minimize_stochastic);
};

const mode = async (request, response) => {
  await Controller.handleRequest(request, response, service.mode);
};

const partial_difference_quotient = async (request, response) => {
  await Controller.handleRequest(request, response, service.partial_difference_quotient);
};

const precision = async (request, response) => {
  await Controller.handleRequest(request, response, service.precision);
};

const quantile = async (request, response) => {
  await Controller.handleRequest(request, response, service.quantile);
};

const recall = async (request, response) => {
  await Controller.handleRequest(request, response, service.recall);
};

const scalar_multiply = async (request, response) => {
  await Controller.handleRequest(request, response, service.scalar_multiply);
};

const shape = async (request, response) => {
  await Controller.handleRequest(request, response, service.shape);
};

const split_data = async (request, response) => {
  await Controller.handleRequest(request, response, service.split_data);
};

const sqrt = async (request, response) => {
  await Controller.handleRequest(request, response, service.sqrt);
};

const squared_distance = async (request, response) => {
  await Controller.handleRequest(request, response, service.squared_distance);
};

const standard_deviation = async (request, response) => {
  await Controller.handleRequest(request, response, service.standard_deviation);
};

const strength = async (request, response) => {
  await Controller.handleRequest(request, response, service.strength);

};

const sum_of_squares = async (request, response) => {
  await Controller.handleRequest(request, response, service.sum_of_squares);
};

const train_test_split = async (request, response) => {
  await Controller.handleRequest(request, response, service.train_test_split);
};

const variance = async (request, response) => {
  await Controller.handleRequest(request, response, service.variance);
};

const vector_add = async (request, response) => {
  await Controller.handleRequest(request, response, service.vector_add);
};

const vector_mean = async (request, response) => {
  await Controller.handleRequest(request, response, service.vector_mean);
};

const vector_subtract = async (request, response) => {
  await Controller.handleRequest(request, response, service.vector_subtract);
};

const vector_sum = async (request, response) => {
  await Controller.handleRequest(request, response, service.vector_sum);
};


module.exports = {
  accuracy,
  bucketize,
  correlation,
  correlation_matrix,
  covariance,
  data_range,
  de_mean,
  difference_quotient,
  distance,
  dot,
  echo,
  estimate_gradient,
  f1_score,
  get_column,
  get_row,
  in_random_order,
  interquartile_range,
  magnitude,
  matrix_add,
  maximize_batch,
  maximize_stochastic,
  mean,
  median,
  minimize_batch,
  minimize_stochastic,
  mode,
  partial_difference_quotient,
  precision,
  quantile,
  recall,
  scalar_multiply,
  shape,
  split_data,
  sqrt,
  squared_distance,
  standard_deviation,
  strength,
  sum_of_squares,
  train_test_split,
  variance,
  vector_add,
  vector_mean,
  vector_subtract,
  vector_sum,
};
