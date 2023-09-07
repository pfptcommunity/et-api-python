"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: et_api
License: MIT
"""

from requests import Response
from requests.adapters import HTTPAdapter
from requests.adapters import Retry

from et_api.v1.resources.CategoryInfo import CategoryInfo
from et_api.web.DictionaryCollection import DictionaryCollection
from src.et_api.v1.endpoints import *
from src.et_api.web.Resource import Resource


class TimeoutHTTPAdapter(HTTPAdapter):
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
    __raise_for_status: bool
    __reputation_categories: DictionaryCollection[CategoryInfo]
    __domains: Domains
    __ips: IPs
    __samples: Samples
    __sids: Sids

    def __session_hook(self, response: Response, **kwargs) -> Response:
        if response.status_code == 401:
            response.reason = "Unauthorized -- You did not provide an API key"
        elif response.status_code == 403:
            response.reason = "Forbidden -- The API key does not have access to the requested action or your subscription has elapsed."
        elif response.status_code == 404:
            response.reason = "Not Found -- The requested action does not exist."
        elif response.status_code == 408:
            response.reason = "Request Timeout -- The request took too long to complete on our side. Please reduce the amount of information you are requesting, or try again later."
        elif response.status_code == 429:
            response.reason = "Request Timeout -- The request took too long to complete on our side. Please reduce the amount of information you are requesting, or try again later."
        elif response.status_code == 500:
            response.reason = "Internal Server Error -- We had a problem internal to our systems. Please try again later."

        if self.__raise_for_status:
            response.raise_for_status()

        return response

    def __init__(self, api_token: str, raise_for_status: bool = False):
        super().__init__(None, "https://api.emergingthreats.net/v1/")
        self.__api_token = api_token
        self.__raise_for_status = raise_for_status
        retries = Retry(total=20, backoff_factor=1, status_forcelist=[429, 408])
        self._session.mount('https://', TimeoutHTTPAdapter(max_retries=retries))
        self._session.hooks = {"response": self.__session_hook}
        self._session.headers.update({'Authorization': api_token})
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
