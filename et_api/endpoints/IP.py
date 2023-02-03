"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
Version: 0.1.0
License: MIT
"""
from et_api.web.Resource import Resource
from et_api.web.CollectionResouce import CollectionResource


class IP(Resource):
    __reputation: CollectionResource = None
    __urls: CollectionResource = None
    __samples: CollectionResource = None
    __events: CollectionResource = None
    __geoloc: CollectionResource = None
    __domains: CollectionResource = None

    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)
        self.__reputation = CollectionResource(self, "reputation")
        self.__urls = CollectionResource(self, "urls")
        self.__samples = CollectionResource(self, "samples")
        self.__events = CollectionResource(self, "events")
        self.__geoloc = CollectionResource(self, "geoloc")
        self.__domains = CollectionResource(self, "domains")

    @property
    def urls(self) -> CollectionResource:
        return self.__urls

    @property
    def reputation(self) -> CollectionResource:
        return self.__reputation

    @property
    def samples(self) -> CollectionResource:
        return self.__samples

    @property
    def events(self) -> CollectionResource:
        return self.__events

    @property
    def geoloc(self) -> CollectionResource:
        return self.__geoloc

    @property
    def geoloc(self) -> CollectionResource:
        return self.__domains
