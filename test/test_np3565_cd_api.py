# coding: utf-8

"""
    ERCOT Public API Client/Developer Documentation

    Client/Developer RESTFul web services documentation for ERCOT Market Information List (EMIL) products.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.np3565_cd_api import NP3565CDApi


class TestNP3565CDApi(unittest.TestCase):
    """NP3565CDApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NP3565CDApi()

    def tearDown(self) -> None:
        pass

    def test_get_data100(self) -> None:
        """Test case for get_data100

        Seven-Day Load Forecast by Model and Weather Zone
        """
        pass


if __name__ == '__main__':
    unittest.main()
