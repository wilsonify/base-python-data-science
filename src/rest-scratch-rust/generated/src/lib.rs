#![allow(missing_docs, trivial_casts, unused_variables, unused_mut, unused_imports, unused_extern_crates, non_camel_case_types)]
#![allow(unused_imports, unused_attributes)]
#![allow(clippy::derive_partial_eq_without_eq, clippy::blacklisted_name)]

use async_trait::async_trait;
use futures::Stream;
use std::error::Error;
use std::task::{Poll, Context};
use swagger::{ApiError, ContextWrapper};
use serde::{Serialize, Deserialize};

type ServiceError = Box<dyn Error + Send + Sync + 'static>;

pub const BASE_PATH: &str = "/v2";
pub const API_VERSION: &str = "1.0.0";

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum AccuracyResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (f64)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum BucketizeResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::BucketizeOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum CorrelationResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::CorrelationOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum CorrelationMatrixResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::CorrelationMatrixOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum CovarianceResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::CovarianceOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum DataRangeResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::DataRangeOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum DeMeanResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::DeMeanOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum DifferenceQuotientResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::DifferenceQuotientOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum DistanceResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::DistanceOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum DotResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::DotOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum EchoResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (serde_json::Value)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum EstimateGradientResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::EstimateGradientOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum F1ScoreResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (f64)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum GetColumnResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::GetColumnOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum GetRowResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::GetRowOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum InRandomOrderResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (Vec<f64>)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum InterquartileRangeResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (f64)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum MagnitudeResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (f64)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum MatrixAddResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (Vec<Vec<f64>>)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum MaximizeBatchResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::MaximizeBatchOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum MaximizeStochasticResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::MaximizeStochasticOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum MeanResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (f64)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum MedianResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (f64)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum MinimizeBatchResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::MinimizeBatchOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum MinimizeStochasticResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::MinimizeStochasticOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum ModeResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (Vec<f64>)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum PartialDifferenceQuotientResponse {
    /// v with h added to just the i-th element
    VWithHAddedToJustTheI
    (models::PartialDifferenceQuotientOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum PrecisionResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (f64)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum QuantileResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (f64)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum RecallResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (f64)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum ScalarMultiplyResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (Vec<Vec<f64>>)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum ShapeResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::ShapeOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum SplitDataResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::SplitDataOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum SqrtResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::SqrtOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum SquaredDistanceResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (Vec<f64>)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum StandardDeviationResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (f64)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum StrengthResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::StrengthOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum SumOfSquaresResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (f64)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum TrainTestSplitResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (models::TrainTestSplitOutput)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum VarianceResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (f64)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum VectorAddResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (Vec<f64>)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum VectorMeanResponse {
    /// success
    Success
    (Vec<f64>)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum VectorSubtractResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (Vec<f64>)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum VectorSumResponse {
    /// Description of this response.
    DescriptionOfThisResponse
    (Vec<f64>)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum AddPetResponse {
    /// Invalid input
    InvalidInput
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
#[must_use]
pub enum DeletePetResponse {
    /// Invalid ID supplied
    InvalidIDSupplied
    ,
    /// Pet not found
    PetNotFound
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
#[must_use]
pub enum FindPetsByStatusResponse {
    /// successful operation
    SuccessfulOperation
    (Vec<models::Pet>)
    ,
    /// Invalid status value
    InvalidStatusValue
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
#[must_use]
pub enum FindPetsByTagsResponse {
    /// successful operation
    SuccessfulOperation
    (Vec<models::Pet>)
    ,
    /// Invalid tag value
    InvalidTagValue
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
#[must_use]
pub enum GetPetByIdResponse {
    /// successful operation
    SuccessfulOperation
    (models::Pet)
    ,
    /// Invalid ID supplied
    InvalidIDSupplied
    ,
    /// Pet not found
    PetNotFound
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
#[must_use]
pub enum UpdatePetResponse {
    /// Invalid ID supplied
    InvalidIDSupplied
    ,
    /// Pet not found
    PetNotFound
    ,
    /// Validation exception
    ValidationException
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum UpdatePetWithFormResponse {
    /// Invalid input
    InvalidInput
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum UploadFileResponse {
    /// successful operation
    SuccessfulOperation
    (models::ApiResponse)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
#[must_use]
pub enum DeleteOrderResponse {
    /// Invalid ID supplied
    InvalidIDSupplied
    ,
    /// Order not found
    OrderNotFound
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum GetInventoryResponse {
    /// successful operation
    SuccessfulOperation
    (std::collections::HashMap<String, i32>)
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
#[must_use]
pub enum GetOrderByIdResponse {
    /// successful operation
    SuccessfulOperation
    (models::Order)
    ,
    /// Invalid ID supplied
    InvalidIDSupplied
    ,
    /// Order not found
    OrderNotFound
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
#[must_use]
pub enum PlaceOrderResponse {
    /// successful operation
    SuccessfulOperation
    (models::Order)
    ,
    /// Invalid Order
    InvalidOrder
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum CreateUserResponse {
    /// successful operation
    SuccessfulOperation
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum CreateUsersWithArrayInputResponse {
    /// successful operation
    SuccessfulOperation
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum CreateUsersWithListInputResponse {
    /// successful operation
    SuccessfulOperation
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
#[must_use]
pub enum DeleteUserResponse {
    /// Invalid username supplied
    InvalidUsernameSupplied
    ,
    /// User not found
    UserNotFound
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
#[must_use]
pub enum GetUserByNameResponse {
    /// successful operation
    SuccessfulOperation
    (models::User)
    ,
    /// Invalid username supplied
    InvalidUsernameSupplied
    ,
    /// User not found
    UserNotFound
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
#[must_use]
pub enum LoginUserResponse {
    /// successful operation
    SuccessfulOperation
    {
        body: String,
        x_rate_limit:
        Option<
        i32
        >
        ,
        x_expires_after:
        Option<
        chrono::DateTime::<chrono::Utc>
        >
    }
    ,
    /// Invalid username/password supplied
    InvalidUsername
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
pub enum LogoutUserResponse {
    /// successful operation
    SuccessfulOperation
}

#[derive(Debug, PartialEq, Serialize, Deserialize)]
#[must_use]
pub enum UpdateUserResponse {
    /// Invalid user supplied
    InvalidUserSupplied
    ,
    /// User not found
    UserNotFound
}

/// API
#[async_trait]
#[allow(clippy::too_many_arguments, clippy::ptr_arg)]
pub trait Api<C: Send + Sync> {
    fn poll_ready(&self, _cx: &mut Context) -> Poll<Result<(), Box<dyn Error + Send + Sync + 'static>>> {
        Poll::Ready(Ok(()))
    }

    async fn accuracy(
        &self,
        accuracy_input: Option<models::AccuracyInput>,
        context: &C) -> Result<AccuracyResponse, ApiError>;

    async fn bucketize(
        &self,
        bucketize_input: Option<models::BucketizeInput>,
        context: &C) -> Result<BucketizeResponse, ApiError>;

    async fn correlation(
        &self,
        correlation_input: Option<models::CorrelationInput>,
        context: &C) -> Result<CorrelationResponse, ApiError>;

    async fn correlation_matrix(
        &self,
        correlation_matrix_input: Option<models::CorrelationMatrixInput>,
        context: &C) -> Result<CorrelationMatrixResponse, ApiError>;

    async fn covariance(
        &self,
        covariance_input: Option<models::CovarianceInput>,
        context: &C) -> Result<CovarianceResponse, ApiError>;

    async fn data_range(
        &self,
        data_range_input: Option<models::DataRangeInput>,
        context: &C) -> Result<DataRangeResponse, ApiError>;

    async fn de_mean(
        &self,
        de_mean_input: Option<models::DeMeanInput>,
        context: &C) -> Result<DeMeanResponse, ApiError>;

    async fn difference_quotient(
        &self,
        difference_quotient_input: Option<models::DifferenceQuotientInput>,
        context: &C) -> Result<DifferenceQuotientResponse, ApiError>;

    async fn distance(
        &self,
        distance_input: Option<models::DistanceInput>,
        context: &C) -> Result<DistanceResponse, ApiError>;

    async fn dot(
        &self,
        dot_input: Option<models::DotInput>,
        context: &C) -> Result<DotResponse, ApiError>;

    async fn echo(
        &self,
        body: Option<models::EchoInput>,
        context: &C) -> Result<EchoResponse, ApiError>;

    async fn estimate_gradient(
        &self,
        estimate_gradient_input: Option<models::EstimateGradientInput>,
        context: &C) -> Result<EstimateGradientResponse, ApiError>;

    async fn f1_score(
        &self,
        f1_score_input: Option<models::F1ScoreInput>,
        context: &C) -> Result<F1ScoreResponse, ApiError>;

    async fn get_column(
        &self,
        get_column_input: Option<models::GetColumnInput>,
        context: &C) -> Result<GetColumnResponse, ApiError>;

    async fn get_row(
        &self,
        get_row_input: Option<models::GetRowInput>,
        context: &C) -> Result<GetRowResponse, ApiError>;

    async fn in_random_order(
        &self,
        in_random_order_input: Option<models::InRandomOrderInput>,
        context: &C) -> Result<InRandomOrderResponse, ApiError>;

    async fn interquartile_range(
        &self,
        interquartile_range_input: Option<models::InterquartileRangeInput>,
        context: &C) -> Result<InterquartileRangeResponse, ApiError>;

    async fn magnitude(
        &self,
        magnitude_input: Option<models::MagnitudeInput>,
        context: &C) -> Result<MagnitudeResponse, ApiError>;

    async fn matrix_add(
        &self,
        matrix_add_input: Option<models::MatrixAddInput>,
        context: &C) -> Result<MatrixAddResponse, ApiError>;

    async fn maximize_batch(
        &self,
        maximize_batch_input: Option<models::MaximizeBatchInput>,
        context: &C) -> Result<MaximizeBatchResponse, ApiError>;

    async fn maximize_stochastic(
        &self,
        maximize_stochastic_input: Option<models::MaximizeStochasticInput>,
        context: &C) -> Result<MaximizeStochasticResponse, ApiError>;

    async fn mean(
        &self,
        mean_input: Option<models::MeanInput>,
        context: &C) -> Result<MeanResponse, ApiError>;

    async fn median(
        &self,
        median_input: Option<models::MedianInput>,
        context: &C) -> Result<MedianResponse, ApiError>;

    async fn minimize_batch(
        &self,
        minimize_batch_input: Option<models::MinimizeBatchInput>,
        context: &C) -> Result<MinimizeBatchResponse, ApiError>;

    async fn minimize_stochastic(
        &self,
        minimize_stochastic_input: Option<models::MinimizeStochasticInput>,
        context: &C) -> Result<MinimizeStochasticResponse, ApiError>;

    async fn mode(
        &self,
        mode_input: Option<models::ModeInput>,
        context: &C) -> Result<ModeResponse, ApiError>;

    async fn partial_difference_quotient(
        &self,
        partial_difference_quotient_input: Option<models::PartialDifferenceQuotientInput>,
        context: &C) -> Result<PartialDifferenceQuotientResponse, ApiError>;

    async fn precision(
        &self,
        precision_input: Option<models::PrecisionInput>,
        context: &C) -> Result<PrecisionResponse, ApiError>;

    async fn quantile(
        &self,
        quantile_input: Option<models::QuantileInput>,
        context: &C) -> Result<QuantileResponse, ApiError>;

    async fn recall(
        &self,
        recall_input: Option<models::RecallInput>,
        context: &C) -> Result<RecallResponse, ApiError>;

    async fn scalar_multiply(
        &self,
        scalar_multiply_input: Option<models::ScalarMultiplyInput>,
        context: &C) -> Result<ScalarMultiplyResponse, ApiError>;

    async fn shape(
        &self,
        shape_input: Option<models::ShapeInput>,
        context: &C) -> Result<ShapeResponse, ApiError>;

    async fn split_data(
        &self,
        split_data_input: Option<models::SplitDataInput>,
        context: &C) -> Result<SplitDataResponse, ApiError>;

    async fn sqrt(
        &self,
        sqrt_input: Option<models::SqrtInput>,
        context: &C) -> Result<SqrtResponse, ApiError>;

    async fn squared_distance(
        &self,
        squared_distance_input: Option<models::SquaredDistanceInput>,
        context: &C) -> Result<SquaredDistanceResponse, ApiError>;

    async fn standard_deviation(
        &self,
        standard_deviation_input: Option<models::StandardDeviationInput>,
        context: &C) -> Result<StandardDeviationResponse, ApiError>;

    async fn strength(
        &self,
        strength_input: Option<models::StrengthInput>,
        context: &C) -> Result<StrengthResponse, ApiError>;

    async fn sum_of_squares(
        &self,
        sum_of_squares_input: Option<models::SumOfSquaresInput>,
        context: &C) -> Result<SumOfSquaresResponse, ApiError>;

    async fn train_test_split(
        &self,
        train_test_split_input: Option<models::TrainTestSplitInput>,
        context: &C) -> Result<TrainTestSplitResponse, ApiError>;

    async fn variance(
        &self,
        variance_input: Option<models::VarianceInput>,
        context: &C) -> Result<VarianceResponse, ApiError>;

    async fn vector_add(
        &self,
        vector_add_input: Option<models::VectorAddInput>,
        context: &C) -> Result<VectorAddResponse, ApiError>;

    async fn vector_mean(
        &self,
        vector_mean_input: Option<models::VectorMeanInput>,
        context: &C) -> Result<VectorMeanResponse, ApiError>;

    async fn vector_subtract(
        &self,
        vector_subtract_input: Option<models::VectorSubtractInput>,
        context: &C) -> Result<VectorSubtractResponse, ApiError>;

    async fn vector_sum(
        &self,
        vector_sum_input: Option<models::VectorSumInput>,
        context: &C) -> Result<VectorSumResponse, ApiError>;

    /// Add a new pet to the store
    async fn add_pet(
        &self,
        body: models::Pet,
        context: &C) -> Result<AddPetResponse, ApiError>;

    /// Deletes a pet
    async fn delete_pet(
        &self,
        pet_id: i64,
        api_key: Option<String>,
        context: &C) -> Result<DeletePetResponse, ApiError>;

    /// Finds Pets by status
    async fn find_pets_by_status(
        &self,
        status: &Vec<String>,
        context: &C) -> Result<FindPetsByStatusResponse, ApiError>;

    /// Finds Pets by tags
    async fn find_pets_by_tags(
        &self,
        tags: &Vec<String>,
        context: &C) -> Result<FindPetsByTagsResponse, ApiError>;

    /// Find pet by ID
    async fn get_pet_by_id(
        &self,
        pet_id: i64,
        context: &C) -> Result<GetPetByIdResponse, ApiError>;

    /// Update an existing pet
    async fn update_pet(
        &self,
        body: models::Pet,
        context: &C) -> Result<UpdatePetResponse, ApiError>;

    /// Updates a pet in the store with form data
    async fn update_pet_with_form(
        &self,
        pet_id: i64,
        name: Option<String>,
        status: Option<String>,
        context: &C) -> Result<UpdatePetWithFormResponse, ApiError>;

    /// uploads an image
    async fn upload_file(
        &self,
        pet_id: i64,
        additional_metadata: Option<String>,
        file: Option<swagger::ByteArray>,
        context: &C) -> Result<UploadFileResponse, ApiError>;

    /// Delete purchase order by ID
    async fn delete_order(
        &self,
        order_id: i64,
        context: &C) -> Result<DeleteOrderResponse, ApiError>;

    /// Returns pet inventories by status
    async fn get_inventory(
        &self,
        context: &C) -> Result<GetInventoryResponse, ApiError>;

    /// Find purchase order by ID
    async fn get_order_by_id(
        &self,
        order_id: i64,
        context: &C) -> Result<GetOrderByIdResponse, ApiError>;

    /// Place an order for a pet
    async fn place_order(
        &self,
        body: models::Order,
        context: &C) -> Result<PlaceOrderResponse, ApiError>;

    /// Create user
    async fn create_user(
        &self,
        body: models::User,
        context: &C) -> Result<CreateUserResponse, ApiError>;

    /// Creates list of users with given input array
    async fn create_users_with_array_input(
        &self,
        body: &Vec<models::User>,
        context: &C) -> Result<CreateUsersWithArrayInputResponse, ApiError>;

    /// Creates list of users with given input array
    async fn create_users_with_list_input(
        &self,
        body: &Vec<models::User>,
        context: &C) -> Result<CreateUsersWithListInputResponse, ApiError>;

    /// Delete user
    async fn delete_user(
        &self,
        username: String,
        context: &C) -> Result<DeleteUserResponse, ApiError>;

    /// Get user by user name
    async fn get_user_by_name(
        &self,
        username: String,
        context: &C) -> Result<GetUserByNameResponse, ApiError>;

    /// Logs user into the system
    async fn login_user(
        &self,
        username: String,
        password: String,
        context: &C) -> Result<LoginUserResponse, ApiError>;

    /// Logs out current logged in user session
    async fn logout_user(
        &self,
        context: &C) -> Result<LogoutUserResponse, ApiError>;

    /// Updated user
    async fn update_user(
        &self,
        username: String,
        body: models::User,
        context: &C) -> Result<UpdateUserResponse, ApiError>;

}

/// API where `Context` isn't passed on every API call
#[async_trait]
#[allow(clippy::too_many_arguments, clippy::ptr_arg)]
pub trait ApiNoContext<C: Send + Sync> {

    fn poll_ready(&self, _cx: &mut Context) -> Poll<Result<(), Box<dyn Error + Send + Sync + 'static>>>;

    fn context(&self) -> &C;

    async fn accuracy(
        &self,
        accuracy_input: Option<models::AccuracyInput>,
        ) -> Result<AccuracyResponse, ApiError>;

    async fn bucketize(
        &self,
        bucketize_input: Option<models::BucketizeInput>,
        ) -> Result<BucketizeResponse, ApiError>;

    async fn correlation(
        &self,
        correlation_input: Option<models::CorrelationInput>,
        ) -> Result<CorrelationResponse, ApiError>;

    async fn correlation_matrix(
        &self,
        correlation_matrix_input: Option<models::CorrelationMatrixInput>,
        ) -> Result<CorrelationMatrixResponse, ApiError>;

    async fn covariance(
        &self,
        covariance_input: Option<models::CovarianceInput>,
        ) -> Result<CovarianceResponse, ApiError>;

    async fn data_range(
        &self,
        data_range_input: Option<models::DataRangeInput>,
        ) -> Result<DataRangeResponse, ApiError>;

    async fn de_mean(
        &self,
        de_mean_input: Option<models::DeMeanInput>,
        ) -> Result<DeMeanResponse, ApiError>;

    async fn difference_quotient(
        &self,
        difference_quotient_input: Option<models::DifferenceQuotientInput>,
        ) -> Result<DifferenceQuotientResponse, ApiError>;

    async fn distance(
        &self,
        distance_input: Option<models::DistanceInput>,
        ) -> Result<DistanceResponse, ApiError>;

    async fn dot(
        &self,
        dot_input: Option<models::DotInput>,
        ) -> Result<DotResponse, ApiError>;

    async fn echo(
        &self,
        body: Option<models::EchoInput>,
        ) -> Result<EchoResponse, ApiError>;

    async fn estimate_gradient(
        &self,
        estimate_gradient_input: Option<models::EstimateGradientInput>,
        ) -> Result<EstimateGradientResponse, ApiError>;

    async fn f1_score(
        &self,
        f1_score_input: Option<models::F1ScoreInput>,
        ) -> Result<F1ScoreResponse, ApiError>;

    async fn get_column(
        &self,
        get_column_input: Option<models::GetColumnInput>,
        ) -> Result<GetColumnResponse, ApiError>;

    async fn get_row(
        &self,
        get_row_input: Option<models::GetRowInput>,
        ) -> Result<GetRowResponse, ApiError>;

    async fn in_random_order(
        &self,
        in_random_order_input: Option<models::InRandomOrderInput>,
        ) -> Result<InRandomOrderResponse, ApiError>;

    async fn interquartile_range(
        &self,
        interquartile_range_input: Option<models::InterquartileRangeInput>,
        ) -> Result<InterquartileRangeResponse, ApiError>;

    async fn magnitude(
        &self,
        magnitude_input: Option<models::MagnitudeInput>,
        ) -> Result<MagnitudeResponse, ApiError>;

    async fn matrix_add(
        &self,
        matrix_add_input: Option<models::MatrixAddInput>,
        ) -> Result<MatrixAddResponse, ApiError>;

    async fn maximize_batch(
        &self,
        maximize_batch_input: Option<models::MaximizeBatchInput>,
        ) -> Result<MaximizeBatchResponse, ApiError>;

    async fn maximize_stochastic(
        &self,
        maximize_stochastic_input: Option<models::MaximizeStochasticInput>,
        ) -> Result<MaximizeStochasticResponse, ApiError>;

    async fn mean(
        &self,
        mean_input: Option<models::MeanInput>,
        ) -> Result<MeanResponse, ApiError>;

    async fn median(
        &self,
        median_input: Option<models::MedianInput>,
        ) -> Result<MedianResponse, ApiError>;

    async fn minimize_batch(
        &self,
        minimize_batch_input: Option<models::MinimizeBatchInput>,
        ) -> Result<MinimizeBatchResponse, ApiError>;

    async fn minimize_stochastic(
        &self,
        minimize_stochastic_input: Option<models::MinimizeStochasticInput>,
        ) -> Result<MinimizeStochasticResponse, ApiError>;

    async fn mode(
        &self,
        mode_input: Option<models::ModeInput>,
        ) -> Result<ModeResponse, ApiError>;

    async fn partial_difference_quotient(
        &self,
        partial_difference_quotient_input: Option<models::PartialDifferenceQuotientInput>,
        ) -> Result<PartialDifferenceQuotientResponse, ApiError>;

    async fn precision(
        &self,
        precision_input: Option<models::PrecisionInput>,
        ) -> Result<PrecisionResponse, ApiError>;

    async fn quantile(
        &self,
        quantile_input: Option<models::QuantileInput>,
        ) -> Result<QuantileResponse, ApiError>;

    async fn recall(
        &self,
        recall_input: Option<models::RecallInput>,
        ) -> Result<RecallResponse, ApiError>;

    async fn scalar_multiply(
        &self,
        scalar_multiply_input: Option<models::ScalarMultiplyInput>,
        ) -> Result<ScalarMultiplyResponse, ApiError>;

    async fn shape(
        &self,
        shape_input: Option<models::ShapeInput>,
        ) -> Result<ShapeResponse, ApiError>;

    async fn split_data(
        &self,
        split_data_input: Option<models::SplitDataInput>,
        ) -> Result<SplitDataResponse, ApiError>;

    async fn sqrt(
        &self,
        sqrt_input: Option<models::SqrtInput>,
        ) -> Result<SqrtResponse, ApiError>;

    async fn squared_distance(
        &self,
        squared_distance_input: Option<models::SquaredDistanceInput>,
        ) -> Result<SquaredDistanceResponse, ApiError>;

    async fn standard_deviation(
        &self,
        standard_deviation_input: Option<models::StandardDeviationInput>,
        ) -> Result<StandardDeviationResponse, ApiError>;

    async fn strength(
        &self,
        strength_input: Option<models::StrengthInput>,
        ) -> Result<StrengthResponse, ApiError>;

    async fn sum_of_squares(
        &self,
        sum_of_squares_input: Option<models::SumOfSquaresInput>,
        ) -> Result<SumOfSquaresResponse, ApiError>;

    async fn train_test_split(
        &self,
        train_test_split_input: Option<models::TrainTestSplitInput>,
        ) -> Result<TrainTestSplitResponse, ApiError>;

    async fn variance(
        &self,
        variance_input: Option<models::VarianceInput>,
        ) -> Result<VarianceResponse, ApiError>;

    async fn vector_add(
        &self,
        vector_add_input: Option<models::VectorAddInput>,
        ) -> Result<VectorAddResponse, ApiError>;

    async fn vector_mean(
        &self,
        vector_mean_input: Option<models::VectorMeanInput>,
        ) -> Result<VectorMeanResponse, ApiError>;

    async fn vector_subtract(
        &self,
        vector_subtract_input: Option<models::VectorSubtractInput>,
        ) -> Result<VectorSubtractResponse, ApiError>;

    async fn vector_sum(
        &self,
        vector_sum_input: Option<models::VectorSumInput>,
        ) -> Result<VectorSumResponse, ApiError>;

    /// Add a new pet to the store
    async fn add_pet(
        &self,
        body: models::Pet,
        ) -> Result<AddPetResponse, ApiError>;

    /// Deletes a pet
    async fn delete_pet(
        &self,
        pet_id: i64,
        api_key: Option<String>,
        ) -> Result<DeletePetResponse, ApiError>;

    /// Finds Pets by status
    async fn find_pets_by_status(
        &self,
        status: &Vec<String>,
        ) -> Result<FindPetsByStatusResponse, ApiError>;

    /// Finds Pets by tags
    async fn find_pets_by_tags(
        &self,
        tags: &Vec<String>,
        ) -> Result<FindPetsByTagsResponse, ApiError>;

    /// Find pet by ID
    async fn get_pet_by_id(
        &self,
        pet_id: i64,
        ) -> Result<GetPetByIdResponse, ApiError>;

    /// Update an existing pet
    async fn update_pet(
        &self,
        body: models::Pet,
        ) -> Result<UpdatePetResponse, ApiError>;

    /// Updates a pet in the store with form data
    async fn update_pet_with_form(
        &self,
        pet_id: i64,
        name: Option<String>,
        status: Option<String>,
        ) -> Result<UpdatePetWithFormResponse, ApiError>;

    /// uploads an image
    async fn upload_file(
        &self,
        pet_id: i64,
        additional_metadata: Option<String>,
        file: Option<swagger::ByteArray>,
        ) -> Result<UploadFileResponse, ApiError>;

    /// Delete purchase order by ID
    async fn delete_order(
        &self,
        order_id: i64,
        ) -> Result<DeleteOrderResponse, ApiError>;

    /// Returns pet inventories by status
    async fn get_inventory(
        &self,
        ) -> Result<GetInventoryResponse, ApiError>;

    /// Find purchase order by ID
    async fn get_order_by_id(
        &self,
        order_id: i64,
        ) -> Result<GetOrderByIdResponse, ApiError>;

    /// Place an order for a pet
    async fn place_order(
        &self,
        body: models::Order,
        ) -> Result<PlaceOrderResponse, ApiError>;

    /// Create user
    async fn create_user(
        &self,
        body: models::User,
        ) -> Result<CreateUserResponse, ApiError>;

    /// Creates list of users with given input array
    async fn create_users_with_array_input(
        &self,
        body: &Vec<models::User>,
        ) -> Result<CreateUsersWithArrayInputResponse, ApiError>;

    /// Creates list of users with given input array
    async fn create_users_with_list_input(
        &self,
        body: &Vec<models::User>,
        ) -> Result<CreateUsersWithListInputResponse, ApiError>;

    /// Delete user
    async fn delete_user(
        &self,
        username: String,
        ) -> Result<DeleteUserResponse, ApiError>;

    /// Get user by user name
    async fn get_user_by_name(
        &self,
        username: String,
        ) -> Result<GetUserByNameResponse, ApiError>;

    /// Logs user into the system
    async fn login_user(
        &self,
        username: String,
        password: String,
        ) -> Result<LoginUserResponse, ApiError>;

    /// Logs out current logged in user session
    async fn logout_user(
        &self,
        ) -> Result<LogoutUserResponse, ApiError>;

    /// Updated user
    async fn update_user(
        &self,
        username: String,
        body: models::User,
        ) -> Result<UpdateUserResponse, ApiError>;

}

/// Trait to extend an API to make it easy to bind it to a context.
pub trait ContextWrapperExt<C: Send + Sync> where Self: Sized
{
    /// Binds this API to a context.
    fn with_context(self, context: C) -> ContextWrapper<Self, C>;
}

impl<T: Api<C> + Send + Sync, C: Clone + Send + Sync> ContextWrapperExt<C> for T {
    fn with_context(self: T, context: C) -> ContextWrapper<T, C> {
         ContextWrapper::<T, C>::new(self, context)
    }
}

#[async_trait]
impl<T: Api<C> + Send + Sync, C: Clone + Send + Sync> ApiNoContext<C> for ContextWrapper<T, C> {
    fn poll_ready(&self, cx: &mut Context) -> Poll<Result<(), ServiceError>> {
        self.api().poll_ready(cx)
    }

    fn context(&self) -> &C {
        ContextWrapper::context(self)
    }

    async fn accuracy(
        &self,
        accuracy_input: Option<models::AccuracyInput>,
        ) -> Result<AccuracyResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().accuracy(accuracy_input, &context).await
    }

    async fn bucketize(
        &self,
        bucketize_input: Option<models::BucketizeInput>,
        ) -> Result<BucketizeResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().bucketize(bucketize_input, &context).await
    }

    async fn correlation(
        &self,
        correlation_input: Option<models::CorrelationInput>,
        ) -> Result<CorrelationResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().correlation(correlation_input, &context).await
    }

    async fn correlation_matrix(
        &self,
        correlation_matrix_input: Option<models::CorrelationMatrixInput>,
        ) -> Result<CorrelationMatrixResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().correlation_matrix(correlation_matrix_input, &context).await
    }

    async fn covariance(
        &self,
        covariance_input: Option<models::CovarianceInput>,
        ) -> Result<CovarianceResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().covariance(covariance_input, &context).await
    }

    async fn data_range(
        &self,
        data_range_input: Option<models::DataRangeInput>,
        ) -> Result<DataRangeResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().data_range(data_range_input, &context).await
    }

    async fn de_mean(
        &self,
        de_mean_input: Option<models::DeMeanInput>,
        ) -> Result<DeMeanResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().de_mean(de_mean_input, &context).await
    }

    async fn difference_quotient(
        &self,
        difference_quotient_input: Option<models::DifferenceQuotientInput>,
        ) -> Result<DifferenceQuotientResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().difference_quotient(difference_quotient_input, &context).await
    }

    async fn distance(
        &self,
        distance_input: Option<models::DistanceInput>,
        ) -> Result<DistanceResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().distance(distance_input, &context).await
    }

    async fn dot(
        &self,
        dot_input: Option<models::DotInput>,
        ) -> Result<DotResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().dot(dot_input, &context).await
    }

    async fn echo(
        &self,
        body: Option<models::EchoInput>,
        ) -> Result<EchoResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().echo(body, &context).await
    }

    async fn estimate_gradient(
        &self,
        estimate_gradient_input: Option<models::EstimateGradientInput>,
        ) -> Result<EstimateGradientResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().estimate_gradient(estimate_gradient_input, &context).await
    }

    async fn f1_score(
        &self,
        f1_score_input: Option<models::F1ScoreInput>,
        ) -> Result<F1ScoreResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().f1_score(f1_score_input, &context).await
    }

    async fn get_column(
        &self,
        get_column_input: Option<models::GetColumnInput>,
        ) -> Result<GetColumnResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().get_column(get_column_input, &context).await
    }

    async fn get_row(
        &self,
        get_row_input: Option<models::GetRowInput>,
        ) -> Result<GetRowResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().get_row(get_row_input, &context).await
    }

    async fn in_random_order(
        &self,
        in_random_order_input: Option<models::InRandomOrderInput>,
        ) -> Result<InRandomOrderResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().in_random_order(in_random_order_input, &context).await
    }

    async fn interquartile_range(
        &self,
        interquartile_range_input: Option<models::InterquartileRangeInput>,
        ) -> Result<InterquartileRangeResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().interquartile_range(interquartile_range_input, &context).await
    }

    async fn magnitude(
        &self,
        magnitude_input: Option<models::MagnitudeInput>,
        ) -> Result<MagnitudeResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().magnitude(magnitude_input, &context).await
    }

    async fn matrix_add(
        &self,
        matrix_add_input: Option<models::MatrixAddInput>,
        ) -> Result<MatrixAddResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().matrix_add(matrix_add_input, &context).await
    }

    async fn maximize_batch(
        &self,
        maximize_batch_input: Option<models::MaximizeBatchInput>,
        ) -> Result<MaximizeBatchResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().maximize_batch(maximize_batch_input, &context).await
    }

    async fn maximize_stochastic(
        &self,
        maximize_stochastic_input: Option<models::MaximizeStochasticInput>,
        ) -> Result<MaximizeStochasticResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().maximize_stochastic(maximize_stochastic_input, &context).await
    }

    async fn mean(
        &self,
        mean_input: Option<models::MeanInput>,
        ) -> Result<MeanResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().mean(mean_input, &context).await
    }

    async fn median(
        &self,
        median_input: Option<models::MedianInput>,
        ) -> Result<MedianResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().median(median_input, &context).await
    }

    async fn minimize_batch(
        &self,
        minimize_batch_input: Option<models::MinimizeBatchInput>,
        ) -> Result<MinimizeBatchResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().minimize_batch(minimize_batch_input, &context).await
    }

    async fn minimize_stochastic(
        &self,
        minimize_stochastic_input: Option<models::MinimizeStochasticInput>,
        ) -> Result<MinimizeStochasticResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().minimize_stochastic(minimize_stochastic_input, &context).await
    }

    async fn mode(
        &self,
        mode_input: Option<models::ModeInput>,
        ) -> Result<ModeResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().mode(mode_input, &context).await
    }

    async fn partial_difference_quotient(
        &self,
        partial_difference_quotient_input: Option<models::PartialDifferenceQuotientInput>,
        ) -> Result<PartialDifferenceQuotientResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().partial_difference_quotient(partial_difference_quotient_input, &context).await
    }

    async fn precision(
        &self,
        precision_input: Option<models::PrecisionInput>,
        ) -> Result<PrecisionResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().precision(precision_input, &context).await
    }

    async fn quantile(
        &self,
        quantile_input: Option<models::QuantileInput>,
        ) -> Result<QuantileResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().quantile(quantile_input, &context).await
    }

    async fn recall(
        &self,
        recall_input: Option<models::RecallInput>,
        ) -> Result<RecallResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().recall(recall_input, &context).await
    }

    async fn scalar_multiply(
        &self,
        scalar_multiply_input: Option<models::ScalarMultiplyInput>,
        ) -> Result<ScalarMultiplyResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().scalar_multiply(scalar_multiply_input, &context).await
    }

    async fn shape(
        &self,
        shape_input: Option<models::ShapeInput>,
        ) -> Result<ShapeResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().shape(shape_input, &context).await
    }

    async fn split_data(
        &self,
        split_data_input: Option<models::SplitDataInput>,
        ) -> Result<SplitDataResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().split_data(split_data_input, &context).await
    }

    async fn sqrt(
        &self,
        sqrt_input: Option<models::SqrtInput>,
        ) -> Result<SqrtResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().sqrt(sqrt_input, &context).await
    }

    async fn squared_distance(
        &self,
        squared_distance_input: Option<models::SquaredDistanceInput>,
        ) -> Result<SquaredDistanceResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().squared_distance(squared_distance_input, &context).await
    }

    async fn standard_deviation(
        &self,
        standard_deviation_input: Option<models::StandardDeviationInput>,
        ) -> Result<StandardDeviationResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().standard_deviation(standard_deviation_input, &context).await
    }

    async fn strength(
        &self,
        strength_input: Option<models::StrengthInput>,
        ) -> Result<StrengthResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().strength(strength_input, &context).await
    }

    async fn sum_of_squares(
        &self,
        sum_of_squares_input: Option<models::SumOfSquaresInput>,
        ) -> Result<SumOfSquaresResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().sum_of_squares(sum_of_squares_input, &context).await
    }

    async fn train_test_split(
        &self,
        train_test_split_input: Option<models::TrainTestSplitInput>,
        ) -> Result<TrainTestSplitResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().train_test_split(train_test_split_input, &context).await
    }

    async fn variance(
        &self,
        variance_input: Option<models::VarianceInput>,
        ) -> Result<VarianceResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().variance(variance_input, &context).await
    }

    async fn vector_add(
        &self,
        vector_add_input: Option<models::VectorAddInput>,
        ) -> Result<VectorAddResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().vector_add(vector_add_input, &context).await
    }

    async fn vector_mean(
        &self,
        vector_mean_input: Option<models::VectorMeanInput>,
        ) -> Result<VectorMeanResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().vector_mean(vector_mean_input, &context).await
    }

    async fn vector_subtract(
        &self,
        vector_subtract_input: Option<models::VectorSubtractInput>,
        ) -> Result<VectorSubtractResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().vector_subtract(vector_subtract_input, &context).await
    }

    async fn vector_sum(
        &self,
        vector_sum_input: Option<models::VectorSumInput>,
        ) -> Result<VectorSumResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().vector_sum(vector_sum_input, &context).await
    }

    /// Add a new pet to the store
    async fn add_pet(
        &self,
        body: models::Pet,
        ) -> Result<AddPetResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().add_pet(body, &context).await
    }

    /// Deletes a pet
    async fn delete_pet(
        &self,
        pet_id: i64,
        api_key: Option<String>,
        ) -> Result<DeletePetResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().delete_pet(pet_id, api_key, &context).await
    }

    /// Finds Pets by status
    async fn find_pets_by_status(
        &self,
        status: &Vec<String>,
        ) -> Result<FindPetsByStatusResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().find_pets_by_status(status, &context).await
    }

    /// Finds Pets by tags
    async fn find_pets_by_tags(
        &self,
        tags: &Vec<String>,
        ) -> Result<FindPetsByTagsResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().find_pets_by_tags(tags, &context).await
    }

    /// Find pet by ID
    async fn get_pet_by_id(
        &self,
        pet_id: i64,
        ) -> Result<GetPetByIdResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().get_pet_by_id(pet_id, &context).await
    }

    /// Update an existing pet
    async fn update_pet(
        &self,
        body: models::Pet,
        ) -> Result<UpdatePetResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().update_pet(body, &context).await
    }

    /// Updates a pet in the store with form data
    async fn update_pet_with_form(
        &self,
        pet_id: i64,
        name: Option<String>,
        status: Option<String>,
        ) -> Result<UpdatePetWithFormResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().update_pet_with_form(pet_id, name, status, &context).await
    }

    /// uploads an image
    async fn upload_file(
        &self,
        pet_id: i64,
        additional_metadata: Option<String>,
        file: Option<swagger::ByteArray>,
        ) -> Result<UploadFileResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().upload_file(pet_id, additional_metadata, file, &context).await
    }

    /// Delete purchase order by ID
    async fn delete_order(
        &self,
        order_id: i64,
        ) -> Result<DeleteOrderResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().delete_order(order_id, &context).await
    }

    /// Returns pet inventories by status
    async fn get_inventory(
        &self,
        ) -> Result<GetInventoryResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().get_inventory(&context).await
    }

    /// Find purchase order by ID
    async fn get_order_by_id(
        &self,
        order_id: i64,
        ) -> Result<GetOrderByIdResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().get_order_by_id(order_id, &context).await
    }

    /// Place an order for a pet
    async fn place_order(
        &self,
        body: models::Order,
        ) -> Result<PlaceOrderResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().place_order(body, &context).await
    }

    /// Create user
    async fn create_user(
        &self,
        body: models::User,
        ) -> Result<CreateUserResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().create_user(body, &context).await
    }

    /// Creates list of users with given input array
    async fn create_users_with_array_input(
        &self,
        body: &Vec<models::User>,
        ) -> Result<CreateUsersWithArrayInputResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().create_users_with_array_input(body, &context).await
    }

    /// Creates list of users with given input array
    async fn create_users_with_list_input(
        &self,
        body: &Vec<models::User>,
        ) -> Result<CreateUsersWithListInputResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().create_users_with_list_input(body, &context).await
    }

    /// Delete user
    async fn delete_user(
        &self,
        username: String,
        ) -> Result<DeleteUserResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().delete_user(username, &context).await
    }

    /// Get user by user name
    async fn get_user_by_name(
        &self,
        username: String,
        ) -> Result<GetUserByNameResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().get_user_by_name(username, &context).await
    }

    /// Logs user into the system
    async fn login_user(
        &self,
        username: String,
        password: String,
        ) -> Result<LoginUserResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().login_user(username, password, &context).await
    }

    /// Logs out current logged in user session
    async fn logout_user(
        &self,
        ) -> Result<LogoutUserResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().logout_user(&context).await
    }

    /// Updated user
    async fn update_user(
        &self,
        username: String,
        body: models::User,
        ) -> Result<UpdateUserResponse, ApiError>
    {
        let context = self.context().clone();
        self.api().update_user(username, body, &context).await
    }

}


#[cfg(feature = "client")]
pub mod client;

// Re-export Client as a top-level name
#[cfg(feature = "client")]
pub use client::Client;

#[cfg(feature = "server")]
pub mod server;

// Re-export router() as a top-level name
#[cfg(feature = "server")]
pub use self::server::Service;

#[cfg(feature = "server")]
pub mod context;

pub mod models;

#[cfg(any(feature = "client", feature = "server"))]
pub(crate) mod header;
