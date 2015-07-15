# -*- coding: utf-8 -*

from .. import Matcher


class be(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject is self._expected, []
