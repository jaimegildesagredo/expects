# -*- coding: utf-8 -*

from .. import Matcher


class HaveLength(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, subject):
        return self.__length(subject) == self._expected

    def __length(self, collection):
        try:
            return len(collection)
        except TypeError:
            return sum(1 for i in collection)

    def _description(self, subject):
        return 'have length {expected}'.format(expected=self._expected)
