"""
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from typing import TypeVar, Type, Generic

from et_api.web.collection import Collection
from et_api.web.resource import Resource

T = TypeVar('T', bound=Collection)


class CollectionResource(Generic[T], Resource):
    __collection_type: Type[T]

    def __init__(self, parent, uri: str, collection_type: Type[T] = Collection):
        super().__init__(parent, uri)
        self.__collection_type = collection_type

    def __call__(self) -> T:
        return self.__collection_type(self.session.get(self.uri))
