"""
Author: Ludvik Jerabek
Package: et-api
License: MIT
"""
from typing import List, Dict


class SigRefInfo(Dict):
    def __init__(self, data: Dict):
        super().__init__(data)

    @property
    def type(self) -> str:
        return self.get('reference_type', None)

    @property
    def description(self) -> str:
        return self.get('reference_description', None)

    @property
    def urls(self) -> List[str]:
        return self.get('reference_urls', [])
