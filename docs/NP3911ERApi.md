# openapi_client.NP3911ERApi

All URIs are relative to *https://api.ercot.com/api/public-reports*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data57**](NP3911ERApi.md#get_data57) | **GET** /np3-911-er/2d_self_arranged_as_rrsufr | 2 Day Self Arranged Ancillary Service RRSUFR
[**get_data58**](NP3911ERApi.md#get_data58) | **GET** /np3-911-er/2d_self_arranged_as_rrspfr | 2 Day Self Arranged Ancillary Service RRSPFR
[**get_data59**](NP3911ERApi.md#get_data59) | **GET** /np3-911-er/2d_self_arranged_as_rrsffr | 2 Day Self Arranged Ancillary Service RRSFFR
[**get_data60**](NP3911ERApi.md#get_data60) | **GET** /np3-911-er/2d_self_arranged_as_regup | 2 Day Self Arranged Ancillary Service REGUP
[**get_data61**](NP3911ERApi.md#get_data61) | **GET** /np3-911-er/2d_self_arranged_as_regdn | 2 Day Self Arranged Ancillary Service REGDN
[**get_data62**](NP3911ERApi.md#get_data62) | **GET** /np3-911-er/2d_self_arranged_as_nspnm | 2 Day Self Arranged Ancillary Service NSPNM
[**get_data63**](NP3911ERApi.md#get_data63) | **GET** /np3-911-er/2d_self_arranged_as_nspin | 2 Day Self Arranged Ancillary Service NSPIN
[**get_data64**](NP3911ERApi.md#get_data64) | **GET** /np3-911-er/2d_self_arranged_as_ecrss | 2 Day Self Arranged Ancillary Service ECRSS
[**get_data65**](NP3911ERApi.md#get_data65) | **GET** /np3-911-er/2d_self_arranged_as_ecrsm | 2 Day Self Arranged Ancillary Service ECRSM
[**get_data66**](NP3911ERApi.md#get_data66) | **GET** /np3-911-er/2d_cleared_dam_as_rrsufr | 2 Day Cleared DAM Ancillary Service RRSUFR
[**get_data67**](NP3911ERApi.md#get_data67) | **GET** /np3-911-er/2d_cleared_dam_as_rrspfr | 2 Day Cleared DAM Ancillary Service RRSPFR
[**get_data68**](NP3911ERApi.md#get_data68) | **GET** /np3-911-er/2d_cleared_dam_as_rrsffr | 2 Day Cleared DAM Ancillary Service RRSFFR
[**get_data69**](NP3911ERApi.md#get_data69) | **GET** /np3-911-er/2d_cleared_dam_as_regup | 2 Day Cleared DAM Ancillary Service REGUP
[**get_data70**](NP3911ERApi.md#get_data70) | **GET** /np3-911-er/2d_cleared_dam_as_regdn | 2 Day Cleared DAM Ancillary Service REGDN
[**get_data71**](NP3911ERApi.md#get_data71) | **GET** /np3-911-er/2d_cleared_dam_as_nspin | 2 Day Cleared DAM Ancillary Service NSPIN
[**get_data72**](NP3911ERApi.md#get_data72) | **GET** /np3-911-er/2d_cleared_dam_as_ecrss | 2 Day Cleared DAM Ancillary Service ECRSS
[**get_data73**](NP3911ERApi.md#get_data73) | **GET** /np3-911-er/2d_cleared_dam_as_ecrsm | 2 Day Cleared DAM Ancillary Service ECRSM
[**get_data74**](NP3911ERApi.md#get_data74) | **GET** /np3-911-er/2d_agg_as_offers_rrsufr | 2 Day Aggregated Ancillary Service Offers RRSUFR
[**get_data75**](NP3911ERApi.md#get_data75) | **GET** /np3-911-er/2d_agg_as_offers_rrspfr | 2 Day Aggregated Ancillary Service Offers RRSPFR
[**get_data76**](NP3911ERApi.md#get_data76) | **GET** /np3-911-er/2d_agg_as_offers_rrsffr | 2 Day Aggregated Ancillary Service Offers RRSFFR
[**get_data77**](NP3911ERApi.md#get_data77) | **GET** /np3-911-er/2d_agg_as_offers_regup | 2 Day Aggregated Ancillary Service Offers REGUP
[**get_data78**](NP3911ERApi.md#get_data78) | **GET** /np3-911-er/2d_agg_as_offers_regdn | 2 Day Aggregated Ancillary Service Offers REGDN
[**get_data79**](NP3911ERApi.md#get_data79) | **GET** /np3-911-er/2d_agg_as_offers_onns | 2 Day Aggregated Ancillary Service Offers ONNS
[**get_data80**](NP3911ERApi.md#get_data80) | **GET** /np3-911-er/2d_agg_as_offers_offns | 2 Day Aggregated Ancillary Service Offers OFFNS
[**get_data81**](NP3911ERApi.md#get_data81) | **GET** /np3-911-er/2d_agg_as_offers_ecrss | 2 Day Aggregated Ancillary Service Offers ECRSS
[**get_data82**](NP3911ERApi.md#get_data82) | **GET** /np3-911-er/2d_agg_as_offers_ecrsm | 2 Day Aggregated Ancillary Service Offers ECRSM


# **get_data57**
> Report get_data57(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_self_arranged_asrrsufr_from=total_self_arranged_asrrsufr_from, total_self_arranged_asrrsufrto=total_self_arranged_asrrsufrto, page=page, size=size, sort=sort, dir=dir)

2 Day Self Arranged Ancillary Service RRSUFR

2 Day Self Arranged Ancillary Service RRSUFR

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    total_self_arranged_asrrsufr_from = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asrrsufrto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Self Arranged Ancillary Service RRSUFR
        api_response = api_instance.get_data57(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_self_arranged_asrrsufr_from=total_self_arranged_asrrsufr_from, total_self_arranged_asrrsufrto=total_self_arranged_asrrsufrto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data57:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data57: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **total_self_arranged_asrrsufr_from** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asrrsufrto** | **float**| Format - ####.###. | [optional] 
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

# **get_data58**
> Report get_data58(ocp_apim_subscription_key, total_self_arranged_asrrspfr_from=total_self_arranged_asrrspfr_from, total_self_arranged_asrrspfrto=total_self_arranged_asrrspfrto, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, page=page, size=size, sort=sort, dir=dir)

2 Day Self Arranged Ancillary Service RRSPFR

2 Day Self Arranged Ancillary Service RRSPFR

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    total_self_arranged_asrrspfr_from = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asrrspfrto = 3.4 # float | Format - ####.###. (optional)
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Self Arranged Ancillary Service RRSPFR
        api_response = api_instance.get_data58(ocp_apim_subscription_key, total_self_arranged_asrrspfr_from=total_self_arranged_asrrspfr_from, total_self_arranged_asrrspfrto=total_self_arranged_asrrspfrto, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data58:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data58: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **total_self_arranged_asrrspfr_from** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asrrspfrto** | **float**| Format - ####.###. | [optional] 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
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

# **get_data59**
> Report get_data59(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_self_arranged_asrrsffr_from=total_self_arranged_asrrsffr_from, total_self_arranged_asrrsffrto=total_self_arranged_asrrsffrto, page=page, size=size, sort=sort, dir=dir)

2 Day Self Arranged Ancillary Service RRSFFR

2 Day Self Arranged Ancillary Service RRSFFR

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    total_self_arranged_asrrsffr_from = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asrrsffrto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Self Arranged Ancillary Service RRSFFR
        api_response = api_instance.get_data59(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_self_arranged_asrrsffr_from=total_self_arranged_asrrsffr_from, total_self_arranged_asrrsffrto=total_self_arranged_asrrsffrto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data59:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data59: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **total_self_arranged_asrrsffr_from** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asrrsffrto** | **float**| Format - ####.###. | [optional] 
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

# **get_data60**
> Report get_data60(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_self_arranged_asregup_from=total_self_arranged_asregup_from, total_self_arranged_asregupto=total_self_arranged_asregupto, page=page, size=size, sort=sort, dir=dir)

2 Day Self Arranged Ancillary Service REGUP

2 Day Self Arranged Ancillary Service REGUP

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    total_self_arranged_asregup_from = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asregupto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Self Arranged Ancillary Service REGUP
        api_response = api_instance.get_data60(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_self_arranged_asregup_from=total_self_arranged_asregup_from, total_self_arranged_asregupto=total_self_arranged_asregupto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data60:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data60: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **total_self_arranged_asregup_from** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asregupto** | **float**| Format - ####.###. | [optional] 
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

# **get_data61**
> Report get_data61(ocp_apim_subscription_key, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_self_arranged_asregdn_from=total_self_arranged_asregdn_from, total_self_arranged_asregdnto=total_self_arranged_asregdnto, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, page=page, size=size, sort=sort, dir=dir)

2 Day Self Arranged Ancillary Service REGDN

2 Day Self Arranged Ancillary Service REGDN

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    total_self_arranged_asregdn_from = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asregdnto = 3.4 # float | Format - ####.###. (optional)
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Self Arranged Ancillary Service REGDN
        api_response = api_instance.get_data61(ocp_apim_subscription_key, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_self_arranged_asregdn_from=total_self_arranged_asregdn_from, total_self_arranged_asregdnto=total_self_arranged_asregdnto, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data61:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data61: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **total_self_arranged_asregdn_from** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asregdnto** | **float**| Format - ####.###. | [optional] 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
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

# **get_data62**
> Report get_data62(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_self_arranged_asnspnm_from=total_self_arranged_asnspnm_from, total_self_arranged_asnspnmto=total_self_arranged_asnspnmto, page=page, size=size, sort=sort, dir=dir)

2 Day Self Arranged Ancillary Service NSPNM

2 Day Self Arranged Ancillary Service NSPNM

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    total_self_arranged_asnspnm_from = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asnspnmto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Self Arranged Ancillary Service NSPNM
        api_response = api_instance.get_data62(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_self_arranged_asnspnm_from=total_self_arranged_asnspnm_from, total_self_arranged_asnspnmto=total_self_arranged_asnspnmto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data62:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data62: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **total_self_arranged_asnspnm_from** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asnspnmto** | **float**| Format - ####.###. | [optional] 
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

# **get_data63**
> Report get_data63(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_self_arranged_asnspin_from=total_self_arranged_asnspin_from, total_self_arranged_asnspinto=total_self_arranged_asnspinto, page=page, size=size, sort=sort, dir=dir)

2 Day Self Arranged Ancillary Service NSPIN

2 Day Self Arranged Ancillary Service NSPIN

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    total_self_arranged_asnspin_from = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asnspinto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Self Arranged Ancillary Service NSPIN
        api_response = api_instance.get_data63(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_self_arranged_asnspin_from=total_self_arranged_asnspin_from, total_self_arranged_asnspinto=total_self_arranged_asnspinto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data63:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data63: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **total_self_arranged_asnspin_from** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asnspinto** | **float**| Format - ####.###. | [optional] 
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

# **get_data64**
> Report get_data64(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_self_arranged_asecrss_from=total_self_arranged_asecrss_from, total_self_arranged_asecrssto=total_self_arranged_asecrssto, page=page, size=size, sort=sort, dir=dir)

2 Day Self Arranged Ancillary Service ECRSS

2 Day Self Arranged Ancillary Service ECRSS

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    total_self_arranged_asecrss_from = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asecrssto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Self Arranged Ancillary Service ECRSS
        api_response = api_instance.get_data64(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_self_arranged_asecrss_from=total_self_arranged_asecrss_from, total_self_arranged_asecrssto=total_self_arranged_asecrssto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data64:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data64: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **total_self_arranged_asecrss_from** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asecrssto** | **float**| Format - ####.###. | [optional] 
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

# **get_data65**
> Report get_data65(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_self_arranged_asecrsm_from=total_self_arranged_asecrsm_from, total_self_arranged_asecrsmto=total_self_arranged_asecrsmto, page=page, size=size, sort=sort, dir=dir)

2 Day Self Arranged Ancillary Service ECRSM

2 Day Self Arranged Ancillary Service ECRSM

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    total_self_arranged_asecrsm_from = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asecrsmto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Self Arranged Ancillary Service ECRSM
        api_response = api_instance.get_data65(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_self_arranged_asecrsm_from=total_self_arranged_asecrsm_from, total_self_arranged_asecrsmto=total_self_arranged_asecrsmto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data65:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data65: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **total_self_arranged_asecrsm_from** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asecrsmto** | **float**| Format - ####.###. | [optional] 
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

# **get_data66**
> Report get_data66(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_cleared_asrrsufr_from=total_cleared_asrrsufr_from, total_cleared_asrrsufrto=total_cleared_asrrsufrto, page=page, size=size, sort=sort, dir=dir)

2 Day Cleared DAM Ancillary Service RRSUFR

2 Day Cleared DAM Ancillary Service RRSUFR

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    total_cleared_asrrsufr_from = 3.4 # float | Format - ####.###. (optional)
    total_cleared_asrrsufrto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Cleared DAM Ancillary Service RRSUFR
        api_response = api_instance.get_data66(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_cleared_asrrsufr_from=total_cleared_asrrsufr_from, total_cleared_asrrsufrto=total_cleared_asrrsufrto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data66:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data66: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **total_cleared_asrrsufr_from** | **float**| Format - ####.###. | [optional] 
 **total_cleared_asrrsufrto** | **float**| Format - ####.###. | [optional] 
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

# **get_data67**
> Report get_data67(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_cleared_asrrspfr_from=total_cleared_asrrspfr_from, total_cleared_asrrspfrto=total_cleared_asrrspfrto, page=page, size=size, sort=sort, dir=dir)

2 Day Cleared DAM Ancillary Service RRSPFR

2 Day Cleared DAM Ancillary Service RRSPFR

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    total_cleared_asrrspfr_from = 3.4 # float | Format - ####.###. (optional)
    total_cleared_asrrspfrto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Cleared DAM Ancillary Service RRSPFR
        api_response = api_instance.get_data67(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_cleared_asrrspfr_from=total_cleared_asrrspfr_from, total_cleared_asrrspfrto=total_cleared_asrrspfrto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data67:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data67: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **total_cleared_asrrspfr_from** | **float**| Format - ####.###. | [optional] 
 **total_cleared_asrrspfrto** | **float**| Format - ####.###. | [optional] 
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

# **get_data68**
> Report get_data68(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_cleared_asrrsffr_from=total_cleared_asrrsffr_from, total_cleared_asrrsffrto=total_cleared_asrrsffrto, page=page, size=size, sort=sort, dir=dir)

2 Day Cleared DAM Ancillary Service RRSFFR

2 Day Cleared DAM Ancillary Service RRSFFR

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    total_cleared_asrrsffr_from = 3.4 # float | Format - ####.###. (optional)
    total_cleared_asrrsffrto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Cleared DAM Ancillary Service RRSFFR
        api_response = api_instance.get_data68(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_cleared_asrrsffr_from=total_cleared_asrrsffr_from, total_cleared_asrrsffrto=total_cleared_asrrsffrto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data68:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data68: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **total_cleared_asrrsffr_from** | **float**| Format - ####.###. | [optional] 
 **total_cleared_asrrsffrto** | **float**| Format - ####.###. | [optional] 
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

# **get_data69**
> Report get_data69(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_cleared_asregup_from=total_cleared_asregup_from, total_cleared_asregupto=total_cleared_asregupto, page=page, size=size, sort=sort, dir=dir)

2 Day Cleared DAM Ancillary Service REGUP

2 Day Cleared DAM Ancillary Service REGUP

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    total_cleared_asregup_from = 3.4 # float | Format - ####.###. (optional)
    total_cleared_asregupto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Cleared DAM Ancillary Service REGUP
        api_response = api_instance.get_data69(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_cleared_asregup_from=total_cleared_asregup_from, total_cleared_asregupto=total_cleared_asregupto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data69:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data69: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **total_cleared_asregup_from** | **float**| Format - ####.###. | [optional] 
 **total_cleared_asregupto** | **float**| Format - ####.###. | [optional] 
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

# **get_data70**
> Report get_data70(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_cleared_asregdn_from=total_cleared_asregdn_from, total_cleared_asregdnto=total_cleared_asregdnto, page=page, size=size, sort=sort, dir=dir)

2 Day Cleared DAM Ancillary Service REGDN

2 Day Cleared DAM Ancillary Service REGDN

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    total_cleared_asregdn_from = 3.4 # float | Format - ####.###. (optional)
    total_cleared_asregdnto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Cleared DAM Ancillary Service REGDN
        api_response = api_instance.get_data70(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_cleared_asregdn_from=total_cleared_asregdn_from, total_cleared_asregdnto=total_cleared_asregdnto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data70:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data70: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **total_cleared_asregdn_from** | **float**| Format - ####.###. | [optional] 
 **total_cleared_asregdnto** | **float**| Format - ####.###. | [optional] 
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

# **get_data71**
> Report get_data71(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_cleared_asnspin_from=total_cleared_asnspin_from, total_cleared_asnspinto=total_cleared_asnspinto, page=page, size=size, sort=sort, dir=dir)

2 Day Cleared DAM Ancillary Service NSPIN

2 Day Cleared DAM Ancillary Service NSPIN

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    total_cleared_asnspin_from = 3.4 # float | Format - ####.###. (optional)
    total_cleared_asnspinto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Cleared DAM Ancillary Service NSPIN
        api_response = api_instance.get_data71(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_cleared_asnspin_from=total_cleared_asnspin_from, total_cleared_asnspinto=total_cleared_asnspinto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data71:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data71: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **total_cleared_asnspin_from** | **float**| Format - ####.###. | [optional] 
 **total_cleared_asnspinto** | **float**| Format - ####.###. | [optional] 
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

# **get_data72**
> Report get_data72(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_cleared_asecrss_from=total_cleared_asecrss_from, total_cleared_asecrssto=total_cleared_asecrssto, page=page, size=size, sort=sort, dir=dir)

2 Day Cleared DAM Ancillary Service ECRSS

2 Day Cleared DAM Ancillary Service ECRSS

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    total_cleared_asecrss_from = 3.4 # float | Format - ####.###. (optional)
    total_cleared_asecrssto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Cleared DAM Ancillary Service ECRSS
        api_response = api_instance.get_data72(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_cleared_asecrss_from=total_cleared_asecrss_from, total_cleared_asecrssto=total_cleared_asecrssto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data72:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data72: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **total_cleared_asecrss_from** | **float**| Format - ####.###. | [optional] 
 **total_cleared_asecrssto** | **float**| Format - ####.###. | [optional] 
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

# **get_data73**
> Report get_data73(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_cleared_asecrsm_from=total_cleared_asecrsm_from, total_cleared_asecrsmto=total_cleared_asecrsmto, page=page, size=size, sort=sort, dir=dir)

2 Day Cleared DAM Ancillary Service ECRSM

2 Day Cleared DAM Ancillary Service ECRSM

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    total_cleared_asecrsm_from = 3.4 # float | Format - ####.###. (optional)
    total_cleared_asecrsmto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Cleared DAM Ancillary Service ECRSM
        api_response = api_instance.get_data73(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, total_cleared_asecrsm_from=total_cleared_asecrsm_from, total_cleared_asecrsmto=total_cleared_asecrsmto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data73:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data73: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **total_cleared_asecrsm_from** | **float**| Format - ####.###. | [optional] 
 **total_cleared_asecrsmto** | **float**| Format - ####.###. | [optional] 
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

# **get_data74**
> Report get_data74(ocp_apim_subscription_key, rrsufr_offer_price_from=rrsufr_offer_price_from, rrsufr_offer_price_to=rrsufr_offer_price_to, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, mw_offered_from=mw_offered_from, mw_offered_to=mw_offered_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Ancillary Service Offers RRSUFR

2 Day Aggregated Ancillary Service Offers RRSUFR

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    rrsufr_offer_price_from = 3.4 # float | Format - ####.###. (optional)
    rrsufr_offer_price_to = 3.4 # float | Format - ####.###. (optional)
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    mw_offered_from = 3.4 # float | Format - ####.###. (optional)
    mw_offered_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Ancillary Service Offers RRSUFR
        api_response = api_instance.get_data74(ocp_apim_subscription_key, rrsufr_offer_price_from=rrsufr_offer_price_from, rrsufr_offer_price_to=rrsufr_offer_price_to, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, mw_offered_from=mw_offered_from, mw_offered_to=mw_offered_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data74:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data74: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **rrsufr_offer_price_from** | **float**| Format - ####.###. | [optional] 
 **rrsufr_offer_price_to** | **float**| Format - ####.###. | [optional] 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **mw_offered_from** | **float**| Format - ####.###. | [optional] 
 **mw_offered_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data75**
> Report get_data75(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, mw_offered_from=mw_offered_from, mw_offered_to=mw_offered_to, rrspfr_offer_price_from=rrspfr_offer_price_from, rrspfr_offer_price_to=rrspfr_offer_price_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Ancillary Service Offers RRSPFR

2 Day Aggregated Ancillary Service Offers RRSPFR

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    mw_offered_from = 3.4 # float | Format - ####.###. (optional)
    mw_offered_to = 3.4 # float | Format - ####.###. (optional)
    rrspfr_offer_price_from = 3.4 # float | Format - ####.###. (optional)
    rrspfr_offer_price_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Ancillary Service Offers RRSPFR
        api_response = api_instance.get_data75(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, mw_offered_from=mw_offered_from, mw_offered_to=mw_offered_to, rrspfr_offer_price_from=rrspfr_offer_price_from, rrspfr_offer_price_to=rrspfr_offer_price_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data75:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data75: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **mw_offered_from** | **float**| Format - ####.###. | [optional] 
 **mw_offered_to** | **float**| Format - ####.###. | [optional] 
 **rrspfr_offer_price_from** | **float**| Format - ####.###. | [optional] 
 **rrspfr_offer_price_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data76**
> Report get_data76(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, mw_offered_from=mw_offered_from, mw_offered_to=mw_offered_to, rrsffr_offer_price_from=rrsffr_offer_price_from, rrsffr_offer_price_to=rrsffr_offer_price_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Ancillary Service Offers RRSFFR

2 Day Aggregated Ancillary Service Offers RRSFFR

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    mw_offered_from = 3.4 # float | Format - ####.###. (optional)
    mw_offered_to = 3.4 # float | Format - ####.###. (optional)
    rrsffr_offer_price_from = 3.4 # float | Format - ####.###. (optional)
    rrsffr_offer_price_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Ancillary Service Offers RRSFFR
        api_response = api_instance.get_data76(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, mw_offered_from=mw_offered_from, mw_offered_to=mw_offered_to, rrsffr_offer_price_from=rrsffr_offer_price_from, rrsffr_offer_price_to=rrsffr_offer_price_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data76:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data76: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **mw_offered_from** | **float**| Format - ####.###. | [optional] 
 **mw_offered_to** | **float**| Format - ####.###. | [optional] 
 **rrsffr_offer_price_from** | **float**| Format - ####.###. | [optional] 
 **rrsffr_offer_price_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data77**
> Report get_data77(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, mw_offered_from=mw_offered_from, mw_offered_to=mw_offered_to, regup_offer_price_from=regup_offer_price_from, regup_offer_price_to=regup_offer_price_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Ancillary Service Offers REGUP

2 Day Aggregated Ancillary Service Offers REGUP

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    mw_offered_from = 3.4 # float | Format - ####.###. (optional)
    mw_offered_to = 3.4 # float | Format - ####.###. (optional)
    regup_offer_price_from = 3.4 # float | Format - ####.###. (optional)
    regup_offer_price_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Ancillary Service Offers REGUP
        api_response = api_instance.get_data77(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, mw_offered_from=mw_offered_from, mw_offered_to=mw_offered_to, regup_offer_price_from=regup_offer_price_from, regup_offer_price_to=regup_offer_price_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data77:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data77: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **mw_offered_from** | **float**| Format - ####.###. | [optional] 
 **mw_offered_to** | **float**| Format - ####.###. | [optional] 
 **regup_offer_price_from** | **float**| Format - ####.###. | [optional] 
 **regup_offer_price_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data78**
> Report get_data78(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, mw_offered_from=mw_offered_from, mw_offered_to=mw_offered_to, regdn_offer_price_from=regdn_offer_price_from, regdn_offer_price_to=regdn_offer_price_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Ancillary Service Offers REGDN

2 Day Aggregated Ancillary Service Offers REGDN

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    mw_offered_from = 3.4 # float | Format - ####.###. (optional)
    mw_offered_to = 3.4 # float | Format - ####.###. (optional)
    regdn_offer_price_from = 3.4 # float | Format - ####.###. (optional)
    regdn_offer_price_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Ancillary Service Offers REGDN
        api_response = api_instance.get_data78(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, mw_offered_from=mw_offered_from, mw_offered_to=mw_offered_to, regdn_offer_price_from=regdn_offer_price_from, regdn_offer_price_to=regdn_offer_price_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data78:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data78: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **mw_offered_from** | **float**| Format - ####.###. | [optional] 
 **mw_offered_to** | **float**| Format - ####.###. | [optional] 
 **regdn_offer_price_from** | **float**| Format - ####.###. | [optional] 
 **regdn_offer_price_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data79**
> Report get_data79(ocp_apim_subscription_key, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, mw_offered_from=mw_offered_from, mw_offered_to=mw_offered_to, onns_offer_price_from=onns_offer_price_from, onns_offer_price_to=onns_offer_price_to, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Ancillary Service Offers ONNS

2 Day Aggregated Ancillary Service Offers ONNS

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    mw_offered_from = 3.4 # float | Format - ####.###. (optional)
    mw_offered_to = 3.4 # float | Format - ####.###. (optional)
    onns_offer_price_from = 3.4 # float | Format - ####.###. (optional)
    onns_offer_price_to = 3.4 # float | Format - ####.###. (optional)
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Ancillary Service Offers ONNS
        api_response = api_instance.get_data79(ocp_apim_subscription_key, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, mw_offered_from=mw_offered_from, mw_offered_to=mw_offered_to, onns_offer_price_from=onns_offer_price_from, onns_offer_price_to=onns_offer_price_to, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data79:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data79: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **mw_offered_from** | **float**| Format - ####.###. | [optional] 
 **mw_offered_to** | **float**| Format - ####.###. | [optional] 
 **onns_offer_price_from** | **float**| Format - ####.###. | [optional] 
 **onns_offer_price_to** | **float**| Format - ####.###. | [optional] 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
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

# **get_data80**
> Report get_data80(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, mw_offered_from=mw_offered_from, mw_offered_to=mw_offered_to, offns_offer_price_from=offns_offer_price_from, offns_offer_price_to=offns_offer_price_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Ancillary Service Offers OFFNS

2 Day Aggregated Ancillary Service Offers OFFNS

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    mw_offered_from = 3.4 # float | Format - ####.###. (optional)
    mw_offered_to = 3.4 # float | Format - ####.###. (optional)
    offns_offer_price_from = 3.4 # float | Format - ####.###. (optional)
    offns_offer_price_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Ancillary Service Offers OFFNS
        api_response = api_instance.get_data80(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, mw_offered_from=mw_offered_from, mw_offered_to=mw_offered_to, offns_offer_price_from=offns_offer_price_from, offns_offer_price_to=offns_offer_price_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data80:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data80: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **mw_offered_from** | **float**| Format - ####.###. | [optional] 
 **mw_offered_to** | **float**| Format - ####.###. | [optional] 
 **offns_offer_price_from** | **float**| Format - ####.###. | [optional] 
 **offns_offer_price_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data81**
> Report get_data81(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, mw_offered_from=mw_offered_from, mw_offered_to=mw_offered_to, ecrss_offer_price_from=ecrss_offer_price_from, ecrss_offer_price_to=ecrss_offer_price_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Ancillary Service Offers ECRSS

2 Day Aggregated Ancillary Service Offers ECRSS

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    mw_offered_from = 3.4 # float | Format - ####.###. (optional)
    mw_offered_to = 3.4 # float | Format - ####.###. (optional)
    ecrss_offer_price_from = 3.4 # float | Format - ####.###. (optional)
    ecrss_offer_price_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Ancillary Service Offers ECRSS
        api_response = api_instance.get_data81(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, mw_offered_from=mw_offered_from, mw_offered_to=mw_offered_to, ecrss_offer_price_from=ecrss_offer_price_from, ecrss_offer_price_to=ecrss_offer_price_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data81:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data81: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **mw_offered_from** | **float**| Format - ####.###. | [optional] 
 **mw_offered_to** | **float**| Format - ####.###. | [optional] 
 **ecrss_offer_price_from** | **float**| Format - ####.###. | [optional] 
 **ecrss_offer_price_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data82**
> Report get_data82(ocp_apim_subscription_key, ecrsm_offer_price_from=ecrsm_offer_price_from, ecrsm_offer_price_to=ecrsm_offer_price_to, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, mw_offered_from=mw_offered_from, mw_offered_to=mw_offered_to, page=page, size=size, sort=sort, dir=dir)

2 Day Aggregated Ancillary Service Offers ECRSM

2 Day Aggregated Ancillary Service Offers ECRSM

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
    api_instance = openapi_client.NP3911ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    ecrsm_offer_price_from = 3.4 # float | Format - ####.###. (optional)
    ecrsm_offer_price_to = 3.4 # float | Format - ####.###. (optional)
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    mw_offered_from = 3.4 # float | Format - ####.###. (optional)
    mw_offered_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 2 Day Aggregated Ancillary Service Offers ECRSM
        api_response = api_instance.get_data82(ocp_apim_subscription_key, ecrsm_offer_price_from=ecrsm_offer_price_from, ecrsm_offer_price_to=ecrsm_offer_price_to, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, mw_offered_from=mw_offered_from, mw_offered_to=mw_offered_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3911ERApi->get_data82:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3911ERApi->get_data82: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **ecrsm_offer_price_from** | **float**| Format - ####.###. | [optional] 
 **ecrsm_offer_price_to** | **float**| Format - ####.###. | [optional] 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **mw_offered_from** | **float**| Format - ####.###. | [optional] 
 **mw_offered_to** | **float**| Format - ####.###. | [optional] 
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

