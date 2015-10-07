# -*- coding: utf-8 -*

from .. import Matcher


class equal(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject == self._expected, []

    def _match_negated(self, subject):
        return subject != self._expected, []
