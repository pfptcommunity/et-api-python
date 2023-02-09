"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
Version: 0.1.0
License: MIT
"""
from typing import Dict
from requests import Response
from et_api.resources.Dictionary import Dictionary


class SidInfo(Dictionary):
    def __init__(self, response: Response):
        super().__init__(response)

    @property
    def sid(self) -> str:
        return self.get_response().get('sid', None)

    @property
    def sig_name(self) -> str:
        return self.get_response().get('sig_name', None)
