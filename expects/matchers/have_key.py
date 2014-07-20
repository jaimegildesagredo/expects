# -*- coding: utf-8 -*

from . import Matcher
from .. import _compat


class HaveKey(Matcher):
    def __init__(self, name, *args):
        self._name = name
        self._args = args

    def _match(self, subject):
        if isinstance(subject, str):
            return False

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

        if isinstance(subject, _compat.string_types):
            message += ' but is not a dict'

        return message
