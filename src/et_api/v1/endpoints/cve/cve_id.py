from et_api.web import DictionaryResource
from .cve_info import CVEInfo


class CVEId(DictionaryResource[CVEInfo]):
    def __init__(self, parent, uri: str):
        super().__init__(parent, uri, CVEInfo)
