# -*- coding: utf-8 -*

from .. import Matcher


class equal(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject == self._expected, []

    def _match_negated(self, subject):
        return subject != self._expected, []

    def within(self, tolerance):
        return equal_within(self._expected, tolerance)


class equal_within(Matcher):
    def __init__(self, expected, tolerance):
        self._expected = expected
        self._tolerance = tolerance

    def _match(self, subject):
        difference = abs(self._expected - subject)
        return difference < self._tolerance, []

    def __repr__(self):
        return 'equal {0} ± {1}'.format(self._expected, self._tolerance)
