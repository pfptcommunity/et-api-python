"""
Author: Ludvik Jerabek
Package: et-api
License: MIT
"""


class ConnectionInfo(dict):
    def __init__(self, data: dict):
        super().__init__(data)

    @property
    def source(self) -> str:
        return self.get('source', None)

    @property
    def date(self) -> str:
        return self.get('date', None)

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
    def bytes_down(self) -> str:
        return self.get('bytes_down', None)

    @property
    def bytes_up(self) -> str:
        return self.get('bytes_up', None)

    @property
    def bytes_total(self) -> str:
        return self.get('bytes_total', None)

    @property
    def packets_down(self) -> str:
        return self.get('packets_down', None)

    @property
    def packets_up(self) -> str:
        return self.get('packets_up', None)

    @property
    def packets_total(self) -> str:
        return self.get('packets_total', None)

    @property
    def protocol(self) -> str:
        return self.get('protocol', None)
