# -*- coding: utf-8 -*

import collections

from .. import Matcher
from ...texts import plain_enumerate
from ... import _compat


class contain(Matcher):
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
        return '{} {expected}'.format(type(self).__name__.replace('_', ' '),
                                      expected=plain_enumerate(self._args))


class contain_exactly(contain):
    def _match(self, subject):
        if not super(contain_exactly, self)._match(subject):
            return False

        return len(subject) == self._args_length(subject)

    def _args_length(self, subject):
        if isinstance(subject, _compat.string_types):
            return len(''.join(self._args))
        return len(self._args)
