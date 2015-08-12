# -*- coding: utf-8 -*

import collections

from .. import Matcher
from ...texts import plain_enumerate
from ... import _compat


class _StarEndWith(Matcher):
    def __init__(self, *args):
        self._args = args

    def _match(self, subject):
        if self._is_unordered_dict(subject):
            return False, ['does not have ordered keys']

        return self._matches(subject)

    def _is_unordered_dict(self, subject):
        if isinstance(subject, collections.Mapping):
            if not hasattr(collections, 'OrderedDict'):
                return True

            return not isinstance(subject, collections.OrderedDict)

        return False

    def _match_negated(self, subject):
        if self._is_unordered_dict(subject):
            return False, ['does not have ordered keys']

        result, reasons = self._matches(subject)
        return not result, reasons

    def __repr__(self):
        return '{0} {1}'.format(type(self).__name__.replace('_', ' '),
                                plain_enumerate(self._args))


class start_with(_StarEndWith):
    def _matches(self, subject):
        if isinstance(subject, _compat.string_types):
            return (
                subject.startswith(self._args[0]),
                ['starts with {0!r}'.format(subject[:-len(self._args[0])])])

        actual_start = list(subject)[:len(self._args)]
        return (
            list(self._args) == actual_start,
            ['starts with {0!r}'.format(actual_start)])


class end_with(_StarEndWith):
    def _matches(self, subject):
        if isinstance(subject, _compat.string_types):
            return (
                subject.endswith(self._args[0]),
                ['ends with {0!r}'.format(subject[-len(self._args[0]):])])

        actual_end = list(subject)[-len(self._args):]
        return (
            list(self._args) == actual_end,
            ['ends with {0!r}'.format(actual_end)])
