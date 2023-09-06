"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from typing import Dict


class DNSInfo(Dict):
    def __init__(self, data: dict):
        super().__init__(data)

    @property
    def source(self) -> str:
        return self.get('source', None)

    @property
    def date(self) -> str:
        return self.get('date', None)

    @property
    def domain(self) -> str:
        return self.get('domain', None)

    @property
    def answer(self) -> str:
        return self.get('answer', None)

    @property
    def record_type(self) -> str:
        return self.get('record_type', None)
