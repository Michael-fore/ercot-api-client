# openapi_client.NP3966ERApi

All URIs are relative to *https://api.ercot.com/api/public-reports*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data38**](NP3966ERApi.md#get_data38) | **GET** /np3-966-er/60_dam_qse_self_as | 60 Day DAM QSE Self Arranged AS
[**get_data39**](NP3966ERApi.md#get_data39) | **GET** /np3-966-er/60_dam_ptp_obl_opt_awards | 60 Day DAM PTP Obligation Option Awards
[**get_data40**](NP3966ERApi.md#get_data40) | **GET** /np3-966-er/60_dam_ptp_obl_opt | 60 Day DAM PTP Obligation Option
[**get_data41**](NP3966ERApi.md#get_data41) | **GET** /np3-966-er/60_dam_ptp_obl_bids | 60 Day DAM PTP Obligation Bids
[**get_data42**](NP3966ERApi.md#get_data42) | **GET** /np3-966-er/60_dam_ptp_obl_bid_awards | 60 Day DAM PTP Obligation Bid Awards
[**get_data43**](NP3966ERApi.md#get_data43) | **GET** /np3-966-er/60_dam_load_res_data | 60 Day DAM Load Resource Data
[**get_data44**](NP3966ERApi.md#get_data44) | **GET** /np3-966-er/60_dam_load_res_as_offers | 60 Day DAM Load Resources AS Offers
[**get_data45**](NP3966ERApi.md#get_data45) | **GET** /np3-966-er/60_dam_gen_res_data | 60 Day DAM Generation Resource Data
[**get_data46**](NP3966ERApi.md#get_data46) | **GET** /np3-966-er/60_dam_gen_res_as_offers | 60 Day DAM Generation Resources AS Offers
[**get_data47**](NP3966ERApi.md#get_data47) | **GET** /np3-966-er/60_dam_energy_only_offers | 60 Day DAM Energy Only Offers
[**get_data48**](NP3966ERApi.md#get_data48) | **GET** /np3-966-er/60_dam_energy_only_offer_awards | 60 Day DAM Energy Offer Only Awards
[**get_data49**](NP3966ERApi.md#get_data49) | **GET** /np3-966-er/60_dam_energy_bids | 60 Day DAM Energy Bids
[**get_data50**](NP3966ERApi.md#get_data50) | **GET** /np3-966-er/60_dam_energy_bid_awards | 60 Day DAM Energy Bid Awards


# **get_data38**
> Report get_data38(ocp_apim_subscription_key, total_self_arranged_asrrsufr_from=total_self_arranged_asrrsufr_from, total_self_arranged_asrrsufrto=total_self_arranged_asrrsufrto, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, total_self_arranged_asregup_from=total_self_arranged_asregup_from, total_self_arranged_asregupto=total_self_arranged_asregupto, total_self_arranged_asregdn_from=total_self_arranged_asregdn_from, total_self_arranged_asregdnto=total_self_arranged_asregdnto, total_self_arranged_asnspin_from=total_self_arranged_asnspin_from, total_self_arranged_asnspinto=total_self_arranged_asnspinto, total_self_arranged_asnspnm_from=total_self_arranged_asnspnm_from, total_self_arranged_asnspnmto=total_self_arranged_asnspnmto, total_self_arranged_asrrspfr_from=total_self_arranged_asrrspfr_from, total_self_arranged_asrrspfrto=total_self_arranged_asrrspfrto, total_self_arranged_asrrsffr_from=total_self_arranged_asrrsffr_from, total_self_arranged_asrrsffrto=total_self_arranged_asrrsffrto, page=page, size=size, sort=sort, dir=dir)

60 Day DAM QSE Self Arranged AS

60 Day DAM QSE Self Arranged AS

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
    api_instance = openapi_client.NP3966ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    total_self_arranged_asrrsufr_from = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asrrsufrto = 3.4 # float | Format - ####.###. (optional)
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    total_self_arranged_asregup_from = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asregupto = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asregdn_from = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asregdnto = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asnspin_from = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asnspinto = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asnspnm_from = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asnspnmto = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asrrspfr_from = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asrrspfrto = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asrrsffr_from = 3.4 # float | Format - ####.###. (optional)
    total_self_arranged_asrrsffrto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day DAM QSE Self Arranged AS
        api_response = api_instance.get_data38(ocp_apim_subscription_key, total_self_arranged_asrrsufr_from=total_self_arranged_asrrsufr_from, total_self_arranged_asrrsufrto=total_self_arranged_asrrsufrto, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, total_self_arranged_asregup_from=total_self_arranged_asregup_from, total_self_arranged_asregupto=total_self_arranged_asregupto, total_self_arranged_asregdn_from=total_self_arranged_asregdn_from, total_self_arranged_asregdnto=total_self_arranged_asregdnto, total_self_arranged_asnspin_from=total_self_arranged_asnspin_from, total_self_arranged_asnspinto=total_self_arranged_asnspinto, total_self_arranged_asnspnm_from=total_self_arranged_asnspnm_from, total_self_arranged_asnspnmto=total_self_arranged_asnspnmto, total_self_arranged_asrrspfr_from=total_self_arranged_asrrspfr_from, total_self_arranged_asrrspfrto=total_self_arranged_asrrspfrto, total_self_arranged_asrrsffr_from=total_self_arranged_asrrsffr_from, total_self_arranged_asrrsffrto=total_self_arranged_asrrsffrto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3966ERApi->get_data38:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3966ERApi->get_data38: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **total_self_arranged_asrrsufr_from** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asrrsufrto** | **float**| Format - ####.###. | [optional] 
 **delivery_date_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **qse_name** | **str**| Format - abc123. | [optional] 
 **total_self_arranged_asregup_from** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asregupto** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asregdn_from** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asregdnto** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asnspin_from** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asnspinto** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asnspnm_from** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asnspnmto** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asrrspfr_from** | **float**| Format - ####.###. | [optional] 
 **total_self_arranged_asrrspfrto** | **float**| Format - ####.###. | [optional] 
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

# **get_data39**
> Report get_data39(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, settlement_point_source=settlement_point_source, settlement_point_sink=settlement_point_sink, mw_from=mw_from, mwto=mwto, price_from=price_from, price_to=price_to, offer_id=offer_id, crrid=crrid, page=page, size=size, sort=sort, dir=dir)

60 Day DAM PTP Obligation Option Awards

60 Day DAM PTP Obligation Option Awards

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
    api_instance = openapi_client.NP3966ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 'hour_ending_from_example' # str | Format - mm:ss. (optional)
    hour_ending_to = 'hour_ending_to_example' # str | Format - mm:ss. (optional)
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    settlement_point_source = 'settlement_point_source_example' # str | Format - abc123. (optional)
    settlement_point_sink = 'settlement_point_sink_example' # str | Format - abc123. (optional)
    mw_from = 3.4 # float | Format - ####.###. (optional)
    mwto = 3.4 # float | Format - ####.###. (optional)
    price_from = 3.4 # float | Format - ####.###. (optional)
    price_to = 3.4 # float | Format - ####.###. (optional)
    offer_id = 'offer_id_example' # str | Format - abc123. (optional)
    crrid = 'crrid_example' # str | Format - abc123. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day DAM PTP Obligation Option Awards
        api_response = api_instance.get_data39(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, settlement_point_source=settlement_point_source, settlement_point_sink=settlement_point_sink, mw_from=mw_from, mwto=mwto, price_from=price_from, price_to=price_to, offer_id=offer_id, crrid=crrid, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3966ERApi->get_data39:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3966ERApi->get_data39: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **str**| Format - mm:ss. | [optional] 
 **hour_ending_to** | **str**| Format - mm:ss. | [optional] 
 **qse_name** | **str**| Format - abc123. | [optional] 
 **settlement_point_source** | **str**| Format - abc123. | [optional] 
 **settlement_point_sink** | **str**| Format - abc123. | [optional] 
 **mw_from** | **float**| Format - ####.###. | [optional] 
 **mwto** | **float**| Format - ####.###. | [optional] 
 **price_from** | **float**| Format - ####.###. | [optional] 
 **price_to** | **float**| Format - ####.###. | [optional] 
 **offer_id** | **str**| Format - abc123. | [optional] 
 **crrid** | **str**| Format - abc123. | [optional] 
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

# **get_data40**
> Report get_data40(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, settlement_point_source=settlement_point_source, settlement_point_sink=settlement_point_sink, mw_from=mw_from, mwto=mwto, price_from=price_from, price_to=price_to, offer_id=offer_id, multi_hour_block=multi_hour_block, crrid_from=crrid_from, crrid_to=crrid_to, page=page, size=size, sort=sort, dir=dir)

60 Day DAM PTP Obligation Option

60 Day DAM PTP Obligation Option

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
    api_instance = openapi_client.NP3966ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 'hour_ending_from_example' # str | Format - mm:ss. (optional)
    hour_ending_to = 'hour_ending_to_example' # str | Format - mm:ss. (optional)
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    settlement_point_source = 'settlement_point_source_example' # str | Format - abc123. (optional)
    settlement_point_sink = 'settlement_point_sink_example' # str | Format - abc123. (optional)
    mw_from = 3.4 # float | Format - ####.###. (optional)
    mwto = 3.4 # float | Format - ####.###. (optional)
    price_from = 56 # int | Format - ###. (optional)
    price_to = 56 # int | Format - ###. (optional)
    offer_id = 'offer_id_example' # str | Format - abc123. (optional)
    multi_hour_block = True # bool | Format - true | false. (optional)
    crrid_from = 56 # int | Format - ###. (optional)
    crrid_to = 56 # int | Format - ###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day DAM PTP Obligation Option
        api_response = api_instance.get_data40(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, settlement_point_source=settlement_point_source, settlement_point_sink=settlement_point_sink, mw_from=mw_from, mwto=mwto, price_from=price_from, price_to=price_to, offer_id=offer_id, multi_hour_block=multi_hour_block, crrid_from=crrid_from, crrid_to=crrid_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3966ERApi->get_data40:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3966ERApi->get_data40: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **str**| Format - mm:ss. | [optional] 
 **hour_ending_to** | **str**| Format - mm:ss. | [optional] 
 **qse_name** | **str**| Format - abc123. | [optional] 
 **settlement_point_source** | **str**| Format - abc123. | [optional] 
 **settlement_point_sink** | **str**| Format - abc123. | [optional] 
 **mw_from** | **float**| Format - ####.###. | [optional] 
 **mwto** | **float**| Format - ####.###. | [optional] 
 **price_from** | **int**| Format - ###. | [optional] 
 **price_to** | **int**| Format - ###. | [optional] 
 **offer_id** | **str**| Format - abc123. | [optional] 
 **multi_hour_block** | **bool**| Format - true | false. | [optional] 
 **crrid_from** | **int**| Format - ###. | [optional] 
 **crrid_to** | **int**| Format - ###. | [optional] 
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

# **get_data41**
> Report get_data41(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, settlement_point_source=settlement_point_source, settlement_point_sink=settlement_point_sink, ptp_bid_mw_from=ptp_bid_mw_from, ptp_bid_mwto=ptp_bid_mwto, ptp_bid_price_from=ptp_bid_price_from, ptp_bid_price_to=ptp_bid_price_to, bid_id=bid_id, multi_hour_block=multi_hour_block, page=page, size=size, sort=sort, dir=dir)

60 Day DAM PTP Obligation Bids

60 Day DAM PTP Obligation Bids

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
    api_instance = openapi_client.NP3966ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 'hour_ending_from_example' # str | Format - mm:ss. (optional)
    hour_ending_to = 'hour_ending_to_example' # str | Format - mm:ss. (optional)
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    settlement_point_source = 'settlement_point_source_example' # str | Format - abc123. (optional)
    settlement_point_sink = 'settlement_point_sink_example' # str | Format - abc123. (optional)
    ptp_bid_mw_from = 3.4 # float | Format - ####.###. (optional)
    ptp_bid_mwto = 3.4 # float | Format - ####.###. (optional)
    ptp_bid_price_from = 3.4 # float | Format - ####.###. (optional)
    ptp_bid_price_to = 3.4 # float | Format - ####.###. (optional)
    bid_id = 'bid_id_example' # str | Format - abc123. (optional)
    multi_hour_block = True # bool | Format - true | false. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day DAM PTP Obligation Bids
        api_response = api_instance.get_data41(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, settlement_point_source=settlement_point_source, settlement_point_sink=settlement_point_sink, ptp_bid_mw_from=ptp_bid_mw_from, ptp_bid_mwto=ptp_bid_mwto, ptp_bid_price_from=ptp_bid_price_from, ptp_bid_price_to=ptp_bid_price_to, bid_id=bid_id, multi_hour_block=multi_hour_block, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3966ERApi->get_data41:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3966ERApi->get_data41: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **str**| Format - mm:ss. | [optional] 
 **hour_ending_to** | **str**| Format - mm:ss. | [optional] 
 **qse_name** | **str**| Format - abc123. | [optional] 
 **settlement_point_source** | **str**| Format - abc123. | [optional] 
 **settlement_point_sink** | **str**| Format - abc123. | [optional] 
 **ptp_bid_mw_from** | **float**| Format - ####.###. | [optional] 
 **ptp_bid_mwto** | **float**| Format - ####.###. | [optional] 
 **ptp_bid_price_from** | **float**| Format - ####.###. | [optional] 
 **ptp_bid_price_to** | **float**| Format - ####.###. | [optional] 
 **bid_id** | **str**| Format - abc123. | [optional] 
 **multi_hour_block** | **bool**| Format - true | false. | [optional] 
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

# **get_data42**
> Report get_data42(ocp_apim_subscription_key, settlement_point_source=settlement_point_source, settlement_point_sink=settlement_point_sink, ptp_bid_award_mw_from=ptp_bid_award_mw_from, ptp_bid_award_mwto=ptp_bid_award_mwto, ptp_bid_price_from=ptp_bid_price_from, ptp_bid_price_to=ptp_bid_price_to, bid_id=bid_id, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, page=page, size=size, sort=sort, dir=dir)

60 Day DAM PTP Obligation Bid Awards

60 Day DAM PTP Obligation Bid Awards

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
    api_instance = openapi_client.NP3966ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    settlement_point_source = 'settlement_point_source_example' # str | Format - abc123. (optional)
    settlement_point_sink = 'settlement_point_sink_example' # str | Format - abc123. (optional)
    ptp_bid_award_mw_from = 3.4 # float | Format - ####.###. (optional)
    ptp_bid_award_mwto = 3.4 # float | Format - ####.###. (optional)
    ptp_bid_price_from = 3.4 # float | Format - ####.###. (optional)
    ptp_bid_price_to = 3.4 # float | Format - ####.###. (optional)
    bid_id = 'bid_id_example' # str | Format - abc123. (optional)
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 'hour_ending_from_example' # str | Format - mm:ss. (optional)
    hour_ending_to = 'hour_ending_to_example' # str | Format - mm:ss. (optional)
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day DAM PTP Obligation Bid Awards
        api_response = api_instance.get_data42(ocp_apim_subscription_key, settlement_point_source=settlement_point_source, settlement_point_sink=settlement_point_sink, ptp_bid_award_mw_from=ptp_bid_award_mw_from, ptp_bid_award_mwto=ptp_bid_award_mwto, ptp_bid_price_from=ptp_bid_price_from, ptp_bid_price_to=ptp_bid_price_to, bid_id=bid_id, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3966ERApi->get_data42:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3966ERApi->get_data42: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **settlement_point_source** | **str**| Format - abc123. | [optional] 
 **settlement_point_sink** | **str**| Format - abc123. | [optional] 
 **ptp_bid_award_mw_from** | **float**| Format - ####.###. | [optional] 
 **ptp_bid_award_mwto** | **float**| Format - ####.###. | [optional] 
 **ptp_bid_price_from** | **float**| Format - ####.###. | [optional] 
 **ptp_bid_price_to** | **float**| Format - ####.###. | [optional] 
 **bid_id** | **str**| Format - abc123. | [optional] 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **str**| Format - mm:ss. | [optional] 
 **hour_ending_to** | **str**| Format - mm:ss. | [optional] 
 **qse_name** | **str**| Format - abc123. | [optional] 
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

# **get_data43**
> Report get_data43(ocp_apim_subscription_key, regupmcpc_from=regupmcpc_from, regupmcpcto=regupmcpcto, regdn_awarded_from=regdn_awarded_from, regdn_awarded_to=regdn_awarded_to, regdnmcpc_from=regdnmcpc_from, regdnmcpcto=regdnmcpcto, rrspfr_awarded_from=rrspfr_awarded_from, rrspfr_awarded_to=rrspfr_awarded_to, rrsffr_awarded_from=rrsffr_awarded_from, rrsffr_awarded_to=rrsffr_awarded_to, rrsufr_awarded_from=rrsufr_awarded_from, rrsufr_awarded_to=rrsufr_awarded_to, rrsmcpc_from=rrsmcpc_from, rrsmcpcto=rrsmcpcto, nspin_awarded_from=nspin_awarded_from, nspin_awarded_to=nspin_awarded_to, nspinmcpc_from=nspinmcpc_from, nspinmcpcto=nspinmcpcto, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, load_resource_name=load_resource_name, max_power_consumption_from=max_power_consumption_from, max_power_consumption_to=max_power_consumption_to, low_power_consumption_from=low_power_consumption_from, low_power_consumption_to=low_power_consumption_to, regup_awarded_from=regup_awarded_from, regup_awarded_to=regup_awarded_to, page=page, size=size, sort=sort, dir=dir)

60 Day DAM Load Resource Data

60 Day DAM Load Resource Data

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
    api_instance = openapi_client.NP3966ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    regupmcpc_from = 3.4 # float | Format - ####.###. (optional)
    regupmcpcto = 3.4 # float | Format - ####.###. (optional)
    regdn_awarded_from = 3.4 # float | Format - ####.###. (optional)
    regdn_awarded_to = 3.4 # float | Format - ####.###. (optional)
    regdnmcpc_from = 3.4 # float | Format - ####.###. (optional)
    regdnmcpcto = 3.4 # float | Format - ####.###. (optional)
    rrspfr_awarded_from = 3.4 # float | Format - ####.###. (optional)
    rrspfr_awarded_to = 3.4 # float | Format - ####.###. (optional)
    rrsffr_awarded_from = 3.4 # float | Format - ####.###. (optional)
    rrsffr_awarded_to = 3.4 # float | Format - ####.###. (optional)
    rrsufr_awarded_from = 3.4 # float | Format - ####.###. (optional)
    rrsufr_awarded_to = 3.4 # float | Format - ####.###. (optional)
    rrsmcpc_from = 3.4 # float | Format - ####.###. (optional)
    rrsmcpcto = 3.4 # float | Format - ####.###. (optional)
    nspin_awarded_from = 3.4 # float | Format - ####.###. (optional)
    nspin_awarded_to = 3.4 # float | Format - ####.###. (optional)
    nspinmcpc_from = 3.4 # float | Format - ####.###. (optional)
    nspinmcpcto = 3.4 # float | Format - ####.###. (optional)
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 'hour_ending_from_example' # str | Format - mm:ss. (optional)
    hour_ending_to = 'hour_ending_to_example' # str | Format - mm:ss. (optional)
    load_resource_name = 'load_resource_name_example' # str | Format - abc123. (optional)
    max_power_consumption_from = 3.4 # float | Format - ####.###. (optional)
    max_power_consumption_to = 3.4 # float | Format - ####.###. (optional)
    low_power_consumption_from = 3.4 # float | Format - ####.###. (optional)
    low_power_consumption_to = 3.4 # float | Format - ####.###. (optional)
    regup_awarded_from = 3.4 # float | Format - ####.###. (optional)
    regup_awarded_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day DAM Load Resource Data
        api_response = api_instance.get_data43(ocp_apim_subscription_key, regupmcpc_from=regupmcpc_from, regupmcpcto=regupmcpcto, regdn_awarded_from=regdn_awarded_from, regdn_awarded_to=regdn_awarded_to, regdnmcpc_from=regdnmcpc_from, regdnmcpcto=regdnmcpcto, rrspfr_awarded_from=rrspfr_awarded_from, rrspfr_awarded_to=rrspfr_awarded_to, rrsffr_awarded_from=rrsffr_awarded_from, rrsffr_awarded_to=rrsffr_awarded_to, rrsufr_awarded_from=rrsufr_awarded_from, rrsufr_awarded_to=rrsufr_awarded_to, rrsmcpc_from=rrsmcpc_from, rrsmcpcto=rrsmcpcto, nspin_awarded_from=nspin_awarded_from, nspin_awarded_to=nspin_awarded_to, nspinmcpc_from=nspinmcpc_from, nspinmcpcto=nspinmcpcto, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, load_resource_name=load_resource_name, max_power_consumption_from=max_power_consumption_from, max_power_consumption_to=max_power_consumption_to, low_power_consumption_from=low_power_consumption_from, low_power_consumption_to=low_power_consumption_to, regup_awarded_from=regup_awarded_from, regup_awarded_to=regup_awarded_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3966ERApi->get_data43:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3966ERApi->get_data43: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **regupmcpc_from** | **float**| Format - ####.###. | [optional] 
 **regupmcpcto** | **float**| Format - ####.###. | [optional] 
 **regdn_awarded_from** | **float**| Format - ####.###. | [optional] 
 **regdn_awarded_to** | **float**| Format - ####.###. | [optional] 
 **regdnmcpc_from** | **float**| Format - ####.###. | [optional] 
 **regdnmcpcto** | **float**| Format - ####.###. | [optional] 
 **rrspfr_awarded_from** | **float**| Format - ####.###. | [optional] 
 **rrspfr_awarded_to** | **float**| Format - ####.###. | [optional] 
 **rrsffr_awarded_from** | **float**| Format - ####.###. | [optional] 
 **rrsffr_awarded_to** | **float**| Format - ####.###. | [optional] 
 **rrsufr_awarded_from** | **float**| Format - ####.###. | [optional] 
 **rrsufr_awarded_to** | **float**| Format - ####.###. | [optional] 
 **rrsmcpc_from** | **float**| Format - ####.###. | [optional] 
 **rrsmcpcto** | **float**| Format - ####.###. | [optional] 
 **nspin_awarded_from** | **float**| Format - ####.###. | [optional] 
 **nspin_awarded_to** | **float**| Format - ####.###. | [optional] 
 **nspinmcpc_from** | **float**| Format - ####.###. | [optional] 
 **nspinmcpcto** | **float**| Format - ####.###. | [optional] 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **str**| Format - mm:ss. | [optional] 
 **hour_ending_to** | **str**| Format - mm:ss. | [optional] 
 **load_resource_name** | **str**| Format - abc123. | [optional] 
 **max_power_consumption_from** | **float**| Format - ####.###. | [optional] 
 **max_power_consumption_to** | **float**| Format - ####.###. | [optional] 
 **low_power_consumption_from** | **float**| Format - ####.###. | [optional] 
 **low_power_consumption_to** | **float**| Format - ####.###. | [optional] 
 **regup_awarded_from** | **float**| Format - ####.###. | [optional] 
 **regup_awarded_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data44**
> Report get_data44(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, dme_name=dme_name, load_resource_name=load_resource_name, multi_hour_block=multi_hour_block, block_indicator1=block_indicator1, price1_rrspfr_from=price1_rrspfr_from, price1_rrspfrto=price1_rrspfrto, price1_rrsffr_from=price1_rrsffr_from, price1_rrsffrto=price1_rrsffrto, price1_rrsufr_from=price1_rrsufr_from, price1_rrsufrto=price1_rrsufrto, price1_online_nspin_from=price1_online_nspin_from, price1_online_nspinto=price1_online_nspinto, price1_regup_from=price1_regup_from, price1_regupto=price1_regupto, price1_regdn_from=price1_regdn_from, price1_regdnto=price1_regdnto, price1_offline_nspin_from=price1_offline_nspin_from, price1_offline_nspinto=price1_offline_nspinto, quantity_mw1_from=quantity_mw1_from, quantity_mw1_to=quantity_mw1_to, block_indicator2=block_indicator2, price2_rrspfr_from=price2_rrspfr_from, price2_rrspfrto=price2_rrspfrto, price2_rrsffr_from=price2_rrsffr_from, price2_rrsffrto=price2_rrsffrto, price2_rrsufr_from=price2_rrsufr_from, price2_rrsufrto=price2_rrsufrto, price2_online_nspin_from=price2_online_nspin_from, price2_online_nspinto=price2_online_nspinto, price2_regup_from=price2_regup_from, price2_regupto=price2_regupto, price2_regdn_from=price2_regdn_from, price2_regdnto=price2_regdnto, price2_offline_nspin_from=price2_offline_nspin_from, price2_offline_nspinto=price2_offline_nspinto, quantity_mw2_from=quantity_mw2_from, quantity_mw2_to=quantity_mw2_to, block_indicator3=block_indicator3, price3_rrspfr_from=price3_rrspfr_from, price3_rrspfrto=price3_rrspfrto, price3_rrsffr_from=price3_rrsffr_from, price3_rrsffrto=price3_rrsffrto, price3_rrsufr_from=price3_rrsufr_from, price3_rrsufrto=price3_rrsufrto, price3_online_nspin_from=price3_online_nspin_from, price3_online_nspinto=price3_online_nspinto, price3_regup_from=price3_regup_from, price3_regupto=price3_regupto, price3_regdn_from=price3_regdn_from, price3_regdnto=price3_regdnto, price3_offline_nspin_from=price3_offline_nspin_from, price3_offline_nspinto=price3_offline_nspinto, quantity_mw3_from=quantity_mw3_from, quantity_mw3_to=quantity_mw3_to, block_indicator4=block_indicator4, price4_rrspfr_from=price4_rrspfr_from, price4_rrspfrto=price4_rrspfrto, price4_rrsffr_from=price4_rrsffr_from, price4_rrsffrto=price4_rrsffrto, price4_rrsufr_from=price4_rrsufr_from, price4_rrsufrto=price4_rrsufrto, price4_online_nspin_from=price4_online_nspin_from, price4_online_nspinto=price4_online_nspinto, price4_regup_from=price4_regup_from, price4_regupto=price4_regupto, price4_regdn_from=price4_regdn_from, price4_regdnto=price4_regdnto, price4_offline_nspin_from=price4_offline_nspin_from, price4_offline_nspinto=price4_offline_nspinto, quantity_mw4_from=quantity_mw4_from, quantity_mw4_to=quantity_mw4_to, block_indicator5=block_indicator5, price5_rrspfr_from=price5_rrspfr_from, price5_rrspfrto=price5_rrspfrto, price5_rrsffr_from=price5_rrsffr_from, price5_rrsffrto=price5_rrsffrto, price5_rrsufr_from=price5_rrsufr_from, price5_rrsufrto=price5_rrsufrto, price5_online_nspin_from=price5_online_nspin_from, price5_online_nspinto=price5_online_nspinto, price5_regup_from=price5_regup_from, price5_regupto=price5_regupto, price5_regdn_from=price5_regdn_from, price5_regdnto=price5_regdnto, price5_offline_nspin_from=price5_offline_nspin_from, price5_offline_nspinto=price5_offline_nspinto, quantity_mw5_from=quantity_mw5_from, quantity_mw5_to=quantity_mw5_to, nclr_flag=nclr_flag, page=page, size=size, sort=sort, dir=dir)

60 Day DAM Load Resources AS Offers

60 Day DAM Load Resources AS Offers

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
    api_instance = openapi_client.NP3966ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 'hour_ending_from_example' # str | Format - mm:ss. (optional)
    hour_ending_to = 'hour_ending_to_example' # str | Format - mm:ss. (optional)
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    dme_name = 'dme_name_example' # str | Format - abc123. (optional)
    load_resource_name = 'load_resource_name_example' # str | Format - abc123. (optional)
    multi_hour_block = True # bool | Format - true | false. (optional)
    block_indicator1 = True # bool | Format - true | false. (optional)
    price1_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price1_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price1_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price1_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price1_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price1_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price1_online_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price1_online_nspinto = 3.4 # float | Format - ####.###. (optional)
    price1_regup_from = 3.4 # float | Format - ####.###. (optional)
    price1_regupto = 3.4 # float | Format - ####.###. (optional)
    price1_regdn_from = 3.4 # float | Format - ####.###. (optional)
    price1_regdnto = 3.4 # float | Format - ####.###. (optional)
    price1_offline_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price1_offline_nspinto = 3.4 # float | Format - ####.###. (optional)
    quantity_mw1_from = 56 # int | Format - ###. (optional)
    quantity_mw1_to = 56 # int | Format - ###. (optional)
    block_indicator2 = True # bool | Format - true | false. (optional)
    price2_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price2_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price2_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price2_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price2_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price2_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price2_online_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price2_online_nspinto = 3.4 # float | Format - ####.###. (optional)
    price2_regup_from = 3.4 # float | Format - ####.###. (optional)
    price2_regupto = 3.4 # float | Format - ####.###. (optional)
    price2_regdn_from = 3.4 # float | Format - ####.###. (optional)
    price2_regdnto = 3.4 # float | Format - ####.###. (optional)
    price2_offline_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price2_offline_nspinto = 3.4 # float | Format - ####.###. (optional)
    quantity_mw2_from = 56 # int | Format - ###. (optional)
    quantity_mw2_to = 56 # int | Format - ###. (optional)
    block_indicator3 = True # bool | Format - true | false. (optional)
    price3_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price3_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price3_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price3_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price3_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price3_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price3_online_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price3_online_nspinto = 3.4 # float | Format - ####.###. (optional)
    price3_regup_from = 3.4 # float | Format - ####.###. (optional)
    price3_regupto = 3.4 # float | Format - ####.###. (optional)
    price3_regdn_from = 3.4 # float | Format - ####.###. (optional)
    price3_regdnto = 3.4 # float | Format - ####.###. (optional)
    price3_offline_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price3_offline_nspinto = 3.4 # float | Format - ####.###. (optional)
    quantity_mw3_from = 56 # int | Format - ###. (optional)
    quantity_mw3_to = 56 # int | Format - ###. (optional)
    block_indicator4 = True # bool | Format - true | false. (optional)
    price4_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price4_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price4_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price4_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price4_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price4_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price4_online_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price4_online_nspinto = 3.4 # float | Format - ####.###. (optional)
    price4_regup_from = 3.4 # float | Format - ####.###. (optional)
    price4_regupto = 3.4 # float | Format - ####.###. (optional)
    price4_regdn_from = 3.4 # float | Format - ####.###. (optional)
    price4_regdnto = 3.4 # float | Format - ####.###. (optional)
    price4_offline_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price4_offline_nspinto = 3.4 # float | Format - ####.###. (optional)
    quantity_mw4_from = 56 # int | Format - ###. (optional)
    quantity_mw4_to = 56 # int | Format - ###. (optional)
    block_indicator5 = True # bool | Format - true | false. (optional)
    price5_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price5_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price5_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price5_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price5_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price5_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price5_online_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price5_online_nspinto = 3.4 # float | Format - ####.###. (optional)
    price5_regup_from = 3.4 # float | Format - ####.###. (optional)
    price5_regupto = 3.4 # float | Format - ####.###. (optional)
    price5_regdn_from = 3.4 # float | Format - ####.###. (optional)
    price5_regdnto = 3.4 # float | Format - ####.###. (optional)
    price5_offline_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price5_offline_nspinto = 3.4 # float | Format - ####.###. (optional)
    quantity_mw5_from = 56 # int | Format - ###. (optional)
    quantity_mw5_to = 56 # int | Format - ###. (optional)
    nclr_flag = True # bool | Format - true | false. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day DAM Load Resources AS Offers
        api_response = api_instance.get_data44(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, dme_name=dme_name, load_resource_name=load_resource_name, multi_hour_block=multi_hour_block, block_indicator1=block_indicator1, price1_rrspfr_from=price1_rrspfr_from, price1_rrspfrto=price1_rrspfrto, price1_rrsffr_from=price1_rrsffr_from, price1_rrsffrto=price1_rrsffrto, price1_rrsufr_from=price1_rrsufr_from, price1_rrsufrto=price1_rrsufrto, price1_online_nspin_from=price1_online_nspin_from, price1_online_nspinto=price1_online_nspinto, price1_regup_from=price1_regup_from, price1_regupto=price1_regupto, price1_regdn_from=price1_regdn_from, price1_regdnto=price1_regdnto, price1_offline_nspin_from=price1_offline_nspin_from, price1_offline_nspinto=price1_offline_nspinto, quantity_mw1_from=quantity_mw1_from, quantity_mw1_to=quantity_mw1_to, block_indicator2=block_indicator2, price2_rrspfr_from=price2_rrspfr_from, price2_rrspfrto=price2_rrspfrto, price2_rrsffr_from=price2_rrsffr_from, price2_rrsffrto=price2_rrsffrto, price2_rrsufr_from=price2_rrsufr_from, price2_rrsufrto=price2_rrsufrto, price2_online_nspin_from=price2_online_nspin_from, price2_online_nspinto=price2_online_nspinto, price2_regup_from=price2_regup_from, price2_regupto=price2_regupto, price2_regdn_from=price2_regdn_from, price2_regdnto=price2_regdnto, price2_offline_nspin_from=price2_offline_nspin_from, price2_offline_nspinto=price2_offline_nspinto, quantity_mw2_from=quantity_mw2_from, quantity_mw2_to=quantity_mw2_to, block_indicator3=block_indicator3, price3_rrspfr_from=price3_rrspfr_from, price3_rrspfrto=price3_rrspfrto, price3_rrsffr_from=price3_rrsffr_from, price3_rrsffrto=price3_rrsffrto, price3_rrsufr_from=price3_rrsufr_from, price3_rrsufrto=price3_rrsufrto, price3_online_nspin_from=price3_online_nspin_from, price3_online_nspinto=price3_online_nspinto, price3_regup_from=price3_regup_from, price3_regupto=price3_regupto, price3_regdn_from=price3_regdn_from, price3_regdnto=price3_regdnto, price3_offline_nspin_from=price3_offline_nspin_from, price3_offline_nspinto=price3_offline_nspinto, quantity_mw3_from=quantity_mw3_from, quantity_mw3_to=quantity_mw3_to, block_indicator4=block_indicator4, price4_rrspfr_from=price4_rrspfr_from, price4_rrspfrto=price4_rrspfrto, price4_rrsffr_from=price4_rrsffr_from, price4_rrsffrto=price4_rrsffrto, price4_rrsufr_from=price4_rrsufr_from, price4_rrsufrto=price4_rrsufrto, price4_online_nspin_from=price4_online_nspin_from, price4_online_nspinto=price4_online_nspinto, price4_regup_from=price4_regup_from, price4_regupto=price4_regupto, price4_regdn_from=price4_regdn_from, price4_regdnto=price4_regdnto, price4_offline_nspin_from=price4_offline_nspin_from, price4_offline_nspinto=price4_offline_nspinto, quantity_mw4_from=quantity_mw4_from, quantity_mw4_to=quantity_mw4_to, block_indicator5=block_indicator5, price5_rrspfr_from=price5_rrspfr_from, price5_rrspfrto=price5_rrspfrto, price5_rrsffr_from=price5_rrsffr_from, price5_rrsffrto=price5_rrsffrto, price5_rrsufr_from=price5_rrsufr_from, price5_rrsufrto=price5_rrsufrto, price5_online_nspin_from=price5_online_nspin_from, price5_online_nspinto=price5_online_nspinto, price5_regup_from=price5_regup_from, price5_regupto=price5_regupto, price5_regdn_from=price5_regdn_from, price5_regdnto=price5_regdnto, price5_offline_nspin_from=price5_offline_nspin_from, price5_offline_nspinto=price5_offline_nspinto, quantity_mw5_from=quantity_mw5_from, quantity_mw5_to=quantity_mw5_to, nclr_flag=nclr_flag, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3966ERApi->get_data44:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3966ERApi->get_data44: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **str**| Format - mm:ss. | [optional] 
 **hour_ending_to** | **str**| Format - mm:ss. | [optional] 
 **qse_name** | **str**| Format - abc123. | [optional] 
 **dme_name** | **str**| Format - abc123. | [optional] 
 **load_resource_name** | **str**| Format - abc123. | [optional] 
 **multi_hour_block** | **bool**| Format - true | false. | [optional] 
 **block_indicator1** | **bool**| Format - true | false. | [optional] 
 **price1_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price1_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price1_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price1_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price1_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price1_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price1_online_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price1_online_nspinto** | **float**| Format - ####.###. | [optional] 
 **price1_regup_from** | **float**| Format - ####.###. | [optional] 
 **price1_regupto** | **float**| Format - ####.###. | [optional] 
 **price1_regdn_from** | **float**| Format - ####.###. | [optional] 
 **price1_regdnto** | **float**| Format - ####.###. | [optional] 
 **price1_offline_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price1_offline_nspinto** | **float**| Format - ####.###. | [optional] 
 **quantity_mw1_from** | **int**| Format - ###. | [optional] 
 **quantity_mw1_to** | **int**| Format - ###. | [optional] 
 **block_indicator2** | **bool**| Format - true | false. | [optional] 
 **price2_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price2_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price2_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price2_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price2_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price2_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price2_online_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price2_online_nspinto** | **float**| Format - ####.###. | [optional] 
 **price2_regup_from** | **float**| Format - ####.###. | [optional] 
 **price2_regupto** | **float**| Format - ####.###. | [optional] 
 **price2_regdn_from** | **float**| Format - ####.###. | [optional] 
 **price2_regdnto** | **float**| Format - ####.###. | [optional] 
 **price2_offline_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price2_offline_nspinto** | **float**| Format - ####.###. | [optional] 
 **quantity_mw2_from** | **int**| Format - ###. | [optional] 
 **quantity_mw2_to** | **int**| Format - ###. | [optional] 
 **block_indicator3** | **bool**| Format - true | false. | [optional] 
 **price3_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price3_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price3_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price3_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price3_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price3_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price3_online_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price3_online_nspinto** | **float**| Format - ####.###. | [optional] 
 **price3_regup_from** | **float**| Format - ####.###. | [optional] 
 **price3_regupto** | **float**| Format - ####.###. | [optional] 
 **price3_regdn_from** | **float**| Format - ####.###. | [optional] 
 **price3_regdnto** | **float**| Format - ####.###. | [optional] 
 **price3_offline_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price3_offline_nspinto** | **float**| Format - ####.###. | [optional] 
 **quantity_mw3_from** | **int**| Format - ###. | [optional] 
 **quantity_mw3_to** | **int**| Format - ###. | [optional] 
 **block_indicator4** | **bool**| Format - true | false. | [optional] 
 **price4_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price4_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price4_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price4_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price4_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price4_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price4_online_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price4_online_nspinto** | **float**| Format - ####.###. | [optional] 
 **price4_regup_from** | **float**| Format - ####.###. | [optional] 
 **price4_regupto** | **float**| Format - ####.###. | [optional] 
 **price4_regdn_from** | **float**| Format - ####.###. | [optional] 
 **price4_regdnto** | **float**| Format - ####.###. | [optional] 
 **price4_offline_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price4_offline_nspinto** | **float**| Format - ####.###. | [optional] 
 **quantity_mw4_from** | **int**| Format - ###. | [optional] 
 **quantity_mw4_to** | **int**| Format - ###. | [optional] 
 **block_indicator5** | **bool**| Format - true | false. | [optional] 
 **price5_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price5_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price5_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price5_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price5_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price5_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price5_online_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price5_online_nspinto** | **float**| Format - ####.###. | [optional] 
 **price5_regup_from** | **float**| Format - ####.###. | [optional] 
 **price5_regupto** | **float**| Format - ####.###. | [optional] 
 **price5_regdn_from** | **float**| Format - ####.###. | [optional] 
 **price5_regdnto** | **float**| Format - ####.###. | [optional] 
 **price5_offline_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price5_offline_nspinto** | **float**| Format - ####.###. | [optional] 
 **quantity_mw5_from** | **int**| Format - ###. | [optional] 
 **quantity_mw5_to** | **int**| Format - ###. | [optional] 
 **nclr_flag** | **bool**| Format - true | false. | [optional] 
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

# **get_data45**
> Report get_data45(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, dme_name=dme_name, resource_name=resource_name, resource_type=resource_type, qse_submitted_curve_mw1_from=qse_submitted_curve_mw1_from, qse_submitted_curve_mw1_to=qse_submitted_curve_mw1_to, qse_submitted_curve_price1_from=qse_submitted_curve_price1_from, qse_submitted_curve_price1_to=qse_submitted_curve_price1_to, qse_submitted_curve_mw2_from=qse_submitted_curve_mw2_from, qse_submitted_curve_mw2_to=qse_submitted_curve_mw2_to, qse_submitted_curve_price2_from=qse_submitted_curve_price2_from, qse_submitted_curve_price2_to=qse_submitted_curve_price2_to, qse_submitted_curve_mw3_from=qse_submitted_curve_mw3_from, qse_submitted_curve_mw3_to=qse_submitted_curve_mw3_to, qse_submitted_curve_price3_from=qse_submitted_curve_price3_from, qse_submitted_curve_price3_to=qse_submitted_curve_price3_to, qse_submitted_curve_mw4_from=qse_submitted_curve_mw4_from, qse_submitted_curve_mw4_to=qse_submitted_curve_mw4_to, qse_submitted_curve_price4_from=qse_submitted_curve_price4_from, qse_submitted_curve_price4_to=qse_submitted_curve_price4_to, qse_submitted_curve_mw5_from=qse_submitted_curve_mw5_from, qse_submitted_curve_mw5_to=qse_submitted_curve_mw5_to, qse_submitted_curve_price5_from=qse_submitted_curve_price5_from, qse_submitted_curve_price5_to=qse_submitted_curve_price5_to, qse_submitted_curve_mw6_from=qse_submitted_curve_mw6_from, qse_submitted_curve_mw6_to=qse_submitted_curve_mw6_to, qse_submitted_curve_price6_from=qse_submitted_curve_price6_from, qse_submitted_curve_price6_to=qse_submitted_curve_price6_to, qse_submitted_curve_mw7_from=qse_submitted_curve_mw7_from, qse_submitted_curve_mw7_to=qse_submitted_curve_mw7_to, qse_submitted_curve_price7_from=qse_submitted_curve_price7_from, qse_submitted_curve_price7_to=qse_submitted_curve_price7_to, qse_submitted_curve_mw8_from=qse_submitted_curve_mw8_from, qse_submitted_curve_mw8_to=qse_submitted_curve_mw8_to, qse_submitted_curve_price8_from=qse_submitted_curve_price8_from, qse_submitted_curve_price8_to=qse_submitted_curve_price8_to, qse_submitted_curve_mw9_from=qse_submitted_curve_mw9_from, qse_submitted_curve_mw9_to=qse_submitted_curve_mw9_to, qse_submitted_curve_price9_from=qse_submitted_curve_price9_from, qse_submitted_curve_price9_to=qse_submitted_curve_price9_to, qse_submitted_curve_mw10_from=qse_submitted_curve_mw10_from, qse_submitted_curve_mw10_to=qse_submitted_curve_mw10_to, qse_submitted_curve_price10_from=qse_submitted_curve_price10_from, qse_submitted_curve_price10_to=qse_submitted_curve_price10_to, start_up_hot_from=start_up_hot_from, start_up_hot_to=start_up_hot_to, start_up_inter_from=start_up_inter_from, start_up_inter_to=start_up_inter_to, start_up_cold_from=start_up_cold_from, start_up_cold_to=start_up_cold_to, min_gen_cost_from=min_gen_cost_from, min_gen_cost_to=min_gen_cost_to, hsl_from=hsl_from, hslto=hslto, lsl_from=lsl_from, lslto=lslto, resource_status=resource_status, awarded_quantity_from=awarded_quantity_from, awarded_quantity_to=awarded_quantity_to, settlement_point_name=settlement_point_name, energy_settlement_point_price_from=energy_settlement_point_price_from, energy_settlement_point_price_to=energy_settlement_point_price_to, regup_awarded_from=regup_awarded_from, regup_awarded_to=regup_awarded_to, regupmcpc_from=regupmcpc_from, regupmcpcto=regupmcpcto, regdn_awarded_from=regdn_awarded_from, regdn_awarded_to=regdn_awarded_to, regdnmcpc_from=regdnmcpc_from, regdnmcpcto=regdnmcpcto, rrspfr_awarded_from=rrspfr_awarded_from, rrspfr_awarded_to=rrspfr_awarded_to, rrsffr_awarded_from=rrsffr_awarded_from, rrsffr_awarded_to=rrsffr_awarded_to, rrsufr_awarded_from=rrsufr_awarded_from, rrsufr_awarded_to=rrsufr_awarded_to, rrsmcpc_from=rrsmcpc_from, rrsmcpcto=rrsmcpcto, nspin_awarded_from=nspin_awarded_from, nspin_awarded_to=nspin_awarded_to, nspinmcpc_from=nspinmcpc_from, nspinmcpcto=nspinmcpcto, page=page, size=size, sort=sort, dir=dir)

60 Day DAM Generation Resource Data

60 Day DAM Generation Resource Data

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
    api_instance = openapi_client.NP3966ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 'hour_ending_from_example' # str | Format - mm:ss. (optional)
    hour_ending_to = 'hour_ending_to_example' # str | Format - mm:ss. (optional)
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    dme_name = 'dme_name_example' # str | Format - abc123. (optional)
    resource_name = 'resource_name_example' # str | Format - abc123. (optional)
    resource_type = 'resource_type_example' # str | Format - abc123. (optional)
    qse_submitted_curve_mw1_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw1_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price1_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price1_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw2_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw2_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price2_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price2_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw3_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw3_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price3_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price3_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw4_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw4_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price4_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price4_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw5_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw5_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price5_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price5_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw6_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw6_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price6_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price6_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw7_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw7_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price7_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price7_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw8_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw8_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price8_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price8_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw9_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw9_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price9_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price9_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw10_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_mw10_to = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price10_from = 3.4 # float | Format - ####.###. (optional)
    qse_submitted_curve_price10_to = 3.4 # float | Format - ####.###. (optional)
    start_up_hot_from = 3.4 # float | Format - ####.###. (optional)
    start_up_hot_to = 3.4 # float | Format - ####.###. (optional)
    start_up_inter_from = 3.4 # float | Format - ####.###. (optional)
    start_up_inter_to = 3.4 # float | Format - ####.###. (optional)
    start_up_cold_from = 3.4 # float | Format - ####.###. (optional)
    start_up_cold_to = 3.4 # float | Format - ####.###. (optional)
    min_gen_cost_from = 3.4 # float | Format - ####.###. (optional)
    min_gen_cost_to = 3.4 # float | Format - ####.###. (optional)
    hsl_from = 3.4 # float | Format - ####.###. (optional)
    hslto = 3.4 # float | Format - ####.###. (optional)
    lsl_from = 3.4 # float | Format - ####.###. (optional)
    lslto = 3.4 # float | Format - ####.###. (optional)
    resource_status = 'resource_status_example' # str | Format - abc123. (optional)
    awarded_quantity_from = 56 # int | Format - ###. (optional)
    awarded_quantity_to = 56 # int | Format - ###. (optional)
    settlement_point_name = 'settlement_point_name_example' # str | Format - abc123. (optional)
    energy_settlement_point_price_from = 3.4 # float | Format - ####.###. (optional)
    energy_settlement_point_price_to = 3.4 # float | Format - ####.###. (optional)
    regup_awarded_from = 3.4 # float | Format - ####.###. (optional)
    regup_awarded_to = 3.4 # float | Format - ####.###. (optional)
    regupmcpc_from = 3.4 # float | Format - ####.###. (optional)
    regupmcpcto = 3.4 # float | Format - ####.###. (optional)
    regdn_awarded_from = 3.4 # float | Format - ####.###. (optional)
    regdn_awarded_to = 3.4 # float | Format - ####.###. (optional)
    regdnmcpc_from = 3.4 # float | Format - ####.###. (optional)
    regdnmcpcto = 3.4 # float | Format - ####.###. (optional)
    rrspfr_awarded_from = 3.4 # float | Format - ####.###. (optional)
    rrspfr_awarded_to = 3.4 # float | Format - ####.###. (optional)
    rrsffr_awarded_from = 3.4 # float | Format - ####.###. (optional)
    rrsffr_awarded_to = 3.4 # float | Format - ####.###. (optional)
    rrsufr_awarded_from = 3.4 # float | Format - ####.###. (optional)
    rrsufr_awarded_to = 3.4 # float | Format - ####.###. (optional)
    rrsmcpc_from = 3.4 # float | Format - ####.###. (optional)
    rrsmcpcto = 3.4 # float | Format - ####.###. (optional)
    nspin_awarded_from = 3.4 # float | Format - ####.###. (optional)
    nspin_awarded_to = 3.4 # float | Format - ####.###. (optional)
    nspinmcpc_from = 3.4 # float | Format - ####.###. (optional)
    nspinmcpcto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day DAM Generation Resource Data
        api_response = api_instance.get_data45(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, dme_name=dme_name, resource_name=resource_name, resource_type=resource_type, qse_submitted_curve_mw1_from=qse_submitted_curve_mw1_from, qse_submitted_curve_mw1_to=qse_submitted_curve_mw1_to, qse_submitted_curve_price1_from=qse_submitted_curve_price1_from, qse_submitted_curve_price1_to=qse_submitted_curve_price1_to, qse_submitted_curve_mw2_from=qse_submitted_curve_mw2_from, qse_submitted_curve_mw2_to=qse_submitted_curve_mw2_to, qse_submitted_curve_price2_from=qse_submitted_curve_price2_from, qse_submitted_curve_price2_to=qse_submitted_curve_price2_to, qse_submitted_curve_mw3_from=qse_submitted_curve_mw3_from, qse_submitted_curve_mw3_to=qse_submitted_curve_mw3_to, qse_submitted_curve_price3_from=qse_submitted_curve_price3_from, qse_submitted_curve_price3_to=qse_submitted_curve_price3_to, qse_submitted_curve_mw4_from=qse_submitted_curve_mw4_from, qse_submitted_curve_mw4_to=qse_submitted_curve_mw4_to, qse_submitted_curve_price4_from=qse_submitted_curve_price4_from, qse_submitted_curve_price4_to=qse_submitted_curve_price4_to, qse_submitted_curve_mw5_from=qse_submitted_curve_mw5_from, qse_submitted_curve_mw5_to=qse_submitted_curve_mw5_to, qse_submitted_curve_price5_from=qse_submitted_curve_price5_from, qse_submitted_curve_price5_to=qse_submitted_curve_price5_to, qse_submitted_curve_mw6_from=qse_submitted_curve_mw6_from, qse_submitted_curve_mw6_to=qse_submitted_curve_mw6_to, qse_submitted_curve_price6_from=qse_submitted_curve_price6_from, qse_submitted_curve_price6_to=qse_submitted_curve_price6_to, qse_submitted_curve_mw7_from=qse_submitted_curve_mw7_from, qse_submitted_curve_mw7_to=qse_submitted_curve_mw7_to, qse_submitted_curve_price7_from=qse_submitted_curve_price7_from, qse_submitted_curve_price7_to=qse_submitted_curve_price7_to, qse_submitted_curve_mw8_from=qse_submitted_curve_mw8_from, qse_submitted_curve_mw8_to=qse_submitted_curve_mw8_to, qse_submitted_curve_price8_from=qse_submitted_curve_price8_from, qse_submitted_curve_price8_to=qse_submitted_curve_price8_to, qse_submitted_curve_mw9_from=qse_submitted_curve_mw9_from, qse_submitted_curve_mw9_to=qse_submitted_curve_mw9_to, qse_submitted_curve_price9_from=qse_submitted_curve_price9_from, qse_submitted_curve_price9_to=qse_submitted_curve_price9_to, qse_submitted_curve_mw10_from=qse_submitted_curve_mw10_from, qse_submitted_curve_mw10_to=qse_submitted_curve_mw10_to, qse_submitted_curve_price10_from=qse_submitted_curve_price10_from, qse_submitted_curve_price10_to=qse_submitted_curve_price10_to, start_up_hot_from=start_up_hot_from, start_up_hot_to=start_up_hot_to, start_up_inter_from=start_up_inter_from, start_up_inter_to=start_up_inter_to, start_up_cold_from=start_up_cold_from, start_up_cold_to=start_up_cold_to, min_gen_cost_from=min_gen_cost_from, min_gen_cost_to=min_gen_cost_to, hsl_from=hsl_from, hslto=hslto, lsl_from=lsl_from, lslto=lslto, resource_status=resource_status, awarded_quantity_from=awarded_quantity_from, awarded_quantity_to=awarded_quantity_to, settlement_point_name=settlement_point_name, energy_settlement_point_price_from=energy_settlement_point_price_from, energy_settlement_point_price_to=energy_settlement_point_price_to, regup_awarded_from=regup_awarded_from, regup_awarded_to=regup_awarded_to, regupmcpc_from=regupmcpc_from, regupmcpcto=regupmcpcto, regdn_awarded_from=regdn_awarded_from, regdn_awarded_to=regdn_awarded_to, regdnmcpc_from=regdnmcpc_from, regdnmcpcto=regdnmcpcto, rrspfr_awarded_from=rrspfr_awarded_from, rrspfr_awarded_to=rrspfr_awarded_to, rrsffr_awarded_from=rrsffr_awarded_from, rrsffr_awarded_to=rrsffr_awarded_to, rrsufr_awarded_from=rrsufr_awarded_from, rrsufr_awarded_to=rrsufr_awarded_to, rrsmcpc_from=rrsmcpc_from, rrsmcpcto=rrsmcpcto, nspin_awarded_from=nspin_awarded_from, nspin_awarded_to=nspin_awarded_to, nspinmcpc_from=nspinmcpc_from, nspinmcpcto=nspinmcpcto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3966ERApi->get_data45:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3966ERApi->get_data45: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **str**| Format - mm:ss. | [optional] 
 **hour_ending_to** | **str**| Format - mm:ss. | [optional] 
 **qse_name** | **str**| Format - abc123. | [optional] 
 **dme_name** | **str**| Format - abc123. | [optional] 
 **resource_name** | **str**| Format - abc123. | [optional] 
 **resource_type** | **str**| Format - abc123. | [optional] 
 **qse_submitted_curve_mw1_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw1_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price1_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price1_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw2_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw2_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price2_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price2_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw3_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw3_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price3_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price3_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw4_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw4_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price4_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price4_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw5_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw5_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price5_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price5_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw6_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw6_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price6_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price6_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw7_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw7_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price7_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price7_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw8_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw8_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price8_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price8_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw9_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw9_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price9_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price9_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw10_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_mw10_to** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price10_from** | **float**| Format - ####.###. | [optional] 
 **qse_submitted_curve_price10_to** | **float**| Format - ####.###. | [optional] 
 **start_up_hot_from** | **float**| Format - ####.###. | [optional] 
 **start_up_hot_to** | **float**| Format - ####.###. | [optional] 
 **start_up_inter_from** | **float**| Format - ####.###. | [optional] 
 **start_up_inter_to** | **float**| Format - ####.###. | [optional] 
 **start_up_cold_from** | **float**| Format - ####.###. | [optional] 
 **start_up_cold_to** | **float**| Format - ####.###. | [optional] 
 **min_gen_cost_from** | **float**| Format - ####.###. | [optional] 
 **min_gen_cost_to** | **float**| Format - ####.###. | [optional] 
 **hsl_from** | **float**| Format - ####.###. | [optional] 
 **hslto** | **float**| Format - ####.###. | [optional] 
 **lsl_from** | **float**| Format - ####.###. | [optional] 
 **lslto** | **float**| Format - ####.###. | [optional] 
 **resource_status** | **str**| Format - abc123. | [optional] 
 **awarded_quantity_from** | **int**| Format - ###. | [optional] 
 **awarded_quantity_to** | **int**| Format - ###. | [optional] 
 **settlement_point_name** | **str**| Format - abc123. | [optional] 
 **energy_settlement_point_price_from** | **float**| Format - ####.###. | [optional] 
 **energy_settlement_point_price_to** | **float**| Format - ####.###. | [optional] 
 **regup_awarded_from** | **float**| Format - ####.###. | [optional] 
 **regup_awarded_to** | **float**| Format - ####.###. | [optional] 
 **regupmcpc_from** | **float**| Format - ####.###. | [optional] 
 **regupmcpcto** | **float**| Format - ####.###. | [optional] 
 **regdn_awarded_from** | **float**| Format - ####.###. | [optional] 
 **regdn_awarded_to** | **float**| Format - ####.###. | [optional] 
 **regdnmcpc_from** | **float**| Format - ####.###. | [optional] 
 **regdnmcpcto** | **float**| Format - ####.###. | [optional] 
 **rrspfr_awarded_from** | **float**| Format - ####.###. | [optional] 
 **rrspfr_awarded_to** | **float**| Format - ####.###. | [optional] 
 **rrsffr_awarded_from** | **float**| Format - ####.###. | [optional] 
 **rrsffr_awarded_to** | **float**| Format - ####.###. | [optional] 
 **rrsufr_awarded_from** | **float**| Format - ####.###. | [optional] 
 **rrsufr_awarded_to** | **float**| Format - ####.###. | [optional] 
 **rrsmcpc_from** | **float**| Format - ####.###. | [optional] 
 **rrsmcpcto** | **float**| Format - ####.###. | [optional] 
 **nspin_awarded_from** | **float**| Format - ####.###. | [optional] 
 **nspin_awarded_to** | **float**| Format - ####.###. | [optional] 
 **nspinmcpc_from** | **float**| Format - ####.###. | [optional] 
 **nspinmcpcto** | **float**| Format - ####.###. | [optional] 
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

# **get_data46**
> Report get_data46(ocp_apim_subscription_key, price2_rrsffr_from=price2_rrsffr_from, price2_rrsffrto=price2_rrsffrto, price2_rrsufr_from=price2_rrsufr_from, price2_rrsufrto=price2_rrsufrto, price2_online_nspin_from=price2_online_nspin_from, price2_online_nspinto=price2_online_nspinto, price2_regup_from=price2_regup_from, price2_regupto=price2_regupto, price2_regdn_from=price2_regdn_from, price2_regdnto=price2_regdnto, price2_offline_nspin_from=price2_offline_nspin_from, price2_offline_nspinto=price2_offline_nspinto, quantity_mw2_from=quantity_mw2_from, quantity_mw2_to=quantity_mw2_to, block_indicator3=block_indicator3, price3_rrspfr_from=price3_rrspfr_from, price3_rrspfrto=price3_rrspfrto, price3_rrsffr_from=price3_rrsffr_from, price3_rrsffrto=price3_rrsffrto, price3_rrsufr_from=price3_rrsufr_from, price3_rrsufrto=price3_rrsufrto, price3_online_nspin_from=price3_online_nspin_from, price3_online_nspinto=price3_online_nspinto, price3_regup_from=price3_regup_from, price3_regupto=price3_regupto, price3_regdn_from=price3_regdn_from, price3_regdnto=price3_regdnto, price3_offline_nspin_from=price3_offline_nspin_from, price3_offline_nspinto=price3_offline_nspinto, quantity_mw3_from=quantity_mw3_from, quantity_mw3_to=quantity_mw3_to, block_indicator4=block_indicator4, price4_rrspfr_from=price4_rrspfr_from, price4_rrspfrto=price4_rrspfrto, price4_rrsffr_from=price4_rrsffr_from, price4_rrsffrto=price4_rrsffrto, price4_rrsufr_from=price4_rrsufr_from, price4_rrsufrto=price4_rrsufrto, price4_online_nspin_from=price4_online_nspin_from, price4_online_nspinto=price4_online_nspinto, price4_regup_from=price4_regup_from, price4_regupto=price4_regupto, price4_regdn_from=price4_regdn_from, price4_regdnto=price4_regdnto, price4_offline_nspin_from=price4_offline_nspin_from, price4_offline_nspinto=price4_offline_nspinto, quantity_mw4_from=quantity_mw4_from, quantity_mw4_to=quantity_mw4_to, block_indicator5=block_indicator5, price5_rrspfr_from=price5_rrspfr_from, price5_rrspfrto=price5_rrspfrto, price5_rrsffr_from=price5_rrsffr_from, price5_rrsffrto=price5_rrsffrto, price5_rrsufr_from=price5_rrsufr_from, price5_rrsufrto=price5_rrsufrto, price5_online_nspin_from=price5_online_nspin_from, price5_online_nspinto=price5_online_nspinto, price5_regup_from=price5_regup_from, price5_regupto=price5_regupto, price5_regdn_from=price5_regdn_from, price5_regdnto=price5_regdnto, price5_offline_nspin_from=price5_offline_nspin_from, price5_offline_nspinto=price5_offline_nspinto, quantity_mw5_from=quantity_mw5_from, quantity_mw5_to=quantity_mw5_to, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, dme_name=dme_name, resource_name=resource_name, multi_hour_block=multi_hour_block, block_indicator1=block_indicator1, price1_rrspfr_from=price1_rrspfr_from, price1_rrspfrto=price1_rrspfrto, price1_rrsffr_from=price1_rrsffr_from, price1_rrsffrto=price1_rrsffrto, price1_rrsufr_from=price1_rrsufr_from, price1_rrsufrto=price1_rrsufrto, price1_online_nspin_from=price1_online_nspin_from, price1_online_nspinto=price1_online_nspinto, price1_regup_from=price1_regup_from, price1_regupto=price1_regupto, price1_regdn_from=price1_regdn_from, price1_regdnto=price1_regdnto, price1_offline_nspin_from=price1_offline_nspin_from, price1_offline_nspinto=price1_offline_nspinto, quantity_mw1_from=quantity_mw1_from, quantity_mw1_to=quantity_mw1_to, block_indicator2=block_indicator2, price2_rrspfr_from=price2_rrspfr_from, price2_rrspfrto=price2_rrspfrto, page=page, size=size, sort=sort, dir=dir)

60 Day DAM Generation Resources AS Offers

60 Day DAM Generation Resources AS Offers

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
    api_instance = openapi_client.NP3966ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    price2_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price2_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price2_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price2_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price2_online_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price2_online_nspinto = 3.4 # float | Format - ####.###. (optional)
    price2_regup_from = 3.4 # float | Format - ####.###. (optional)
    price2_regupto = 3.4 # float | Format - ####.###. (optional)
    price2_regdn_from = 3.4 # float | Format - ####.###. (optional)
    price2_regdnto = 3.4 # float | Format - ####.###. (optional)
    price2_offline_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price2_offline_nspinto = 3.4 # float | Format - ####.###. (optional)
    quantity_mw2_from = 56 # int | Format - ###. (optional)
    quantity_mw2_to = 56 # int | Format - ###. (optional)
    block_indicator3 = True # bool | Format - true | false. (optional)
    price3_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price3_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price3_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price3_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price3_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price3_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price3_online_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price3_online_nspinto = 3.4 # float | Format - ####.###. (optional)
    price3_regup_from = 3.4 # float | Format - ####.###. (optional)
    price3_regupto = 3.4 # float | Format - ####.###. (optional)
    price3_regdn_from = 3.4 # float | Format - ####.###. (optional)
    price3_regdnto = 3.4 # float | Format - ####.###. (optional)
    price3_offline_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price3_offline_nspinto = 3.4 # float | Format - ####.###. (optional)
    quantity_mw3_from = 56 # int | Format - ###. (optional)
    quantity_mw3_to = 56 # int | Format - ###. (optional)
    block_indicator4 = True # bool | Format - true | false. (optional)
    price4_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price4_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price4_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price4_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price4_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price4_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price4_online_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price4_online_nspinto = 3.4 # float | Format - ####.###. (optional)
    price4_regup_from = 3.4 # float | Format - ####.###. (optional)
    price4_regupto = 3.4 # float | Format - ####.###. (optional)
    price4_regdn_from = 3.4 # float | Format - ####.###. (optional)
    price4_regdnto = 3.4 # float | Format - ####.###. (optional)
    price4_offline_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price4_offline_nspinto = 3.4 # float | Format - ####.###. (optional)
    quantity_mw4_from = 56 # int | Format - ###. (optional)
    quantity_mw4_to = 56 # int | Format - ###. (optional)
    block_indicator5 = True # bool | Format - true | false. (optional)
    price5_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price5_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price5_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price5_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price5_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price5_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price5_online_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price5_online_nspinto = 3.4 # float | Format - ####.###. (optional)
    price5_regup_from = 3.4 # float | Format - ####.###. (optional)
    price5_regupto = 3.4 # float | Format - ####.###. (optional)
    price5_regdn_from = 3.4 # float | Format - ####.###. (optional)
    price5_regdnto = 3.4 # float | Format - ####.###. (optional)
    price5_offline_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price5_offline_nspinto = 3.4 # float | Format - ####.###. (optional)
    quantity_mw5_from = 56 # int | Format - ###. (optional)
    quantity_mw5_to = 56 # int | Format - ###. (optional)
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 'hour_ending_from_example' # str | Format - mm:ss. (optional)
    hour_ending_to = 'hour_ending_to_example' # str | Format - mm:ss. (optional)
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    dme_name = 'dme_name_example' # str | Format - abc123. (optional)
    resource_name = 'resource_name_example' # str | Format - abc123. (optional)
    multi_hour_block = True # bool | Format - true | false. (optional)
    block_indicator1 = True # bool | Format - true | false. (optional)
    price1_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price1_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price1_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price1_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price1_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price1_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price1_online_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price1_online_nspinto = 3.4 # float | Format - ####.###. (optional)
    price1_regup_from = 3.4 # float | Format - ####.###. (optional)
    price1_regupto = 3.4 # float | Format - ####.###. (optional)
    price1_regdn_from = 3.4 # float | Format - ####.###. (optional)
    price1_regdnto = 3.4 # float | Format - ####.###. (optional)
    price1_offline_nspin_from = 3.4 # float | Format - ####.###. (optional)
    price1_offline_nspinto = 3.4 # float | Format - ####.###. (optional)
    quantity_mw1_from = 56 # int | Format - ###. (optional)
    quantity_mw1_to = 56 # int | Format - ###. (optional)
    block_indicator2 = True # bool | Format - true | false. (optional)
    price2_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price2_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day DAM Generation Resources AS Offers
        api_response = api_instance.get_data46(ocp_apim_subscription_key, price2_rrsffr_from=price2_rrsffr_from, price2_rrsffrto=price2_rrsffrto, price2_rrsufr_from=price2_rrsufr_from, price2_rrsufrto=price2_rrsufrto, price2_online_nspin_from=price2_online_nspin_from, price2_online_nspinto=price2_online_nspinto, price2_regup_from=price2_regup_from, price2_regupto=price2_regupto, price2_regdn_from=price2_regdn_from, price2_regdnto=price2_regdnto, price2_offline_nspin_from=price2_offline_nspin_from, price2_offline_nspinto=price2_offline_nspinto, quantity_mw2_from=quantity_mw2_from, quantity_mw2_to=quantity_mw2_to, block_indicator3=block_indicator3, price3_rrspfr_from=price3_rrspfr_from, price3_rrspfrto=price3_rrspfrto, price3_rrsffr_from=price3_rrsffr_from, price3_rrsffrto=price3_rrsffrto, price3_rrsufr_from=price3_rrsufr_from, price3_rrsufrto=price3_rrsufrto, price3_online_nspin_from=price3_online_nspin_from, price3_online_nspinto=price3_online_nspinto, price3_regup_from=price3_regup_from, price3_regupto=price3_regupto, price3_regdn_from=price3_regdn_from, price3_regdnto=price3_regdnto, price3_offline_nspin_from=price3_offline_nspin_from, price3_offline_nspinto=price3_offline_nspinto, quantity_mw3_from=quantity_mw3_from, quantity_mw3_to=quantity_mw3_to, block_indicator4=block_indicator4, price4_rrspfr_from=price4_rrspfr_from, price4_rrspfrto=price4_rrspfrto, price4_rrsffr_from=price4_rrsffr_from, price4_rrsffrto=price4_rrsffrto, price4_rrsufr_from=price4_rrsufr_from, price4_rrsufrto=price4_rrsufrto, price4_online_nspin_from=price4_online_nspin_from, price4_online_nspinto=price4_online_nspinto, price4_regup_from=price4_regup_from, price4_regupto=price4_regupto, price4_regdn_from=price4_regdn_from, price4_regdnto=price4_regdnto, price4_offline_nspin_from=price4_offline_nspin_from, price4_offline_nspinto=price4_offline_nspinto, quantity_mw4_from=quantity_mw4_from, quantity_mw4_to=quantity_mw4_to, block_indicator5=block_indicator5, price5_rrspfr_from=price5_rrspfr_from, price5_rrspfrto=price5_rrspfrto, price5_rrsffr_from=price5_rrsffr_from, price5_rrsffrto=price5_rrsffrto, price5_rrsufr_from=price5_rrsufr_from, price5_rrsufrto=price5_rrsufrto, price5_online_nspin_from=price5_online_nspin_from, price5_online_nspinto=price5_online_nspinto, price5_regup_from=price5_regup_from, price5_regupto=price5_regupto, price5_regdn_from=price5_regdn_from, price5_regdnto=price5_regdnto, price5_offline_nspin_from=price5_offline_nspin_from, price5_offline_nspinto=price5_offline_nspinto, quantity_mw5_from=quantity_mw5_from, quantity_mw5_to=quantity_mw5_to, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, dme_name=dme_name, resource_name=resource_name, multi_hour_block=multi_hour_block, block_indicator1=block_indicator1, price1_rrspfr_from=price1_rrspfr_from, price1_rrspfrto=price1_rrspfrto, price1_rrsffr_from=price1_rrsffr_from, price1_rrsffrto=price1_rrsffrto, price1_rrsufr_from=price1_rrsufr_from, price1_rrsufrto=price1_rrsufrto, price1_online_nspin_from=price1_online_nspin_from, price1_online_nspinto=price1_online_nspinto, price1_regup_from=price1_regup_from, price1_regupto=price1_regupto, price1_regdn_from=price1_regdn_from, price1_regdnto=price1_regdnto, price1_offline_nspin_from=price1_offline_nspin_from, price1_offline_nspinto=price1_offline_nspinto, quantity_mw1_from=quantity_mw1_from, quantity_mw1_to=quantity_mw1_to, block_indicator2=block_indicator2, price2_rrspfr_from=price2_rrspfr_from, price2_rrspfrto=price2_rrspfrto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3966ERApi->get_data46:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3966ERApi->get_data46: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **price2_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price2_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price2_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price2_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price2_online_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price2_online_nspinto** | **float**| Format - ####.###. | [optional] 
 **price2_regup_from** | **float**| Format - ####.###. | [optional] 
 **price2_regupto** | **float**| Format - ####.###. | [optional] 
 **price2_regdn_from** | **float**| Format - ####.###. | [optional] 
 **price2_regdnto** | **float**| Format - ####.###. | [optional] 
 **price2_offline_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price2_offline_nspinto** | **float**| Format - ####.###. | [optional] 
 **quantity_mw2_from** | **int**| Format - ###. | [optional] 
 **quantity_mw2_to** | **int**| Format - ###. | [optional] 
 **block_indicator3** | **bool**| Format - true | false. | [optional] 
 **price3_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price3_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price3_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price3_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price3_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price3_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price3_online_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price3_online_nspinto** | **float**| Format - ####.###. | [optional] 
 **price3_regup_from** | **float**| Format - ####.###. | [optional] 
 **price3_regupto** | **float**| Format - ####.###. | [optional] 
 **price3_regdn_from** | **float**| Format - ####.###. | [optional] 
 **price3_regdnto** | **float**| Format - ####.###. | [optional] 
 **price3_offline_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price3_offline_nspinto** | **float**| Format - ####.###. | [optional] 
 **quantity_mw3_from** | **int**| Format - ###. | [optional] 
 **quantity_mw3_to** | **int**| Format - ###. | [optional] 
 **block_indicator4** | **bool**| Format - true | false. | [optional] 
 **price4_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price4_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price4_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price4_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price4_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price4_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price4_online_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price4_online_nspinto** | **float**| Format - ####.###. | [optional] 
 **price4_regup_from** | **float**| Format - ####.###. | [optional] 
 **price4_regupto** | **float**| Format - ####.###. | [optional] 
 **price4_regdn_from** | **float**| Format - ####.###. | [optional] 
 **price4_regdnto** | **float**| Format - ####.###. | [optional] 
 **price4_offline_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price4_offline_nspinto** | **float**| Format - ####.###. | [optional] 
 **quantity_mw4_from** | **int**| Format - ###. | [optional] 
 **quantity_mw4_to** | **int**| Format - ###. | [optional] 
 **block_indicator5** | **bool**| Format - true | false. | [optional] 
 **price5_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price5_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price5_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price5_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price5_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price5_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price5_online_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price5_online_nspinto** | **float**| Format - ####.###. | [optional] 
 **price5_regup_from** | **float**| Format - ####.###. | [optional] 
 **price5_regupto** | **float**| Format - ####.###. | [optional] 
 **price5_regdn_from** | **float**| Format - ####.###. | [optional] 
 **price5_regdnto** | **float**| Format - ####.###. | [optional] 
 **price5_offline_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price5_offline_nspinto** | **float**| Format - ####.###. | [optional] 
 **quantity_mw5_from** | **int**| Format - ###. | [optional] 
 **quantity_mw5_to** | **int**| Format - ###. | [optional] 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **str**| Format - mm:ss. | [optional] 
 **hour_ending_to** | **str**| Format - mm:ss. | [optional] 
 **qse_name** | **str**| Format - abc123. | [optional] 
 **dme_name** | **str**| Format - abc123. | [optional] 
 **resource_name** | **str**| Format - abc123. | [optional] 
 **multi_hour_block** | **bool**| Format - true | false. | [optional] 
 **block_indicator1** | **bool**| Format - true | false. | [optional] 
 **price1_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price1_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price1_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price1_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price1_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price1_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price1_online_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price1_online_nspinto** | **float**| Format - ####.###. | [optional] 
 **price1_regup_from** | **float**| Format - ####.###. | [optional] 
 **price1_regupto** | **float**| Format - ####.###. | [optional] 
 **price1_regdn_from** | **float**| Format - ####.###. | [optional] 
 **price1_regdnto** | **float**| Format - ####.###. | [optional] 
 **price1_offline_nspin_from** | **float**| Format - ####.###. | [optional] 
 **price1_offline_nspinto** | **float**| Format - ####.###. | [optional] 
 **quantity_mw1_from** | **int**| Format - ###. | [optional] 
 **quantity_mw1_to** | **int**| Format - ###. | [optional] 
 **block_indicator2** | **bool**| Format - true | false. | [optional] 
 **price2_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price2_rrspfrto** | **float**| Format - ####.###. | [optional] 
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

# **get_data47**
> Report get_data47(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, settlement_point_name=settlement_point_name, qse_name=qse_name, energy_only_offer_mw1_from=energy_only_offer_mw1_from, energy_only_offer_mw1_to=energy_only_offer_mw1_to, energy_only_offer_price1_from=energy_only_offer_price1_from, energy_only_offer_price1_to=energy_only_offer_price1_to, energy_only_offer_mw2_from=energy_only_offer_mw2_from, energy_only_offer_mw2_to=energy_only_offer_mw2_to, energy_only_offer_price2_from=energy_only_offer_price2_from, energy_only_offer_price2_to=energy_only_offer_price2_to, energy_only_offer_mw3_from=energy_only_offer_mw3_from, energy_only_offer_mw3_to=energy_only_offer_mw3_to, energy_only_offer_price3_from=energy_only_offer_price3_from, energy_only_offer_price3_to=energy_only_offer_price3_to, energy_only_offer_mw4_from=energy_only_offer_mw4_from, energy_only_offer_mw4_to=energy_only_offer_mw4_to, energy_only_offer_price4_from=energy_only_offer_price4_from, energy_only_offer_price4_to=energy_only_offer_price4_to, energy_only_offer_mw5_from=energy_only_offer_mw5_from, energy_only_offer_mw5_to=energy_only_offer_mw5_to, energy_only_offer_price5_from=energy_only_offer_price5_from, energy_only_offer_price5_to=energy_only_offer_price5_to, energy_only_offer_mw6_from=energy_only_offer_mw6_from, energy_only_offer_mw6_to=energy_only_offer_mw6_to, energy_only_offer_price6_from=energy_only_offer_price6_from, energy_only_offer_price6_to=energy_only_offer_price6_to, energy_only_offer_mw7_from=energy_only_offer_mw7_from, energy_only_offer_mw7_to=energy_only_offer_mw7_to, energy_only_offer_price7_from=energy_only_offer_price7_from, energy_only_offer_price7_to=energy_only_offer_price7_to, energy_only_offer_mw8_from=energy_only_offer_mw8_from, energy_only_offer_mw8_to=energy_only_offer_mw8_to, energy_only_offer_price8_from=energy_only_offer_price8_from, energy_only_offer_price8_to=energy_only_offer_price8_to, energy_only_offer_mw9_from=energy_only_offer_mw9_from, energy_only_offer_mw9_to=energy_only_offer_mw9_to, energy_only_offer_price9_from=energy_only_offer_price9_from, energy_only_offer_price9_to=energy_only_offer_price9_to, energy_only_offer_mw10_from=energy_only_offer_mw10_from, energy_only_offer_mw10_to=energy_only_offer_mw10_to, energy_only_offer_price10_from=energy_only_offer_price10_from, energy_only_offer_price10_to=energy_only_offer_price10_to, offer_id_from=offer_id_from, offer_id_to=offer_id_to, multi_hour_block=multi_hour_block, block_curve=block_curve, page=page, size=size, sort=sort, dir=dir)

60 Day DAM Energy Only Offers

60 Day DAM Energy Only Offers

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
    api_instance = openapi_client.NP3966ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 'hour_ending_from_example' # str | Format - mm:ss. (optional)
    hour_ending_to = 'hour_ending_to_example' # str | Format - mm:ss. (optional)
    settlement_point_name = 'settlement_point_name_example' # str | Format - abc123. (optional)
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    energy_only_offer_mw1_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw1_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price1_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price1_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw2_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw2_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price2_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price2_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw3_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw3_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price3_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price3_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw4_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw4_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price4_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price4_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw5_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw5_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price5_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price5_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw6_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw6_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price6_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price6_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw7_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw7_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price7_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price7_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw8_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw8_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price8_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price8_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw9_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw9_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price9_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price9_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw10_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_mw10_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price10_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_price10_to = 3.4 # float | Format - ####.###. (optional)
    offer_id_from = 3.4 # float | Format - ####.###. (optional)
    offer_id_to = 3.4 # float | Format - ####.###. (optional)
    multi_hour_block = True # bool | Format - true | false. (optional)
    block_curve = True # bool | Format - true | false. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day DAM Energy Only Offers
        api_response = api_instance.get_data47(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, settlement_point_name=settlement_point_name, qse_name=qse_name, energy_only_offer_mw1_from=energy_only_offer_mw1_from, energy_only_offer_mw1_to=energy_only_offer_mw1_to, energy_only_offer_price1_from=energy_only_offer_price1_from, energy_only_offer_price1_to=energy_only_offer_price1_to, energy_only_offer_mw2_from=energy_only_offer_mw2_from, energy_only_offer_mw2_to=energy_only_offer_mw2_to, energy_only_offer_price2_from=energy_only_offer_price2_from, energy_only_offer_price2_to=energy_only_offer_price2_to, energy_only_offer_mw3_from=energy_only_offer_mw3_from, energy_only_offer_mw3_to=energy_only_offer_mw3_to, energy_only_offer_price3_from=energy_only_offer_price3_from, energy_only_offer_price3_to=energy_only_offer_price3_to, energy_only_offer_mw4_from=energy_only_offer_mw4_from, energy_only_offer_mw4_to=energy_only_offer_mw4_to, energy_only_offer_price4_from=energy_only_offer_price4_from, energy_only_offer_price4_to=energy_only_offer_price4_to, energy_only_offer_mw5_from=energy_only_offer_mw5_from, energy_only_offer_mw5_to=energy_only_offer_mw5_to, energy_only_offer_price5_from=energy_only_offer_price5_from, energy_only_offer_price5_to=energy_only_offer_price5_to, energy_only_offer_mw6_from=energy_only_offer_mw6_from, energy_only_offer_mw6_to=energy_only_offer_mw6_to, energy_only_offer_price6_from=energy_only_offer_price6_from, energy_only_offer_price6_to=energy_only_offer_price6_to, energy_only_offer_mw7_from=energy_only_offer_mw7_from, energy_only_offer_mw7_to=energy_only_offer_mw7_to, energy_only_offer_price7_from=energy_only_offer_price7_from, energy_only_offer_price7_to=energy_only_offer_price7_to, energy_only_offer_mw8_from=energy_only_offer_mw8_from, energy_only_offer_mw8_to=energy_only_offer_mw8_to, energy_only_offer_price8_from=energy_only_offer_price8_from, energy_only_offer_price8_to=energy_only_offer_price8_to, energy_only_offer_mw9_from=energy_only_offer_mw9_from, energy_only_offer_mw9_to=energy_only_offer_mw9_to, energy_only_offer_price9_from=energy_only_offer_price9_from, energy_only_offer_price9_to=energy_only_offer_price9_to, energy_only_offer_mw10_from=energy_only_offer_mw10_from, energy_only_offer_mw10_to=energy_only_offer_mw10_to, energy_only_offer_price10_from=energy_only_offer_price10_from, energy_only_offer_price10_to=energy_only_offer_price10_to, offer_id_from=offer_id_from, offer_id_to=offer_id_to, multi_hour_block=multi_hour_block, block_curve=block_curve, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3966ERApi->get_data47:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3966ERApi->get_data47: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **str**| Format - mm:ss. | [optional] 
 **hour_ending_to** | **str**| Format - mm:ss. | [optional] 
 **settlement_point_name** | **str**| Format - abc123. | [optional] 
 **qse_name** | **str**| Format - abc123. | [optional] 
 **energy_only_offer_mw1_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw1_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price1_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price1_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw2_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw2_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price2_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price2_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw3_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw3_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price3_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price3_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw4_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw4_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price4_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price4_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw5_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw5_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price5_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price5_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw6_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw6_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price6_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price6_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw7_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw7_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price7_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price7_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw8_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw8_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price8_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price8_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw9_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw9_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price9_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price9_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw10_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_mw10_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price10_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_price10_to** | **float**| Format - ####.###. | [optional] 
 **offer_id_from** | **float**| Format - ####.###. | [optional] 
 **offer_id_to** | **float**| Format - ####.###. | [optional] 
 **multi_hour_block** | **bool**| Format - true | false. | [optional] 
 **block_curve** | **bool**| Format - true | false. | [optional] 
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

# **get_data48**
> Report get_data48(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, settlement_point_name=settlement_point_name, qse_name=qse_name, energy_only_offer_award_in_mw_from=energy_only_offer_award_in_mw_from, energy_only_offer_award_in_mwto=energy_only_offer_award_in_mwto, settlement_point_price_from=settlement_point_price_from, settlement_point_price_to=settlement_point_price_to, offer_id=offer_id, page=page, size=size, sort=sort, dir=dir)

60 Day DAM Energy Offer Only Awards

60 Day DAM Energy Offer Only Awards

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
    api_instance = openapi_client.NP3966ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 'hour_ending_from_example' # str | Format - mm:ss. (optional)
    hour_ending_to = 'hour_ending_to_example' # str | Format - mm:ss. (optional)
    settlement_point_name = 'settlement_point_name_example' # str | Format - abc123. (optional)
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    energy_only_offer_award_in_mw_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_offer_award_in_mwto = 3.4 # float | Format - ####.###. (optional)
    settlement_point_price_from = 3.4 # float | Format - ####.###. (optional)
    settlement_point_price_to = 3.4 # float | Format - ####.###. (optional)
    offer_id = 'offer_id_example' # str | Format - abc123. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day DAM Energy Offer Only Awards
        api_response = api_instance.get_data48(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, settlement_point_name=settlement_point_name, qse_name=qse_name, energy_only_offer_award_in_mw_from=energy_only_offer_award_in_mw_from, energy_only_offer_award_in_mwto=energy_only_offer_award_in_mwto, settlement_point_price_from=settlement_point_price_from, settlement_point_price_to=settlement_point_price_to, offer_id=offer_id, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3966ERApi->get_data48:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3966ERApi->get_data48: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **str**| Format - mm:ss. | [optional] 
 **hour_ending_to** | **str**| Format - mm:ss. | [optional] 
 **settlement_point_name** | **str**| Format - abc123. | [optional] 
 **qse_name** | **str**| Format - abc123. | [optional] 
 **energy_only_offer_award_in_mw_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_offer_award_in_mwto** | **float**| Format - ####.###. | [optional] 
 **settlement_point_price_from** | **float**| Format - ####.###. | [optional] 
 **settlement_point_price_to** | **float**| Format - ####.###. | [optional] 
 **offer_id** | **str**| Format - abc123. | [optional] 
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

# **get_data49**
> Report get_data49(ocp_apim_subscription_key, energy_only_bid_mw1_from=energy_only_bid_mw1_from, energy_only_bid_mw1_to=energy_only_bid_mw1_to, energy_only_bid_price1_from=energy_only_bid_price1_from, energy_only_bid_price1_to=energy_only_bid_price1_to, energy_only_bid_mw2_from=energy_only_bid_mw2_from, energy_only_bid_mw2_to=energy_only_bid_mw2_to, energy_only_bid_price2_from=energy_only_bid_price2_from, energy_only_bid_price2_to=energy_only_bid_price2_to, energy_only_bid_mw3_from=energy_only_bid_mw3_from, energy_only_bid_mw3_to=energy_only_bid_mw3_to, energy_only_bid_price3_from=energy_only_bid_price3_from, energy_only_bid_price3_to=energy_only_bid_price3_to, energy_only_bid_mw4_from=energy_only_bid_mw4_from, energy_only_bid_mw4_to=energy_only_bid_mw4_to, energy_only_bid_price4_from=energy_only_bid_price4_from, energy_only_bid_price4_to=energy_only_bid_price4_to, energy_only_bid_mw5_from=energy_only_bid_mw5_from, energy_only_bid_mw5_to=energy_only_bid_mw5_to, energy_only_bid_price5_from=energy_only_bid_price5_from, energy_only_bid_price5_to=energy_only_bid_price5_to, energy_only_bid_mw6_from=energy_only_bid_mw6_from, energy_only_bid_mw6_to=energy_only_bid_mw6_to, energy_only_bid_price6_from=energy_only_bid_price6_from, energy_only_bid_price6_to=energy_only_bid_price6_to, energy_only_bid_mw7_from=energy_only_bid_mw7_from, energy_only_bid_mw7_to=energy_only_bid_mw7_to, energy_only_bid_price7_from=energy_only_bid_price7_from, energy_only_bid_price7_to=energy_only_bid_price7_to, energy_only_bid_mw8_from=energy_only_bid_mw8_from, energy_only_bid_mw8_to=energy_only_bid_mw8_to, energy_only_bid_price8_from=energy_only_bid_price8_from, energy_only_bid_price8_to=energy_only_bid_price8_to, energy_only_bid_mw9_from=energy_only_bid_mw9_from, energy_only_bid_mw9_to=energy_only_bid_mw9_to, energy_only_bid_price9_from=energy_only_bid_price9_from, energy_only_bid_price9_to=energy_only_bid_price9_to, energy_only_bid_mw10_from=energy_only_bid_mw10_from, energy_only_bid_mw10_to=energy_only_bid_mw10_to, energy_only_bid_price10_from=energy_only_bid_price10_from, energy_only_bid_price10_to=energy_only_bid_price10_to, bid_id_from=bid_id_from, bid_id_to=bid_id_to, multi_hour_block=multi_hour_block, block_curve=block_curve, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, settlement_point_name=settlement_point_name, qse_name=qse_name, page=page, size=size, sort=sort, dir=dir)

60 Day DAM Energy Bids

60 Day DAM Energy Bids

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
    api_instance = openapi_client.NP3966ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    energy_only_bid_mw1_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw1_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price1_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price1_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw2_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw2_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price2_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price2_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw3_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw3_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price3_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price3_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw4_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw4_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price4_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price4_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw5_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw5_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price5_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price5_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw6_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw6_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price6_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price6_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw7_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw7_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price7_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price7_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw8_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw8_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price8_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price8_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw9_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw9_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price9_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price9_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw10_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_mw10_to = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price10_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_price10_to = 3.4 # float | Format - ####.###. (optional)
    bid_id_from = 3.4 # float | Format - ####.###. (optional)
    bid_id_to = 3.4 # float | Format - ####.###. (optional)
    multi_hour_block = True # bool | Format - true | false. (optional)
    block_curve = True # bool | Format - true | false. (optional)
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 'hour_ending_from_example' # str | Format - mm:ss. (optional)
    hour_ending_to = 'hour_ending_to_example' # str | Format - mm:ss. (optional)
    settlement_point_name = 'settlement_point_name_example' # str | Format - abc123. (optional)
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day DAM Energy Bids
        api_response = api_instance.get_data49(ocp_apim_subscription_key, energy_only_bid_mw1_from=energy_only_bid_mw1_from, energy_only_bid_mw1_to=energy_only_bid_mw1_to, energy_only_bid_price1_from=energy_only_bid_price1_from, energy_only_bid_price1_to=energy_only_bid_price1_to, energy_only_bid_mw2_from=energy_only_bid_mw2_from, energy_only_bid_mw2_to=energy_only_bid_mw2_to, energy_only_bid_price2_from=energy_only_bid_price2_from, energy_only_bid_price2_to=energy_only_bid_price2_to, energy_only_bid_mw3_from=energy_only_bid_mw3_from, energy_only_bid_mw3_to=energy_only_bid_mw3_to, energy_only_bid_price3_from=energy_only_bid_price3_from, energy_only_bid_price3_to=energy_only_bid_price3_to, energy_only_bid_mw4_from=energy_only_bid_mw4_from, energy_only_bid_mw4_to=energy_only_bid_mw4_to, energy_only_bid_price4_from=energy_only_bid_price4_from, energy_only_bid_price4_to=energy_only_bid_price4_to, energy_only_bid_mw5_from=energy_only_bid_mw5_from, energy_only_bid_mw5_to=energy_only_bid_mw5_to, energy_only_bid_price5_from=energy_only_bid_price5_from, energy_only_bid_price5_to=energy_only_bid_price5_to, energy_only_bid_mw6_from=energy_only_bid_mw6_from, energy_only_bid_mw6_to=energy_only_bid_mw6_to, energy_only_bid_price6_from=energy_only_bid_price6_from, energy_only_bid_price6_to=energy_only_bid_price6_to, energy_only_bid_mw7_from=energy_only_bid_mw7_from, energy_only_bid_mw7_to=energy_only_bid_mw7_to, energy_only_bid_price7_from=energy_only_bid_price7_from, energy_only_bid_price7_to=energy_only_bid_price7_to, energy_only_bid_mw8_from=energy_only_bid_mw8_from, energy_only_bid_mw8_to=energy_only_bid_mw8_to, energy_only_bid_price8_from=energy_only_bid_price8_from, energy_only_bid_price8_to=energy_only_bid_price8_to, energy_only_bid_mw9_from=energy_only_bid_mw9_from, energy_only_bid_mw9_to=energy_only_bid_mw9_to, energy_only_bid_price9_from=energy_only_bid_price9_from, energy_only_bid_price9_to=energy_only_bid_price9_to, energy_only_bid_mw10_from=energy_only_bid_mw10_from, energy_only_bid_mw10_to=energy_only_bid_mw10_to, energy_only_bid_price10_from=energy_only_bid_price10_from, energy_only_bid_price10_to=energy_only_bid_price10_to, bid_id_from=bid_id_from, bid_id_to=bid_id_to, multi_hour_block=multi_hour_block, block_curve=block_curve, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, settlement_point_name=settlement_point_name, qse_name=qse_name, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3966ERApi->get_data49:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3966ERApi->get_data49: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **energy_only_bid_mw1_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw1_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price1_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price1_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw2_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw2_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price2_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price2_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw3_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw3_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price3_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price3_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw4_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw4_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price4_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price4_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw5_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw5_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price5_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price5_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw6_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw6_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price6_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price6_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw7_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw7_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price7_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price7_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw8_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw8_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price8_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price8_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw9_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw9_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price9_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price9_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw10_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_mw10_to** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price10_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_price10_to** | **float**| Format - ####.###. | [optional] 
 **bid_id_from** | **float**| Format - ####.###. | [optional] 
 **bid_id_to** | **float**| Format - ####.###. | [optional] 
 **multi_hour_block** | **bool**| Format - true | false. | [optional] 
 **block_curve** | **bool**| Format - true | false. | [optional] 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **str**| Format - mm:ss. | [optional] 
 **hour_ending_to** | **str**| Format - mm:ss. | [optional] 
 **settlement_point_name** | **str**| Format - abc123. | [optional] 
 **qse_name** | **str**| Format - abc123. | [optional] 
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

# **get_data50**
> Report get_data50(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, settlement_point_name=settlement_point_name, qse_name=qse_name, energy_only_bid_award_in_mw_from=energy_only_bid_award_in_mw_from, energy_only_bid_award_in_mwto=energy_only_bid_award_in_mwto, settlement_point_price_from=settlement_point_price_from, settlement_point_price_to=settlement_point_price_to, bid_id=bid_id, page=page, size=size, sort=sort, dir=dir)

60 Day DAM Energy Bid Awards

60 Day DAM Energy Bid Awards

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
    api_instance = openapi_client.NP3966ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 'hour_ending_from_example' # str | Format - mm:ss. (optional)
    hour_ending_to = 'hour_ending_to_example' # str | Format - mm:ss. (optional)
    settlement_point_name = 'settlement_point_name_example' # str | Format - abc123. (optional)
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    energy_only_bid_award_in_mw_from = 3.4 # float | Format - ####.###. (optional)
    energy_only_bid_award_in_mwto = 3.4 # float | Format - ####.###. (optional)
    settlement_point_price_from = 3.4 # float | Format - ####.###. (optional)
    settlement_point_price_to = 3.4 # float | Format - ####.###. (optional)
    bid_id = 'bid_id_example' # str | Format - abc123. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day DAM Energy Bid Awards
        api_response = api_instance.get_data50(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, settlement_point_name=settlement_point_name, qse_name=qse_name, energy_only_bid_award_in_mw_from=energy_only_bid_award_in_mw_from, energy_only_bid_award_in_mwto=energy_only_bid_award_in_mwto, settlement_point_price_from=settlement_point_price_from, settlement_point_price_to=settlement_point_price_to, bid_id=bid_id, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3966ERApi->get_data50:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3966ERApi->get_data50: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **str**| Format - mm:ss. | [optional] 
 **hour_ending_to** | **str**| Format - mm:ss. | [optional] 
 **settlement_point_name** | **str**| Format - abc123. | [optional] 
 **qse_name** | **str**| Format - abc123. | [optional] 
 **energy_only_bid_award_in_mw_from** | **float**| Format - ####.###. | [optional] 
 **energy_only_bid_award_in_mwto** | **float**| Format - ####.###. | [optional] 
 **settlement_point_price_from** | **float**| Format - ####.###. | [optional] 
 **settlement_point_price_to** | **float**| Format - ####.###. | [optional] 
 **bid_id** | **str**| Format - abc123. | [optional] 
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

