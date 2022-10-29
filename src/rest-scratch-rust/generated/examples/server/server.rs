//! Main library entry point for openapi_client implementation.

#![allow(unused_imports)]

use async_trait::async_trait;
use futures::{future, Stream, StreamExt, TryFutureExt, TryStreamExt};
use hyper::server::conn::Http;
use hyper::service::Service;
use log::info;
use std::future::Future;
use std::marker::PhantomData;
use std::net::SocketAddr;
use std::sync::{Arc, Mutex};
use std::task::{Context, Poll};
use swagger::{Has, XSpanIdString};
use swagger::auth::MakeAllowAllAuthenticator;
use swagger::EmptyContext;
use tokio::net::TcpListener;

#[cfg(not(any(target_os = "macos", target_os = "windows", target_os = "ios")))]
use openssl::ssl::{Ssl, SslAcceptor, SslAcceptorBuilder, SslFiletype, SslMethod};

use openapi_client::models;

/// Builds an SSL implementation for Simple HTTPS from some hard-coded file names
pub async fn create(addr: &str, https: bool) {
    let addr = addr.parse().expect("Failed to parse bind address");

    let server = Server::new();

    let service = MakeService::new(server);

    let service = MakeAllowAllAuthenticator::new(service, "cosmo");

    #[allow(unused_mut)]
    let mut service =
        openapi_client::server::context::MakeAddContext::<_, EmptyContext>::new(
            service
        );

    if https {
        #[cfg(any(target_os = "macos", target_os = "windows", target_os = "ios"))]
        {
            unimplemented!("SSL is not implemented for the examples on MacOS, Windows or iOS");
        }

        #[cfg(not(any(target_os = "macos", target_os = "windows", target_os = "ios")))]
        {
            let mut ssl = SslAcceptor::mozilla_intermediate_v5(SslMethod::tls()).expect("Failed to create SSL Acceptor");

            // Server authentication
            ssl.set_private_key_file("examples/server-key.pem", SslFiletype::PEM).expect("Failed to set private key");
            ssl.set_certificate_chain_file("examples/server-chain.pem").expect("Failed to set certificate chain");
            ssl.check_private_key().expect("Failed to check private key");

            let tls_acceptor = ssl.build();
            let tcp_listener = TcpListener::bind(&addr).await.unwrap();

            loop {
                if let Ok((tcp, _)) = tcp_listener.accept().await {
                    let ssl = Ssl::new(tls_acceptor.context()).unwrap();
                    let addr = tcp.peer_addr().expect("Unable to get remote address");
                    let service = service.call(addr);

                    tokio::spawn(async move {
                        let tls = tokio_openssl::SslStream::new(ssl, tcp).map_err(|_| ())?;
                        let service = service.await.map_err(|_| ())?;

                        Http::new()
                            .serve_connection(tls, service)
                            .await
                            .map_err(|_| ())
                    });
                }
            }
        }
    } else {
        // Using HTTP
        hyper::server::Server::bind(&addr).serve(service).await.unwrap()
    }
}

#[derive(Copy, Clone)]
pub struct Server<C> {
    marker: PhantomData<C>,
}

impl<C> Server<C> {
    pub fn new() -> Self {
        Server{marker: PhantomData}
    }
}


use openapi_client::{
    Api,
    AccuracyResponse,
    BucketizeResponse,
    CorrelationResponse,
    CorrelationMatrixResponse,
    CovarianceResponse,
    DataRangeResponse,
    DeMeanResponse,
    DifferenceQuotientResponse,
    DistanceResponse,
    DotResponse,
    EchoResponse,
    EstimateGradientResponse,
    F1ScoreResponse,
    GetColumnResponse,
    GetRowResponse,
    InRandomOrderResponse,
    InterquartileRangeResponse,
    MagnitudeResponse,
    MatrixAddResponse,
    MaximizeBatchResponse,
    MaximizeStochasticResponse,
    MeanResponse,
    MedianResponse,
    MinimizeBatchResponse,
    MinimizeStochasticResponse,
    ModeResponse,
    PartialDifferenceQuotientResponse,
    PrecisionResponse,
    QuantileResponse,
    RecallResponse,
    ScalarMultiplyResponse,
    ShapeResponse,
    SplitDataResponse,
    SqrtResponse,
    SquaredDistanceResponse,
    StandardDeviationResponse,
    StrengthResponse,
    SumOfSquaresResponse,
    TrainTestSplitResponse,
    VarianceResponse,
    VectorAddResponse,
    VectorMeanResponse,
    VectorSubtractResponse,
    VectorSumResponse,
    AddPetResponse,
    DeletePetResponse,
    FindPetsByStatusResponse,
    FindPetsByTagsResponse,
    GetPetByIdResponse,
    UpdatePetResponse,
    UpdatePetWithFormResponse,
    UploadFileResponse,
    DeleteOrderResponse,
    GetInventoryResponse,
    GetOrderByIdResponse,
    PlaceOrderResponse,
    CreateUserResponse,
    CreateUsersWithArrayInputResponse,
    CreateUsersWithListInputResponse,
    DeleteUserResponse,
    GetUserByNameResponse,
    LoginUserResponse,
    LogoutUserResponse,
    UpdateUserResponse,
};
use openapi_client::server::MakeService;
use std::error::Error;
use swagger::ApiError;

#[async_trait]
impl<C> Api<C> for Server<C> where C: Has<XSpanIdString> + Send + Sync
{
    async fn accuracy(
        &self,
        accuracy_input: Option<models::AccuracyInput>,
        context: &C) -> Result<AccuracyResponse, ApiError>
    {
        let context = context.clone();
        info!("accuracy({:?}) - X-Span-ID: {:?}", accuracy_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn bucketize(
        &self,
        bucketize_input: Option<models::BucketizeInput>,
        context: &C) -> Result<BucketizeResponse, ApiError>
    {
        let context = context.clone();
        info!("bucketize({:?}) - X-Span-ID: {:?}", bucketize_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn correlation(
        &self,
        correlation_input: Option<models::CorrelationInput>,
        context: &C) -> Result<CorrelationResponse, ApiError>
    {
        let context = context.clone();
        info!("correlation({:?}) - X-Span-ID: {:?}", correlation_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn correlation_matrix(
        &self,
        correlation_matrix_input: Option<models::CorrelationMatrixInput>,
        context: &C) -> Result<CorrelationMatrixResponse, ApiError>
    {
        let context = context.clone();
        info!("correlation_matrix({:?}) - X-Span-ID: {:?}", correlation_matrix_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn covariance(
        &self,
        covariance_input: Option<models::CovarianceInput>,
        context: &C) -> Result<CovarianceResponse, ApiError>
    {
        let context = context.clone();
        info!("covariance({:?}) - X-Span-ID: {:?}", covariance_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn data_range(
        &self,
        data_range_input: Option<models::DataRangeInput>,
        context: &C) -> Result<DataRangeResponse, ApiError>
    {
        let context = context.clone();
        info!("data_range({:?}) - X-Span-ID: {:?}", data_range_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn de_mean(
        &self,
        de_mean_input: Option<models::DeMeanInput>,
        context: &C) -> Result<DeMeanResponse, ApiError>
    {
        let context = context.clone();
        info!("de_mean({:?}) - X-Span-ID: {:?}", de_mean_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn difference_quotient(
        &self,
        difference_quotient_input: Option<models::DifferenceQuotientInput>,
        context: &C) -> Result<DifferenceQuotientResponse, ApiError>
    {
        let context = context.clone();
        info!("difference_quotient({:?}) - X-Span-ID: {:?}", difference_quotient_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn distance(
        &self,
        distance_input: Option<models::DistanceInput>,
        context: &C) -> Result<DistanceResponse, ApiError>
    {
        let context = context.clone();
        info!("distance({:?}) - X-Span-ID: {:?}", distance_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn dot(
        &self,
        dot_input: Option<models::DotInput>,
        context: &C) -> Result<DotResponse, ApiError>
    {
        let context = context.clone();
        info!("dot({:?}) - X-Span-ID: {:?}", dot_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn echo(
        &self,
        body: Option<models::EchoInput>,
        context: &C) -> Result<EchoResponse, ApiError>
    {
        let context = context.clone();
        info!("echo({:?}) - X-Span-ID: {:?}", body, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn estimate_gradient(
        &self,
        estimate_gradient_input: Option<models::EstimateGradientInput>,
        context: &C) -> Result<EstimateGradientResponse, ApiError>
    {
        let context = context.clone();
        info!("estimate_gradient({:?}) - X-Span-ID: {:?}", estimate_gradient_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn f1_score(
        &self,
        f1_score_input: Option<models::F1ScoreInput>,
        context: &C) -> Result<F1ScoreResponse, ApiError>
    {
        let context = context.clone();
        info!("f1_score({:?}) - X-Span-ID: {:?}", f1_score_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn get_column(
        &self,
        get_column_input: Option<models::GetColumnInput>,
        context: &C) -> Result<GetColumnResponse, ApiError>
    {
        let context = context.clone();
        info!("get_column({:?}) - X-Span-ID: {:?}", get_column_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn get_row(
        &self,
        get_row_input: Option<models::GetRowInput>,
        context: &C) -> Result<GetRowResponse, ApiError>
    {
        let context = context.clone();
        info!("get_row({:?}) - X-Span-ID: {:?}", get_row_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn in_random_order(
        &self,
        in_random_order_input: Option<models::InRandomOrderInput>,
        context: &C) -> Result<InRandomOrderResponse, ApiError>
    {
        let context = context.clone();
        info!("in_random_order({:?}) - X-Span-ID: {:?}", in_random_order_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn interquartile_range(
        &self,
        interquartile_range_input: Option<models::InterquartileRangeInput>,
        context: &C) -> Result<InterquartileRangeResponse, ApiError>
    {
        let context = context.clone();
        info!("interquartile_range({:?}) - X-Span-ID: {:?}", interquartile_range_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn magnitude(
        &self,
        magnitude_input: Option<models::MagnitudeInput>,
        context: &C) -> Result<MagnitudeResponse, ApiError>
    {
        let context = context.clone();
        info!("magnitude({:?}) - X-Span-ID: {:?}", magnitude_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn matrix_add(
        &self,
        matrix_add_input: Option<models::MatrixAddInput>,
        context: &C) -> Result<MatrixAddResponse, ApiError>
    {
        let context = context.clone();
        info!("matrix_add({:?}) - X-Span-ID: {:?}", matrix_add_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn maximize_batch(
        &self,
        maximize_batch_input: Option<models::MaximizeBatchInput>,
        context: &C) -> Result<MaximizeBatchResponse, ApiError>
    {
        let context = context.clone();
        info!("maximize_batch({:?}) - X-Span-ID: {:?}", maximize_batch_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn maximize_stochastic(
        &self,
        maximize_stochastic_input: Option<models::MaximizeStochasticInput>,
        context: &C) -> Result<MaximizeStochasticResponse, ApiError>
    {
        let context = context.clone();
        info!("maximize_stochastic({:?}) - X-Span-ID: {:?}", maximize_stochastic_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn mean(
        &self,
        mean_input: Option<models::MeanInput>,
        context: &C) -> Result<MeanResponse, ApiError>
    {
        let context = context.clone();
        info!("mean({:?}) - X-Span-ID: {:?}", mean_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn median(
        &self,
        median_input: Option<models::MedianInput>,
        context: &C) -> Result<MedianResponse, ApiError>
    {
        let context = context.clone();
        info!("median({:?}) - X-Span-ID: {:?}", median_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn minimize_batch(
        &self,
        minimize_batch_input: Option<models::MinimizeBatchInput>,
        context: &C) -> Result<MinimizeBatchResponse, ApiError>
    {
        let context = context.clone();
        info!("minimize_batch({:?}) - X-Span-ID: {:?}", minimize_batch_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn minimize_stochastic(
        &self,
        minimize_stochastic_input: Option<models::MinimizeStochasticInput>,
        context: &C) -> Result<MinimizeStochasticResponse, ApiError>
    {
        let context = context.clone();
        info!("minimize_stochastic({:?}) - X-Span-ID: {:?}", minimize_stochastic_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn mode(
        &self,
        mode_input: Option<models::ModeInput>,
        context: &C) -> Result<ModeResponse, ApiError>
    {
        let context = context.clone();
        info!("mode({:?}) - X-Span-ID: {:?}", mode_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn partial_difference_quotient(
        &self,
        partial_difference_quotient_input: Option<models::PartialDifferenceQuotientInput>,
        context: &C) -> Result<PartialDifferenceQuotientResponse, ApiError>
    {
        let context = context.clone();
        info!("partial_difference_quotient({:?}) - X-Span-ID: {:?}", partial_difference_quotient_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn precision(
        &self,
        precision_input: Option<models::PrecisionInput>,
        context: &C) -> Result<PrecisionResponse, ApiError>
    {
        let context = context.clone();
        info!("precision({:?}) - X-Span-ID: {:?}", precision_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn quantile(
        &self,
        quantile_input: Option<models::QuantileInput>,
        context: &C) -> Result<QuantileResponse, ApiError>
    {
        let context = context.clone();
        info!("quantile({:?}) - X-Span-ID: {:?}", quantile_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn recall(
        &self,
        recall_input: Option<models::RecallInput>,
        context: &C) -> Result<RecallResponse, ApiError>
    {
        let context = context.clone();
        info!("recall({:?}) - X-Span-ID: {:?}", recall_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn scalar_multiply(
        &self,
        scalar_multiply_input: Option<models::ScalarMultiplyInput>,
        context: &C) -> Result<ScalarMultiplyResponse, ApiError>
    {
        let context = context.clone();
        info!("scalar_multiply({:?}) - X-Span-ID: {:?}", scalar_multiply_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn shape(
        &self,
        shape_input: Option<models::ShapeInput>,
        context: &C) -> Result<ShapeResponse, ApiError>
    {
        let context = context.clone();
        info!("shape({:?}) - X-Span-ID: {:?}", shape_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn split_data(
        &self,
        split_data_input: Option<models::SplitDataInput>,
        context: &C) -> Result<SplitDataResponse, ApiError>
    {
        let context = context.clone();
        info!("split_data({:?}) - X-Span-ID: {:?}", split_data_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn sqrt(
        &self,
        sqrt_input: Option<models::SqrtInput>,
        context: &C) -> Result<SqrtResponse, ApiError>
    {
        let context = context.clone();
        info!("sqrt({:?}) - X-Span-ID: {:?}", sqrt_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn squared_distance(
        &self,
        squared_distance_input: Option<models::SquaredDistanceInput>,
        context: &C) -> Result<SquaredDistanceResponse, ApiError>
    {
        let context = context.clone();
        info!("squared_distance({:?}) - X-Span-ID: {:?}", squared_distance_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn standard_deviation(
        &self,
        standard_deviation_input: Option<models::StandardDeviationInput>,
        context: &C) -> Result<StandardDeviationResponse, ApiError>
    {
        let context = context.clone();
        info!("standard_deviation({:?}) - X-Span-ID: {:?}", standard_deviation_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn strength(
        &self,
        strength_input: Option<models::StrengthInput>,
        context: &C) -> Result<StrengthResponse, ApiError>
    {
        let context = context.clone();
        info!("strength({:?}) - X-Span-ID: {:?}", strength_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn sum_of_squares(
        &self,
        sum_of_squares_input: Option<models::SumOfSquaresInput>,
        context: &C) -> Result<SumOfSquaresResponse, ApiError>
    {
        let context = context.clone();
        info!("sum_of_squares({:?}) - X-Span-ID: {:?}", sum_of_squares_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn train_test_split(
        &self,
        train_test_split_input: Option<models::TrainTestSplitInput>,
        context: &C) -> Result<TrainTestSplitResponse, ApiError>
    {
        let context = context.clone();
        info!("train_test_split({:?}) - X-Span-ID: {:?}", train_test_split_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn variance(
        &self,
        variance_input: Option<models::VarianceInput>,
        context: &C) -> Result<VarianceResponse, ApiError>
    {
        let context = context.clone();
        info!("variance({:?}) - X-Span-ID: {:?}", variance_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn vector_add(
        &self,
        vector_add_input: Option<models::VectorAddInput>,
        context: &C) -> Result<VectorAddResponse, ApiError>
    {
        let context = context.clone();
        info!("vector_add({:?}) - X-Span-ID: {:?}", vector_add_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn vector_mean(
        &self,
        vector_mean_input: Option<models::VectorMeanInput>,
        context: &C) -> Result<VectorMeanResponse, ApiError>
    {
        let context = context.clone();
        info!("vector_mean({:?}) - X-Span-ID: {:?}", vector_mean_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn vector_subtract(
        &self,
        vector_subtract_input: Option<models::VectorSubtractInput>,
        context: &C) -> Result<VectorSubtractResponse, ApiError>
    {
        let context = context.clone();
        info!("vector_subtract({:?}) - X-Span-ID: {:?}", vector_subtract_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    async fn vector_sum(
        &self,
        vector_sum_input: Option<models::VectorSumInput>,
        context: &C) -> Result<VectorSumResponse, ApiError>
    {
        let context = context.clone();
        info!("vector_sum({:?}) - X-Span-ID: {:?}", vector_sum_input, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Add a new pet to the store
    async fn add_pet(
        &self,
        body: models::Pet,
        context: &C) -> Result<AddPetResponse, ApiError>
    {
        let context = context.clone();
        info!("add_pet({:?}) - X-Span-ID: {:?}", body, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Deletes a pet
    async fn delete_pet(
        &self,
        pet_id: i64,
        api_key: Option<String>,
        context: &C) -> Result<DeletePetResponse, ApiError>
    {
        let context = context.clone();
        info!("delete_pet({}, {:?}) - X-Span-ID: {:?}", pet_id, api_key, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Finds Pets by status
    async fn find_pets_by_status(
        &self,
        status: &Vec<String>,
        context: &C) -> Result<FindPetsByStatusResponse, ApiError>
    {
        let context = context.clone();
        info!("find_pets_by_status({:?}) - X-Span-ID: {:?}", status, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Finds Pets by tags
    async fn find_pets_by_tags(
        &self,
        tags: &Vec<String>,
        context: &C) -> Result<FindPetsByTagsResponse, ApiError>
    {
        let context = context.clone();
        info!("find_pets_by_tags({:?}) - X-Span-ID: {:?}", tags, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Find pet by ID
    async fn get_pet_by_id(
        &self,
        pet_id: i64,
        context: &C) -> Result<GetPetByIdResponse, ApiError>
    {
        let context = context.clone();
        info!("get_pet_by_id({}) - X-Span-ID: {:?}", pet_id, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Update an existing pet
    async fn update_pet(
        &self,
        body: models::Pet,
        context: &C) -> Result<UpdatePetResponse, ApiError>
    {
        let context = context.clone();
        info!("update_pet({:?}) - X-Span-ID: {:?}", body, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Updates a pet in the store with form data
    async fn update_pet_with_form(
        &self,
        pet_id: i64,
        name: Option<String>,
        status: Option<String>,
        context: &C) -> Result<UpdatePetWithFormResponse, ApiError>
    {
        let context = context.clone();
        info!("update_pet_with_form({}, {:?}, {:?}) - X-Span-ID: {:?}", pet_id, name, status, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// uploads an image
    async fn upload_file(
        &self,
        pet_id: i64,
        additional_metadata: Option<String>,
        file: Option<swagger::ByteArray>,
        context: &C) -> Result<UploadFileResponse, ApiError>
    {
        let context = context.clone();
        info!("upload_file({}, {:?}, {:?}) - X-Span-ID: {:?}", pet_id, additional_metadata, file, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Delete purchase order by ID
    async fn delete_order(
        &self,
        order_id: i64,
        context: &C) -> Result<DeleteOrderResponse, ApiError>
    {
        let context = context.clone();
        info!("delete_order({}) - X-Span-ID: {:?}", order_id, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Returns pet inventories by status
    async fn get_inventory(
        &self,
        context: &C) -> Result<GetInventoryResponse, ApiError>
    {
        let context = context.clone();
        info!("get_inventory() - X-Span-ID: {:?}", context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Find purchase order by ID
    async fn get_order_by_id(
        &self,
        order_id: i64,
        context: &C) -> Result<GetOrderByIdResponse, ApiError>
    {
        let context = context.clone();
        info!("get_order_by_id({}) - X-Span-ID: {:?}", order_id, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Place an order for a pet
    async fn place_order(
        &self,
        body: models::Order,
        context: &C) -> Result<PlaceOrderResponse, ApiError>
    {
        let context = context.clone();
        info!("place_order({:?}) - X-Span-ID: {:?}", body, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Create user
    async fn create_user(
        &self,
        body: models::User,
        context: &C) -> Result<CreateUserResponse, ApiError>
    {
        let context = context.clone();
        info!("create_user({:?}) - X-Span-ID: {:?}", body, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Creates list of users with given input array
    async fn create_users_with_array_input(
        &self,
        body: &Vec<models::User>,
        context: &C) -> Result<CreateUsersWithArrayInputResponse, ApiError>
    {
        let context = context.clone();
        info!("create_users_with_array_input({:?}) - X-Span-ID: {:?}", body, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Creates list of users with given input array
    async fn create_users_with_list_input(
        &self,
        body: &Vec<models::User>,
        context: &C) -> Result<CreateUsersWithListInputResponse, ApiError>
    {
        let context = context.clone();
        info!("create_users_with_list_input({:?}) - X-Span-ID: {:?}", body, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Delete user
    async fn delete_user(
        &self,
        username: String,
        context: &C) -> Result<DeleteUserResponse, ApiError>
    {
        let context = context.clone();
        info!("delete_user(\"{}\") - X-Span-ID: {:?}", username, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Get user by user name
    async fn get_user_by_name(
        &self,
        username: String,
        context: &C) -> Result<GetUserByNameResponse, ApiError>
    {
        let context = context.clone();
        info!("get_user_by_name(\"{}\") - X-Span-ID: {:?}", username, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Logs user into the system
    async fn login_user(
        &self,
        username: String,
        password: String,
        context: &C) -> Result<LoginUserResponse, ApiError>
    {
        let context = context.clone();
        info!("login_user(\"{}\", \"{}\") - X-Span-ID: {:?}", username, password, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Logs out current logged in user session
    async fn logout_user(
        &self,
        context: &C) -> Result<LogoutUserResponse, ApiError>
    {
        let context = context.clone();
        info!("logout_user() - X-Span-ID: {:?}", context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

    /// Updated user
    async fn update_user(
        &self,
        username: String,
        body: models::User,
        context: &C) -> Result<UpdateUserResponse, ApiError>
    {
        let context = context.clone();
        info!("update_user(\"{}\", {:?}) - X-Span-ID: {:?}", username, body, context.get().0.clone());
        Err(ApiError("Generic failure".into()))
    }

}
