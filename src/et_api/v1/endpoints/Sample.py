"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from src.et_api.v1.resources.SampleInfo import SampleInfo
from src.et_api.web.CollectionResource import CollectionResource
from src.et_api.web.DictionaryResource import DictionaryResource


class Sample(DictionaryResource[SampleInfo]):
    __connections: CollectionResource = None
    __dns: CollectionResource = None
    __events: CollectionResource = None
    __http: CollectionResource = None

    def __init__(self, parent, uri: str):
        super().__init__(parent, uri, SampleInfo)
        self.__connections = CollectionResource(self, "connections")
        self.__dns = CollectionResource(self, "dns")
        self.__events = CollectionResource(self, "events")
        self.__http = CollectionResource(self, "http")

    @property
    def info(self) -> SampleInfo:
        return self()

    @property
    def connections(self) -> CollectionResource:
        return self.__connections

    @property
    def dns(self) -> CollectionResource:
        return self.__dns

    @property
    def events(self) -> CollectionResource:
        return self.__events

    @property
    def http(self) -> CollectionResource:
        return self.__http
