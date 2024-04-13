# openapi_client.NP4745CDApi

All URIs are relative to *https://api.ercot.com/api/public-reports*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data9**](NP4745CDApi.md#get_data9) | **GET** /np4-745-cd/spp_hrly_actual_fcast_geo | Solar Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region


# **get_data9**
> Report get_data9(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, posted_datetime_from=posted_datetime_from, posted_datetime_to=posted_datetime_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, gen_system_wide_from=gen_system_wide_from, gen_system_wide_to=gen_system_wide_to, cophsl_system_wide_from=cophsl_system_wide_from, cophsl_system_wide_to=cophsl_system_wide_to, stppf_system_wide_from=stppf_system_wide_from, stppf_system_wide_to=stppf_system_wide_to, pvgrpp_system_wide_from=pvgrpp_system_wide_from, pvgrpp_system_wide_to=pvgrpp_system_wide_to, gen_center_west_from=gen_center_west_from, gen_center_west_to=gen_center_west_to, cophsl_center_west_from=cophsl_center_west_from, cophsl_center_west_to=cophsl_center_west_to, stppf_center_west_from=stppf_center_west_from, stppf_center_west_to=stppf_center_west_to, pvgrpp_center_west_from=pvgrpp_center_west_from, pvgrpp_center_west_to=pvgrpp_center_west_to, gen_north_west_from=gen_north_west_from, gen_north_west_to=gen_north_west_to, cophsl_north_west_from=cophsl_north_west_from, cophsl_north_west_to=cophsl_north_west_to, stppf_north_west_from=stppf_north_west_from, stppf_north_west_to=stppf_north_west_to, pvgrpp_north_west_from=pvgrpp_north_west_from, pvgrpp_north_west_to=pvgrpp_north_west_to, gen_far_west_from=gen_far_west_from, gen_far_west_to=gen_far_west_to, cophsl_far_west_from=cophsl_far_west_from, cophsl_far_west_to=cophsl_far_west_to, stppf_far_west_from=stppf_far_west_from, stppf_far_west_to=stppf_far_west_to, pvgrpp_far_west_from=pvgrpp_far_west_from, pvgrpp_far_west_to=pvgrpp_far_west_to, gen_far_east_from=gen_far_east_from, gen_far_east_to=gen_far_east_to, cophsl_far_east_from=cophsl_far_east_from, cophsl_far_east_to=cophsl_far_east_to, stppf_far_east_from=stppf_far_east_from, stppf_far_east_to=stppf_far_east_to, pvgrpp_far_east_from=pvgrpp_far_east_from, pvgrpp_far_east_to=pvgrpp_far_east_to, gen_south_east_from=gen_south_east_from, gen_south_east_to=gen_south_east_to, cophsl_south_east_from=cophsl_south_east_from, cophsl_south_east_to=cophsl_south_east_to, stppf_south_east_from=stppf_south_east_from, stppf_south_east_to=stppf_south_east_to, pvgrpp_south_east_from=pvgrpp_south_east_from, pvgrpp_south_east_to=pvgrpp_south_east_to, gen_center_east_from=gen_center_east_from, gen_center_east_to=gen_center_east_to, cophsl_center_east_from=cophsl_center_east_from, cophsl_center_east_to=cophsl_center_east_to, stppf_center_east_from=stppf_center_east_from, stppf_center_east_to=stppf_center_east_to, pvgrpp_center_east_from=pvgrpp_center_east_from, pvgrpp_center_east_to=pvgrpp_center_east_to, dst_flag=dst_flag, page=page, size=size, sort=sort, dir=dir)

Solar Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region

Solar Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region

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
    api_instance = openapi_client.NP4745CDApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    posted_datetime_from = 'posted_datetime_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    posted_datetime_to = 'posted_datetime_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    gen_system_wide_from = 3.4 # float | Format - ####.###. (optional)
    gen_system_wide_to = 3.4 # float | Format - ####.###. (optional)
    cophsl_system_wide_from = 3.4 # float | Format - ####.###. (optional)
    cophsl_system_wide_to = 3.4 # float | Format - ####.###. (optional)
    stppf_system_wide_from = 3.4 # float | Format - ####.###. (optional)
    stppf_system_wide_to = 3.4 # float | Format - ####.###. (optional)
    pvgrpp_system_wide_from = 3.4 # float | Format - ####.###. (optional)
    pvgrpp_system_wide_to = 3.4 # float | Format - ####.###. (optional)
    gen_center_west_from = 3.4 # float | Format - ####.###. (optional)
    gen_center_west_to = 3.4 # float | Format - ####.###. (optional)
    cophsl_center_west_from = 3.4 # float | Format - ####.###. (optional)
    cophsl_center_west_to = 3.4 # float | Format - ####.###. (optional)
    stppf_center_west_from = 3.4 # float | Format - ####.###. (optional)
    stppf_center_west_to = 3.4 # float | Format - ####.###. (optional)
    pvgrpp_center_west_from = 3.4 # float | Format - ####.###. (optional)
    pvgrpp_center_west_to = 3.4 # float | Format - ####.###. (optional)
    gen_north_west_from = 3.4 # float | Format - ####.###. (optional)
    gen_north_west_to = 3.4 # float | Format - ####.###. (optional)
    cophsl_north_west_from = 3.4 # float | Format - ####.###. (optional)
    cophsl_north_west_to = 3.4 # float | Format - ####.###. (optional)
    stppf_north_west_from = 3.4 # float | Format - ####.###. (optional)
    stppf_north_west_to = 3.4 # float | Format - ####.###. (optional)
    pvgrpp_north_west_from = 3.4 # float | Format - ####.###. (optional)
    pvgrpp_north_west_to = 3.4 # float | Format - ####.###. (optional)
    gen_far_west_from = 3.4 # float | Format - ####.###. (optional)
    gen_far_west_to = 3.4 # float | Format - ####.###. (optional)
    cophsl_far_west_from = 3.4 # float | Format - ####.###. (optional)
    cophsl_far_west_to = 3.4 # float | Format - ####.###. (optional)
    stppf_far_west_from = 3.4 # float | Format - ####.###. (optional)
    stppf_far_west_to = 3.4 # float | Format - ####.###. (optional)
    pvgrpp_far_west_from = 3.4 # float | Format - ####.###. (optional)
    pvgrpp_far_west_to = 3.4 # float | Format - ####.###. (optional)
    gen_far_east_from = 3.4 # float | Format - ####.###. (optional)
    gen_far_east_to = 3.4 # float | Format - ####.###. (optional)
    cophsl_far_east_from = 3.4 # float | Format - ####.###. (optional)
    cophsl_far_east_to = 3.4 # float | Format - ####.###. (optional)
    stppf_far_east_from = 3.4 # float | Format - ####.###. (optional)
    stppf_far_east_to = 3.4 # float | Format - ####.###. (optional)
    pvgrpp_far_east_from = 3.4 # float | Format - ####.###. (optional)
    pvgrpp_far_east_to = 3.4 # float | Format - ####.###. (optional)
    gen_south_east_from = 3.4 # float | Format - ####.###. (optional)
    gen_south_east_to = 3.4 # float | Format - ####.###. (optional)
    cophsl_south_east_from = 3.4 # float | Format - ####.###. (optional)
    cophsl_south_east_to = 3.4 # float | Format - ####.###. (optional)
    stppf_south_east_from = 3.4 # float | Format - ####.###. (optional)
    stppf_south_east_to = 3.4 # float | Format - ####.###. (optional)
    pvgrpp_south_east_from = 3.4 # float | Format - ####.###. (optional)
    pvgrpp_south_east_to = 3.4 # float | Format - ####.###. (optional)
    gen_center_east_from = 3.4 # float | Format - ####.###. (optional)
    gen_center_east_to = 3.4 # float | Format - ####.###. (optional)
    cophsl_center_east_from = 3.4 # float | Format - ####.###. (optional)
    cophsl_center_east_to = 3.4 # float | Format - ####.###. (optional)
    stppf_center_east_from = 3.4 # float | Format - ####.###. (optional)
    stppf_center_east_to = 3.4 # float | Format - ####.###. (optional)
    pvgrpp_center_east_from = 3.4 # float | Format - ####.###. (optional)
    pvgrpp_center_east_to = 3.4 # float | Format - ####.###. (optional)
    dst_flag = True # bool | Format - true | false. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # Solar Power Production - Hourly Averaged Actual and Forecasted Values by Geographical Region
        api_response = api_instance.get_data9(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, posted_datetime_from=posted_datetime_from, posted_datetime_to=posted_datetime_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, gen_system_wide_from=gen_system_wide_from, gen_system_wide_to=gen_system_wide_to, cophsl_system_wide_from=cophsl_system_wide_from, cophsl_system_wide_to=cophsl_system_wide_to, stppf_system_wide_from=stppf_system_wide_from, stppf_system_wide_to=stppf_system_wide_to, pvgrpp_system_wide_from=pvgrpp_system_wide_from, pvgrpp_system_wide_to=pvgrpp_system_wide_to, gen_center_west_from=gen_center_west_from, gen_center_west_to=gen_center_west_to, cophsl_center_west_from=cophsl_center_west_from, cophsl_center_west_to=cophsl_center_west_to, stppf_center_west_from=stppf_center_west_from, stppf_center_west_to=stppf_center_west_to, pvgrpp_center_west_from=pvgrpp_center_west_from, pvgrpp_center_west_to=pvgrpp_center_west_to, gen_north_west_from=gen_north_west_from, gen_north_west_to=gen_north_west_to, cophsl_north_west_from=cophsl_north_west_from, cophsl_north_west_to=cophsl_north_west_to, stppf_north_west_from=stppf_north_west_from, stppf_north_west_to=stppf_north_west_to, pvgrpp_north_west_from=pvgrpp_north_west_from, pvgrpp_north_west_to=pvgrpp_north_west_to, gen_far_west_from=gen_far_west_from, gen_far_west_to=gen_far_west_to, cophsl_far_west_from=cophsl_far_west_from, cophsl_far_west_to=cophsl_far_west_to, stppf_far_west_from=stppf_far_west_from, stppf_far_west_to=stppf_far_west_to, pvgrpp_far_west_from=pvgrpp_far_west_from, pvgrpp_far_west_to=pvgrpp_far_west_to, gen_far_east_from=gen_far_east_from, gen_far_east_to=gen_far_east_to, cophsl_far_east_from=cophsl_far_east_from, cophsl_far_east_to=cophsl_far_east_to, stppf_far_east_from=stppf_far_east_from, stppf_far_east_to=stppf_far_east_to, pvgrpp_far_east_from=pvgrpp_far_east_from, pvgrpp_far_east_to=pvgrpp_far_east_to, gen_south_east_from=gen_south_east_from, gen_south_east_to=gen_south_east_to, cophsl_south_east_from=cophsl_south_east_from, cophsl_south_east_to=cophsl_south_east_to, stppf_south_east_from=stppf_south_east_from, stppf_south_east_to=stppf_south_east_to, pvgrpp_south_east_from=pvgrpp_south_east_from, pvgrpp_south_east_to=pvgrpp_south_east_to, gen_center_east_from=gen_center_east_from, gen_center_east_to=gen_center_east_to, cophsl_center_east_from=cophsl_center_east_from, cophsl_center_east_to=cophsl_center_east_to, stppf_center_east_from=stppf_center_east_from, stppf_center_east_to=stppf_center_east_to, pvgrpp_center_east_from=pvgrpp_center_east_from, pvgrpp_center_east_to=pvgrpp_center_east_to, dst_flag=dst_flag, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP4745CDApi->get_data9:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP4745CDApi->get_data9: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **posted_datetime_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **posted_datetime_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **gen_system_wide_from** | **float**| Format - ####.###. | [optional] 
 **gen_system_wide_to** | **float**| Format - ####.###. | [optional] 
 **cophsl_system_wide_from** | **float**| Format - ####.###. | [optional] 
 **cophsl_system_wide_to** | **float**| Format - ####.###. | [optional] 
 **stppf_system_wide_from** | **float**| Format - ####.###. | [optional] 
 **stppf_system_wide_to** | **float**| Format - ####.###. | [optional] 
 **pvgrpp_system_wide_from** | **float**| Format - ####.###. | [optional] 
 **pvgrpp_system_wide_to** | **float**| Format - ####.###. | [optional] 
 **gen_center_west_from** | **float**| Format - ####.###. | [optional] 
 **gen_center_west_to** | **float**| Format - ####.###. | [optional] 
 **cophsl_center_west_from** | **float**| Format - ####.###. | [optional] 
 **cophsl_center_west_to** | **float**| Format - ####.###. | [optional] 
 **stppf_center_west_from** | **float**| Format - ####.###. | [optional] 
 **stppf_center_west_to** | **float**| Format - ####.###. | [optional] 
 **pvgrpp_center_west_from** | **float**| Format - ####.###. | [optional] 
 **pvgrpp_center_west_to** | **float**| Format - ####.###. | [optional] 
 **gen_north_west_from** | **float**| Format - ####.###. | [optional] 
 **gen_north_west_to** | **float**| Format - ####.###. | [optional] 
 **cophsl_north_west_from** | **float**| Format - ####.###. | [optional] 
 **cophsl_north_west_to** | **float**| Format - ####.###. | [optional] 
 **stppf_north_west_from** | **float**| Format - ####.###. | [optional] 
 **stppf_north_west_to** | **float**| Format - ####.###. | [optional] 
 **pvgrpp_north_west_from** | **float**| Format - ####.###. | [optional] 
 **pvgrpp_north_west_to** | **float**| Format - ####.###. | [optional] 
 **gen_far_west_from** | **float**| Format - ####.###. | [optional] 
 **gen_far_west_to** | **float**| Format - ####.###. | [optional] 
 **cophsl_far_west_from** | **float**| Format - ####.###. | [optional] 
 **cophsl_far_west_to** | **float**| Format - ####.###. | [optional] 
 **stppf_far_west_from** | **float**| Format - ####.###. | [optional] 
 **stppf_far_west_to** | **float**| Format - ####.###. | [optional] 
 **pvgrpp_far_west_from** | **float**| Format - ####.###. | [optional] 
 **pvgrpp_far_west_to** | **float**| Format - ####.###. | [optional] 
 **gen_far_east_from** | **float**| Format - ####.###. | [optional] 
 **gen_far_east_to** | **float**| Format - ####.###. | [optional] 
 **cophsl_far_east_from** | **float**| Format - ####.###. | [optional] 
 **cophsl_far_east_to** | **float**| Format - ####.###. | [optional] 
 **stppf_far_east_from** | **float**| Format - ####.###. | [optional] 
 **stppf_far_east_to** | **float**| Format - ####.###. | [optional] 
 **pvgrpp_far_east_from** | **float**| Format - ####.###. | [optional] 
 **pvgrpp_far_east_to** | **float**| Format - ####.###. | [optional] 
 **gen_south_east_from** | **float**| Format - ####.###. | [optional] 
 **gen_south_east_to** | **float**| Format - ####.###. | [optional] 
 **cophsl_south_east_from** | **float**| Format - ####.###. | [optional] 
 **cophsl_south_east_to** | **float**| Format - ####.###. | [optional] 
 **stppf_south_east_from** | **float**| Format - ####.###. | [optional] 
 **stppf_south_east_to** | **float**| Format - ####.###. | [optional] 
 **pvgrpp_south_east_from** | **float**| Format - ####.###. | [optional] 
 **pvgrpp_south_east_to** | **float**| Format - ####.###. | [optional] 
 **gen_center_east_from** | **float**| Format - ####.###. | [optional] 
 **gen_center_east_to** | **float**| Format - ####.###. | [optional] 
 **cophsl_center_east_from** | **float**| Format - ####.###. | [optional] 
 **cophsl_center_east_to** | **float**| Format - ####.###. | [optional] 
 **stppf_center_east_from** | **float**| Format - ####.###. | [optional] 
 **stppf_center_east_to** | **float**| Format - ####.###. | [optional] 
 **pvgrpp_center_east_from** | **float**| Format - ####.###. | [optional] 
 **pvgrpp_center_east_to** | **float**| Format - ####.###. | [optional] 
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

