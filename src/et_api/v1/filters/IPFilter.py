"""
This code was tested against Python 3.9

Author: Ludvik Jerabek
Package: et-api
License: MIT
"""
from et_api.common import *
from et_api.web.FilterOptions import FilterOptions, TFilterOptions


class IPFilter(FilterOptions):
    __SORT_BY = 'sortBy'
    __SORT_ORDER = 'sortDirection'

    def __init__(self):
        super().__init__()

    def set_sort_by(self, by: SortBy) -> TFilterOptions:
        self._options[self.__SORT_BY] = by
        return self

    def get_sort_by(self) -> SortBy:
        return self._options[self.__SORT_BY]

    def set_sort_direction(self, order: SortOrder) -> TFilterOptions:
        self._options[self.__SORT_ORDER] = order
        return self

    def get_sort_direction(self) -> SortOrder:
        return self._options[self.__SORT_ORDER]
