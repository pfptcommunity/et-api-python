"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et_api
License: MIT
"""
from requests import Response


class ErrorHandler:
    __raise_for_status: bool

    def __init__(self, raise_for_status: bool = False):
        self.__raise_for_status = raise_for_status

    def handler(self, response: Response, *args, **kwargs) -> Response:
        if response.status_code == 401:
            response.reason = "Unauthorized -- You did not provide an API key"
        elif response.status_code == 403:
            response.reason = "Forbidden -- The API key does not have access to the requested action or your subscription has elapsed."
        elif response.status_code == 404:
            response.reason = "Not Found -- The requested action does not exist."
        elif response.status_code == 408:
            response.reason = "Request Timeout -- The request took too long to complete on our side. Please reduce the amount of information you are requesting, or try again later."
        elif response.status_code == 429:
            response.reason = "Rate Limit Exceeded -- You have exceeded your provisioned rate limit. If this becomes a regular occurrence, please contact sales to have your rate limit increased."
        elif response.status_code == 500:
            response.reason = "Internal Server Error -- We had a problem internal to our systems. Please try again later."

        if self.__raise_for_status:
            response.raise_for_status()

        return response

    @property
    def raise_for_status(self) -> bool:
        return self.__raise_for_status

    @raise_for_status.setter
    def raise_for_status(self, raise_for_status: bool):
        self.__raise_for_status = raise_for_status
