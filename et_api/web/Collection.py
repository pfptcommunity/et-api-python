"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: et_api
Version: 0.1.0
License: MIT
"""
from urllib.parse import urljoin
from requests import Response
from typing import List
from typing import Iterator


class Collection:
    __response: Response
    __iterator = Iterator

    def __init__(self, response: Response):
        self.__response = response
        self.__initial = True

    def __getitem__(self, index):
        return self.__response.json().get('response', [])[index]

    def __len__(self) -> int:
        return len(self.__response.json().get('response', []))

    def __iter__(self):
        self.__iterator = iter(self.__response.json().get('response', []))
        return self

    def __next__(self):
        return next(self.__iterator)

    def get_success(self) -> bool:
        return self.__response.json().get('success', False)

    def get_response(self) -> List[str]:
        return self.__response.json().get('response', [])

    def get_status(self) -> int:
        return self.__response.status_code

    def get_reason(self) -> str:
        return self.__response.reason

    def get_raw_response(self) -> Response:
        return self.__response
