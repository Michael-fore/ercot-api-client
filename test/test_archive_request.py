# coding: utf-8

"""
    ERCOT Public API Client/Developer Documentation

    Client/Developer RESTFul web services documentation for ERCOT Market Information List (EMIL) products.

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.archive_request import ArchiveRequest

class TestArchiveRequest(unittest.TestCase):
    """ArchiveRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArchiveRequest:
        """Test ArchiveRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArchiveRequest`
        """
        model = ArchiveRequest()
        if include_optional:
            return ArchiveRequest(
                doc_ids = [
                    56
                    ]
            )
        else:
            return ArchiveRequest(
                doc_ids = [
                    56
                    ],
        )
        """

    def testArchiveRequest(self):
        """Test ArchiveRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
