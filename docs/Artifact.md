# Artifact

Each artifact represents a single report for the given time period designated by the EMIL metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_type_id** | **int** |  | [optional] 
**display_name** | **str** |  | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from openapi_client.models.artifact import Artifact

# TODO update the JSON string below
json = "{}"
# create an instance of Artifact from a JSON string
artifact_instance = Artifact.from_json(json)
# print the JSON string representation of the object
print(Artifact.to_json())

# convert the object into a dict
artifact_dict = artifact_instance.to_dict()
# create an instance of Artifact from a dict
artifact_form_dict = artifact.from_dict(artifact_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


