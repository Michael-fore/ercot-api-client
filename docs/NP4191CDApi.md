# openapi_client.NP4191CDApi

All URIs are relative to *https://api.ercot.com/api/public-reports*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data27**](NP4191CDApi.md#get_data27) | **GET** /np4-191-cd/dam_shadow_prices | DAM Shadow Prices


# **get_data27**
> Report get_data27(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending=hour_ending, constraint_id_from=constraint_id_from, constraint_id_to=constraint_id_to, constraint_name=constraint_name, contingency_name=contingency_name, constraint_limit_from=constraint_limit_from, constraint_limit_to=constraint_limit_to, constraint_value_from=constraint_value_from, constraint_value_to=constraint_value_to, violation_amount_from=violation_amount_from, violation_amount_to=violation_amount_to, shadow_price_from=shadow_price_from, shadow_price_to=shadow_price_to, from_station=from_station, to_station=to_station, from_stationk_v_from=from_stationk_v_from, from_stationk_vto=from_stationk_vto, to_stationk_v_from=to_stationk_v_from, to_stationk_vto=to_stationk_vto, delivery_time_from=delivery_time_from, delivery_time_to=delivery_time_to, dst_flag=dst_flag, page=page, size=size, sort=sort, dir=dir)

DAM Shadow Prices

DAM Shadow Prices

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
    api_instance = openapi_client.NP4191CDApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending = 'hour_ending_example' # str | Format - abc123. (optional)
    constraint_id_from = 56 # int | Format - ###. (optional)
    constraint_id_to = 56 # int | Format - ###. (optional)
    constraint_name = 'constraint_name_example' # str | Format - abc123. (optional)
    contingency_name = 'contingency_name_example' # str | Format - abc123. (optional)
    constraint_limit_from = 56 # int | Format - ###. (optional)
    constraint_limit_to = 56 # int | Format - ###. (optional)
    constraint_value_from = 56 # int | Format - ###. (optional)
    constraint_value_to = 56 # int | Format - ###. (optional)
    violation_amount_from = 56 # int | Format - ###. (optional)
    violation_amount_to = 56 # int | Format - ###. (optional)
    shadow_price_from = 3.4 # float | Format - ####.###. (optional)
    shadow_price_to = 3.4 # float | Format - ####.###. (optional)
    from_station = 'from_station_example' # str | Format - abc123. (optional)
    to_station = 'to_station_example' # str | Format - abc123. (optional)
    from_stationk_v_from = 3.4 # float | Format - ####.###. (optional)
    from_stationk_vto = 3.4 # float | Format - ####.###. (optional)
    to_stationk_v_from = 3.4 # float | Format - ####.###. (optional)
    to_stationk_vto = 3.4 # float | Format - ####.###. (optional)
    delivery_time_from = 'delivery_time_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    delivery_time_to = 'delivery_time_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    dst_flag = True # bool | Format - true | false. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # DAM Shadow Prices
        api_response = api_instance.get_data27(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending=hour_ending, constraint_id_from=constraint_id_from, constraint_id_to=constraint_id_to, constraint_name=constraint_name, contingency_name=contingency_name, constraint_limit_from=constraint_limit_from, constraint_limit_to=constraint_limit_to, constraint_value_from=constraint_value_from, constraint_value_to=constraint_value_to, violation_amount_from=violation_amount_from, violation_amount_to=violation_amount_to, shadow_price_from=shadow_price_from, shadow_price_to=shadow_price_to, from_station=from_station, to_station=to_station, from_stationk_v_from=from_stationk_v_from, from_stationk_vto=from_stationk_vto, to_stationk_v_from=to_stationk_v_from, to_stationk_vto=to_stationk_vto, delivery_time_from=delivery_time_from, delivery_time_to=delivery_time_to, dst_flag=dst_flag, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP4191CDApi->get_data27:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP4191CDApi->get_data27: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending** | **str**| Format - abc123. | [optional] 
 **constraint_id_from** | **int**| Format - ###. | [optional] 
 **constraint_id_to** | **int**| Format - ###. | [optional] 
 **constraint_name** | **str**| Format - abc123. | [optional] 
 **contingency_name** | **str**| Format - abc123. | [optional] 
 **constraint_limit_from** | **int**| Format - ###. | [optional] 
 **constraint_limit_to** | **int**| Format - ###. | [optional] 
 **constraint_value_from** | **int**| Format - ###. | [optional] 
 **constraint_value_to** | **int**| Format - ###. | [optional] 
 **violation_amount_from** | **int**| Format - ###. | [optional] 
 **violation_amount_to** | **int**| Format - ###. | [optional] 
 **shadow_price_from** | **float**| Format - ####.###. | [optional] 
 **shadow_price_to** | **float**| Format - ####.###. | [optional] 
 **from_station** | **str**| Format - abc123. | [optional] 
 **to_station** | **str**| Format - abc123. | [optional] 
 **from_stationk_v_from** | **float**| Format - ####.###. | [optional] 
 **from_stationk_vto** | **float**| Format - ####.###. | [optional] 
 **to_stationk_v_from** | **float**| Format - ####.###. | [optional] 
 **to_stationk_vto** | **float**| Format - ####.###. | [optional] 
 **delivery_time_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **delivery_time_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
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

