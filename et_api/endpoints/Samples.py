"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
Version: 0.1.0
License: MIT
"""
from et_api.endpoints.Sample import Sample
from et_api.web.Resource import Resource


class Samples(Resource):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri)

    def __call__(self, md5: str) -> Sample:
        return Sample(self, md5.casefold().strip())
