"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
Version: 0.1.0
License: MIT
"""
from et_api.web.Collection import Collection
from et_api.web.Resource import Resource


class IP(Resource):
    __reputation: Resource = None
    __urls: Resource = None
    __samples: Resource = None
    __ips: Resource = None
    __events: Resource = None
    __nameservers: Resource = None
    __whois: Resource = None
    __geoloc: Resource = None

    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)
        self.__reputation = Resource(self, "reputation")
        self.__urls = Resource(self, "urls")
        self.__samples = Resource(self, "samples")
        self.__ips = Resource(self, "ips")
        self.__events = Resource(self, "events")
        self.__nameservers = Resource(self, "nameservers")
        self.__whois = Resource(self, "whois")
        self.__geoloc = Resource(self, "geoloc")

    def urls(self) -> Collection:
        return Collection(self._session.get(self.__urls.uri))

    def reputation(self):
        r = self.session.get(self.__reputation.uri)
        r.raise_for_status()
        return r.json()

    def samples(self):
        r = self.session.get(self.__samples.uri)
        r.raise_for_status()
        return r.json()

    def ips(self):
        r = self.session.get(self.__ips.uri)
        r.raise_for_status()
        return r.json()

    def events(self):
        r = self.session.get(self.__events.uri)
        r.raise_for_status()
        return r.json()

    def nameservers(self):
        r = self.session.get(self.__nameservers.uri)
        r.raise_for_status()
        return r.json()

    def whois(self):
        r = self.session.get(self.__whois.uri)
        r.raise_for_status()
        return r.json()

    def geoloc(self):
        r = self.session.get(self.__geoloc.uri)
        r.raise_for_status()
        return r.json()
