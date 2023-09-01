"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from requests import Response
from src.et_api.v1.resources.Dictionary import Dictionary


class Whois(Dictionary):
    def __init__(self, response: Response):
        super().__init__(response)

    @property
    def domain(self) -> str:
        return self.get_response().get('domain', None)

    @property
    def registrant_name(self) -> str:
        return self.get_response().get('registrant', {}).get('name', None)

    @property
    def registrant_email(self) -> str:
        return self.get_response().get('registrant', {}).get('email', None)

    @property
    def registrant_created(self) -> str:
        return self.get_response().get('registrant', {}).get('created', None)

    @property
    def registrant_updated(self) -> str:
        return self.get_response().get('registrant', {}).get('updated', None)

    @property
    def registrant_expires(self) -> str:
        return self.get_response().get('registrant', {}).get('expires', None)

    @property
    def registrar_name(self) -> str:
        return self.get_response().get('registrar', {}).get('name', None)

    @property
    def registrar_country(self) -> str:
        return self.get_response().get('registrar', {}).get('country', None)

    @property
    def registrar_website(self) -> str:
        return self.get_response().get('registrar', {}).get('website', None)

