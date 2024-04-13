# openapi_client.NP3233CDApi

All URIs are relative to *https://api.ercot.com/api/public-reports*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data101**](NP3233CDApi.md#get_data101) | **GET** /np3-233-cd/hourly_res_outage_cap | Hourly Resource Outage Capacity


# **get_data101**
> Report get_data101(ocp_apim_subscription_key, operating_date_from=operating_date_from, operating_date_to=operating_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_resource_mw_zone_south_from=total_resource_mw_zone_south_from, total_resource_mw_zone_south_to=total_resource_mw_zone_south_to, total_resource_mw_zone_north_from=total_resource_mw_zone_north_from, total_resource_mw_zone_north_to=total_resource_mw_zone_north_to, total_resource_mw_zone_west_from=total_resource_mw_zone_west_from, total_resource_mw_zone_west_to=total_resource_mw_zone_west_to, total_resource_mw_zone_houston_from=total_resource_mw_zone_houston_from, total_resource_mw_zone_houston_to=total_resource_mw_zone_houston_to, total_irrmw_zone_south_from=total_irrmw_zone_south_from, total_irrmw_zone_south_to=total_irrmw_zone_south_to, total_irrmw_zone_north_from=total_irrmw_zone_north_from, total_irrmw_zone_north_to=total_irrmw_zone_north_to, total_irrmw_zone_west_from=total_irrmw_zone_west_from, total_irrmw_zone_west_to=total_irrmw_zone_west_to, total_irrmw_zone_houston_from=total_irrmw_zone_houston_from, total_irrmw_zone_houston_to=total_irrmw_zone_houston_to, total_new_equip_resource_mw_zone_south_from=total_new_equip_resource_mw_zone_south_from, total_new_equip_resource_mw_zone_south_to=total_new_equip_resource_mw_zone_south_to, total_new_equip_resource_mw_zone_north_from=total_new_equip_resource_mw_zone_north_from, total_new_equip_resource_mw_zone_north_to=total_new_equip_resource_mw_zone_north_to, total_new_equip_resource_mw_zone_west_from=total_new_equip_resource_mw_zone_west_from, total_new_equip_resource_mw_zone_west_to=total_new_equip_resource_mw_zone_west_to, total_new_equip_resource_mw_zone_houston_from=total_new_equip_resource_mw_zone_houston_from, total_new_equip_resource_mw_zone_houston_to=total_new_equip_resource_mw_zone_houston_to, posted_datetime_from=posted_datetime_from, posted_datetime_to=posted_datetime_to, page=page, size=size, sort=sort, dir=dir)

Hourly Resource Outage Capacity

Hourly Resource Outage Capacity

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
    api_instance = openapi_client.NP3233CDApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    operating_date_from = 'operating_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    operating_date_to = 'operating_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    total_resource_mw_zone_south_from = 56 # int | Format - ###. (optional)
    total_resource_mw_zone_south_to = 56 # int | Format - ###. (optional)
    total_resource_mw_zone_north_from = 56 # int | Format - ###. (optional)
    total_resource_mw_zone_north_to = 56 # int | Format - ###. (optional)
    total_resource_mw_zone_west_from = 56 # int | Format - ###. (optional)
    total_resource_mw_zone_west_to = 56 # int | Format - ###. (optional)
    total_resource_mw_zone_houston_from = 56 # int | Format - ###. (optional)
    total_resource_mw_zone_houston_to = 56 # int | Format - ###. (optional)
    total_irrmw_zone_south_from = 56 # int | Format - ###. (optional)
    total_irrmw_zone_south_to = 56 # int | Format - ###. (optional)
    total_irrmw_zone_north_from = 56 # int | Format - ###. (optional)
    total_irrmw_zone_north_to = 56 # int | Format - ###. (optional)
    total_irrmw_zone_west_from = 56 # int | Format - ###. (optional)
    total_irrmw_zone_west_to = 56 # int | Format - ###. (optional)
    total_irrmw_zone_houston_from = 56 # int | Format - ###. (optional)
    total_irrmw_zone_houston_to = 56 # int | Format - ###. (optional)
    total_new_equip_resource_mw_zone_south_from = 56 # int | Format - ###. (optional)
    total_new_equip_resource_mw_zone_south_to = 56 # int | Format - ###. (optional)
    total_new_equip_resource_mw_zone_north_from = 56 # int | Format - ###. (optional)
    total_new_equip_resource_mw_zone_north_to = 56 # int | Format - ###. (optional)
    total_new_equip_resource_mw_zone_west_from = 56 # int | Format - ###. (optional)
    total_new_equip_resource_mw_zone_west_to = 56 # int | Format - ###. (optional)
    total_new_equip_resource_mw_zone_houston_from = 56 # int | Format - ###. (optional)
    total_new_equip_resource_mw_zone_houston_to = 56 # int | Format - ###. (optional)
    posted_datetime_from = 'posted_datetime_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    posted_datetime_to = 'posted_datetime_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # Hourly Resource Outage Capacity
        api_response = api_instance.get_data101(ocp_apim_subscription_key, operating_date_from=operating_date_from, operating_date_to=operating_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_resource_mw_zone_south_from=total_resource_mw_zone_south_from, total_resource_mw_zone_south_to=total_resource_mw_zone_south_to, total_resource_mw_zone_north_from=total_resource_mw_zone_north_from, total_resource_mw_zone_north_to=total_resource_mw_zone_north_to, total_resource_mw_zone_west_from=total_resource_mw_zone_west_from, total_resource_mw_zone_west_to=total_resource_mw_zone_west_to, total_resource_mw_zone_houston_from=total_resource_mw_zone_houston_from, total_resource_mw_zone_houston_to=total_resource_mw_zone_houston_to, total_irrmw_zone_south_from=total_irrmw_zone_south_from, total_irrmw_zone_south_to=total_irrmw_zone_south_to, total_irrmw_zone_north_from=total_irrmw_zone_north_from, total_irrmw_zone_north_to=total_irrmw_zone_north_to, total_irrmw_zone_west_from=total_irrmw_zone_west_from, total_irrmw_zone_west_to=total_irrmw_zone_west_to, total_irrmw_zone_houston_from=total_irrmw_zone_houston_from, total_irrmw_zone_houston_to=total_irrmw_zone_houston_to, total_new_equip_resource_mw_zone_south_from=total_new_equip_resource_mw_zone_south_from, total_new_equip_resource_mw_zone_south_to=total_new_equip_resource_mw_zone_south_to, total_new_equip_resource_mw_zone_north_from=total_new_equip_resource_mw_zone_north_from, total_new_equip_resource_mw_zone_north_to=total_new_equip_resource_mw_zone_north_to, total_new_equip_resource_mw_zone_west_from=total_new_equip_resource_mw_zone_west_from, total_new_equip_resource_mw_zone_west_to=total_new_equip_resource_mw_zone_west_to, total_new_equip_resource_mw_zone_houston_from=total_new_equip_resource_mw_zone_houston_from, total_new_equip_resource_mw_zone_houston_to=total_new_equip_resource_mw_zone_houston_to, posted_datetime_from=posted_datetime_from, posted_datetime_to=posted_datetime_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3233CDApi->get_data101:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3233CDApi->get_data101: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **operating_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **operating_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **total_resource_mw_zone_south_from** | **int**| Format - ###. | [optional] 
 **total_resource_mw_zone_south_to** | **int**| Format - ###. | [optional] 
 **total_resource_mw_zone_north_from** | **int**| Format - ###. | [optional] 
 **total_resource_mw_zone_north_to** | **int**| Format - ###. | [optional] 
 **total_resource_mw_zone_west_from** | **int**| Format - ###. | [optional] 
 **total_resource_mw_zone_west_to** | **int**| Format - ###. | [optional] 
 **total_resource_mw_zone_houston_from** | **int**| Format - ###. | [optional] 
 **total_resource_mw_zone_houston_to** | **int**| Format - ###. | [optional] 
 **total_irrmw_zone_south_from** | **int**| Format - ###. | [optional] 
 **total_irrmw_zone_south_to** | **int**| Format - ###. | [optional] 
 **total_irrmw_zone_north_from** | **int**| Format - ###. | [optional] 
 **total_irrmw_zone_north_to** | **int**| Format - ###. | [optional] 
 **total_irrmw_zone_west_from** | **int**| Format - ###. | [optional] 
 **total_irrmw_zone_west_to** | **int**| Format - ###. | [optional] 
 **total_irrmw_zone_houston_from** | **int**| Format - ###. | [optional] 
 **total_irrmw_zone_houston_to** | **int**| Format - ###. | [optional] 
 **total_new_equip_resource_mw_zone_south_from** | **int**| Format - ###. | [optional] 
 **total_new_equip_resource_mw_zone_south_to** | **int**| Format - ###. | [optional] 
 **total_new_equip_resource_mw_zone_north_from** | **int**| Format - ###. | [optional] 
 **total_new_equip_resource_mw_zone_north_to** | **int**| Format - ###. | [optional] 
 **total_new_equip_resource_mw_zone_west_from** | **int**| Format - ###. | [optional] 
 **total_new_equip_resource_mw_zone_west_to** | **int**| Format - ###. | [optional] 
 **total_new_equip_resource_mw_zone_houston_from** | **int**| Format - ###. | [optional] 
 **total_new_equip_resource_mw_zone_houston_to** | **int**| Format - ###. | [optional] 
 **posted_datetime_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **posted_datetime_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
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

