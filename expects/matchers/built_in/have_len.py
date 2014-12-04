# -*- coding: utf-8 -*

from .. import Matcher


class have_length(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, subject):
        return self._match_value(self._expected, self.__length(subject))

    def __length(self, collection):
        try:
            return len(collection)
        except TypeError:
            return sum(1 for i in collection)


class have_len(have_length):
    pass
