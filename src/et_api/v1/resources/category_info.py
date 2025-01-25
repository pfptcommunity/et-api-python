"""
Author: Ludvik Jerabek
Package: et-api
License: MIT
"""
from typing import Dict


class CategoryInfo(Dict):
    def __init__(self, data: dict):
        super().__init__(data)

    @property
    def name(self) -> str:
        return self.get('name', None)

    @property
    def description(self) -> str:
        return self.get('description', None)
