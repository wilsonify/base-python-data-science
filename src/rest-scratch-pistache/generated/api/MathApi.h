/**
* Minimal Pistache
* This is a sample server
*
* The version of the OpenAPI document: 1.0.0
* 
*
* NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
* https://openapi-generator.tech
* Do not edit the class manually.
*/
/*
 * MathApi.h
 *
 * 
 */

#ifndef MathApi_H_
#define MathApi_H_


#include <pistache/http.h>
#include <pistache/router.h>
#include <pistache/http_headers.h>

#include <optional>
#include <utility>

#include "Accuracy_input.h"
#include "Bucketize_input.h"
#include "Bucketize_output.h"
#include "Correlation_input.h"
#include "Correlation_matrix_input.h"
#include "Correlation_matrix_output.h"
#include "Correlation_output.h"
#include "Covariance_input.h"
#include "Covariance_output.h"
#include "Data_range_input.h"
#include "Data_range_output.h"
#include "De_mean_input.h"
#include "De_mean_output.h"
#include "Difference_quotient_input.h"
#include "Difference_quotient_output.h"
#include "Distance_input.h"
#include "Distance_output.h"
#include "Dot_input.h"
#include "Dot_output.h"
#include "Estimate_gradient_input.h"
#include "Estimate_gradient_output.h"
#include "F1_score_input.h"
#include "Get_column_input.h"
#include "Get_column_output.h"
#include "Get_row_input.h"
#include "Get_row_output.h"
#include "In_random_order_input.h"
#include "Interquartile_range_input.h"
#include "Magnitude_input.h"
#include "Matrix_add_input.h"
#include "Maximize_batch_input.h"
#include "Maximize_batch_output.h"
#include "Maximize_stochastic_input.h"
#include "Maximize_stochastic_output.h"
#include "Mean_input.h"
#include "Median_input.h"
#include "Minimize_batch_input.h"
#include "Minimize_batch_output.h"
#include "Minimize_stochastic_input.h"
#include "Minimize_stochastic_output.h"
#include "Mode_input.h"
#include "Partial_difference_quotient_input.h"
#include "Partial_difference_quotient_output.h"
#include "Precision_input.h"
#include "Quantile_input.h"
#include "Recall_input.h"
#include "Scalar_multiply_input.h"
#include "Shape_input.h"
#include "Shape_output.h"
#include "Split_data_input.h"
#include "Split_data_output.h"
#include "Sqrt_input.h"
#include "Sqrt_output.h"
#include "Squared_distance_input.h"
#include "Standard_deviation_input.h"
#include "Strength_input.h"
#include "Strength_output.h"
#include "Sum_of_squares_input.h"
#include "Train_test_split_input.h"
#include "Train_test_split_output.h"
#include "Variance_input.h"
#include "Vector_add_input.h"
#include "Vector_mean_input.h"
#include "Vector_subtract_input.h"
#include "Vector_sum_input.h"
#include <string>

namespace org::openapitools::server::api
{

class  MathApi {
public:
    explicit MathApi(const std::shared_ptr<Pistache::Rest::Router>& rtr);
    virtual ~MathApi() = default;
    void init();

    static const std::string base;

private:
    void setupRoutes();

    void accuracy_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void bucketize_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void correlation_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void correlation_matrix_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void covariance_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void data_range_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void de_mean_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void difference_quotient_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void distance_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void dot_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void echo_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void estimate_gradient_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void f1_score_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void get_column_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void get_row_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void in_random_order_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void interquartile_range_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void magnitude_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void matrix_add_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void maximize_batch_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void maximize_stochastic_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void mean_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void median_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void minimize_batch_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void minimize_stochastic_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void mode_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void partial_difference_quotient_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void precision_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void quantile_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void recall_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void scalar_multiply_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void shape_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void split_data_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void sqrt_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void squared_distance_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void standard_deviation_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void strength_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void sum_of_squares_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void train_test_split_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void variance_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void vector_add_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void vector_mean_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void vector_subtract_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void vector_sum_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);
    void math_api_default_handler(const Pistache::Rest::Request &request, Pistache::Http::ResponseWriter response);

    const std::shared_ptr<Pistache::Rest::Router> router;

    /// <summary>
    /// Helper function to handle unexpected Exceptions during Parameter parsing and validation.
    /// May be overridden to return custom error formats. This is called inside a catch block.
    /// Important: When overriding, do not call `throw ex;`, but instead use `throw;`.
    /// </summary>
    virtual std::pair<Pistache::Http::Code, std::string> handleParsingException(const std::exception& ex) const noexcept;

    /// <summary>
    /// Helper function to handle unexpected Exceptions during processing of the request in handler functions.
    /// May be overridden to return custom error formats. This is called inside a catch block.
    /// Important: When overriding, do not call `throw ex;`, but instead use `throw;`.
    /// </summary>
    virtual std::pair<Pistache::Http::Code, std::string> handleOperationException(const std::exception& ex) const noexcept;

    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="accuracyInput"> (optional)</param>
    virtual void accuracy(const org::openapitools::server::model::Accuracy_input &accuracyInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="bucketizeInput"> (optional)</param>
    virtual void bucketize(const org::openapitools::server::model::Bucketize_input &bucketizeInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="correlationInput"> (optional)</param>
    virtual void correlation(const org::openapitools::server::model::Correlation_input &correlationInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="correlationMatrixInput"> (optional)</param>
    virtual void correlation_matrix(const org::openapitools::server::model::Correlation_matrix_input &correlationMatrixInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="covarianceInput"> (optional)</param>
    virtual void covariance(const org::openapitools::server::model::Covariance_input &covarianceInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="dataRangeInput"> (optional)</param>
    virtual void data_range(const org::openapitools::server::model::Data_range_input &dataRangeInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="deMeanInput"> (optional)</param>
    virtual void de_mean(const org::openapitools::server::model::De_mean_input &deMeanInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="differenceQuotientInput"> (optional)</param>
    virtual void difference_quotient(const org::openapitools::server::model::Difference_quotient_input &differenceQuotientInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="distanceInput"> (optional)</param>
    virtual void distance(const org::openapitools::server::model::Distance_input &distanceInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="dotInput"> (optional)</param>
    virtual void dot(const org::openapitools::server::model::Dot_input &dotInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="body"> (optional)</param>
    virtual void echo(const std::string &body, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="estimateGradientInput"> (optional)</param>
    virtual void estimate_gradient(const org::openapitools::server::model::Estimate_gradient_input &estimateGradientInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="f1ScoreInput"> (optional)</param>
    virtual void f1_score(const org::openapitools::server::model::F1_score_input &f1ScoreInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="getColumnInput"> (optional)</param>
    virtual void get_column(const org::openapitools::server::model::Get_column_input &getColumnInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="getRowInput"> (optional)</param>
    virtual void get_row(const org::openapitools::server::model::Get_row_input &getRowInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="inRandomOrderInput"> (optional)</param>
    virtual void in_random_order(const org::openapitools::server::model::In_random_order_input &inRandomOrderInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="interquartileRangeInput"> (optional)</param>
    virtual void interquartile_range(const org::openapitools::server::model::Interquartile_range_input &interquartileRangeInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="magnitudeInput"> (optional)</param>
    virtual void magnitude(const org::openapitools::server::model::Magnitude_input &magnitudeInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="matrixAddInput"> (optional)</param>
    virtual void matrix_add(const org::openapitools::server::model::Matrix_add_input &matrixAddInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// use gradient descent to find theta that minimizes target function
    /// </remarks>
    /// <param name="maximizeBatchInput"> (optional)</param>
    virtual void maximize_batch(const org::openapitools::server::model::Maximize_batch_input &maximizeBatchInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="maximizeStochasticInput"> (optional)</param>
    virtual void maximize_stochastic(const org::openapitools::server::model::Maximize_stochastic_input &maximizeStochasticInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="meanInput"> (optional)</param>
    virtual void mean(const org::openapitools::server::model::Mean_input &meanInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="medianInput"> (optional)</param>
    virtual void median(const org::openapitools::server::model::Median_input &medianInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="minimizeBatchInput"> (optional)</param>
    virtual void minimize_batch(const org::openapitools::server::model::Minimize_batch_input &minimizeBatchInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="minimizeStochasticInput"> (optional)</param>
    virtual void minimize_stochastic(const org::openapitools::server::model::Minimize_stochastic_input &minimizeStochasticInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="modeInput"> (optional)</param>
    virtual void mode(const org::openapitools::server::model::Mode_input &modeInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// add h to just the i-th element of v
    /// </remarks>
    /// <param name="partialDifferenceQuotientInput"> (optional)</param>
    virtual void partial_difference_quotient(const org::openapitools::server::model::Partial_difference_quotient_input &partialDifferenceQuotientInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="precisionInput"> (optional)</param>
    virtual void precision(const org::openapitools::server::model::Precision_input &precisionInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="quantileInput"> (optional)</param>
    virtual void quantile(const org::openapitools::server::model::Quantile_input &quantileInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="recallInput"> (optional)</param>
    virtual void recall(const org::openapitools::server::model::Recall_input &recallInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="scalarMultiplyInput"> (optional)</param>
    virtual void scalar_multiply(const org::openapitools::server::model::Scalar_multiply_input &scalarMultiplyInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="shapeInput"> (optional)</param>
    virtual void shape(const org::openapitools::server::model::Shape_input &shapeInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="splitDataInput"> (optional)</param>
    virtual void split_data(const org::openapitools::server::model::Split_data_input &splitDataInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="sqrtInput"> (optional)</param>
    virtual void sqrt(const org::openapitools::server::model::Sqrt_input &sqrtInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="squaredDistanceInput"> (optional)</param>
    virtual void squared_distance(const org::openapitools::server::model::Squared_distance_input &squaredDistanceInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="standardDeviationInput"> (optional)</param>
    virtual void standard_deviation(const org::openapitools::server::model::Standard_deviation_input &standardDeviationInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="strengthInput"> (optional)</param>
    virtual void strength(const org::openapitools::server::model::Strength_input &strengthInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="sumOfSquaresInput"> (optional)</param>
    virtual void sum_of_squares(const org::openapitools::server::model::Sum_of_squares_input &sumOfSquaresInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="trainTestSplitInput"> (optional)</param>
    virtual void train_test_split(const org::openapitools::server::model::Train_test_split_input &trainTestSplitInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="varianceInput"> (optional)</param>
    virtual void variance(const org::openapitools::server::model::Variance_input &varianceInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="vectorAddInput"> (optional)</param>
    virtual void vector_add(const org::openapitools::server::model::Vector_add_input &vectorAddInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// compute the vector whose i-th element is the mean of the i-th elements of the input vectors
    /// </remarks>
    /// <param name="vectorMeanInput"> (optional)</param>
    virtual void vector_mean(const org::openapitools::server::model::Vector_mean_input &vectorMeanInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="vectorSubtractInput"> (optional)</param>
    virtual void vector_subtract(const org::openapitools::server::model::Vector_subtract_input &vectorSubtractInput, Pistache::Http::ResponseWriter &response) = 0;
    /// <summary>
    /// 
    /// </summary>
    /// <remarks>
    /// Description of the endpoint
    /// </remarks>
    /// <param name="vectorSumInput"> (optional)</param>
    virtual void vector_sum(const org::openapitools::server::model::Vector_sum_input &vectorSumInput, Pistache::Http::ResponseWriter &response) = 0;

};

} // namespace org::openapitools::server::api

#endif /* MathApi_H_ */
