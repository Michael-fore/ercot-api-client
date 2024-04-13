# ReportMetadata

Represents metadata for the specified object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**report_name** | **str** |  | [optional] 
**report_display_name** | **str** |  | [optional] 
**report_id** | **str** |  | [optional] 
**report_emil** | **str** |  | [optional] 
**download_limit** | **int** |  | [optional] 
**default_filter** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.report_metadata import ReportMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ReportMetadata from a JSON string
report_metadata_instance = ReportMetadata.from_json(json)
# print the JSON string representation of the object
print(ReportMetadata.to_json())

# convert the object into a dict
report_metadata_dict = report_metadata_instance.to_dict()
# create an instance of ReportMetadata from a dict
report_metadata_form_dict = report_metadata.from_dict(report_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


