# -*- coding: utf-8 -*

from .. import Matcher


class equal_values(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject.__dict__ == self._expected.__dict__, []

    def _match_negated(self, subject):
        return subject.__dict__ != self._expected.__dict__, []
