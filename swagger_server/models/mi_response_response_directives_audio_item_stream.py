# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class MiResponseResponseDirectivesAudioItemStream(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, token: str=None, url: str=None, offset_in_milliseconds: int=None):  # noqa: E501
        """MiResponseResponseDirectivesAudioItemStream - a model defined in Swagger

        :param token: The token of this MiResponseResponseDirectivesAudioItemStream.  # noqa: E501
        :type token: str
        :param url: The url of this MiResponseResponseDirectivesAudioItemStream.  # noqa: E501
        :type url: str
        :param offset_in_milliseconds: The offset_in_milliseconds of this MiResponseResponseDirectivesAudioItemStream.  # noqa: E501
        :type offset_in_milliseconds: int
        """
        self.swagger_types = {
            'token': str,
            'url': str,
            'offset_in_milliseconds': int
        }

        self.attribute_map = {
            'token': 'token',
            'url': 'url',
            'offset_in_milliseconds': 'offset_in_milliseconds'
        }

        self._token = token
        self._url = url
        self._offset_in_milliseconds = offset_in_milliseconds

    @classmethod
    def from_dict(cls, dikt) -> 'MiResponseResponseDirectivesAudioItemStream':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MiResponse_response_directives_audio_item_stream of this MiResponseResponseDirectivesAudioItemStream.  # noqa: E501
        :rtype: MiResponseResponseDirectivesAudioItemStream
        """
        return util.deserialize_model(dikt, cls)

    @property
    def token(self) -> str:
        """Gets the token of this MiResponseResponseDirectivesAudioItemStream.


        :return: The token of this MiResponseResponseDirectivesAudioItemStream.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token: str):
        """Sets the token of this MiResponseResponseDirectivesAudioItemStream.


        :param token: The token of this MiResponseResponseDirectivesAudioItemStream.
        :type token: str
        """

        self._token = token

    @property
    def url(self) -> str:
        """Gets the url of this MiResponseResponseDirectivesAudioItemStream.


        :return: The url of this MiResponseResponseDirectivesAudioItemStream.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url: str):
        """Sets the url of this MiResponseResponseDirectivesAudioItemStream.


        :param url: The url of this MiResponseResponseDirectivesAudioItemStream.
        :type url: str
        """

        self._url = url

    @property
    def offset_in_milliseconds(self) -> int:
        """Gets the offset_in_milliseconds of this MiResponseResponseDirectivesAudioItemStream.


        :return: The offset_in_milliseconds of this MiResponseResponseDirectivesAudioItemStream.
        :rtype: int
        """
        return self._offset_in_milliseconds

    @offset_in_milliseconds.setter
    def offset_in_milliseconds(self, offset_in_milliseconds: int):
        """Sets the offset_in_milliseconds of this MiResponseResponseDirectivesAudioItemStream.


        :param offset_in_milliseconds: The offset_in_milliseconds of this MiResponseResponseDirectivesAudioItemStream.
        :type offset_in_milliseconds: int
        """

        self._offset_in_milliseconds = offset_in_milliseconds