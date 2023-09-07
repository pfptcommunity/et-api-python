"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from et_api.v1.resources.CategoryInfo import CategoryInfo
from et_api.web.DictionaryCollection import DictionaryCollection
from src.et_api.web.Resource import Resource


class ReputationCategories(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def __call__(self) -> DictionaryCollection[CategoryInfo]:
        return DictionaryCollection[CategoryInfo](self.session.get(self.uri))
