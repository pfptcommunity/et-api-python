"""
Author: Ludvik Jerabek
Package: et-api
License: MIT
"""
from requests.adapters import HTTPAdapter
from requests.adapters import Retry

from et_api.v1.endpoints.domain import Domain
from et_api.v1.endpoints.ip import IP
from et_api.v1.endpoints.sample import Sample
from et_api.v1.endpoints.sid import Sid
from et_api.v1.resources.category_info import CategoryInfo
from et_api.web.dictionary_collection import DictionaryCollection
from et_api.web.error_handler import ErrorHandler
from et_api.web.resource import Resource
from et_api.web.resources import Resources


class TimeoutHTTPAdapter(HTTPAdapter):
    timeout = None

    def __init__(self, *args, **kwargs):
        if "timeout" in kwargs:
            self.timeout = kwargs["timeout"]
            del kwargs["timeout"]
        super().__init__(*args, **kwargs)

    def send(self, request, **kwargs):
        timeout = kwargs.get("timeout")
        if timeout is None and hasattr(self, 'timeout'):
            kwargs["timeout"] = self.timeout
        return super().send(request, **kwargs)


class Client(Resource):
    __api_token: str
    __error_handler: ErrorHandler
    __reputation_categories: DictionaryCollection[CategoryInfo]
    __domains: Resources[Domain]
    __ips: Resources[IP]
    __samples: Resources[Sample]
    __sids: Resources[Sid]

    def __init__(self, api_token: str):
        super().__init__(None, "https://api.emergingthreats.net/v1/")
        self.__api_token = api_token
        retries = Retry(total=20, backoff_factor=1, status_forcelist=[429, 408])
        self._session.mount('https://', TimeoutHTTPAdapter(max_retries=retries))
        self._session.headers.update({'Authorization': api_token})
        self.__error_handler = ErrorHandler()
        self._session.hooks = {"response": self.__error_handler.handler}
        self.__reputation_categories = DictionaryCollection[CategoryInfo](self, "repcategories", CategoryInfo)
        self.__domains = Resources[Domain](self, "domains", Domain)
        self.__ips = Resources[IP](self, "ips", IP)
        self.__samples = Resources[Sample](self, "samples", Sample)
        self.__sids = Resources[Sid](self, "sids", Sid)

    @property
    def reputation_categories(self) -> DictionaryCollection[CategoryInfo]:
        return self.__reputation_categories

    @property
    def domains(self) -> Resources[Domain]:
        return self.__domains

    @property
    def ips(self) -> Resources[IP]:
        return self.__ips

    @property
    def samples(self) -> Resources[Sample]:
        return self.__samples

    @property
    def sids(self) -> Resources[Sid]:
        return self.__sids

    @property
    def timeout(self):
        return self._session.adapters.get('https://').timeout

    @timeout.setter
    def timeout(self, timeout):
        self._session.adapters.get('https://').timeout = timeout

    @property
    def error_handler(self) -> ErrorHandler:
        return self.__error_handler

    @error_handler.setter
    def error_handler(self, error_handler: ErrorHandler):
        self.__error_handler = error_handler
