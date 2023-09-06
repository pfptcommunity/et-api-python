"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from typing import TypeVar, Type, Dict, Generic

from et_api.web.Collection import Collection
from src.et_api.web.Resource import Resource

D = TypeVar('D', bound='Dict')


class DictionaryCollection(Generic[D], Resource):
    __dictionary_type: Type[D]

    def __init__(self, parent, uri: str, dictionary_type: Type[D] = Dict):
        Resource.__init__(self, parent, uri)
        self.__dictionary_type = dictionary_type

    def __call__(self) -> Collection[D]:
        collection = Collection(self._session.get(self.uri))
        for idx, x in enumerate(collection):
            collection[idx] = self.__dictionary_type(x)
        return collection
