import connexion
import six

from swagger_server.models.inline_response200 import InlineResponse200  # noqa: E501
from swagger_server.models.mi_request import MiRequest  # noqa: E501
from swagger_server.models.mi_response import MiResponse  # noqa: E501
from swagger_server import util
from mi.utils import validate


def mi_qa(contents=None):  # noqa: E501
    """小米AI音箱

    小米AI音箱 # noqa: E501

    :param contents: 输入
    :type contents: dict | bytes

    :rtype: MiResponse
    """
    if connexion.request.is_json:
        contents = MiRequest.from_dict(connexion.request.get_json())  # noqa: E501
    headers = connexion.request.headers
    ip=headers.get('X_FORWARDED_FOR')
    query=contents.query

    print(ip,query)
    if not validate(headers):
        print("验证失败")
        return {"version": "0.1"}

    result = {"version": "0.1",
              "session_attributes": {},
              "is_session_end": False,
              "response": {
                  "to_speak": {
                      "type": 0,
                      "text": query
                  },
                  "open_mic": True,
                  "not_understand": False
              },
            }
    return result


def mi_test(content=None):  # noqa: E501
    """测试请求

    测试请求 # noqa: E501

    :param content: 传入一个句子
    :type content: str

    :rtype: InlineResponse200
    """
    return 'do some magic!'
