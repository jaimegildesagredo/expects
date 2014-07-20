# -*- coding: utf-8 -*

import collections

from . import Matcher, plain_enumerate
from .. import _compat


class EndWith(Matcher):
    def __init__(self, *args):
        self._args = args

    def _match(self, subject):
        if isinstance(subject, _compat.string_types):
            return subject.endswith(self._args[0])

        elif (isinstance(subject, collections.Mapping) and
              not isinstance(subject, collections.OrderedDict)):

            assert False, 'Expected {subject!r} to end with {expected} but it does not have ordered keys'.format(subject=subject, expected=plain_enumerate(self._args))
        else:
            return (list(self._args) ==
                    list(reversed(list(subject)[-len(self._args):])))

    def _description(self, subject):
        return 'end with {expected}'.format(expected=plain_enumerate(self._args))
