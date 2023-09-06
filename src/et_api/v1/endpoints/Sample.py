"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from et_api.v1.resources.ConnectionInfoCollection import ConnectionInfoCollection
from et_api.v1.resources.DNSInfoCollection import DNSInfoCollection
from et_api.v1.resources.HTTPInfoCollection import HTTPInfoCollection
from et_api.v1.resources.IDSEventInfoCollection import IDSEventInfoCollection
from et_api.web import DictionaryResource
from src.et_api.v1.resources.MalwareInfo import MalwareInfo
from src.et_api.web.CollectionResource import CollectionResource


class Sample(DictionaryResource[MalwareInfo]):
    __connections: CollectionResource[ConnectionInfoCollection]
    __dns: CollectionResource[DNSInfoCollection]
    __ids_events: CollectionResource[IDSEventInfoCollection]
    __http: CollectionResource[HTTPInfoCollection]

    def __init__(self, parent, uri: str):
        super().__init__(parent, uri, MalwareInfo)
        self.__connections = CollectionResource[ConnectionInfoCollection](self, "connections", ConnectionInfoCollection)
        self.__dns = CollectionResource[DNSInfoCollection](self, "dns", DNSInfoCollection)
        self.__ids_events = CollectionResource[IDSEventInfoCollection](self, "events", IDSEventInfoCollection)
        self.__http = CollectionResource[HTTPInfoCollection](self, "http", HTTPInfoCollection)

    @property
    def connections(self) -> CollectionResource[ConnectionInfoCollection]:
        return self.__connections

    @property
    def dns(self) -> CollectionResource[DNSInfoCollection]:
        return self.__dns

    @property
    def ids_events(self) -> CollectionResource[IDSEventInfoCollection]:
        return self.__ids_events

    @property
    def http(self) -> CollectionResource[HTTPInfoCollection]:
        return self.__http
