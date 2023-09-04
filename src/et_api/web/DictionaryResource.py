"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""

from typing import TypeVar, Type, Generic

from src.et_api.v1.resources.Dictionary import Dictionary
from src.et_api.web.Resource import Resource

T = TypeVar('T', bound=Dictionary)


class DictionaryResource(Generic[T], Resource):
    __dict_type: Type[T]

    def __init__(self, parent, uri: str, dict_type: Type[T] = Dictionary):
        super().__init__(parent, uri)
        self.__dict_type = dict_type

    def __call__(self) -> T:
        return self.__dict_type(self._session.get(self.uri))
