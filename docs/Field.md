# Field

Represents report data field.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**label** | **str** |  | [optional] 
**cardinality** | **int** |  | [optional] 
**data_type** | **str** |  | [optional] 
**searchable** | **bool** |  | [optional] 
**sortable** | **bool** |  | [optional] 
**has_range** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.field import Field

# TODO update the JSON string below
json = "{}"
# create an instance of Field from a JSON string
field_instance = Field.from_json(json)
# print the JSON string representation of the object
print(Field.to_json())

# convert the object into a dict
field_dict = field_instance.to_dict()
# create an instance of Field from a dict
field_form_dict = field.from_dict(field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


