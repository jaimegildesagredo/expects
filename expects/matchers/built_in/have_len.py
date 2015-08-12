# -*- coding: utf-8 -*

from .. import Matcher, default_matcher


class have_length(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, subject):
        expected_length = default_matcher(self._expected)
        actual_length = self.__length(subject)
        result, _ = expected_length._match(actual_length)
        return result, ['was {0!r}'.format(actual_length)]

    def __length(self, collection):
        try:
            return len(collection)
        except TypeError:
            return sum(1 for i in collection)


class have_len(have_length):
    pass
