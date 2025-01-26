from et_api.web import Resources

from .cve_id import CVEId


class CVE(Resources[CVEId]):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri, CVEId)
