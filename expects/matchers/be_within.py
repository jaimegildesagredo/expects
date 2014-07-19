# -*- coding: utf-8 -*

from . import Matcher


class BeWithIn(Matcher):
    def _initialize(self, start, stop):
        self._start = start
        self._stop = stop

    def _match(self, subject):
        return subject in range(self._start, self._stop)

    @property
    def _description(self):
        return 'be within {start} and {stop}'.format(start=self._start, stop=self._stop)
