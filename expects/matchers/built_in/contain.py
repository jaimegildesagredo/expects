# -*- coding: utf-8 -*

import functools
import collections

from .. import Matcher
from ...texts import plain_enumerate
from ... import _compat


class contain(Matcher):
    def __init__(self, *args):
        self._args = args

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
        for arg in self._args:
            if arg not in subject:
                return False

        return True

    @_normalize_subject
    def _match_negated(self, subject):
        if self._is_not_a_sequence(subject):
            return False

        return not self._matches(subject)

    @_normalize_subject
    def _description(self, subject):
        result = '{} {expected}'.format(type(self).__name__.replace('_', ' '),
                                        expected=plain_enumerate(self._args))

        if self._is_not_a_sequence(subject):
            result += ' but is not a valid sequence type'

        return result


class contain_exactly(contain):
    def _matches(self, subject):
        if not super(contain_exactly, self)._matches(subject):
            return False

        return len(subject) == self._args_length(subject)

    def _args_length(self, subject):
        if isinstance(subject, _compat.string_types):
            return len(''.join(self._args))
        return len(self._args)
