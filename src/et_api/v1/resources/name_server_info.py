"""
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from typing import Dict


class NameServerInfo(Dict):
    def __init__(self, data: dict):
        super().__init__(data)

    @property
    def server(self) -> str:
        return self.get('server', None)

    @property
    def first_seen(self) -> str:
        return self.get('first_seen', None)

    @property
    def last_seen(self) -> str:
        return self.get('last_seen', None)
