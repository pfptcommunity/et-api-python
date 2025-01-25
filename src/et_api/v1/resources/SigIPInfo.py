"""
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from et_api.v1.filters.IPFilter import IPFilter
from et_api.v1.resources.IPInfoEx import IPInfoEx
from et_api.web import Resource
from et_api.web.Collection import Collection


class SigIPInfo(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def __call__(self, options: IPFilter = IPFilter()) -> Collection[IPInfoEx]:
        collection = Collection[IPInfoEx](self.session.get(self.uri, params=options.params))
        for idx, x in enumerate(collection):
            collection[idx] = IPInfoEx(x)
        return collection
