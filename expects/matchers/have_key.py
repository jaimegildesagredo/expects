# -*- coding: utf-8 -*

import collections

from .matcher import Matcher
from .. import _compat


class HaveKey(Matcher):
    def __init__(self, name, *args):
        self._name = name
        self._args = args

    def _match(self, subject):
        if self._not_a_dict(subject):
            return False

        return self._matches(subject)

    def _match_negated(self, subject):
        if self._not_a_dict(subject):
            return False

        return not self._matches(subject)

    def _not_a_dict(self, value):
        return not isinstance(value, collections.Mapping)

    def _matches(self, subject):
        if self._args:
            try:
                value = subject[self._name]
            except KeyError:
                return False
            else:
                expected_value = self._args[0]

                if hasattr(expected_value, '_match'):
                    return expected_value._match(value)

                return value == expected_value

        return self._name in subject

    def _description(self, subject):
        if not self._args:
            return 'have key {expected!r}'.format(expected=self._name)

        expected_value = self._args[0]
        if isinstance(expected_value, Matcher):
            message = 'have key {expected!r} with value {expected_value}'.format(expected=self._name, expected_value=expected_value._description(subject))
        else:
            message = 'have key {expected!r} with value {expected_value!r}'.format(expected=self._name, expected_value=expected_value)

        if self._not_a_dict(subject):
            message += ' but is not a dict'

        return message
