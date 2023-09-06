"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from requests import Response

from et_api.v1.resources.WhoisRegistrant import WhoisRegistrant
from et_api.v1.resources.WhoisRegistrar import WhoisRegistrar
from src.et_api.v1.resources.Dictionary import Dictionary


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
