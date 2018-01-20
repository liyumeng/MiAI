# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.mi_request import MiRequest  # noqa: E501
from swagger_server.models.mi_response import MiResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestMIController(BaseTestCase):
    """MIController integration test stubs"""

    def test_mi_qa(self):
        """Test case for mi_qa

        小米AI音箱
        """
        contents = MiRequest()
        response = self.client.open(
            '/yuml/MIAI/1.0.0/mi_qa',
            method='POST',
            data=json.dumps(contents),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_mi_test(self):
        """Test case for mi_test

        测试请求
        """
        query_string = [('content', 'content_example')]
        response = self.client.open(
            '/yuml/MIAI/1.0.0/test',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
