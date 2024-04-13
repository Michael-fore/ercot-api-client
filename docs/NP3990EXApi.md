# openapi_client.NP3990EXApi

All URIs are relative to *https://api.ercot.com/api/public-reports*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_data34**](NP3990EXApi.md#get_data34) | **GET** /np3-990-ex/60_sasm_load_res_as_offers | 60 Day SASM Load Resource AS Offers
[**get_data35**](NP3990EXApi.md#get_data35) | **GET** /np3-990-ex/60_sasm_load_res_as_offer_awards | 60 Day SASM Load Resource AS Offer Awards
[**get_data36**](NP3990EXApi.md#get_data36) | **GET** /np3-990-ex/60_sasm_gen_res_as_offers | 60 Day SASM Generation Resource AS Offers
[**get_data37**](NP3990EXApi.md#get_data37) | **GET** /np3-990-ex/60_sasm_gen_res_as_offer_awards | 60 Day SASM Generation Resource AS Offer Awards


# **get_data34**
> Report get_data34(ocp_apim_subscription_key, resource_name=resource_name, multi_hour_block_flag=multi_hour_block_flag, block_indicator1=block_indicator1, price1_rrspfr_from=price1_rrspfr_from, price1_rrspfrto=price1_rrspfrto, price1_rrsffr_from=price1_rrsffr_from, price1_rrsffrto=price1_rrsffrto, price1_rrsufr_from=price1_rrsufr_from, price1_rrsufrto=price1_rrsufrto, price1_online_nonspin_from=price1_online_nonspin_from, price1_online_nonspinto=price1_online_nonspinto, price1_regup_from=price1_regup_from, price1_regupto=price1_regupto, price1_regdown_from=price1_regdown_from, price1_regdownto=price1_regdownto, price1_offline_nonspin_from=price1_offline_nonspin_from, price1_offline_nonspinto=price1_offline_nonspinto, quantity_mw1_from=quantity_mw1_from, quantity_mw1_to=quantity_mw1_to, block_indicator2=block_indicator2, price2_rrspfr_from=price2_rrspfr_from, price2_rrspfrto=price2_rrspfrto, price2_rrsffr_from=price2_rrsffr_from, price2_rrsffrto=price2_rrsffrto, price2_rrsufr_from=price2_rrsufr_from, price2_rrsufrto=price2_rrsufrto, price2_online_nonspin_from=price2_online_nonspin_from, price2_online_nonspinto=price2_online_nonspinto, price2_regup_from=price2_regup_from, price2_regupto=price2_regupto, price2_regdown_from=price2_regdown_from, price2_regdownto=price2_regdownto, price2_offline_nonspin_from=price2_offline_nonspin_from, price2_offline_nonspinto=price2_offline_nonspinto, quantity_mw2_from=quantity_mw2_from, quantity_mw2_to=quantity_mw2_to, block_indicator3=block_indicator3, price3_rrspfr_from=price3_rrspfr_from, price3_rrspfrto=price3_rrspfrto, price3_rrsffr_from=price3_rrsffr_from, price3_rrsffrto=price3_rrsffrto, price3_rrsufr_from=price3_rrsufr_from, price3_rrsufrto=price3_rrsufrto, price3_online_nonspin_from=price3_online_nonspin_from, price3_online_nonspinto=price3_online_nonspinto, price3_regup_from=price3_regup_from, price3_regupto=price3_regupto, price3_regdown_from=price3_regdown_from, price3_regdownto=price3_regdownto, price3_offline_nonspin_from=price3_offline_nonspin_from, price3_offline_nonspinto=price3_offline_nonspinto, quantity_mw3_from=quantity_mw3_from, quantity_mw3_to=quantity_mw3_to, block_indicator4=block_indicator4, price4_rrspfr_from=price4_rrspfr_from, price4_rrspfrto=price4_rrspfrto, price4_rrsffr_from=price4_rrsffr_from, price4_rrsffrto=price4_rrsffrto, price4_rrsufr_from=price4_rrsufr_from, price4_rrsufrto=price4_rrsufrto, price4_online_nonspin_from=price4_online_nonspin_from, price4_online_nonspinto=price4_online_nonspinto, price4_regup_from=price4_regup_from, price4_regupto=price4_regupto, price4_regdown_from=price4_regdown_from, price4_regdownto=price4_regdownto, price4_offline_nonspin_from=price4_offline_nonspin_from, price4_offline_nonspinto=price4_offline_nonspinto, quantity_mw4_from=quantity_mw4_from, quantity_mw4_to=quantity_mw4_to, block_indicator5=block_indicator5, price5_rrspfr_from=price5_rrspfr_from, price5_rrspfrto=price5_rrspfrto, price5_rrsffr_from=price5_rrsffr_from, price5_rrsffrto=price5_rrsffrto, price5_rrsufr_from=price5_rrsufr_from, price5_rrsufrto=price5_rrsufrto, price5_online_nonspin_from=price5_online_nonspin_from, price5_online_nonspinto=price5_online_nonspinto, price5_regup=price5_regup, price5_regdown=price5_regdown, price5_offline_nonspin=price5_offline_nonspin, quantity_mw5_from=quantity_mw5_from, quantity_mw5_to=quantity_mw5_to, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, sasmid_from=sasmid_from, sasmid_to=sasmid_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, dme_name=dme_name, page=page, size=size, sort=sort, dir=dir)

60 Day SASM Load Resource AS Offers

60 Day SASM Load Resource AS Offers

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
    api_instance = openapi_client.NP3990EXApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    resource_name = 'resource_name_example' # str | Format - abc123. (optional)
    multi_hour_block_flag = True # bool | Format - true | false. (optional)
    block_indicator1 = 'block_indicator1_example' # str | Format - abc123. (optional)
    price1_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price1_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price1_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price1_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price1_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price1_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price1_online_nonspin_from = 3.4 # float | Format - ####.###. (optional)
    price1_online_nonspinto = 3.4 # float | Format - ####.###. (optional)
    price1_regup_from = 3.4 # float | Format - ####.###. (optional)
    price1_regupto = 3.4 # float | Format - ####.###. (optional)
    price1_regdown_from = 3.4 # float | Format - ####.###. (optional)
    price1_regdownto = 3.4 # float | Format - ####.###. (optional)
    price1_offline_nonspin_from = 3.4 # float | Format - ####.###. (optional)
    price1_offline_nonspinto = 3.4 # float | Format - ####.###. (optional)
    quantity_mw1_from = 56 # int | Format - ###. (optional)
    quantity_mw1_to = 56 # int | Format - ###. (optional)
    block_indicator2 = 'block_indicator2_example' # str | Format - abc123. (optional)
    price2_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price2_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price2_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price2_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price2_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price2_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price2_online_nonspin_from = 3.4 # float | Format - ####.###. (optional)
    price2_online_nonspinto = 3.4 # float | Format - ####.###. (optional)
    price2_regup_from = 3.4 # float | Format - ####.###. (optional)
    price2_regupto = 3.4 # float | Format - ####.###. (optional)
    price2_regdown_from = 3.4 # float | Format - ####.###. (optional)
    price2_regdownto = 3.4 # float | Format - ####.###. (optional)
    price2_offline_nonspin_from = 3.4 # float | Format - ####.###. (optional)
    price2_offline_nonspinto = 3.4 # float | Format - ####.###. (optional)
    quantity_mw2_from = 56 # int | Format - ###. (optional)
    quantity_mw2_to = 56 # int | Format - ###. (optional)
    block_indicator3 = 'block_indicator3_example' # str | Format - abc123. (optional)
    price3_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price3_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price3_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price3_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price3_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price3_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price3_online_nonspin_from = 3.4 # float | Format - ####.###. (optional)
    price3_online_nonspinto = 3.4 # float | Format - ####.###. (optional)
    price3_regup_from = 3.4 # float | Format - ####.###. (optional)
    price3_regupto = 3.4 # float | Format - ####.###. (optional)
    price3_regdown_from = 3.4 # float | Format - ####.###. (optional)
    price3_regdownto = 3.4 # float | Format - ####.###. (optional)
    price3_offline_nonspin_from = 3.4 # float | Format - ####.###. (optional)
    price3_offline_nonspinto = 3.4 # float | Format - ####.###. (optional)
    quantity_mw3_from = 56 # int | Format - ###. (optional)
    quantity_mw3_to = 56 # int | Format - ###. (optional)
    block_indicator4 = 'block_indicator4_example' # str | Format - abc123. (optional)
    price4_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price4_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price4_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price4_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price4_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price4_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price4_online_nonspin_from = 3.4 # float | Format - ####.###. (optional)
    price4_online_nonspinto = 3.4 # float | Format - ####.###. (optional)
    price4_regup_from = 3.4 # float | Format - ####.###. (optional)
    price4_regupto = 3.4 # float | Format - ####.###. (optional)
    price4_regdown_from = 3.4 # float | Format - ####.###. (optional)
    price4_regdownto = 3.4 # float | Format - ####.###. (optional)
    price4_offline_nonspin_from = 3.4 # float | Format - ####.###. (optional)
    price4_offline_nonspinto = 3.4 # float | Format - ####.###. (optional)
    quantity_mw4_from = 56 # int | Format - ###. (optional)
    quantity_mw4_to = 56 # int | Format - ###. (optional)
    block_indicator5 = 'block_indicator5_example' # str | Format - abc123. (optional)
    price5_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price5_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price5_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price5_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price5_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price5_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price5_online_nonspin_from = 3.4 # float | Format - ####.###. (optional)
    price5_online_nonspinto = 3.4 # float | Format - ####.###. (optional)
    price5_regup = True # bool | Format - true | false. (optional)
    price5_regdown = True # bool | Format - true | false. (optional)
    price5_offline_nonspin = True # bool | Format - true | false. (optional)
    quantity_mw5_from = 56 # int | Format - ###. (optional)
    quantity_mw5_to = 56 # int | Format - ###. (optional)
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    sasmid_from = 'sasmid_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sasmid_to = 'sasmid_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    dme_name = 'dme_name_example' # str | Format - abc123. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day SASM Load Resource AS Offers
        api_response = api_instance.get_data34(ocp_apim_subscription_key, resource_name=resource_name, multi_hour_block_flag=multi_hour_block_flag, block_indicator1=block_indicator1, price1_rrspfr_from=price1_rrspfr_from, price1_rrspfrto=price1_rrspfrto, price1_rrsffr_from=price1_rrsffr_from, price1_rrsffrto=price1_rrsffrto, price1_rrsufr_from=price1_rrsufr_from, price1_rrsufrto=price1_rrsufrto, price1_online_nonspin_from=price1_online_nonspin_from, price1_online_nonspinto=price1_online_nonspinto, price1_regup_from=price1_regup_from, price1_regupto=price1_regupto, price1_regdown_from=price1_regdown_from, price1_regdownto=price1_regdownto, price1_offline_nonspin_from=price1_offline_nonspin_from, price1_offline_nonspinto=price1_offline_nonspinto, quantity_mw1_from=quantity_mw1_from, quantity_mw1_to=quantity_mw1_to, block_indicator2=block_indicator2, price2_rrspfr_from=price2_rrspfr_from, price2_rrspfrto=price2_rrspfrto, price2_rrsffr_from=price2_rrsffr_from, price2_rrsffrto=price2_rrsffrto, price2_rrsufr_from=price2_rrsufr_from, price2_rrsufrto=price2_rrsufrto, price2_online_nonspin_from=price2_online_nonspin_from, price2_online_nonspinto=price2_online_nonspinto, price2_regup_from=price2_regup_from, price2_regupto=price2_regupto, price2_regdown_from=price2_regdown_from, price2_regdownto=price2_regdownto, price2_offline_nonspin_from=price2_offline_nonspin_from, price2_offline_nonspinto=price2_offline_nonspinto, quantity_mw2_from=quantity_mw2_from, quantity_mw2_to=quantity_mw2_to, block_indicator3=block_indicator3, price3_rrspfr_from=price3_rrspfr_from, price3_rrspfrto=price3_rrspfrto, price3_rrsffr_from=price3_rrsffr_from, price3_rrsffrto=price3_rrsffrto, price3_rrsufr_from=price3_rrsufr_from, price3_rrsufrto=price3_rrsufrto, price3_online_nonspin_from=price3_online_nonspin_from, price3_online_nonspinto=price3_online_nonspinto, price3_regup_from=price3_regup_from, price3_regupto=price3_regupto, price3_regdown_from=price3_regdown_from, price3_regdownto=price3_regdownto, price3_offline_nonspin_from=price3_offline_nonspin_from, price3_offline_nonspinto=price3_offline_nonspinto, quantity_mw3_from=quantity_mw3_from, quantity_mw3_to=quantity_mw3_to, block_indicator4=block_indicator4, price4_rrspfr_from=price4_rrspfr_from, price4_rrspfrto=price4_rrspfrto, price4_rrsffr_from=price4_rrsffr_from, price4_rrsffrto=price4_rrsffrto, price4_rrsufr_from=price4_rrsufr_from, price4_rrsufrto=price4_rrsufrto, price4_online_nonspin_from=price4_online_nonspin_from, price4_online_nonspinto=price4_online_nonspinto, price4_regup_from=price4_regup_from, price4_regupto=price4_regupto, price4_regdown_from=price4_regdown_from, price4_regdownto=price4_regdownto, price4_offline_nonspin_from=price4_offline_nonspin_from, price4_offline_nonspinto=price4_offline_nonspinto, quantity_mw4_from=quantity_mw4_from, quantity_mw4_to=quantity_mw4_to, block_indicator5=block_indicator5, price5_rrspfr_from=price5_rrspfr_from, price5_rrspfrto=price5_rrspfrto, price5_rrsffr_from=price5_rrsffr_from, price5_rrsffrto=price5_rrsffrto, price5_rrsufr_from=price5_rrsufr_from, price5_rrsufrto=price5_rrsufrto, price5_online_nonspin_from=price5_online_nonspin_from, price5_online_nonspinto=price5_online_nonspinto, price5_regup=price5_regup, price5_regdown=price5_regdown, price5_offline_nonspin=price5_offline_nonspin, quantity_mw5_from=quantity_mw5_from, quantity_mw5_to=quantity_mw5_to, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, sasmid_from=sasmid_from, sasmid_to=sasmid_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, dme_name=dme_name, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3990EXApi->get_data34:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3990EXApi->get_data34: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **resource_name** | **str**| Format - abc123. | [optional] 
 **multi_hour_block_flag** | **bool**| Format - true | false. | [optional] 
 **block_indicator1** | **str**| Format - abc123. | [optional] 
 **price1_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price1_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price1_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price1_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price1_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price1_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price1_online_nonspin_from** | **float**| Format - ####.###. | [optional] 
 **price1_online_nonspinto** | **float**| Format - ####.###. | [optional] 
 **price1_regup_from** | **float**| Format - ####.###. | [optional] 
 **price1_regupto** | **float**| Format - ####.###. | [optional] 
 **price1_regdown_from** | **float**| Format - ####.###. | [optional] 
 **price1_regdownto** | **float**| Format - ####.###. | [optional] 
 **price1_offline_nonspin_from** | **float**| Format - ####.###. | [optional] 
 **price1_offline_nonspinto** | **float**| Format - ####.###. | [optional] 
 **quantity_mw1_from** | **int**| Format - ###. | [optional] 
 **quantity_mw1_to** | **int**| Format - ###. | [optional] 
 **block_indicator2** | **str**| Format - abc123. | [optional] 
 **price2_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price2_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price2_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price2_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price2_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price2_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price2_online_nonspin_from** | **float**| Format - ####.###. | [optional] 
 **price2_online_nonspinto** | **float**| Format - ####.###. | [optional] 
 **price2_regup_from** | **float**| Format - ####.###. | [optional] 
 **price2_regupto** | **float**| Format - ####.###. | [optional] 
 **price2_regdown_from** | **float**| Format - ####.###. | [optional] 
 **price2_regdownto** | **float**| Format - ####.###. | [optional] 
 **price2_offline_nonspin_from** | **float**| Format - ####.###. | [optional] 
 **price2_offline_nonspinto** | **float**| Format - ####.###. | [optional] 
 **quantity_mw2_from** | **int**| Format - ###. | [optional] 
 **quantity_mw2_to** | **int**| Format - ###. | [optional] 
 **block_indicator3** | **str**| Format - abc123. | [optional] 
 **price3_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price3_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price3_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price3_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price3_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price3_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price3_online_nonspin_from** | **float**| Format - ####.###. | [optional] 
 **price3_online_nonspinto** | **float**| Format - ####.###. | [optional] 
 **price3_regup_from** | **float**| Format - ####.###. | [optional] 
 **price3_regupto** | **float**| Format - ####.###. | [optional] 
 **price3_regdown_from** | **float**| Format - ####.###. | [optional] 
 **price3_regdownto** | **float**| Format - ####.###. | [optional] 
 **price3_offline_nonspin_from** | **float**| Format - ####.###. | [optional] 
 **price3_offline_nonspinto** | **float**| Format - ####.###. | [optional] 
 **quantity_mw3_from** | **int**| Format - ###. | [optional] 
 **quantity_mw3_to** | **int**| Format - ###. | [optional] 
 **block_indicator4** | **str**| Format - abc123. | [optional] 
 **price4_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price4_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price4_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price4_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price4_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price4_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price4_online_nonspin_from** | **float**| Format - ####.###. | [optional] 
 **price4_online_nonspinto** | **float**| Format - ####.###. | [optional] 
 **price4_regup_from** | **float**| Format - ####.###. | [optional] 
 **price4_regupto** | **float**| Format - ####.###. | [optional] 
 **price4_regdown_from** | **float**| Format - ####.###. | [optional] 
 **price4_regdownto** | **float**| Format - ####.###. | [optional] 
 **price4_offline_nonspin_from** | **float**| Format - ####.###. | [optional] 
 **price4_offline_nonspinto** | **float**| Format - ####.###. | [optional] 
 **quantity_mw4_from** | **int**| Format - ###. | [optional] 
 **quantity_mw4_to** | **int**| Format - ###. | [optional] 
 **block_indicator5** | **str**| Format - abc123. | [optional] 
 **price5_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price5_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price5_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price5_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price5_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price5_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price5_online_nonspin_from** | **float**| Format - ####.###. | [optional] 
 **price5_online_nonspinto** | **float**| Format - ####.###. | [optional] 
 **price5_regup** | **bool**| Format - true | false. | [optional] 
 **price5_regdown** | **bool**| Format - true | false. | [optional] 
 **price5_offline_nonspin** | **bool**| Format - true | false. | [optional] 
 **quantity_mw5_from** | **int**| Format - ###. | [optional] 
 **quantity_mw5_to** | **int**| Format - ###. | [optional] 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **sasmid_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sasmid_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **qse_name** | **str**| Format - abc123. | [optional] 
 **dme_name** | **str**| Format - abc123. | [optional] 
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

# **get_data35**
> Report get_data35(ocp_apim_subscription_key, sasmid_from=sasmid_from, sasmid_to=sasmid_to, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, resource_name=resource_name, resource_type=resource_type, regup_aawarded_from=regup_aawarded_from, regup_aawarded_to=regup_aawarded_to, regupmcpc_from=regupmcpc_from, regupmcpcto=regupmcpcto, regdn_awarded_from=regdn_awarded_from, regdn_awarded_to=regdn_awarded_to, regdnmcpc_from=regdnmcpc_from, regdnmcpcto=regdnmcpcto, rrspfr_awarded_from=rrspfr_awarded_from, rrspfr_awarded_to=rrspfr_awarded_to, rrsffr_awarded_from=rrsffr_awarded_from, rrsffr_awarded_to=rrsffr_awarded_to, rrsufr_awarded_from=rrsufr_awarded_from, rrsufr_awarded_to=rrsufr_awarded_to, rrsmcpc_from=rrsmcpc_from, rrsmcpcto=rrsmcpcto, nspin_awarded_from=nspin_awarded_from, nspin_awarded_to=nspin_awarded_to, nspinmcpc_from=nspinmcpc_from, nspinmcpcto=nspinmcpcto, page=page, size=size, sort=sort, dir=dir)

60 Day SASM Load Resource AS Offer Awards

60 Day SASM Load Resource AS Offer Awards

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
    api_instance = openapi_client.NP3990EXApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sasmid_from = 'sasmid_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sasmid_to = 'sasmid_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    resource_name = 'resource_name_example' # str | Format - abc123. (optional)
    resource_type = 'resource_type_example' # str | Format - abc123. (optional)
    regup_aawarded_from = 3.4 # float | Format - ####.###. (optional)
    regup_aawarded_to = 3.4 # float | Format - ####.###. (optional)
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
        # 60 Day SASM Load Resource AS Offer Awards
        api_response = api_instance.get_data35(ocp_apim_subscription_key, sasmid_from=sasmid_from, sasmid_to=sasmid_to, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, resource_name=resource_name, resource_type=resource_type, regup_aawarded_from=regup_aawarded_from, regup_aawarded_to=regup_aawarded_to, regupmcpc_from=regupmcpc_from, regupmcpcto=regupmcpcto, regdn_awarded_from=regdn_awarded_from, regdn_awarded_to=regdn_awarded_to, regdnmcpc_from=regdnmcpc_from, regdnmcpcto=regdnmcpcto, rrspfr_awarded_from=rrspfr_awarded_from, rrspfr_awarded_to=rrspfr_awarded_to, rrsffr_awarded_from=rrsffr_awarded_from, rrsffr_awarded_to=rrsffr_awarded_to, rrsufr_awarded_from=rrsufr_awarded_from, rrsufr_awarded_to=rrsufr_awarded_to, rrsmcpc_from=rrsmcpc_from, rrsmcpcto=rrsmcpcto, nspin_awarded_from=nspin_awarded_from, nspin_awarded_to=nspin_awarded_to, nspinmcpc_from=nspinmcpc_from, nspinmcpcto=nspinmcpcto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3990EXApi->get_data35:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3990EXApi->get_data35: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sasmid_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sasmid_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **resource_name** | **str**| Format - abc123. | [optional] 
 **resource_type** | **str**| Format - abc123. | [optional] 
 **regup_aawarded_from** | **float**| Format - ####.###. | [optional] 
 **regup_aawarded_to** | **float**| Format - ####.###. | [optional] 
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

# **get_data36**
> Report get_data36(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, sasmid_from=sasmid_from, sasmid_to=sasmid_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, dme_name=dme_name, resource_name=resource_name, multi_hour_block_flag=multi_hour_block_flag, block_indicator1=block_indicator1, price1_rrspfr_from=price1_rrspfr_from, price1_rrspfrto=price1_rrspfrto, price1_rrsffr_from=price1_rrsffr_from, price1_rrsffrto=price1_rrsffrto, price1_rrsufr_from=price1_rrsufr_from, price1_rrsufrto=price1_rrsufrto, price1_online_nonspin_from=price1_online_nonspin_from, price1_online_nonspinto=price1_online_nonspinto, price1_regup_from=price1_regup_from, price1_regupto=price1_regupto, price1_regdown_from=price1_regdown_from, price1_regdownto=price1_regdownto, price1_offline_nonspin_from=price1_offline_nonspin_from, price1_offline_nonspinto=price1_offline_nonspinto, quantity_mw1_from=quantity_mw1_from, quantity_mw1_to=quantity_mw1_to, block_indicator2=block_indicator2, price2_rrspfr_from=price2_rrspfr_from, price2_rrspfrto=price2_rrspfrto, price2_rrsffr_from=price2_rrsffr_from, price2_rrsffrto=price2_rrsffrto, price2_rrsufr_from=price2_rrsufr_from, price2_rrsufrto=price2_rrsufrto, price2_online_nonspin_from=price2_online_nonspin_from, price2_online_nonspinto=price2_online_nonspinto, price2_regup_from=price2_regup_from, price2_regupto=price2_regupto, price2_regdown_from=price2_regdown_from, price2_regdownto=price2_regdownto, price2_offline_nonspin_from=price2_offline_nonspin_from, price2_offline_nonspinto=price2_offline_nonspinto, quantity_mw2_from=quantity_mw2_from, quantity_mw2_to=quantity_mw2_to, block_indicator3=block_indicator3, price3_rrspfr_from=price3_rrspfr_from, price3_rrspfrto=price3_rrspfrto, price3_rrsffr_from=price3_rrsffr_from, price3_rrsffrto=price3_rrsffrto, price3_rrsufr_from=price3_rrsufr_from, price3_rrsufrto=price3_rrsufrto, price3_online_nonspin_from=price3_online_nonspin_from, price3_online_nonspinto=price3_online_nonspinto, price3_regup_from=price3_regup_from, price3_regupto=price3_regupto, price3_regdown_from=price3_regdown_from, price3_regdownto=price3_regdownto, price3_offline_nonspin_from=price3_offline_nonspin_from, price3_offline_nonspinto=price3_offline_nonspinto, quantity_mw3_from=quantity_mw3_from, quantity_mw3_to=quantity_mw3_to, block_indicator4=block_indicator4, price4_rrspfr_from=price4_rrspfr_from, price4_rrspfrto=price4_rrspfrto, price4_rrsffr_from=price4_rrsffr_from, price4_rrsffrto=price4_rrsffrto, price4_rrsufr_from=price4_rrsufr_from, price4_rrsufrto=price4_rrsufrto, price4_online_nonspin_from=price4_online_nonspin_from, price4_online_nonspinto=price4_online_nonspinto, price4_regup_from=price4_regup_from, price4_regupto=price4_regupto, price4_regdown_from=price4_regdown_from, price4_regdownto=price4_regdownto, price4_offline_nonspin_from=price4_offline_nonspin_from, price4_offline_nonspinto=price4_offline_nonspinto, quantity_mw4_from=quantity_mw4_from, quantity_mw4_to=quantity_mw4_to, block_indicator5=block_indicator5, price5_rrspfr_from=price5_rrspfr_from, price5_rrspfrto=price5_rrspfrto, price5_rrsffr_from=price5_rrsffr_from, price5_rrsffrto=price5_rrsffrto, price5_rrsufr_from=price5_rrsufr_from, price5_rrsufrto=price5_rrsufrto, price5_online_nonspin_from=price5_online_nonspin_from, price5_online_nonspinto=price5_online_nonspinto, price5_regup=price5_regup, price5_regdown=price5_regdown, price5_offline_nonspin=price5_offline_nonspin, quantity_mw5_from=quantity_mw5_from, quantity_mw5_to=quantity_mw5_to, page=page, size=size, sort=sort, dir=dir)

60 Day SASM Generation Resource AS Offers

60 Day SASM Generation Resource AS Offers

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
    api_instance = openapi_client.NP3990EXApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    sasmid_from = 'sasmid_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sasmid_to = 'sasmid_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    qse_name = 'qse_name_example' # str | Format - abc123. (optional)
    dme_name = 'dme_name_example' # str | Format - abc123. (optional)
    resource_name = 'resource_name_example' # str | Format - abc123. (optional)
    multi_hour_block_flag = True # bool | Format - true | false. (optional)
    block_indicator1 = 'block_indicator1_example' # str | Format - abc123. (optional)
    price1_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price1_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price1_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price1_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price1_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price1_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price1_online_nonspin_from = 3.4 # float | Format - ####.###. (optional)
    price1_online_nonspinto = 3.4 # float | Format - ####.###. (optional)
    price1_regup_from = 3.4 # float | Format - ####.###. (optional)
    price1_regupto = 3.4 # float | Format - ####.###. (optional)
    price1_regdown_from = 3.4 # float | Format - ####.###. (optional)
    price1_regdownto = 3.4 # float | Format - ####.###. (optional)
    price1_offline_nonspin_from = 3.4 # float | Format - ####.###. (optional)
    price1_offline_nonspinto = 3.4 # float | Format - ####.###. (optional)
    quantity_mw1_from = 56 # int | Format - ###. (optional)
    quantity_mw1_to = 56 # int | Format - ###. (optional)
    block_indicator2 = 'block_indicator2_example' # str | Format - abc123. (optional)
    price2_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price2_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price2_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price2_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price2_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price2_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price2_online_nonspin_from = 3.4 # float | Format - ####.###. (optional)
    price2_online_nonspinto = 3.4 # float | Format - ####.###. (optional)
    price2_regup_from = 3.4 # float | Format - ####.###. (optional)
    price2_regupto = 3.4 # float | Format - ####.###. (optional)
    price2_regdown_from = 3.4 # float | Format - ####.###. (optional)
    price2_regdownto = 3.4 # float | Format - ####.###. (optional)
    price2_offline_nonspin_from = 3.4 # float | Format - ####.###. (optional)
    price2_offline_nonspinto = 3.4 # float | Format - ####.###. (optional)
    quantity_mw2_from = 56 # int | Format - ###. (optional)
    quantity_mw2_to = 56 # int | Format - ###. (optional)
    block_indicator3 = 'block_indicator3_example' # str | Format - abc123. (optional)
    price3_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price3_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price3_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price3_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price3_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price3_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price3_online_nonspin_from = 3.4 # float | Format - ####.###. (optional)
    price3_online_nonspinto = 3.4 # float | Format - ####.###. (optional)
    price3_regup_from = 3.4 # float | Format - ####.###. (optional)
    price3_regupto = 3.4 # float | Format - ####.###. (optional)
    price3_regdown_from = 3.4 # float | Format - ####.###. (optional)
    price3_regdownto = 3.4 # float | Format - ####.###. (optional)
    price3_offline_nonspin_from = 3.4 # float | Format - ####.###. (optional)
    price3_offline_nonspinto = 3.4 # float | Format - ####.###. (optional)
    quantity_mw3_from = 56 # int | Format - ###. (optional)
    quantity_mw3_to = 56 # int | Format - ###. (optional)
    block_indicator4 = 'block_indicator4_example' # str | Format - abc123. (optional)
    price4_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price4_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price4_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price4_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price4_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price4_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price4_online_nonspin_from = 3.4 # float | Format - ####.###. (optional)
    price4_online_nonspinto = 3.4 # float | Format - ####.###. (optional)
    price4_regup_from = 3.4 # float | Format - ####.###. (optional)
    price4_regupto = 3.4 # float | Format - ####.###. (optional)
    price4_regdown_from = 3.4 # float | Format - ####.###. (optional)
    price4_regdownto = 3.4 # float | Format - ####.###. (optional)
    price4_offline_nonspin_from = 3.4 # float | Format - ####.###. (optional)
    price4_offline_nonspinto = 3.4 # float | Format - ####.###. (optional)
    quantity_mw4_from = 56 # int | Format - ###. (optional)
    quantity_mw4_to = 56 # int | Format - ###. (optional)
    block_indicator5 = 'block_indicator5_example' # str | Format - abc123. (optional)
    price5_rrspfr_from = 3.4 # float | Format - ####.###. (optional)
    price5_rrspfrto = 3.4 # float | Format - ####.###. (optional)
    price5_rrsffr_from = 3.4 # float | Format - ####.###. (optional)
    price5_rrsffrto = 3.4 # float | Format - ####.###. (optional)
    price5_rrsufr_from = 3.4 # float | Format - ####.###. (optional)
    price5_rrsufrto = 3.4 # float | Format - ####.###. (optional)
    price5_online_nonspin_from = 3.4 # float | Format - ####.###. (optional)
    price5_online_nonspinto = 3.4 # float | Format - ####.###. (optional)
    price5_regup = True # bool | Format - true | false. (optional)
    price5_regdown = True # bool | Format - true | false. (optional)
    price5_offline_nonspin = True # bool | Format - true | false. (optional)
    quantity_mw5_from = 56 # int | Format - ###. (optional)
    quantity_mw5_to = 56 # int | Format - ###. (optional)
    page = 56 # int | Format - ###. Page number of returned values in the collection. (optional)
    size = 56 # int | Format - ###. Number of returned items per page. (optional)
    sort = 'sort_example' # str | Format - abc123. Defines field by which to sort the returned resource values. (optional)
    dir = 'dir_example' # str | Format - abc123. Defines sort order of returned values based on the primary business key of the resource. (optional)

    try:
        # 60 Day SASM Generation Resource AS Offers
        api_response = api_instance.get_data36(ocp_apim_subscription_key, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, sasmid_from=sasmid_from, sasmid_to=sasmid_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, qse_name=qse_name, dme_name=dme_name, resource_name=resource_name, multi_hour_block_flag=multi_hour_block_flag, block_indicator1=block_indicator1, price1_rrspfr_from=price1_rrspfr_from, price1_rrspfrto=price1_rrspfrto, price1_rrsffr_from=price1_rrsffr_from, price1_rrsffrto=price1_rrsffrto, price1_rrsufr_from=price1_rrsufr_from, price1_rrsufrto=price1_rrsufrto, price1_online_nonspin_from=price1_online_nonspin_from, price1_online_nonspinto=price1_online_nonspinto, price1_regup_from=price1_regup_from, price1_regupto=price1_regupto, price1_regdown_from=price1_regdown_from, price1_regdownto=price1_regdownto, price1_offline_nonspin_from=price1_offline_nonspin_from, price1_offline_nonspinto=price1_offline_nonspinto, quantity_mw1_from=quantity_mw1_from, quantity_mw1_to=quantity_mw1_to, block_indicator2=block_indicator2, price2_rrspfr_from=price2_rrspfr_from, price2_rrspfrto=price2_rrspfrto, price2_rrsffr_from=price2_rrsffr_from, price2_rrsffrto=price2_rrsffrto, price2_rrsufr_from=price2_rrsufr_from, price2_rrsufrto=price2_rrsufrto, price2_online_nonspin_from=price2_online_nonspin_from, price2_online_nonspinto=price2_online_nonspinto, price2_regup_from=price2_regup_from, price2_regupto=price2_regupto, price2_regdown_from=price2_regdown_from, price2_regdownto=price2_regdownto, price2_offline_nonspin_from=price2_offline_nonspin_from, price2_offline_nonspinto=price2_offline_nonspinto, quantity_mw2_from=quantity_mw2_from, quantity_mw2_to=quantity_mw2_to, block_indicator3=block_indicator3, price3_rrspfr_from=price3_rrspfr_from, price3_rrspfrto=price3_rrspfrto, price3_rrsffr_from=price3_rrsffr_from, price3_rrsffrto=price3_rrsffrto, price3_rrsufr_from=price3_rrsufr_from, price3_rrsufrto=price3_rrsufrto, price3_online_nonspin_from=price3_online_nonspin_from, price3_online_nonspinto=price3_online_nonspinto, price3_regup_from=price3_regup_from, price3_regupto=price3_regupto, price3_regdown_from=price3_regdown_from, price3_regdownto=price3_regdownto, price3_offline_nonspin_from=price3_offline_nonspin_from, price3_offline_nonspinto=price3_offline_nonspinto, quantity_mw3_from=quantity_mw3_from, quantity_mw3_to=quantity_mw3_to, block_indicator4=block_indicator4, price4_rrspfr_from=price4_rrspfr_from, price4_rrspfrto=price4_rrspfrto, price4_rrsffr_from=price4_rrsffr_from, price4_rrsffrto=price4_rrsffrto, price4_rrsufr_from=price4_rrsufr_from, price4_rrsufrto=price4_rrsufrto, price4_online_nonspin_from=price4_online_nonspin_from, price4_online_nonspinto=price4_online_nonspinto, price4_regup_from=price4_regup_from, price4_regupto=price4_regupto, price4_regdown_from=price4_regdown_from, price4_regdownto=price4_regdownto, price4_offline_nonspin_from=price4_offline_nonspin_from, price4_offline_nonspinto=price4_offline_nonspinto, quantity_mw4_from=quantity_mw4_from, quantity_mw4_to=quantity_mw4_to, block_indicator5=block_indicator5, price5_rrspfr_from=price5_rrspfr_from, price5_rrspfrto=price5_rrspfrto, price5_rrsffr_from=price5_rrsffr_from, price5_rrsffrto=price5_rrsffrto, price5_rrsufr_from=price5_rrsufr_from, price5_rrsufrto=price5_rrsufrto, price5_online_nonspin_from=price5_online_nonspin_from, price5_online_nonspinto=price5_online_nonspinto, price5_regup=price5_regup, price5_regdown=price5_regdown, price5_offline_nonspin=price5_offline_nonspin, quantity_mw5_from=quantity_mw5_from, quantity_mw5_to=quantity_mw5_to, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3990EXApi->get_data36:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3990EXApi->get_data36: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **sasmid_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sasmid_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **qse_name** | **str**| Format - abc123. | [optional] 
 **dme_name** | **str**| Format - abc123. | [optional] 
 **resource_name** | **str**| Format - abc123. | [optional] 
 **multi_hour_block_flag** | **bool**| Format - true | false. | [optional] 
 **block_indicator1** | **str**| Format - abc123. | [optional] 
 **price1_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price1_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price1_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price1_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price1_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price1_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price1_online_nonspin_from** | **float**| Format - ####.###. | [optional] 
 **price1_online_nonspinto** | **float**| Format - ####.###. | [optional] 
 **price1_regup_from** | **float**| Format - ####.###. | [optional] 
 **price1_regupto** | **float**| Format - ####.###. | [optional] 
 **price1_regdown_from** | **float**| Format - ####.###. | [optional] 
 **price1_regdownto** | **float**| Format - ####.###. | [optional] 
 **price1_offline_nonspin_from** | **float**| Format - ####.###. | [optional] 
 **price1_offline_nonspinto** | **float**| Format - ####.###. | [optional] 
 **quantity_mw1_from** | **int**| Format - ###. | [optional] 
 **quantity_mw1_to** | **int**| Format - ###. | [optional] 
 **block_indicator2** | **str**| Format - abc123. | [optional] 
 **price2_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price2_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price2_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price2_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price2_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price2_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price2_online_nonspin_from** | **float**| Format - ####.###. | [optional] 
 **price2_online_nonspinto** | **float**| Format - ####.###. | [optional] 
 **price2_regup_from** | **float**| Format - ####.###. | [optional] 
 **price2_regupto** | **float**| Format - ####.###. | [optional] 
 **price2_regdown_from** | **float**| Format - ####.###. | [optional] 
 **price2_regdownto** | **float**| Format - ####.###. | [optional] 
 **price2_offline_nonspin_from** | **float**| Format - ####.###. | [optional] 
 **price2_offline_nonspinto** | **float**| Format - ####.###. | [optional] 
 **quantity_mw2_from** | **int**| Format - ###. | [optional] 
 **quantity_mw2_to** | **int**| Format - ###. | [optional] 
 **block_indicator3** | **str**| Format - abc123. | [optional] 
 **price3_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price3_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price3_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price3_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price3_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price3_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price3_online_nonspin_from** | **float**| Format - ####.###. | [optional] 
 **price3_online_nonspinto** | **float**| Format - ####.###. | [optional] 
 **price3_regup_from** | **float**| Format - ####.###. | [optional] 
 **price3_regupto** | **float**| Format - ####.###. | [optional] 
 **price3_regdown_from** | **float**| Format - ####.###. | [optional] 
 **price3_regdownto** | **float**| Format - ####.###. | [optional] 
 **price3_offline_nonspin_from** | **float**| Format - ####.###. | [optional] 
 **price3_offline_nonspinto** | **float**| Format - ####.###. | [optional] 
 **quantity_mw3_from** | **int**| Format - ###. | [optional] 
 **quantity_mw3_to** | **int**| Format - ###. | [optional] 
 **block_indicator4** | **str**| Format - abc123. | [optional] 
 **price4_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price4_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price4_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price4_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price4_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price4_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price4_online_nonspin_from** | **float**| Format - ####.###. | [optional] 
 **price4_online_nonspinto** | **float**| Format - ####.###. | [optional] 
 **price4_regup_from** | **float**| Format - ####.###. | [optional] 
 **price4_regupto** | **float**| Format - ####.###. | [optional] 
 **price4_regdown_from** | **float**| Format - ####.###. | [optional] 
 **price4_regdownto** | **float**| Format - ####.###. | [optional] 
 **price4_offline_nonspin_from** | **float**| Format - ####.###. | [optional] 
 **price4_offline_nonspinto** | **float**| Format - ####.###. | [optional] 
 **quantity_mw4_from** | **int**| Format - ###. | [optional] 
 **quantity_mw4_to** | **int**| Format - ###. | [optional] 
 **block_indicator5** | **str**| Format - abc123. | [optional] 
 **price5_rrspfr_from** | **float**| Format - ####.###. | [optional] 
 **price5_rrspfrto** | **float**| Format - ####.###. | [optional] 
 **price5_rrsffr_from** | **float**| Format - ####.###. | [optional] 
 **price5_rrsffrto** | **float**| Format - ####.###. | [optional] 
 **price5_rrsufr_from** | **float**| Format - ####.###. | [optional] 
 **price5_rrsufrto** | **float**| Format - ####.###. | [optional] 
 **price5_online_nonspin_from** | **float**| Format - ####.###. | [optional] 
 **price5_online_nonspinto** | **float**| Format - ####.###. | [optional] 
 **price5_regup** | **bool**| Format - true | false. | [optional] 
 **price5_regdown** | **bool**| Format - true | false. | [optional] 
 **price5_offline_nonspin** | **bool**| Format - true | false. | [optional] 
 **quantity_mw5_from** | **int**| Format - ###. | [optional] 
 **quantity_mw5_to** | **int**| Format - ###. | [optional] 
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

# **get_data37**
> Report get_data37(ocp_apim_subscription_key, sasmid_from=sasmid_from, sasmid_to=sasmid_to, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, resource_name=resource_name, resource_type=resource_type, regup_aawarded_from=regup_aawarded_from, regup_aawarded_to=regup_aawarded_to, regupmcpc_from=regupmcpc_from, regupmcpcto=regupmcpcto, regdn_awarded_from=regdn_awarded_from, regdn_awarded_to=regdn_awarded_to, regdnmcpc_from=regdnmcpc_from, regdnmcpcto=regdnmcpcto, rrspfr_awarded_from=rrspfr_awarded_from, rrspfr_awarded_to=rrspfr_awarded_to, rrsffr_awarded_from=rrsffr_awarded_from, rrsffr_awarded_to=rrsffr_awarded_to, rrsufr_awarded_from=rrsufr_awarded_from, rrsufr_awarded_to=rrsufr_awarded_to, rrsmcpc_from=rrsmcpc_from, rrsmcpcto=rrsmcpcto, nspin_awarded_from=nspin_awarded_from, nspin_awarded_to=nspin_awarded_to, nspinmcpc_from=nspinmcpc_from, nspinmcpcto=nspinmcpcto, page=page, size=size, sort=sort, dir=dir)

60 Day SASM Generation Resource AS Offer Awards

60 Day SASM Generation Resource AS Offer Awards

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
    api_instance = openapi_client.NP3990EXApi(api_client)
    ocp_apim_subscription_key = '90796ffc22254fa89ad8400d996c992f' # str | The subscription key assigned to your ERCOT Public API account.
    sasmid_from = 'sasmid_from_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    sasmid_to = 'sasmid_to_example' # str | Format - yyyy-MM-ddTH24:mm:ss. (optional)
    delivery_date_from = 'delivery_date_from_example' # str | Format - yyyy-MM-dd. (optional)
    delivery_date_to = 'delivery_date_to_example' # str | Format - yyyy-MM-dd. (optional)
    hour_ending_from = 56 # int | Format - ###. (optional)
    hour_ending_to = 56 # int | Format - ###. (optional)
    resource_name = 'resource_name_example' # str | Format - abc123. (optional)
    resource_type = 'resource_type_example' # str | Format - abc123. (optional)
    regup_aawarded_from = 3.4 # float | Format - ####.###. (optional)
    regup_aawarded_to = 3.4 # float | Format - ####.###. (optional)
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
        # 60 Day SASM Generation Resource AS Offer Awards
        api_response = api_instance.get_data37(ocp_apim_subscription_key, sasmid_from=sasmid_from, sasmid_to=sasmid_to, delivery_date_from=delivery_date_from, delivery_date_to=delivery_date_to, hour_ending_from=hour_ending_from, hour_ending_to=hour_ending_to, resource_name=resource_name, resource_type=resource_type, regup_aawarded_from=regup_aawarded_from, regup_aawarded_to=regup_aawarded_to, regupmcpc_from=regupmcpc_from, regupmcpcto=regupmcpcto, regdn_awarded_from=regdn_awarded_from, regdn_awarded_to=regdn_awarded_to, regdnmcpc_from=regdnmcpc_from, regdnmcpcto=regdnmcpcto, rrspfr_awarded_from=rrspfr_awarded_from, rrspfr_awarded_to=rrspfr_awarded_to, rrsffr_awarded_from=rrsffr_awarded_from, rrsffr_awarded_to=rrsffr_awarded_to, rrsufr_awarded_from=rrsufr_awarded_from, rrsufr_awarded_to=rrsufr_awarded_to, rrsmcpc_from=rrsmcpc_from, rrsmcpcto=rrsmcpcto, nspin_awarded_from=nspin_awarded_from, nspin_awarded_to=nspin_awarded_to, nspinmcpc_from=nspinmcpc_from, nspinmcpcto=nspinmcpcto, page=page, size=size, sort=sort, dir=dir)
        print("The response of NP3990EXApi->get_data37:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NP3990EXApi->get_data37: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ocp_apim_subscription_key** | **str**| The subscription key assigned to your ERCOT Public API account. | 
 **sasmid_from** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **sasmid_to** | **str**| Format - yyyy-MM-ddTH24:mm:ss. | [optional] 
 **delivery_date_from** | **str**| Format - yyyy-MM-dd. | [optional] 
 **delivery_date_to** | **str**| Format - yyyy-MM-dd. | [optional] 
 **hour_ending_from** | **int**| Format - ###. | [optional] 
 **hour_ending_to** | **int**| Format - ###. | [optional] 
 **resource_name** | **str**| Format - abc123. | [optional] 
 **resource_type** | **str**| Format - abc123. | [optional] 
 **regup_aawarded_from** | **float**| Format - ####.###. | [optional] 
 **regup_aawarded_to** | **float**| Format - ####.###. | [optional] 
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

