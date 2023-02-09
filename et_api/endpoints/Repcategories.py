"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
Version: 0.1.0
License: MIT
"""
from et_api.resources.Collection import Collection
from et_api.rest.Resource import Resource


class Repcategories(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def __call__(self) -> Collection:
        return Collection(self._session.get(self.uri))
