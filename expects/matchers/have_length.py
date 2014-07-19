# -*- coding: utf-8 -*

from . import Matcher


class HaveLength(Matcher):
    def _initialize(self, expected):
        self._expected = expected

    def _match(self, subject):
        return self.__length(subject) == self._expected

    def __length(self, collection):
        try:
            return len(collection)
        except TypeError:
            return sum(1 for i in collection)

    @property
    def _description(self):
        return 'have length {expected}'.format(expected=self._expected)
