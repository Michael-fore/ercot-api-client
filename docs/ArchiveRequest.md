# ArchiveRequest

Represents a multi-document download request in JSON format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_ids** | **List[int]** |  | 

## Example

```python
from openapi_client.models.archive_request import ArchiveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveRequest from a JSON string
archive_request_instance = ArchiveRequest.from_json(json)
# print the JSON string representation of the object
print(ArchiveRequest.to_json())

# convert the object into a dict
archive_request_dict = archive_request_instance.to_dict()
# create an instance of ArchiveRequest from a dict
archive_request_form_dict = archive_request.from_dict(archive_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


