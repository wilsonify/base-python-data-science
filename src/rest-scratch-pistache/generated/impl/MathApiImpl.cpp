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

#include "MathApiImpl.h"

namespace org {
namespace openapitools {
namespace server {
namespace api {

using namespace org::openapitools::server::model;

MathApiImpl::MathApiImpl(const std::shared_ptr<Pistache::Rest::Router>& rtr)
    : MathApi(rtr)
{
}

void MathApiImpl::accuracy(const Accuracy_input &accuracyInput, Pistache::Http::ResponseWriter &response) {
    double tp;
    double fp;
    double fn;
    double tn;    
    double result;
    double eps = 0.001;
    nlohmann::json json_to_dump;    
    std::string string_to_send;

    tp=accuracyInput.getTp();
    fp=accuracyInput.getFp();
    fn=accuracyInput.getFn();
    tn=accuracyInput.getTn();

    result = (tp + tn) / (tp + fp + fn + tn + eps);

    nlohmann::to_json(json_to_dump, result);
    string_to_send = json_to_dump.dump();
    response.send(Pistache::Http::Code::Ok, string_to_send);
}
void MathApiImpl::bucketize(const Bucketize_input &bucketizeInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::correlation(const Correlation_input &correlationInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::correlation_matrix(const Correlation_matrix_input &correlationMatrixInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::covariance(const Covariance_input &covarianceInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::data_range(const Data_range_input &dataRangeInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::de_mean(const De_mean_input &deMeanInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::difference_quotient(const Difference_quotient_input &differenceQuotientInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::distance(const Distance_input &distanceInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::dot(const Dot_input &dotInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::echo(const std::string &body, Pistache::Http::ResponseWriter &response) {
    nlohmann::json json_to_dump;
    std::string string_to_send;
    std::string result = body;
    nlohmann::to_json(json_to_dump, result);
    string_to_send = json_to_dump.dump();
    response.send(Pistache::Http::Code::Ok, string_to_send);
}
void MathApiImpl::estimate_gradient(const Estimate_gradient_input &estimateGradientInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::f1_score(const F1_score_input &f1ScoreInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::get_column(const Get_column_input &getColumnInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::get_row(const Get_row_input &getRowInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::in_random_order(const In_random_order_input &inRandomOrderInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::interquartile_range(const Interquartile_range_input &interquartileRangeInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::magnitude(const Magnitude_input &magnitudeInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::matrix_add(const Matrix_add_input &matrixAddInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::maximize_batch(const Maximize_batch_input &maximizeBatchInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::maximize_stochastic(const Maximize_stochastic_input &maximizeStochasticInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::mean(const Mean_input &meanInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::median(const Median_input &medianInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::minimize_batch(const Minimize_batch_input &minimizeBatchInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::minimize_stochastic(const Minimize_stochastic_input &minimizeStochasticInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::mode(const Mode_input &modeInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::partial_difference_quotient(const Partial_difference_quotient_input &partialDifferenceQuotientInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::precision(const Precision_input &precisionInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::quantile(const Quantile_input &quantileInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::recall(const Recall_input &recallInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::scalar_multiply(const Scalar_multiply_input &scalarMultiplyInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::shape(const Shape_input &shapeInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::split_data(const Split_data_input &splitDataInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::sqrt(const Sqrt_input &sqrtInput, Pistache::Http::ResponseWriter &response) {
    double x;
    Sqrt_output result;    
    nlohmann::json json_to_dump;    
    std::string string_to_send;
        
    x=sqrtInput.getX();
    result.setX(x);
    result.setResult(std::sqrt(x));  
    
    nlohmann::to_json(json_to_dump, result);
    string_to_send = json_to_dump.dump();
    response.send(Pistache::Http::Code::Ok, string_to_send);
}
void MathApiImpl::squared_distance(const Squared_distance_input &squaredDistanceInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::standard_deviation(const Standard_deviation_input &standardDeviationInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::strength(const Strength_input &strengthInput, Pistache::Http::ResponseWriter &response) {
    double expected;
    double actual;        
    double result;    
    double eps=0.01;
    nlohmann::json json_to_dump;
    std::string string_to_send;
    actual=strengthInput.getActual();
    expected=strengthInput.getExpected();
    result = actual / (expected+eps);
    nlohmann::to_json(json_to_dump, result);
    string_to_send = json_to_dump.dump();
    response.send(Pistache::Http::Code::Ok, string_to_send);
}
void MathApiImpl::sum_of_squares(const Sum_of_squares_input &sumOfSquaresInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::train_test_split(const Train_test_split_input &trainTestSplitInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::variance(const Variance_input &varianceInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::vector_add(const Vector_add_input &vectorAddInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::vector_mean(const Vector_mean_input &vectorMeanInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::vector_subtract(const Vector_subtract_input &vectorSubtractInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}
void MathApiImpl::vector_sum(const Vector_sum_input &vectorSumInput, Pistache::Http::ResponseWriter &response) {
    response.send(Pistache::Http::Code::Ok, "Do some magic\n");
}

}
}
}
}

