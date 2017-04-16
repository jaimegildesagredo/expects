# -*- coding: utf-8 -*

from numbers import Number

from .. import Matcher


class be(Matcher):
    def __init__(self, expected):
        self._expected = expected
        self.is_number = isinstance(expected, Number)

    def _match(self, subject):
        if self.is_number:
            return isinstance(subject, type(self._expected)) \
                and subject == self._expected, []
        return subject is self._expected, []
