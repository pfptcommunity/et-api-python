"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from src.et_api.v1.resources.CategoryInfoCollection import CategoryInfoCollection
from src.et_api.web.Resource import Resource


class ReputationCategories(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def __call__(self) -> CategoryInfoCollection:
        return CategoryInfoCollection(self._session.get(self.uri))
