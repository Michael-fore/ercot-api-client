# coding: utf-8

"""
    ERCOT Public API Client/Developer Documentation

    Client/Developer RESTFul web services documentation for ERCOT Market Information List (EMIL) products.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Optional, Union
from typing_extensions import Annotated
from openapi_client.models.report import Report

from openapi_client.api_client import ApiClient, RequestSerialized
from openapi_client.api_response import ApiResponse
from openapi_client.rest import RESTResponseType


class NP6787CDApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_data4(
        self,
        ocp_apim_subscription_key: Annotated[StrictStr, Field(description="The subscription key assigned to your ERCOT Public API account.")],
        sced_timestamp_from: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-ddTH24:mm:ss.")] = None,
        sced_timestamp_to: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-ddTH24:mm:ss.")] = None,
        repeat_hour_flag: Annotated[Optional[StrictBool], Field(description="Format - true | false.")] = None,
        electrical_bus: Annotated[Optional[StrictStr], Field(description="Format - abc123.")] = None,
        lmp_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        lmpto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Format - ###. Page number of returned values in the collection.")] = None,
        size: Annotated[Optional[StrictInt], Field(description="Format - ###. Number of returned items per page.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Format - abc123. Defines field by which to sort the returned resource values.")] = None,
        dir: Annotated[Optional[StrictStr], Field(description="Format - abc123. Defines sort order of returned values based on the primary business key of the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Report:
        """LMP by Electrical Bus

        LMP by Electrical Bus

        :param ocp_apim_subscription_key: The subscription key assigned to your ERCOT Public API account. (required)
        :type ocp_apim_subscription_key: str
        :param sced_timestamp_from: Format - yyyy-MM-ddTH24:mm:ss.
        :type sced_timestamp_from: str
        :param sced_timestamp_to: Format - yyyy-MM-ddTH24:mm:ss.
        :type sced_timestamp_to: str
        :param repeat_hour_flag: Format - true | false.
        :type repeat_hour_flag: bool
        :param electrical_bus: Format - abc123.
        :type electrical_bus: str
        :param lmp_from: Format - ####.###.
        :type lmp_from: float
        :param lmpto: Format - ####.###.
        :type lmpto: float
        :param page: Format - ###. Page number of returned values in the collection.
        :type page: int
        :param size: Format - ###. Number of returned items per page.
        :type size: int
        :param sort: Format - abc123. Defines field by which to sort the returned resource values.
        :type sort: str
        :param dir: Format - abc123. Defines sort order of returned values based on the primary business key of the resource.
        :type dir: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_data4_serialize(
            ocp_apim_subscription_key=ocp_apim_subscription_key,
            sced_timestamp_from=sced_timestamp_from,
            sced_timestamp_to=sced_timestamp_to,
            repeat_hour_flag=repeat_hour_flag,
            electrical_bus=electrical_bus,
            lmp_from=lmp_from,
            lmpto=lmpto,
            page=page,
            size=size,
            sort=sort,
            dir=dir,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Report",
            '400': "Exception",
            '403': "Exception",
            '404': "Exception",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_data4_with_http_info(
        self,
        ocp_apim_subscription_key: Annotated[StrictStr, Field(description="The subscription key assigned to your ERCOT Public API account.")],
        sced_timestamp_from: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-ddTH24:mm:ss.")] = None,
        sced_timestamp_to: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-ddTH24:mm:ss.")] = None,
        repeat_hour_flag: Annotated[Optional[StrictBool], Field(description="Format - true | false.")] = None,
        electrical_bus: Annotated[Optional[StrictStr], Field(description="Format - abc123.")] = None,
        lmp_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        lmpto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Format - ###. Page number of returned values in the collection.")] = None,
        size: Annotated[Optional[StrictInt], Field(description="Format - ###. Number of returned items per page.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Format - abc123. Defines field by which to sort the returned resource values.")] = None,
        dir: Annotated[Optional[StrictStr], Field(description="Format - abc123. Defines sort order of returned values based on the primary business key of the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Report]:
        """LMP by Electrical Bus

        LMP by Electrical Bus

        :param ocp_apim_subscription_key: The subscription key assigned to your ERCOT Public API account. (required)
        :type ocp_apim_subscription_key: str
        :param sced_timestamp_from: Format - yyyy-MM-ddTH24:mm:ss.
        :type sced_timestamp_from: str
        :param sced_timestamp_to: Format - yyyy-MM-ddTH24:mm:ss.
        :type sced_timestamp_to: str
        :param repeat_hour_flag: Format - true | false.
        :type repeat_hour_flag: bool
        :param electrical_bus: Format - abc123.
        :type electrical_bus: str
        :param lmp_from: Format - ####.###.
        :type lmp_from: float
        :param lmpto: Format - ####.###.
        :type lmpto: float
        :param page: Format - ###. Page number of returned values in the collection.
        :type page: int
        :param size: Format - ###. Number of returned items per page.
        :type size: int
        :param sort: Format - abc123. Defines field by which to sort the returned resource values.
        :type sort: str
        :param dir: Format - abc123. Defines sort order of returned values based on the primary business key of the resource.
        :type dir: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_data4_serialize(
            ocp_apim_subscription_key=ocp_apim_subscription_key,
            sced_timestamp_from=sced_timestamp_from,
            sced_timestamp_to=sced_timestamp_to,
            repeat_hour_flag=repeat_hour_flag,
            electrical_bus=electrical_bus,
            lmp_from=lmp_from,
            lmpto=lmpto,
            page=page,
            size=size,
            sort=sort,
            dir=dir,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Report",
            '400': "Exception",
            '403': "Exception",
            '404': "Exception",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_data4_without_preload_content(
        self,
        ocp_apim_subscription_key: Annotated[StrictStr, Field(description="The subscription key assigned to your ERCOT Public API account.")],
        sced_timestamp_from: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-ddTH24:mm:ss.")] = None,
        sced_timestamp_to: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-ddTH24:mm:ss.")] = None,
        repeat_hour_flag: Annotated[Optional[StrictBool], Field(description="Format - true | false.")] = None,
        electrical_bus: Annotated[Optional[StrictStr], Field(description="Format - abc123.")] = None,
        lmp_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        lmpto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        page: Annotated[Optional[StrictInt], Field(description="Format - ###. Page number of returned values in the collection.")] = None,
        size: Annotated[Optional[StrictInt], Field(description="Format - ###. Number of returned items per page.")] = None,
        sort: Annotated[Optional[StrictStr], Field(description="Format - abc123. Defines field by which to sort the returned resource values.")] = None,
        dir: Annotated[Optional[StrictStr], Field(description="Format - abc123. Defines sort order of returned values based on the primary business key of the resource.")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """LMP by Electrical Bus

        LMP by Electrical Bus

        :param ocp_apim_subscription_key: The subscription key assigned to your ERCOT Public API account. (required)
        :type ocp_apim_subscription_key: str
        :param sced_timestamp_from: Format - yyyy-MM-ddTH24:mm:ss.
        :type sced_timestamp_from: str
        :param sced_timestamp_to: Format - yyyy-MM-ddTH24:mm:ss.
        :type sced_timestamp_to: str
        :param repeat_hour_flag: Format - true | false.
        :type repeat_hour_flag: bool
        :param electrical_bus: Format - abc123.
        :type electrical_bus: str
        :param lmp_from: Format - ####.###.
        :type lmp_from: float
        :param lmpto: Format - ####.###.
        :type lmpto: float
        :param page: Format - ###. Page number of returned values in the collection.
        :type page: int
        :param size: Format - ###. Number of returned items per page.
        :type size: int
        :param sort: Format - abc123. Defines field by which to sort the returned resource values.
        :type sort: str
        :param dir: Format - abc123. Defines sort order of returned values based on the primary business key of the resource.
        :type dir: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_data4_serialize(
            ocp_apim_subscription_key=ocp_apim_subscription_key,
            sced_timestamp_from=sced_timestamp_from,
            sced_timestamp_to=sced_timestamp_to,
            repeat_hour_flag=repeat_hour_flag,
            electrical_bus=electrical_bus,
            lmp_from=lmp_from,
            lmpto=lmpto,
            page=page,
            size=size,
            sort=sort,
            dir=dir,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Report",
            '400': "Exception",
            '403': "Exception",
            '404': "Exception",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_data4_serialize(
        self,
        ocp_apim_subscription_key,
        sced_timestamp_from,
        sced_timestamp_to,
        repeat_hour_flag,
        electrical_bus,
        lmp_from,
        lmpto,
        page,
        size,
        sort,
        dir,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if sced_timestamp_from is not None:
            
            _query_params.append(('SCEDTimestampFrom', sced_timestamp_from))
            
        if sced_timestamp_to is not None:
            
            _query_params.append(('SCEDTimestampTo', sced_timestamp_to))
            
        if repeat_hour_flag is not None:
            
            _query_params.append(('repeatHourFlag', repeat_hour_flag))
            
        if electrical_bus is not None:
            
            _query_params.append(('electricalBus', electrical_bus))
            
        if lmp_from is not None:
            
            _query_params.append(('LMPFrom', lmp_from))
            
        if lmpto is not None:
            
            _query_params.append(('LMPTo', lmpto))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if size is not None:
            
            _query_params.append(('size', size))
            
        if sort is not None:
            
            _query_params.append(('sort', sort))
            
        if dir is not None:
            
            _query_params.append(('dir', dir))
            
        # process the header parameters
        if ocp_apim_subscription_key is not None:
            _header_params['Ocp-Apim-Subscription-Key'] = ocp_apim_subscription_key
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
            'apiKeyQuery', 
            'apiKeyHeader'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/np6-787-cd/lmp_electrical_bus',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


