"""
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from typing import Dict


class GeoInfo(Dict):
    def __init__(self, data: dict):
        super().__init__(data)

    @property
    def ip(self) -> str:
        return self.get('ip', None)

    @property
    def country_code(self) -> str:
        return self.get('country_code', None)

    @property
    def country(self) -> str:
        return self.get('country', None)

    @property
    def city(self) -> str:
        return self.get('city', None)

    @property
    def latitude(self) -> str:
        return self.get('latitude', None)

    @property
    def longitude(self) -> str:
        return self.get('longitude', None)
