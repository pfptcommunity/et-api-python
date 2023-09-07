"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from typing import TypeVar, Type, Generic

from src.et_api.web.Collection import Collection
from src.et_api.web.Resource import Resource

T = TypeVar('T', bound=Collection)


class CollectionResource(Generic[T], Resource):
    __collection_type: Type[T]

    def __init__(self, parent, uri: str, collection_type: Type[T] = Collection):
        super().__init__(parent, uri)
        self.__collection_type = collection_type

    def __call__(self) -> T:
        return self.__collection_type(self.session.get(self.uri))
