"""
Author: Ludvik Jerabek
Package: et-api
License: MIT
"""
from typing import Dict


class IDSEventInfo(Dict):
    def __init__(self, data: Dict):
        super().__init__(data)

    @property
    def source(self) -> str:
        return self.get('source', None)

    @property
    def date(self) -> str:
        return self.get('date', None)

    @property
    def sid(self) -> str:
        return self.get('sid', None)

    @property
    def source_ip(self) -> str:
        return self.get('source_ip', None)

    @property
    def destination_ip(self) -> str:
        return self.get('destination_ip', None)

    @property
    def source_port(self) -> str:
        return self.get('source_port', None)

    @property
    def destination_port(self) -> str:
        return self.get('destination_port', None)

    @property
    def revision(self) -> str:
        return self.get('revision', None)

    @property
    def signature_name(self) -> str:
        return self.get('signature_name', None)
