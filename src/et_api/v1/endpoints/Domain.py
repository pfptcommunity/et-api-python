"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from src.et_api.web.Resource import Resource
from src.et_api.v1.resources.Whois import Whois
from src.et_api.web.DictionaryResource import DictionaryResource
from src.et_api.web.CollectionResource import CollectionResource


class Domain(Resource):
    __reputation: CollectionResource = None
    __urls: CollectionResource = None
    __samples: CollectionResource = None
    __ips: CollectionResource = None
    __events: CollectionResource = None
    __nameservers: CollectionResource = None
    __whois: DictionaryResource[Whois] = None
    __geoloc: CollectionResource = None

    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)
        self.__reputation = CollectionResource(self, "reputation")
        self.__urls = CollectionResource(self, "urls")
        self.__samples = CollectionResource(self, "samples")
        self.__ips = CollectionResource(self, "ips")
        self.__events = CollectionResource(self, "events")
        self.__nameservers = CollectionResource(self, "nameservers")
        self.__whois = DictionaryResource[Whois](self, "whois", Whois)
        self.__geoloc = CollectionResource(self, "geoloc")

    @property
    def urls(self) -> CollectionResource:
        return self.__urls

    @property
    def reputation(self)  -> CollectionResource:
        return self.__reputation

    @property
    def samples(self)  -> CollectionResource:
        return self.__samples

    @property
    def ips(self) -> CollectionResource:
        return self.__ips

    @property
    def events(self) -> CollectionResource:
        return self.__events

    @property
    def nameservers(self) -> CollectionResource:
        return self.__nameservers

    @property
    def whois(self) -> DictionaryResource[Whois]:
        return self.__whois

    @property
    def geoloc(self) -> CollectionResource:
        return self.__geoloc
