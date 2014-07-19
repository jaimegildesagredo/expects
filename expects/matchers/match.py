# -*- coding: utf-8 -*

import re

from . import Matcher


class Match(Matcher):
    def _initialize(self, expected, *args):
        self._expected = expected
        self._args = args

    def _match(self, subject):
        return True if re.match(self._expected, subject, *self._args) is not None else False

    @property
    def _description(self):
        # TODO: Add self._args to failure message
        return 'match {expected!r}'.format(expected=self._expected)
