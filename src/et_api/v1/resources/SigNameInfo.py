"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from requests import Response

from et_api.web.Dictionary import Dictionary


class SigNameInfo(Dictionary):
    def __init__(self, response: Response):
        super().__init__(response)

    @property
    def sid(self) -> str:
        return self.get_response().get('sid', None)

    @property
    def name(self) -> str:
        return self.get_response().get('sig_name', None)
