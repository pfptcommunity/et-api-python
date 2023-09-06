"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from requests import Response

from et_api.v1.resources.Collection import Collection
from et_api.v1.resources.SampleInfo import SampleInfo


class SampleInfoCollection(Collection[SampleInfo]):
    def __init__(self, response: Response):
        super().__init__(response)
        for idx, x in enumerate(self):
            self[idx] = SampleInfo(x)
