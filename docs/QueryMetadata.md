# QueryMetadata

Represents query parameter summary for the specified query results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parameter_count** | **int** |  | [optional] 
**parameters** | **Dict[str, object]** |  | [optional] 
**sorted_by** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.query_metadata import QueryMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of QueryMetadata from a JSON string
query_metadata_instance = QueryMetadata.from_json(json)
# print the JSON string representation of the object
print(QueryMetadata.to_json())

# convert the object into a dict
query_metadata_dict = query_metadata_instance.to_dict()
# create an instance of QueryMetadata from a dict
query_metadata_form_dict = query_metadata.from_dict(query_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


