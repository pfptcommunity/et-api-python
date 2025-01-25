"""
Author: Ludvik Jerabek
Package: et-api
License: MIT
"""
from datetime import datetime
from enum import Enum
from typing import TypeVar, Dict

TFilterOptions = TypeVar('TFilterOptions', bound='FilterOptions')


class FilterOptions:
    _options: dict[str]

    def __init__(self):
        self._options = {}

    def clear(self):
        self._options.clear()

    def __str__(self) -> str:
        param = ''
        for k, v in self._options.items():
            if type(v) == list:
                if len(v):
                    if all(isinstance(n, str) for n in v):
                        param += "{}{}=[{}]".format(('', '&')[len(param) > 0], k, ','.join(v))
                    elif all(isinstance(n, Enum) for n in v):
                        param += "{}{}=[{}]".format(('', '&')[len(param) > 0], k, ','.join([n.value for n in v]))
            elif type(v) == datetime:
                param += "{}{}=[{}]".format(('', '&')[len(param) > 0], k, v.strftime('%Y-%m-%dT%H:%M:%S'))
            elif isinstance(v, Enum):
                param += "{}{}={}".format(('', '&')[len(param) > 0], k, v.value)
            else:
                param += "{}{}={}".format(('', '&')[len(param) > 0], k, v)
        return param

    @property
    def params(self) -> Dict:
        param = {}
        for k, v in self._options.items():
            if type(v) == list:
                if len(v):
                    if all(isinstance(n, str) for n in v):
                        param[k] = "[{}]".format(','.join(v))
                    elif all(isinstance(n, Enum) for n in v):
                        param[k] = "[{}]".format(','.join([n.value for n in v]))
            elif type(v) == datetime:
                param[k] = "[{}]".format(v.strftime('%Y-%m-%dT%H:%M:%S'))
            elif isinstance(v, Enum):
                param[k] = v.value
            else:
                param[k] = v
        return param
