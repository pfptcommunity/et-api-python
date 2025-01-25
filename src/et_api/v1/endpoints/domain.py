"""
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""

from et_api.v1.resources.event_info import EventInfo
from et_api.v1.resources.geo_info import GeoInfo
from et_api.v1.resources.ip_info import IPInfo
from et_api.v1.resources.name_server_info import NameServerInfo
from et_api.v1.resources.reputation_info import ReputationInfo
from et_api.v1.resources.sample_info import SampleInfo
from et_api.v1.resources.whois import Whois
from et_api.web.collection_resource import CollectionResource
from et_api.web.dictionary_collection import DictionaryCollection
from et_api.web.dictionary_resource import DictionaryResource
from et_api.web.resource import Resource


class Domain(Resource):
    __reputation: DictionaryCollection[ReputationInfo]
    __urls: CollectionResource
    __samples: DictionaryCollection[SampleInfo]
    __ips: DictionaryCollection[IPInfo]
    __events: DictionaryCollection[EventInfo]
    __nameservers: DictionaryCollection[NameServerInfo]
    __whois: DictionaryResource[Whois]
    __geo_location: DictionaryCollection[GeoInfo]

    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)
        self.__reputation = DictionaryCollection[ReputationInfo](self, "reputation", ReputationInfo)
        self.__urls = CollectionResource(self, "urls")
        self.__samples = DictionaryCollection[SampleInfo](self, "samples", SampleInfo)
        self.__ips = DictionaryCollection[IPInfo](self, "ips", IPInfo)
        self.__events = DictionaryCollection[EventInfo](self, "events", EventInfo)
        self.__nameservers = DictionaryCollection[NameServerInfo](self, "nameservers", NameServerInfo)
        self.__whois = DictionaryResource[Whois](self, "whois", Whois)
        self.__geo_location = DictionaryCollection[GeoInfo](self, "geoloc", GeoInfo)

    @property
    def urls(self) -> CollectionResource:
        return self.__urls

    @property
    def reputation(self) -> DictionaryCollection[ReputationInfo]:
        return self.__reputation

    @property
    def samples(self) -> DictionaryCollection[SampleInfo]:
        return self.__samples

    @property
    def ips(self) -> DictionaryCollection[IPInfo]:
        return self.__ips

    @property
    def events(self) -> DictionaryCollection[EventInfo]:
        return self.__events

    @property
    def nameservers(self) -> DictionaryCollection[NameServerInfo]:
        return self.__nameservers

    @property
    def whois(self) -> DictionaryResource[Whois]:
        return self.__whois

    @property
    def geo_location(self) -> DictionaryCollection[GeoInfo]:
        return self.__geo_location
