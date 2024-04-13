# coding: utf-8

"""
    ERCOT Public API Client/Developer Documentation

    Client/Developer RESTFul web services documentation for ERCOT Market Information List (EMIL) products.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.np3990_ex_api import NP3990EXApi


class TestNP3990EXApi(unittest.TestCase):
    """NP3990EXApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NP3990EXApi()

    def tearDown(self) -> None:
        pass

    def test_get_data34(self) -> None:
        """Test case for get_data34

        60 Day SASM Load Resource AS Offers
        """
        pass

    def test_get_data35(self) -> None:
        """Test case for get_data35

        60 Day SASM Load Resource AS Offer Awards
        """
        pass

    def test_get_data36(self) -> None:
        """Test case for get_data36

        60 Day SASM Generation Resource AS Offers
        """
        pass

    def test_get_data37(self) -> None:
        """Test case for get_data37

        60 Day SASM Generation Resource AS Offer Awards
        """
        pass


if __name__ == '__main__':
    unittest.main()
