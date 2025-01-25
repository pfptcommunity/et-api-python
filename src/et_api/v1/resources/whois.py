"""
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from requests import Response

from et_api.v1.resources.whois_registrant import WhoisRegistrant
from et_api.v1.resources.whois_registrar import WhoisRegistrar
from et_api.web.dictionary import Dictionary


class Whois(Dictionary):
    def __init__(self, response: Response):
        super().__init__(response)
        self['registrant'] = WhoisRegistrant(self.get('registrant', {}))
        self['registrar'] = WhoisRegistrant(self.get('registrar', {}))

    @property
    def domain(self) -> str:
        return self.get('domain', None)

    @property
    def registrant(self) -> WhoisRegistrant:
        return self.get('registrant')

    @property
    def registrar(self) -> WhoisRegistrar:
        return self.get('registrar')
