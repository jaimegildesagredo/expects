# -*- coding: utf-8 -*

from .matcher import Matcher
from .. import _compat


class HaveProperties(Matcher):
    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    def _match(self, subject):
        args, kwargs = self._properties

        for name in args:
            if not self._has_property(subject, name):
                return False

        for name, value in kwargs.items():
            if not self._has_property(subject, name, value):
                return False

        return True

    @property
    def _properties(self):
        try:
            return (), dict(*self._args, **self._kwargs)
        except (TypeError, ValueError):
            return self._args, self._kwargs

    def _has_property(self, subject, name, *args):
        if args:
            try:
                value = getattr(subject, name)
            except AttributeError:
                return False
            else:
                expected_value = args[0]

                if hasattr(expected_value, '_match'):
                    return expected_value._match(value)

                return value == expected_value

        return hasattr(subject, name)

    def _description(self, subject):
        return 'have properties {}'.format(plain_enumerate(*self._properties))


def plain_enumerate(args, kwargs):
    total = len(args) + len(kwargs)

    result = ''
    i = 0
    for i, arg in enumerate(args):
        result += repr(arg)

        if i + 2 == total:
            result += ' and '
        elif i + 1 != total:
            result += ', '

    for i, pair in enumerate(_ordered_items(kwargs), i):
        result += '{}={!r}'.format(*pair)

        if i + 2 == total:
            result += ' and '
        elif i + 1 != total:
            result += ', '

    return result


def _ordered_items(dct):
    return sorted(dct.items(), key=lambda args: args[0])
