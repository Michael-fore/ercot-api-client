# coding: utf-8

"""
    ERCOT Public API Client/Developer Documentation

    Client/Developer RESTFul web services documentation for ERCOT Market Information List (EMIL) products.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.np4737_cd_api import NP4737CDApi


class TestNP4737CDApi(unittest.TestCase):
    """NP4737CDApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NP4737CDApi()

    def tearDown(self) -> None:
        pass

    def test_get_data13(self) -> None:
        """Test case for get_data13

        Solar Power Production - Hourly Averaged Actual and Forecasted Values
        """
        pass


if __name__ == '__main__':
    unittest.main()
