"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from urllib.parse import urljoin
from requests import Response
from typing import List
from typing import Iterator


class Collection(List):
    __response: Response

    def __init__(self, response: Response):
        super().__init__(response.json().get('response', []))
        self.__response = response

    def get_success(self) -> bool:
        return self.__response.json().get('success', False)

    def get_response(self) -> List:
        return self.__response.json().get('response', [])

    def get_status(self) -> int:
        return self.__response.status_code

    def get_reason(self) -> str:
        return self.__response.reason

    def get_raw_response(self) -> Response:
        return self.__response
