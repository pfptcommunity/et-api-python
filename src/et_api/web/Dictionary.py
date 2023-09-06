"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from typing import Dict

from requests import Response


class Dictionary(Dict):
    __response: Response

    def __init__(self, response: Response):
        super().__init__(response.json().get('response', {}))
        self.__response = response

    def get_response(self) -> Dict:
        return self.__response.json().get('response', {})

    def get_success(self) -> bool:
        return self.__response.json().get('success', False)

    def get_status(self) -> int:
        return self.__response.status_code

    def get_reason(self) -> str:
        return self.__response.reason

    def get_raw_response(self) -> Response:
        return self.__response
