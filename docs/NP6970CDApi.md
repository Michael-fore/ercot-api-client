# openapi_client.NP6970CDApi

All URIs are relative to *https://api.ercot.com/api/public-reports*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data**](NP6970CDApi.md#get_data) | **GET** /np6-970-cd/rtd_lmp_node_zone_hub | RTD Indicative LMPs by Resource Nodes, Load Zones and Hubs


# **get_data**
> Report get_data(ocp_apim_subscription_key, rtd_timestamp_from=rtd_timestamp_from, rtd_timestamp_to=rtd_timestamp_to, repeat_hour_flag=repeat_hour_flag, interval_id_from=interval_id_from, interval_id_to=interval_id_to, interval_ending_from=interval_ending_from, interval_ending_to=interval_ending_to, interval_repeat_hour_flag=interval_repeat_hour_flag, settlement_point=settlement_point, settlement_point_type=settlement_point_type, lmp_from=lmp_from, lmpto=lmpto, page=page, size=size, sort=sort, dir=dir)

RTD Indicative LMPs by Resource Nodes, Load Zones and Hubs

RTD Indicative LMPs by Resource Nodes, Load Zones and Hubs

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
    api_instance = openapi_client.NP6970CDApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    rtd_timestamp_from = 'rtd_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    rtd_timestamp_to = 'rtd_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    interval_id_from = 56 # int | Format - ###. (optional)
    interval_id_to = 56 # int | Format - ###. (optional)
    interval_ending_from = 'interval_ending_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    interval_ending_to = 'interval_ending_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    interval_repeat_hour_flag = True # bool | Format - true | false. (optional)
    settlement_point = 'settlement_point_example' # str | Format - abc123. (optional)
    settlement_point_type = 'settlement_point_type_example' # str | Format - abc123. (optional)
    lmp_from = 3.4 # float | Format - ####.###. (optional)
    lmpto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # RTD Indicative LMPs by Resource Nodes, Load Zones and Hubs
        api_response = api_instance.get_data(ocp_apim_subscription_key, rtd_timestamp_from=rtd_timestamp_from, rtd_timestamp_to=rtd_timestamp_to, repeat_hour_flag=repeat_hour_flag, interval_id_from=interval_id_from, interval_id_to=interval_id_to, interval_ending_from=interval_ending_from, interval_ending_to=interval_ending_to, interval_repeat_hour_flag=interval_repeat_hour_flag, settlement_point=settlement_point, settlement_point_type=settlement_point_type, lmp_from=lmp_from, lmpto=lmpto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP6970CDApi->get_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP6970CDApi->get_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **rtd_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **rtd_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **interval_id_from** | **int**| Format - ###. | [optional] 
 **interval_id_to** | **int**| Format - ###. | [optional] 
 **interval_ending_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **interval_ending_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **interval_repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **settlement_point** | **str**| Format - abc123. | [optional] 
 **settlement_point_type** | **str**| Format - abc123. | [optional] 
 **lmp_from** | **float**| Format - ####.###. | [optional] 
 **lmpto** | **float**| Format - ####.###. | [optional] 
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

