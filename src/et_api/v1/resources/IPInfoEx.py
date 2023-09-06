"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from et_api.v1.resources.IPInfo import IPInfo


class IPInfoEx(IPInfo):
    def __init__(self, data: dict):
        super().__init__(data)

    @property
    def long_ip(self) -> str:
        return self.get('long_ip', None)
