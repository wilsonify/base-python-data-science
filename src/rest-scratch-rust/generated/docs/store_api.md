# store_api

All URIs are relative to */v2*

Method | HTTP request | Description
------------- | ------------- | -------------
**delete_order**](store_api.md#delete_order) | **DELETE** /store/order/{orderId} | Delete purchase order by ID
**get_inventory**](store_api.md#get_inventory) | **GET** /store/inventory | Returns pet inventories by status
**get_order_by_id**](store_api.md#get_order_by_id) | **GET** /store/order/{orderId} | Find purchase order by ID
**place_order**](store_api.md#place_order) | **POST** /store/order | Place an order for a pet


# **delete_order**
> delete_order(order_id)
Delete purchase order by ID

For valid response try integer IDs with positive integer value.         Negative or non-integer values will generate API errors

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
  **order_id** | **i64**| ID of the order that needs to be deleted | 

### Return type

 (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory**
> std::collections::HashMap<String, i32> get_inventory(ctx, )
Returns pet inventories by status

Returns a map of status codes to quantities

### Required Parameters
This endpoint does not need any parameter.

### Return type

[**std::collections::HashMap<String, i32>**](integer.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_by_id**
> models::Order get_order_by_id(order_id)
Find purchase order by ID

For valid response try integer IDs with value >= 1 and <= 10.         Other values will generated exceptions

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
  **order_id** | **i64**| ID of pet that needs to be fetched | 

### Return type

[**models::Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **place_order**
> models::Order place_order(body)
Place an order for a pet

### Required Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
  **body** | [**Order**](Order.md)| order placed for purchasing the pet | 

### Return type

[**models::Order**](Order.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

