"""
Author: Ludvik Jerabek
Package: et-api
License: MIT
"""
from typing import Dict


class HTTPInfo(Dict):
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
    def source_ip(self) -> str:
        return self.get('source_ip', None)

    @property
    def destination_ip(self) -> str:
        return self.get('destination_ip', None)

    @property
    def source_port(self) -> str:
        return self.get('source_port', None)

    @property
    def destination_port(self) -> str:
        return self.get('destination_port', None)

    @property
    def method(self) -> str:
        return self.get('method', None)

    @property
    def url(self) -> str:
        return self.get('url', None)
