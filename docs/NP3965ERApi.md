# openapi_client.NP3965ERApi

All URIs are relative to *https://api.ercot.com/api/public-reports*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data51**](NP3965ERApi.md#get_data51) | **GET** /np3-965-er/60_sced_smne_gen_res | 60 Day SCED Settlement Metered Net Energy for Generation Resources
[**get_data52**](NP3965ERApi.md#get_data52) | **GET** /np3-965-er/60_sced_qse_self_arranged_as | 60 Day QSE-specific Self-Arranged AS in SCED
[**get_data53**](NP3965ERApi.md#get_data53) | **GET** /np3-965-er/60_sced_gen_res_data | 60 Day SCED Gen Resource Data
[**get_data54**](NP3965ERApi.md#get_data54) | **GET** /np3-965-er/60_sced_dsr_load_data | 60 Day SCED DSR Load Data
[**get_data55**](NP3965ERApi.md#get_data55) | **GET** /np3-965-er/60_load_res_data_in_sced | 60 Day Load Resource Data in SCED
[**get_data56**](NP3965ERApi.md#get_data56) | **GET** /np3-965-er/60_hdl_ldl_man_override | 60 Day HDL and LDL Manual Override Summary


# **get_data51**
> Report get_data51(ocp_apim_subscription_key, interval_value_from=interval_value_from, interval_value_to=interval_value_to, interval_time_from=interval_time_from, interval_time_to=interval_time_to, interval_number_from=interval_number_from, interval_number_to=interval_number_to, resource_code=resource_code, page=page, size=size, sort=sort, dir=dir)

60 Day SCED Settlement Metered Net Energy for Generation Resources

60 Day SCED Settlement Metered Net Energy for Generation Resources

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
    api_instance = openapi_client.NP3965ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    interval_value_from = 3.4 # float | Format - ####.###. (optional)
    interval_value_to = 3.4 # float | Format - ####.###. (optional)
    interval_time_from = 'interval_time_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    interval_time_to = 'interval_time_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    interval_number_from = 56 # int | Format - ###. (optional)
    interval_number_to = 56 # int | Format - ###. (optional)
    resource_code = 'resource_code_example' # str | Format - abc123. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day SCED Settlement Metered Net Energy for Generation Resources
        api_response = api_instance.get_data51(ocp_apim_subscription_key, interval_value_from=interval_value_from, interval_value_to=interval_value_to, interval_time_from=interval_time_from, interval_time_to=interval_time_to, interval_number_from=interval_number_from, interval_number_to=interval_number_to, resource_code=resource_code, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3965ERApi->get_data51:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3965ERApi->get_data51: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **interval_value_from** | **float**| Format - ####.###. | [optional] 
 **interval_value_to** | **float**| Format - ####.###. | [optional] 
 **interval_time_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **interval_time_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **interval_number_from** | **int**| Format - ###. | [optional] 
 **interval_number_to** | **int**| Format - ###. | [optional] 
 **resource_code** | **str**| Format - abc123. | [optional] 
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

# **get_data52**
> Report get_data52(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, qse_name=qse_name, regup=regup, regdn_from=regdn_from, regdnto=regdnto, nspin_from=nspin_from, nspinto=nspinto, nspnm_from=nspnm_from, nspnmto=nspnmto, rrspfr_from=rrspfr_from, rrspfrto=rrspfrto, rrsffr_from=rrsffr_from, rrsffrto=rrsffrto, rrsufr_from=rrsufr_from, rrsufrto=rrsufrto, page=page, size=size, sort=sort, dir=dir)

60 Day QSE-specific Self-Arranged AS in SCED

60 Day QSE-specific Self-Arranged AS in SCED

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
    api_instance = openapi_client.NP3965ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    regup = 'regup_example' # str | Format - abc123. (optional)
    regdn_from = 3.4 # float | Format - ####.###. (optional)
    regdnto = 3.4 # float | Format - ####.###. (optional)
    nspin_from = 3.4 # float | Format - ####.###. (optional)
    nspinto = 3.4 # float | Format - ####.###. (optional)
    nspnm_from = 3.4 # float | Format - ####.###. (optional)
    nspnmto = 3.4 # float | Format - ####.###. (optional)
    rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    rrspfrto = 3.4 # float | Format - ####.###. (optional)
    rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    rrsffrto = 3.4 # float | Format - ####.###. (optional)
    rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    rrsufrto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day QSE-specific Self-Arranged AS in SCED
        api_response = api_instance.get_data52(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, qse_name=qse_name, regup=regup, regdn_from=regdn_from, regdnto=regdnto, nspin_from=nspin_from, nspinto=nspinto, nspnm_from=nspnm_from, nspnmto=nspnmto, rrspfr_from=rrspfr_from, rrspfrto=rrspfrto, rrsffr_from=rrsffr_from, rrsffrto=rrsffrto, rrsufr_from=rrsufr_from, rrsufrto=rrsufrto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3965ERApi->get_data52:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3965ERApi->get_data52: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **qse_name** | **str**| Format - abc123. | [optional] 
 **regup** | **str**| Format - abc123. | [optional] 
 **regdn_from** | **float**| Format - ####.###. | [optional] 
 **regdnto** | **float**| Format - ####.###. | [optional] 
 **nspin_from** | **float**| Format - ####.###. | [optional] 
 **nspinto** | **float**| Format - ####.###. | [optional] 
 **nspnm_from** | **float**| Format - ####.###. | [optional] 
 **nspnmto** | **float**| Format - ####.###. | [optional] 
 **rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **rrspfrto** | **float**| Format - ####.###. | [optional] 
 **rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **rrsffrto** | **float**| Format - ####.###. | [optional] 
 **rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **rrsufrto** | **float**| Format - ####.###. | [optional] 
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

# **get_data53**
> Report get_data53(ocp_apim_subscription_key, sced2_curve_mw9_from=sced2_curve_mw9_from, sced2_curve_mw9_to=sced2_curve_mw9_to, sced2_curve_price9_from=sced2_curve_price9_from, sced2_curve_price9_to=sced2_curve_price9_to, sced2_curve_mw10_from=sced2_curve_mw10_from, sced2_curve_mw10_to=sced2_curve_mw10_to, sced2_curve_price10_from=sced2_curve_price10_from, sced2_curve_price10_to=sced2_curve_price10_to, sced2_curve_mw11_from=sced2_curve_mw11_from, sced2_curve_mw11_to=sced2_curve_mw11_to, sced2_curve_price11_from=sced2_curve_price11_from, sced2_curve_price11_to=sced2_curve_price11_to, sced2_curve_mw12_from=sced2_curve_mw12_from, sced2_curve_mw12_to=sced2_curve_mw12_to, sced2_curve_price12_from=sced2_curve_price12_from, sced2_curve_price12_to=sced2_curve_price12_to, sced2_curve_mw13_from=sced2_curve_mw13_from, sced2_curve_mw13_to=sced2_curve_mw13_to, sced2_curve_price13_from=sced2_curve_price13_from, sced2_curve_price13_to=sced2_curve_price13_to, sced2_curve_mw14_from=sced2_curve_mw14_from, sced2_curve_mw14_to=sced2_curve_mw14_to, sced2_curve_price14_from=sced2_curve_price14_from, sced2_curve_price14_to=sced2_curve_price14_to, sced2_curve_mw15_from=sced2_curve_mw15_from, sced2_curve_mw15_to=sced2_curve_mw15_to, sced2_curve_price15_from=sced2_curve_price15_from, sced2_curve_price15_to=sced2_curve_price15_to, sced2_curve_mw16_from=sced2_curve_mw16_from, sced2_curve_mw16_to=sced2_curve_mw16_to, sced2_curve_price16_from=sced2_curve_price16_from, sced2_curve_price16_to=sced2_curve_price16_to, sced2_curve_mw17_from=sced2_curve_mw17_from, sced2_curve_mw17_to=sced2_curve_mw17_to, sced2_curve_price17_from=sced2_curve_price17_from, sced2_curve_price17_to=sced2_curve_price17_to, sced2_curve_mw18_from=sced2_curve_mw18_from, sced2_curve_mw18_to=sced2_curve_mw18_to, sced2_curve_price18_from=sced2_curve_price18_from, sced2_curve_price18_to=sced2_curve_price18_to, sced2_curve_mw19_from=sced2_curve_mw19_from, sced2_curve_mw19_to=sced2_curve_mw19_to, sced2_curve_price19_from=sced2_curve_price19_from, sced2_curve_price19_to=sced2_curve_price19_to, sced2_curve_mw20_from=sced2_curve_mw20_from, sced2_curve_mw20_to=sced2_curve_mw20_to, sced2_curve_price20_from=sced2_curve_price20_from, sced2_curve_price20_to=sced2_curve_price20_to, sced2_curve_mw21_from=sced2_curve_mw21_from, sced2_curve_mw21_to=sced2_curve_mw21_to, sced2_curve_price21_from=sced2_curve_price21_from, sced2_curve_price21_to=sced2_curve_price21_to, sced2_curve_mw22_from=sced2_curve_mw22_from, sced2_curve_mw22_to=sced2_curve_mw22_to, sced2_curve_price22_from=sced2_curve_price22_from, sced2_curve_price22_to=sced2_curve_price22_to, sced2_curve_mw23_from=sced2_curve_mw23_from, sced2_curve_mw23_to=sced2_curve_mw23_to, sced2_curve_price23_from=sced2_curve_price23_from, sced2_curve_price23_to=sced2_curve_price23_to, sced2_curve_mw24_from=sced2_curve_mw24_from, sced2_curve_mw24_to=sced2_curve_mw24_to, sced2_curve_price24_from=sced2_curve_price24_from, sced2_curve_price24_to=sced2_curve_price24_to, sced2_curve_mw25_from=sced2_curve_mw25_from, sced2_curve_mw25_to=sced2_curve_mw25_to, sced2_curve_price25_from=sced2_curve_price25_from, sced2_curve_price25_to=sced2_curve_price25_to, sced2_curve_mw26_from=sced2_curve_mw26_from, sced2_curve_mw26_to=sced2_curve_mw26_to, sced2_curve_price26_from=sced2_curve_price26_from, sced2_curve_price26_to=sced2_curve_price26_to, sced2_curve_mw27_from=sced2_curve_mw27_from, sced2_curve_mw27_to=sced2_curve_mw27_to, sced2_curve_price27_from=sced2_curve_price27_from, sced2_curve_price27_to=sced2_curve_price27_to, sced2_curve_mw28_from=sced2_curve_mw28_from, sced2_curve_mw28_to=sced2_curve_mw28_to, sced2_curve_price28_from=sced2_curve_price28_from, sced2_curve_price28_to=sced2_curve_price28_to, sced2_curve_mw29_from=sced2_curve_mw29_from, sced2_curve_mw29_to=sced2_curve_mw29_to, sced2_curve_price29_from=sced2_curve_price29_from, sced2_curve_price29_to=sced2_curve_price29_to, sced2_curve_mw30_from=sced2_curve_mw30_from, sced2_curve_mw30_to=sced2_curve_mw30_to, sced2_curve_price30_from=sced2_curve_price30_from, sced2_curve_price30_to=sced2_curve_price30_to, sced2_curve_mw31_from=sced2_curve_mw31_from, sced2_curve_mw31_to=sced2_curve_mw31_to, sced2_curve_price31_from=sced2_curve_price31_from, sced2_curve_price31_to=sced2_curve_price31_to, sced2_curve_mw32_from=sced2_curve_mw32_from, sced2_curve_mw32_to=sced2_curve_mw32_to, sced2_curve_price32_from=sced2_curve_price32_from, sced2_curve_price32_to=sced2_curve_price32_to, sced2_curve_mw33_from=sced2_curve_mw33_from, sced2_curve_mw33_to=sced2_curve_mw33_to, sced2_curve_price33_from=sced2_curve_price33_from, sced2_curve_price33_to=sced2_curve_price33_to, sced2_curve_mw34_from=sced2_curve_mw34_from, sced2_curve_mw34_to=sced2_curve_mw34_to, sced2_curve_price34_from=sced2_curve_price34_from, sced2_curve_price34_to=sced2_curve_price34_to, sced2_curve_mw35_from=sced2_curve_mw35_from, sced2_curve_mw35_to=sced2_curve_mw35_to, sced2_curve_price35_from=sced2_curve_price35_from, sced2_curve_price35_to=sced2_curve_price35_to, output_schedule_from=output_schedule_from, output_schedule_to=output_schedule_to, hsl_from=hsl_from, hslto=hslto, hasl_from=hasl_from, haslto=haslto, hdl_from=hdl_from, hdlto=hdlto, lsl_from=lsl_from, lslto=lslto, lasl_from=lasl_from, laslto=laslto, ldl_from=ldl_from, ldlto=ldlto, telemetered_resource_status=telemetered_resource_status, base_point_from=base_point_from, base_point_to=base_point_to, telemetered_net_output_from=telemetered_net_output_from, telemetered_net_output_to=telemetered_net_output_to, asregup_from=asregup_from, asregupto=asregupto, asregdn_from=asregdn_from, asregdnto=asregdnto, asrrs_from=asrrs_from, asrrsto=asrrsto, asrrsffr_from=asrrsffr_from, asrrsffrto=asrrsffrto, asnsrs_from=asnsrs_from, asnsrsto=asnsrsto, bid_type=bid_type, start_up_cold_offer_from=start_up_cold_offer_from, start_up_cold_offer_to=start_up_cold_offer_to, start_up_hot_offer_from=start_up_hot_offer_from, start_up_hot_offer_to=start_up_hot_offer_to, start_up_inter_offer_from=start_up_inter_offer_from, start_up_inter_offer_to=start_up_inter_offer_to, min_gen_cost_from=min_gen_cost_from, min_gen_cost_to=min_gen_cost_to, submitted_tpomw1_from=submitted_tpomw1_from, submitted_tpomw1_to=submitted_tpomw1_to, submitted_tpo_price1_from=submitted_tpo_price1_from, submitted_tpo_price1_to=submitted_tpo_price1_to, submitted_tpomw2_from=submitted_tpomw2_from, submitted_tpomw2_to=submitted_tpomw2_to, submitted_tpo_price2_from=submitted_tpo_price2_from, submitted_tpo_price2_to=submitted_tpo_price2_to, submitted_tpomw3_from=submitted_tpomw3_from, submitted_tpomw3_to=submitted_tpomw3_to, submitted_tpo_price3_from=submitted_tpo_price3_from, submitted_tpo_price3_to=submitted_tpo_price3_to, submitted_tpomw4_from=submitted_tpomw4_from, submitted_tpomw4_to=submitted_tpomw4_to, submitted_tpo_price4_from=submitted_tpo_price4_from, submitted_tpo_price4_to=submitted_tpo_price4_to, submitted_tpomw5_from=submitted_tpomw5_from, submitted_tpomw5_to=submitted_tpomw5_to, submitted_tpo_price5_from=submitted_tpo_price5_from, submitted_tpo_price5_to=submitted_tpo_price5_to, submitted_tpomw6_from=submitted_tpomw6_from, submitted_tpomw6_to=submitted_tpomw6_to, submitted_tpo_price6_from=submitted_tpo_price6_from, submitted_tpo_price6_to=submitted_tpo_price6_to, submitted_tpomw7_from=submitted_tpomw7_from, submitted_tpomw7_to=submitted_tpomw7_to, submitted_tpo_price7_from=submitted_tpo_price7_from, submitted_tpo_price7_to=submitted_tpo_price7_to, submitted_tpomw8_from=submitted_tpomw8_from, submitted_tpomw8_to=submitted_tpomw8_to, submitted_tpo_price8_from=submitted_tpo_price8_from, submitted_tpo_price8_to=submitted_tpo_price8_to, submitted_tpomw9_from=submitted_tpomw9_from, submitted_tpomw9_to=submitted_tpomw9_to, submitted_tpo_price9_from=submitted_tpo_price9_from, submitted_tpo_price9_to=submitted_tpo_price9_to, submitted_tpomw10_from=submitted_tpomw10_from, submitted_tpomw10_to=submitted_tpomw10_to, submitted_tpo_price10_from=submitted_tpo_price10_from, submitted_tpo_price10_to=submitted_tpo_price10_to, proxy_extension=proxy_extension, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, qse_name=qse_name, dme_name=dme_name, resource_name=resource_name, resource_type=resource_type, sced1_curve_mw1_from=sced1_curve_mw1_from, sced1_curve_mw1_to=sced1_curve_mw1_to, sced1_curve_price1_from=sced1_curve_price1_from, sced1_curve_price1_to=sced1_curve_price1_to, sced1_curve_mw2_from=sced1_curve_mw2_from, sced1_curve_mw2_to=sced1_curve_mw2_to, sced1_curve_price2_from=sced1_curve_price2_from, sced1_curve_price2_to=sced1_curve_price2_to, sced1_curve_mw3_from=sced1_curve_mw3_from, sced1_curve_mw3_to=sced1_curve_mw3_to, sced1_curve_price3_from=sced1_curve_price3_from, sced1_curve_price3_to=sced1_curve_price3_to, sced1_curve_mw4_from=sced1_curve_mw4_from, sced1_curve_mw4_to=sced1_curve_mw4_to, sced1_curve_price4_from=sced1_curve_price4_from, sced1_curve_price4_to=sced1_curve_price4_to, sced1_curve_mw5_from=sced1_curve_mw5_from, sced1_curve_mw5_to=sced1_curve_mw5_to, sced1_curve_price5_from=sced1_curve_price5_from, sced1_curve_price5_to=sced1_curve_price5_to, sced1_curve_mw6_from=sced1_curve_mw6_from, sced1_curve_mw6_to=sced1_curve_mw6_to, sced1_curve_price6_from=sced1_curve_price6_from, sced1_curve_price6_to=sced1_curve_price6_to, sced1_curve_mw7_from=sced1_curve_mw7_from, sced1_curve_mw7_to=sced1_curve_mw7_to, sced1_curve_price7_from=sced1_curve_price7_from, sced1_curve_price7_to=sced1_curve_price7_to, sced1_curve_mw8_from=sced1_curve_mw8_from, sced1_curve_mw8_to=sced1_curve_mw8_to, sced1_curve_price8_from=sced1_curve_price8_from, sced1_curve_price8_to=sced1_curve_price8_to, sced1_curve_mw9_from=sced1_curve_mw9_from, sced1_curve_mw9_to=sced1_curve_mw9_to, sced1_curve_price9_from=sced1_curve_price9_from, sced1_curve_price9_to=sced1_curve_price9_to, sced1_curve_mw10_from=sced1_curve_mw10_from, sced1_curve_mw10_to=sced1_curve_mw10_to, sced1_curve_price10_from=sced1_curve_price10_from, sced1_curve_price10_to=sced1_curve_price10_to, sced1_curve_mw11_from=sced1_curve_mw11_from, sced1_curve_mw11_to=sced1_curve_mw11_to, sced1_curve_price11_from=sced1_curve_price11_from, sced1_curve_price11_to=sced1_curve_price11_to, sced1_curve_mw12_from=sced1_curve_mw12_from, sced1_curve_mw12_to=sced1_curve_mw12_to, sced1_curve_price12_from=sced1_curve_price12_from, sced1_curve_price12_to=sced1_curve_price12_to, sced1_curve_mw13_from=sced1_curve_mw13_from, sced1_curve_mw13_to=sced1_curve_mw13_to, sced1_curve_price13_from=sced1_curve_price13_from, sced1_curve_price13_to=sced1_curve_price13_to, sced1_curve_mw14_from=sced1_curve_mw14_from, sced1_curve_mw14_to=sced1_curve_mw14_to, asecrs_from=asecrs_from, asecrsto=asecrsto, sced1_curve_price14_from=sced1_curve_price14_from, sced1_curve_price14_to=sced1_curve_price14_to, sced1_curve_mw15_from=sced1_curve_mw15_from, sced1_curve_mw15_to=sced1_curve_mw15_to, sced1_curve_price15_from=sced1_curve_price15_from, sced1_curve_price15_to=sced1_curve_price15_to, sced1_curve_mw16_from=sced1_curve_mw16_from, sced1_curve_mw16_to=sced1_curve_mw16_to, sced1_curve_price16_from=sced1_curve_price16_from, sced1_curve_price16_to=sced1_curve_price16_to, sced1_curve_mw17_from=sced1_curve_mw17_from, sced1_curve_mw17_to=sced1_curve_mw17_to, sced1_curve_price17_from=sced1_curve_price17_from, sced1_curve_price17_to=sced1_curve_price17_to, sced1_curve_mw18_from=sced1_curve_mw18_from, sced1_curve_mw18_to=sced1_curve_mw18_to, sced1_curve_price18_from=sced1_curve_price18_from, sced1_curve_price18_to=sced1_curve_price18_to, sced1_curve_mw19_from=sced1_curve_mw19_from, sced1_curve_mw19_to=sced1_curve_mw19_to, sced1_curve_price19_from=sced1_curve_price19_from, sced1_curve_price19_to=sced1_curve_price19_to, sced1_curve_mw20_from=sced1_curve_mw20_from, sced1_curve_mw20_to=sced1_curve_mw20_to, sced1_curve_price20_from=sced1_curve_price20_from, sced1_curve_price20_to=sced1_curve_price20_to, sced1_curve_mw21_from=sced1_curve_mw21_from, sced1_curve_mw21_to=sced1_curve_mw21_to, sced1_curve_price21_from=sced1_curve_price21_from, sced1_curve_price21_to=sced1_curve_price21_to, sced1_curve_mw22_from=sced1_curve_mw22_from, sced1_curve_mw22_to=sced1_curve_mw22_to, sced1_curve_price22_from=sced1_curve_price22_from, sced1_curve_price22_to=sced1_curve_price22_to, sced1_curve_mw23_from=sced1_curve_mw23_from, sced1_curve_mw23_to=sced1_curve_mw23_to, sced1_curve_price23_from=sced1_curve_price23_from, sced1_curve_price23_to=sced1_curve_price23_to, sced1_curve_mw24_from=sced1_curve_mw24_from, sced1_curve_mw24_to=sced1_curve_mw24_to, sced1_curve_price24_from=sced1_curve_price24_from, sced1_curve_price24_to=sced1_curve_price24_to, sced1_curve_mw25_from=sced1_curve_mw25_from, sced1_curve_mw25_to=sced1_curve_mw25_to, sced1_curve_price25_from=sced1_curve_price25_from, sced1_curve_price25_to=sced1_curve_price25_to, sced1_curve_mw26_from=sced1_curve_mw26_from, sced1_curve_mw26_to=sced1_curve_mw26_to, sced1_curve_price26_from=sced1_curve_price26_from, sced1_curve_price26_to=sced1_curve_price26_to, sced1_curve_mw27_from=sced1_curve_mw27_from, sced1_curve_mw27_to=sced1_curve_mw27_to, sced1_curve_price27_from=sced1_curve_price27_from, sced1_curve_price27_to=sced1_curve_price27_to, sced1_curve_mw28_from=sced1_curve_mw28_from, sced1_curve_mw28_to=sced1_curve_mw28_to, sced1_curve_price28_from=sced1_curve_price28_from, sced1_curve_price28_to=sced1_curve_price28_to, sced1_curve_mw29_from=sced1_curve_mw29_from, sced1_curve_mw29_to=sced1_curve_mw29_to, sced1_curve_price29_from=sced1_curve_price29_from, sced1_curve_price29_to=sced1_curve_price29_to, sced1_curve_mw30_from=sced1_curve_mw30_from, sced1_curve_mw30_to=sced1_curve_mw30_to, sced1_curve_price30_from=sced1_curve_price30_from, sced1_curve_price30_to=sced1_curve_price30_to, sced1_curve_mw31_from=sced1_curve_mw31_from, sced1_curve_mw31_to=sced1_curve_mw31_to, sced1_curve_price31_from=sced1_curve_price31_from, sced1_curve_price31_to=sced1_curve_price31_to, sced1_curve_mw32_from=sced1_curve_mw32_from, sced1_curve_mw32_to=sced1_curve_mw32_to, sced1_curve_price32_from=sced1_curve_price32_from, sced1_curve_price32_to=sced1_curve_price32_to, sced1_curve_mw33_from=sced1_curve_mw33_from, sced1_curve_mw33_to=sced1_curve_mw33_to, sced1_curve_price33_from=sced1_curve_price33_from, sced1_curve_price33_to=sced1_curve_price33_to, sced1_curve_mw34_from=sced1_curve_mw34_from, sced1_curve_mw34_to=sced1_curve_mw34_to, sced1_curve_price34_from=sced1_curve_price34_from, sced1_curve_price34_to=sced1_curve_price34_to, sced1_curve_mw35_from=sced1_curve_mw35_from, sced1_curve_mw35_to=sced1_curve_mw35_to, sced1_curve_price35_from=sced1_curve_price35_from, sced1_curve_price35_to=sced1_curve_price35_to, sced2_curve_mw1_from=sced2_curve_mw1_from, sced2_curve_mw1_to=sced2_curve_mw1_to, sced2_curve_price1_from=sced2_curve_price1_from, sced2_curve_price1_to=sced2_curve_price1_to, sced2_curve_mw2_from=sced2_curve_mw2_from, sced2_curve_mw2_to=sced2_curve_mw2_to, sced2_curve_price2_from=sced2_curve_price2_from, sced2_curve_price2_to=sced2_curve_price2_to, sced2_curve_mw3_from=sced2_curve_mw3_from, sced2_curve_mw3_to=sced2_curve_mw3_to, sced2_curve_price3_from=sced2_curve_price3_from, sced2_curve_price3_to=sced2_curve_price3_to, sced2_curve_mw4_from=sced2_curve_mw4_from, sced2_curve_mw4_to=sced2_curve_mw4_to, sced2_curve_price4_from=sced2_curve_price4_from, sced2_curve_price4_to=sced2_curve_price4_to, sced2_curve_mw5_from=sced2_curve_mw5_from, sced2_curve_mw5_to=sced2_curve_mw5_to, sced2_curve_price5_from=sced2_curve_price5_from, sced2_curve_price5_to=sced2_curve_price5_to, sced2_curve_mw6_from=sced2_curve_mw6_from, sced2_curve_mw6_to=sced2_curve_mw6_to, sced2_curve_price6_from=sced2_curve_price6_from, sced2_curve_price6_to=sced2_curve_price6_to, sced2_curve_mw7_from=sced2_curve_mw7_from, sced2_curve_mw7_to=sced2_curve_mw7_to, sced2_curve_price7_from=sced2_curve_price7_from, sced2_curve_price7_to=sced2_curve_price7_to, sced2_curve_mw8_from=sced2_curve_mw8_from, sced2_curve_mw8_to=sced2_curve_mw8_to, sced2_curve_price8_from=sced2_curve_price8_from, sced2_curve_price8_to=sced2_curve_price8_to, page=page, size=size, sort=sort, dir=dir)

60 Day SCED Gen Resource Data

60 Day SCED Gen Resource Data

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
    api_instance = openapi_client.NP3965ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sced2_curve_mw9_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw9_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price9_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price9_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw10_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw10_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price10_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price10_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw11_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw11_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price11_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price11_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw12_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw12_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price12_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price12_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw13_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw13_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price13_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price13_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw14_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw14_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price14_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price14_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw15_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw15_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price15_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price15_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw16_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw16_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price16_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price16_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw17_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw17_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price17_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price17_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw18_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw18_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price18_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price18_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw19_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw19_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price19_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price19_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw20_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw20_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price20_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price20_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw21_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw21_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price21_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price21_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw22_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw22_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price22_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price22_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw23_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw23_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price23_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price23_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw24_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw24_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price24_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price24_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw25_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw25_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price25_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price25_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw26_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw26_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price26_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price26_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw27_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw27_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price27_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price27_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw28_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw28_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price28_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price28_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw29_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw29_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price29_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price29_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw30_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw30_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price30_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price30_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw31_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw31_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price31_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price31_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw32_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw32_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price32_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price32_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw33_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw33_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price33_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price33_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw34_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw34_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price34_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price34_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw35_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw35_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price35_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price35_to = 3.4 # float | Format - ####.###. (optional)
    output_schedule_from = 3.4 # float | Format - ####.###. (optional)
    output_schedule_to = 3.4 # float | Format - ####.###. (optional)
    hsl_from = 3.4 # float | Format - ####.###. (optional)
    hslto = 3.4 # float | Format - ####.###. (optional)
    hasl_from = 3.4 # float | Format - ####.###. (optional)
    haslto = 3.4 # float | Format - ####.###. (optional)
    hdl_from = 3.4 # float | Format - ####.###. (optional)
    hdlto = 3.4 # float | Format - ####.###. (optional)
    lsl_from = 3.4 # float | Format - ####.###. (optional)
    lslto = 3.4 # float | Format - ####.###. (optional)
    lasl_from = 3.4 # float | Format - ####.###. (optional)
    laslto = 3.4 # float | Format - ####.###. (optional)
    ldl_from = 3.4 # float | Format - ####.###. (optional)
    ldlto = 3.4 # float | Format - ####.###. (optional)
    telemetered_resource_status = 'telemetered_resource_status_example' # str | Format - abc123. (optional)
    base_point_from = 3.4 # float | Format - ####.###. (optional)
    base_point_to = 3.4 # float | Format - ####.###. (optional)
    telemetered_net_output_from = 3.4 # float | Format - ####.###. (optional)
    telemetered_net_output_to = 3.4 # float | Format - ####.###. (optional)
    asregup_from = 3.4 # float | Format - ####.###. (optional)
    asregupto = 3.4 # float | Format - ####.###. (optional)
    asregdn_from = 3.4 # float | Format - ####.###. (optional)
    asregdnto = 3.4 # float | Format - ####.###. (optional)
    asrrs_from = 3.4 # float | Format - ####.###. (optional)
    asrrsto = 3.4 # float | Format - ####.###. (optional)
    asrrsffr_from = 3.4 # float | Format - ####.###. (optional)
    asrrsffrto = 3.4 # float | Format - ####.###. (optional)
    asnsrs_from = 3.4 # float | Format - ####.###. (optional)
    asnsrsto = 3.4 # float | Format - ####.###. (optional)
    bid_type = 'bid_type_example' # str | Format - abc123. (optional)
    start_up_cold_offer_from = 3.4 # float | Format - ####.###. (optional)
    start_up_cold_offer_to = 3.4 # float | Format - ####.###. (optional)
    start_up_hot_offer_from = 3.4 # float | Format - ####.###. (optional)
    start_up_hot_offer_to = 3.4 # float | Format - ####.###. (optional)
    start_up_inter_offer_from = 3.4 # float | Format - ####.###. (optional)
    start_up_inter_offer_to = 3.4 # float | Format - ####.###. (optional)
    min_gen_cost_from = 3.4 # float | Format - ####.###. (optional)
    min_gen_cost_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw1_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw1_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price1_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price1_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw2_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw2_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price2_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price2_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw3_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw3_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price3_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price3_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw4_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw4_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price4_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price4_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw5_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw5_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price5_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price5_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw6_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw6_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price6_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price6_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw7_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw7_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price7_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price7_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw8_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw8_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price8_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price8_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw9_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw9_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price9_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price9_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw10_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpomw10_to = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price10_from = 3.4 # float | Format - ####.###. (optional)
    submitted_tpo_price10_to = 3.4 # float | Format - ####.###. (optional)
    proxy_extension = 'proxy_extension_example' # str | Format - abc123. (optional)
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    dme_name = 'dme_name_example' # str | Format - abc123. (optional)
    resource_name = 'resource_name_example' # str | Format - abc123. (optional)
    resource_type = 'resource_type_example' # str | Format - abc123. (optional)
    sced1_curve_mw1_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw1_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price1_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price1_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw2_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw2_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price2_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price2_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw3_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw3_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price3_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price3_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw4_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw4_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price4_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price4_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw5_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw5_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price5_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price5_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw6_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw6_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price6_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price6_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw7_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw7_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price7_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price7_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw8_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw8_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price8_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price8_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw9_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw9_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price9_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price9_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw10_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw10_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price10_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price10_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw11_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw11_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price11_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price11_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw12_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw12_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price12_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price12_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw13_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw13_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price13_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price13_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw14_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw14_to = 3.4 # float | Format - ####.###. (optional)
    asecrs_from = 3.4 # float | Format - ####.###. (optional)
    asecrsto = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price14_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price14_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw15_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw15_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price15_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price15_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw16_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw16_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price16_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price16_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw17_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw17_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price17_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price17_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw18_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw18_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price18_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price18_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw19_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw19_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price19_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price19_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw20_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw20_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price20_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price20_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw21_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw21_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price21_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price21_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw22_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw22_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price22_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price22_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw23_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw23_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price23_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price23_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw24_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw24_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price24_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price24_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw25_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw25_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price25_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price25_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw26_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw26_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price26_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price26_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw27_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw27_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price27_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price27_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw28_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw28_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price28_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price28_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw29_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw29_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price29_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price29_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw30_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw30_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price30_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price30_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw31_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw31_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price31_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price31_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw32_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw32_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price32_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price32_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw33_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw33_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price33_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price33_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw34_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw34_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price34_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price34_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw35_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_mw35_to = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price35_from = 3.4 # float | Format - ####.###. (optional)
    sced1_curve_price35_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw1_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw1_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price1_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price1_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw2_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw2_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price2_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price2_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw3_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw3_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price3_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price3_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw4_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw4_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price4_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price4_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw5_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw5_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price5_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price5_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw6_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw6_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price6_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price6_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw7_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw7_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price7_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price7_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw8_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_mw8_to = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price8_from = 3.4 # float | Format - ####.###. (optional)
    sced2_curve_price8_to = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day SCED Gen Resource Data
        api_response = api_instance.get_data53(ocp_apim_subscription_key, sced2_curve_mw9_from=sced2_curve_mw9_from, sced2_curve_mw9_to=sced2_curve_mw9_to, sced2_curve_price9_from=sced2_curve_price9_from, sced2_curve_price9_to=sced2_curve_price9_to, sced2_curve_mw10_from=sced2_curve_mw10_from, sced2_curve_mw10_to=sced2_curve_mw10_to, sced2_curve_price10_from=sced2_curve_price10_from, sced2_curve_price10_to=sced2_curve_price10_to, sced2_curve_mw11_from=sced2_curve_mw11_from, sced2_curve_mw11_to=sced2_curve_mw11_to, sced2_curve_price11_from=sced2_curve_price11_from, sced2_curve_price11_to=sced2_curve_price11_to, sced2_curve_mw12_from=sced2_curve_mw12_from, sced2_curve_mw12_to=sced2_curve_mw12_to, sced2_curve_price12_from=sced2_curve_price12_from, sced2_curve_price12_to=sced2_curve_price12_to, sced2_curve_mw13_from=sced2_curve_mw13_from, sced2_curve_mw13_to=sced2_curve_mw13_to, sced2_curve_price13_from=sced2_curve_price13_from, sced2_curve_price13_to=sced2_curve_price13_to, sced2_curve_mw14_from=sced2_curve_mw14_from, sced2_curve_mw14_to=sced2_curve_mw14_to, sced2_curve_price14_from=sced2_curve_price14_from, sced2_curve_price14_to=sced2_curve_price14_to, sced2_curve_mw15_from=sced2_curve_mw15_from, sced2_curve_mw15_to=sced2_curve_mw15_to, sced2_curve_price15_from=sced2_curve_price15_from, sced2_curve_price15_to=sced2_curve_price15_to, sced2_curve_mw16_from=sced2_curve_mw16_from, sced2_curve_mw16_to=sced2_curve_mw16_to, sced2_curve_price16_from=sced2_curve_price16_from, sced2_curve_price16_to=sced2_curve_price16_to, sced2_curve_mw17_from=sced2_curve_mw17_from, sced2_curve_mw17_to=sced2_curve_mw17_to, sced2_curve_price17_from=sced2_curve_price17_from, sced2_curve_price17_to=sced2_curve_price17_to, sced2_curve_mw18_from=sced2_curve_mw18_from, sced2_curve_mw18_to=sced2_curve_mw18_to, sced2_curve_price18_from=sced2_curve_price18_from, sced2_curve_price18_to=sced2_curve_price18_to, sced2_curve_mw19_from=sced2_curve_mw19_from, sced2_curve_mw19_to=sced2_curve_mw19_to, sced2_curve_price19_from=sced2_curve_price19_from, sced2_curve_price19_to=sced2_curve_price19_to, sced2_curve_mw20_from=sced2_curve_mw20_from, sced2_curve_mw20_to=sced2_curve_mw20_to, sced2_curve_price20_from=sced2_curve_price20_from, sced2_curve_price20_to=sced2_curve_price20_to, sced2_curve_mw21_from=sced2_curve_mw21_from, sced2_curve_mw21_to=sced2_curve_mw21_to, sced2_curve_price21_from=sced2_curve_price21_from, sced2_curve_price21_to=sced2_curve_price21_to, sced2_curve_mw22_from=sced2_curve_mw22_from, sced2_curve_mw22_to=sced2_curve_mw22_to, sced2_curve_price22_from=sced2_curve_price22_from, sced2_curve_price22_to=sced2_curve_price22_to, sced2_curve_mw23_from=sced2_curve_mw23_from, sced2_curve_mw23_to=sced2_curve_mw23_to, sced2_curve_price23_from=sced2_curve_price23_from, sced2_curve_price23_to=sced2_curve_price23_to, sced2_curve_mw24_from=sced2_curve_mw24_from, sced2_curve_mw24_to=sced2_curve_mw24_to, sced2_curve_price24_from=sced2_curve_price24_from, sced2_curve_price24_to=sced2_curve_price24_to, sced2_curve_mw25_from=sced2_curve_mw25_from, sced2_curve_mw25_to=sced2_curve_mw25_to, sced2_curve_price25_from=sced2_curve_price25_from, sced2_curve_price25_to=sced2_curve_price25_to, sced2_curve_mw26_from=sced2_curve_mw26_from, sced2_curve_mw26_to=sced2_curve_mw26_to, sced2_curve_price26_from=sced2_curve_price26_from, sced2_curve_price26_to=sced2_curve_price26_to, sced2_curve_mw27_from=sced2_curve_mw27_from, sced2_curve_mw27_to=sced2_curve_mw27_to, sced2_curve_price27_from=sced2_curve_price27_from, sced2_curve_price27_to=sced2_curve_price27_to, sced2_curve_mw28_from=sced2_curve_mw28_from, sced2_curve_mw28_to=sced2_curve_mw28_to, sced2_curve_price28_from=sced2_curve_price28_from, sced2_curve_price28_to=sced2_curve_price28_to, sced2_curve_mw29_from=sced2_curve_mw29_from, sced2_curve_mw29_to=sced2_curve_mw29_to, sced2_curve_price29_from=sced2_curve_price29_from, sced2_curve_price29_to=sced2_curve_price29_to, sced2_curve_mw30_from=sced2_curve_mw30_from, sced2_curve_mw30_to=sced2_curve_mw30_to, sced2_curve_price30_from=sced2_curve_price30_from, sced2_curve_price30_to=sced2_curve_price30_to, sced2_curve_mw31_from=sced2_curve_mw31_from, sced2_curve_mw31_to=sced2_curve_mw31_to, sced2_curve_price31_from=sced2_curve_price31_from, sced2_curve_price31_to=sced2_curve_price31_to, sced2_curve_mw32_from=sced2_curve_mw32_from, sced2_curve_mw32_to=sced2_curve_mw32_to, sced2_curve_price32_from=sced2_curve_price32_from, sced2_curve_price32_to=sced2_curve_price32_to, sced2_curve_mw33_from=sced2_curve_mw33_from, sced2_curve_mw33_to=sced2_curve_mw33_to, sced2_curve_price33_from=sced2_curve_price33_from, sced2_curve_price33_to=sced2_curve_price33_to, sced2_curve_mw34_from=sced2_curve_mw34_from, sced2_curve_mw34_to=sced2_curve_mw34_to, sced2_curve_price34_from=sced2_curve_price34_from, sced2_curve_price34_to=sced2_curve_price34_to, sced2_curve_mw35_from=sced2_curve_mw35_from, sced2_curve_mw35_to=sced2_curve_mw35_to, sced2_curve_price35_from=sced2_curve_price35_from, sced2_curve_price35_to=sced2_curve_price35_to, output_schedule_from=output_schedule_from, output_schedule_to=output_schedule_to, hsl_from=hsl_from, hslto=hslto, hasl_from=hasl_from, haslto=haslto, hdl_from=hdl_from, hdlto=hdlto, lsl_from=lsl_from, lslto=lslto, lasl_from=lasl_from, laslto=laslto, ldl_from=ldl_from, ldlto=ldlto, telemetered_resource_status=telemetered_resource_status, base_point_from=base_point_from, base_point_to=base_point_to, telemetered_net_output_from=telemetered_net_output_from, telemetered_net_output_to=telemetered_net_output_to, asregup_from=asregup_from, asregupto=asregupto, asregdn_from=asregdn_from, asregdnto=asregdnto, asrrs_from=asrrs_from, asrrsto=asrrsto, asrrsffr_from=asrrsffr_from, asrrsffrto=asrrsffrto, asnsrs_from=asnsrs_from, asnsrsto=asnsrsto, bid_type=bid_type, start_up_cold_offer_from=start_up_cold_offer_from, start_up_cold_offer_to=start_up_cold_offer_to, start_up_hot_offer_from=start_up_hot_offer_from, start_up_hot_offer_to=start_up_hot_offer_to, start_up_inter_offer_from=start_up_inter_offer_from, start_up_inter_offer_to=start_up_inter_offer_to, min_gen_cost_from=min_gen_cost_from, min_gen_cost_to=min_gen_cost_to, submitted_tpomw1_from=submitted_tpomw1_from, submitted_tpomw1_to=submitted_tpomw1_to, submitted_tpo_price1_from=submitted_tpo_price1_from, submitted_tpo_price1_to=submitted_tpo_price1_to, submitted_tpomw2_from=submitted_tpomw2_from, submitted_tpomw2_to=submitted_tpomw2_to, submitted_tpo_price2_from=submitted_tpo_price2_from, submitted_tpo_price2_to=submitted_tpo_price2_to, submitted_tpomw3_from=submitted_tpomw3_from, submitted_tpomw3_to=submitted_tpomw3_to, submitted_tpo_price3_from=submitted_tpo_price3_from, submitted_tpo_price3_to=submitted_tpo_price3_to, submitted_tpomw4_from=submitted_tpomw4_from, submitted_tpomw4_to=submitted_tpomw4_to, submitted_tpo_price4_from=submitted_tpo_price4_from, submitted_tpo_price4_to=submitted_tpo_price4_to, submitted_tpomw5_from=submitted_tpomw5_from, submitted_tpomw5_to=submitted_tpomw5_to, submitted_tpo_price5_from=submitted_tpo_price5_from, submitted_tpo_price5_to=submitted_tpo_price5_to, submitted_tpomw6_from=submitted_tpomw6_from, submitted_tpomw6_to=submitted_tpomw6_to, submitted_tpo_price6_from=submitted_tpo_price6_from, submitted_tpo_price6_to=submitted_tpo_price6_to, submitted_tpomw7_from=submitted_tpomw7_from, submitted_tpomw7_to=submitted_tpomw7_to, submitted_tpo_price7_from=submitted_tpo_price7_from, submitted_tpo_price7_to=submitted_tpo_price7_to, submitted_tpomw8_from=submitted_tpomw8_from, submitted_tpomw8_to=submitted_tpomw8_to, submitted_tpo_price8_from=submitted_tpo_price8_from, submitted_tpo_price8_to=submitted_tpo_price8_to, submitted_tpomw9_from=submitted_tpomw9_from, submitted_tpomw9_to=submitted_tpomw9_to, submitted_tpo_price9_from=submitted_tpo_price9_from, submitted_tpo_price9_to=submitted_tpo_price9_to, submitted_tpomw10_from=submitted_tpomw10_from, submitted_tpomw10_to=submitted_tpomw10_to, submitted_tpo_price10_from=submitted_tpo_price10_from, submitted_tpo_price10_to=submitted_tpo_price10_to, proxy_extension=proxy_extension, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, qse_name=qse_name, dme_name=dme_name, resource_name=resource_name, resource_type=resource_type, sced1_curve_mw1_from=sced1_curve_mw1_from, sced1_curve_mw1_to=sced1_curve_mw1_to, sced1_curve_price1_from=sced1_curve_price1_from, sced1_curve_price1_to=sced1_curve_price1_to, sced1_curve_mw2_from=sced1_curve_mw2_from, sced1_curve_mw2_to=sced1_curve_mw2_to, sced1_curve_price2_from=sced1_curve_price2_from, sced1_curve_price2_to=sced1_curve_price2_to, sced1_curve_mw3_from=sced1_curve_mw3_from, sced1_curve_mw3_to=sced1_curve_mw3_to, sced1_curve_price3_from=sced1_curve_price3_from, sced1_curve_price3_to=sced1_curve_price3_to, sced1_curve_mw4_from=sced1_curve_mw4_from, sced1_curve_mw4_to=sced1_curve_mw4_to, sced1_curve_price4_from=sced1_curve_price4_from, sced1_curve_price4_to=sced1_curve_price4_to, sced1_curve_mw5_from=sced1_curve_mw5_from, sced1_curve_mw5_to=sced1_curve_mw5_to, sced1_curve_price5_from=sced1_curve_price5_from, sced1_curve_price5_to=sced1_curve_price5_to, sced1_curve_mw6_from=sced1_curve_mw6_from, sced1_curve_mw6_to=sced1_curve_mw6_to, sced1_curve_price6_from=sced1_curve_price6_from, sced1_curve_price6_to=sced1_curve_price6_to, sced1_curve_mw7_from=sced1_curve_mw7_from, sced1_curve_mw7_to=sced1_curve_mw7_to, sced1_curve_price7_from=sced1_curve_price7_from, sced1_curve_price7_to=sced1_curve_price7_to, sced1_curve_mw8_from=sced1_curve_mw8_from, sced1_curve_mw8_to=sced1_curve_mw8_to, sced1_curve_price8_from=sced1_curve_price8_from, sced1_curve_price8_to=sced1_curve_price8_to, sced1_curve_mw9_from=sced1_curve_mw9_from, sced1_curve_mw9_to=sced1_curve_mw9_to, sced1_curve_price9_from=sced1_curve_price9_from, sced1_curve_price9_to=sced1_curve_price9_to, sced1_curve_mw10_from=sced1_curve_mw10_from, sced1_curve_mw10_to=sced1_curve_mw10_to, sced1_curve_price10_from=sced1_curve_price10_from, sced1_curve_price10_to=sced1_curve_price10_to, sced1_curve_mw11_from=sced1_curve_mw11_from, sced1_curve_mw11_to=sced1_curve_mw11_to, sced1_curve_price11_from=sced1_curve_price11_from, sced1_curve_price11_to=sced1_curve_price11_to, sced1_curve_mw12_from=sced1_curve_mw12_from, sced1_curve_mw12_to=sced1_curve_mw12_to, sced1_curve_price12_from=sced1_curve_price12_from, sced1_curve_price12_to=sced1_curve_price12_to, sced1_curve_mw13_from=sced1_curve_mw13_from, sced1_curve_mw13_to=sced1_curve_mw13_to, sced1_curve_price13_from=sced1_curve_price13_from, sced1_curve_price13_to=sced1_curve_price13_to, sced1_curve_mw14_from=sced1_curve_mw14_from, sced1_curve_mw14_to=sced1_curve_mw14_to, asecrs_from=asecrs_from, asecrsto=asecrsto, sced1_curve_price14_from=sced1_curve_price14_from, sced1_curve_price14_to=sced1_curve_price14_to, sced1_curve_mw15_from=sced1_curve_mw15_from, sced1_curve_mw15_to=sced1_curve_mw15_to, sced1_curve_price15_from=sced1_curve_price15_from, sced1_curve_price15_to=sced1_curve_price15_to, sced1_curve_mw16_from=sced1_curve_mw16_from, sced1_curve_mw16_to=sced1_curve_mw16_to, sced1_curve_price16_from=sced1_curve_price16_from, sced1_curve_price16_to=sced1_curve_price16_to, sced1_curve_mw17_from=sced1_curve_mw17_from, sced1_curve_mw17_to=sced1_curve_mw17_to, sced1_curve_price17_from=sced1_curve_price17_from, sced1_curve_price17_to=sced1_curve_price17_to, sced1_curve_mw18_from=sced1_curve_mw18_from, sced1_curve_mw18_to=sced1_curve_mw18_to, sced1_curve_price18_from=sced1_curve_price18_from, sced1_curve_price18_to=sced1_curve_price18_to, sced1_curve_mw19_from=sced1_curve_mw19_from, sced1_curve_mw19_to=sced1_curve_mw19_to, sced1_curve_price19_from=sced1_curve_price19_from, sced1_curve_price19_to=sced1_curve_price19_to, sced1_curve_mw20_from=sced1_curve_mw20_from, sced1_curve_mw20_to=sced1_curve_mw20_to, sced1_curve_price20_from=sced1_curve_price20_from, sced1_curve_price20_to=sced1_curve_price20_to, sced1_curve_mw21_from=sced1_curve_mw21_from, sced1_curve_mw21_to=sced1_curve_mw21_to, sced1_curve_price21_from=sced1_curve_price21_from, sced1_curve_price21_to=sced1_curve_price21_to, sced1_curve_mw22_from=sced1_curve_mw22_from, sced1_curve_mw22_to=sced1_curve_mw22_to, sced1_curve_price22_from=sced1_curve_price22_from, sced1_curve_price22_to=sced1_curve_price22_to, sced1_curve_mw23_from=sced1_curve_mw23_from, sced1_curve_mw23_to=sced1_curve_mw23_to, sced1_curve_price23_from=sced1_curve_price23_from, sced1_curve_price23_to=sced1_curve_price23_to, sced1_curve_mw24_from=sced1_curve_mw24_from, sced1_curve_mw24_to=sced1_curve_mw24_to, sced1_curve_price24_from=sced1_curve_price24_from, sced1_curve_price24_to=sced1_curve_price24_to, sced1_curve_mw25_from=sced1_curve_mw25_from, sced1_curve_mw25_to=sced1_curve_mw25_to, sced1_curve_price25_from=sced1_curve_price25_from, sced1_curve_price25_to=sced1_curve_price25_to, sced1_curve_mw26_from=sced1_curve_mw26_from, sced1_curve_mw26_to=sced1_curve_mw26_to, sced1_curve_price26_from=sced1_curve_price26_from, sced1_curve_price26_to=sced1_curve_price26_to, sced1_curve_mw27_from=sced1_curve_mw27_from, sced1_curve_mw27_to=sced1_curve_mw27_to, sced1_curve_price27_from=sced1_curve_price27_from, sced1_curve_price27_to=sced1_curve_price27_to, sced1_curve_mw28_from=sced1_curve_mw28_from, sced1_curve_mw28_to=sced1_curve_mw28_to, sced1_curve_price28_from=sced1_curve_price28_from, sced1_curve_price28_to=sced1_curve_price28_to, sced1_curve_mw29_from=sced1_curve_mw29_from, sced1_curve_mw29_to=sced1_curve_mw29_to, sced1_curve_price29_from=sced1_curve_price29_from, sced1_curve_price29_to=sced1_curve_price29_to, sced1_curve_mw30_from=sced1_curve_mw30_from, sced1_curve_mw30_to=sced1_curve_mw30_to, sced1_curve_price30_from=sced1_curve_price30_from, sced1_curve_price30_to=sced1_curve_price30_to, sced1_curve_mw31_from=sced1_curve_mw31_from, sced1_curve_mw31_to=sced1_curve_mw31_to, sced1_curve_price31_from=sced1_curve_price31_from, sced1_curve_price31_to=sced1_curve_price31_to, sced1_curve_mw32_from=sced1_curve_mw32_from, sced1_curve_mw32_to=sced1_curve_mw32_to, sced1_curve_price32_from=sced1_curve_price32_from, sced1_curve_price32_to=sced1_curve_price32_to, sced1_curve_mw33_from=sced1_curve_mw33_from, sced1_curve_mw33_to=sced1_curve_mw33_to, sced1_curve_price33_from=sced1_curve_price33_from, sced1_curve_price33_to=sced1_curve_price33_to, sced1_curve_mw34_from=sced1_curve_mw34_from, sced1_curve_mw34_to=sced1_curve_mw34_to, sced1_curve_price34_from=sced1_curve_price34_from, sced1_curve_price34_to=sced1_curve_price34_to, sced1_curve_mw35_from=sced1_curve_mw35_from, sced1_curve_mw35_to=sced1_curve_mw35_to, sced1_curve_price35_from=sced1_curve_price35_from, sced1_curve_price35_to=sced1_curve_price35_to, sced2_curve_mw1_from=sced2_curve_mw1_from, sced2_curve_mw1_to=sced2_curve_mw1_to, sced2_curve_price1_from=sced2_curve_price1_from, sced2_curve_price1_to=sced2_curve_price1_to, sced2_curve_mw2_from=sced2_curve_mw2_from, sced2_curve_mw2_to=sced2_curve_mw2_to, sced2_curve_price2_from=sced2_curve_price2_from, sced2_curve_price2_to=sced2_curve_price2_to, sced2_curve_mw3_from=sced2_curve_mw3_from, sced2_curve_mw3_to=sced2_curve_mw3_to, sced2_curve_price3_from=sced2_curve_price3_from, sced2_curve_price3_to=sced2_curve_price3_to, sced2_curve_mw4_from=sced2_curve_mw4_from, sced2_curve_mw4_to=sced2_curve_mw4_to, sced2_curve_price4_from=sced2_curve_price4_from, sced2_curve_price4_to=sced2_curve_price4_to, sced2_curve_mw5_from=sced2_curve_mw5_from, sced2_curve_mw5_to=sced2_curve_mw5_to, sced2_curve_price5_from=sced2_curve_price5_from, sced2_curve_price5_to=sced2_curve_price5_to, sced2_curve_mw6_from=sced2_curve_mw6_from, sced2_curve_mw6_to=sced2_curve_mw6_to, sced2_curve_price6_from=sced2_curve_price6_from, sced2_curve_price6_to=sced2_curve_price6_to, sced2_curve_mw7_from=sced2_curve_mw7_from, sced2_curve_mw7_to=sced2_curve_mw7_to, sced2_curve_price7_from=sced2_curve_price7_from, sced2_curve_price7_to=sced2_curve_price7_to, sced2_curve_mw8_from=sced2_curve_mw8_from, sced2_curve_mw8_to=sced2_curve_mw8_to, sced2_curve_price8_from=sced2_curve_price8_from, sced2_curve_price8_to=sced2_curve_price8_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3965ERApi->get_data53:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3965ERApi->get_data53: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sced2_curve_mw9_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw9_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price9_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price9_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw10_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw10_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price10_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price10_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw11_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw11_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price11_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price11_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw12_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw12_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price12_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price12_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw13_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw13_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price13_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price13_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw14_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw14_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price14_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price14_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw15_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw15_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price15_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price15_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw16_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw16_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price16_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price16_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw17_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw17_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price17_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price17_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw18_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw18_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price18_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price18_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw19_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw19_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price19_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price19_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw20_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw20_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price20_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price20_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw21_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw21_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price21_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price21_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw22_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw22_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price22_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price22_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw23_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw23_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price23_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price23_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw24_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw24_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price24_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price24_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw25_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw25_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price25_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price25_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw26_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw26_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price26_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price26_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw27_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw27_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price27_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price27_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw28_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw28_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price28_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price28_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw29_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw29_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price29_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price29_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw30_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw30_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price30_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price30_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw31_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw31_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price31_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price31_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw32_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw32_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price32_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price32_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw33_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw33_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price33_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price33_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw34_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw34_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price34_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price34_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw35_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw35_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price35_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price35_to** | **float**| Format - ####.###. | [optional] 
 **output_schedule_from** | **float**| Format - ####.###. | [optional] 
 **output_schedule_to** | **float**| Format - ####.###. | [optional] 
 **hsl_from** | **float**| Format - ####.###. | [optional] 
 **hslto** | **float**| Format - ####.###. | [optional] 
 **hasl_from** | **float**| Format - ####.###. | [optional] 
 **haslto** | **float**| Format - ####.###. | [optional] 
 **hdl_from** | **float**| Format - ####.###. | [optional] 
 **hdlto** | **float**| Format - ####.###. | [optional] 
 **lsl_from** | **float**| Format - ####.###. | [optional] 
 **lslto** | **float**| Format - ####.###. | [optional] 
 **lasl_from** | **float**| Format - ####.###. | [optional] 
 **laslto** | **float**| Format - ####.###. | [optional] 
 **ldl_from** | **float**| Format - ####.###. | [optional] 
 **ldlto** | **float**| Format - ####.###. | [optional] 
 **telemetered_resource_status** | **str**| Format - abc123. | [optional] 
 **base_point_from** | **float**| Format - ####.###. | [optional] 
 **base_point_to** | **float**| Format - ####.###. | [optional] 
 **telemetered_net_output_from** | **float**| Format - ####.###. | [optional] 
 **telemetered_net_output_to** | **float**| Format - ####.###. | [optional] 
 **asregup_from** | **float**| Format - ####.###. | [optional] 
 **asregupto** | **float**| Format - ####.###. | [optional] 
 **asregdn_from** | **float**| Format - ####.###. | [optional] 
 **asregdnto** | **float**| Format - ####.###. | [optional] 
 **asrrs_from** | **float**| Format - ####.###. | [optional] 
 **asrrsto** | **float**| Format - ####.###. | [optional] 
 **asrrsffr_from** | **float**| Format - ####.###. | [optional] 
 **asrrsffrto** | **float**| Format - ####.###. | [optional] 
 **asnsrs_from** | **float**| Format - ####.###. | [optional] 
 **asnsrsto** | **float**| Format - ####.###. | [optional] 
 **bid_type** | **str**| Format - abc123. | [optional] 
 **start_up_cold_offer_from** | **float**| Format - ####.###. | [optional] 
 **start_up_cold_offer_to** | **float**| Format - ####.###. | [optional] 
 **start_up_hot_offer_from** | **float**| Format - ####.###. | [optional] 
 **start_up_hot_offer_to** | **float**| Format - ####.###. | [optional] 
 **start_up_inter_offer_from** | **float**| Format - ####.###. | [optional] 
 **start_up_inter_offer_to** | **float**| Format - ####.###. | [optional] 
 **min_gen_cost_from** | **float**| Format - ####.###. | [optional] 
 **min_gen_cost_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw1_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw1_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price1_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price1_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw2_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw2_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price2_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price2_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw3_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw3_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price3_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price3_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw4_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw4_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price4_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price4_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw5_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw5_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price5_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price5_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw6_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw6_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price6_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price6_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw7_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw7_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price7_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price7_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw8_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw8_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price8_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price8_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw9_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw9_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price9_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price9_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw10_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpomw10_to** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price10_from** | **float**| Format - ####.###. | [optional] 
 **submitted_tpo_price10_to** | **float**| Format - ####.###. | [optional] 
 **proxy_extension** | **str**| Format - abc123. | [optional] 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **qse_name** | **str**| Format - abc123. | [optional] 
 **dme_name** | **str**| Format - abc123. | [optional] 
 **resource_name** | **str**| Format - abc123. | [optional] 
 **resource_type** | **str**| Format - abc123. | [optional] 
 **sced1_curve_mw1_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw1_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price1_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price1_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw2_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw2_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price2_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price2_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw3_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw3_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price3_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price3_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw4_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw4_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price4_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price4_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw5_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw5_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price5_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price5_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw6_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw6_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price6_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price6_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw7_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw7_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price7_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price7_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw8_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw8_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price8_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price8_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw9_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw9_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price9_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price9_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw10_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw10_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price10_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price10_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw11_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw11_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price11_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price11_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw12_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw12_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price12_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price12_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw13_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw13_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price13_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price13_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw14_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw14_to** | **float**| Format - ####.###. | [optional] 
 **asecrs_from** | **float**| Format - ####.###. | [optional] 
 **asecrsto** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price14_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price14_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw15_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw15_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price15_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price15_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw16_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw16_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price16_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price16_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw17_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw17_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price17_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price17_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw18_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw18_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price18_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price18_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw19_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw19_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price19_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price19_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw20_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw20_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price20_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price20_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw21_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw21_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price21_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price21_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw22_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw22_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price22_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price22_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw23_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw23_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price23_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price23_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw24_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw24_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price24_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price24_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw25_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw25_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price25_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price25_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw26_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw26_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price26_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price26_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw27_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw27_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price27_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price27_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw28_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw28_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price28_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price28_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw29_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw29_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price29_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price29_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw30_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw30_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price30_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price30_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw31_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw31_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price31_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price31_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw32_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw32_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price32_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price32_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw33_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw33_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price33_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price33_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw34_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw34_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price34_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price34_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw35_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_mw35_to** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price35_from** | **float**| Format - ####.###. | [optional] 
 **sced1_curve_price35_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw1_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw1_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price1_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price1_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw2_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw2_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price2_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price2_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw3_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw3_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price3_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price3_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw4_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw4_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price4_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price4_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw5_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw5_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price5_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price5_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw6_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw6_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price6_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price6_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw7_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw7_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price7_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price7_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw8_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_mw8_to** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price8_from** | **float**| Format - ####.###. | [optional] 
 **sced2_curve_price8_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data54**
> Report get_data54(ocp_apim_subscription_key, qse_name=qse_name, total_telemetered_dsr_loads_from=total_telemetered_dsr_loads_from, total_telemetered_dsr_loads_to=total_telemetered_dsr_loads_to, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, page=page, size=size, sort=sort, dir=dir)

60 Day SCED DSR Load Data

60 Day SCED DSR Load Data

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
    api_instance = openapi_client.NP3965ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    total_telemetered_dsr_loads_from = 3.4 # float | Format - ####.###. (optional)
    total_telemetered_dsr_loads_to = 3.4 # float | Format - ####.###. (optional)
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day SCED DSR Load Data
        api_response = api_instance.get_data54(ocp_apim_subscription_key, qse_name=qse_name, total_telemetered_dsr_loads_from=total_telemetered_dsr_loads_from, total_telemetered_dsr_loads_to=total_telemetered_dsr_loads_to, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3965ERApi->get_data54:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3965ERApi->get_data54: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **qse_name** | **str**| Format - abc123. | [optional] 
 **total_telemetered_dsr_loads_from** | **float**| Format - ####.###. | [optional] 
 **total_telemetered_dsr_loads_to** | **float**| Format - ####.###. | [optional] 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
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

# **get_data55**
> Report get_data55(ocp_apim_subscription_key, as_resp_for_nspin_from=as_resp_for_nspin_from, as_resp_for_nspinto=as_resp_for_nspinto, as_resp_for_regup_from=as_resp_for_regup_from, as_resp_for_regupto=as_resp_for_regupto, as_resp_for_regdn_from=as_resp_for_regdn_from, as_resp_for_regdnto=as_resp_for_regdnto, sced_bid_curve_mw1_from=sced_bid_curve_mw1_from, sced_bid_curve_mw1_to=sced_bid_curve_mw1_to, sced_bid_curve_price1_from=sced_bid_curve_price1_from, sced_bid_curve_price1_to=sced_bid_curve_price1_to, sced_bid_curve_mw2_from=sced_bid_curve_mw2_from, sced_bid_curve_mw2_to=sced_bid_curve_mw2_to, as_resp_for_ecrs_from=as_resp_for_ecrs_from, as_resp_for_ecrsto=as_resp_for_ecrsto, sced_bid_curve_price2_from=sced_bid_curve_price2_from, sced_bid_curve_price2_to=sced_bid_curve_price2_to, sced_bid_curve_mw3_from=sced_bid_curve_mw3_from, sced_bid_curve_mw3_to=sced_bid_curve_mw3_to, sced_bid_curve_price3_from=sced_bid_curve_price3_from, sced_bid_curve_price3_to=sced_bid_curve_price3_to, sced_bid_curve_mw4_from=sced_bid_curve_mw4_from, sced_bid_curve_mw4_to=sced_bid_curve_mw4_to, sced_bid_curve_price4_from=sced_bid_curve_price4_from, sced_bid_curve_price4_to=sced_bid_curve_price4_to, sced_bid_curve_mw5_from=sced_bid_curve_mw5_from, sced_bid_curve_mw5_to=sced_bid_curve_mw5_to, sced_bid_curve_price5_from=sced_bid_curve_price5_from, sced_bid_curve_price5_to=sced_bid_curve_price5_to, sced_bid_curve_mw6_from=sced_bid_curve_mw6_from, sced_bid_curve_mw6_to=sced_bid_curve_mw6_to, sced_bid_curve_price6_from=sced_bid_curve_price6_from, sced_bid_curve_price6_to=sced_bid_curve_price6_to, sced_bid_curve_mw7_from=sced_bid_curve_mw7_from, sced_bid_curve_mw7_to=sced_bid_curve_mw7_to, sced_bid_curve_price7_from=sced_bid_curve_price7_from, sced_bid_curve_price7_to=sced_bid_curve_price7_to, sced_bid_curve_mw8_from=sced_bid_curve_mw8_from, sced_bid_curve_mw8_to=sced_bid_curve_mw8_to, sced_bid_curve_price8_from=sced_bid_curve_price8_from, sced_bid_curve_price8_to=sced_bid_curve_price8_to, sced_bid_curve_mw9_from=sced_bid_curve_mw9_from, sced_bid_curve_mw9_to=sced_bid_curve_mw9_to, sced_bid_curve_price9_from=sced_bid_curve_price9_from, sced_bid_curve_price9_to=sced_bid_curve_price9_to, sced_bid_curve_mw10_from=sced_bid_curve_mw10_from, sced_bid_curve_mw10_to=sced_bid_curve_mw10_to, sced_bid_curve_price10_from=sced_bid_curve_price10_from, sced_bid_curve_price10_to=sced_bid_curve_price10_to, hasl_from=hasl_from, haslto=haslto, hdl_from=hdl_from, hdlto=hdlto, lasl_from=lasl_from, laslto=laslto, ldl_from=ldl_from, ldlto=ldlto, base_point_from=base_point_from, base_point_to=base_point_to, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, qse_name=qse_name, dme_name=dme_name, resource_name=resource_name, tel_res_status=tel_res_status, max_power_consumption_from=max_power_consumption_from, max_power_consumption_to=max_power_consumption_to, low_power_consumption_from=low_power_consumption_from, low_power_consumption_to=low_power_consumption_to, real_power_consumption_from=real_power_consumption_from, real_power_consumption_to=real_power_consumption_to, as_resp_for_rrs_from=as_resp_for_rrs_from, as_resp_for_rrsto=as_resp_for_rrsto, as_resp_for_rrsffr_from=as_resp_for_rrsffr_from, as_resp_for_rrsffrto=as_resp_for_rrsffrto, page=page, size=size, sort=sort, dir=dir)

60 Day Load Resource Data in SCED

60 Day Load Resource Data in SCED

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
    api_instance = openapi_client.NP3965ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    as_resp_for_nspin_from = 3.4 # float | Format - ####.###. (optional)
    as_resp_for_nspinto = 3.4 # float | Format - ####.###. (optional)
    as_resp_for_regup_from = 3.4 # float | Format - ####.###. (optional)
    as_resp_for_regupto = 3.4 # float | Format - ####.###. (optional)
    as_resp_for_regdn_from = 3.4 # float | Format - ####.###. (optional)
    as_resp_for_regdnto = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw1_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw1_to = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price1_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price1_to = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw2_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw2_to = 3.4 # float | Format - ####.###. (optional)
    as_resp_for_ecrs_from = 3.4 # float | Format - ####.###. (optional)
    as_resp_for_ecrsto = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price2_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price2_to = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw3_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw3_to = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price3_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price3_to = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw4_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw4_to = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price4_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price4_to = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw5_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw5_to = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price5_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price5_to = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw6_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw6_to = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price6_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price6_to = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw7_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw7_to = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price7_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price7_to = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw8_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw8_to = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price8_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price8_to = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw9_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw9_to = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price9_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price9_to = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw10_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_mw10_to = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price10_from = 3.4 # float | Format - ####.###. (optional)
    sced_bid_curve_price10_to = 3.4 # float | Format - ####.###. (optional)
    hasl_from = 3.4 # float | Format - ####.###. (optional)
    haslto = 3.4 # float | Format - ####.###. (optional)
    hdl_from = 3.4 # float | Format - ####.###. (optional)
    hdlto = 3.4 # float | Format - ####.###. (optional)
    lasl_from = 3.4 # float | Format - ####.###. (optional)
    laslto = 3.4 # float | Format - ####.###. (optional)
    ldl_from = 3.4 # float | Format - ####.###. (optional)
    ldlto = 3.4 # float | Format - ####.###. (optional)
    base_point_from = 3.4 # float | Format - ####.###. (optional)
    base_point_to = 3.4 # float | Format - ####.###. (optional)
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    dme_name = 'dme_name_example' # str | Format - abc123. (optional)
    resource_name = 'resource_name_example' # str | Format - abc123. (optional)
    tel_res_status = 'tel_res_status_example' # str | Format - abc123. (optional)
    max_power_consumption_from = 3.4 # float | Format - ####.###. (optional)
    max_power_consumption_to = 3.4 # float | Format - ####.###. (optional)
    low_power_consumption_from = 3.4 # float | Format - ####.###. (optional)
    low_power_consumption_to = 3.4 # float | Format - ####.###. (optional)
    real_power_consumption_from = 3.4 # float | Format - ####.###. (optional)
    real_power_consumption_to = 3.4 # float | Format - ####.###. (optional)
    as_resp_for_rrs_from = 3.4 # float | Format - ####.###. (optional)
    as_resp_for_rrsto = 3.4 # float | Format - ####.###. (optional)
    as_resp_for_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    as_resp_for_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day Load Resource Data in SCED
        api_response = api_instance.get_data55(ocp_apim_subscription_key, as_resp_for_nspin_from=as_resp_for_nspin_from, as_resp_for_nspinto=as_resp_for_nspinto, as_resp_for_regup_from=as_resp_for_regup_from, as_resp_for_regupto=as_resp_for_regupto, as_resp_for_regdn_from=as_resp_for_regdn_from, as_resp_for_regdnto=as_resp_for_regdnto, sced_bid_curve_mw1_from=sced_bid_curve_mw1_from, sced_bid_curve_mw1_to=sced_bid_curve_mw1_to, sced_bid_curve_price1_from=sced_bid_curve_price1_from, sced_bid_curve_price1_to=sced_bid_curve_price1_to, sced_bid_curve_mw2_from=sced_bid_curve_mw2_from, sced_bid_curve_mw2_to=sced_bid_curve_mw2_to, as_resp_for_ecrs_from=as_resp_for_ecrs_from, as_resp_for_ecrsto=as_resp_for_ecrsto, sced_bid_curve_price2_from=sced_bid_curve_price2_from, sced_bid_curve_price2_to=sced_bid_curve_price2_to, sced_bid_curve_mw3_from=sced_bid_curve_mw3_from, sced_bid_curve_mw3_to=sced_bid_curve_mw3_to, sced_bid_curve_price3_from=sced_bid_curve_price3_from, sced_bid_curve_price3_to=sced_bid_curve_price3_to, sced_bid_curve_mw4_from=sced_bid_curve_mw4_from, sced_bid_curve_mw4_to=sced_bid_curve_mw4_to, sced_bid_curve_price4_from=sced_bid_curve_price4_from, sced_bid_curve_price4_to=sced_bid_curve_price4_to, sced_bid_curve_mw5_from=sced_bid_curve_mw5_from, sced_bid_curve_mw5_to=sced_bid_curve_mw5_to, sced_bid_curve_price5_from=sced_bid_curve_price5_from, sced_bid_curve_price5_to=sced_bid_curve_price5_to, sced_bid_curve_mw6_from=sced_bid_curve_mw6_from, sced_bid_curve_mw6_to=sced_bid_curve_mw6_to, sced_bid_curve_price6_from=sced_bid_curve_price6_from, sced_bid_curve_price6_to=sced_bid_curve_price6_to, sced_bid_curve_mw7_from=sced_bid_curve_mw7_from, sced_bid_curve_mw7_to=sced_bid_curve_mw7_to, sced_bid_curve_price7_from=sced_bid_curve_price7_from, sced_bid_curve_price7_to=sced_bid_curve_price7_to, sced_bid_curve_mw8_from=sced_bid_curve_mw8_from, sced_bid_curve_mw8_to=sced_bid_curve_mw8_to, sced_bid_curve_price8_from=sced_bid_curve_price8_from, sced_bid_curve_price8_to=sced_bid_curve_price8_to, sced_bid_curve_mw9_from=sced_bid_curve_mw9_from, sced_bid_curve_mw9_to=sced_bid_curve_mw9_to, sced_bid_curve_price9_from=sced_bid_curve_price9_from, sced_bid_curve_price9_to=sced_bid_curve_price9_to, sced_bid_curve_mw10_from=sced_bid_curve_mw10_from, sced_bid_curve_mw10_to=sced_bid_curve_mw10_to, sced_bid_curve_price10_from=sced_bid_curve_price10_from, sced_bid_curve_price10_to=sced_bid_curve_price10_to, hasl_from=hasl_from, haslto=haslto, hdl_from=hdl_from, hdlto=hdlto, lasl_from=lasl_from, laslto=laslto, ldl_from=ldl_from, ldlto=ldlto, base_point_from=base_point_from, base_point_to=base_point_to, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, qse_name=qse_name, dme_name=dme_name, resource_name=resource_name, tel_res_status=tel_res_status, max_power_consumption_from=max_power_consumption_from, max_power_consumption_to=max_power_consumption_to, low_power_consumption_from=low_power_consumption_from, low_power_consumption_to=low_power_consumption_to, real_power_consumption_from=real_power_consumption_from, real_power_consumption_to=real_power_consumption_to, as_resp_for_rrs_from=as_resp_for_rrs_from, as_resp_for_rrsto=as_resp_for_rrsto, as_resp_for_rrsffr_from=as_resp_for_rrsffr_from, as_resp_for_rrsffrto=as_resp_for_rrsffrto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3965ERApi->get_data55:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3965ERApi->get_data55: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **as_resp_for_nspin_from** | **float**| Format - ####.###. | [optional] 
 **as_resp_for_nspinto** | **float**| Format - ####.###. | [optional] 
 **as_resp_for_regup_from** | **float**| Format - ####.###. | [optional] 
 **as_resp_for_regupto** | **float**| Format - ####.###. | [optional] 
 **as_resp_for_regdn_from** | **float**| Format - ####.###. | [optional] 
 **as_resp_for_regdnto** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw1_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw1_to** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price1_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price1_to** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw2_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw2_to** | **float**| Format - ####.###. | [optional] 
 **as_resp_for_ecrs_from** | **float**| Format - ####.###. | [optional] 
 **as_resp_for_ecrsto** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price2_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price2_to** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw3_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw3_to** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price3_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price3_to** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw4_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw4_to** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price4_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price4_to** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw5_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw5_to** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price5_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price5_to** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw6_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw6_to** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price6_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price6_to** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw7_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw7_to** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price7_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price7_to** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw8_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw8_to** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price8_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price8_to** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw9_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw9_to** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price9_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price9_to** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw10_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_mw10_to** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price10_from** | **float**| Format - ####.###. | [optional] 
 **sced_bid_curve_price10_to** | **float**| Format - ####.###. | [optional] 
 **hasl_from** | **float**| Format - ####.###. | [optional] 
 **haslto** | **float**| Format - ####.###. | [optional] 
 **hdl_from** | **float**| Format - ####.###. | [optional] 
 **hdlto** | **float**| Format - ####.###. | [optional] 
 **lasl_from** | **float**| Format - ####.###. | [optional] 
 **laslto** | **float**| Format - ####.###. | [optional] 
 **ldl_from** | **float**| Format - ####.###. | [optional] 
 **ldlto** | **float**| Format - ####.###. | [optional] 
 **base_point_from** | **float**| Format - ####.###. | [optional] 
 **base_point_to** | **float**| Format - ####.###. | [optional] 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **qse_name** | **str**| Format - abc123. | [optional] 
 **dme_name** | **str**| Format - abc123. | [optional] 
 **resource_name** | **str**| Format - abc123. | [optional] 
 **tel_res_status** | **str**| Format - abc123. | [optional] 
 **max_power_consumption_from** | **float**| Format - ####.###. | [optional] 
 **max_power_consumption_to** | **float**| Format - ####.###. | [optional] 
 **low_power_consumption_from** | **float**| Format - ####.###. | [optional] 
 **low_power_consumption_to** | **float**| Format - ####.###. | [optional] 
 **real_power_consumption_from** | **float**| Format - ####.###. | [optional] 
 **real_power_consumption_to** | **float**| Format - ####.###. | [optional] 
 **as_resp_for_rrs_from** | **float**| Format - ####.###. | [optional] 
 **as_resp_for_rrsto** | **float**| Format - ####.###. | [optional] 
 **as_resp_for_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **as_resp_for_rrsffrto** | **float**| Format - ####.###. | [optional] 
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

# **get_data56**
> Report get_data56(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, participant_name=participant_name, resource_name=resource_name, hdl_original_from=hdl_original_from, hdl_original_to=hdl_original_to, hdl_manual_from=hdl_manual_from, hdl_manual_to=hdl_manual_to, hdl_final_from=hdl_final_from, hdl_final_to=hdl_final_to, ldl_original_from=ldl_original_from, ldl_original_to=ldl_original_to, ldl_manual_from=ldl_manual_from, ldl_manual_to=ldl_manual_to, ldl_final_from=ldl_final_from, ldl_final_to=ldl_final_to, reason_code=reason_code, page=page, size=size, sort=sort, dir=dir)

60 Day HDL and LDL Manual Override Summary

60 Day HDL and LDL Manual Override Summary

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
    api_instance = openapi_client.NP3965ERApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sced_timestamp_from = 'sced_timestamp_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sced_timestamp_to = 'sced_timestamp_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    repeat_hour_flag = True # bool | Format - true | false. (optional)
    participant_name = 'participant_name_example' # str | Format - abc123. (optional)
    resource_name = 'resource_name_example' # str | Format - abc123. (optional)
    hdl_original_from = 3.4 # float | Format - ####.###. (optional)
    hdl_original_to = 3.4 # float | Format - ####.###. (optional)
    hdl_manual_from = 3.4 # float | Format - ####.###. (optional)
    hdl_manual_to = 3.4 # float | Format - ####.###. (optional)
    hdl_final_from = 3.4 # float | Format - ####.###. (optional)
    hdl_final_to = 3.4 # float | Format - ####.###. (optional)
    ldl_original_from = 3.4 # float | Format - ####.###. (optional)
    ldl_original_to = 3.4 # float | Format - ####.###. (optional)
    ldl_manual_from = 3.4 # float | Format - ####.###. (optional)
    ldl_manual_to = 3.4 # float | Format - ####.###. (optional)
    ldl_final_from = 3.4 # float | Format - ####.###. (optional)
    ldl_final_to = 3.4 # float | Format - ####.###. (optional)
    reason_code = 'reason_code_example' # str | Format - abc123. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day HDL and LDL Manual Override Summary
        api_response = api_instance.get_data56(ocp_apim_subscription_key, sced_timestamp_from=sced_timestamp_from, sced_timestamp_to=sced_timestamp_to, repeat_hour_flag=repeat_hour_flag, participant_name=participant_name, resource_name=resource_name, hdl_original_from=hdl_original_from, hdl_original_to=hdl_original_to, hdl_manual_from=hdl_manual_from, hdl_manual_to=hdl_manual_to, hdl_final_from=hdl_final_from, hdl_final_to=hdl_final_to, ldl_original_from=ldl_original_from, ldl_original_to=ldl_original_to, ldl_manual_from=ldl_manual_from, ldl_manual_to=ldl_manual_to, ldl_final_from=ldl_final_from, ldl_final_to=ldl_final_to, reason_code=reason_code, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3965ERApi->get_data56:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3965ERApi->get_data56: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sced_timestamp_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sced_timestamp_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **repeat_hour_flag** | **bool**| Format - true | false. | [optional] 
 **participant_name** | **str**| Format - abc123. | [optional] 
 **resource_name** | **str**| Format - abc123. | [optional] 
 **hdl_original_from** | **float**| Format - ####.###. | [optional] 
 **hdl_original_to** | **float**| Format - ####.###. | [optional] 
 **hdl_manual_from** | **float**| Format - ####.###. | [optional] 
 **hdl_manual_to** | **float**| Format - ####.###. | [optional] 
 **hdl_final_from** | **float**| Format - ####.###. | [optional] 
 **hdl_final_to** | **float**| Format - ####.###. | [optional] 
 **ldl_original_from** | **float**| Format - ####.###. | [optional] 
 **ldl_original_to** | **float**| Format - ####.###. | [optional] 
 **ldl_manual_from** | **float**| Format - ####.###. | [optional] 
 **ldl_manual_to** | **float**| Format - ####.###. | [optional] 
 **ldl_final_from** | **float**| Format - ####.###. | [optional] 
 **ldl_final_to** | **float**| Format - ####.###. | [optional] 
 **reason_code** | **str**| Format - abc123. | [optional] 
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

