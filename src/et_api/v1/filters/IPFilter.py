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

    @property
    def sort_by(self) -> SortBy:
        return self._options[self.__SORT_BY]

    @sort_by.setter
    def sort_by(self, by: SortBy):
        assert isinstance(by, SortBy)
        self._options[self.__SORT_BY] = by

    def set_sort_by(self, by: SortBy) -> TFilterOptions:
        self.sort_by = by
        return self

    @property
    def sort_direction(self) -> SortOrder:
        return self._options[self.__SORT_ORDER]

    @sort_direction.setter
    def sort_direction(self, order: SortOrder):
        assert isinstance(order, SortOrder)
        self._options[self.__SORT_ORDER] = order

    def set_sort_direction(self, order: SortOrder) -> TFilterOptions:
        self.sort_direction = order
        return self
