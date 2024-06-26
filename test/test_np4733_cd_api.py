# coding: utf-8

"""
    ERCOT Public API Client/Developer Documentation

    Client/Developer RESTFul web services documentation for ERCOT Market Information List (EMIL) products.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.np4733_cd_api import NP4733CDApi


class TestNP4733CDApi(unittest.TestCase):
    """NP4733CDApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NP4733CDApi()

    def tearDown(self) -> None:
        pass

    def test_get_data14(self) -> None:
        """Test case for get_data14

        Wind Power Production - Actual 5-Minute Averaged Values
        """
        pass


if __name__ == '__main__':
    unittest.main()
