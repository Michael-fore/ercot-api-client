# Archive

Represents an EMIL Product archive file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_id** | **int** |  | [optional] 
**friendly_name** | **str** |  | [optional] 
**post_datetime** | **datetime** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from openapi_client.models.archive import Archive

# TODO update the JSON string below
json = "{}"
# create an instance of Archive from a JSON string
archive_instance = Archive.from_json(json)
# print the JSON string representation of the object
print(Archive.to_json())

# convert the object into a dict
archive_dict = archive_instance.to_dict()
# create an instance of Archive from a dict
archive_form_dict = archive.from_dict(archive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


