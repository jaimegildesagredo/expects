# -*- coding: utf-8 -*

from .. import Matcher


class be_within(Matcher):
    def __init__(self, start, stop):
        self._start = start
        self._stop = stop

    def _match(self, subject):
        return self._start < subject < self._stop, []

    def __repr__(self):
        return 'be within {start} and {stop}'.format(start=self._start, stop=self._stop)
