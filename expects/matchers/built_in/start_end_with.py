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
            return False, ['does not have ordered keys']

        return self._matches(subject)

    def _is_unordered(self, subject):
        return (isinstance(subject, collections.Mapping) and
                not isinstance(subject, collections.OrderedDict))

    def _match_negated(self, subject):
        if self._is_unordered(subject):
            return False, ['does not have ordered keys']

        result, reasons = self._matches(subject)
        return not result, reasons

    def __repr__(self):
        return '{} {expected}'.format(type(self).__name__.replace('_', ' '),
                                      expected=plain_enumerate(self._args))


class start_with(_StarEndWith):
    def _matches(self, subject):
        if isinstance(subject, _compat.string_types):
            return (
                subject.startswith(self._args[0]),
                ['starts with {!r}'.format(subject[:-len(self._args[0])])])

        actual_start = list(subject)[:len(self._args)]
        return (
            list(self._args) == actual_start,
            ['starts with {!r}'.format(actual_start)])


class end_with(_StarEndWith):
    def _matches(self, subject):
        if isinstance(subject, _compat.string_types):
            return (
                subject.endswith(self._args[0]),
                ['ends with {!r}'.format(subject[-len(self._args[0]):])])

        actual_end = list(subject)[-len(self._args):]
        return (
            list(self._args) == actual_end,
            ['ends with {!r}'.format(actual_end)])
