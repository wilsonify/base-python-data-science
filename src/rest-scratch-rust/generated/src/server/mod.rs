use futures::{future, future::BoxFuture, Stream, stream, future::FutureExt, stream::TryStreamExt};
use hyper::{Request, Response, StatusCode, Body, HeaderMap};
use hyper::header::{HeaderName, HeaderValue, CONTENT_TYPE};
use log::warn;
#[allow(unused_imports)]
use std::convert::{TryFrom, TryInto};
use std::error::Error;
use std::future::Future;
use std::marker::PhantomData;
use std::task::{Context, Poll};
use swagger::{ApiError, BodyExt, Has, RequestParser, XSpanIdString};
pub use swagger::auth::Authorization;
use swagger::auth::Scopes;
use url::form_urlencoded;
use multipart::server::Multipart;
use multipart::server::save::SaveResult;

#[allow(unused_imports)]
use crate::models;
use crate::header;

pub use crate::context;

type ServiceFuture = BoxFuture<'static, Result<Response<Body>, crate::ServiceError>>;

use crate::{Api,
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
     UpdateUserResponse
};

mod paths {
    use lazy_static::lazy_static;

    lazy_static! {
        pub static ref GLOBAL_REGEX_SET: regex::RegexSet = regex::RegexSet::new(vec![
            r"^/v2/accuracy$",
            r"^/v2/bucketize$",
            r"^/v2/correlation$",
            r"^/v2/correlation_matrix$",
            r"^/v2/covariance$",
            r"^/v2/data_range$",
            r"^/v2/de_mean$",
            r"^/v2/difference_quotient$",
            r"^/v2/distance$",
            r"^/v2/dot$",
            r"^/v2/echo$",
            r"^/v2/estimate_gradient$",
            r"^/v2/f1_score$",
            r"^/v2/get_column$",
            r"^/v2/get_row$",
            r"^/v2/in_random_order$",
            r"^/v2/interquartile_range$",
            r"^/v2/magnitude$",
            r"^/v2/matrix_add$",
            r"^/v2/maximize_batch$",
            r"^/v2/maximize_stochastic$",
            r"^/v2/mean$",
            r"^/v2/median$",
            r"^/v2/minimize_batch$",
            r"^/v2/minimize_stochastic$",
            r"^/v2/mode$",
            r"^/v2/partial_difference_quotient$",
            r"^/v2/pet$",
            r"^/v2/pet/findByStatus$",
            r"^/v2/pet/findByTags$",
            r"^/v2/pet/(?P<petId>[^/?#]*)$",
            r"^/v2/pet/(?P<petId>[^/?#]*)/uploadImage$",
            r"^/v2/precision$",
            r"^/v2/quantile$",
            r"^/v2/recall$",
            r"^/v2/scalar_multiply$",
            r"^/v2/shape$",
            r"^/v2/split_data$",
            r"^/v2/sqrt$",
            r"^/v2/squared_distance$",
            r"^/v2/standard_deviation$",
            r"^/v2/store/inventory$",
            r"^/v2/store/order$",
            r"^/v2/store/order/(?P<orderId>[^/?#]*)$",
            r"^/v2/strength$",
            r"^/v2/sum_of_squares$",
            r"^/v2/train_test_split$",
            r"^/v2/user$",
            r"^/v2/user/createWithArray$",
            r"^/v2/user/createWithList$",
            r"^/v2/user/login$",
            r"^/v2/user/logout$",
            r"^/v2/user/(?P<username>[^/?#]*)$",
            r"^/v2/variance$",
            r"^/v2/vector_add$",
            r"^/v2/vector_mean$",
            r"^/v2/vector_subtract$",
            r"^/v2/vector_sum$"
        ])
        .expect("Unable to create global regex set");
    }
    pub(crate) static ID_ACCURACY: usize = 0;
    pub(crate) static ID_BUCKETIZE: usize = 1;
    pub(crate) static ID_CORRELATION: usize = 2;
    pub(crate) static ID_CORRELATION_MATRIX: usize = 3;
    pub(crate) static ID_COVARIANCE: usize = 4;
    pub(crate) static ID_DATA_RANGE: usize = 5;
    pub(crate) static ID_DE_MEAN: usize = 6;
    pub(crate) static ID_DIFFERENCE_QUOTIENT: usize = 7;
    pub(crate) static ID_DISTANCE: usize = 8;
    pub(crate) static ID_DOT: usize = 9;
    pub(crate) static ID_ECHO: usize = 10;
    pub(crate) static ID_ESTIMATE_GRADIENT: usize = 11;
    pub(crate) static ID_F1_SCORE: usize = 12;
    pub(crate) static ID_GET_COLUMN: usize = 13;
    pub(crate) static ID_GET_ROW: usize = 14;
    pub(crate) static ID_IN_RANDOM_ORDER: usize = 15;
    pub(crate) static ID_INTERQUARTILE_RANGE: usize = 16;
    pub(crate) static ID_MAGNITUDE: usize = 17;
    pub(crate) static ID_MATRIX_ADD: usize = 18;
    pub(crate) static ID_MAXIMIZE_BATCH: usize = 19;
    pub(crate) static ID_MAXIMIZE_STOCHASTIC: usize = 20;
    pub(crate) static ID_MEAN: usize = 21;
    pub(crate) static ID_MEDIAN: usize = 22;
    pub(crate) static ID_MINIMIZE_BATCH: usize = 23;
    pub(crate) static ID_MINIMIZE_STOCHASTIC: usize = 24;
    pub(crate) static ID_MODE: usize = 25;
    pub(crate) static ID_PARTIAL_DIFFERENCE_QUOTIENT: usize = 26;
    pub(crate) static ID_PET: usize = 27;
    pub(crate) static ID_PET_FINDBYSTATUS: usize = 28;
    pub(crate) static ID_PET_FINDBYTAGS: usize = 29;
    pub(crate) static ID_PET_PETID: usize = 30;
    lazy_static! {
        pub static ref REGEX_PET_PETID: regex::Regex =
            #[allow(clippy::invalid_regex)]
            regex::Regex::new(r"^/v2/pet/(?P<petId>[^/?#]*)$")
                .expect("Unable to create regex for PET_PETID");
    }
    pub(crate) static ID_PET_PETID_UPLOADIMAGE: usize = 31;
    lazy_static! {
        pub static ref REGEX_PET_PETID_UPLOADIMAGE: regex::Regex =
            #[allow(clippy::invalid_regex)]
            regex::Regex::new(r"^/v2/pet/(?P<petId>[^/?#]*)/uploadImage$")
                .expect("Unable to create regex for PET_PETID_UPLOADIMAGE");
    }
    pub(crate) static ID_PRECISION: usize = 32;
    pub(crate) static ID_QUANTILE: usize = 33;
    pub(crate) static ID_RECALL: usize = 34;
    pub(crate) static ID_SCALAR_MULTIPLY: usize = 35;
    pub(crate) static ID_SHAPE: usize = 36;
    pub(crate) static ID_SPLIT_DATA: usize = 37;
    pub(crate) static ID_SQRT: usize = 38;
    pub(crate) static ID_SQUARED_DISTANCE: usize = 39;
    pub(crate) static ID_STANDARD_DEVIATION: usize = 40;
    pub(crate) static ID_STORE_INVENTORY: usize = 41;
    pub(crate) static ID_STORE_ORDER: usize = 42;
    pub(crate) static ID_STORE_ORDER_ORDERID: usize = 43;
    lazy_static! {
        pub static ref REGEX_STORE_ORDER_ORDERID: regex::Regex =
            #[allow(clippy::invalid_regex)]
            regex::Regex::new(r"^/v2/store/order/(?P<orderId>[^/?#]*)$")
                .expect("Unable to create regex for STORE_ORDER_ORDERID");
    }
    pub(crate) static ID_STRENGTH: usize = 44;
    pub(crate) static ID_SUM_OF_SQUARES: usize = 45;
    pub(crate) static ID_TRAIN_TEST_SPLIT: usize = 46;
    pub(crate) static ID_USER: usize = 47;
    pub(crate) static ID_USER_CREATEWITHARRAY: usize = 48;
    pub(crate) static ID_USER_CREATEWITHLIST: usize = 49;
    pub(crate) static ID_USER_LOGIN: usize = 50;
    pub(crate) static ID_USER_LOGOUT: usize = 51;
    pub(crate) static ID_USER_USERNAME: usize = 52;
    lazy_static! {
        pub static ref REGEX_USER_USERNAME: regex::Regex =
            #[allow(clippy::invalid_regex)]
            regex::Regex::new(r"^/v2/user/(?P<username>[^/?#]*)$")
                .expect("Unable to create regex for USER_USERNAME");
    }
    pub(crate) static ID_VARIANCE: usize = 53;
    pub(crate) static ID_VECTOR_ADD: usize = 54;
    pub(crate) static ID_VECTOR_MEAN: usize = 55;
    pub(crate) static ID_VECTOR_SUBTRACT: usize = 56;
    pub(crate) static ID_VECTOR_SUM: usize = 57;
}

pub struct MakeService<T, C> where
    T: Api<C> + Clone + Send + 'static,
    C: Has<XSpanIdString> + Has<Option<Authorization>> + Send + Sync + 'static
{
    api_impl: T,
    marker: PhantomData<C>,
}

impl<T, C> MakeService<T, C> where
    T: Api<C> + Clone + Send + 'static,
    C: Has<XSpanIdString> + Has<Option<Authorization>> + Send + Sync + 'static
{
    pub fn new(api_impl: T) -> Self {
        MakeService {
            api_impl,
            marker: PhantomData
        }
    }
}

impl<T, C, Target> hyper::service::Service<Target> for MakeService<T, C> where
    T: Api<C> + Clone + Send + 'static,
    C: Has<XSpanIdString> + Has<Option<Authorization>> + Send + Sync + 'static
{
    type Response = Service<T, C>;
    type Error = crate::ServiceError;
    type Future = future::Ready<Result<Self::Response, Self::Error>>;

    fn poll_ready(&mut self, cx: &mut Context<'_>) -> Poll<Result<(), Self::Error>> {
        Poll::Ready(Ok(()))
    }

    fn call(&mut self, target: Target) -> Self::Future {
        futures::future::ok(Service::new(
            self.api_impl.clone(),
        ))
    }
}

fn method_not_allowed() -> Result<Response<Body>, crate::ServiceError> {
    Ok(
        Response::builder().status(StatusCode::METHOD_NOT_ALLOWED)
            .body(Body::empty())
            .expect("Unable to create Method Not Allowed response")
    )
}

pub struct Service<T, C> where
    T: Api<C> + Clone + Send + 'static,
    C: Has<XSpanIdString> + Has<Option<Authorization>> + Send + Sync + 'static
{
    api_impl: T,
    marker: PhantomData<C>,
}

impl<T, C> Service<T, C> where
    T: Api<C> + Clone + Send + 'static,
    C: Has<XSpanIdString> + Has<Option<Authorization>> + Send + Sync + 'static
{
    pub fn new(api_impl: T) -> Self {
        Service {
            api_impl,
            marker: PhantomData
        }
    }
}

impl<T, C> Clone for Service<T, C> where
    T: Api<C> + Clone + Send + 'static,
    C: Has<XSpanIdString> + Has<Option<Authorization>> + Send + Sync + 'static
{
    fn clone(&self) -> Self {
        Service {
            api_impl: self.api_impl.clone(),
            marker: self.marker,
        }
    }
}

impl<T, C> hyper::service::Service<(Request<Body>, C)> for Service<T, C> where
    T: Api<C> + Clone + Send + Sync + 'static,
    C: Has<XSpanIdString> + Has<Option<Authorization>> + Send + Sync + 'static
{
    type Response = Response<Body>;
    type Error = crate::ServiceError;
    type Future = ServiceFuture;

    fn poll_ready(&mut self, cx: &mut Context) -> Poll<Result<(), Self::Error>> {
        self.api_impl.poll_ready(cx)
    }

    fn call(&mut self, req: (Request<Body>, C)) -> Self::Future { async fn run<T, C>(mut api_impl: T, req: (Request<Body>, C)) -> Result<Response<Body>, crate::ServiceError> where
        T: Api<C> + Clone + Send + 'static,
        C: Has<XSpanIdString> + Has<Option<Authorization>> + Send + Sync + 'static
    {
        let (request, context) = req;
        let (parts, body) = request.into_parts();
        let (method, uri, headers) = (parts.method, parts.uri, parts.headers);
        let path = paths::GLOBAL_REGEX_SET.matches(uri.path());

        match method {

            // Accuracy - POST /accuracy
            hyper::Method::POST if path.matched(paths::ID_ACCURACY) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_accuracy_input: Option<models::AccuracyInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_accuracy_input) => param_accuracy_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.accuracy(
                                            param_accuracy_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                AccuracyResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for ACCURACY_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter AccuracyInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter AccuracyInput")),
                        }
            },

            // Bucketize - POST /bucketize
            hyper::Method::POST if path.matched(paths::ID_BUCKETIZE) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_bucketize_input: Option<models::BucketizeInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_bucketize_input) => param_bucketize_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.bucketize(
                                            param_bucketize_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                BucketizeResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for BUCKETIZE_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter BucketizeInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter BucketizeInput")),
                        }
            },

            // Correlation - POST /correlation
            hyper::Method::POST if path.matched(paths::ID_CORRELATION) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_correlation_input: Option<models::CorrelationInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_correlation_input) => param_correlation_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.correlation(
                                            param_correlation_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                CorrelationResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for CORRELATION_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter CorrelationInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter CorrelationInput")),
                        }
            },

            // CorrelationMatrix - POST /correlation_matrix
            hyper::Method::POST if path.matched(paths::ID_CORRELATION_MATRIX) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_correlation_matrix_input: Option<models::CorrelationMatrixInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_correlation_matrix_input) => param_correlation_matrix_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.correlation_matrix(
                                            param_correlation_matrix_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                CorrelationMatrixResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for CORRELATION_MATRIX_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter CorrelationMatrixInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter CorrelationMatrixInput")),
                        }
            },

            // Covariance - POST /covariance
            hyper::Method::POST if path.matched(paths::ID_COVARIANCE) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_covariance_input: Option<models::CovarianceInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_covariance_input) => param_covariance_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.covariance(
                                            param_covariance_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                CovarianceResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for COVARIANCE_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter CovarianceInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter CovarianceInput")),
                        }
            },

            // DataRange - POST /data_range
            hyper::Method::POST if path.matched(paths::ID_DATA_RANGE) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_data_range_input: Option<models::DataRangeInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_data_range_input) => param_data_range_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.data_range(
                                            param_data_range_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                DataRangeResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for DATA_RANGE_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter DataRangeInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter DataRangeInput")),
                        }
            },

            // DeMean - POST /de_mean
            hyper::Method::POST if path.matched(paths::ID_DE_MEAN) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_de_mean_input: Option<models::DeMeanInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_de_mean_input) => param_de_mean_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.de_mean(
                                            param_de_mean_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                DeMeanResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for DE_MEAN_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter DeMeanInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter DeMeanInput")),
                        }
            },

            // DifferenceQuotient - POST /difference_quotient
            hyper::Method::POST if path.matched(paths::ID_DIFFERENCE_QUOTIENT) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_difference_quotient_input: Option<models::DifferenceQuotientInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_difference_quotient_input) => param_difference_quotient_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.difference_quotient(
                                            param_difference_quotient_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                DifferenceQuotientResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for DIFFERENCE_QUOTIENT_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter DifferenceQuotientInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter DifferenceQuotientInput")),
                        }
            },

            // Distance - POST /distance
            hyper::Method::POST if path.matched(paths::ID_DISTANCE) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_distance_input: Option<models::DistanceInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_distance_input) => param_distance_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.distance(
                                            param_distance_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                DistanceResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for DISTANCE_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter DistanceInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter DistanceInput")),
                        }
            },

            // Dot - POST /dot
            hyper::Method::POST if path.matched(paths::ID_DOT) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_dot_input: Option<models::DotInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_dot_input) => param_dot_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.dot(
                                            param_dot_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                DotResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for DOT_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter DotInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter DotInput")),
                        }
            },

            // Echo - POST /echo
            hyper::Method::POST if path.matched(paths::ID_ECHO) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_body: Option<models::EchoInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_body) => param_body,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.echo(
                                            param_body,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                EchoResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for ECHO_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter body: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter body")),
                        }
            },

            // EstimateGradient - POST /estimate_gradient
            hyper::Method::POST if path.matched(paths::ID_ESTIMATE_GRADIENT) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_estimate_gradient_input: Option<models::EstimateGradientInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_estimate_gradient_input) => param_estimate_gradient_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.estimate_gradient(
                                            param_estimate_gradient_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                EstimateGradientResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for ESTIMATE_GRADIENT_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter EstimateGradientInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter EstimateGradientInput")),
                        }
            },

            // F1Score - POST /f1_score
            hyper::Method::POST if path.matched(paths::ID_F1_SCORE) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_f1_score_input: Option<models::F1ScoreInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_f1_score_input) => param_f1_score_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.f1_score(
                                            param_f1_score_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                F1ScoreResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for F1_SCORE_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter F1ScoreInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter F1ScoreInput")),
                        }
            },

            // GetColumn - POST /get_column
            hyper::Method::POST if path.matched(paths::ID_GET_COLUMN) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_get_column_input: Option<models::GetColumnInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_get_column_input) => param_get_column_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.get_column(
                                            param_get_column_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                GetColumnResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for GET_COLUMN_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter GetColumnInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter GetColumnInput")),
                        }
            },

            // GetRow - POST /get_row
            hyper::Method::POST if path.matched(paths::ID_GET_ROW) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_get_row_input: Option<models::GetRowInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_get_row_input) => param_get_row_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.get_row(
                                            param_get_row_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                GetRowResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for GET_ROW_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter GetRowInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter GetRowInput")),
                        }
            },

            // InRandomOrder - POST /in_random_order
            hyper::Method::POST if path.matched(paths::ID_IN_RANDOM_ORDER) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_in_random_order_input: Option<models::InRandomOrderInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_in_random_order_input) => param_in_random_order_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.in_random_order(
                                            param_in_random_order_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                InRandomOrderResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for IN_RANDOM_ORDER_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter InRandomOrderInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter InRandomOrderInput")),
                        }
            },

            // InterquartileRange - POST /interquartile_range
            hyper::Method::POST if path.matched(paths::ID_INTERQUARTILE_RANGE) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_interquartile_range_input: Option<models::InterquartileRangeInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_interquartile_range_input) => param_interquartile_range_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.interquartile_range(
                                            param_interquartile_range_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                InterquartileRangeResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for INTERQUARTILE_RANGE_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter InterquartileRangeInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter InterquartileRangeInput")),
                        }
            },

            // Magnitude - POST /magnitude
            hyper::Method::POST if path.matched(paths::ID_MAGNITUDE) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_magnitude_input: Option<models::MagnitudeInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_magnitude_input) => param_magnitude_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.magnitude(
                                            param_magnitude_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                MagnitudeResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for MAGNITUDE_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter MagnitudeInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter MagnitudeInput")),
                        }
            },

            // MatrixAdd - POST /matrix_add
            hyper::Method::POST if path.matched(paths::ID_MATRIX_ADD) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_matrix_add_input: Option<models::MatrixAddInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_matrix_add_input) => param_matrix_add_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.matrix_add(
                                            param_matrix_add_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                MatrixAddResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for MATRIX_ADD_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter MatrixAddInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter MatrixAddInput")),
                        }
            },

            // MaximizeBatch - POST /maximize_batch
            hyper::Method::POST if path.matched(paths::ID_MAXIMIZE_BATCH) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_maximize_batch_input: Option<models::MaximizeBatchInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_maximize_batch_input) => param_maximize_batch_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.maximize_batch(
                                            param_maximize_batch_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                MaximizeBatchResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for MAXIMIZE_BATCH_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter MaximizeBatchInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter MaximizeBatchInput")),
                        }
            },

            // MaximizeStochastic - POST /maximize_stochastic
            hyper::Method::POST if path.matched(paths::ID_MAXIMIZE_STOCHASTIC) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_maximize_stochastic_input: Option<models::MaximizeStochasticInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_maximize_stochastic_input) => param_maximize_stochastic_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.maximize_stochastic(
                                            param_maximize_stochastic_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                MaximizeStochasticResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for MAXIMIZE_STOCHASTIC_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter MaximizeStochasticInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter MaximizeStochasticInput")),
                        }
            },

            // Mean - POST /mean
            hyper::Method::POST if path.matched(paths::ID_MEAN) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_mean_input: Option<models::MeanInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_mean_input) => param_mean_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.mean(
                                            param_mean_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                MeanResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for MEAN_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter MeanInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter MeanInput")),
                        }
            },

            // Median - POST /median
            hyper::Method::POST if path.matched(paths::ID_MEDIAN) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_median_input: Option<models::MedianInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_median_input) => param_median_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.median(
                                            param_median_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                MedianResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for MEDIAN_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter MedianInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter MedianInput")),
                        }
            },

            // MinimizeBatch - POST /minimize_batch
            hyper::Method::POST if path.matched(paths::ID_MINIMIZE_BATCH) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_minimize_batch_input: Option<models::MinimizeBatchInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_minimize_batch_input) => param_minimize_batch_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.minimize_batch(
                                            param_minimize_batch_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                MinimizeBatchResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for MINIMIZE_BATCH_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter MinimizeBatchInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter MinimizeBatchInput")),
                        }
            },

            // MinimizeStochastic - POST /minimize_stochastic
            hyper::Method::POST if path.matched(paths::ID_MINIMIZE_STOCHASTIC) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_minimize_stochastic_input: Option<models::MinimizeStochasticInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_minimize_stochastic_input) => param_minimize_stochastic_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.minimize_stochastic(
                                            param_minimize_stochastic_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                MinimizeStochasticResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for MINIMIZE_STOCHASTIC_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter MinimizeStochasticInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter MinimizeStochasticInput")),
                        }
            },

            // Mode - POST /mode
            hyper::Method::POST if path.matched(paths::ID_MODE) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_mode_input: Option<models::ModeInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_mode_input) => param_mode_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.mode(
                                            param_mode_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                ModeResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for MODE_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter ModeInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter ModeInput")),
                        }
            },

            // PartialDifferenceQuotient - POST /partial_difference_quotient
            hyper::Method::POST if path.matched(paths::ID_PARTIAL_DIFFERENCE_QUOTIENT) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_partial_difference_quotient_input: Option<models::PartialDifferenceQuotientInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_partial_difference_quotient_input) => param_partial_difference_quotient_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.partial_difference_quotient(
                                            param_partial_difference_quotient_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                PartialDifferenceQuotientResponse::VWithHAddedToJustTheI
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for PARTIAL_DIFFERENCE_QUOTIENT_V_WITH_H_ADDED_TO_JUST_THE_I"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter PartialDifferenceQuotientInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter PartialDifferenceQuotientInput")),
                        }
            },

            // Precision - POST /precision
            hyper::Method::POST if path.matched(paths::ID_PRECISION) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_precision_input: Option<models::PrecisionInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_precision_input) => param_precision_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.precision(
                                            param_precision_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                PrecisionResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for PRECISION_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter PrecisionInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter PrecisionInput")),
                        }
            },

            // Quantile - POST /quantile
            hyper::Method::POST if path.matched(paths::ID_QUANTILE) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_quantile_input: Option<models::QuantileInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_quantile_input) => param_quantile_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.quantile(
                                            param_quantile_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                QuantileResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for QUANTILE_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter QuantileInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter QuantileInput")),
                        }
            },

            // Recall - POST /recall
            hyper::Method::POST if path.matched(paths::ID_RECALL) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_recall_input: Option<models::RecallInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_recall_input) => param_recall_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.recall(
                                            param_recall_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                RecallResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for RECALL_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter RecallInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter RecallInput")),
                        }
            },

            // ScalarMultiply - POST /scalar_multiply
            hyper::Method::POST if path.matched(paths::ID_SCALAR_MULTIPLY) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_scalar_multiply_input: Option<models::ScalarMultiplyInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_scalar_multiply_input) => param_scalar_multiply_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.scalar_multiply(
                                            param_scalar_multiply_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                ScalarMultiplyResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for SCALAR_MULTIPLY_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter ScalarMultiplyInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter ScalarMultiplyInput")),
                        }
            },

            // Shape - POST /shape
            hyper::Method::POST if path.matched(paths::ID_SHAPE) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_shape_input: Option<models::ShapeInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_shape_input) => param_shape_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.shape(
                                            param_shape_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                ShapeResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for SHAPE_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter ShapeInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter ShapeInput")),
                        }
            },

            // SplitData - POST /split_data
            hyper::Method::POST if path.matched(paths::ID_SPLIT_DATA) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_split_data_input: Option<models::SplitDataInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_split_data_input) => param_split_data_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.split_data(
                                            param_split_data_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                SplitDataResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for SPLIT_DATA_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter SplitDataInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter SplitDataInput")),
                        }
            },

            // Sqrt - POST /sqrt
            hyper::Method::POST if path.matched(paths::ID_SQRT) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_sqrt_input: Option<models::SqrtInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_sqrt_input) => param_sqrt_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.sqrt(
                                            param_sqrt_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                SqrtResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for SQRT_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter SqrtInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter SqrtInput")),
                        }
            },

            // SquaredDistance - POST /squared_distance
            hyper::Method::POST if path.matched(paths::ID_SQUARED_DISTANCE) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_squared_distance_input: Option<models::SquaredDistanceInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_squared_distance_input) => param_squared_distance_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.squared_distance(
                                            param_squared_distance_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                SquaredDistanceResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for SQUARED_DISTANCE_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter SquaredDistanceInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter SquaredDistanceInput")),
                        }
            },

            // StandardDeviation - POST /standard_deviation
            hyper::Method::POST if path.matched(paths::ID_STANDARD_DEVIATION) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_standard_deviation_input: Option<models::StandardDeviationInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_standard_deviation_input) => param_standard_deviation_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.standard_deviation(
                                            param_standard_deviation_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                StandardDeviationResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for STANDARD_DEVIATION_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter StandardDeviationInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter StandardDeviationInput")),
                        }
            },

            // Strength - POST /strength
            hyper::Method::POST if path.matched(paths::ID_STRENGTH) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_strength_input: Option<models::StrengthInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_strength_input) => param_strength_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.strength(
                                            param_strength_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                StrengthResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for STRENGTH_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter StrengthInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter StrengthInput")),
                        }
            },

            // SumOfSquares - POST /sum_of_squares
            hyper::Method::POST if path.matched(paths::ID_SUM_OF_SQUARES) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_sum_of_squares_input: Option<models::SumOfSquaresInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_sum_of_squares_input) => param_sum_of_squares_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.sum_of_squares(
                                            param_sum_of_squares_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                SumOfSquaresResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for SUM_OF_SQUARES_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter SumOfSquaresInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter SumOfSquaresInput")),
                        }
            },

            // TrainTestSplit - POST /train_test_split
            hyper::Method::POST if path.matched(paths::ID_TRAIN_TEST_SPLIT) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_train_test_split_input: Option<models::TrainTestSplitInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_train_test_split_input) => param_train_test_split_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.train_test_split(
                                            param_train_test_split_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                TrainTestSplitResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for TRAIN_TEST_SPLIT_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter TrainTestSplitInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter TrainTestSplitInput")),
                        }
            },

            // Variance - POST /variance
            hyper::Method::POST if path.matched(paths::ID_VARIANCE) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_variance_input: Option<models::VarianceInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_variance_input) => param_variance_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.variance(
                                            param_variance_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                VarianceResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for VARIANCE_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter VarianceInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter VarianceInput")),
                        }
            },

            // VectorAdd - POST /vector_add
            hyper::Method::POST if path.matched(paths::ID_VECTOR_ADD) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_vector_add_input: Option<models::VectorAddInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_vector_add_input) => param_vector_add_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.vector_add(
                                            param_vector_add_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                VectorAddResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for VECTOR_ADD_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter VectorAddInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter VectorAddInput")),
                        }
            },

            // VectorMean - POST /vector_mean
            hyper::Method::POST if path.matched(paths::ID_VECTOR_MEAN) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_vector_mean_input: Option<models::VectorMeanInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_vector_mean_input) => param_vector_mean_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.vector_mean(
                                            param_vector_mean_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                VectorMeanResponse::Success
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for VECTOR_MEAN_SUCCESS"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter VectorMeanInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter VectorMeanInput")),
                        }
            },

            // VectorSubtract - POST /vector_subtract
            hyper::Method::POST if path.matched(paths::ID_VECTOR_SUBTRACT) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_vector_subtract_input: Option<models::VectorSubtractInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_vector_subtract_input) => param_vector_subtract_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.vector_subtract(
                                            param_vector_subtract_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                VectorSubtractResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for VECTOR_SUBTRACT_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter VectorSubtractInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter VectorSubtractInput")),
                        }
            },

            // VectorSum - POST /vector_sum
            hyper::Method::POST if path.matched(paths::ID_VECTOR_SUM) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_vector_sum_input: Option<models::VectorSumInput> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_vector_sum_input) => param_vector_sum_input,
                                        Err(_) => None,
                                    }
                                } else {
                                    None
                                };

                                let result = api_impl.vector_sum(
                                            param_vector_sum_input,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                VectorSumResponse::DescriptionOfThisResponse
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for VECTOR_SUM_DESCRIPTION_OF_THIS_RESPONSE"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter VectorSumInput: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter VectorSumInput")),
                        }
            },

            // AddPet - POST /pet
            hyper::Method::POST if path.matched(paths::ID_PET) => {
                {
                    let authorization = match *(&context as &dyn Has<Option<Authorization>>).get() {
                        Some(ref authorization) => authorization,
                        None => return Ok(Response::builder()
                                                .status(StatusCode::FORBIDDEN)
                                                .body(Body::from("Unauthenticated"))
                                                .expect("Unable to create Authentication Forbidden response")),
                    };

                    // Authorization
                    if let Scopes::Some(ref scopes) = authorization.scopes {
                        let required_scopes: std::collections::BTreeSet<String> = vec![
                            "write:pets".to_string(), // modify pets in your account
                            "read:pets".to_string(), // read your pets
                        ].into_iter().collect();

                        if !required_scopes.is_subset(scopes) {
                            let missing_scopes = required_scopes.difference(scopes);
                            return Ok(Response::builder()
                                .status(StatusCode::FORBIDDEN)
                                .body(Body::from(missing_scopes.fold(
                                    "Insufficient authorization, missing scopes".to_string(),
                                    |s, scope| format!("{} {}", s, scope))
                                ))
                                .expect("Unable to create Authentication Insufficient response")
                            );
                        }
                    }
                }

                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_body: Option<models::Pet> = if !body.is_empty() {
                                    let deserializer = &mut serde_xml_rs::de::Deserializer::new_from_reader(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_body) => param_body,
                                        Err(e) => return Ok(Response::builder()
                                                        .status(StatusCode::BAD_REQUEST)
                                                        .body(Body::from(format!("Couldn't parse body parameter body - doesn't match schema: {}", e)))
                                                        .expect("Unable to create Bad Request response for invalid body parameter body due to schema")),
                                    }
                                } else {
                                    None
                                };
                                let param_body = match param_body {
                                    Some(param_body) => param_body,
                                    None => return Ok(Response::builder()
                                                        .status(StatusCode::BAD_REQUEST)
                                                        .body(Body::from("Missing required body parameter body"))
                                                        .expect("Unable to create Bad Request response for missing body parameter body")),
                                };

                                let result = api_impl.add_pet(
                                            param_body,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                AddPetResponse::InvalidInput
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(405).expect("Unable to turn 405 into a StatusCode");
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter body: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter body")),
                        }
            },

            // DeletePet - DELETE /pet/{petId}
            hyper::Method::DELETE if path.matched(paths::ID_PET_PETID) => {
                {
                    let authorization = match *(&context as &dyn Has<Option<Authorization>>).get() {
                        Some(ref authorization) => authorization,
                        None => return Ok(Response::builder()
                                                .status(StatusCode::FORBIDDEN)
                                                .body(Body::from("Unauthenticated"))
                                                .expect("Unable to create Authentication Forbidden response")),
                    };

                    // Authorization
                    if let Scopes::Some(ref scopes) = authorization.scopes {
                        let required_scopes: std::collections::BTreeSet<String> = vec![
                            "write:pets".to_string(), // modify pets in your account
                            "read:pets".to_string(), // read your pets
                        ].into_iter().collect();

                        if !required_scopes.is_subset(scopes) {
                            let missing_scopes = required_scopes.difference(scopes);
                            return Ok(Response::builder()
                                .status(StatusCode::FORBIDDEN)
                                .body(Body::from(missing_scopes.fold(
                                    "Insufficient authorization, missing scopes".to_string(),
                                    |s, scope| format!("{} {}", s, scope))
                                ))
                                .expect("Unable to create Authentication Insufficient response")
                            );
                        }
                    }
                }

                // Path parameters
                let path: &str = uri.path();
                let path_params =
                    paths::REGEX_PET_PETID
                    .captures(path)
                    .unwrap_or_else(||
                        panic!("Path {} matched RE PET_PETID in set but failed match against \"{}\"", path, paths::REGEX_PET_PETID.as_str())
                    );

                let param_pet_id = match percent_encoding::percent_decode(path_params["petId"].as_bytes()).decode_utf8() {
                    Ok(param_pet_id) => match param_pet_id.parse::<i64>() {
                        Ok(param_pet_id) => param_pet_id,
                        Err(e) => return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Couldn't parse path parameter petId: {}", e)))
                                        .expect("Unable to create Bad Request response for invalid path parameter")),
                    },
                    Err(_) => return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Couldn't percent-decode path parameter as UTF-8: {}", &path_params["petId"])))
                                        .expect("Unable to create Bad Request response for invalid percent decode"))
                };

                // Header parameters
                let param_api_key = headers.get(HeaderName::from_static("api_key"));

                let param_api_key = match param_api_key {
                    Some(v) => match header::IntoHeaderValue::<String>::try_from((*v).clone()) {
                        Ok(result) =>
                            Some(result.0),
                        Err(err) => {
                            return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Invalid header api_key - {}", err)))
                                        .expect("Unable to create Bad Request response for invalid header api_key"));

                        },
                    },
                    None => {
                        None
                    }
                };

                                let result = api_impl.delete_pet(
                                            param_pet_id,
                                            param_api_key,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        match result {
                                            Ok(rsp) => match rsp {
                                                DeletePetResponse::InvalidIDSupplied
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(400).expect("Unable to turn 400 into a StatusCode");
                                                },
                                                DeletePetResponse::PetNotFound
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(404).expect("Unable to turn 404 into a StatusCode");
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
            },

            // FindPetsByStatus - GET /pet/findByStatus
            hyper::Method::GET if path.matched(paths::ID_PET_FINDBYSTATUS) => {
                {
                    let authorization = match *(&context as &dyn Has<Option<Authorization>>).get() {
                        Some(ref authorization) => authorization,
                        None => return Ok(Response::builder()
                                                .status(StatusCode::FORBIDDEN)
                                                .body(Body::from("Unauthenticated"))
                                                .expect("Unable to create Authentication Forbidden response")),
                    };

                    // Authorization
                    if let Scopes::Some(ref scopes) = authorization.scopes {
                        let required_scopes: std::collections::BTreeSet<String> = vec![
                            "write:pets".to_string(), // modify pets in your account
                            "read:pets".to_string(), // read your pets
                        ].into_iter().collect();

                        if !required_scopes.is_subset(scopes) {
                            let missing_scopes = required_scopes.difference(scopes);
                            return Ok(Response::builder()
                                .status(StatusCode::FORBIDDEN)
                                .body(Body::from(missing_scopes.fold(
                                    "Insufficient authorization, missing scopes".to_string(),
                                    |s, scope| format!("{} {}", s, scope))
                                ))
                                .expect("Unable to create Authentication Insufficient response")
                            );
                        }
                    }
                }

                // Query parameters (note that non-required or collection query parameters will ignore garbage values, rather than causing a 400 response)
                let query_params = form_urlencoded::parse(uri.query().unwrap_or_default().as_bytes()).collect::<Vec<_>>();
                let param_status = query_params.iter().filter(|e| e.0 == "status").map(|e| e.1.to_owned())
                    .filter_map(|param_status| param_status.parse().ok())
                    .collect::<Vec<_>>();

                                let result = api_impl.find_pets_by_status(
                                            param_status.as_ref(),
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        match result {
                                            Ok(rsp) => match rsp {
                                                FindPetsByStatusResponse::SuccessfulOperation
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/xml")
                                                            .expect("Unable to create Content-Type header for FIND_PETS_BY_STATUS_SUCCESSFUL_OPERATION"));
                                                    let body = serde_xml_rs::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                                FindPetsByStatusResponse::InvalidStatusValue
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(400).expect("Unable to turn 400 into a StatusCode");
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
            },

            // FindPetsByTags - GET /pet/findByTags
            hyper::Method::GET if path.matched(paths::ID_PET_FINDBYTAGS) => {
                {
                    let authorization = match *(&context as &dyn Has<Option<Authorization>>).get() {
                        Some(ref authorization) => authorization,
                        None => return Ok(Response::builder()
                                                .status(StatusCode::FORBIDDEN)
                                                .body(Body::from("Unauthenticated"))
                                                .expect("Unable to create Authentication Forbidden response")),
                    };

                    // Authorization
                    if let Scopes::Some(ref scopes) = authorization.scopes {
                        let required_scopes: std::collections::BTreeSet<String> = vec![
                            "write:pets".to_string(), // modify pets in your account
                            "read:pets".to_string(), // read your pets
                        ].into_iter().collect();

                        if !required_scopes.is_subset(scopes) {
                            let missing_scopes = required_scopes.difference(scopes);
                            return Ok(Response::builder()
                                .status(StatusCode::FORBIDDEN)
                                .body(Body::from(missing_scopes.fold(
                                    "Insufficient authorization, missing scopes".to_string(),
                                    |s, scope| format!("{} {}", s, scope))
                                ))
                                .expect("Unable to create Authentication Insufficient response")
                            );
                        }
                    }
                }

                // Query parameters (note that non-required or collection query parameters will ignore garbage values, rather than causing a 400 response)
                let query_params = form_urlencoded::parse(uri.query().unwrap_or_default().as_bytes()).collect::<Vec<_>>();
                let param_tags = query_params.iter().filter(|e| e.0 == "tags").map(|e| e.1.to_owned())
                    .filter_map(|param_tags| param_tags.parse().ok())
                    .collect::<Vec<_>>();

                                let result = api_impl.find_pets_by_tags(
                                            param_tags.as_ref(),
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        match result {
                                            Ok(rsp) => match rsp {
                                                FindPetsByTagsResponse::SuccessfulOperation
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/xml")
                                                            .expect("Unable to create Content-Type header for FIND_PETS_BY_TAGS_SUCCESSFUL_OPERATION"));
                                                    let body = serde_xml_rs::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                                FindPetsByTagsResponse::InvalidTagValue
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(400).expect("Unable to turn 400 into a StatusCode");
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
            },

            // GetPetById - GET /pet/{petId}
            hyper::Method::GET if path.matched(paths::ID_PET_PETID) => {
                {
                    let authorization = match *(&context as &dyn Has<Option<Authorization>>).get() {
                        Some(ref authorization) => authorization,
                        None => return Ok(Response::builder()
                                                .status(StatusCode::FORBIDDEN)
                                                .body(Body::from("Unauthenticated"))
                                                .expect("Unable to create Authentication Forbidden response")),
                    };
                }

                // Path parameters
                let path: &str = uri.path();
                let path_params =
                    paths::REGEX_PET_PETID
                    .captures(path)
                    .unwrap_or_else(||
                        panic!("Path {} matched RE PET_PETID in set but failed match against \"{}\"", path, paths::REGEX_PET_PETID.as_str())
                    );

                let param_pet_id = match percent_encoding::percent_decode(path_params["petId"].as_bytes()).decode_utf8() {
                    Ok(param_pet_id) => match param_pet_id.parse::<i64>() {
                        Ok(param_pet_id) => param_pet_id,
                        Err(e) => return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Couldn't parse path parameter petId: {}", e)))
                                        .expect("Unable to create Bad Request response for invalid path parameter")),
                    },
                    Err(_) => return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Couldn't percent-decode path parameter as UTF-8: {}", &path_params["petId"])))
                                        .expect("Unable to create Bad Request response for invalid percent decode"))
                };

                                let result = api_impl.get_pet_by_id(
                                            param_pet_id,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        match result {
                                            Ok(rsp) => match rsp {
                                                GetPetByIdResponse::SuccessfulOperation
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/xml")
                                                            .expect("Unable to create Content-Type header for GET_PET_BY_ID_SUCCESSFUL_OPERATION"));
                                                    let body = serde_xml_rs::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                                GetPetByIdResponse::InvalidIDSupplied
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(400).expect("Unable to turn 400 into a StatusCode");
                                                },
                                                GetPetByIdResponse::PetNotFound
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(404).expect("Unable to turn 404 into a StatusCode");
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
            },

            // UpdatePet - PUT /pet
            hyper::Method::PUT if path.matched(paths::ID_PET) => {
                {
                    let authorization = match *(&context as &dyn Has<Option<Authorization>>).get() {
                        Some(ref authorization) => authorization,
                        None => return Ok(Response::builder()
                                                .status(StatusCode::FORBIDDEN)
                                                .body(Body::from("Unauthenticated"))
                                                .expect("Unable to create Authentication Forbidden response")),
                    };

                    // Authorization
                    if let Scopes::Some(ref scopes) = authorization.scopes {
                        let required_scopes: std::collections::BTreeSet<String> = vec![
                            "write:pets".to_string(), // modify pets in your account
                            "read:pets".to_string(), // read your pets
                        ].into_iter().collect();

                        if !required_scopes.is_subset(scopes) {
                            let missing_scopes = required_scopes.difference(scopes);
                            return Ok(Response::builder()
                                .status(StatusCode::FORBIDDEN)
                                .body(Body::from(missing_scopes.fold(
                                    "Insufficient authorization, missing scopes".to_string(),
                                    |s, scope| format!("{} {}", s, scope))
                                ))
                                .expect("Unable to create Authentication Insufficient response")
                            );
                        }
                    }
                }

                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_body: Option<models::Pet> = if !body.is_empty() {
                                    let deserializer = &mut serde_xml_rs::de::Deserializer::new_from_reader(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_body) => param_body,
                                        Err(e) => return Ok(Response::builder()
                                                        .status(StatusCode::BAD_REQUEST)
                                                        .body(Body::from(format!("Couldn't parse body parameter body - doesn't match schema: {}", e)))
                                                        .expect("Unable to create Bad Request response for invalid body parameter body due to schema")),
                                    }
                                } else {
                                    None
                                };
                                let param_body = match param_body {
                                    Some(param_body) => param_body,
                                    None => return Ok(Response::builder()
                                                        .status(StatusCode::BAD_REQUEST)
                                                        .body(Body::from("Missing required body parameter body"))
                                                        .expect("Unable to create Bad Request response for missing body parameter body")),
                                };

                                let result = api_impl.update_pet(
                                            param_body,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                UpdatePetResponse::InvalidIDSupplied
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(400).expect("Unable to turn 400 into a StatusCode");
                                                },
                                                UpdatePetResponse::PetNotFound
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(404).expect("Unable to turn 404 into a StatusCode");
                                                },
                                                UpdatePetResponse::ValidationException
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(405).expect("Unable to turn 405 into a StatusCode");
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter body: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter body")),
                        }
            },

            // UpdatePetWithForm - POST /pet/{petId}
            hyper::Method::POST if path.matched(paths::ID_PET_PETID) => {
                {
                    let authorization = match *(&context as &dyn Has<Option<Authorization>>).get() {
                        Some(ref authorization) => authorization,
                        None => return Ok(Response::builder()
                                                .status(StatusCode::FORBIDDEN)
                                                .body(Body::from("Unauthenticated"))
                                                .expect("Unable to create Authentication Forbidden response")),
                    };

                    // Authorization
                    if let Scopes::Some(ref scopes) = authorization.scopes {
                        let required_scopes: std::collections::BTreeSet<String> = vec![
                            "write:pets".to_string(), // modify pets in your account
                            "read:pets".to_string(), // read your pets
                        ].into_iter().collect();

                        if !required_scopes.is_subset(scopes) {
                            let missing_scopes = required_scopes.difference(scopes);
                            return Ok(Response::builder()
                                .status(StatusCode::FORBIDDEN)
                                .body(Body::from(missing_scopes.fold(
                                    "Insufficient authorization, missing scopes".to_string(),
                                    |s, scope| format!("{} {}", s, scope))
                                ))
                                .expect("Unable to create Authentication Insufficient response")
                            );
                        }
                    }
                }

                // Path parameters
                let path: &str = uri.path();
                let path_params =
                    paths::REGEX_PET_PETID
                    .captures(path)
                    .unwrap_or_else(||
                        panic!("Path {} matched RE PET_PETID in set but failed match against \"{}\"", path, paths::REGEX_PET_PETID.as_str())
                    );

                let param_pet_id = match percent_encoding::percent_decode(path_params["petId"].as_bytes()).decode_utf8() {
                    Ok(param_pet_id) => match param_pet_id.parse::<i64>() {
                        Ok(param_pet_id) => param_pet_id,
                        Err(e) => return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Couldn't parse path parameter petId: {}", e)))
                                        .expect("Unable to create Bad Request response for invalid path parameter")),
                    },
                    Err(_) => return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Couldn't percent-decode path parameter as UTF-8: {}", &path_params["petId"])))
                                        .expect("Unable to create Bad Request response for invalid percent decode"))
                };

                                // Form parameters
                                let param_name = Some("name_example".to_string());
                                let param_status = Some("status_example".to_string());

                                let result = api_impl.update_pet_with_form(
                                            param_pet_id,
                                            param_name,
                                            param_status,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        match result {
                                            Ok(rsp) => match rsp {
                                                UpdatePetWithFormResponse::InvalidInput
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(405).expect("Unable to turn 405 into a StatusCode");
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
            },

            // UploadFile - POST /pet/{petId}/uploadImage
            hyper::Method::POST if path.matched(paths::ID_PET_PETID_UPLOADIMAGE) => {
                {
                    let authorization = match *(&context as &dyn Has<Option<Authorization>>).get() {
                        Some(ref authorization) => authorization,
                        None => return Ok(Response::builder()
                                                .status(StatusCode::FORBIDDEN)
                                                .body(Body::from("Unauthenticated"))
                                                .expect("Unable to create Authentication Forbidden response")),
                    };

                    // Authorization
                    if let Scopes::Some(ref scopes) = authorization.scopes {
                        let required_scopes: std::collections::BTreeSet<String> = vec![
                            "write:pets".to_string(), // modify pets in your account
                            "read:pets".to_string(), // read your pets
                        ].into_iter().collect();

                        if !required_scopes.is_subset(scopes) {
                            let missing_scopes = required_scopes.difference(scopes);
                            return Ok(Response::builder()
                                .status(StatusCode::FORBIDDEN)
                                .body(Body::from(missing_scopes.fold(
                                    "Insufficient authorization, missing scopes".to_string(),
                                    |s, scope| format!("{} {}", s, scope))
                                ))
                                .expect("Unable to create Authentication Insufficient response")
                            );
                        }
                    }
                }

                let boundary = match swagger::multipart::form::boundary(&headers) {
                    Some(boundary) => boundary.to_string(),
                    None => return Ok(Response::builder()
                                .status(StatusCode::BAD_REQUEST)
                                .body(Body::from("Couldn't find valid multipart body".to_string()))
                                .expect("Unable to create Bad Request response for incorrect boundary")),
                };

                // Path parameters
                let path: &str = uri.path();
                let path_params =
                    paths::REGEX_PET_PETID_UPLOADIMAGE
                    .captures(path)
                    .unwrap_or_else(||
                        panic!("Path {} matched RE PET_PETID_UPLOADIMAGE in set but failed match against \"{}\"", path, paths::REGEX_PET_PETID_UPLOADIMAGE.as_str())
                    );

                let param_pet_id = match percent_encoding::percent_decode(path_params["petId"].as_bytes()).decode_utf8() {
                    Ok(param_pet_id) => match param_pet_id.parse::<i64>() {
                        Ok(param_pet_id) => param_pet_id,
                        Err(e) => return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Couldn't parse path parameter petId: {}", e)))
                                        .expect("Unable to create Bad Request response for invalid path parameter")),
                    },
                    Err(_) => return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Couldn't percent-decode path parameter as UTF-8: {}", &path_params["petId"])))
                                        .expect("Unable to create Bad Request response for invalid percent decode"))
                };

                // Form Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw();
                match result.await {
                            Ok(body) => {
                                use std::io::Read;

                                // Read Form Parameters from body
                                let mut entries = match Multipart::with_body(&body.to_vec()[..], boundary).save().temp() {
                                    SaveResult::Full(entries) => {
                                        entries
                                    },
                                    _ => {
                                        return Ok(Response::builder()
                                                        .status(StatusCode::BAD_REQUEST)
                                                        .body(Body::from("Unable to process all message parts".to_string()))
                                                        .expect("Unable to create Bad Request response due to failure to process all message"))
                                    },
                                };
                                let field_additional_metadata = entries.fields.remove("additional_metadata");
                                let param_additional_metadata = match field_additional_metadata {
                                    Some(field) => {
                                        let mut reader = field[0].data.readable().expect("Unable to read field for additional_metadata");
                                    Some({
                                        let mut data = String::new();
                                        reader.read_to_string(&mut data).expect("Reading saved String should never fail");
                                        let additional_metadata_model: String = match serde_json::from_str(&data) {
                                            Ok(model) => model,
                                            Err(e) => {
                                                return Ok(
                                                    Response::builder()
                                                    .status(StatusCode::BAD_REQUEST)
                                                    .body(Body::from(format!("additional_metadata data does not match API definition : {}", e)))
                                                    .expect("Unable to create Bad Request due to missing required form parameter additional_metadata"))
                                            }
                                        };
                                        additional_metadata_model
                                    })
                                    },
                                    None => {
                                            None
                                    }
                                };
                                let field_file = entries.fields.remove("file");
                                let param_file = match field_file {
                                    Some(field) => {
                                        let mut reader = field[0].data.readable().expect("Unable to read field for file");
                                    Some({
                                        let mut data = String::new();
                                        reader.read_to_string(&mut data).expect("Reading saved String should never fail");
                                        let file_model: swagger::ByteArray = match serde_json::from_str(&data) {
                                            Ok(model) => model,
                                            Err(e) => {
                                                return Ok(
                                                    Response::builder()
                                                    .status(StatusCode::BAD_REQUEST)
                                                    .body(Body::from(format!("file data does not match API definition : {}", e)))
                                                    .expect("Unable to create Bad Request due to missing required form parameter file"))
                                            }
                                        };
                                        file_model
                                    })
                                    },
                                    None => {
                                            None
                                    }
                                };
                                let result = api_impl.upload_file(
                                            param_pet_id,
                                            param_additional_metadata,
                                            param_file,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        match result {
                                            Ok(rsp) => match rsp {
                                                UploadFileResponse::SuccessfulOperation
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for UPLOAD_FILE_SUCCESSFUL_OPERATION"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from("Couldn't read multipart body".to_string()))
                                                .expect("Unable to create Bad Request response due to unable read multipart body")),
                        }
            },

            // DeleteOrder - DELETE /store/order/{orderId}
            hyper::Method::DELETE if path.matched(paths::ID_STORE_ORDER_ORDERID) => {
                // Path parameters
                let path: &str = uri.path();
                let path_params =
                    paths::REGEX_STORE_ORDER_ORDERID
                    .captures(path)
                    .unwrap_or_else(||
                        panic!("Path {} matched RE STORE_ORDER_ORDERID in set but failed match against \"{}\"", path, paths::REGEX_STORE_ORDER_ORDERID.as_str())
                    );

                let param_order_id = match percent_encoding::percent_decode(path_params["orderId"].as_bytes()).decode_utf8() {
                    Ok(param_order_id) => match param_order_id.parse::<i64>() {
                        Ok(param_order_id) => param_order_id,
                        Err(e) => return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Couldn't parse path parameter orderId: {}", e)))
                                        .expect("Unable to create Bad Request response for invalid path parameter")),
                    },
                    Err(_) => return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Couldn't percent-decode path parameter as UTF-8: {}", &path_params["orderId"])))
                                        .expect("Unable to create Bad Request response for invalid percent decode"))
                };

                                let result = api_impl.delete_order(
                                            param_order_id,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        match result {
                                            Ok(rsp) => match rsp {
                                                DeleteOrderResponse::InvalidIDSupplied
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(400).expect("Unable to turn 400 into a StatusCode");
                                                },
                                                DeleteOrderResponse::OrderNotFound
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(404).expect("Unable to turn 404 into a StatusCode");
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
            },

            // GetInventory - GET /store/inventory
            hyper::Method::GET if path.matched(paths::ID_STORE_INVENTORY) => {
                {
                    let authorization = match *(&context as &dyn Has<Option<Authorization>>).get() {
                        Some(ref authorization) => authorization,
                        None => return Ok(Response::builder()
                                                .status(StatusCode::FORBIDDEN)
                                                .body(Body::from("Unauthenticated"))
                                                .expect("Unable to create Authentication Forbidden response")),
                    };
                }

                                let result = api_impl.get_inventory(
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        match result {
                                            Ok(rsp) => match rsp {
                                                GetInventoryResponse::SuccessfulOperation
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/json")
                                                            .expect("Unable to create Content-Type header for GET_INVENTORY_SUCCESSFUL_OPERATION"));
                                                    let body = serde_json::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
            },

            // GetOrderById - GET /store/order/{orderId}
            hyper::Method::GET if path.matched(paths::ID_STORE_ORDER_ORDERID) => {
                // Path parameters
                let path: &str = uri.path();
                let path_params =
                    paths::REGEX_STORE_ORDER_ORDERID
                    .captures(path)
                    .unwrap_or_else(||
                        panic!("Path {} matched RE STORE_ORDER_ORDERID in set but failed match against \"{}\"", path, paths::REGEX_STORE_ORDER_ORDERID.as_str())
                    );

                let param_order_id = match percent_encoding::percent_decode(path_params["orderId"].as_bytes()).decode_utf8() {
                    Ok(param_order_id) => match param_order_id.parse::<i64>() {
                        Ok(param_order_id) => param_order_id,
                        Err(e) => return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Couldn't parse path parameter orderId: {}", e)))
                                        .expect("Unable to create Bad Request response for invalid path parameter")),
                    },
                    Err(_) => return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Couldn't percent-decode path parameter as UTF-8: {}", &path_params["orderId"])))
                                        .expect("Unable to create Bad Request response for invalid percent decode"))
                };

                                let result = api_impl.get_order_by_id(
                                            param_order_id,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        match result {
                                            Ok(rsp) => match rsp {
                                                GetOrderByIdResponse::SuccessfulOperation
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/xml")
                                                            .expect("Unable to create Content-Type header for GET_ORDER_BY_ID_SUCCESSFUL_OPERATION"));
                                                    let body = serde_xml_rs::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                                GetOrderByIdResponse::InvalidIDSupplied
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(400).expect("Unable to turn 400 into a StatusCode");
                                                },
                                                GetOrderByIdResponse::OrderNotFound
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(404).expect("Unable to turn 404 into a StatusCode");
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
            },

            // PlaceOrder - POST /store/order
            hyper::Method::POST if path.matched(paths::ID_STORE_ORDER) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_body: Option<models::Order> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_body) => param_body,
                                        Err(e) => return Ok(Response::builder()
                                                        .status(StatusCode::BAD_REQUEST)
                                                        .body(Body::from(format!("Couldn't parse body parameter body - doesn't match schema: {}", e)))
                                                        .expect("Unable to create Bad Request response for invalid body parameter body due to schema")),
                                    }
                                } else {
                                    None
                                };
                                let param_body = match param_body {
                                    Some(param_body) => param_body,
                                    None => return Ok(Response::builder()
                                                        .status(StatusCode::BAD_REQUEST)
                                                        .body(Body::from("Missing required body parameter body"))
                                                        .expect("Unable to create Bad Request response for missing body parameter body")),
                                };

                                let result = api_impl.place_order(
                                            param_body,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                PlaceOrderResponse::SuccessfulOperation
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/xml")
                                                            .expect("Unable to create Content-Type header for PLACE_ORDER_SUCCESSFUL_OPERATION"));
                                                    let body = serde_xml_rs::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                                PlaceOrderResponse::InvalidOrder
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(400).expect("Unable to turn 400 into a StatusCode");
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter body: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter body")),
                        }
            },

            // CreateUser - POST /user
            hyper::Method::POST if path.matched(paths::ID_USER) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_body: Option<models::User> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_body) => param_body,
                                        Err(e) => return Ok(Response::builder()
                                                        .status(StatusCode::BAD_REQUEST)
                                                        .body(Body::from(format!("Couldn't parse body parameter body - doesn't match schema: {}", e)))
                                                        .expect("Unable to create Bad Request response for invalid body parameter body due to schema")),
                                    }
                                } else {
                                    None
                                };
                                let param_body = match param_body {
                                    Some(param_body) => param_body,
                                    None => return Ok(Response::builder()
                                                        .status(StatusCode::BAD_REQUEST)
                                                        .body(Body::from("Missing required body parameter body"))
                                                        .expect("Unable to create Bad Request response for missing body parameter body")),
                                };

                                let result = api_impl.create_user(
                                            param_body,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                CreateUserResponse::SuccessfulOperation
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(0).expect("Unable to turn 0 into a StatusCode");
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter body: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter body")),
                        }
            },

            // CreateUsersWithArrayInput - POST /user/createWithArray
            hyper::Method::POST if path.matched(paths::ID_USER_CREATEWITHARRAY) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_body: Option<Vec<models::User>> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_body) => param_body,
                                        Err(e) => return Ok(Response::builder()
                                                        .status(StatusCode::BAD_REQUEST)
                                                        .body(Body::from(format!("Couldn't parse body parameter body - doesn't match schema: {}", e)))
                                                        .expect("Unable to create Bad Request response for invalid body parameter body due to schema")),
                                    }
                                } else {
                                    None
                                };
                                let param_body = match param_body {
                                    Some(param_body) => param_body,
                                    None => return Ok(Response::builder()
                                                        .status(StatusCode::BAD_REQUEST)
                                                        .body(Body::from("Missing required body parameter body"))
                                                        .expect("Unable to create Bad Request response for missing body parameter body")),
                                };

                                let result = api_impl.create_users_with_array_input(
                                            param_body.as_ref(),
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                CreateUsersWithArrayInputResponse::SuccessfulOperation
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(0).expect("Unable to turn 0 into a StatusCode");
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter body: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter body")),
                        }
            },

            // CreateUsersWithListInput - POST /user/createWithList
            hyper::Method::POST if path.matched(paths::ID_USER_CREATEWITHLIST) => {
                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_body: Option<Vec<models::User>> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_body) => param_body,
                                        Err(e) => return Ok(Response::builder()
                                                        .status(StatusCode::BAD_REQUEST)
                                                        .body(Body::from(format!("Couldn't parse body parameter body - doesn't match schema: {}", e)))
                                                        .expect("Unable to create Bad Request response for invalid body parameter body due to schema")),
                                    }
                                } else {
                                    None
                                };
                                let param_body = match param_body {
                                    Some(param_body) => param_body,
                                    None => return Ok(Response::builder()
                                                        .status(StatusCode::BAD_REQUEST)
                                                        .body(Body::from("Missing required body parameter body"))
                                                        .expect("Unable to create Bad Request response for missing body parameter body")),
                                };

                                let result = api_impl.create_users_with_list_input(
                                            param_body.as_ref(),
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                CreateUsersWithListInputResponse::SuccessfulOperation
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(0).expect("Unable to turn 0 into a StatusCode");
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter body: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter body")),
                        }
            },

            // DeleteUser - DELETE /user/{username}
            hyper::Method::DELETE if path.matched(paths::ID_USER_USERNAME) => {
                // Path parameters
                let path: &str = uri.path();
                let path_params =
                    paths::REGEX_USER_USERNAME
                    .captures(path)
                    .unwrap_or_else(||
                        panic!("Path {} matched RE USER_USERNAME in set but failed match against \"{}\"", path, paths::REGEX_USER_USERNAME.as_str())
                    );

                let param_username = match percent_encoding::percent_decode(path_params["username"].as_bytes()).decode_utf8() {
                    Ok(param_username) => match param_username.parse::<String>() {
                        Ok(param_username) => param_username,
                        Err(e) => return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Couldn't parse path parameter username: {}", e)))
                                        .expect("Unable to create Bad Request response for invalid path parameter")),
                    },
                    Err(_) => return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Couldn't percent-decode path parameter as UTF-8: {}", &path_params["username"])))
                                        .expect("Unable to create Bad Request response for invalid percent decode"))
                };

                                let result = api_impl.delete_user(
                                            param_username,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        match result {
                                            Ok(rsp) => match rsp {
                                                DeleteUserResponse::InvalidUsernameSupplied
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(400).expect("Unable to turn 400 into a StatusCode");
                                                },
                                                DeleteUserResponse::UserNotFound
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(404).expect("Unable to turn 404 into a StatusCode");
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
            },

            // GetUserByName - GET /user/{username}
            hyper::Method::GET if path.matched(paths::ID_USER_USERNAME) => {
                // Path parameters
                let path: &str = uri.path();
                let path_params =
                    paths::REGEX_USER_USERNAME
                    .captures(path)
                    .unwrap_or_else(||
                        panic!("Path {} matched RE USER_USERNAME in set but failed match against \"{}\"", path, paths::REGEX_USER_USERNAME.as_str())
                    );

                let param_username = match percent_encoding::percent_decode(path_params["username"].as_bytes()).decode_utf8() {
                    Ok(param_username) => match param_username.parse::<String>() {
                        Ok(param_username) => param_username,
                        Err(e) => return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Couldn't parse path parameter username: {}", e)))
                                        .expect("Unable to create Bad Request response for invalid path parameter")),
                    },
                    Err(_) => return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Couldn't percent-decode path parameter as UTF-8: {}", &path_params["username"])))
                                        .expect("Unable to create Bad Request response for invalid percent decode"))
                };

                                let result = api_impl.get_user_by_name(
                                            param_username,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        match result {
                                            Ok(rsp) => match rsp {
                                                GetUserByNameResponse::SuccessfulOperation
                                                    (body)
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/xml")
                                                            .expect("Unable to create Content-Type header for GET_USER_BY_NAME_SUCCESSFUL_OPERATION"));
                                                    let body = serde_xml_rs::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                                GetUserByNameResponse::InvalidUsernameSupplied
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(400).expect("Unable to turn 400 into a StatusCode");
                                                },
                                                GetUserByNameResponse::UserNotFound
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(404).expect("Unable to turn 404 into a StatusCode");
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
            },

            // LoginUser - GET /user/login
            hyper::Method::GET if path.matched(paths::ID_USER_LOGIN) => {
                // Query parameters (note that non-required or collection query parameters will ignore garbage values, rather than causing a 400 response)
                let query_params = form_urlencoded::parse(uri.query().unwrap_or_default().as_bytes()).collect::<Vec<_>>();
                let param_username = query_params.iter().filter(|e| e.0 == "username").map(|e| e.1.to_owned())
                    .next();
                let param_username = match param_username {
                    Some(param_username) => {
                        let param_username =
                            <String as std::str::FromStr>::from_str
                                (&param_username);
                        match param_username {
                            Ok(param_username) => Some(param_username),
                            Err(e) => return Ok(Response::builder()
                                .status(StatusCode::BAD_REQUEST)
                                .body(Body::from(format!("Couldn't parse query parameter username - doesn't match schema: {}", e)))
                                .expect("Unable to create Bad Request response for invalid query parameter username")),
                        }
                    },
                    None => None,
                };
                let param_username = match param_username {
                    Some(param_username) => param_username,
                    None => return Ok(Response::builder()
                        .status(StatusCode::BAD_REQUEST)
                        .body(Body::from("Missing required query parameter username"))
                        .expect("Unable to create Bad Request response for missing query parameter username")),
                };
                let param_password = query_params.iter().filter(|e| e.0 == "password").map(|e| e.1.to_owned())
                    .next();
                let param_password = match param_password {
                    Some(param_password) => {
                        let param_password =
                            <String as std::str::FromStr>::from_str
                                (&param_password);
                        match param_password {
                            Ok(param_password) => Some(param_password),
                            Err(e) => return Ok(Response::builder()
                                .status(StatusCode::BAD_REQUEST)
                                .body(Body::from(format!("Couldn't parse query parameter password - doesn't match schema: {}", e)))
                                .expect("Unable to create Bad Request response for invalid query parameter password")),
                        }
                    },
                    None => None,
                };
                let param_password = match param_password {
                    Some(param_password) => param_password,
                    None => return Ok(Response::builder()
                        .status(StatusCode::BAD_REQUEST)
                        .body(Body::from("Missing required query parameter password"))
                        .expect("Unable to create Bad Request response for missing query parameter password")),
                };

                                let result = api_impl.login_user(
                                            param_username,
                                            param_password,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        match result {
                                            Ok(rsp) => match rsp {
                                                LoginUserResponse::SuccessfulOperation
                                                    {
                                                        body,
                                                        x_rate_limit,
                                                        x_expires_after
                                                    }
                                                => {
                                                    if let Some(x_rate_limit) = x_rate_limit {
                                                    let x_rate_limit = match header::IntoHeaderValue(x_rate_limit).try_into() {
                                                        Ok(val) => val,
                                                        Err(e) => {
                                                            return Ok(Response::builder()
                                                                    .status(StatusCode::INTERNAL_SERVER_ERROR)
                                                                    .body(Body::from(format!("An internal server error occurred handling x_rate_limit header - {}", e)))
                                                                    .expect("Unable to create Internal Server Error for invalid response header"))
                                                        }
                                                    };

                                                    response.headers_mut().insert(
                                                        HeaderName::from_static("x-rate-limit"),
                                                        x_rate_limit
                                                    );
                                                    }
                                                    if let Some(x_expires_after) = x_expires_after {
                                                    let x_expires_after = match header::IntoHeaderValue(x_expires_after).try_into() {
                                                        Ok(val) => val,
                                                        Err(e) => {
                                                            return Ok(Response::builder()
                                                                    .status(StatusCode::INTERNAL_SERVER_ERROR)
                                                                    .body(Body::from(format!("An internal server error occurred handling x_expires_after header - {}", e)))
                                                                    .expect("Unable to create Internal Server Error for invalid response header"))
                                                        }
                                                    };

                                                    response.headers_mut().insert(
                                                        HeaderName::from_static("x-expires-after"),
                                                        x_expires_after
                                                    );
                                                    }
                                                    *response.status_mut() = StatusCode::from_u16(200).expect("Unable to turn 200 into a StatusCode");
                                                    response.headers_mut().insert(
                                                        CONTENT_TYPE,
                                                        HeaderValue::from_str("application/xml")
                                                            .expect("Unable to create Content-Type header for LOGIN_USER_SUCCESSFUL_OPERATION"));
                                                    let body = serde_xml_rs::to_string(&body).expect("impossible to fail to serialize");
                                                    *response.body_mut() = Body::from(body);
                                                },
                                                LoginUserResponse::InvalidUsername
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(400).expect("Unable to turn 400 into a StatusCode");
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
            },

            // LogoutUser - GET /user/logout
            hyper::Method::GET if path.matched(paths::ID_USER_LOGOUT) => {
                                let result = api_impl.logout_user(
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        match result {
                                            Ok(rsp) => match rsp {
                                                LogoutUserResponse::SuccessfulOperation
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(0).expect("Unable to turn 0 into a StatusCode");
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
            },

            // UpdateUser - PUT /user/{username}
            hyper::Method::PUT if path.matched(paths::ID_USER_USERNAME) => {
                // Path parameters
                let path: &str = uri.path();
                let path_params =
                    paths::REGEX_USER_USERNAME
                    .captures(path)
                    .unwrap_or_else(||
                        panic!("Path {} matched RE USER_USERNAME in set but failed match against \"{}\"", path, paths::REGEX_USER_USERNAME.as_str())
                    );

                let param_username = match percent_encoding::percent_decode(path_params["username"].as_bytes()).decode_utf8() {
                    Ok(param_username) => match param_username.parse::<String>() {
                        Ok(param_username) => param_username,
                        Err(e) => return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Couldn't parse path parameter username: {}", e)))
                                        .expect("Unable to create Bad Request response for invalid path parameter")),
                    },
                    Err(_) => return Ok(Response::builder()
                                        .status(StatusCode::BAD_REQUEST)
                                        .body(Body::from(format!("Couldn't percent-decode path parameter as UTF-8: {}", &path_params["username"])))
                                        .expect("Unable to create Bad Request response for invalid percent decode"))
                };

                // Body parameters (note that non-required body parameters will ignore garbage
                // values, rather than causing a 400 response). Produce warning header and logs for
                // any unused fields.
                let result = body.into_raw().await;
                match result {
                            Ok(body) => {
                                let mut unused_elements = Vec::new();
                                let param_body: Option<models::User> = if !body.is_empty() {
                                    let deserializer = &mut serde_json::Deserializer::from_slice(&*body);
                                    match serde_ignored::deserialize(deserializer, |path| {
                                            warn!("Ignoring unknown field in body: {}", path);
                                            unused_elements.push(path.to_string());
                                    }) {
                                        Ok(param_body) => param_body,
                                        Err(e) => return Ok(Response::builder()
                                                        .status(StatusCode::BAD_REQUEST)
                                                        .body(Body::from(format!("Couldn't parse body parameter body - doesn't match schema: {}", e)))
                                                        .expect("Unable to create Bad Request response for invalid body parameter body due to schema")),
                                    }
                                } else {
                                    None
                                };
                                let param_body = match param_body {
                                    Some(param_body) => param_body,
                                    None => return Ok(Response::builder()
                                                        .status(StatusCode::BAD_REQUEST)
                                                        .body(Body::from("Missing required body parameter body"))
                                                        .expect("Unable to create Bad Request response for missing body parameter body")),
                                };

                                let result = api_impl.update_user(
                                            param_username,
                                            param_body,
                                        &context
                                    ).await;
                                let mut response = Response::new(Body::empty());
                                response.headers_mut().insert(
                                            HeaderName::from_static("x-span-id"),
                                            HeaderValue::from_str((&context as &dyn Has<XSpanIdString>).get().0.clone().as_str())
                                                .expect("Unable to create X-Span-ID header value"));

                                        if !unused_elements.is_empty() {
                                            response.headers_mut().insert(
                                                HeaderName::from_static("warning"),
                                                HeaderValue::from_str(format!("Ignoring unknown fields in body: {:?}", unused_elements).as_str())
                                                    .expect("Unable to create Warning header value"));
                                        }

                                        match result {
                                            Ok(rsp) => match rsp {
                                                UpdateUserResponse::InvalidUserSupplied
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(400).expect("Unable to turn 400 into a StatusCode");
                                                },
                                                UpdateUserResponse::UserNotFound
                                                => {
                                                    *response.status_mut() = StatusCode::from_u16(404).expect("Unable to turn 404 into a StatusCode");
                                                },
                                            },
                                            Err(_) => {
                                                // Application code returned an error. This should not happen, as the implementation should
                                                // return a valid response.
                                                *response.status_mut() = StatusCode::INTERNAL_SERVER_ERROR;
                                                *response.body_mut() = Body::from("An internal error occurred");
                                            },
                                        }

                                        Ok(response)
                            },
                            Err(e) => Ok(Response::builder()
                                                .status(StatusCode::BAD_REQUEST)
                                                .body(Body::from(format!("Couldn't read body parameter body: {}", e)))
                                                .expect("Unable to create Bad Request response due to unable to read body parameter body")),
                        }
            },

            _ if path.matched(paths::ID_ACCURACY) => method_not_allowed(),
            _ if path.matched(paths::ID_BUCKETIZE) => method_not_allowed(),
            _ if path.matched(paths::ID_CORRELATION) => method_not_allowed(),
            _ if path.matched(paths::ID_CORRELATION_MATRIX) => method_not_allowed(),
            _ if path.matched(paths::ID_COVARIANCE) => method_not_allowed(),
            _ if path.matched(paths::ID_DATA_RANGE) => method_not_allowed(),
            _ if path.matched(paths::ID_DE_MEAN) => method_not_allowed(),
            _ if path.matched(paths::ID_DIFFERENCE_QUOTIENT) => method_not_allowed(),
            _ if path.matched(paths::ID_DISTANCE) => method_not_allowed(),
            _ if path.matched(paths::ID_DOT) => method_not_allowed(),
            _ if path.matched(paths::ID_ECHO) => method_not_allowed(),
            _ if path.matched(paths::ID_ESTIMATE_GRADIENT) => method_not_allowed(),
            _ if path.matched(paths::ID_F1_SCORE) => method_not_allowed(),
            _ if path.matched(paths::ID_GET_COLUMN) => method_not_allowed(),
            _ if path.matched(paths::ID_GET_ROW) => method_not_allowed(),
            _ if path.matched(paths::ID_IN_RANDOM_ORDER) => method_not_allowed(),
            _ if path.matched(paths::ID_INTERQUARTILE_RANGE) => method_not_allowed(),
            _ if path.matched(paths::ID_MAGNITUDE) => method_not_allowed(),
            _ if path.matched(paths::ID_MATRIX_ADD) => method_not_allowed(),
            _ if path.matched(paths::ID_MAXIMIZE_BATCH) => method_not_allowed(),
            _ if path.matched(paths::ID_MAXIMIZE_STOCHASTIC) => method_not_allowed(),
            _ if path.matched(paths::ID_MEAN) => method_not_allowed(),
            _ if path.matched(paths::ID_MEDIAN) => method_not_allowed(),
            _ if path.matched(paths::ID_MINIMIZE_BATCH) => method_not_allowed(),
            _ if path.matched(paths::ID_MINIMIZE_STOCHASTIC) => method_not_allowed(),
            _ if path.matched(paths::ID_MODE) => method_not_allowed(),
            _ if path.matched(paths::ID_PARTIAL_DIFFERENCE_QUOTIENT) => method_not_allowed(),
            _ if path.matched(paths::ID_PET) => method_not_allowed(),
            _ if path.matched(paths::ID_PET_FINDBYSTATUS) => method_not_allowed(),
            _ if path.matched(paths::ID_PET_FINDBYTAGS) => method_not_allowed(),
            _ if path.matched(paths::ID_PET_PETID) => method_not_allowed(),
            _ if path.matched(paths::ID_PET_PETID_UPLOADIMAGE) => method_not_allowed(),
            _ if path.matched(paths::ID_PRECISION) => method_not_allowed(),
            _ if path.matched(paths::ID_QUANTILE) => method_not_allowed(),
            _ if path.matched(paths::ID_RECALL) => method_not_allowed(),
            _ if path.matched(paths::ID_SCALAR_MULTIPLY) => method_not_allowed(),
            _ if path.matched(paths::ID_SHAPE) => method_not_allowed(),
            _ if path.matched(paths::ID_SPLIT_DATA) => method_not_allowed(),
            _ if path.matched(paths::ID_SQRT) => method_not_allowed(),
            _ if path.matched(paths::ID_SQUARED_DISTANCE) => method_not_allowed(),
            _ if path.matched(paths::ID_STANDARD_DEVIATION) => method_not_allowed(),
            _ if path.matched(paths::ID_STORE_INVENTORY) => method_not_allowed(),
            _ if path.matched(paths::ID_STORE_ORDER) => method_not_allowed(),
            _ if path.matched(paths::ID_STORE_ORDER_ORDERID) => method_not_allowed(),
            _ if path.matched(paths::ID_STRENGTH) => method_not_allowed(),
            _ if path.matched(paths::ID_SUM_OF_SQUARES) => method_not_allowed(),
            _ if path.matched(paths::ID_TRAIN_TEST_SPLIT) => method_not_allowed(),
            _ if path.matched(paths::ID_USER) => method_not_allowed(),
            _ if path.matched(paths::ID_USER_CREATEWITHARRAY) => method_not_allowed(),
            _ if path.matched(paths::ID_USER_CREATEWITHLIST) => method_not_allowed(),
            _ if path.matched(paths::ID_USER_LOGIN) => method_not_allowed(),
            _ if path.matched(paths::ID_USER_LOGOUT) => method_not_allowed(),
            _ if path.matched(paths::ID_USER_USERNAME) => method_not_allowed(),
            _ if path.matched(paths::ID_VARIANCE) => method_not_allowed(),
            _ if path.matched(paths::ID_VECTOR_ADD) => method_not_allowed(),
            _ if path.matched(paths::ID_VECTOR_MEAN) => method_not_allowed(),
            _ if path.matched(paths::ID_VECTOR_SUBTRACT) => method_not_allowed(),
            _ if path.matched(paths::ID_VECTOR_SUM) => method_not_allowed(),
            _ => Ok(Response::builder().status(StatusCode::NOT_FOUND)
                    .body(Body::empty())
                    .expect("Unable to create Not Found response"))
        }
    } Box::pin(run(self.api_impl.clone(), req)) }
}

/// Request parser for `Api`.
pub struct ApiRequestParser;
impl<T> RequestParser<T> for ApiRequestParser {
    fn parse_operation_id(request: &Request<T>) -> Option<&'static str> {
        let path = paths::GLOBAL_REGEX_SET.matches(request.uri().path());
        match *request.method() {
            // Accuracy - POST /accuracy
            hyper::Method::POST if path.matched(paths::ID_ACCURACY) => Some("Accuracy"),
            // Bucketize - POST /bucketize
            hyper::Method::POST if path.matched(paths::ID_BUCKETIZE) => Some("Bucketize"),
            // Correlation - POST /correlation
            hyper::Method::POST if path.matched(paths::ID_CORRELATION) => Some("Correlation"),
            // CorrelationMatrix - POST /correlation_matrix
            hyper::Method::POST if path.matched(paths::ID_CORRELATION_MATRIX) => Some("CorrelationMatrix"),
            // Covariance - POST /covariance
            hyper::Method::POST if path.matched(paths::ID_COVARIANCE) => Some("Covariance"),
            // DataRange - POST /data_range
            hyper::Method::POST if path.matched(paths::ID_DATA_RANGE) => Some("DataRange"),
            // DeMean - POST /de_mean
            hyper::Method::POST if path.matched(paths::ID_DE_MEAN) => Some("DeMean"),
            // DifferenceQuotient - POST /difference_quotient
            hyper::Method::POST if path.matched(paths::ID_DIFFERENCE_QUOTIENT) => Some("DifferenceQuotient"),
            // Distance - POST /distance
            hyper::Method::POST if path.matched(paths::ID_DISTANCE) => Some("Distance"),
            // Dot - POST /dot
            hyper::Method::POST if path.matched(paths::ID_DOT) => Some("Dot"),
            // Echo - POST /echo
            hyper::Method::POST if path.matched(paths::ID_ECHO) => Some("Echo"),
            // EstimateGradient - POST /estimate_gradient
            hyper::Method::POST if path.matched(paths::ID_ESTIMATE_GRADIENT) => Some("EstimateGradient"),
            // F1Score - POST /f1_score
            hyper::Method::POST if path.matched(paths::ID_F1_SCORE) => Some("F1Score"),
            // GetColumn - POST /get_column
            hyper::Method::POST if path.matched(paths::ID_GET_COLUMN) => Some("GetColumn"),
            // GetRow - POST /get_row
            hyper::Method::POST if path.matched(paths::ID_GET_ROW) => Some("GetRow"),
            // InRandomOrder - POST /in_random_order
            hyper::Method::POST if path.matched(paths::ID_IN_RANDOM_ORDER) => Some("InRandomOrder"),
            // InterquartileRange - POST /interquartile_range
            hyper::Method::POST if path.matched(paths::ID_INTERQUARTILE_RANGE) => Some("InterquartileRange"),
            // Magnitude - POST /magnitude
            hyper::Method::POST if path.matched(paths::ID_MAGNITUDE) => Some("Magnitude"),
            // MatrixAdd - POST /matrix_add
            hyper::Method::POST if path.matched(paths::ID_MATRIX_ADD) => Some("MatrixAdd"),
            // MaximizeBatch - POST /maximize_batch
            hyper::Method::POST if path.matched(paths::ID_MAXIMIZE_BATCH) => Some("MaximizeBatch"),
            // MaximizeStochastic - POST /maximize_stochastic
            hyper::Method::POST if path.matched(paths::ID_MAXIMIZE_STOCHASTIC) => Some("MaximizeStochastic"),
            // Mean - POST /mean
            hyper::Method::POST if path.matched(paths::ID_MEAN) => Some("Mean"),
            // Median - POST /median
            hyper::Method::POST if path.matched(paths::ID_MEDIAN) => Some("Median"),
            // MinimizeBatch - POST /minimize_batch
            hyper::Method::POST if path.matched(paths::ID_MINIMIZE_BATCH) => Some("MinimizeBatch"),
            // MinimizeStochastic - POST /minimize_stochastic
            hyper::Method::POST if path.matched(paths::ID_MINIMIZE_STOCHASTIC) => Some("MinimizeStochastic"),
            // Mode - POST /mode
            hyper::Method::POST if path.matched(paths::ID_MODE) => Some("Mode"),
            // PartialDifferenceQuotient - POST /partial_difference_quotient
            hyper::Method::POST if path.matched(paths::ID_PARTIAL_DIFFERENCE_QUOTIENT) => Some("PartialDifferenceQuotient"),
            // Precision - POST /precision
            hyper::Method::POST if path.matched(paths::ID_PRECISION) => Some("Precision"),
            // Quantile - POST /quantile
            hyper::Method::POST if path.matched(paths::ID_QUANTILE) => Some("Quantile"),
            // Recall - POST /recall
            hyper::Method::POST if path.matched(paths::ID_RECALL) => Some("Recall"),
            // ScalarMultiply - POST /scalar_multiply
            hyper::Method::POST if path.matched(paths::ID_SCALAR_MULTIPLY) => Some("ScalarMultiply"),
            // Shape - POST /shape
            hyper::Method::POST if path.matched(paths::ID_SHAPE) => Some("Shape"),
            // SplitData - POST /split_data
            hyper::Method::POST if path.matched(paths::ID_SPLIT_DATA) => Some("SplitData"),
            // Sqrt - POST /sqrt
            hyper::Method::POST if path.matched(paths::ID_SQRT) => Some("Sqrt"),
            // SquaredDistance - POST /squared_distance
            hyper::Method::POST if path.matched(paths::ID_SQUARED_DISTANCE) => Some("SquaredDistance"),
            // StandardDeviation - POST /standard_deviation
            hyper::Method::POST if path.matched(paths::ID_STANDARD_DEVIATION) => Some("StandardDeviation"),
            // Strength - POST /strength
            hyper::Method::POST if path.matched(paths::ID_STRENGTH) => Some("Strength"),
            // SumOfSquares - POST /sum_of_squares
            hyper::Method::POST if path.matched(paths::ID_SUM_OF_SQUARES) => Some("SumOfSquares"),
            // TrainTestSplit - POST /train_test_split
            hyper::Method::POST if path.matched(paths::ID_TRAIN_TEST_SPLIT) => Some("TrainTestSplit"),
            // Variance - POST /variance
            hyper::Method::POST if path.matched(paths::ID_VARIANCE) => Some("Variance"),
            // VectorAdd - POST /vector_add
            hyper::Method::POST if path.matched(paths::ID_VECTOR_ADD) => Some("VectorAdd"),
            // VectorMean - POST /vector_mean
            hyper::Method::POST if path.matched(paths::ID_VECTOR_MEAN) => Some("VectorMean"),
            // VectorSubtract - POST /vector_subtract
            hyper::Method::POST if path.matched(paths::ID_VECTOR_SUBTRACT) => Some("VectorSubtract"),
            // VectorSum - POST /vector_sum
            hyper::Method::POST if path.matched(paths::ID_VECTOR_SUM) => Some("VectorSum"),
            // AddPet - POST /pet
            hyper::Method::POST if path.matched(paths::ID_PET) => Some("AddPet"),
            // DeletePet - DELETE /pet/{petId}
            hyper::Method::DELETE if path.matched(paths::ID_PET_PETID) => Some("DeletePet"),
            // FindPetsByStatus - GET /pet/findByStatus
            hyper::Method::GET if path.matched(paths::ID_PET_FINDBYSTATUS) => Some("FindPetsByStatus"),
            // FindPetsByTags - GET /pet/findByTags
            hyper::Method::GET if path.matched(paths::ID_PET_FINDBYTAGS) => Some("FindPetsByTags"),
            // GetPetById - GET /pet/{petId}
            hyper::Method::GET if path.matched(paths::ID_PET_PETID) => Some("GetPetById"),
            // UpdatePet - PUT /pet
            hyper::Method::PUT if path.matched(paths::ID_PET) => Some("UpdatePet"),
            // UpdatePetWithForm - POST /pet/{petId}
            hyper::Method::POST if path.matched(paths::ID_PET_PETID) => Some("UpdatePetWithForm"),
            // UploadFile - POST /pet/{petId}/uploadImage
            hyper::Method::POST if path.matched(paths::ID_PET_PETID_UPLOADIMAGE) => Some("UploadFile"),
            // DeleteOrder - DELETE /store/order/{orderId}
            hyper::Method::DELETE if path.matched(paths::ID_STORE_ORDER_ORDERID) => Some("DeleteOrder"),
            // GetInventory - GET /store/inventory
            hyper::Method::GET if path.matched(paths::ID_STORE_INVENTORY) => Some("GetInventory"),
            // GetOrderById - GET /store/order/{orderId}
            hyper::Method::GET if path.matched(paths::ID_STORE_ORDER_ORDERID) => Some("GetOrderById"),
            // PlaceOrder - POST /store/order
            hyper::Method::POST if path.matched(paths::ID_STORE_ORDER) => Some("PlaceOrder"),
            // CreateUser - POST /user
            hyper::Method::POST if path.matched(paths::ID_USER) => Some("CreateUser"),
            // CreateUsersWithArrayInput - POST /user/createWithArray
            hyper::Method::POST if path.matched(paths::ID_USER_CREATEWITHARRAY) => Some("CreateUsersWithArrayInput"),
            // CreateUsersWithListInput - POST /user/createWithList
            hyper::Method::POST if path.matched(paths::ID_USER_CREATEWITHLIST) => Some("CreateUsersWithListInput"),
            // DeleteUser - DELETE /user/{username}
            hyper::Method::DELETE if path.matched(paths::ID_USER_USERNAME) => Some("DeleteUser"),
            // GetUserByName - GET /user/{username}
            hyper::Method::GET if path.matched(paths::ID_USER_USERNAME) => Some("GetUserByName"),
            // LoginUser - GET /user/login
            hyper::Method::GET if path.matched(paths::ID_USER_LOGIN) => Some("LoginUser"),
            // LogoutUser - GET /user/logout
            hyper::Method::GET if path.matched(paths::ID_USER_LOGOUT) => Some("LogoutUser"),
            // UpdateUser - PUT /user/{username}
            hyper::Method::PUT if path.matched(paths::ID_USER_USERNAME) => Some("UpdateUser"),
            _ => None,
        }
    }
}
