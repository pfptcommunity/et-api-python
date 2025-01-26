"""
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from typing import List, TypeVar

from requests import Response

from et_api.web.response_wrapper import ResponseWrapper

T = TypeVar('T')


class Collection(List[T], ResponseWrapper):
    def __init__(self, response: Response):
        ResponseWrapper.__init__(self, response)
        super().__init__(response.json().get('response', []))

    @property
    def response(self) -> List:
        return self._response.json().get('response', [])

    @property
    def success(self) -> bool:
        return self._response.json().get('success', False)
