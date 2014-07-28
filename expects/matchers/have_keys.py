# -*- coding: utf-8 -*

from .matcher import Matcher


class HaveKeys(Matcher):
    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    def _match(self, subject):
        args, kwargs = self._keys

        for name in args:
            if not self._has_key(subject, name):
                return False

        for name, value in kwargs.items():
            if not self._has_key(subject, name, value):
                return False

        return True

    @property
    def _keys(self):
        try:
            return (), dict(*self._args, **self._kwargs)
        except (TypeError, ValueError):
            return self._args, self._kwargs

    def _has_key(self, subject, name, *args):
        if args:
            try:
                value = subject[name]
            except KeyError:
                return False
            else:
                expected_value = args[0]

                if hasattr(expected_value, '_match'):
                    return expected_value._match(value)

                return value == expected_value

        return name in subject

    def _description(self, subject):
        return 'have keys {}'.format(plain_enumerate(*self._keys))


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
