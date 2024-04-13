# openapi_client.NP4733CDApi

All URIs are relative to *https://api.ercot.com/api/public-reports*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data14**](NP4733CDApi.md#get_data14) | **GET** /np4-733-cd/wpp_actual_5min_avg_values | Wind Power Production - Actual 5-Minute Averaged Values


# **get_data14**
> Report get_data14(ocp_apim_subscription_key, interval_ending_from=interval_ending_from, interval_ending_to=interval_ending_to, posted_datetime_from=posted_datetime_from, posted_datetime_to=posted_datetime_to, system_wide_from=system_wide_from, system_wide_to=system_wide_to, lz_south_houston_from=lz_south_houston_from, lz_south_houston_to=lz_south_houston_to, lz_west_from=lz_west_from, lz_west_to=lz_west_to, lz_north_from=lz_north_from, lz_north_to=lz_north_to, dst_flag=dst_flag, page=page, size=size, sort=sort, dir=dir)

Wind Power Production - Actual 5-Minute Averaged Values

Wind Power Production - Actual 5-Minute Averaged Values

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
    api_instance = openapi_client.NP4733CDApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    interval_ending_from = 'interval_ending_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    interval_ending_to = 'interval_ending_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    posted_datetime_from = 'posted_datetime_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    posted_datetime_to = 'posted_datetime_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    system_wide_from = 3.4 # float | Format - ####.###. (optional)
    system_wide_to = 3.4 # float | Format - ####.###. (optional)
    lz_south_houston_from = 3.4 # float | Format - ####.###. (optional)
    lz_south_houston_to = 3.4 # float | Format - ####.###. (optional)
    lz_west_from = 3.4 # float | Format - ####.###. (optional)
    lz_west_to = 3.4 # float | Format - ####.###. (optional)
    lz_north_from = 3.4 # float | Format - ####.###. (optional)
    lz_north_to = 3.4 # float | Format - ####.###. (optional)
    dst_flag = True # bool | Format - true | false. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # Wind Power Production - Actual 5-Minute Averaged Values
        api_response = api_instance.get_data14(ocp_apim_subscription_key, interval_ending_from=interval_ending_from, interval_ending_to=interval_ending_to, posted_datetime_from=posted_datetime_from, posted_datetime_to=posted_datetime_to, system_wide_from=system_wide_from, system_wide_to=system_wide_to, lz_south_houston_from=lz_south_houston_from, lz_south_houston_to=lz_south_houston_to, lz_west_from=lz_west_from, lz_west_to=lz_west_to, lz_north_from=lz_north_from, lz_north_to=lz_north_to, dst_flag=dst_flag, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP4733CDApi->get_data14:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP4733CDApi->get_data14: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **interval_ending_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **interval_ending_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **posted_datetime_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **posted_datetime_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **system_wide_from** | **float**| Format - ####.###. | [optional] 
 **system_wide_to** | **float**| Format - ####.###. | [optional] 
 **lz_south_houston_from** | **float**| Format - ####.###. | [optional] 
 **lz_south_houston_to** | **float**| Format - ####.###. | [optional] 
 **lz_west_from** | **float**| Format - ####.###. | [optional] 
 **lz_west_to** | **float**| Format - ####.###. | [optional] 
 **lz_north_from** | **float**| Format - ####.###. | [optional] 
 **lz_north_to** | **float**| Format - ####.###. | [optional] 
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

