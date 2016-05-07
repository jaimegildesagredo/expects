# -*- coding: utf-8 -*

import functools
import collections

from .. import Matcher, default_matcher
from ...texts import plain_enumerate
from ... import _compat


class contain(Matcher):
    _NON_NORMALIZED_SEQUENCE_TYPES = (
        collections.Iterator,
        collections.MappingView,
        collections.Set
    )

    def __init__(self, *expected):
        self._expected = expected

    def _normalize_sequence(method):
        @functools.wraps(method)
        def wrapper(self, subject):
            if isinstance(subject, self._NON_NORMALIZED_SEQUENCE_TYPES):
                subject = list(subject)

            return method(self, subject)
        return wrapper

    @_normalize_sequence
    def _match(self, subject):
        if self._is_not_a_sequence(subject):
            return False, ['is not a valid sequence type']

        return self._matches(subject)

    def _is_not_a_sequence(self, value):
        return not isinstance(value, collections.Sequence)

    def _matches(self, subject):
        reasons = []
        for expected_item in self._expected:
            matches_any, reason = self._matches_any(expected_item, subject)

            if not matches_any:
                return False, [reason]
            else:
                reasons.append(reason)

        return True, reasons

    def _matches_any(self, expected, subject):
        if len(subject) == 0:
            return False, 'is empty'

        if isinstance(subject, _compat.string_types):
            if expected in subject:
                return True, 'item {0!r} found'.format(expected)
            return False, 'item {0!r} not found'.format(expected)

        expected = default_matcher(expected)
        for item in subject:
            matches, _ = expected._match(item)
            if matches:
                return True, 'item {0!r} found'.format(expected)

        return False, 'item {0!r} not found'.format(expected)

    @_normalize_sequence
    def _match_negated(self, subject):
        if self._is_not_a_sequence(subject):
            return False, ['is not a valid sequence type']

        ok, message = self._matches(subject)

        return not ok, message

    def __repr__(self):
        return '{0} {1}'.format(type(self).__name__.replace('_', ' '),
                                plain_enumerate(self._expected))


class contain_exactly(contain):
    def _matches(self, subject):
        if isinstance(subject, _compat.string_types):
            return self.__match_string(subject)

        reasons = []
        try:
            for index, expected_item in enumerate(self._expected):
                expected_item = default_matcher(expected_item)
                result, _ = expected_item._match(subject[index])
                if not result:
                    return False, ['item {0!r} not found at index {1}'.format(expected_item, index)]
                else:
                    reasons.append('item {0!r} found at index {1}'.format(expected_item, index))
        except IndexError:
            return False, ['item {0!r} not found at index {1}'.format(expected_item, index)]

        if len(subject) != len(reasons):
            return False, ['have a different length']
        return True, reasons

    def __match_string(self, subject):
        reasons = []
        index = 0
        for part in self._expected:
            if part != subject[index:index+len(part)]:
                return False, ['item equal {0!r} not found at index {1}'.format(part, index)]
            else:
                reasons.append('item equal {0!r} found at index {1}'.format(part, index))
            index = len(part)

        if len(subject) != len(''.join(self._expected)):
            return False, ['have a different length']
        return True, reasons


class contain_only(contain):
    def _matches(self, subject):
        if isinstance(subject, _compat.string_types):
            return self.__match_string(subject)

        result, reason = super(contain_only, self)._matches(subject)
        if not result:
            return False, reason

        if len(subject) != len(self._expected):
            return False, ['have a different length']
        return True, reason

    def __match_string(self, subject):
        reasons = []
        for item in self._expected:
            if not item in subject:
                return False, ['item {0!r} not found'.format(item)]
            else:
                reasons.append('item {0!r} found'.format(item))

        if len(subject) != len(''.join(self._expected)):
            return False, ['have a different length']
        return True, reasons
