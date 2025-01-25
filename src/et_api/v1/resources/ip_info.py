"""
Author: Ludvik Jerabek
Package: et-api
License: MIT
"""
from typing import Dict


class IPInfo(Dict):
    def __init__(self, data: dict):
        super().__init__(data)

    @property
    def ip(self) -> str:
        return self.get('ip', None)

    @property
    def first_seen(self) -> str:
        return self.get('first_seen', None)

    @property
    def last_seen(self) -> str:
        return self.get('last_seen', None)
