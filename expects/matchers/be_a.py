# -*- coding: utf-8 -*

from . import Matcher


class BeAnInstanceOf(Matcher):
    def _initialize(self, expected):
        self._expected = expected

    def _match(self, subject):
        return isinstance(subject, self._expected)

    @property
    def _description(self):
        return 'be an instance of {expected.__name__}'.format(expected=self._expected)
