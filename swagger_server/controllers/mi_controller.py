import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.mi_request import MiRequest  # noqa: E501
from swagger_server.models.mi_response import MiResponse  # noqa: E501
from swagger_server import util


def mi_qa(contents=None):  # noqa: E501
    """小米AI音箱

    小米AI音箱 # noqa: E501

    :param contents: 输入
    :type contents: dict | bytes

    :rtype: MiResponse
    """
    if connexion.request.is_json:
        contents = MiRequest.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def mi_test(content=None):  # noqa: E501
    """测试请求

    测试请求 # noqa: E501

    :param content: 传入一个句子
    :type content: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'
