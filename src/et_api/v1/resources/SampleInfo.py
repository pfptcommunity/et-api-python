"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from requests import Response

from src.et_api.v1.resources.Dictionary import Dictionary


class SampleInfo(Dictionary):
    def __init__(self, response: Response):
        super().__init__(response)

    @property
    def md5sum(self) -> str:
        return self.get_response().get('md5sum', None)

    @property
    def submit_date(self) -> str:
        return self.get_response().get('submit_date', None)

    @property
    def file_type(self) -> str:
        return self.get_response().get('file_type', None)

    @property
    def file_size(self) -> str:
        return self.get_response().get('file_size', None)

    @property
    def sha256(self) -> str:
        return self.get_response().get('sha256', None)
