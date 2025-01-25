"""
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from requests import Response

from et_api.web.Dictionary import Dictionary


class SigInfo(Dictionary):
    def __init__(self, response: Response):
        super().__init__(response)

    @property
    def sid(self) -> str:
        return self.get('sid', None)

    @property
    def suricata(self) -> str:
        return self.get('suricata_text')

    @property
    def snort(self) -> str:
        return self.get('snort_text')
