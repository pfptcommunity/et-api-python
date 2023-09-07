"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from requests.adapters import HTTPAdapter
from requests.adapters import Retry

from et_api.v1.resources.CategoryInfo import CategoryInfo
from et_api.web.DictionaryCollection import DictionaryCollection
from et_api.web.ErrorHandler import ErrorHandler
from src.et_api.v1.endpoints import *
from src.et_api.web.Resource import Resource


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
    __domains: Domains
    __ips: IPs
    __samples: Samples
    __sids: Sids

    def __init__(self, api_token: str):
        super().__init__(None, "https://api.emergingthreats.net/v1/")
        self.__api_token = api_token
        retries = Retry(total=20, backoff_factor=1, status_forcelist=[429, 408])
        self.session.mount('https://', TimeoutHTTPAdapter(max_retries=retries))
        self.session.headers.update({'Authorization': api_token})
        self.__error_handler = ErrorHandler()
        self.session.hooks = {"response": self.__error_handler.handler}
        self.__reputation_categories = DictionaryCollection[CategoryInfo](self, "repcategories", CategoryInfo)
        self.__domains = Domains(self, "domains")
        self.__ips = IPs(self, "ips")
        self.__samples = Samples(self, "samples")
        self.__sids = Sids(self, "sids")

    @property
    def reputation_categories(self) -> DictionaryCollection[CategoryInfo]:
        return self.__reputation_categories

    @property
    def domains(self) -> Domains:
        return self.__domains

    @property
    def ips(self) -> IPs:
        return self.__ips

    @property
    def samples(self) -> Samples:
        return self.__samples

    @property
    def sids(self) -> Sids:
        return self.__sids

    @property
    def timeout(self):
        return self.session.adapters.get('https://').timeout

    @timeout.setter
    def timeout(self, timeout):
        self.session.adapters.get('https://').timeout = timeout

    @property
    def error_handler(self) -> ErrorHandler:
        return self.__error_handler

    @error_handler.setter
    def error_handler(self, error_handler: ErrorHandler):
        self.__error_handler = error_handler
