"""
Author: Ludvik Jerabek
Package: et-api
License: MIT
"""
from enum import Enum


class SortBy(Enum):
    IP = 'ip'
    LAST_SEEN = 'last_seen'
