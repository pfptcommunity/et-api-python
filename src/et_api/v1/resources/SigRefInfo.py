"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from typing import List, Dict

from requests import Response

from et_api.web.Dictionary import Dictionary


class SigRefInfo(Dict):
    def __init__(self, data: Dict):
        super().__init__(data)

    @property
    def reference_type(self) -> str:
        return self.get('reference_type', None)

    @property
    def reference_description(self) -> str:
        return self.get('reference_description', None)

    @property
    def reference_urls(self) -> List[str]:
        return self.get('reference_urls', [])
