"""
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""

from typing import TypeVar, Type, Generic
from .Resource import Resource

R = TypeVar('R', bound='Resource')


class Resources(Generic[R], Resource):
    __res: Type[R]

    def __init__(self, parent, uri: str, res: Type[R]):
        super().__init__(parent, uri)
        self.__res = res

    def __getitem__(self, domain: str) -> R:
        return self.__res(self, domain.casefold().strip())
