# -*- coding: utf-8 -*

import collections

from .matcher import Matcher, plain_enumerate
from .. import _compat


class ContainOnly(Matcher):
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

        if isinstance(subject, _compat.string_types):
            args_length = len(''.join(self._args))
        else:
            args_length = len(self._args)

        return len(subject) == args_length

    def _description(self, subject):
        return 'contain only {expected}'.format(expected=plain_enumerate(self._args))
