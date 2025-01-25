"""
Author: Ludvik Jerabek
Package: et-api
License: MIT
"""
from typing import Dict


class WhoisRegistrant(Dict):
    def __init__(self, data: Dict):
        super().__init__(data)

    @property
    def name(self) -> str:
        return self.get('name', None)

    @property
    def email(self) -> str:
        return self.get('email', None)

    @property
    def created(self) -> str:
        return self.get('created', None)

    @property
    def updated(self) -> str:
        return self.get('updated', None)

    @property
    def expires(self) -> str:
        return self.get('expires', None)
