"""
Author: Ludvik Jerabek
Package: tap_api
License: MIT
"""
from requests import Response


class ResponseWrapper:
    """
    Mixin for managing an HTTP response, providing utilities for status,
    reason, and access to the raw response.
    """

    def __init__(self, response: Response):
        """
        Initializes the ResponseWrapper with a response.

        Args:
            response (Response): The HTTP response object to wrap.
        """
        self._response: Response = response

    def get_status(self) -> int:
        """
        Returns the HTTP status code from the response.

        Returns:
            int: The HTTP status code.
        """
        return self._response.status_code

    def get_reason(self) -> str:
        """
        Returns the HTTP reason phrase from the response.

        Returns:
            str: The HTTP reason phrase.
        """
        return self._response.reason

    def get_response(self) -> Response:
        """
        Returns the original HTTP response object.

        Returns:
            Response: The HTTP response object.
        """
        return self._response
