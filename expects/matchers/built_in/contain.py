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
        if isinstance(subject, _compat.string_types):
            # TODO: test this
            return expected in subject, ['contain {!r}'.format(expected)]

        # TODO: test this
        reason = None
        for item in subject:
            matches, reason = self._match_value(expected, item)
            if matches:
                return True, 'item {} found'.format(reason)

        return False, 'item {} not found'.format(reason) if reason is not None else 'is empty'

    @_normalize_subject
    def _match_negated(self, subject):
        if self._is_not_a_sequence(subject):
            return False, ['is not a valid sequence type']

        ok, message = self._matches(subject)

        return not ok, message

    @_normalize_subject
    def _description(self, subject):
        return '{} {expected}'.format(type(self).__name__.replace('_', ' '),
                                      expected=plain_enumerate(self._expected))

    def _failure_message(self, subject, reasons):
        return '\nexpected: {!r} to {}\n     but: {}'.format(
            subject,
            self._description(subject),
            '\n          '.join(reasons))

    def _failure_message_negated(self, subject, reasons):
        return '\nexpected: {!r} not to {}\n     but: {}'.format(
            subject,
            self._description(subject),
            '\n          '.join(reasons))


class contain_exactly(contain):
    def _matches(self, subject):
        if isinstance(subject, _compat.string_types):
            return subject == ''.join(self._expected), ['string false o true']

        try:
            for index, expected_item in enumerate(self._expected):
                result, reason = self._match_value(expected_item, subject[index])
                if not result:
                    return False, ['item {!r} not found'.format(expected_item)]
        except IndexError:
            return False, ['item {!r} not found'.format(expected_item)]

        return len(subject) == len(self._expected), ['true o false']


class contain_only(contain):
    def _matches(self, subject):
        if isinstance(subject, _compat.string_types):
            return subject == ''.join(self._expected)

        if not super(contain_only, self)._matches(subject):
            return False

        return len(subject) == len(self._expected)
