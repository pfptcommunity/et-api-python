"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from et_api.v1.resources.DomainInfo import DomainInfo
from et_api.v1.resources.IPInfoEx import IPInfoEx
from et_api.v1.resources.SampleInfo import SampleInfo
from et_api.v1.resources.SidDocInfo import SigDocInfo
from et_api.v1.resources.SigRefInfo import SigRefInfo
from et_api.v1.resources.SigInfo import SigInfo
from et_api.web.DictionaryCollection import DictionaryCollection
from src.et_api.v1.resources.SidInfo import SidInfo
from src.et_api.web.DictionaryResource import DictionaryResource


class Sid(DictionaryResource[SidInfo]):
    __ips: DictionaryCollection[IPInfoEx]
    __domains: DictionaryCollection[DomainInfo]
    __samples: DictionaryCollection[SampleInfo]
    __signature_info: DictionaryResource[SigInfo]
    __documentation: DictionaryResource[SigDocInfo]
    __references: DictionaryCollection[SigRefInfo]

    def __init__(self, parent, uri: str):
        super().__init__(parent, uri, SidInfo)
        self.__ips = DictionaryCollection[IPInfoEx](self, "ips", IPInfoEx)
        self.__domains = DictionaryCollection[DomainInfo](self, "domains", DomainInfo)
        self.__samples = DictionaryCollection[SampleInfo](self, "samples", SampleInfo)
        self.__signature_info = DictionaryResource[SigInfo](self, "text", SigInfo)
        self.__documentation = DictionaryResource[SigDocInfo](self, "documentation", SigDocInfo)
        self.__references = DictionaryCollection[SigRefInfo](self, "references", SigRefInfo)

    @property
    def ips(self) -> DictionaryCollection[IPInfoEx]:
        return self.__ips

    @property
    def domains(self) -> DictionaryCollection[DomainInfo]:
        return self.__domains

    @property
    def samples(self) -> DictionaryCollection[SampleInfo]:
        return self.__samples

    @property
    def signature(self) -> DictionaryResource[SigInfo]:
        return self.__signature_info

    @property
    def documentation(self) -> DictionaryResource[SigDocInfo]:
        return self.__documentation

    @property
    def references(self) -> DictionaryCollection[SigRefInfo]:
        return self.__references
