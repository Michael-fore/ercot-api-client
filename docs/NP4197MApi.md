# openapi_client.NP4197MApi

All URIs are relative to *https://api.ercot.com/api/public-reports*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data18**](NP4197MApi.md#get_data18) | **GET** /np4-197-m/rtm_price_corrections_spp | RTM Price Corrections for SPP
[**get_data19**](NP4197MApi.md#get_data19) | **GET** /np4-197-m/rtm_price_corrections_splmp | RTM Price Corrections SP LMP
[**get_data20**](NP4197MApi.md#get_data20) | **GET** /np4-197-m/rtm_price_corrections_sogprice | RTM Price Corrections for SOG Price
[**get_data21**](NP4197MApi.md#get_data21) | **GET** /np4-197-m/rtm_price_corrections_soglmp | RTM Price Corrections for SOG LMP
[**get_data22**](NP4197MApi.md#get_data22) | **GET** /np4-197-m/rtm_price_corrections_shadow | RTM Price Corrections for Shadow Prices
[**get_data23**](NP4197MApi.md#get_data23) | **GET** /np4-197-m/rtm_price_corrections_eblmp | RTM Price Corrections for EB LMP


# **get_data18**
> Report get_data18(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, delivery_hour_from=delivery_hour_from, delivery_hour_to=delivery_hour_to, delivery_interval_from=delivery_interval_from, delivery_interval_to=delivery_interval_to, settlement_point_name=settlement_point_name, settlement_point_type=settlement_point_type, spp_original_from=spp_original_from, spp_original_to=spp_original_to, spp_corrected_from=spp_corrected_from, spp_corrected_to=spp_corrected_to, price_correction_time_from=price_correction_time_from, price_correction_time_to=price_correction_time_to, dst_flag=dst_flag, page=page, size=size, sort=sort, dir=dir)

RTM Price Corrections for SPP

RTM Price Corrections for SPP

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
    api_instance = openapi_client.NP4197MApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_hour_from = 56 # int | Format - ###. (optional)
    delivery_hour_to = 56 # int | Format - ###. (optional)
    delivery_interval_from = 56 # int | Format - ###. (optional)
    delivery_interval_to = 56 # int | Format - ###. (optional)
    settlement_point_name = 'settlement_point_name_example' # str | Format - abc123. (optional)
    settlement_point_type = 'settlement_point_type_example' # str | Format - abc123. (optional)
    spp_original_from = 3.4 # float | Format - ####.###. (optional)
    spp_original_to = 3.4 # float | Format - ####.###. (optional)
    spp_corrected_from = 3.4 # float | Format - ####.###. (optional)
    spp_corrected_to = 3.4 # float | Format - ####.###. (optional)
    price_correction_time_from = 'price_correction_time_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    price_correction_time_to = 'price_correction_time_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    dst_flag = True # bool | Format - true | false. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # RTM Price Corrections for SPP
        api_response = api_instance.get_data18(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, delivery_hour_from=delivery_hour_from, delivery_hour_to=delivery_hour_to, delivery_interval_from=delivery_interval_from, delivery_interval_to=delivery_interval_to, settlement_point_name=settlement_point_name, settlement_point_type=settlement_point_type, spp_original_from=spp_original_from, spp_original_to=spp_original_to, spp_corrected_from=spp_corrected_from, spp_corrected_to=spp_corrected_to, price_correction_time_from=price_correction_time_from, price_correction_time_to=price_correction_time_to, dst_flag=dst_flag, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP4197MApi->get_data18:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP4197MApi->get_data18: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_hour_from** | **int**| Format - ###. | [optional] 
 **delivery_hour_to** | **int**| Format - ###. | [optional] 
 **delivery_interval_from** | **int**| Format - ###. | [optional] 
 **delivery_interval_to** | **int**| Format - ###. | [optional] 
 **settlement_point_name** | **str**| Format - abc123. | [optional] 
 **settlement_point_type** | **str**| Format - abc123. | [optional] 
 **spp_original_from** | **float**| Format - ####.###. | [optional] 
 **spp_original_to** | **float**| Format - ####.###. | [optional] 
 **spp_corrected_from** | **float**| Format - ####.###. | [optional] 
 **spp_corrected_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data19**
> Report get_data19(ocp_apim_subscription_key, settlement_point_name=settlement_point_name, lmp_original_from=lmp_original_from, lmp_original_to=lmp_original_to, lmp_corrected_from=lmp_corrected_from, lmp_corrected_to=lmp_corrected_to, price_correction_time_from=price_correction_time_from, price_correction_time_to=price_correction_time_to, dst_flag=dst_flag, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, page=page, size=size, sort=sort, dir=dir)

RTM Price Corrections SP LMP

RTM Price Corrections SP LMP

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
    api_instance = openapi_client.NP4197MApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    settlement_point_name = 'settlement_point_name_example' # str | Format - abc123. (optional)
    lmp_original_from = 3.4 # float | Format - ####.###. (optional)
    lmp_original_to = 3.4 # float | Format - ####.###. (optional)
    lmp_corrected_from = 3.4 # float | Format - ####.###. (optional)
    lmp_corrected_to = 3.4 # float | Format - ####.###. (optional)
    price_correction_time_from = 'price_correction_time_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    price_correction_time_to = 'price_correction_time_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    dst_flag = True # bool | Format - true | false. (optional)
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # RTM Price Corrections SP LMP
        api_response = api_instance.get_data19(ocp_apim_subscription_key, settlement_point_name=settlement_point_name, lmp_original_from=lmp_original_from, lmp_original_to=lmp_original_to, lmp_corrected_from=lmp_corrected_from, lmp_corrected_to=lmp_corrected_to, price_correction_time_from=price_correction_time_from, price_correction_time_to=price_correction_time_to, dst_flag=dst_flag, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP4197MApi->get_data19:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP4197MApi->get_data19: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **settlement_point_name** | **str**| Format - abc123. | [optional] 
 **lmp_original_from** | **float**| Format - ####.###. | [optional] 
 **lmp_original_to** | **float**| Format - ####.###. | [optional] 
 **lmp_corrected_from** | **float**| Format - ####.###. | [optional] 
 **lmp_corrected_to** | **float**| Format - ####.###. | [optional] 
 **price_correction_time_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **price_correction_time_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **dst_flag** | **bool**| Format - true | false. | [optional] 
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

# **get_data20**
> Report get_data20(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, delivery_hour_from=delivery_hour_from, delivery_hour_to=delivery_hour_to, delivery_interval_from=delivery_interval_from, delivery_interval_to=delivery_interval_to, resource_type=resource_type, resource_name=resource_name, meter_name=meter_name, price_original_from=price_original_from, price_original_to=price_original_to, price_corrected_from=price_corrected_from, price_corrected_to=price_corrected_to, price_correction_time_from=price_correction_time_from, price_correction_time_to=price_correction_time_to, dst_flag=dst_flag, page=page, size=size, sort=sort, dir=dir)

RTM Price Corrections for SOG Price

RTM Price Corrections for SOG Price

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
    api_instance = openapi_client.NP4197MApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_hour_from = 56 # int | Format - ###. (optional)
    delivery_hour_to = 56 # int | Format - ###. (optional)
    delivery_interval_from = 56 # int | Format - ###. (optional)
    delivery_interval_to = 56 # int | Format - ###. (optional)
    resource_type = 'resource_type_example' # str | Format - abc123. (optional)
    resource_name = 'resource_name_example' # str | Format - abc123. (optional)
    meter_name = 'meter_name_example' # str | Format - abc123. (optional)
    price_original_from = 3.4 # float | Format - ####.###. (optional)
    price_original_to = 3.4 # float | Format - ####.###. (optional)
    price_corrected_from = 3.4 # float | Format - ####.###. (optional)
    price_corrected_to = 3.4 # float | Format - ####.###. (optional)
    price_correction_time_from = 'price_correction_time_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    price_correction_time_to = 'price_correction_time_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    dst_flag = True # bool | Format - true | false. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # RTM Price Corrections for SOG Price
        api_response = api_instance.get_data20(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, delivery_hour_from=delivery_hour_from, delivery_hour_to=delivery_hour_to, delivery_interval_from=delivery_interval_from, delivery_interval_to=delivery_interval_to, resource_type=resource_type, resource_name=resource_name, meter_name=meter_name, price_original_from=price_original_from, price_original_to=price_original_to, price_corrected_from=price_corrected_from, price_corrected_to=price_corrected_to, price_correction_time_from=price_correction_time_from, price_correction_time_to=price_correction_time_to, dst_flag=dst_flag, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP4197MApi->get_data20:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP4197MApi->get_data20: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_hour_from** | **int**| Format - ###. | [optional] 
 **delivery_hour_to** | **int**| Format - ###. | [optional] 
 **delivery_interval_from** | **int**| Format - ###. | [optional] 
 **delivery_interval_to** | **int**| Format - ###. | [optional] 
 **resource_type** | **str**| Format - abc123. | [optional] 
 **resource_name** | **str**| Format - abc123. | [optional] 
 **meter_name** | **str**| Format - abc123. | [optional] 
 **price_original_from** | **float**| Format - ####.###. | [optional] 
 **price_original_to** | **float**| Format - ####.###. | [optional] 
 **price_corrected_from** | **float**| Format - ####.###. | [optional] 
 **price_corrected_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data21**
> Report get_data21(ocp_apim_subscription_key, dst_flag=dst_flag, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, resource_type=resource_type, resource_name=resource_name, meter_name=meter_name, meter_lmp_original_from=meter_lmp_original_from, meter_lmp_original_to=meter_lmp_original_to, meter_lmp_corrected_from=meter_lmp_corrected_from, meter_lmp_corrected_to=meter_lmp_corrected_to, rtorpa_original_from=rtorpa_original_from, rtorpa_original_to=rtorpa_original_to, rtorpa_corrected_from=rtorpa_corrected_from, rtorpa_corrected_to=rtorpa_corrected_to, rtordpa_original_from=rtordpa_original_from, rtordpa_original_to=rtordpa_original_to, rtordpa_corrected_from=rtordpa_corrected_from, rtordpa_corrected_to=rtordpa_corrected_to, final_lmp_original_from=final_lmp_original_from, final_lmp_original_to=final_lmp_original_to, final_lmp_corrected_from=final_lmp_corrected_from, final_lmp_corrected_to=final_lmp_corrected_to, price_correction_time_from=price_correction_time_from, price_correction_time_to=price_correction_time_to, page=page, size=size, sort=sort, dir=dir)

RTM Price Corrections for SOG LMP

RTM Price Corrections for SOG LMP

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
    api_instance = openapi_client.NP4197MApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    dst_flag = True # bool | Format - true | false. (optional)
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    resource_type = 'resource_type_example' # str | Format - abc123. (optional)
    resource_name = 'resource_name_example' # str | Format - abc123. (optional)
    meter_name = 'meter_name_example' # str | Format - abc123. (optional)
    meter_lmp_original_from = 3.4 # float | Format - ####.###. (optional)
    meter_lmp_original_to = 3.4 # float | Format - ####.###. (optional)
    meter_lmp_corrected_from = 3.4 # float | Format - ####.###. (optional)
    meter_lmp_corrected_to = 3.4 # float | Format - ####.###. (optional)
    rtorpa_original_from = 3.4 # float | Format - ####.###. (optional)
    rtorpa_original_to = 3.4 # float | Format - ####.###. (optional)
    rtorpa_corrected_from = 3.4 # float | Format - ####.###. (optional)
    rtorpa_corrected_to = 3.4 # float | Format - ####.###. (optional)
    rtordpa_original_from = 3.4 # float | Format - ####.###. (optional)
    rtordpa_original_to = 3.4 # float | Format - ####.###. (optional)
    rtordpa_corrected_from = 3.4 # float | Format - ####.###. (optional)
    rtordpa_corrected_to = 3.4 # float | Format - ####.###. (optional)
    final_lmp_original_from = 3.4 # float | Format - ####.###. (optional)
    final_lmp_original_to = 3.4 # float | Format - ####.###. (optional)
    final_lmp_corrected_from = 3.4 # float | Format - ####.###. (optional)
    final_lmp_corrected_to = 3.4 # float | Format - ####.###. (optional)
    price_correction_time_from = 'price_correction_time_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    price_correction_time_to = 'price_correction_time_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # RTM Price Corrections for SOG LMP
        api_response = api_instance.get_data21(ocp_apim_subscription_key, dst_flag=dst_flag, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, resource_type=resource_type, resource_name=resource_name, meter_name=meter_name, meter_lmp_original_from=meter_lmp_original_from, meter_lmp_original_to=meter_lmp_original_to, meter_lmp_corrected_from=meter_lmp_corrected_from, meter_lmp_corrected_to=meter_lmp_corrected_to, rtorpa_original_from=rtorpa_original_from, rtorpa_original_to=rtorpa_original_to, rtorpa_corrected_from=rtorpa_corrected_from, rtorpa_corrected_to=rtorpa_corrected_to, rtordpa_original_from=rtordpa_original_from, rtordpa_original_to=rtordpa_original_to, rtordpa_corrected_from=rtordpa_corrected_from, rtordpa_corrected_to=rtordpa_corrected_to, final_lmp_original_from=final_lmp_original_from, final_lmp_original_to=final_lmp_original_to, final_lmp_corrected_from=final_lmp_corrected_from, final_lmp_corrected_to=final_lmp_corrected_to, price_correction_time_from=price_correction_time_from, price_correction_time_to=price_correction_time_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP4197MApi->get_data21:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP4197MApi->get_data21: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **dst_flag** | **bool**| Format - true | false. | [optional] 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **resource_type** | **str**| Format - abc123. | [optional] 
 **resource_name** | **str**| Format - abc123. | [optional] 
 **meter_name** | **str**| Format - abc123. | [optional] 
 **meter_lmp_original_from** | **float**| Format - ####.###. | [optional] 
 **meter_lmp_original_to** | **float**| Format - ####.###. | [optional] 
 **meter_lmp_corrected_from** | **float**| Format - ####.###. | [optional] 
 **meter_lmp_corrected_to** | **float**| Format - ####.###. | [optional] 
 **rtorpa_original_from** | **float**| Format - ####.###. | [optional] 
 **rtorpa_original_to** | **float**| Format - ####.###. | [optional] 
 **rtorpa_corrected_from** | **float**| Format - ####.###. | [optional] 
 **rtorpa_corrected_to** | **float**| Format - ####.###. | [optional] 
 **rtordpa_original_from** | **float**| Format - ####.###. | [optional] 
 **rtordpa_original_to** | **float**| Format - ####.###. | [optional] 
 **rtordpa_corrected_from** | **float**| Format - ####.###. | [optional] 
 **rtordpa_corrected_to** | **float**| Format - ####.###. | [optional] 
 **final_lmp_original_from** | **float**| Format - ####.###. | [optional] 
 **final_lmp_original_to** | **float**| Format - ####.###. | [optional] 
 **final_lmp_corrected_from** | **float**| Format - ####.###. | [optional] 
 **final_lmp_corrected_to** | **float**| Format - ####.###. | [optional] 
 **price_correction_time_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **price_correction_time_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
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

# **get_data22**
> Report get_data22(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, constraint_id_from=constraint_id_from, constraint_id_to=constraint_id_to, constraint_name=constraint_name, contingency_name=contingency_name, shadow_price_original_from=shadow_price_original_from, shadow_price_original_to=shadow_price_original_to, shadow_price_corrected_from=shadow_price_corrected_from, shadow_price_corrected_to=shadow_price_corrected_to, limit_original_from=limit_original_from, limit_original_to=limit_original_to, limit_corrected_from=limit_corrected_from, limit_corrected_to=limit_corrected_to, value_original_from=value_original_from, value_original_to=value_original_to, value_corrected_from=value_corrected_from, value_corrected_to=value_corrected_to, price_correction_time_from=price_correction_time_from, price_correction_time_to=price_correction_time_to, dst_flag=dst_flag, page=page, size=size, sort=sort, dir=dir)

RTM Price Corrections for Shadow Prices

RTM Price Corrections for Shadow Prices

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
    api_instance = openapi_client.NP4197MApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    constraint_id_from = 56 # int | Format - ###. (optional)
    constraint_id_to = 56 # int | Format - ###. (optional)
    constraint_name = 'constraint_name_example' # str | Format - abc123. (optional)
    contingency_name = 'contingency_name_example' # str | Format - abc123. (optional)
    shadow_price_original_from = 3.4 # float | Format - ####.###. (optional)
    shadow_price_original_to = 3.4 # float | Format - ####.###. (optional)
    shadow_price_corrected_from = 3.4 # float | Format - ####.###. (optional)
    shadow_price_corrected_to = 3.4 # float | Format - ####.###. (optional)
    limit_original_from = 3.4 # float | Format - ####.###. (optional)
    limit_original_to = 3.4 # float | Format - ####.###. (optional)
    limit_corrected_from = 3.4 # float | Format - ####.###. (optional)
    limit_corrected_to = 3.4 # float | Format - ####.###. (optional)
    value_original_from = 3.4 # float | Format - ####.###. (optional)
    value_original_to = 3.4 # float | Format - ####.###. (optional)
    value_corrected_from = 3.4 # float | Format - ####.###. (optional)
    value_corrected_to = 3.4 # float | Format - ####.###. (optional)
    price_correction_time_from = 'price_correction_time_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    price_correction_time_to = 'price_correction_time_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    dst_flag = True # bool | Format - true | false. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # RTM Price Corrections for Shadow Prices
        api_response = api_instance.get_data22(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, constraint_id_from=constraint_id_from, constraint_id_to=constraint_id_to, constraint_name=constraint_name, contingency_name=contingency_name, shadow_price_original_from=shadow_price_original_from, shadow_price_original_to=shadow_price_original_to, shadow_price_corrected_from=shadow_price_corrected_from, shadow_price_corrected_to=shadow_price_corrected_to, limit_original_from=limit_original_from, limit_original_to=limit_original_to, limit_corrected_from=limit_corrected_from, limit_corrected_to=limit_corrected_to, value_original_from=value_original_from, value_original_to=value_original_to, value_corrected_from=value_corrected_from, value_corrected_to=value_corrected_to, price_correction_time_from=price_correction_time_from, price_correction_time_to=price_correction_time_to, dst_flag=dst_flag, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP4197MApi->get_data22:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP4197MApi->get_data22: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **constraint_id_from** | **int**| Format - ###. | [optional] 
 **constraint_id_to** | **int**| Format - ###. | [optional] 
 **constraint_name** | **str**| Format - abc123. | [optional] 
 **contingency_name** | **str**| Format - abc123. | [optional] 
 **shadow_price_original_from** | **float**| Format - ####.###. | [optional] 
 **shadow_price_original_to** | **float**| Format - ####.###. | [optional] 
 **shadow_price_corrected_from** | **float**| Format - ####.###. | [optional] 
 **shadow_price_corrected_to** | **float**| Format - ####.###. | [optional] 
 **limit_original_from** | **float**| Format - ####.###. | [optional] 
 **limit_original_to** | **float**| Format - ####.###. | [optional] 
 **limit_corrected_from** | **float**| Format - ####.###. | [optional] 
 **limit_corrected_to** | **float**| Format - ####.###. | [optional] 
 **value_original_from** | **float**| Format - ####.###. | [optional] 
 **value_original_to** | **float**| Format - ####.###. | [optional] 
 **value_corrected_from** | **float**| Format - ####.###. | [optional] 
 **value_corrected_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data23**
> Report get_data23(ocp_apim_subscription_key, lmp_corrected_from=lmp_corrected_from, lmp_corrected_to=lmp_corrected_to, price_correction_time_from=price_correction_time_from, price_correction_time_to=price_correction_time_to, dst_flag=dst_flag, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, electrical_bus=electrical_bus, lmp_original_from=lmp_original_from, lmp_original_to=lmp_original_to, page=page, size=size, sort=sort, dir=dir)

RTM Price Corrections for EB LMP

RTM Price Corrections for EB LMP

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
    api_instance = openapi_client.NP4197MApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    lmp_corrected_from = 3.4 # float | Format - ####.###. (optional)
    lmp_corrected_to = 3.4 # float | Format - ####.###. (optional)
    price_correction_time_from = 'price_correction_time_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    price_correction_time_to = 'price_correction_time_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    dst_flag = True # bool | Format - true | false. (optional)
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    electrical_bus = 'electrical_bus_example' # str | Format - abc123. (optional)
    lmp_original_from = 3.4 # float | Format - ####.###. (optional)
    lmp_original_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # RTM Price Corrections for EB LMP
        api_response = api_instance.get_data23(ocp_apim_subscription_key, lmp_corrected_from=lmp_corrected_from, lmp_corrected_to=lmp_corrected_to, price_correction_time_from=price_correction_time_from, price_correction_time_to=price_correction_time_to, dst_flag=dst_flag, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, electrical_bus=electrical_bus, lmp_original_from=lmp_original_from, lmp_original_to=lmp_original_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP4197MApi->get_data23:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP4197MApi->get_data23: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **lmp_corrected_from** | **float**| Format - ####.###. | [optional] 
 **lmp_corrected_to** | **float**| Format - ####.###. | [optional] 
 **price_correction_time_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **price_correction_time_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **dst_flag** | **bool**| Format - true | false. | [optional] 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **electrical_bus** | **str**| Format - abc123. | [optional] 
 **lmp_original_from** | **float**| Format - ####.###. | [optional] 
 **lmp_original_to** | **float**| Format - ####.###. | [optional] 
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

