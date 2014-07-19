# -*- coding: utf-8 -*

import collections

from . import Matcher, plain_enumerate
from .. import _compat


class StartWith(Matcher):
    def _initialize(self, *args):
        self._args = args

    def _match(self, subject):
        if isinstance(subject, _compat.string_types):
            return subject.startswith(self._args[0])

        elif (isinstance(subject, collections.Mapping) and
              not isinstance(subject, collections.OrderedDict)):

            assert False, 'Expected {subject!r} to start with {expected} but it does not have ordered keys'.format(subject=subject, expected=plain_enumerate(self._args))
        else:
            return list(self._args) == list(subject)[:len(self._args)]

    @property
    def _description(self):
        return 'start with {expected}'.format(expected=plain_enumerate(self._args))
