# -*- coding: utf-8 -*

import re

from .. import Matcher


class match(Matcher):
    def __init__(self, expected, *args):
        self._expected = expected
        self._args = args

    def _match(self, subject):
        return self.__matches(subject), []

    def __matches(self, subject):
        return True if re.search(self._expected, subject, *self._args) is not None else False
