# Product

Represents an EMIL Product, which includes its metadata along with all Artifact information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**emil_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**report_type_id** | **int** |  | [optional] 
**audience** | **str** |  | [optional] 
**generation_frequency** | **str** |  | [optional] 
**security_classification** | **str** |  | [optional] 
**last_updated** | **datetime** |  | [optional] 
**first_run** | **datetime** |  | [optional] 
**eceii** | **str** |  | [optional] 
**channel** | **str** |  | [optional] 
**user_guide** | **str** |  | [optional] 
**posting_type** | **str** |  | [optional] 
**market** | **str** |  | [optional] 
**extract_subscriber** | **str** |  | [optional] 
**xsd_name** | **str** |  | [optional] 
**mis_posting_location** | **str** |  | [optional] 
**certificate_role** | **str** |  | [optional] 
**file_type** | **str** |  | [optional] 
**ddl_name** | **str** |  | [optional] 
**mis_display_duration** | **int** |  | [optional] 
**archive_duration** | **int** |  | [optional] 
**notification_type** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**download_limit** | **int** |  | [optional] 
**last_post_datetime** | **datetime** |  | [optional] 
**protocol_rules** | **Dict[str, str]** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**artifacts** | [**List[Artifact]**](Artifact.md) |  | [optional] 

## Example

```python
from openapi_client.models.product import Product

# TODO update the JSON string below
json = "{}"
# create an instance of Product from a JSON string
product_instance = Product.from_json(json)
# print the JSON string representation of the object
print(Product.to_json())

# convert the object into a dict
product_dict = product_instance.to_dict()
# create an instance of Product from a dict
product_form_dict = product.from_dict(product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


