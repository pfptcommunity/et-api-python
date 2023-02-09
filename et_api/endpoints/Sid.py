"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
Version: 0.1.0
License: MIT
"""
from et_api.web.DictionaryResouce import DictionaryResource
from et_api.web.CollectionResouce import CollectionResource
from et_api.web.SidInfo import SidInfo


class Sid(DictionaryResource[SidInfo]):
    __ips: CollectionResource = None
    __domains: CollectionResource = None
    __samples: CollectionResource = None
    __text: DictionaryResource = None
    __documentation: DictionaryResource = None
    __references: DictionaryResource = None
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri, SidInfo)
        self.__ips = CollectionResource(self, "ips")
        self.__domains = CollectionResource(self, "domains")
        self.__samples = CollectionResource(self, "samples")
        self.__text = DictionaryResource(self, "text")
        self.__documentation = DictionaryResource(self, "documentation")
        self.__references = DictionaryResource(self, "references")

    @property
    def info(self) -> SidInfo:
        return self()

    @property
    def ips(self) -> CollectionResource:
        return self.__ips

    @property
    def domains(self) -> CollectionResource:
        return self.__domains

    @property
    def samples(self) -> CollectionResource:
        return self.__samples

    @property
    def text(self) -> DictionaryResource:
        return self.__text


    @property
    def documentation(self) -> DictionaryResource:
        return self.__documentation


    @property
    def references(self) -> DictionaryResource:
        return self.__references