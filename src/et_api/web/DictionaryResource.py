"""
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""

from typing import TypeVar, Type, Generic

from et_api.web.Dictionary import Dictionary
from et_api.web.Resource import Resource

T = TypeVar('T', bound=Dictionary)


class DictionaryResource(Generic[T], Resource):
    __dict_type: Type[T]

    def __init__(self, parent, uri: str, dict_type: Type[T] = Dictionary):
        super().__init__(parent, uri)
        self.__dict_type = dict_type

    def __call__(self) -> T:
        return self.__dict_type(self.session.get(self.uri))
