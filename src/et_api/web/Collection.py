"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from typing import List, TypeVar

from requests import Response

T = TypeVar('T')


class Collection(List[T]):
    __response: Response

    def __init__(self, response: Response):
        super().__init__(response.json().get('response', []))
        self.__response = response

    @property
    def response(self) -> List:
        return self.__response.json().get('response', [])

    @property
    def success(self) -> bool:
        return self.__response.json().get('success', False)

    @property
    def status(self) -> int:
        return self.__response.status_code

    @property
    def reason(self) -> str:
        return self.__response.reason

    @property
    def raw_response(self) -> Response:
        return self.__response

