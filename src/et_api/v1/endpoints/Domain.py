"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""

from et_api.v1.resources.EventInfo import EventInfo
from et_api.v1.resources.GeoInfo import GeoInfo
from et_api.v1.resources.IPInfo import IPInfo
from et_api.v1.resources.NameServerInfo import NameServerInfo
from et_api.v1.resources.ReputationInfo import ReputationInfo
from et_api.v1.resources.SampleInfo import SampleInfo
from et_api.v1.resources.Whois import Whois
from et_api.web.CollectionResource import CollectionResource
from et_api.web.DictionaryCollection import DictionaryCollection
from et_api.web.DictionaryResource import DictionaryResource
from et_api.web.Resource import Resource


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
