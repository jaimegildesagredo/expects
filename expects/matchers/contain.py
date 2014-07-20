# -*- coding: utf-8 -*

import collections

from . import Matcher, plain_enumerate


class Contain(Matcher):
    def __init__(self, *args):
        self._args = args

    def _match(self, subject):
        if isinstance(subject, collections.Iterator):
            collection = list(subject)
        else:
            collection = subject

        for arg in self._args:
            if arg not in collection:
                return False

        return True

    def _description(self, subject):
        return 'contain {expected}'.format(expected=plain_enumerate(self._args))
