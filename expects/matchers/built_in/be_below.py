# -*- coding: utf-8 -*

from .. import Matcher


class be_below(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject < self._expected, []


class below(be_below):
    pass
