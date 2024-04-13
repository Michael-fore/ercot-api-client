# ProductHistory

Each archive represents a single EMIL Product archive (zip file).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta** | [**ResultMetadata**](ResultMetadata.md) |  | [optional] 
**product** | [**ProductHistoryMetadata**](ProductHistoryMetadata.md) |  | [optional] 
**archives** | [**List[Archive]**](Archive.md) |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from openapi_client.models.product_history import ProductHistory

# TODO update the JSON string below
json = "{}"
# create an instance of ProductHistory from a JSON string
product_history_instance = ProductHistory.from_json(json)
# print the JSON string representation of the object
print(ProductHistory.to_json())

# convert the object into a dict
product_history_dict = product_history_instance.to_dict()
# create an instance of ProductHistory from a dict
product_history_form_dict = product_history.from_dict(product_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


