# -*- coding: utf-8 -*

from . import Matcher


class Be(Matcher):
    def _initialize(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject is self._expected

    @property
    def _description(self):
        return 'be {expected!r}'.format(expected=self._expected)
