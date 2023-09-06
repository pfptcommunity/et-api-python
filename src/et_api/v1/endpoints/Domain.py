"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from et_api.v1.resources.EventInfoCollection import EventInfoCollection
from et_api.v1.resources.GeoInfoCollection import GeoInfoCollection
from et_api.v1.resources.IPInfoCollection import IPInfoCollection
from et_api.v1.resources.NameServerInfoCollection import NameServerInfoCollection
from et_api.v1.resources.ReputationInfoCollection import ReputationInfoCollection
from et_api.v1.resources.SampleInfoCollection import SampleInfoCollection
from src.et_api.v1.resources.Whois import Whois
from src.et_api.web.CollectionResource import CollectionResource
from src.et_api.web.DictionaryResource import DictionaryResource
from src.et_api.web.Resource import Resource


class Domain(Resource):
    __reputation: CollectionResource[ReputationInfoCollection]
    __urls: CollectionResource
    __samples: CollectionResource[SampleInfoCollection]
    __ips: CollectionResource[IPInfoCollection]
    __events: CollectionResource[EventInfoCollection]
    __nameservers: CollectionResource[NameServerInfoCollection]
    __whois: DictionaryResource[Whois]
    __geo_location: CollectionResource[GeoInfoCollection]

    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)
        self.__reputation = CollectionResource[ReputationInfoCollection](self, "reputation", ReputationInfoCollection)
        self.__urls = CollectionResource(self, "urls")
        self.__samples = CollectionResource[SampleInfoCollection](self, "samples", SampleInfoCollection)
        self.__ips = CollectionResource[IPInfoCollection](self, "ips", IPInfoCollection)
        self.__events = CollectionResource[EventInfoCollection](self, "events", EventInfoCollection)
        self.__nameservers = CollectionResource[NameServerInfoCollection](self, "nameservers", NameServerInfoCollection)
        self.__whois = DictionaryResource[Whois](self, "whois", Whois)
        self.__geo_location = CollectionResource[GeoInfoCollection](self, "geoloc", GeoInfoCollection)

    @property
    def urls(self) -> CollectionResource:
        return self.__urls

    @property
    def reputation(self) -> CollectionResource[ReputationInfoCollection]:
        return self.__reputation

    @property
    def samples(self) -> CollectionResource[SampleInfoCollection]:
        return self.__samples

    @property
    def ips(self) -> CollectionResource[IPInfoCollection]:
        return self.__ips

    @property
    def events(self) -> CollectionResource[EventInfoCollection]:
        return self.__events

    @property
    def nameservers(self) -> CollectionResource[NameServerInfoCollection]:
        return self.__nameservers

    @property
    def whois(self) -> DictionaryResource[Whois]:
        return self.__whois

    @property
    def geo_location(self) -> CollectionResource[GeoInfoCollection]:
        return self.__geo_location
