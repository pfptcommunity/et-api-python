"""
Author: Ludvik Jerabek
Package: et-api
License: MIT
"""
from typing import Dict


class WhoisRegistrar(Dict):
    def __init__(self, data: Dict):
        super().__init__(data)

    @property
    def name(self) -> str:
        return self.get('name', None)

    @property
    def country(self) -> str:
        return self.get('country', None)

    @property
    def website(self) -> str:
        return self.get('website', None)
