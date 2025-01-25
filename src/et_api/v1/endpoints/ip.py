"""
Author: Ludvik Jerabek
Package: et-api
License: MIT
"""
from et_api.v1.resources.domain_info import DomainInfo
from et_api.v1.resources.event_info import EventInfo
from et_api.v1.resources.geo_info import GeoInfo
from et_api.v1.resources.reputation_info import ReputationInfo
from et_api.v1.resources.sample_info import SampleInfo
from et_api.web.collection_resource import CollectionResource
from et_api.web.dictionary_collection import DictionaryCollection
from et_api.web.resource import Resource


class IP(Resource):
    __reputation: DictionaryCollection[ReputationInfo]
    __urls: CollectionResource
    __samples: DictionaryCollection[SampleInfo]
    __events: DictionaryCollection[EventInfo]
    __geo_location: DictionaryCollection[GeoInfo]
    __domains: DictionaryCollection[DomainInfo]

    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)
        self.__reputation = DictionaryCollection[ReputationInfo](self, "reputation", ReputationInfo)
        self.__urls = CollectionResource(self, "urls")
        self.__samples = DictionaryCollection[SampleInfo](self, "samples", SampleInfo)
        self.__events = DictionaryCollection[EventInfo](self, "events", EventInfo)
        self.__geo_location = DictionaryCollection[GeoInfo](self, "geoloc", GeoInfo)
        self.__domains = DictionaryCollection[DomainInfo](self, "domains", DomainInfo)

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
    def events(self) -> DictionaryCollection[EventInfo]:
        return self.__events

    @property
    def geo_location(self) -> DictionaryCollection[GeoInfo]:
        return self.__geo_location

    @property
    def domains(self) -> DictionaryCollection[DomainInfo]:
        return self.__domains
