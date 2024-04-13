# coding: utf-8

"""
    ERCOT Public API Client/Developer Documentation

    Client/Developer RESTFul web services documentation for ERCOT Market Information List (EMIL) products.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.np4190_cd_api import NP4190CDApi


class TestNP4190CDApi(unittest.TestCase):
    """NP4190CDApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NP4190CDApi()

    def tearDown(self) -> None:
        pass

    def test_get_data28(self) -> None:
        """Test case for get_data28

        DAM Settlement Point Prices
        """
        pass


if __name__ == '__main__':
    unittest.main()