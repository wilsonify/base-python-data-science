/* eslint-disable no-unused-vars */
const Service = require('./Service');

/**
* Description of the endpoint
*
* accuracyInput AccuracyInput  (optional)
* returns BigDecimal
* */
const accuracy = ({ accuracyInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        accuracyInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* bucketizeInput BucketizeInput  (optional)
* returns bucketize-output
* */
const bucketize = ({ bucketizeInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        bucketizeInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* correlationInput CorrelationInput  (optional)
* returns correlation-output
* */
const correlation = ({ correlationInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        correlationInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* correlationMatrixInput CorrelationMatrixInput  (optional)
* returns correlation_matrix-output
* */
const correlation_matrix = ({ correlationMatrixInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        correlationMatrixInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* covarianceInput CovarianceInput  (optional)
* returns covariance-output
* */
const covariance = ({ covarianceInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        covarianceInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* dataRangeInput DataRangeInput  (optional)
* returns data_range-output
* */
const data_range = ({ dataRangeInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        dataRangeInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* deMeanInput DeMeanInput  (optional)
* returns de_mean-output
* */
const de_mean = ({ deMeanInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        deMeanInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* differenceQuotientInput DifferenceQuotientInput  (optional)
* returns difference_quotient-output
* */
const difference_quotient = ({ differenceQuotientInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        differenceQuotientInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* distanceInput DistanceInput  (optional)
* returns distance-output
* */
const distance = ({ distanceInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        distanceInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* dotInput DotInput  (optional)
* returns dot-output
* */
const dot = ({ dotInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        dotInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* body Object  (optional)
* returns Object
* */
const echo = ({ body }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        body,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* estimateGradientInput EstimateGradientInput  (optional)
* returns estimate_gradient-output
* */
const estimate_gradient = ({ estimateGradientInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        estimateGradientInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* f1ScoreInput F1ScoreInput  (optional)
* returns BigDecimal
* */
const f1_score = ({ f1ScoreInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        f1ScoreInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* getColumnInput GetColumnInput  (optional)
* returns get_column-output
* */
const get_column = ({ getColumnInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        getColumnInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* getRowInput GetRowInput  (optional)
* returns get_row-output
* */
const get_row = ({ getRowInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        getRowInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* inRandomOrderInput InRandomOrderInput  (optional)
* returns List
* */
const in_random_order = ({ inRandomOrderInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        inRandomOrderInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* interquartileRangeInput InterquartileRangeInput  (optional)
* returns BigDecimal
* */
const interquartile_range = ({ interquartileRangeInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        interquartileRangeInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* magnitudeInput MagnitudeInput  (optional)
* returns BigDecimal
* */
const magnitude = ({ magnitudeInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        magnitudeInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* matrixAddInput MatrixAddInput  (optional)
* returns List
* */
const matrix_add = ({ matrixAddInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        matrixAddInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* use gradient descent to find theta that minimizes target function
*
* maximizeBatchInput MaximizeBatchInput  (optional)
* returns maximize_batch-output
* */
const maximize_batch = ({ maximizeBatchInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        maximizeBatchInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* maximizeStochasticInput MaximizeStochasticInput  (optional)
* returns maximize_stochastic-output
* */
const maximize_stochastic = ({ maximizeStochasticInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        maximizeStochasticInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* meanInput MeanInput  (optional)
* returns BigDecimal
* */
const mean = ({ meanInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        meanInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* medianInput MedianInput  (optional)
* returns BigDecimal
* */
const median = ({ medianInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        medianInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* minimizeBatchInput MinimizeBatchInput  (optional)
* returns minimize_batch-output
* */
const minimize_batch = ({ minimizeBatchInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        minimizeBatchInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* minimizeStochasticInput MinimizeStochasticInput  (optional)
* returns minimize_stochastic-output
* */
const minimize_stochastic = ({ minimizeStochasticInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        minimizeStochasticInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* modeInput ModeInput  (optional)
* returns List
* */
const mode = ({ modeInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        modeInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* add h to just the i-th element of v
*
* partialDifferenceQuotientInput PartialDifferenceQuotientInput  (optional)
* returns partial_difference_quotient-output
* */
const partial_difference_quotient = ({ partialDifferenceQuotientInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        partialDifferenceQuotientInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* precisionInput PrecisionInput  (optional)
* returns BigDecimal
* */
const precision = ({ precisionInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        precisionInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* quantileInput QuantileInput  (optional)
* returns BigDecimal
* */
const quantile = ({ quantileInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        quantileInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* recallInput RecallInput  (optional)
* returns BigDecimal
* */
const recall = ({ recallInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        recallInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* scalarMultiplyInput ScalarMultiplyInput  (optional)
* returns List
* */
const scalar_multiply = ({ scalarMultiplyInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        scalarMultiplyInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* shapeInput ShapeInput  (optional)
* returns shape-output
* */
const shape = ({ shapeInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        shapeInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* splitDataInput SplitDataInput  (optional)
* returns split_data-output
* */
const split_data = ({ splitDataInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        splitDataInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* sqrtInput SqrtInput  (optional)
* returns sqrt-output
* */
const sqrt = ({ sqrtInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        sqrtInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* squaredDistanceInput SquaredDistanceInput  (optional)
* returns List
* */
const squared_distance = ({ squaredDistanceInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        squaredDistanceInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* standardDeviationInput StandardDeviationInput  (optional)
* returns BigDecimal
* */
const standard_deviation = ({ standardDeviationInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        standardDeviationInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* strengthInput StrengthInput  (optional)
* returns strength-output
* */
const strength = ({ strengthInput }) => new Promise(
  async (resolve, reject) => {
    try {
        console.log('strengthInput = ', strengthInput)
        var actual, expected, eps, strength, payload;
        eps = 0.001;
        actual = strengthInput.actual;
        expected = strengthInput.expected;
        strength = actual / (expected + eps);
        payload={
          "expected":expected,
          "actual":actual,
          "strength": strength
          };
        resolve(Service.successResponse(payload));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* sumOfSquaresInput SumOfSquaresInput  (optional)
* returns BigDecimal
* */
const sum_of_squares = ({ sumOfSquaresInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        sumOfSquaresInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* trainTestSplitInput TrainTestSplitInput  (optional)
* returns train_test_split-output
* */
const train_test_split = ({ trainTestSplitInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        trainTestSplitInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* varianceInput VarianceInput  (optional)
* returns BigDecimal
* */
const variance = ({ varianceInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        varianceInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* vectorAddInput VectorAddInput  (optional)
* returns List
* */
const vector_add = ({ vectorAddInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        vectorAddInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* compute the vector whose i-th element is the mean of the i-th elements of the input vectors
*
* vectorMeanInput VectorMeanInput  (optional)
* returns List
* */
const vector_mean = ({ vectorMeanInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        vectorMeanInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* vectorSubtractInput VectorSubtractInput  (optional)
* returns List
* */
const vector_subtract = ({ vectorSubtractInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        vectorSubtractInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);
/**
* Description of the endpoint
*
* vectorSumInput VectorSumInput  (optional)
* returns List
* */
const vector_sum = ({ vectorSumInput }) => new Promise(
  async (resolve, reject) => {
    try {
      resolve(Service.successResponse({
        vectorSumInput,
      }));
    } catch (e) {
      reject(Service.rejectResponse(
        e.message || 'Invalid input',
        e.status || 405,
      ));
    }
  },
);

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
