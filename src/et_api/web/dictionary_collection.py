"""
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from typing import TypeVar, Type, Dict, Generic

from et_api.web.collection import Collection
from et_api.web.resource import Resource

D = TypeVar('D', bound='Dict')


class DictionaryCollection(Generic[D], Resource):
    __dictionary_type: Type[D]

    def __init__(self, parent, uri: str, dictionary_type: Type[D] = Dict):
        Resource.__init__(self, parent, uri)
        self.__dictionary_type = dictionary_type

    def __call__(self) -> Collection[D]:
        collection = Collection(self.session.get(self.uri))
        for idx, x in enumerate(collection):
            collection[idx] = self.__dictionary_type(x)
        return collection
