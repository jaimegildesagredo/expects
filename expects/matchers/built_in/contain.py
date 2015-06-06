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
    def _matches(self, subject):
        if isinstance(subject, _compat.string_types):
            return subject == ''.join(self._expected)
        try:
            for index, expected_item in enumerate(self._expected):
                if not self._match_value(expected_item, subject[index]):
                    return False
        except IndexError:
            return False

        return len(subject) == len(self._expected)


class contain_only(contain):
    def _matches(self, subject):
        if isinstance(subject, _compat.string_types):
            return subject == ''.join(self._expected)

        if not super(contain_only, self)._matches(subject):
            return False

        return len(subject) == len(self._expected)
