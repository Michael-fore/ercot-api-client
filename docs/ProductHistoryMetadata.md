# ProductHistoryMetadata

Represents record and paging summary for the specified query results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_records** | **int** |  | [optional] 
**page_size** | **int** |  | [optional] 
**total_pages** | **int** |  | [optional] 
**current_page** | **int** |  | [optional] 
**query** | [**QueryMetadata**](QueryMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.product_history_metadata import ProductHistoryMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ProductHistoryMetadata from a JSON string
product_history_metadata_instance = ProductHistoryMetadata.from_json(json)
# print the JSON string representation of the object
print(ProductHistoryMetadata.to_json())

# convert the object into a dict
product_history_metadata_dict = product_history_metadata_instance.to_dict()
# create an instance of ProductHistoryMetadata from a dict
product_history_metadata_form_dict = product_history_metadata.from_dict(product_history_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


