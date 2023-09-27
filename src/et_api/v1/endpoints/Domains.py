"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from src.et_api.v1.endpoints.Domain import Domain
from src.et_api.web.Resource import Resource


class Domains(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def __getitem__(self, domain: str) -> Domain:
        return Domain(self, domain.casefold().strip())
