# openapi_client.NP6345CDApi

All URIs are relative to *https://api.ercot.com/api/public-reports*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data6**](NP6345CDApi.md#get_data6) | **GET** /np6-345-cd/act_sys_load_by_wzn | Actual System Load by Weather Zone


# **get_data6**
> Report get_data6(ocp_apim_subscription_key, operating_day_from=operating_day_from, operating_day_to=operating_day_to, hour_ending=hour_ending, coast_from=coast_from, coast_to=coast_to, east_from=east_from, east_to=east_to, far_west_from=far_west_from, far_west_to=far_west_to, north_from=north_from, north_to=north_to, north_c_from=north_c_from, north_cto=north_cto, southern_from=southern_from, southern_to=southern_to, south_c_from=south_c_from, south_cto=south_cto, west_from=west_from, west_to=west_to, total_from=total_from, total_to=total_to, dst_flag=dst_flag, page=page, size=size, sort=sort, dir=dir)

Actual System Load by Weather Zone

Actual System Load by Weather Zone

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
    api_instance = openapi_client.NP6345CDApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    operating_day_from = 'operating_day_from_example' # str | Format - yyyy-MM-dd. (optional)
    operating_day_to = 'operating_day_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending = 'hour_ending_example' # str | Format - abc123. (optional)
    coast_from = 3.4 # float | Format - ####.###. (optional)
    coast_to = 3.4 # float | Format - ####.###. (optional)
    east_from = 3.4 # float | Format - ####.###. (optional)
    east_to = 3.4 # float | Format - ####.###. (optional)
    far_west_from = 3.4 # float | Format - ####.###. (optional)
    far_west_to = 3.4 # float | Format - ####.###. (optional)
    north_from = 3.4 # float | Format - ####.###. (optional)
    north_to = 3.4 # float | Format - ####.###. (optional)
    north_c_from = 3.4 # float | Format - ####.###. (optional)
    north_cto = 3.4 # float | Format - ####.###. (optional)
    southern_from = 3.4 # float | Format - ####.###. (optional)
    southern_to = 3.4 # float | Format - ####.###. (optional)
    south_c_from = 3.4 # float | Format - ####.###. (optional)
    south_cto = 3.4 # float | Format - ####.###. (optional)
    west_from = 3.4 # float | Format - ####.###. (optional)
    west_to = 3.4 # float | Format - ####.###. (optional)
    total_from = 3.4 # float | Format - ####.###. (optional)
    total_to = 3.4 # float | Format - ####.###. (optional)
    dst_flag = True # bool | Format - true | false. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # Actual System Load by Weather Zone
        api_response = api_instance.get_data6(ocp_apim_subscription_key, operating_day_from=operating_day_from, operating_day_to=operating_day_to, hour_ending=hour_ending, coast_from=coast_from, coast_to=coast_to, east_from=east_from, east_to=east_to, far_west_from=far_west_from, far_west_to=far_west_to, north_from=north_from, north_to=north_to, north_c_from=north_c_from, north_cto=north_cto, southern_from=southern_from, southern_to=southern_to, south_c_from=south_c_from, south_cto=south_cto, west_from=west_from, west_to=west_to, total_from=total_from, total_to=total_to, dst_flag=dst_flag, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP6345CDApi->get_data6:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP6345CDApi->get_data6: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **operating_day_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **operating_day_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending** | **str**| Format - abc123. | [optional] 
 **coast_from** | **float**| Format - ####.###. | [optional] 
 **coast_to** | **float**| Format - ####.###. | [optional] 
 **east_from** | **float**| Format - ####.###. | [optional] 
 **east_to** | **float**| Format - ####.###. | [optional] 
 **far_west_from** | **float**| Format - ####.###. | [optional] 
 **far_west_to** | **float**| Format - ####.###. | [optional] 
 **north_from** | **float**| Format - ####.###. | [optional] 
 **north_to** | **float**| Format - ####.###. | [optional] 
 **north_c_from** | **float**| Format - ####.###. | [optional] 
 **north_cto** | **float**| Format - ####.###. | [optional] 
 **southern_from** | **float**| Format - ####.###. | [optional] 
 **southern_to** | **float**| Format - ####.###. | [optional] 
 **south_c_from** | **float**| Format - ####.###. | [optional] 
 **south_cto** | **float**| Format - ####.###. | [optional] 
 **west_from** | **float**| Format - ####.###. | [optional] 
 **west_to** | **float**| Format - ####.###. | [optional] 
 **total_from** | **float**| Format - ####.###. | [optional] 
 **total_to** | **float**| Format - ####.###. | [optional] 
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

