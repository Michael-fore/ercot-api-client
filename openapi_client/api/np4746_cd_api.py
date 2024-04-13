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


class NP4746CDApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_data8(
        self,
        ocp_apim_subscription_key: Annotated[StrictStr, Field(description="The subscription key assigned to your ERCOT Public API account.")],
        interval_ending_from: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-ddTH24:mm:ss.")] = None,
        interval_ending_to: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-ddTH24:mm:ss.")] = None,
        posted_datetime_from: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-ddTH24:mm:ss.")] = None,
        posted_datetime_to: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-ddTH24:mm:ss.")] = None,
        gen_system_wide_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_system_wide_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_center_west_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_center_west_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_north_west_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_north_west_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_far_west_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_far_west_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_far_east_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_far_east_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_south_east_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_south_east_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_center_east_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_center_east_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        dst_flag: Annotated[Optional[StrictBool], Field(description="Format - true | false.")] = None,
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
        """Solar Power Production - Actual 5-Minute Averaged Values by Geographical Region

        Solar Power Production - Actual 5-Minute Averaged Values by Geographical Region

        :param ocp_apim_subscription_key: The subscription key assigned to your ERCOT Public API account. (required)
        :type ocp_apim_subscription_key: str
        :param interval_ending_from: Format - yyyy-MM-ddTH24:mm:ss.
        :type interval_ending_from: str
        :param interval_ending_to: Format - yyyy-MM-ddTH24:mm:ss.
        :type interval_ending_to: str
        :param posted_datetime_from: Format - yyyy-MM-ddTH24:mm:ss.
        :type posted_datetime_from: str
        :param posted_datetime_to: Format - yyyy-MM-ddTH24:mm:ss.
        :type posted_datetime_to: str
        :param gen_system_wide_from: Format - ####.###.
        :type gen_system_wide_from: float
        :param gen_system_wide_to: Format - ####.###.
        :type gen_system_wide_to: float
        :param gen_center_west_from: Format - ####.###.
        :type gen_center_west_from: float
        :param gen_center_west_to: Format - ####.###.
        :type gen_center_west_to: float
        :param gen_north_west_from: Format - ####.###.
        :type gen_north_west_from: float
        :param gen_north_west_to: Format - ####.###.
        :type gen_north_west_to: float
        :param gen_far_west_from: Format - ####.###.
        :type gen_far_west_from: float
        :param gen_far_west_to: Format - ####.###.
        :type gen_far_west_to: float
        :param gen_far_east_from: Format - ####.###.
        :type gen_far_east_from: float
        :param gen_far_east_to: Format - ####.###.
        :type gen_far_east_to: float
        :param gen_south_east_from: Format - ####.###.
        :type gen_south_east_from: float
        :param gen_south_east_to: Format - ####.###.
        :type gen_south_east_to: float
        :param gen_center_east_from: Format - ####.###.
        :type gen_center_east_from: float
        :param gen_center_east_to: Format - ####.###.
        :type gen_center_east_to: float
        :param dst_flag: Format - true | false.
        :type dst_flag: bool
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

        _param = self._get_data8_serialize(
            ocp_apim_subscription_key=ocp_apim_subscription_key,
            interval_ending_from=interval_ending_from,
            interval_ending_to=interval_ending_to,
            posted_datetime_from=posted_datetime_from,
            posted_datetime_to=posted_datetime_to,
            gen_system_wide_from=gen_system_wide_from,
            gen_system_wide_to=gen_system_wide_to,
            gen_center_west_from=gen_center_west_from,
            gen_center_west_to=gen_center_west_to,
            gen_north_west_from=gen_north_west_from,
            gen_north_west_to=gen_north_west_to,
            gen_far_west_from=gen_far_west_from,
            gen_far_west_to=gen_far_west_to,
            gen_far_east_from=gen_far_east_from,
            gen_far_east_to=gen_far_east_to,
            gen_south_east_from=gen_south_east_from,
            gen_south_east_to=gen_south_east_to,
            gen_center_east_from=gen_center_east_from,
            gen_center_east_to=gen_center_east_to,
            dst_flag=dst_flag,
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
    def get_data8_with_http_info(
        self,
        ocp_apim_subscription_key: Annotated[StrictStr, Field(description="The subscription key assigned to your ERCOT Public API account.")],
        interval_ending_from: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-ddTH24:mm:ss.")] = None,
        interval_ending_to: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-ddTH24:mm:ss.")] = None,
        posted_datetime_from: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-ddTH24:mm:ss.")] = None,
        posted_datetime_to: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-ddTH24:mm:ss.")] = None,
        gen_system_wide_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_system_wide_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_center_west_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_center_west_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_north_west_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_north_west_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_far_west_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_far_west_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_far_east_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_far_east_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_south_east_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_south_east_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_center_east_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_center_east_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        dst_flag: Annotated[Optional[StrictBool], Field(description="Format - true | false.")] = None,
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
        """Solar Power Production - Actual 5-Minute Averaged Values by Geographical Region

        Solar Power Production - Actual 5-Minute Averaged Values by Geographical Region

        :param ocp_apim_subscription_key: The subscription key assigned to your ERCOT Public API account. (required)
        :type ocp_apim_subscription_key: str
        :param interval_ending_from: Format - yyyy-MM-ddTH24:mm:ss.
        :type interval_ending_from: str
        :param interval_ending_to: Format - yyyy-MM-ddTH24:mm:ss.
        :type interval_ending_to: str
        :param posted_datetime_from: Format - yyyy-MM-ddTH24:mm:ss.
        :type posted_datetime_from: str
        :param posted_datetime_to: Format - yyyy-MM-ddTH24:mm:ss.
        :type posted_datetime_to: str
        :param gen_system_wide_from: Format - ####.###.
        :type gen_system_wide_from: float
        :param gen_system_wide_to: Format - ####.###.
        :type gen_system_wide_to: float
        :param gen_center_west_from: Format - ####.###.
        :type gen_center_west_from: float
        :param gen_center_west_to: Format - ####.###.
        :type gen_center_west_to: float
        :param gen_north_west_from: Format - ####.###.
        :type gen_north_west_from: float
        :param gen_north_west_to: Format - ####.###.
        :type gen_north_west_to: float
        :param gen_far_west_from: Format - ####.###.
        :type gen_far_west_from: float
        :param gen_far_west_to: Format - ####.###.
        :type gen_far_west_to: float
        :param gen_far_east_from: Format - ####.###.
        :type gen_far_east_from: float
        :param gen_far_east_to: Format - ####.###.
        :type gen_far_east_to: float
        :param gen_south_east_from: Format - ####.###.
        :type gen_south_east_from: float
        :param gen_south_east_to: Format - ####.###.
        :type gen_south_east_to: float
        :param gen_center_east_from: Format - ####.###.
        :type gen_center_east_from: float
        :param gen_center_east_to: Format - ####.###.
        :type gen_center_east_to: float
        :param dst_flag: Format - true | false.
        :type dst_flag: bool
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

        _param = self._get_data8_serialize(
            ocp_apim_subscription_key=ocp_apim_subscription_key,
            interval_ending_from=interval_ending_from,
            interval_ending_to=interval_ending_to,
            posted_datetime_from=posted_datetime_from,
            posted_datetime_to=posted_datetime_to,
            gen_system_wide_from=gen_system_wide_from,
            gen_system_wide_to=gen_system_wide_to,
            gen_center_west_from=gen_center_west_from,
            gen_center_west_to=gen_center_west_to,
            gen_north_west_from=gen_north_west_from,
            gen_north_west_to=gen_north_west_to,
            gen_far_west_from=gen_far_west_from,
            gen_far_west_to=gen_far_west_to,
            gen_far_east_from=gen_far_east_from,
            gen_far_east_to=gen_far_east_to,
            gen_south_east_from=gen_south_east_from,
            gen_south_east_to=gen_south_east_to,
            gen_center_east_from=gen_center_east_from,
            gen_center_east_to=gen_center_east_to,
            dst_flag=dst_flag,
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
    def get_data8_without_preload_content(
        self,
        ocp_apim_subscription_key: Annotated[StrictStr, Field(description="The subscription key assigned to your ERCOT Public API account.")],
        interval_ending_from: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-ddTH24:mm:ss.")] = None,
        interval_ending_to: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-ddTH24:mm:ss.")] = None,
        posted_datetime_from: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-ddTH24:mm:ss.")] = None,
        posted_datetime_to: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-ddTH24:mm:ss.")] = None,
        gen_system_wide_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_system_wide_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_center_west_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_center_west_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_north_west_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_north_west_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_far_west_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_far_west_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_far_east_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_far_east_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_south_east_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_south_east_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_center_east_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        gen_center_east_to: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        dst_flag: Annotated[Optional[StrictBool], Field(description="Format - true | false.")] = None,
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
        """Solar Power Production - Actual 5-Minute Averaged Values by Geographical Region

        Solar Power Production - Actual 5-Minute Averaged Values by Geographical Region

        :param ocp_apim_subscription_key: The subscription key assigned to your ERCOT Public API account. (required)
        :type ocp_apim_subscription_key: str
        :param interval_ending_from: Format - yyyy-MM-ddTH24:mm:ss.
        :type interval_ending_from: str
        :param interval_ending_to: Format - yyyy-MM-ddTH24:mm:ss.
        :type interval_ending_to: str
        :param posted_datetime_from: Format - yyyy-MM-ddTH24:mm:ss.
        :type posted_datetime_from: str
        :param posted_datetime_to: Format - yyyy-MM-ddTH24:mm:ss.
        :type posted_datetime_to: str
        :param gen_system_wide_from: Format - ####.###.
        :type gen_system_wide_from: float
        :param gen_system_wide_to: Format - ####.###.
        :type gen_system_wide_to: float
        :param gen_center_west_from: Format - ####.###.
        :type gen_center_west_from: float
        :param gen_center_west_to: Format - ####.###.
        :type gen_center_west_to: float
        :param gen_north_west_from: Format - ####.###.
        :type gen_north_west_from: float
        :param gen_north_west_to: Format - ####.###.
        :type gen_north_west_to: float
        :param gen_far_west_from: Format - ####.###.
        :type gen_far_west_from: float
        :param gen_far_west_to: Format - ####.###.
        :type gen_far_west_to: float
        :param gen_far_east_from: Format - ####.###.
        :type gen_far_east_from: float
        :param gen_far_east_to: Format - ####.###.
        :type gen_far_east_to: float
        :param gen_south_east_from: Format - ####.###.
        :type gen_south_east_from: float
        :param gen_south_east_to: Format - ####.###.
        :type gen_south_east_to: float
        :param gen_center_east_from: Format - ####.###.
        :type gen_center_east_from: float
        :param gen_center_east_to: Format - ####.###.
        :type gen_center_east_to: float
        :param dst_flag: Format - true | false.
        :type dst_flag: bool
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

        _param = self._get_data8_serialize(
            ocp_apim_subscription_key=ocp_apim_subscription_key,
            interval_ending_from=interval_ending_from,
            interval_ending_to=interval_ending_to,
            posted_datetime_from=posted_datetime_from,
            posted_datetime_to=posted_datetime_to,
            gen_system_wide_from=gen_system_wide_from,
            gen_system_wide_to=gen_system_wide_to,
            gen_center_west_from=gen_center_west_from,
            gen_center_west_to=gen_center_west_to,
            gen_north_west_from=gen_north_west_from,
            gen_north_west_to=gen_north_west_to,
            gen_far_west_from=gen_far_west_from,
            gen_far_west_to=gen_far_west_to,
            gen_far_east_from=gen_far_east_from,
            gen_far_east_to=gen_far_east_to,
            gen_south_east_from=gen_south_east_from,
            gen_south_east_to=gen_south_east_to,
            gen_center_east_from=gen_center_east_from,
            gen_center_east_to=gen_center_east_to,
            dst_flag=dst_flag,
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


    def _get_data8_serialize(
        self,
        ocp_apim_subscription_key,
        interval_ending_from,
        interval_ending_to,
        posted_datetime_from,
        posted_datetime_to,
        gen_system_wide_from,
        gen_system_wide_to,
        gen_center_west_from,
        gen_center_west_to,
        gen_north_west_from,
        gen_north_west_to,
        gen_far_west_from,
        gen_far_west_to,
        gen_far_east_from,
        gen_far_east_to,
        gen_south_east_from,
        gen_south_east_to,
        gen_center_east_from,
        gen_center_east_to,
        dst_flag,
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
        if interval_ending_from is not None:
            
            _query_params.append(('intervalEndingFrom', interval_ending_from))
            
        if interval_ending_to is not None:
            
            _query_params.append(('intervalEndingTo', interval_ending_to))
            
        if posted_datetime_from is not None:
            
            _query_params.append(('postedDatetimeFrom', posted_datetime_from))
            
        if posted_datetime_to is not None:
            
            _query_params.append(('postedDatetimeTo', posted_datetime_to))
            
        if gen_system_wide_from is not None:
            
            _query_params.append(('genSystemWideFrom', gen_system_wide_from))
            
        if gen_system_wide_to is not None:
            
            _query_params.append(('genSystemWideTo', gen_system_wide_to))
            
        if gen_center_west_from is not None:
            
            _query_params.append(('genCenterWestFrom', gen_center_west_from))
            
        if gen_center_west_to is not None:
            
            _query_params.append(('genCenterWestTo', gen_center_west_to))
            
        if gen_north_west_from is not None:
            
            _query_params.append(('genNorthWestFrom', gen_north_west_from))
            
        if gen_north_west_to is not None:
            
            _query_params.append(('genNorthWestTo', gen_north_west_to))
            
        if gen_far_west_from is not None:
            
            _query_params.append(('genFarWestFrom', gen_far_west_from))
            
        if gen_far_west_to is not None:
            
            _query_params.append(('genFarWestTo', gen_far_west_to))
            
        if gen_far_east_from is not None:
            
            _query_params.append(('genFarEastFrom', gen_far_east_from))
            
        if gen_far_east_to is not None:
            
            _query_params.append(('genFarEastTo', gen_far_east_to))
            
        if gen_south_east_from is not None:
            
            _query_params.append(('genSouthEastFrom', gen_south_east_from))
            
        if gen_south_east_to is not None:
            
            _query_params.append(('genSouthEastTo', gen_south_east_to))
            
        if gen_center_east_from is not None:
            
            _query_params.append(('genCenterEastFrom', gen_center_east_from))
            
        if gen_center_east_to is not None:
            
            _query_params.append(('genCenterEastTo', gen_center_east_to))
            
        if dst_flag is not None:
            
            _query_params.append(('DSTFlag', dst_flag))
            
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
            resource_path='/np4-746-cd/spp_actual_5min_avg_values_geo',
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


