"""
This code was tested against Python 3.9
 
Author: Ludvik Jerabek
Package: et_api
Version: 0.1.0
License: MIT
"""
from et_api import Version
from et_api.endpoints.Repcategories import Repcategories
from et_api.endpoints.Domains import Domains
from et_api.endpoints.IPs import IPs
from et_api.web.Resource import Resource
from requests import Response

class Client(Resource):
    __api_token: str
    __version: Version
    __repcategories: Repcategories = None
    __domains: Domains = None
    __ips: IPs = None

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
        return response

    def __init__(self, version: Version, api_token: str):
        super().__init__(None, "https://api.emergingthreats.net/{}/".format(version.value))
        self._session.hooks = {"response": self.__session_hook}
        self.__version = version
        self.__api_token = api_token
        self._session.headers.update({'Authorization': api_token})
        self.__repcategories = Repcategories(self, "repcategories")
        self.__domains = Domains(self, "domains")
        self.__ips = Domains(self, "ips")

    @property
    def token(self):
        return self.__api_token

    @property
    def version(self):
        return self.__version.value

    @property
    def repcategories(self):
        return self.__repcategories

    @property
    def domains(self):
        return self.__domains

    @property
    def ips(self):
        return self.__ips
