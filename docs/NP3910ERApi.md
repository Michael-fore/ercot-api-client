# openapi_client.NP3910ERApi

All URIs are relative to *https://api.ercot.com/api/public-reports*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data83**](NP3910ERApi.md#get_data83) | **GET** /np3-910-er/2d_agg_out_sched_west | 2 Day Aggregated Output Schedule West
[**get_data84**](NP3910ERApi.md#get_data84) | **GET** /np3-910-er/2d_agg_out_sched_south | 2 Day Aggregated Output Schedule South
[**get_data85**](NP3910ERApi.md#get_data85) | **GET** /np3-910-er/2d_agg_out_sched_north | 2 Day Aggregated Output Schedule North
[**get_data86**](NP3910ERApi.md#get_data86) | **GET** /np3-910-er/2d_agg_out_sched_houston | 2 Day Aggregated Output Schedule Houston
[**get_data87**](NP3910ERApi.md#get_data87) | **GET** /np3-910-er/2d_agg_out_sched | 2 Day Aggregated Output Schedule
[**get_data88**](NP3910ERApi.md#get_data88) | **GET** /np3-910-er/2d_agg_load_summary_west | 2 Day Aggregated Load Summary West
[**get_data89**](NP3910ERApi.md#get_data89) | **GET** /np3-910-er/2d_agg_load_summary_south | 2 Day Aggregated Load Summary South
[**get_data90**](NP3910ERApi.md#get_data90) | **GET** /np3-910-er/2d_agg_load_summary_north | 2 Day Aggregated Load Summary North
[**get_data91**](NP3910ERApi.md#get_data91) | **GET** /np3-910-er/2d_agg_load_summary_houston | 2 Day Aggregated Load Summary Houston
[**get_data92**](NP3910ERApi.md#get_data92) | **GET** /np3-910-er/2d_agg_load_summary | 2 Day Aggregated Load Summary
[**get_data93**](NP3910ERApi.md#get_data93) | **GET** /np3-910-er/2d_agg_gen_summary_west | 2 Day Aggregated Generation Summary West
[**get_data94**](NP3910ERApi.md#get_data94) | **GET** /np3-910-er/2d_agg_gen_summary_south | 2 Day Aggregated Generation Summary South
[**get_data95**](NP3910ERApi.md#get_data95) | **GET** /np3-910-er/2d_agg_gen_summary_north | 2 Day Aggregated Generation Summary North
[**get_data96**](NP3910ERApi.md#get_data96) | **GET** /np3-910-er/2d_agg_gen_summary_houston | 2 Day Aggregated Generation Summary Houston
[**get_data97**](NP3910ERApi.md#get_data97) | **GET** /np3-910-er/2d_agg_gen_summary | 2 Day Aggregated Generation Summary
[**get_data98**](NP3910ERApi.md#get_data98) | **GET** /np3-910-er/2d_agg_dsr_loads | 2 Day Aggregated DSR Loads


# **get_data83**
> Report get_data83(ocp_apim_subscription_key, repeat_hour_flag=repeat_hour_flag, sum_lsl_output_sched_from=sum_lsl_output_sched_from, sum_lsl_output_sched_to=sum_lsl_output_sched_to, sum_hsl_output_sched_from=sum_hsl_output_sched_from, sum_hsl_output_sched_to=sum_hsl_output_sched_to, sum_output_sched_from=sum_output_sched_from, sum_output_sched_to=sum_output_sched_to, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Output Schedule West

2 Day Aggregated Output Schedule West

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
    api_instance = openapi_client.NP3910ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    sum_lsl_output_sched_from = 3.4 # float | Format - ####.###. (optional)
    sum_lsl_output_sched_to = 3.4 # float | Format - ####.###. (optional)
    sum_hsl_output_sched_from = 3.4 # float | Format - ####.###. (optional)
    sum_hsl_output_sched_to = 3.4 # float | Format - ####.###. (optional)
    sum_output_sched_from = 3.4 # float | Format - ####.###. (optional)
    sum_output_sched_to = 3.4 # float | Format - ####.###. (optional)
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Output Schedule West
        api_response = api_instance.get_data83(ocp_apim_subscription_key, repeat_hour_flag=repeat_hour_flag, sum_lsl_output_sched_from=sum_lsl_output_sched_from, sum_lsl_output_sched_to=sum_lsl_output_sched_to, sum_hsl_output_sched_from=sum_hsl_output_sched_from, sum_hsl_output_sched_to=sum_hsl_output_sched_to, sum_output_sched_from=sum_output_sched_from, sum_output_sched_to=sum_output_sched_to, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3910ERApi->get_data83:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3910ERApi->get_data83: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **sum_lsl_output_sched_from** | **float**| Format - ####.###. | [optional] 
 **sum_lsl_output_sched_to** | **float**| Format - ####.###. | [optional] 
 **sum_hsl_output_sched_from** | **float**| Format - ####.###. | [optional] 
 **sum_hsl_output_sched_to** | **float**| Format - ####.###. | [optional] 
 **sum_output_sched_from** | **float**| Format - ####.###. | [optional] 
 **sum_output_sched_to** | **float**| Format - ####.###. | [optional] 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
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

# **get_data84**
> Report get_data84(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_lsl_output_sched_from=sum_lsl_output_sched_from, sum_lsl_output_sched_to=sum_lsl_output_sched_to, sum_hsl_output_sched_from=sum_hsl_output_sched_from, sum_hsl_output_sched_to=sum_hsl_output_sched_to, sum_output_sched_from=sum_output_sched_from, sum_output_sched_to=sum_output_sched_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Output Schedule South

2 Day Aggregated Output Schedule South

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
    api_instance = openapi_client.NP3910ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    sum_lsl_output_sched_from = 3.4 # float | Format - ####.###. (optional)
    sum_lsl_output_sched_to = 3.4 # float | Format - ####.###. (optional)
    sum_hsl_output_sched_from = 3.4 # float | Format - ####.###. (optional)
    sum_hsl_output_sched_to = 3.4 # float | Format - ####.###. (optional)
    sum_output_sched_from = 3.4 # float | Format - ####.###. (optional)
    sum_output_sched_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Output Schedule South
        api_response = api_instance.get_data84(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_lsl_output_sched_from=sum_lsl_output_sched_from, sum_lsl_output_sched_to=sum_lsl_output_sched_to, sum_hsl_output_sched_from=sum_hsl_output_sched_from, sum_hsl_output_sched_to=sum_hsl_output_sched_to, sum_output_sched_from=sum_output_sched_from, sum_output_sched_to=sum_output_sched_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3910ERApi->get_data84:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3910ERApi->get_data84: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **sum_lsl_output_sched_from** | **float**| Format - ####.###. | [optional] 
 **sum_lsl_output_sched_to** | **float**| Format - ####.###. | [optional] 
 **sum_hsl_output_sched_from** | **float**| Format - ####.###. | [optional] 
 **sum_hsl_output_sched_to** | **float**| Format - ####.###. | [optional] 
 **sum_output_sched_from** | **float**| Format - ####.###. | [optional] 
 **sum_output_sched_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data85**
> Report get_data85(ocp_apim_subscription_key, sum_hsl_output_sched_from=sum_hsl_output_sched_from, sum_hsl_output_sched_to=sum_hsl_output_sched_to, sum_output_sched_from=sum_output_sched_from, sum_output_sched_to=sum_output_sched_to, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_lsl_output_sched_from=sum_lsl_output_sched_from, sum_lsl_output_sched_to=sum_lsl_output_sched_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Output Schedule North

2 Day Aggregated Output Schedule North

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
    api_instance = openapi_client.NP3910ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sum_hsl_output_sched_from = 3.4 # float | Format - ####.###. (optional)
    sum_hsl_output_sched_to = 3.4 # float | Format - ####.###. (optional)
    sum_output_sched_from = 3.4 # float | Format - ####.###. (optional)
    sum_output_sched_to = 3.4 # float | Format - ####.###. (optional)
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    sum_lsl_output_sched_from = 3.4 # float | Format - ####.###. (optional)
    sum_lsl_output_sched_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Output Schedule North
        api_response = api_instance.get_data85(ocp_apim_subscription_key, sum_hsl_output_sched_from=sum_hsl_output_sched_from, sum_hsl_output_sched_to=sum_hsl_output_sched_to, sum_output_sched_from=sum_output_sched_from, sum_output_sched_to=sum_output_sched_to, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_lsl_output_sched_from=sum_lsl_output_sched_from, sum_lsl_output_sched_to=sum_lsl_output_sched_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3910ERApi->get_data85:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3910ERApi->get_data85: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sum_hsl_output_sched_from** | **float**| Format - ####.###. | [optional] 
 **sum_hsl_output_sched_to** | **float**| Format - ####.###. | [optional] 
 **sum_output_sched_from** | **float**| Format - ####.###. | [optional] 
 **sum_output_sched_to** | **float**| Format - ####.###. | [optional] 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **sum_lsl_output_sched_from** | **float**| Format - ####.###. | [optional] 
 **sum_lsl_output_sched_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data86**
> Report get_data86(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_lsl_output_sched_from=sum_lsl_output_sched_from, sum_lsl_output_sched_to=sum_lsl_output_sched_to, sum_hsl_output_sched_from=sum_hsl_output_sched_from, sum_hsl_output_sched_to=sum_hsl_output_sched_to, sum_output_sched_from=sum_output_sched_from, sum_output_sched_to=sum_output_sched_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Output Schedule Houston

2 Day Aggregated Output Schedule Houston

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
    api_instance = openapi_client.NP3910ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    sum_lsl_output_sched_from = 3.4 # float | Format - ####.###. (optional)
    sum_lsl_output_sched_to = 3.4 # float | Format - ####.###. (optional)
    sum_hsl_output_sched_from = 3.4 # float | Format - ####.###. (optional)
    sum_hsl_output_sched_to = 3.4 # float | Format - ####.###. (optional)
    sum_output_sched_from = 3.4 # float | Format - ####.###. (optional)
    sum_output_sched_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Output Schedule Houston
        api_response = api_instance.get_data86(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_lsl_output_sched_from=sum_lsl_output_sched_from, sum_lsl_output_sched_to=sum_lsl_output_sched_to, sum_hsl_output_sched_from=sum_hsl_output_sched_from, sum_hsl_output_sched_to=sum_hsl_output_sched_to, sum_output_sched_from=sum_output_sched_from, sum_output_sched_to=sum_output_sched_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3910ERApi->get_data86:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3910ERApi->get_data86: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **sum_lsl_output_sched_from** | **float**| Format - ####.###. | [optional] 
 **sum_lsl_output_sched_to** | **float**| Format - ####.###. | [optional] 
 **sum_hsl_output_sched_from** | **float**| Format - ####.###. | [optional] 
 **sum_hsl_output_sched_to** | **float**| Format - ####.###. | [optional] 
 **sum_output_sched_from** | **float**| Format - ####.###. | [optional] 
 **sum_output_sched_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data87**
> Report get_data87(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_lsl_output_sched_from=sum_lsl_output_sched_from, sum_lsl_output_sched_to=sum_lsl_output_sched_to, sum_hsl_output_sched_from=sum_hsl_output_sched_from, sum_hsl_output_sched_to=sum_hsl_output_sched_to, sum_output_sched_from=sum_output_sched_from, sum_output_sched_to=sum_output_sched_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Output Schedule

2 Day Aggregated Output Schedule

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
    api_instance = openapi_client.NP3910ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    sum_lsl_output_sched_from = 3.4 # float | Format - ####.###. (optional)
    sum_lsl_output_sched_to = 3.4 # float | Format - ####.###. (optional)
    sum_hsl_output_sched_from = 3.4 # float | Format - ####.###. (optional)
    sum_hsl_output_sched_to = 3.4 # float | Format - ####.###. (optional)
    sum_output_sched_from = 3.4 # float | Format - ####.###. (optional)
    sum_output_sched_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Output Schedule
        api_response = api_instance.get_data87(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_lsl_output_sched_from=sum_lsl_output_sched_from, sum_lsl_output_sched_to=sum_lsl_output_sched_to, sum_hsl_output_sched_from=sum_hsl_output_sched_from, sum_hsl_output_sched_to=sum_hsl_output_sched_to, sum_output_sched_from=sum_output_sched_from, sum_output_sched_to=sum_output_sched_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3910ERApi->get_data87:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3910ERApi->get_data87: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **sum_lsl_output_sched_from** | **float**| Format - ####.###. | [optional] 
 **sum_lsl_output_sched_to** | **float**| Format - ####.###. | [optional] 
 **sum_hsl_output_sched_from** | **float**| Format - ####.###. | [optional] 
 **sum_hsl_output_sched_to** | **float**| Format - ####.###. | [optional] 
 **sum_output_sched_from** | **float**| Format - ####.###. | [optional] 
 **sum_output_sched_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data88**
> Report get_data88(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_telem_gen_mw_from=sum_telem_gen_mw_from, sum_telem_gen_mwto=sum_telem_gen_mwto, sum_telem_d_ctie_mw_from=sum_telem_d_ctie_mw_from, sum_telem_d_ctie_mwto=sum_telem_d_ctie_mwto, agg_load_summary_from=agg_load_summary_from, agg_load_summary_to=agg_load_summary_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Load Summary West

2 Day Aggregated Load Summary West

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
    api_instance = openapi_client.NP3910ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    sum_telem_gen_mw_from = 3.4 # float | Format - ####.###. (optional)
    sum_telem_gen_mwto = 3.4 # float | Format - ####.###. (optional)
    sum_telem_d_ctie_mw_from = 3.4 # float | Format - ####.###. (optional)
    sum_telem_d_ctie_mwto = 3.4 # float | Format - ####.###. (optional)
    agg_load_summary_from = 3.4 # float | Format - ####.###. (optional)
    agg_load_summary_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Load Summary West
        api_response = api_instance.get_data88(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_telem_gen_mw_from=sum_telem_gen_mw_from, sum_telem_gen_mwto=sum_telem_gen_mwto, sum_telem_d_ctie_mw_from=sum_telem_d_ctie_mw_from, sum_telem_d_ctie_mwto=sum_telem_d_ctie_mwto, agg_load_summary_from=agg_load_summary_from, agg_load_summary_to=agg_load_summary_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3910ERApi->get_data88:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3910ERApi->get_data88: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **sum_telem_gen_mw_from** | **float**| Format - ####.###. | [optional] 
 **sum_telem_gen_mwto** | **float**| Format - ####.###. | [optional] 
 **sum_telem_d_ctie_mw_from** | **float**| Format - ####.###. | [optional] 
 **sum_telem_d_ctie_mwto** | **float**| Format - ####.###. | [optional] 
 **agg_load_summary_from** | **float**| Format - ####.###. | [optional] 
 **agg_load_summary_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data89**
> Report get_data89(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_telem_gen_mw_from=sum_telem_gen_mw_from, sum_telem_gen_mwto=sum_telem_gen_mwto, sum_telem_d_ctie_mw_from=sum_telem_d_ctie_mw_from, sum_telem_d_ctie_mwto=sum_telem_d_ctie_mwto, agg_load_summary_from=agg_load_summary_from, agg_load_summary_to=agg_load_summary_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Load Summary South

2 Day Aggregated Load Summary South

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
    api_instance = openapi_client.NP3910ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    sum_telem_gen_mw_from = 3.4 # float | Format - ####.###. (optional)
    sum_telem_gen_mwto = 3.4 # float | Format - ####.###. (optional)
    sum_telem_d_ctie_mw_from = 3.4 # float | Format - ####.###. (optional)
    sum_telem_d_ctie_mwto = 3.4 # float | Format - ####.###. (optional)
    agg_load_summary_from = 3.4 # float | Format - ####.###. (optional)
    agg_load_summary_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Load Summary South
        api_response = api_instance.get_data89(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_telem_gen_mw_from=sum_telem_gen_mw_from, sum_telem_gen_mwto=sum_telem_gen_mwto, sum_telem_d_ctie_mw_from=sum_telem_d_ctie_mw_from, sum_telem_d_ctie_mwto=sum_telem_d_ctie_mwto, agg_load_summary_from=agg_load_summary_from, agg_load_summary_to=agg_load_summary_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3910ERApi->get_data89:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3910ERApi->get_data89: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **sum_telem_gen_mw_from** | **float**| Format - ####.###. | [optional] 
 **sum_telem_gen_mwto** | **float**| Format - ####.###. | [optional] 
 **sum_telem_d_ctie_mw_from** | **float**| Format - ####.###. | [optional] 
 **sum_telem_d_ctie_mwto** | **float**| Format - ####.###. | [optional] 
 **agg_load_summary_from** | **float**| Format - ####.###. | [optional] 
 **agg_load_summary_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data90**
> Report get_data90(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_telem_gen_mw_from=sum_telem_gen_mw_from, sum_telem_gen_mwto=sum_telem_gen_mwto, sum_telem_d_ctie_mw_from=sum_telem_d_ctie_mw_from, sum_telem_d_ctie_mwto=sum_telem_d_ctie_mwto, agg_load_summary_from=agg_load_summary_from, agg_load_summary_to=agg_load_summary_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Load Summary North

2 Day Aggregated Load Summary North

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
    api_instance = openapi_client.NP3910ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    sum_telem_gen_mw_from = 3.4 # float | Format - ####.###. (optional)
    sum_telem_gen_mwto = 3.4 # float | Format - ####.###. (optional)
    sum_telem_d_ctie_mw_from = 3.4 # float | Format - ####.###. (optional)
    sum_telem_d_ctie_mwto = 3.4 # float | Format - ####.###. (optional)
    agg_load_summary_from = 3.4 # float | Format - ####.###. (optional)
    agg_load_summary_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Load Summary North
        api_response = api_instance.get_data90(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_telem_gen_mw_from=sum_telem_gen_mw_from, sum_telem_gen_mwto=sum_telem_gen_mwto, sum_telem_d_ctie_mw_from=sum_telem_d_ctie_mw_from, sum_telem_d_ctie_mwto=sum_telem_d_ctie_mwto, agg_load_summary_from=agg_load_summary_from, agg_load_summary_to=agg_load_summary_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3910ERApi->get_data90:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3910ERApi->get_data90: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **sum_telem_gen_mw_from** | **float**| Format - ####.###. | [optional] 
 **sum_telem_gen_mwto** | **float**| Format - ####.###. | [optional] 
 **sum_telem_d_ctie_mw_from** | **float**| Format - ####.###. | [optional] 
 **sum_telem_d_ctie_mwto** | **float**| Format - ####.###. | [optional] 
 **agg_load_summary_from** | **float**| Format - ####.###. | [optional] 
 **agg_load_summary_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data91**
> Report get_data91(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_telem_gen_mw_from=sum_telem_gen_mw_from, sum_telem_gen_mwto=sum_telem_gen_mwto, sum_telem_d_ctie_mw_from=sum_telem_d_ctie_mw_from, sum_telem_d_ctie_mwto=sum_telem_d_ctie_mwto, agg_load_summary_from=agg_load_summary_from, agg_load_summary_to=agg_load_summary_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Load Summary Houston

2 Day Aggregated Load Summary Houston

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
    api_instance = openapi_client.NP3910ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    sum_telem_gen_mw_from = 3.4 # float | Format - ####.###. (optional)
    sum_telem_gen_mwto = 3.4 # float | Format - ####.###. (optional)
    sum_telem_d_ctie_mw_from = 3.4 # float | Format - ####.###. (optional)
    sum_telem_d_ctie_mwto = 3.4 # float | Format - ####.###. (optional)
    agg_load_summary_from = 3.4 # float | Format - ####.###. (optional)
    agg_load_summary_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Load Summary Houston
        api_response = api_instance.get_data91(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_telem_gen_mw_from=sum_telem_gen_mw_from, sum_telem_gen_mwto=sum_telem_gen_mwto, sum_telem_d_ctie_mw_from=sum_telem_d_ctie_mw_from, sum_telem_d_ctie_mwto=sum_telem_d_ctie_mwto, agg_load_summary_from=agg_load_summary_from, agg_load_summary_to=agg_load_summary_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3910ERApi->get_data91:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3910ERApi->get_data91: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **sum_telem_gen_mw_from** | **float**| Format - ####.###. | [optional] 
 **sum_telem_gen_mwto** | **float**| Format - ####.###. | [optional] 
 **sum_telem_d_ctie_mw_from** | **float**| Format - ####.###. | [optional] 
 **sum_telem_d_ctie_mwto** | **float**| Format - ####.###. | [optional] 
 **agg_load_summary_from** | **float**| Format - ####.###. | [optional] 
 **agg_load_summary_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data92**
> Report get_data92(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_telem_gen_mw_from=sum_telem_gen_mw_from, sum_telem_gen_mwto=sum_telem_gen_mwto, sum_telem_d_ctie_mw_from=sum_telem_d_ctie_mw_from, sum_telem_d_ctie_mwto=sum_telem_d_ctie_mwto, agg_load_summary_from=agg_load_summary_from, agg_load_summary_to=agg_load_summary_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Load Summary

2 Day Aggregated Load Summary

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
    api_instance = openapi_client.NP3910ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    sum_telem_gen_mw_from = 3.4 # float | Format - ####.###. (optional)
    sum_telem_gen_mwto = 3.4 # float | Format - ####.###. (optional)
    sum_telem_d_ctie_mw_from = 3.4 # float | Format - ####.###. (optional)
    sum_telem_d_ctie_mwto = 3.4 # float | Format - ####.###. (optional)
    agg_load_summary_from = 3.4 # float | Format - ####.###. (optional)
    agg_load_summary_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Load Summary
        api_response = api_instance.get_data92(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_telem_gen_mw_from=sum_telem_gen_mw_from, sum_telem_gen_mwto=sum_telem_gen_mwto, sum_telem_d_ctie_mw_from=sum_telem_d_ctie_mw_from, sum_telem_d_ctie_mwto=sum_telem_d_ctie_mwto, agg_load_summary_from=agg_load_summary_from, agg_load_summary_to=agg_load_summary_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3910ERApi->get_data92:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3910ERApi->get_data92: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **sum_telem_gen_mw_from** | **float**| Format - ####.###. | [optional] 
 **sum_telem_gen_mwto** | **float**| Format - ####.###. | [optional] 
 **sum_telem_d_ctie_mw_from** | **float**| Format - ####.###. | [optional] 
 **sum_telem_d_ctie_mwto** | **float**| Format - ####.###. | [optional] 
 **agg_load_summary_from** | **float**| Format - ####.###. | [optional] 
 **agg_load_summary_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data93**
> Report get_data93(ocp_apim_subscription_key, repeat_hour_flag=repeat_hour_flag, sum_base_point_non_wgr_from=sum_base_point_non_wgr_from, sum_base_point_non_wgrto=sum_base_point_non_wgrto, sum_hasl_non_wgr_from=sum_hasl_non_wgr_from, sum_hasl_non_wgrto=sum_hasl_non_wgrto, sum_lasl_non_wgr_from=sum_lasl_non_wgr_from, sum_lasl_non_wgrto=sum_lasl_non_wgrto, sum_base_point_wgr_from=sum_base_point_wgr_from, sum_base_point_wgrto=sum_base_point_wgrto, sum_hasl_wgr_from=sum_hasl_wgr_from, sum_hasl_wgrto=sum_hasl_wgrto, sum_lasl_wgr_from=sum_lasl_wgr_from, sum_lasl_wgrto=sum_lasl_wgrto, sum_base_point_rem_res_from=sum_base_point_rem_res_from, sum_base_point_rem_res_to=sum_base_point_rem_res_to, sum_hasl_rem_res_from=sum_hasl_rem_res_from, sum_hasl_rem_res_to=sum_hasl_rem_res_to, sum_lasl_rem_res_from=sum_lasl_rem_res_from, sum_lasl_rem_res_to=sum_lasl_rem_res_to, sum_gen_telem_mw_from=sum_gen_telem_mw_from, sum_gen_telem_mwto=sum_gen_telem_mwto, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Generation Summary West

2 Day Aggregated Generation Summary West

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
    api_instance = openapi_client.NP3910ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    sum_base_point_non_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_non_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_non_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_non_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_non_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_non_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_rem_res_from = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_rem_res_to = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_rem_res_from = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_rem_res_to = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_rem_res_from = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_rem_res_to = 3.4 # float | Format - ####.###. (optional)
    sum_gen_telem_mw_from = 3.4 # float | Format - ####.###. (optional)
    sum_gen_telem_mwto = 3.4 # float | Format - ####.###. (optional)
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Generation Summary West
        api_response = api_instance.get_data93(ocp_apim_subscription_key, repeat_hour_flag=repeat_hour_flag, sum_base_point_non_wgr_from=sum_base_point_non_wgr_from, sum_base_point_non_wgrto=sum_base_point_non_wgrto, sum_hasl_non_wgr_from=sum_hasl_non_wgr_from, sum_hasl_non_wgrto=sum_hasl_non_wgrto, sum_lasl_non_wgr_from=sum_lasl_non_wgr_from, sum_lasl_non_wgrto=sum_lasl_non_wgrto, sum_base_point_wgr_from=sum_base_point_wgr_from, sum_base_point_wgrto=sum_base_point_wgrto, sum_hasl_wgr_from=sum_hasl_wgr_from, sum_hasl_wgrto=sum_hasl_wgrto, sum_lasl_wgr_from=sum_lasl_wgr_from, sum_lasl_wgrto=sum_lasl_wgrto, sum_base_point_rem_res_from=sum_base_point_rem_res_from, sum_base_point_rem_res_to=sum_base_point_rem_res_to, sum_hasl_rem_res_from=sum_hasl_rem_res_from, sum_hasl_rem_res_to=sum_hasl_rem_res_to, sum_lasl_rem_res_from=sum_lasl_rem_res_from, sum_lasl_rem_res_to=sum_lasl_rem_res_to, sum_gen_telem_mw_from=sum_gen_telem_mw_from, sum_gen_telem_mwto=sum_gen_telem_mwto, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3910ERApi->get_data93:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3910ERApi->get_data93: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **sum_base_point_non_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_non_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_non_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_non_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_non_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_non_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_rem_res_from** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_rem_res_to** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_rem_res_from** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_rem_res_to** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_rem_res_from** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_rem_res_to** | **float**| Format - ####.###. | [optional] 
 **sum_gen_telem_mw_from** | **float**| Format - ####.###. | [optional] 
 **sum_gen_telem_mwto** | **float**| Format - ####.###. | [optional] 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
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

# **get_data94**
> Report get_data94(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_base_point_non_wgr_from=sum_base_point_non_wgr_from, sum_base_point_non_wgrto=sum_base_point_non_wgrto, sum_hasl_non_wgr_from=sum_hasl_non_wgr_from, sum_hasl_non_wgrto=sum_hasl_non_wgrto, sum_lasl_non_wgr_from=sum_lasl_non_wgr_from, sum_lasl_non_wgrto=sum_lasl_non_wgrto, sum_base_point_wgr_from=sum_base_point_wgr_from, sum_base_point_wgrto=sum_base_point_wgrto, sum_hasl_wgr_from=sum_hasl_wgr_from, sum_hasl_wgrto=sum_hasl_wgrto, sum_lasl_wgr_from=sum_lasl_wgr_from, sum_lasl_wgrto=sum_lasl_wgrto, sum_base_point_rem_res_from=sum_base_point_rem_res_from, sum_base_point_rem_res_to=sum_base_point_rem_res_to, sum_hasl_rem_res_from=sum_hasl_rem_res_from, sum_hasl_rem_res_to=sum_hasl_rem_res_to, sum_lasl_rem_res_from=sum_lasl_rem_res_from, sum_lasl_rem_res_to=sum_lasl_rem_res_to, sum_gen_telem_mw_from=sum_gen_telem_mw_from, sum_gen_telem_mwto=sum_gen_telem_mwto, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Generation Summary South

2 Day Aggregated Generation Summary South

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
    api_instance = openapi_client.NP3910ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    sum_base_point_non_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_non_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_non_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_non_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_non_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_non_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_rem_res_from = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_rem_res_to = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_rem_res_from = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_rem_res_to = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_rem_res_from = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_rem_res_to = 3.4 # float | Format - ####.###. (optional)
    sum_gen_telem_mw_from = 3.4 # float | Format - ####.###. (optional)
    sum_gen_telem_mwto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Generation Summary South
        api_response = api_instance.get_data94(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_base_point_non_wgr_from=sum_base_point_non_wgr_from, sum_base_point_non_wgrto=sum_base_point_non_wgrto, sum_hasl_non_wgr_from=sum_hasl_non_wgr_from, sum_hasl_non_wgrto=sum_hasl_non_wgrto, sum_lasl_non_wgr_from=sum_lasl_non_wgr_from, sum_lasl_non_wgrto=sum_lasl_non_wgrto, sum_base_point_wgr_from=sum_base_point_wgr_from, sum_base_point_wgrto=sum_base_point_wgrto, sum_hasl_wgr_from=sum_hasl_wgr_from, sum_hasl_wgrto=sum_hasl_wgrto, sum_lasl_wgr_from=sum_lasl_wgr_from, sum_lasl_wgrto=sum_lasl_wgrto, sum_base_point_rem_res_from=sum_base_point_rem_res_from, sum_base_point_rem_res_to=sum_base_point_rem_res_to, sum_hasl_rem_res_from=sum_hasl_rem_res_from, sum_hasl_rem_res_to=sum_hasl_rem_res_to, sum_lasl_rem_res_from=sum_lasl_rem_res_from, sum_lasl_rem_res_to=sum_lasl_rem_res_to, sum_gen_telem_mw_from=sum_gen_telem_mw_from, sum_gen_telem_mwto=sum_gen_telem_mwto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3910ERApi->get_data94:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3910ERApi->get_data94: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **sum_base_point_non_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_non_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_non_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_non_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_non_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_non_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_rem_res_from** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_rem_res_to** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_rem_res_from** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_rem_res_to** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_rem_res_from** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_rem_res_to** | **float**| Format - ####.###. | [optional] 
 **sum_gen_telem_mw_from** | **float**| Format - ####.###. | [optional] 
 **sum_gen_telem_mwto** | **float**| Format - ####.###. | [optional] 
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

# **get_data95**
> Report get_data95(ocp_apim_subscription_key, sum_base_point_wgr_from=sum_base_point_wgr_from, sum_base_point_wgrto=sum_base_point_wgrto, sum_hasl_wgr_from=sum_hasl_wgr_from, sum_hasl_wgrto=sum_hasl_wgrto, sum_lasl_wgr_from=sum_lasl_wgr_from, sum_lasl_wgrto=sum_lasl_wgrto, sum_base_point_rem_res_from=sum_base_point_rem_res_from, sum_base_point_rem_res_to=sum_base_point_rem_res_to, sum_hasl_rem_res_from=sum_hasl_rem_res_from, sum_hasl_rem_res_to=sum_hasl_rem_res_to, sum_lasl_rem_res_from=sum_lasl_rem_res_from, sum_lasl_rem_res_to=sum_lasl_rem_res_to, sum_gen_telem_mw_from=sum_gen_telem_mw_from, sum_gen_telem_mwto=sum_gen_telem_mwto, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_base_point_non_wgr_from=sum_base_point_non_wgr_from, sum_base_point_non_wgrto=sum_base_point_non_wgrto, sum_hasl_non_wgr_from=sum_hasl_non_wgr_from, sum_hasl_non_wgrto=sum_hasl_non_wgrto, sum_lasl_non_wgr_from=sum_lasl_non_wgr_from, sum_lasl_non_wgrto=sum_lasl_non_wgrto, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Generation Summary North

2 Day Aggregated Generation Summary North

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
    api_instance = openapi_client.NP3910ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sum_base_point_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_rem_res_from = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_rem_res_to = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_rem_res_from = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_rem_res_to = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_rem_res_from = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_rem_res_to = 3.4 # float | Format - ####.###. (optional)
    sum_gen_telem_mw_from = 3.4 # float | Format - ####.###. (optional)
    sum_gen_telem_mwto = 3.4 # float | Format - ####.###. (optional)
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    sum_base_point_non_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_non_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_non_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_non_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_non_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_non_wgrto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Generation Summary North
        api_response = api_instance.get_data95(ocp_apim_subscription_key, sum_base_point_wgr_from=sum_base_point_wgr_from, sum_base_point_wgrto=sum_base_point_wgrto, sum_hasl_wgr_from=sum_hasl_wgr_from, sum_hasl_wgrto=sum_hasl_wgrto, sum_lasl_wgr_from=sum_lasl_wgr_from, sum_lasl_wgrto=sum_lasl_wgrto, sum_base_point_rem_res_from=sum_base_point_rem_res_from, sum_base_point_rem_res_to=sum_base_point_rem_res_to, sum_hasl_rem_res_from=sum_hasl_rem_res_from, sum_hasl_rem_res_to=sum_hasl_rem_res_to, sum_lasl_rem_res_from=sum_lasl_rem_res_from, sum_lasl_rem_res_to=sum_lasl_rem_res_to, sum_gen_telem_mw_from=sum_gen_telem_mw_from, sum_gen_telem_mwto=sum_gen_telem_mwto, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_base_point_non_wgr_from=sum_base_point_non_wgr_from, sum_base_point_non_wgrto=sum_base_point_non_wgrto, sum_hasl_non_wgr_from=sum_hasl_non_wgr_from, sum_hasl_non_wgrto=sum_hasl_non_wgrto, sum_lasl_non_wgr_from=sum_lasl_non_wgr_from, sum_lasl_non_wgrto=sum_lasl_non_wgrto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3910ERApi->get_data95:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3910ERApi->get_data95: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sum_base_point_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_rem_res_from** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_rem_res_to** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_rem_res_from** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_rem_res_to** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_rem_res_from** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_rem_res_to** | **float**| Format - ####.###. | [optional] 
 **sum_gen_telem_mw_from** | **float**| Format - ####.###. | [optional] 
 **sum_gen_telem_mwto** | **float**| Format - ####.###. | [optional] 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **sum_base_point_non_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_non_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_non_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_non_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_non_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_non_wgrto** | **float**| Format - ####.###. | [optional] 
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

# **get_data96**
> Report get_data96(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_base_point_non_wgr_from=sum_base_point_non_wgr_from, sum_base_point_non_wgrto=sum_base_point_non_wgrto, sum_hasl_non_wgr_from=sum_hasl_non_wgr_from, sum_hasl_non_wgrto=sum_hasl_non_wgrto, sum_lasl_non_wgr_from=sum_lasl_non_wgr_from, sum_lasl_non_wgrto=sum_lasl_non_wgrto, sum_base_point_wgr_from=sum_base_point_wgr_from, sum_base_point_wgrto=sum_base_point_wgrto, sum_hasl_wgr_from=sum_hasl_wgr_from, sum_hasl_wgrto=sum_hasl_wgrto, sum_lasl_wgr_from=sum_lasl_wgr_from, sum_lasl_wgrto=sum_lasl_wgrto, sum_base_point_rem_res_from=sum_base_point_rem_res_from, sum_base_point_rem_res_to=sum_base_point_rem_res_to, sum_hasl_rem_res_from=sum_hasl_rem_res_from, sum_hasl_rem_res_to=sum_hasl_rem_res_to, sum_lasl_rem_res_from=sum_lasl_rem_res_from, sum_lasl_rem_res_to=sum_lasl_rem_res_to, sum_gen_telem_mw_from=sum_gen_telem_mw_from, sum_gen_telem_mwto=sum_gen_telem_mwto, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Generation Summary Houston

2 Day Aggregated Generation Summary Houston

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
    api_instance = openapi_client.NP3910ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    sum_base_point_non_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_non_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_non_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_non_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_non_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_non_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_rem_res_from = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_rem_res_to = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_rem_res_from = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_rem_res_to = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_rem_res_from = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_rem_res_to = 3.4 # float | Format - ####.###. (optional)
    sum_gen_telem_mw_from = 3.4 # float | Format - ####.###. (optional)
    sum_gen_telem_mwto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Generation Summary Houston
        api_response = api_instance.get_data96(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_base_point_non_wgr_from=sum_base_point_non_wgr_from, sum_base_point_non_wgrto=sum_base_point_non_wgrto, sum_hasl_non_wgr_from=sum_hasl_non_wgr_from, sum_hasl_non_wgrto=sum_hasl_non_wgrto, sum_lasl_non_wgr_from=sum_lasl_non_wgr_from, sum_lasl_non_wgrto=sum_lasl_non_wgrto, sum_base_point_wgr_from=sum_base_point_wgr_from, sum_base_point_wgrto=sum_base_point_wgrto, sum_hasl_wgr_from=sum_hasl_wgr_from, sum_hasl_wgrto=sum_hasl_wgrto, sum_lasl_wgr_from=sum_lasl_wgr_from, sum_lasl_wgrto=sum_lasl_wgrto, sum_base_point_rem_res_from=sum_base_point_rem_res_from, sum_base_point_rem_res_to=sum_base_point_rem_res_to, sum_hasl_rem_res_from=sum_hasl_rem_res_from, sum_hasl_rem_res_to=sum_hasl_rem_res_to, sum_lasl_rem_res_from=sum_lasl_rem_res_from, sum_lasl_rem_res_to=sum_lasl_rem_res_to, sum_gen_telem_mw_from=sum_gen_telem_mw_from, sum_gen_telem_mwto=sum_gen_telem_mwto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3910ERApi->get_data96:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3910ERApi->get_data96: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **sum_base_point_non_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_non_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_non_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_non_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_non_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_non_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_rem_res_from** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_rem_res_to** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_rem_res_from** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_rem_res_to** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_rem_res_from** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_rem_res_to** | **float**| Format - ####.###. | [optional] 
 **sum_gen_telem_mw_from** | **float**| Format - ####.###. | [optional] 
 **sum_gen_telem_mwto** | **float**| Format - ####.###. | [optional] 
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

# **get_data97**
> Report get_data97(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_base_point_non_irr_from=sum_base_point_non_irr_from, sum_base_point_non_irrto=sum_base_point_non_irrto, sum_hasl_non_irr_from=sum_hasl_non_irr_from, sum_hasl_non_irrto=sum_hasl_non_irrto, sum_lasl_non_irr_from=sum_lasl_non_irr_from, sum_lasl_non_irrto=sum_lasl_non_irrto, sum_base_point_wgr_from=sum_base_point_wgr_from, sum_base_point_wgrto=sum_base_point_wgrto, sum_haslwgr_from=sum_haslwgr_from, sum_haslwgrto=sum_haslwgrto, sum_laslwgr_from=sum_laslwgr_from, sum_laslwgrto=sum_laslwgrto, sum_base_point_pvgr_from=sum_base_point_pvgr_from, sum_base_point_pvgrto=sum_base_point_pvgrto, sum_haslpvgr_from=sum_haslpvgr_from, sum_haslpvgrto=sum_haslpvgrto, sum_laslpvgr_from=sum_laslpvgr_from, sum_laslpvgrto=sum_laslpvgrto, sum_base_point_remres_from=sum_base_point_remres_from, sum_base_point_remresto=sum_base_point_remresto, sum_haslremres_from=sum_haslremres_from, sum_haslremresto=sum_haslremresto, sum_laslremres_from=sum_laslremres_from, sum_laslremresto=sum_laslremresto, sum_gen_telem_mw_from=sum_gen_telem_mw_from, sum_gen_telem_mwto=sum_gen_telem_mwto, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Generation Summary

2 Day Aggregated Generation Summary

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
    api_instance = openapi_client.NP3910ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    sum_base_point_non_irr_from = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_non_irrto = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_non_irr_from = 3.4 # float | Format - ####.###. (optional)
    sum_hasl_non_irrto = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_non_irr_from = 3.4 # float | Format - ####.###. (optional)
    sum_lasl_non_irrto = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_wgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_wgrto = 3.4 # float | Format - ####.###. (optional)
    sum_haslwgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_haslwgrto = 3.4 # float | Format - ####.###. (optional)
    sum_laslwgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_laslwgrto = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_pvgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_pvgrto = 3.4 # float | Format - ####.###. (optional)
    sum_haslpvgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_haslpvgrto = 3.4 # float | Format - ####.###. (optional)
    sum_laslpvgr_from = 3.4 # float | Format - ####.###. (optional)
    sum_laslpvgrto = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_remres_from = 3.4 # float | Format - ####.###. (optional)
    sum_base_point_remresto = 3.4 # float | Format - ####.###. (optional)
    sum_haslremres_from = 3.4 # float | Format - ####.###. (optional)
    sum_haslremresto = 3.4 # float | Format - ####.###. (optional)
    sum_laslremres_from = 3.4 # float | Format - ####.###. (optional)
    sum_laslremresto = 3.4 # float | Format - ####.###. (optional)
    sum_gen_telem_mw_from = 3.4 # float | Format - ####.###. (optional)
    sum_gen_telem_mwto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Generation Summary
        api_response = api_instance.get_data97(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_base_point_non_irr_from=sum_base_point_non_irr_from, sum_base_point_non_irrto=sum_base_point_non_irrto, sum_hasl_non_irr_from=sum_hasl_non_irr_from, sum_hasl_non_irrto=sum_hasl_non_irrto, sum_lasl_non_irr_from=sum_lasl_non_irr_from, sum_lasl_non_irrto=sum_lasl_non_irrto, sum_base_point_wgr_from=sum_base_point_wgr_from, sum_base_point_wgrto=sum_base_point_wgrto, sum_haslwgr_from=sum_haslwgr_from, sum_haslwgrto=sum_haslwgrto, sum_laslwgr_from=sum_laslwgr_from, sum_laslwgrto=sum_laslwgrto, sum_base_point_pvgr_from=sum_base_point_pvgr_from, sum_base_point_pvgrto=sum_base_point_pvgrto, sum_haslpvgr_from=sum_haslpvgr_from, sum_haslpvgrto=sum_haslpvgrto, sum_laslpvgr_from=sum_laslpvgr_from, sum_laslpvgrto=sum_laslpvgrto, sum_base_point_remres_from=sum_base_point_remres_from, sum_base_point_remresto=sum_base_point_remresto, sum_haslremres_from=sum_haslremres_from, sum_haslremresto=sum_haslremresto, sum_laslremres_from=sum_laslremres_from, sum_laslremresto=sum_laslremresto, sum_gen_telem_mw_from=sum_gen_telem_mw_from, sum_gen_telem_mwto=sum_gen_telem_mwto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3910ERApi->get_data97:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3910ERApi->get_data97: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **sum_base_point_non_irr_from** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_non_irrto** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_non_irr_from** | **float**| Format - ####.###. | [optional] 
 **sum_hasl_non_irrto** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_non_irr_from** | **float**| Format - ####.###. | [optional] 
 **sum_lasl_non_irrto** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_wgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_wgrto** | **float**| Format - ####.###. | [optional] 
 **sum_haslwgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_haslwgrto** | **float**| Format - ####.###. | [optional] 
 **sum_laslwgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_laslwgrto** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_pvgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_pvgrto** | **float**| Format - ####.###. | [optional] 
 **sum_haslpvgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_haslpvgrto** | **float**| Format - ####.###. | [optional] 
 **sum_laslpvgr_from** | **float**| Format - ####.###. | [optional] 
 **sum_laslpvgrto** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_remres_from** | **float**| Format - ####.###. | [optional] 
 **sum_base_point_remresto** | **float**| Format - ####.###. | [optional] 
 **sum_haslremres_from** | **float**| Format - ####.###. | [optional] 
 **sum_haslremresto** | **float**| Format - ####.###. | [optional] 
 **sum_laslremres_from** | **float**| Format - ####.###. | [optional] 
 **sum_laslremresto** | **float**| Format - ####.###. | [optional] 
 **sum_gen_telem_mw_from** | **float**| Format - ####.###. | [optional] 
 **sum_gen_telem_mwto** | **float**| Format - ####.###. | [optional] 
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

# **get_data98**
> Report get_data98(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_telem_dsr_load_from=sum_telem_dsr_load_from, sum_telem_dsr_load_to=sum_telem_dsr_load_to, sum_telem_dsr_gen_from=sum_telem_dsr_gen_from, sum_telem_dsr_gen_to=sum_telem_dsr_gen_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated DSR Loads

2 Day Aggregated DSR Loads

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
    api_instance = openapi_client.NP3910ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    sum_telem_dsr_load_from = 3.4 # float | Format - ####.###. (optional)
    sum_telem_dsr_load_to = 3.4 # float | Format - ####.###. (optional)
    sum_telem_dsr_gen_from = 3.4 # float | Format - ####.###. (optional)
    sum_telem_dsr_gen_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated DSR Loads
        api_response = api_instance.get_data98(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, sum_telem_dsr_load_from=sum_telem_dsr_load_from, sum_telem_dsr_load_to=sum_telem_dsr_load_to, sum_telem_dsr_gen_from=sum_telem_dsr_gen_from, sum_telem_dsr_gen_to=sum_telem_dsr_gen_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3910ERApi->get_data98:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3910ERApi->get_data98: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **sum_telem_dsr_load_from** | **float**| Format - ####.###. | [optional] 
 **sum_telem_dsr_load_to** | **float**| Format - ####.###. | [optional] 
 **sum_telem_dsr_gen_from** | **float**| Format - ####.###. | [optional] 
 **sum_telem_dsr_gen_to** | **float**| Format - ####.###. | [optional] 
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

