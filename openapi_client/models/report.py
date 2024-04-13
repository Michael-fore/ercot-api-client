# coding: utf-8

"""
    ERCOT Public API Client/Developer Documentation

    Client/Developer RESTFul web services documentation for ERCOT Market Information List (EMIL) products.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.field import Field
from openapi_client.models.link import Link
from openapi_client.models.report_metadata import ReportMetadata
from openapi_client.models.result_metadata import ResultMetadata
from typing import Optional, Set
from typing_extensions import Self

class Report(BaseModel):
    """
    Represents report data search results from any EMIL artifact report query.
    """ # noqa: E501
    meta: Optional[ResultMetadata] = Field(default=None, alias="_meta")
    report: Optional[ReportMetadata] = None
    fields: Optional[List[Field]] = None
    data: Optional[Dict[str, Any]] = None
    links: Optional[List[Link]] = None
    __properties: ClassVar[List[str]] = ["_meta", "report", "fields", "data", "links"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Report from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of meta
        if self.meta:
            _dict['_meta'] = self.meta.to_dict()
        # override the default output from pydantic by calling `to_dict()` of report
        if self.report:
            _dict['report'] = self.report.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in fields (list)
        _items = []
        if self.fields:
            for _item in self.fields:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fields'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Report from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "_meta": ResultMetadata.from_dict(obj["_meta"]) if obj.get("_meta") is not None else None,
            "report": ReportMetadata.from_dict(obj["report"]) if obj.get("report") is not None else None,
            "fields": [Field.from_dict(_item) for _item in obj["fields"]] if obj.get("fields") is not None else None,
            "data": obj.get("data"),
            "links": [Link.from_dict(_item) for _item in obj["links"]] if obj.get("links") is not None else None
        })
        return _obj


