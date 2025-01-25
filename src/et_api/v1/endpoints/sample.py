"""
Author: Ludvik Jerabek
Package: et-api
License: MIT
"""

from et_api.v1.resources.connection_info import ConnectionInfo
from et_api.v1.resources.dns_info import DNSInfo
from et_api.v1.resources.http_info import HTTPInfo
from et_api.v1.resources.ids_event_info import IDSEventInfo
from et_api.v1.resources.malware_info import MalwareInfo
from et_api.web import DictionaryResource
from et_api.web.dictionary_collection import DictionaryCollection


class Sample(DictionaryResource[MalwareInfo]):
    __connections: DictionaryCollection[ConnectionInfo]
    __dns: DictionaryCollection[DNSInfo]
    __ids_events: DictionaryCollection[IDSEventInfo]
    __http: DictionaryCollection[HTTPInfo]

    def __init__(self, parent, uri: str):
        super().__init__(parent, uri, MalwareInfo)
        self.__connections = DictionaryCollection[ConnectionInfo](self, "connections", ConnectionInfo)
        self.__dns = DictionaryCollection[DNSInfo](self, "dns", DNSInfo)
        self.__ids_events = DictionaryCollection[IDSEventInfo](self, "events", IDSEventInfo)
        self.__http = DictionaryCollection[HTTPInfo](self, "http", HTTPInfo)

    @property
    def connections(self) -> DictionaryCollection[ConnectionInfo]:
        return self.__connections

    @property
    def dns(self) -> DictionaryCollection[DNSInfo]:
        return self.__dns

    @property
    def ids_events(self) -> DictionaryCollection[IDSEventInfo]:
        return self.__ids_events

    @property
    def http(self) -> DictionaryCollection[HTTPInfo]:
        return self.__http
