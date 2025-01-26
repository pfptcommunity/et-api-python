"""
Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from __future__ import annotations

from typing import Type, Generic, Union

from .resource import Resource, TResource


class Resources(Generic[TResource], Resource):
    __res: Type[TResource]

    def __init__(self, parent: Union[Resource, None], uri: str, res: Type[TResource]):
        super().__init__(parent, uri)
        self.__res = res

    def __getitem__(self, domain: str) -> TResource:
        return self.__res(self, domain.strip())
