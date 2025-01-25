"""
Author: Ludvik Jerabek
Package: et-api
License: MIT
"""
from et_api.v1.resources.domain_info import DomainInfo
from et_api.v1.resources.sample_info import SampleInfo
from et_api.v1.resources.sid_doc_info import SigDocInfo
from et_api.v1.resources.sig_ip_info import SigIPInfo
from et_api.v1.resources.sig_info import SigInfo
from et_api.v1.resources.sig_name_info import SigNameInfo
from et_api.v1.resources.sig_ref_info import SigRefInfo
from et_api.web.dictionary_collection import DictionaryCollection
from et_api.web.dictionary_resource import DictionaryResource


class Sid(DictionaryResource[SigNameInfo]):
    __ips: SigIPInfo
    __domains: DictionaryCollection[DomainInfo]
    __samples: DictionaryCollection[SampleInfo]
    __signature_info: DictionaryResource[SigInfo]
    __documentation: DictionaryResource[SigDocInfo]
    __references: DictionaryCollection[SigRefInfo]

    def __init__(self, parent, uri: str):
        super().__init__(parent, uri, SigNameInfo)
        self.__ips = SigIPInfo(self, "ips")
        self.__domains = DictionaryCollection[DomainInfo](self, "domains", DomainInfo)
        self.__samples = DictionaryCollection[SampleInfo](self, "samples", SampleInfo)
        self.__signature_info = DictionaryResource[SigInfo](self, "text", SigInfo)
        self.__documentation = DictionaryResource[SigDocInfo](self, "documentation", SigDocInfo)
        self.__references = DictionaryCollection[SigRefInfo](self, "references", SigRefInfo)

    @property
    def ips(self) -> SigIPInfo:
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
