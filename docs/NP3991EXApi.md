# openapi_client.NP3991EXApi

All URIs are relative to *https://api.ercot.com/api/public-reports*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data33**](NP3991EXApi.md#get_data33) | **GET** /np3-991-ex/60_cop_all_updates | 60-Day COP All Updates


# **get_data33**
> Report get_data33(ocp_apim_subscription_key, cancel_flag=cancel_flag, update_time_from=update_time_from, update_time_to=update_time_to, submit_time_from=submit_time_from, submit_time_to=submit_time_to, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, qse_name=qse_name, resource_name=resource_name, hour_ending=hour_ending, status=status, high_sustained_limit_from=high_sustained_limit_from, high_sustained_limit_to=high_sustained_limit_to, low_sustained_limit_from=low_sustained_limit_from, low_sustained_limit_to=low_sustained_limit_to, high_emergency_limit_from=high_emergency_limit_from, high_emergency_limit_to=high_emergency_limit_to, low_emergency_limit_from=low_emergency_limit_from, low_emergency_limit_to=low_emergency_limit_to, regup_from=regup_from, regupto=regupto, regdn_from=regdn_from, regdnto=regdnto, rrspfr_from=rrspfr_from, rrspfrto=rrspfrto, rrsffr_from=rrsffr_from, rrsffrto=rrsffrto, rrsufr_from=rrsufr_from, rrsufrto=rrsufrto, nspin_from=nspin_from, nspinto=nspinto, page=page, size=size, sort=sort, dir=dir)

60-Day COP All Updates

60-Day COP All Updates

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
    api_instance = openapi_client.NP3991EXApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    cancel_flag = True # bool | Format - true | false. (optional)
    update_time_from = 'update_time_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    update_time_to = 'update_time_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    submit_time_from = 'submit_time_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    submit_time_to = 'submit_time_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    resource_name = 'resource_name_example' # str | Format - abc123. (optional)
    hour_ending = 'hour_ending_example' # str | Format - abc123. (optional)
    status = 'status_example' # str | Format - abc123. (optional)
    high_sustained_limit_from = 3.4 # float | Format - ####.###. (optional)
    high_sustained_limit_to = 3.4 # float | Format - ####.###. (optional)
    low_sustained_limit_from = 3.4 # float | Format - ####.###. (optional)
    low_sustained_limit_to = 3.4 # float | Format - ####.###. (optional)
    high_emergency_limit_from = 3.4 # float | Format - ####.###. (optional)
    high_emergency_limit_to = 3.4 # float | Format - ####.###. (optional)
    low_emergency_limit_from = 3.4 # float | Format - ####.###. (optional)
    low_emergency_limit_to = 3.4 # float | Format - ####.###. (optional)
    regup_from = 3.4 # float | Format - ####.###. (optional)
    regupto = 3.4 # float | Format - ####.###. (optional)
    regdn_from = 3.4 # float | Format - ####.###. (optional)
    regdnto = 3.4 # float | Format - ####.###. (optional)
    rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    rrspfrto = 3.4 # float | Format - ####.###. (optional)
    rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    rrsffrto = 3.4 # float | Format - ####.###. (optional)
    rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    rrsufrto = 3.4 # float | Format - ####.###. (optional)
    nspin_from = 3.4 # float | Format - ####.###. (optional)
    nspinto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60-Day COP All Updates
        api_response = api_instance.get_data33(ocp_apim_subscription_key, cancel_flag=cancel_flag, update_time_from=update_time_from, update_time_to=update_time_to, submit_time_from=submit_time_from, submit_time_to=submit_time_to, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, qse_name=qse_name, resource_name=resource_name, hour_ending=hour_ending, status=status, high_sustained_limit_from=high_sustained_limit_from, high_sustained_limit_to=high_sustained_limit_to, low_sustained_limit_from=low_sustained_limit_from, low_sustained_limit_to=low_sustained_limit_to, high_emergency_limit_from=high_emergency_limit_from, high_emergency_limit_to=high_emergency_limit_to, low_emergency_limit_from=low_emergency_limit_from, low_emergency_limit_to=low_emergency_limit_to, regup_from=regup_from, regupto=regupto, regdn_from=regdn_from, regdnto=regdnto, rrspfr_from=rrspfr_from, rrspfrto=rrspfrto, rrsffr_from=rrsffr_from, rrsffrto=rrsffrto, rrsufr_from=rrsufr_from, rrsufrto=rrsufrto, nspin_from=nspin_from, nspinto=nspinto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3991EXApi->get_data33:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3991EXApi->get_data33: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **cancel_flag** | **bool**| Format - true | false. | [optional] 
 **update_time_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **update_time_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **submit_time_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **submit_time_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **qse_name** | **str**| Format - abc123. | [optional] 
 **resource_name** | **str**| Format - abc123. | [optional] 
 **hour_ending** | **str**| Format - abc123. | [optional] 
 **status** | **str**| Format - abc123. | [optional] 
 **high_sustained_limit_from** | **float**| Format - ####.###. | [optional] 
 **high_sustained_limit_to** | **float**| Format - ####.###. | [optional] 
 **low_sustained_limit_from** | **float**| Format - ####.###. | [optional] 
 **low_sustained_limit_to** | **float**| Format - ####.###. | [optional] 
 **high_emergency_limit_from** | **float**| Format - ####.###. | [optional] 
 **high_emergency_limit_to** | **float**| Format - ####.###. | [optional] 
 **low_emergency_limit_from** | **float**| Format - ####.###. | [optional] 
 **low_emergency_limit_to** | **float**| Format - ####.###. | [optional] 
 **regup_from** | **float**| Format - ####.###. | [optional] 
 **regupto** | **float**| Format - ####.###. | [optional] 
 **regdn_from** | **float**| Format - ####.###. | [optional] 
 **regdnto** | **float**| Format - ####.###. | [optional] 
 **rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **rrspfrto** | **float**| Format - ####.###. | [optional] 
 **rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **rrsffrto** | **float**| Format - ####.###. | [optional] 
 **rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **rrsufrto** | **float**| Format - ####.###. | [optional] 
 **nspin_from** | **float**| Format - ####.###. | [optional] 
 **nspinto** | **float**| Format - ####.###. | [optional] 
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

