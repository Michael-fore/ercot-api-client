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


class NP4179CDApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_data31(
        self,
        ocp_apim_subscription_key: Annotated[StrictStr, Field(description="The subscription key assigned to your ERCOT Public API account.")],
        delivery_date_from: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-dd.")] = None,
        delivery_date_to: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-dd.")] = None,
        hour_ending: Annotated[Optional[StrictStr], Field(description="Format - abc123.")] = None,
        regdn_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        regdnto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        regup_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        regupto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        rrspfr_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        rrspfrto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        rrsffr_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        rrsffrto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        rrsufr_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        rrsufrto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        ecrssd_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        ecrssdto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        ecrsmd_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        ecrsmdto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        nspin_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        nspinto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
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
        """Total Ancillary Service Offers

        Total Ancillary Service Offers

        :param ocp_apim_subscription_key: The subscription key assigned to your ERCOT Public API account. (required)
        :type ocp_apim_subscription_key: str
        :param delivery_date_from: Format - yyyy-MM-dd.
        :type delivery_date_from: str
        :param delivery_date_to: Format - yyyy-MM-dd.
        :type delivery_date_to: str
        :param hour_ending: Format - abc123.
        :type hour_ending: str
        :param regdn_from: Format - ####.###.
        :type regdn_from: float
        :param regdnto: Format - ####.###.
        :type regdnto: float
        :param regup_from: Format - ####.###.
        :type regup_from: float
        :param regupto: Format - ####.###.
        :type regupto: float
        :param rrspfr_from: Format - ####.###.
        :type rrspfr_from: float
        :param rrspfrto: Format - ####.###.
        :type rrspfrto: float
        :param rrsffr_from: Format - ####.###.
        :type rrsffr_from: float
        :param rrsffrto: Format - ####.###.
        :type rrsffrto: float
        :param rrsufr_from: Format - ####.###.
        :type rrsufr_from: float
        :param rrsufrto: Format - ####.###.
        :type rrsufrto: float
        :param ecrssd_from: Format - ####.###.
        :type ecrssd_from: float
        :param ecrssdto: Format - ####.###.
        :type ecrssdto: float
        :param ecrsmd_from: Format - ####.###.
        :type ecrsmd_from: float
        :param ecrsmdto: Format - ####.###.
        :type ecrsmdto: float
        :param nspin_from: Format - ####.###.
        :type nspin_from: float
        :param nspinto: Format - ####.###.
        :type nspinto: float
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

        _param = self._get_data31_serialize(
            ocp_apim_subscription_key=ocp_apim_subscription_key,
            delivery_date_from=delivery_date_from,
            delivery_date_to=delivery_date_to,
            hour_ending=hour_ending,
            regdn_from=regdn_from,
            regdnto=regdnto,
            regup_from=regup_from,
            regupto=regupto,
            rrspfr_from=rrspfr_from,
            rrspfrto=rrspfrto,
            rrsffr_from=rrsffr_from,
            rrsffrto=rrsffrto,
            rrsufr_from=rrsufr_from,
            rrsufrto=rrsufrto,
            ecrssd_from=ecrssd_from,
            ecrssdto=ecrssdto,
            ecrsmd_from=ecrsmd_from,
            ecrsmdto=ecrsmdto,
            nspin_from=nspin_from,
            nspinto=nspinto,
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
    def get_data31_with_http_info(
        self,
        ocp_apim_subscription_key: Annotated[StrictStr, Field(description="The subscription key assigned to your ERCOT Public API account.")],
        delivery_date_from: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-dd.")] = None,
        delivery_date_to: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-dd.")] = None,
        hour_ending: Annotated[Optional[StrictStr], Field(description="Format - abc123.")] = None,
        regdn_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        regdnto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        regup_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        regupto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        rrspfr_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        rrspfrto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        rrsffr_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        rrsffrto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        rrsufr_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        rrsufrto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        ecrssd_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        ecrssdto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        ecrsmd_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        ecrsmdto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        nspin_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        nspinto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
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
        """Total Ancillary Service Offers

        Total Ancillary Service Offers

        :param ocp_apim_subscription_key: The subscription key assigned to your ERCOT Public API account. (required)
        :type ocp_apim_subscription_key: str
        :param delivery_date_from: Format - yyyy-MM-dd.
        :type delivery_date_from: str
        :param delivery_date_to: Format - yyyy-MM-dd.
        :type delivery_date_to: str
        :param hour_ending: Format - abc123.
        :type hour_ending: str
        :param regdn_from: Format - ####.###.
        :type regdn_from: float
        :param regdnto: Format - ####.###.
        :type regdnto: float
        :param regup_from: Format - ####.###.
        :type regup_from: float
        :param regupto: Format - ####.###.
        :type regupto: float
        :param rrspfr_from: Format - ####.###.
        :type rrspfr_from: float
        :param rrspfrto: Format - ####.###.
        :type rrspfrto: float
        :param rrsffr_from: Format - ####.###.
        :type rrsffr_from: float
        :param rrsffrto: Format - ####.###.
        :type rrsffrto: float
        :param rrsufr_from: Format - ####.###.
        :type rrsufr_from: float
        :param rrsufrto: Format - ####.###.
        :type rrsufrto: float
        :param ecrssd_from: Format - ####.###.
        :type ecrssd_from: float
        :param ecrssdto: Format - ####.###.
        :type ecrssdto: float
        :param ecrsmd_from: Format - ####.###.
        :type ecrsmd_from: float
        :param ecrsmdto: Format - ####.###.
        :type ecrsmdto: float
        :param nspin_from: Format - ####.###.
        :type nspin_from: float
        :param nspinto: Format - ####.###.
        :type nspinto: float
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

        _param = self._get_data31_serialize(
            ocp_apim_subscription_key=ocp_apim_subscription_key,
            delivery_date_from=delivery_date_from,
            delivery_date_to=delivery_date_to,
            hour_ending=hour_ending,
            regdn_from=regdn_from,
            regdnto=regdnto,
            regup_from=regup_from,
            regupto=regupto,
            rrspfr_from=rrspfr_from,
            rrspfrto=rrspfrto,
            rrsffr_from=rrsffr_from,
            rrsffrto=rrsffrto,
            rrsufr_from=rrsufr_from,
            rrsufrto=rrsufrto,
            ecrssd_from=ecrssd_from,
            ecrssdto=ecrssdto,
            ecrsmd_from=ecrsmd_from,
            ecrsmdto=ecrsmdto,
            nspin_from=nspin_from,
            nspinto=nspinto,
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
    def get_data31_without_preload_content(
        self,
        ocp_apim_subscription_key: Annotated[StrictStr, Field(description="The subscription key assigned to your ERCOT Public API account.")],
        delivery_date_from: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-dd.")] = None,
        delivery_date_to: Annotated[Optional[StrictStr], Field(description="Format - yyyy-MM-dd.")] = None,
        hour_ending: Annotated[Optional[StrictStr], Field(description="Format - abc123.")] = None,
        regdn_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        regdnto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        regup_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        regupto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        rrspfr_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        rrspfrto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        rrsffr_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        rrsffrto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        rrsufr_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        rrsufrto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        ecrssd_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        ecrssdto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        ecrsmd_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        ecrsmdto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        nspin_from: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
        nspinto: Annotated[Optional[Union[StrictFloat, StrictInt]], Field(description="Format - ####.###.")] = None,
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
        """Total Ancillary Service Offers

        Total Ancillary Service Offers

        :param ocp_apim_subscription_key: The subscription key assigned to your ERCOT Public API account. (required)
        :type ocp_apim_subscription_key: str
        :param delivery_date_from: Format - yyyy-MM-dd.
        :type delivery_date_from: str
        :param delivery_date_to: Format - yyyy-MM-dd.
        :type delivery_date_to: str
        :param hour_ending: Format - abc123.
        :type hour_ending: str
        :param regdn_from: Format - ####.###.
        :type regdn_from: float
        :param regdnto: Format - ####.###.
        :type regdnto: float
        :param regup_from: Format - ####.###.
        :type regup_from: float
        :param regupto: Format - ####.###.
        :type regupto: float
        :param rrspfr_from: Format - ####.###.
        :type rrspfr_from: float
        :param rrspfrto: Format - ####.###.
        :type rrspfrto: float
        :param rrsffr_from: Format - ####.###.
        :type rrsffr_from: float
        :param rrsffrto: Format - ####.###.
        :type rrsffrto: float
        :param rrsufr_from: Format - ####.###.
        :type rrsufr_from: float
        :param rrsufrto: Format - ####.###.
        :type rrsufrto: float
        :param ecrssd_from: Format - ####.###.
        :type ecrssd_from: float
        :param ecrssdto: Format - ####.###.
        :type ecrssdto: float
        :param ecrsmd_from: Format - ####.###.
        :type ecrsmd_from: float
        :param ecrsmdto: Format - ####.###.
        :type ecrsmdto: float
        :param nspin_from: Format - ####.###.
        :type nspin_from: float
        :param nspinto: Format - ####.###.
        :type nspinto: float
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

        _param = self._get_data31_serialize(
            ocp_apim_subscription_key=ocp_apim_subscription_key,
            delivery_date_from=delivery_date_from,
            delivery_date_to=delivery_date_to,
            hour_ending=hour_ending,
            regdn_from=regdn_from,
            regdnto=regdnto,
            regup_from=regup_from,
            regupto=regupto,
            rrspfr_from=rrspfr_from,
            rrspfrto=rrspfrto,
            rrsffr_from=rrsffr_from,
            rrsffrto=rrsffrto,
            rrsufr_from=rrsufr_from,
            rrsufrto=rrsufrto,
            ecrssd_from=ecrssd_from,
            ecrssdto=ecrssdto,
            ecrsmd_from=ecrsmd_from,
            ecrsmdto=ecrsmdto,
            nspin_from=nspin_from,
            nspinto=nspinto,
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


    def _get_data31_serialize(
        self,
        ocp_apim_subscription_key,
        delivery_date_from,
        delivery_date_to,
        hour_ending,
        regdn_from,
        regdnto,
        regup_from,
        regupto,
        rrspfr_from,
        rrspfrto,
        rrsffr_from,
        rrsffrto,
        rrsufr_from,
        rrsufrto,
        ecrssd_from,
        ecrssdto,
        ecrsmd_from,
        ecrsmdto,
        nspin_from,
        nspinto,
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
        if delivery_date_from is not None:
            
            _query_params.append(('deliveryDateFrom', delivery_date_from))
            
        if delivery_date_to is not None:
            
            _query_params.append(('deliveryDateTo', delivery_date_to))
            
        if hour_ending is not None:
            
            _query_params.append(('hourEnding', hour_ending))
            
        if regdn_from is not None:
            
            _query_params.append(('REGDNFrom', regdn_from))
            
        if regdnto is not None:
            
            _query_params.append(('REGDNTo', regdnto))
            
        if regup_from is not None:
            
            _query_params.append(('REGUPFrom', regup_from))
            
        if regupto is not None:
            
            _query_params.append(('REGUPTo', regupto))
            
        if rrspfr_from is not None:
            
            _query_params.append(('RRSPFRFrom', rrspfr_from))
            
        if rrspfrto is not None:
            
            _query_params.append(('RRSPFRTo', rrspfrto))
            
        if rrsffr_from is not None:
            
            _query_params.append(('RRSFFRFrom', rrsffr_from))
            
        if rrsffrto is not None:
            
            _query_params.append(('RRSFFRTo', rrsffrto))
            
        if rrsufr_from is not None:
            
            _query_params.append(('RRSUFRFrom', rrsufr_from))
            
        if rrsufrto is not None:
            
            _query_params.append(('RRSUFRTo', rrsufrto))
            
        if ecrssd_from is not None:
            
            _query_params.append(('ECRSSDFrom', ecrssd_from))
            
        if ecrssdto is not None:
            
            _query_params.append(('ECRSSDTo', ecrssdto))
            
        if ecrsmd_from is not None:
            
            _query_params.append(('ECRSMDFrom', ecrsmd_from))
            
        if ecrsmdto is not None:
            
            _query_params.append(('ECRSMDTo', ecrsmdto))
            
        if nspin_from is not None:
            
            _query_params.append(('NSPINFrom', nspin_from))
            
        if nspinto is not None:
            
            _query_params.append(('NSPINTo', nspinto))
            
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
            resource_path='/np4-179-cd/total_as_service_offers',
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


