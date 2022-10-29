# math_api

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
**accuracy**](math_api.md#accuracy) | **POST** /accuracy | 
**bucketize**](math_api.md#bucketize) | **POST** /bucketize | 
**correlation**](math_api.md#correlation) | **POST** /correlation | 
**correlation_matrix**](math_api.md#correlation_matrix) | **POST** /correlation_matrix | 
**covariance**](math_api.md#covariance) | **POST** /covariance | 
**data_range**](math_api.md#data_range) | **POST** /data_range | 
**de_mean**](math_api.md#de_mean) | **POST** /de_mean | 
**difference_quotient**](math_api.md#difference_quotient) | **POST** /difference_quotient | 
**distance**](math_api.md#distance) | **POST** /distance | 
**dot**](math_api.md#dot) | **POST** /dot | 
**echo**](math_api.md#echo) | **POST** /echo | 
**estimate_gradient**](math_api.md#estimate_gradient) | **POST** /estimate_gradient | 
**f1_score**](math_api.md#f1_score) | **POST** /f1_score | 
**get_column**](math_api.md#get_column) | **POST** /get_column | 
**get_row**](math_api.md#get_row) | **POST** /get_row | 
**in_random_order**](math_api.md#in_random_order) | **POST** /in_random_order | 
**interquartile_range**](math_api.md#interquartile_range) | **POST** /interquartile_range | 
**magnitude**](math_api.md#magnitude) | **POST** /magnitude | 
**matrix_add**](math_api.md#matrix_add) | **POST** /matrix_add | 
**maximize_batch**](math_api.md#maximize_batch) | **POST** /maximize_batch | 
**maximize_stochastic**](math_api.md#maximize_stochastic) | **POST** /maximize_stochastic | 
**mean**](math_api.md#mean) | **POST** /mean | 
**median**](math_api.md#median) | **POST** /median | 
**minimize_batch**](math_api.md#minimize_batch) | **POST** /minimize_batch | 
**minimize_stochastic**](math_api.md#minimize_stochastic) | **POST** /minimize_stochastic | 
**mode**](math_api.md#mode) | **POST** /mode | 
**partial_difference_quotient**](math_api.md#partial_difference_quotient) | **POST** /partial_difference_quotient | 
**precision**](math_api.md#precision) | **POST** /precision | 
**quantile**](math_api.md#quantile) | **POST** /quantile | 
**recall**](math_api.md#recall) | **POST** /recall | 
**scalar_multiply**](math_api.md#scalar_multiply) | **POST** /scalar_multiply | 
**shape**](math_api.md#shape) | **POST** /shape | 
**split_data**](math_api.md#split_data) | **POST** /split_data | 
**sqrt**](math_api.md#sqrt) | **POST** /sqrt | 
**squared_distance**](math_api.md#squared_distance) | **POST** /squared_distance | 
**standard_deviation**](math_api.md#standard_deviation) | **POST** /standard_deviation | 
**strength**](math_api.md#strength) | **POST** /strength | 
**sum_of_squares**](math_api.md#sum_of_squares) | **POST** /sum_of_squares | 
**train_test_split**](math_api.md#train_test_split) | **POST** /train_test_split | 
**variance**](math_api.md#variance) | **POST** /variance | 
**vector_add**](math_api.md#vector_add) | **POST** /vector_add | 
**vector_mean**](math_api.md#vector_mean) | **POST** /vector_mean | 
**vector_subtract**](math_api.md#vector_subtract) | **POST** /vector_subtract | 
**vector_sum**](math_api.md#vector_sum) | **POST** /vector_sum | 


# **accuracy**
> f64 accuracy(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accuracy_input** | [**AccuracyInput**](AccuracyInput.md)|  | 

### Return type

[**f64**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bucketize**
> models::BucketizeOutput bucketize(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bucketize_input** | [**BucketizeInput**](BucketizeInput.md)|  | 

### Return type

[**models::BucketizeOutput**](bucketize-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **correlation**
> models::CorrelationOutput correlation(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **correlation_input** | [**CorrelationInput**](CorrelationInput.md)|  | 

### Return type

[**models::CorrelationOutput**](correlation-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **correlation_matrix**
> models::CorrelationMatrixOutput correlation_matrix(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **correlation_matrix_input** | [**CorrelationMatrixInput**](CorrelationMatrixInput.md)|  | 

### Return type

[**models::CorrelationMatrixOutput**](correlation_matrix-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **covariance**
> models::CovarianceOutput covariance(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **covariance_input** | [**CovarianceInput**](CovarianceInput.md)|  | 

### Return type

[**models::CovarianceOutput**](covariance-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **data_range**
> models::DataRangeOutput data_range(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_range_input** | [**DataRangeInput**](DataRangeInput.md)|  | 

### Return type

[**models::DataRangeOutput**](data_range-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **de_mean**
> models::DeMeanOutput de_mean(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **de_mean_input** | [**DeMeanInput**](DeMeanInput.md)|  | 

### Return type

[**models::DeMeanOutput**](de_mean-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **difference_quotient**
> models::DifferenceQuotientOutput difference_quotient(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **difference_quotient_input** | [**DifferenceQuotientInput**](DifferenceQuotientInput.md)|  | 

### Return type

[**models::DifferenceQuotientOutput**](difference_quotient-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **distance**
> models::DistanceOutput distance(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **distance_input** | [**DistanceInput**](DistanceInput.md)|  | 

### Return type

[**models::DistanceOutput**](distance-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dot**
> models::DotOutput dot(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dot_input** | [**DotInput**](DotInput.md)|  | 

### Return type

[**models::DotOutput**](dot-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **echo**
> serde_json::Value echo(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 

### Return type

[**serde_json::Value**](object.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **estimate_gradient**
> models::EstimateGradientOutput estimate_gradient(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **estimate_gradient_input** | [**EstimateGradientInput**](EstimateGradientInput.md)|  | 

### Return type

[**models::EstimateGradientOutput**](estimate_gradient-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **f1_score**
> f64 f1_score(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **f1_score_input** | [**F1ScoreInput**](F1ScoreInput.md)|  | 

### Return type

[**f64**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_column**
> models::GetColumnOutput get_column(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_column_input** | [**GetColumnInput**](GetColumnInput.md)|  | 

### Return type

[**models::GetColumnOutput**](get_column-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_row**
> models::GetRowOutput get_row(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_row_input** | [**GetRowInput**](GetRowInput.md)|  | 

### Return type

[**models::GetRowOutput**](get_row-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **in_random_order**
> Vec<f64> in_random_order(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **in_random_order_input** | [**InRandomOrderInput**](InRandomOrderInput.md)|  | 

### Return type

[**Vec<f64>**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **interquartile_range**
> f64 interquartile_range(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **interquartile_range_input** | [**InterquartileRangeInput**](InterquartileRangeInput.md)|  | 

### Return type

[**f64**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **magnitude**
> f64 magnitude(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **magnitude_input** | [**MagnitudeInput**](MagnitudeInput.md)|  | 

### Return type

[**f64**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matrix_add**
> Vec<Vec<f64>> matrix_add(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **matrix_add_input** | [**MatrixAddInput**](MatrixAddInput.md)|  | 

### Return type

[**Vec<Vec<f64>>**](array.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maximize_batch**
> models::MaximizeBatchOutput maximize_batch(optional)


use gradient descent to find theta that minimizes target function

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maximize_batch_input** | [**MaximizeBatchInput**](MaximizeBatchInput.md)|  | 

### Return type

[**models::MaximizeBatchOutput**](maximize_batch-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **maximize_stochastic**
> models::MaximizeStochasticOutput maximize_stochastic(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maximize_stochastic_input** | [**MaximizeStochasticInput**](MaximizeStochasticInput.md)|  | 

### Return type

[**models::MaximizeStochasticOutput**](maximize_stochastic-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mean**
> f64 mean(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mean_input** | [**MeanInput**](MeanInput.md)|  | 

### Return type

[**f64**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **median**
> f64 median(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **median_input** | [**MedianInput**](MedianInput.md)|  | 

### Return type

[**f64**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **minimize_batch**
> models::MinimizeBatchOutput minimize_batch(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minimize_batch_input** | [**MinimizeBatchInput**](MinimizeBatchInput.md)|  | 

### Return type

[**models::MinimizeBatchOutput**](minimize_batch-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **minimize_stochastic**
> models::MinimizeStochasticOutput minimize_stochastic(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **minimize_stochastic_input** | [**MinimizeStochasticInput**](MinimizeStochasticInput.md)|  | 

### Return type

[**models::MinimizeStochasticOutput**](minimize_stochastic-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **mode**
> Vec<f64> mode(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mode_input** | [**ModeInput**](ModeInput.md)|  | 

### Return type

[**Vec<f64>**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **partial_difference_quotient**
> models::PartialDifferenceQuotientOutput partial_difference_quotient(optional)


add h to just the i-th element of v

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **partial_difference_quotient_input** | [**PartialDifferenceQuotientInput**](PartialDifferenceQuotientInput.md)|  | 

### Return type

[**models::PartialDifferenceQuotientOutput**](partial_difference_quotient-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **precision**
> f64 precision(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **precision_input** | [**PrecisionInput**](PrecisionInput.md)|  | 

### Return type

[**f64**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **quantile**
> f64 quantile(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quantile_input** | [**QuantileInput**](QuantileInput.md)|  | 

### Return type

[**f64**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recall**
> f64 recall(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **recall_input** | [**RecallInput**](RecallInput.md)|  | 

### Return type

[**f64**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **scalar_multiply**
> Vec<Vec<f64>> scalar_multiply(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scalar_multiply_input** | [**ScalarMultiplyInput**](ScalarMultiplyInput.md)|  | 

### Return type

[**Vec<Vec<f64>>**](array.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shape**
> models::ShapeOutput shape(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shape_input** | [**ShapeInput**](ShapeInput.md)|  | 

### Return type

[**models::ShapeOutput**](shape-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **split_data**
> models::SplitDataOutput split_data(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **split_data_input** | [**SplitDataInput**](SplitDataInput.md)|  | 

### Return type

[**models::SplitDataOutput**](split_data-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sqrt**
> models::SqrtOutput sqrt(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sqrt_input** | [**SqrtInput**](SqrtInput.md)|  | 

### Return type

[**models::SqrtOutput**](sqrt-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **squared_distance**
> Vec<f64> squared_distance(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **squared_distance_input** | [**SquaredDistanceInput**](SquaredDistanceInput.md)|  | 

### Return type

[**Vec<f64>**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **standard_deviation**
> f64 standard_deviation(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **standard_deviation_input** | [**StandardDeviationInput**](StandardDeviationInput.md)|  | 

### Return type

[**f64**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **strength**
> models::StrengthOutput strength(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **strength_input** | [**StrengthInput**](StrengthInput.md)|  | 

### Return type

[**models::StrengthOutput**](strength-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sum_of_squares**
> f64 sum_of_squares(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sum_of_squares_input** | [**SumOfSquaresInput**](SumOfSquaresInput.md)|  | 

### Return type

[**f64**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **train_test_split**
> models::TrainTestSplitOutput train_test_split(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **train_test_split_input** | [**TrainTestSplitInput**](TrainTestSplitInput.md)|  | 

### Return type

[**models::TrainTestSplitOutput**](train_test_split-output.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **variance**
> f64 variance(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **variance_input** | [**VarianceInput**](VarianceInput.md)|  | 

### Return type

[**f64**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vector_add**
> Vec<f64> vector_add(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vector_add_input** | [**VectorAddInput**](VectorAddInput.md)|  | 

### Return type

[**Vec<f64>**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vector_mean**
> Vec<f64> vector_mean(optional)


compute the vector whose i-th element is the mean of the i-th elements of the input vectors

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vector_mean_input** | [**VectorMeanInput**](VectorMeanInput.md)|  | 

### Return type

[**Vec<f64>**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vector_subtract**
> Vec<f64> vector_subtract(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vector_subtract_input** | [**VectorSubtractInput**](VectorSubtractInput.md)|  | 

### Return type

[**Vec<f64>**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vector_sum**
> Vec<f64> vector_sum(optional)


Description of the endpoint

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **optional** | **map[string]interface{}** | optional parameters | nil if no parameters

### Optional Parameters
Optional parameters are passed through a map[string]interface{}.

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vector_sum_input** | [**VectorSumInput**](VectorSumInput.md)|  | 

### Return type

[**Vec<f64>**](number.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

