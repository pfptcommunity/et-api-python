"""
Author: Ludvik Jerabek
Package: et-api
License: MIT
"""
from typing import Dict


class EventInfo(Dict):
    def __init__(self, data: Dict):
        super().__init__(data)

    @property
    def domain(self) -> str:
        return self.get('domain', None)

    @property
    def date(self) -> str:
        return self.get('date', None)

    @property
    def source(self) -> str:
        return self.get('source', None)

    @property
    def sid(self) -> str:
        return self.get('sid', None)

    @property
    def signature(self) -> str:
        return self.get('signature', None)

    @property
    def count(self) -> str:
        return self.get('count', None)
