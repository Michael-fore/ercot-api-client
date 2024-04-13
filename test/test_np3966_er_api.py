# coding: utf-8

"""
    ERCOT Public API Client/Developer Documentation

    Client/Developer RESTFul web services documentation for ERCOT Market Information List (EMIL) products.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.np3966_er_api import NP3966ERApi


class TestNP3966ERApi(unittest.TestCase):
    """NP3966ERApi unit test stubs"""

    def setUp(self) -> None:
        self.api = NP3966ERApi()

    def tearDown(self) -> None:
        pass

    def test_get_data38(self) -> None:
        """Test case for get_data38

        60 Day DAM QSE Self Arranged AS
        """
        pass

    def test_get_data39(self) -> None:
        """Test case for get_data39

        60 Day DAM PTP Obligation Option Awards
        """
        pass

    def test_get_data40(self) -> None:
        """Test case for get_data40

        60 Day DAM PTP Obligation Option
        """
        pass

    def test_get_data41(self) -> None:
        """Test case for get_data41

        60 Day DAM PTP Obligation Bids
        """
        pass

    def test_get_data42(self) -> None:
        """Test case for get_data42

        60 Day DAM PTP Obligation Bid Awards
        """
        pass

    def test_get_data43(self) -> None:
        """Test case for get_data43

        60 Day DAM Load Resource Data
        """
        pass

    def test_get_data44(self) -> None:
        """Test case for get_data44

        60 Day DAM Load Resources AS Offers
        """
        pass

    def test_get_data45(self) -> None:
        """Test case for get_data45

        60 Day DAM Generation Resource Data
        """
        pass

    def test_get_data46(self) -> None:
        """Test case for get_data46

        60 Day DAM Generation Resources AS Offers
        """
        pass

    def test_get_data47(self) -> None:
        """Test case for get_data47

        60 Day DAM Energy Only Offers
        """
        pass

    def test_get_data48(self) -> None:
        """Test case for get_data48

        60 Day DAM Energy Offer Only Awards
        """
        pass

    def test_get_data49(self) -> None:
        """Test case for get_data49

        60 Day DAM Energy Bids
        """
        pass

    def test_get_data50(self) -> None:
        """Test case for get_data50

        60 Day DAM Energy Bid Awards
        """
        pass


if __name__ == '__main__':
    unittest.main()