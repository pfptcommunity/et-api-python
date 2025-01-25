"""
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from requests import Response

from et_api.web.dictionary import Dictionary


class SigDocInfo(Dictionary):
    def __init__(self, response: Response):
        super().__init__(response)

    @property
    def sid(self) -> str:
        return self.get('sid', None)

    @property
    def summary(self) -> str:
        return self.get('summary')

    @property
    def description(self) -> str:
        return self.get('description')

    @property
    def impact(self) -> str:
        return self.get('impact')
