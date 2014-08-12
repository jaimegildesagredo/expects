# -*- coding: utf-8 -*

from .. import Matcher
from ... import _compat
from ...texts import plain_enumerate


class _PropertyMatcher(Matcher):
    def _match(self, subject):
        args, kwargs = self._expected

        for name in args:
            if not self._has_property(subject, name):
                return False

        for name, value in kwargs.items():
            if not self._has_property(subject, name, value):
                return False

        return True

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
        return '{} {}'.format(type(self).__name__.replace('_', ' '),
                              plain_enumerate(*self._expected))


class have_properties(_PropertyMatcher):
    def __init__(self, *args, **kwargs):
        try:
            self._expected = (), dict(*args, **kwargs)
        except (TypeError, ValueError):
            self._expected = args, kwargs


class have_property(_PropertyMatcher):
    def __init__(self, name, *args):
        if args:
            self._expected = (), {name: args[0]}
        else:
            self._expected = (name,), {}
