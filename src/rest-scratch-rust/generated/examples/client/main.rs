#![allow(missing_docs, unused_variables, trivial_casts)]


#[allow(unused_imports)]
use futures::{future, Stream, stream};
#[allow(unused_imports)]
use openapi_client::{Api, ApiNoContext, Client, ContextWrapperExt, models,
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
use clap::{App, Arg};

#[allow(unused_imports)]
use log::info;

// swagger::Has may be unused if there are no examples
#[allow(unused_imports)]
use swagger::{AuthData, ContextBuilder, EmptyContext, Has, Push, XSpanIdString};

type ClientContext = swagger::make_context_ty!(ContextBuilder, EmptyContext, Option<AuthData>, XSpanIdString);

// rt may be unused if there are no examples
#[allow(unused_mut)]
fn main() {
    env_logger::init();

    let matches = App::new("client")
        .arg(Arg::with_name("operation")
            .help("Sets the operation to run")
            .possible_values(&[
                "Accuracy",
                "Bucketize",
                "Correlation",
                "CorrelationMatrix",
                "Covariance",
                "DataRange",
                "DeMean",
                "DifferenceQuotient",
                "Distance",
                "Dot",
                "Echo",
                "EstimateGradient",
                "F1Score",
                "GetColumn",
                "GetRow",
                "InRandomOrder",
                "InterquartileRange",
                "Magnitude",
                "MatrixAdd",
                "MaximizeBatch",
                "MaximizeStochastic",
                "Mean",
                "Median",
                "MinimizeBatch",
                "MinimizeStochastic",
                "Mode",
                "PartialDifferenceQuotient",
                "Precision",
                "Quantile",
                "Recall",
                "ScalarMultiply",
                "Shape",
                "SplitData",
                "Sqrt",
                "SquaredDistance",
                "StandardDeviation",
                "Strength",
                "SumOfSquares",
                "TrainTestSplit",
                "Variance",
                "VectorAdd",
                "VectorMean",
                "VectorSubtract",
                "VectorSum",
                "DeletePet",
                "FindPetsByStatus",
                "FindPetsByTags",
                "GetPetById",
                "UpdatePetWithForm",
                "UploadFile",
                "DeleteOrder",
                "GetInventory",
                "GetOrderById",
                "CreateUsersWithArrayInput",
                "CreateUsersWithListInput",
                "DeleteUser",
                "GetUserByName",
                "LoginUser",
                "LogoutUser",
            ])
            .required(true)
            .index(1))
        .arg(Arg::with_name("https")
            .long("https")
            .help("Whether to use HTTPS or not"))
        .arg(Arg::with_name("host")
            .long("host")
            .takes_value(true)
            .default_value("localhost")
            .help("Hostname to contact"))
        .arg(Arg::with_name("port")
            .long("port")
            .takes_value(true)
            .default_value("8080")
            .help("Port to contact"))
        .get_matches();

    let is_https = matches.is_present("https");
    let base_url = format!("{}://{}:{}",
                           if is_https { "https" } else { "http" },
                           matches.value_of("host").unwrap(),
                           matches.value_of("port").unwrap());

    let context: ClientContext =
        swagger::make_context!(ContextBuilder, EmptyContext, None as Option<AuthData>, XSpanIdString::default());

    let mut client : Box<dyn ApiNoContext<ClientContext>> = if matches.is_present("https") {
        // Using Simple HTTPS
        let client = Box::new(Client::try_new_https(&base_url)
            .expect("Failed to create HTTPS client"));
        Box::new(client.with_context(context))
    } else {
        // Using HTTP
        let client = Box::new(Client::try_new_http(
            &base_url)
            .expect("Failed to create HTTP client"));
        Box::new(client.with_context(context))
    };

    let mut rt = tokio::runtime::Runtime::new().unwrap();

    match matches.value_of("operation") {
        Some("Accuracy") => {
            let result = rt.block_on(client.accuracy(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("Bucketize") => {
            let result = rt.block_on(client.bucketize(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("Correlation") => {
            let result = rt.block_on(client.correlation(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("CorrelationMatrix") => {
            let result = rt.block_on(client.correlation_matrix(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("Covariance") => {
            let result = rt.block_on(client.covariance(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("DataRange") => {
            let result = rt.block_on(client.data_range(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("DeMean") => {
            let result = rt.block_on(client.de_mean(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("DifferenceQuotient") => {
            let result = rt.block_on(client.difference_quotient(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("Distance") => {
            let result = rt.block_on(client.distance(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("Dot") => {
            let result = rt.block_on(client.dot(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("Echo") => {
            let result = rt.block_on(client.echo(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("EstimateGradient") => {
            let result = rt.block_on(client.estimate_gradient(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("F1Score") => {
            let result = rt.block_on(client.f1_score(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("GetColumn") => {
            let result = rt.block_on(client.get_column(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("GetRow") => {
            let result = rt.block_on(client.get_row(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("InRandomOrder") => {
            let result = rt.block_on(client.in_random_order(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("InterquartileRange") => {
            let result = rt.block_on(client.interquartile_range(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("Magnitude") => {
            let result = rt.block_on(client.magnitude(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("MatrixAdd") => {
            let result = rt.block_on(client.matrix_add(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("MaximizeBatch") => {
            let result = rt.block_on(client.maximize_batch(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("MaximizeStochastic") => {
            let result = rt.block_on(client.maximize_stochastic(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("Mean") => {
            let result = rt.block_on(client.mean(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("Median") => {
            let result = rt.block_on(client.median(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("MinimizeBatch") => {
            let result = rt.block_on(client.minimize_batch(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("MinimizeStochastic") => {
            let result = rt.block_on(client.minimize_stochastic(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("Mode") => {
            let result = rt.block_on(client.mode(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("PartialDifferenceQuotient") => {
            let result = rt.block_on(client.partial_difference_quotient(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("Precision") => {
            let result = rt.block_on(client.precision(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("Quantile") => {
            let result = rt.block_on(client.quantile(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("Recall") => {
            let result = rt.block_on(client.recall(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("ScalarMultiply") => {
            let result = rt.block_on(client.scalar_multiply(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("Shape") => {
            let result = rt.block_on(client.shape(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("SplitData") => {
            let result = rt.block_on(client.split_data(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("Sqrt") => {
            let result = rt.block_on(client.sqrt(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("SquaredDistance") => {
            let result = rt.block_on(client.squared_distance(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("StandardDeviation") => {
            let result = rt.block_on(client.standard_deviation(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("Strength") => {
            let result = rt.block_on(client.strength(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("SumOfSquares") => {
            let result = rt.block_on(client.sum_of_squares(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("TrainTestSplit") => {
            let result = rt.block_on(client.train_test_split(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("Variance") => {
            let result = rt.block_on(client.variance(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("VectorAdd") => {
            let result = rt.block_on(client.vector_add(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("VectorMean") => {
            let result = rt.block_on(client.vector_mean(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("VectorSubtract") => {
            let result = rt.block_on(client.vector_subtract(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("VectorSum") => {
            let result = rt.block_on(client.vector_sum(
                  None
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        /* Disabled because there's no example.
        Some("AddPet") => {
            let result = rt.block_on(client.add_pet(
                  ???
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        */
        Some("DeletePet") => {
            let result = rt.block_on(client.delete_pet(
                  789,
                  Some("api_key_example".to_string())
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("FindPetsByStatus") => {
            let result = rt.block_on(client.find_pets_by_status(
                  &Vec::new()
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("FindPetsByTags") => {
            let result = rt.block_on(client.find_pets_by_tags(
                  &Vec::new()
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("GetPetById") => {
            let result = rt.block_on(client.get_pet_by_id(
                  789
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        /* Disabled because there's no example.
        Some("UpdatePet") => {
            let result = rt.block_on(client.update_pet(
                  ???
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        */
        Some("UpdatePetWithForm") => {
            let result = rt.block_on(client.update_pet_with_form(
                  789,
                  Some("name_example".to_string()),
                  Some("status_example".to_string())
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("UploadFile") => {
            let result = rt.block_on(client.upload_file(
                  789,
                  Some("additional_metadata_example".to_string()),
                  Some(swagger::ByteArray(Vec::from("BINARY_DATA_HERE")))
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("DeleteOrder") => {
            let result = rt.block_on(client.delete_order(
                  789
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("GetInventory") => {
            let result = rt.block_on(client.get_inventory(
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("GetOrderById") => {
            let result = rt.block_on(client.get_order_by_id(
                  789
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        /* Disabled because there's no example.
        Some("PlaceOrder") => {
            let result = rt.block_on(client.place_order(
                  ???
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        */
        /* Disabled because there's no example.
        Some("CreateUser") => {
            let result = rt.block_on(client.create_user(
                  ???
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        */
        Some("CreateUsersWithArrayInput") => {
            let result = rt.block_on(client.create_users_with_array_input(
                  &Vec::new()
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("CreateUsersWithListInput") => {
            let result = rt.block_on(client.create_users_with_list_input(
                  &Vec::new()
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("DeleteUser") => {
            let result = rt.block_on(client.delete_user(
                  "username_example".to_string()
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("GetUserByName") => {
            let result = rt.block_on(client.get_user_by_name(
                  "username_example".to_string()
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("LoginUser") => {
            let result = rt.block_on(client.login_user(
                  "username_example".to_string(),
                  "password_example".to_string()
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        Some("LogoutUser") => {
            let result = rt.block_on(client.logout_user(
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        /* Disabled because there's no example.
        Some("UpdateUser") => {
            let result = rt.block_on(client.update_user(
                  "username_example".to_string(),
                  ???
            ));
            info!("{:?} (X-Span-ID: {:?})", result, (client.context() as &dyn Has<XSpanIdString>).get().clone());
        },
        */
        _ => {
            panic!("Invalid operation provided")
        }
    }
}
