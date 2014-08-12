# -*- coding: utf-8 -*

import collections

from .. import Matcher
from ...texts import plain_enumerate
from ... import _compat


class _StarEndWith(Matcher):
    def __init__(self, *args):
        self._args = args

    def _match(self, subject):
        if self._is_unordered(subject):
            return False

        return self._matches(subject)

    def _is_unordered(self, subject):
        return (isinstance(subject, collections.Mapping) and
                not isinstance(subject, collections.OrderedDict))

    def _match_negated(self, subject):
        if self._is_unordered(subject):
            return False

        return not self._matches(subject)

    def _description(self, subject):
        message = '{} {expected}'.format(type(self).__name__.replace('_', ' '),
                                         expected=plain_enumerate(self._args))

        if self._is_unordered(subject):
            message += ' but it does not have ordered keys'

        return message


class start_with(_StarEndWith):
    def _matches(self, subject):
        if isinstance(subject, _compat.string_types):
            return subject.startswith(self._args[0])
        return list(self._args) == list(subject)[:len(self._args)]


class end_with(_StarEndWith):
    def _matches(self, subject):
        if isinstance(subject, _compat.string_types):
            return subject.endswith(self._args[0])
        return (list(self._args) == list(subject)[-len(self._args):])
