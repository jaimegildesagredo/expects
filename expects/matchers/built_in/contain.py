# -*- coding: utf-8 -*

import functools
import collections

from .. import Matcher
from ...texts import plain_enumerate
from ... import _compat


class contain(Matcher):
    def __init__(self, *expected):
        self._expected = expected

    def _normalize_subject(method):
        @functools.wraps(method)
        def wrapper(self, subject):
            if isinstance(subject, collections.Iterator):
                subject = list(subject)

            return method(self, subject)
        return wrapper

    @_normalize_subject
    def _match(self, subject):
        if self._is_not_a_sequence(subject):
            return False

        return self._matches(subject)

    def _is_not_a_sequence(self, value):
        return not isinstance(value, collections.Sequence)

    def _matches(self, subject):
        for expected_item in self._expected:
            if not self._matches_any(expected_item, subject):
                return False

        return True

    def _matches_any(self, expected, subject):
        if isinstance(subject, _compat.string_types):
            return expected in subject

        for item in subject:
            if self._match_value(expected, item):
                return True
        return False

    @_normalize_subject
    def _match_negated(self, subject):
        if self._is_not_a_sequence(subject):
            return False

        return not self._matches(subject)

    @_normalize_subject
    def _description(self, subject):
        result = '{} {expected}'.format(type(self).__name__.replace('_', ' '),
                                        expected=plain_enumerate(self._expected))

        if self._is_not_a_sequence(subject):
            result += ' but is not a valid sequence type'

        return result


class contain_exactly(contain):
    def _match(self, subject):
        if not super(contain_exactly, self)._match(subject):
            return False

        return len(subject) == self._expected_length(subject)

    def _expected_length(self, subject):
        if isinstance(subject, _compat.string_types):
            return len(''.join(self._expected))
        return len(self._expected)
