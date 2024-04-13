# openapi_client.NP4196MApi

All URIs are relative to *https://api.ercot.com/api/public-reports*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data24**](NP4196MApi.md#get_data24) | **GET** /np4-196-m/dam_price_corrections_spp | DAM Price Corrections for SPP
[**get_data25**](NP4196MApi.md#get_data25) | **GET** /np4-196-m/dam_price_corrections_mcpc | DAM Price Corrections for MCPC
[**get_data26**](NP4196MApi.md#get_data26) | **GET** /np4-196-m/dam_price_corrections_eblmp | DAM Price Corrections for EBLMP


# **get_data24**
> Report get_data24(ocp_apim_subscription_key, price_correction_time_from=price_correction_time_from, price_correction_time_to=price_correction_time_to, dst_flag=dst_flag, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, delivery_hour_from=delivery_hour_from, delivery_hour_to=delivery_hour_to, settlement_point=settlement_point, spp_original_from=spp_original_from, spp_original_to=spp_original_to, spp_corrected_from=spp_corrected_from, spp_corrected_to=spp_corrected_to, page=page, size=size, sort=sort, dir=dir)

DAM Price Corrections for SPP

DAM Price Corrections for SPP

### Example

* Api Key Authentication (apiKeyQuery):
* Api Key Authentication (apiKeyHeader):

```python
import openapi_client
from openapi_client.models.report import Report
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
    api_instance = openapi_client.NP4196MApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    price_correction_time_from = 'price_correction_time_from_example' # str | Format - mm:ss. (optional)
    price_correction_time_to = 'price_correction_time_to_example' # str | Format - mm:ss. (optional)
    dst_flag = True # bool | Format - true | false. (optional)
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_hour_from = 56 # int | Format - ###. (optional)
    delivery_hour_to = 56 # int | Format - ###. (optional)
    settlement_point = 'settlement_point_example' # str | Format - abc123. (optional)
    spp_original_from = 3.4 # float | Format - ####.###. (optional)
    spp_original_to = 3.4 # float | Format - ####.###. (optional)
    spp_corrected_from = 3.4 # float | Format - ####.###. (optional)
    spp_corrected_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # DAM Price Corrections for SPP
        api_response = api_instance.get_data24(ocp_apim_subscription_key, price_correction_time_from=price_correction_time_from, price_correction_time_to=price_correction_time_to, dst_flag=dst_flag, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, delivery_hour_from=delivery_hour_from, delivery_hour_to=delivery_hour_to, settlement_point=settlement_point, spp_original_from=spp_original_from, spp_original_to=spp_original_to, spp_corrected_from=spp_corrected_from, spp_corrected_to=spp_corrected_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP4196MApi->get_data24:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP4196MApi->get_data24: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **price_correction_time_from** | **str**| Format - mm:ss. | [optional] 
 **price_correction_time_to** | **str**| Format - mm:ss. | [optional] 
 **dst_flag** | **bool**| Format - true | false. | [optional] 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_hour_from** | **int**| Format - ###. | [optional] 
 **delivery_hour_to** | **int**| Format - ###. | [optional] 
 **settlement_point** | **str**| Format - abc123. | [optional] 
 **spp_original_from** | **float**| Format - ####.###. | [optional] 
 **spp_original_to** | **float**| Format - ####.###. | [optional] 
 **spp_corrected_from** | **float**| Format - ####.###. | [optional] 
 **spp_corrected_to** | **float**| Format - ####.###. | [optional] 
 **page** | **int**| Format - ###. Page number of returned values in the collection. | [optional] 
 **size** | **int**| Format - ###. Number of returned items per page. | [optional] 
 **sort** | **str**| Format - abc123. Defines field by which to sort the returned resource values. | [optional] 
 **dir** | **str**| Format - abc123. Defines sort order of returned values based on the primary business key of the resource. | [optional] 

### Return type

[**Report**](Report.md)

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

# **get_data25**
> Report get_data25(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, delivery_hour_from=delivery_hour_from, delivery_hour_to=delivery_hour_to, as_type=as_type, mcpc_original_from=mcpc_original_from, mcpc_original_to=mcpc_original_to, mcpc_corrected_from=mcpc_corrected_from, mcpc_corrected_to=mcpc_corrected_to, price_correction_time_from=price_correction_time_from, price_correction_time_to=price_correction_time_to, dst_flag=dst_flag, page=page, size=size, sort=sort, dir=dir)

DAM Price Corrections for MCPC

DAM Price Corrections for MCPC

### Example

* Api Key Authentication (apiKeyQuery):
* Api Key Authentication (apiKeyHeader):

```python
import openapi_client
from openapi_client.models.report import Report
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
    api_instance = openapi_client.NP4196MApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_hour_from = 56 # int | Format - ###. (optional)
    delivery_hour_to = 56 # int | Format - ###. (optional)
    as_type = 'as_type_example' # str | Format - abc123. (optional)
    mcpc_original_from = 3.4 # float | Format - ####.###. (optional)
    mcpc_original_to = 3.4 # float | Format - ####.###. (optional)
    mcpc_corrected_from = 3.4 # float | Format - ####.###. (optional)
    mcpc_corrected_to = 3.4 # float | Format - ####.###. (optional)
    price_correction_time_from = 'price_correction_time_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    price_correction_time_to = 'price_correction_time_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    dst_flag = True # bool | Format - true | false. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # DAM Price Corrections for MCPC
        api_response = api_instance.get_data25(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, delivery_hour_from=delivery_hour_from, delivery_hour_to=delivery_hour_to, as_type=as_type, mcpc_original_from=mcpc_original_from, mcpc_original_to=mcpc_original_to, mcpc_corrected_from=mcpc_corrected_from, mcpc_corrected_to=mcpc_corrected_to, price_correction_time_from=price_correction_time_from, price_correction_time_to=price_correction_time_to, dst_flag=dst_flag, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP4196MApi->get_data25:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP4196MApi->get_data25: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_hour_from** | **int**| Format - ###. | [optional] 
 **delivery_hour_to** | **int**| Format - ###. | [optional] 
 **as_type** | **str**| Format - abc123. | [optional] 
 **mcpc_original_from** | **float**| Format - ####.###. | [optional] 
 **mcpc_original_to** | **float**| Format - ####.###. | [optional] 
 **mcpc_corrected_from** | **float**| Format - ####.###. | [optional] 
 **mcpc_corrected_to** | **float**| Format - ####.###. | [optional] 
 **price_correction_time_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **price_correction_time_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **dst_flag** | **bool**| Format - true | false. | [optional] 
 **page** | **int**| Format - ###. Page number of returned values in the collection. | [optional] 
 **size** | **int**| Format - ###. Number of returned items per page. | [optional] 
 **sort** | **str**| Format - abc123. Defines field by which to sort the returned resource values. | [optional] 
 **dir** | **str**| Format - abc123. Defines sort order of returned values based on the primary business key of the resource. | [optional] 

### Return type

[**Report**](Report.md)

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

# **get_data26**
> Report get_data26(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, delivery_hour_from=delivery_hour_from, delivery_hour_to=delivery_hour_to, electrical_bus=electrical_bus, lmp_original_from=lmp_original_from, lmp_original_to=lmp_original_to, lmp_corrected_from=lmp_corrected_from, lmp_corrected_to=lmp_corrected_to, price_correction_time_from=price_correction_time_from, price_correction_time_to=price_correction_time_to, dst_flag=dst_flag, page=page, size=size, sort=sort, dir=dir)

DAM Price Corrections for EBLMP

DAM Price Corrections for EBLMP

### Example

* Api Key Authentication (apiKeyQuery):
* Api Key Authentication (apiKeyHeader):

```python
import openapi_client
from openapi_client.models.report import Report
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
    api_instance = openapi_client.NP4196MApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_hour_from = 56 # int | Format - ###. (optional)
    delivery_hour_to = 56 # int | Format - ###. (optional)
    electrical_bus = 'electrical_bus_example' # str | Format - abc123. (optional)
    lmp_original_from = 3.4 # float | Format - ####.###. (optional)
    lmp_original_to = 3.4 # float | Format - ####.###. (optional)
    lmp_corrected_from = 3.4 # float | Format - ####.###. (optional)
    lmp_corrected_to = 3.4 # float | Format - ####.###. (optional)
    price_correction_time_from = 'price_correction_time_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    price_correction_time_to = 'price_correction_time_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    dst_flag = True # bool | Format - true | false. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # DAM Price Corrections for EBLMP
        api_response = api_instance.get_data26(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, delivery_hour_from=delivery_hour_from, delivery_hour_to=delivery_hour_to, electrical_bus=electrical_bus, lmp_original_from=lmp_original_from, lmp_original_to=lmp_original_to, lmp_corrected_from=lmp_corrected_from, lmp_corrected_to=lmp_corrected_to, price_correction_time_from=price_correction_time_from, price_correction_time_to=price_correction_time_to, dst_flag=dst_flag, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP4196MApi->get_data26:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP4196MApi->get_data26: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_hour_from** | **int**| Format - ###. | [optional] 
 **delivery_hour_to** | **int**| Format - ###. | [optional] 
 **electrical_bus** | **str**| Format - abc123. | [optional] 
 **lmp_original_from** | **float**| Format - ####.###. | [optional] 
 **lmp_original_to** | **float**| Format - ####.###. | [optional] 
 **lmp_corrected_from** | **float**| Format - ####.###. | [optional] 
 **lmp_corrected_to** | **float**| Format - ####.###. | [optional] 
 **price_correction_time_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **price_correction_time_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **dst_flag** | **bool**| Format - true | false. | [optional] 
 **page** | **int**| Format - ###. Page number of returned values in the collection. | [optional] 
 **size** | **int**| Format - ###. Number of returned items per page. | [optional] 
 **sort** | **str**| Format - abc123. Defines field by which to sort the returned resource values. | [optional] 
 **dir** | **str**| Format - abc123. Defines sort order of returned values based on the primary business key of the resource. | [optional] 

### Return type

[**Report**](Report.md)

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

