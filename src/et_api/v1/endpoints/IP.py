"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from et_api.v1.resources.DomainInfoCollection import DomainInfoCollection
from et_api.v1.resources.EventInfoCollection import EventInfoCollection
from et_api.v1.resources.GeoInfoCollection import GeoInfoCollection
from et_api.v1.resources.ReputationInfoCollection import ReputationInfoCollection
from et_api.v1.resources.SampleInfoCollection import SampleInfoCollection
from src.et_api.web.CollectionResource import CollectionResource
from src.et_api.web.Resource import Resource


class IP(Resource):
    __reputation: CollectionResource[ReputationInfoCollection]
    __urls: CollectionResource
    __samples: CollectionResource[SampleInfoCollection]
    __events: CollectionResource[EventInfoCollection]
    __geo_location: CollectionResource[GeoInfoCollection]
    __domains: CollectionResource[DomainInfoCollection]

    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)
        self.__reputation = CollectionResource[ReputationInfoCollection](self, "reputation", ReputationInfoCollection)
        self.__urls = CollectionResource(self, "urls")
        self.__samples = CollectionResource[SampleInfoCollection](self, "samples", SampleInfoCollection)
        self.__events = CollectionResource[EventInfoCollection](self, "events", EventInfoCollection)
        self.__geo_location = CollectionResource[GeoInfoCollection](self, "geoloc", GeoInfoCollection)
        self.__domains = CollectionResource[DomainInfoCollection](self, "domains", DomainInfoCollection)

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
    def events(self) -> CollectionResource[EventInfoCollection]:
        return self.__events

    @property
    def geo_location(self) -> CollectionResource[GeoInfoCollection]:
        return self.__geo_location

    @property
    def domains(self) -> CollectionResource[DomainInfoCollection]:
        return self.__domains
