# openapi_client.NP686CDApi

All URIs are relative to *https://api.ercot.com/api/public-reports*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data2**](NP686CDApi.md#get_data2) | **GET** /np6-86-cd/shdw_prices_bnd_trns_const | SCED Shadow Prices and Binding Transmission Constraints


# **get_data2**
> Report get_data2(ocp_apim_subscription_key, from_station=from_station, to_station=to_station, from_stationk_v_from=from_stationk_v_from, from_stationk_vto=from_stationk_vto, to_stationk_v_from=to_stationk_v_from, to_stationk_vto=to_stationk_vto, cct_status=cct_status, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeated_hour_flag=repeated_hour_flag, constraint_id_from=constraint_id_from, constraint_idto=constraint_idto, constraint_name=constraint_name, contingency_name=contingency_name, shadow_price_from=shadow_price_from, shadow_price_to=shadow_price_to, max_shadow_price_from=max_shadow_price_from, max_shadow_price_to=max_shadow_price_to, limit_from=limit_from, limit_to=limit_to, value_from=value_from, value_to=value_to, violated_mw_from=violated_mw_from, violated_mwto=violated_mwto, page=page, size=size, sort=sort, dir=dir)

SCED Shadow Prices and Binding Transmission Constraints

SCED Shadow Prices and Binding Transmission Constraints

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
    api_instance = openapi_client.NP686CDApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    from_station = 'from_station_example' # str | Format - abc123. (optional)
    to_station = 'to_station_example' # str | Format - abc123. (optional)
    from_stationk_v_from = 3.4 # float | Format - ####.###. (optional)
    from_stationk_vto = 3.4 # float | Format - ####.###. (optional)
    to_stationk_v_from = 3.4 # float | Format - ####.###. (optional)
    to_stationk_vto = 3.4 # float | Format - ####.###. (optional)
    cct_status = 'cct_status_example' # str | Format - abc123. (optional)
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeated_hour_flag = True # bool | Format - true | false. (optional)
    constraint_id_from = 56 # int | Format - ###. (optional)
    constraint_idto = 56 # int | Format - ###. (optional)
    constraint_name = 'constraint_name_example' # str | Format - abc123. (optional)
    contingency_name = 'contingency_name_example' # str | Format - abc123. (optional)
    shadow_price_from = 3.4 # float | Format - ####.###. (optional)
    shadow_price_to = 3.4 # float | Format - ####.###. (optional)
    max_shadow_price_from = 3.4 # float | Format - ####.###. (optional)
    max_shadow_price_to = 3.4 # float | Format - ####.###. (optional)
    limit_from = 3.4 # float | Format - ####.###. (optional)
    limit_to = 3.4 # float | Format - ####.###. (optional)
    value_from = 3.4 # float | Format - ####.###. (optional)
    value_to = 3.4 # float | Format - ####.###. (optional)
    violated_mw_from = 3.4 # float | Format - ####.###. (optional)
    violated_mwto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # SCED Shadow Prices and Binding Transmission Constraints
        api_response = api_instance.get_data2(ocp_apim_subscription_key, from_station=from_station, to_station=to_station, from_stationk_v_from=from_stationk_v_from, from_stationk_vto=from_stationk_vto, to_stationk_v_from=to_stationk_v_from, to_stationk_vto=to_stationk_vto, cct_status=cct_status, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeated_hour_flag=repeated_hour_flag, constraint_id_from=constraint_id_from, constraint_idto=constraint_idto, constraint_name=constraint_name, contingency_name=contingency_name, shadow_price_from=shadow_price_from, shadow_price_to=shadow_price_to, max_shadow_price_from=max_shadow_price_from, max_shadow_price_to=max_shadow_price_to, limit_from=limit_from, limit_to=limit_to, value_from=value_from, value_to=value_to, violated_mw_from=violated_mw_from, violated_mwto=violated_mwto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP686CDApi->get_data2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP686CDApi->get_data2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **from_station** | **str**| Format - abc123. | [optional] 
 **to_station** | **str**| Format - abc123. | [optional] 
 **from_stationk_v_from** | **float**| Format - ####.###. | [optional] 
 **from_stationk_vto** | **float**| Format - ####.###. | [optional] 
 **to_stationk_v_from** | **float**| Format - ####.###. | [optional] 
 **to_stationk_vto** | **float**| Format - ####.###. | [optional] 
 **cct_status** | **str**| Format - abc123. | [optional] 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeated_hour_flag** | **bool**| Format - true | false. | [optional] 
 **constraint_id_from** | **int**| Format - ###. | [optional] 
 **constraint_idto** | **int**| Format - ###. | [optional] 
 **constraint_name** | **str**| Format - abc123. | [optional] 
 **contingency_name** | **str**| Format - abc123. | [optional] 
 **shadow_price_from** | **float**| Format - ####.###. | [optional] 
 **shadow_price_to** | **float**| Format - ####.###. | [optional] 
 **max_shadow_price_from** | **float**| Format - ####.###. | [optional] 
 **max_shadow_price_to** | **float**| Format - ####.###. | [optional] 
 **limit_from** | **float**| Format - ####.###. | [optional] 
 **limit_to** | **float**| Format - ####.###. | [optional] 
 **value_from** | **float**| Format - ####.###. | [optional] 
 **value_to** | **float**| Format - ####.###. | [optional] 
 **violated_mw_from** | **float**| Format - ####.###. | [optional] 
 **violated_mwto** | **float**| Format - ####.###. | [optional] 
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

