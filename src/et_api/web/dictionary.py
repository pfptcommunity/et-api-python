"""
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from typing import Dict

from requests import Response

from et_api.web.response_wrapper import ResponseWrapper


class Dictionary(Dict, ResponseWrapper):
    def __init__(self, response: Response):
        ResponseWrapper.__init__(self, response)
        super().__init__(response.json().get('response', {}))

    @property
    def response(self) -> Dict:
        return self._response.json().get('response', {})

    @property
    def success(self) -> bool:
        return self._response.json().get('success', False)
