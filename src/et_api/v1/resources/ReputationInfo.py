"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from typing import Dict


class ReputationInfo(Dict):
    def __init__(self, data: dict):
        super().__init__(data)

    @property
    def name(self) -> str:
        return self.get('category', None)

    @property
    def description(self) -> str:
        return self.get('score', None)
