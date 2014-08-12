# -*- coding: utf-8 -*

from .. import Matcher


class BeAnInstanceOf(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, subject):
        return isinstance(subject, self._expected)

    def _description(self, subject):
        return 'be an instance of {expected.__name__}'.format(expected=self._expected)


be_a = be_an = BeAnInstanceOf
