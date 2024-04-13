# ResultMetadata

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
from openapi_client.models.result_metadata import ResultMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ResultMetadata from a JSON string
result_metadata_instance = ResultMetadata.from_json(json)
# print the JSON string representation of the object
print(ResultMetadata.to_json())

# convert the object into a dict
result_metadata_dict = result_metadata_instance.to_dict()
# create an instance of ResultMetadata from a dict
result_metadata_form_dict = result_metadata.from_dict(result_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


