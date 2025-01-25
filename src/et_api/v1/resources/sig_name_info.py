"""
Author: Ludvik Jerabek
Package: et-api
License: MIT
"""
from requests import Response

from et_api.web.dictionary import Dictionary


class SigNameInfo(Dictionary):
    def __init__(self, response: Response):
        super().__init__(response)

    @property
    def sid(self) -> str:
        return self.get('sid', None)

    @property
    def name(self) -> str:
        return self.get('sig_name', None)
