# openapi_client.EMILProductsApi

All URIs are relative to *https://api.ercot.com/api/public-reports*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_list_for_products**](EMILProductsApi.md#get_list_for_products) | **GET** / | All available EMIL Products
[**get_product**](EMILProductsApi.md#get_product) | **GET** /{emilId} | Available report artifacts for a specified EMIL product.
[**get_product_archives**](EMILProductsApi.md#get_product_archives) | **POST** /archive/{emilId}/download | Download a collection of EMIL Product archives.
[**get_product_history**](EMILProductsApi.md#get_product_history) | **GET** /archive/{emilId} | Available report archives for a specified EMIL product.


# **get_list_for_products**
> Product get_list_for_products(ocp_apim_subscription_key)

All available EMIL Products

Retrieve all available (active) products in the current EMIL registry having public accessibility.

### Example

* Api Key Authentication (apiKeyQuery):
* Api Key Authentication (apiKeyHeader):

```python
import openapi_client
from openapi_client.models.product import Product
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ercot.com/api/public-reports
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.ercot.com/api/public-reports"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyQuery
configuration.api_key['apiKeyQuery'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyQuery'] = 'Bearer'

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EMILProductsApi(api_client)
    ocp_apim_subscription_key = '35796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.

    try:
        # All available EMIL Products
        api_response = api_instance.get_list_for_products(ocp_apim_subscription_key)
        print("The response of EMILProductsApi->get_list_for_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EMILProductsApi->get_list_for_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 

### Return type

[**Product**](Product.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK The operation completed successfully. |  -  |
**400** | The request operation failed. The request and/or one or more of its parameters are invalid. |  -  |
**403** | The request operation failed. You do not have access to the requested resource. |  -  |
**404** | The request operation failed. The requested resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product**
> Product get_product(emil_id, ocp_apim_subscription_key)

Available report artifacts for a specified EMIL product.

Available report artifacts for a specified EMIL product.

### Example

* Api Key Authentication (apiKeyQuery):
* Api Key Authentication (apiKeyHeader):

```python
import openapi_client
from openapi_client.models.product import Product
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ercot.com/api/public-reports
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.ercot.com/api/public-reports"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyQuery
configuration.api_key['apiKeyQuery'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyQuery'] = 'Bearer'

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EMILProductsApi(api_client)
    emil_id = 'NP3-566-CD' # str | The unique EMIL Product identifier.
    ocp_apim_subscription_key = '35796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.

    try:
        # Available report artifacts for a specified EMIL product.
        api_response = api_instance.get_product(emil_id, ocp_apim_subscription_key)
        print("The response of EMILProductsApi->get_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EMILProductsApi->get_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emil_id** | **str**| The unique EMIL Product identifier. | 
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 

### Return type

[**Product**](Product.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK The operation completed successfully. |  -  |
**400** | The request operation failed. The request and/or one or more of its parameters are invalid. |  -  |
**403** | The request operation failed. You do not have access to the requested resource. |  -  |
**404** | The request operation failed. The requested resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_archives**
> bytearray get_product_archives(emil_id, ocp_apim_subscription_key, archive_request=archive_request)

Download a collection of EMIL Product archives.

Download a collection of EMIL Product archives by generating a JSON request with a single 'docIds' element containing the document identifiers you wish to download.

### Example

* Api Key Authentication (apiKeyQuery):
* Api Key Authentication (apiKeyHeader):

```python
import openapi_client
from openapi_client.models.archive_request import ArchiveRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ercot.com/api/public-reports
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.ercot.com/api/public-reports"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyQuery
configuration.api_key['apiKeyQuery'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyQuery'] = 'Bearer'

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EMILProductsApi(api_client)
    emil_id = 'NP3-566-CD' # str | The EMIL Product identifier for the desired set of archives.
    ocp_apim_subscription_key = '35796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    archive_request = {"docIds":[0]} # ArchiveRequest |  (optional)

    try:
        # Download a collection of EMIL Product archives.
        api_response = api_instance.get_product_archives(emil_id, ocp_apim_subscription_key, archive_request=archive_request)
        print("The response of EMILProductsApi->get_product_archives:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EMILProductsApi->get_product_archives: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emil_id** | **str**| The EMIL Product identifier for the desired set of archives. | 
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **archive_request** | [**ArchiveRequest**](ArchiveRequest.md)|  | [optional] 

### Return type

**bytearray**

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/zip, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK The operation completed successfully. |  -  |
**400** | The request operation failed. The request and/or one or more of its parameters are invalid. |  -  |
**403** | The request operation failed. You do not have access to the requested resource. |  -  |
**404** | The request operation failed. The requested resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_history**
> ProductHistory get_product_history(emil_id, ocp_apim_subscription_key)

Available report archives for a specified EMIL product.

Available report archives for a specified EMIL product.

### Example

* Api Key Authentication (apiKeyQuery):
* Api Key Authentication (apiKeyHeader):

```python
import openapi_client
from openapi_client.models.product_history import ProductHistory
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ercot.com/api/public-reports
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.ercot.com/api/public-reports"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKeyQuery
configuration.api_key['apiKeyQuery'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyQuery'] = 'Bearer'

# Configure API key authorization: apiKeyHeader
configuration.api_key['apiKeyHeader'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKeyHeader'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.EMILProductsApi(api_client)
    emil_id = 'NP3-566-CD' # str | The unique EMIL Product identifier.
    ocp_apim_subscription_key = '35796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.

    try:
        # Available report archives for a specified EMIL product.
        api_response = api_instance.get_product_history(emil_id, ocp_apim_subscription_key)
        print("The response of EMILProductsApi->get_product_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EMILProductsApi->get_product_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **emil_id** | **str**| The unique EMIL Product identifier. | 
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 

### Return type

[**ProductHistory**](ProductHistory.md)

### Authorization

[apiKeyQuery](../README.md#apiKeyQuery), [apiKeyHeader](../README.md#apiKeyHeader)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK The operation completed successfully. |  -  |
**400** | The request operation failed. The request and/or one or more of its parameters are invalid. |  -  |
**403** | The request operation failed. You do not have access to the requested resource. |  -  |
**404** | The request operation failed. The requested resource does not exist. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

