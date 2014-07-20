# -*- coding: utf-8 -*

from . import Matcher
from .. import _compat


class HaveProperties(Matcher):
    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        self._missing = None

    def _match(self, subject):
        try:
            self._kwargs = dict(*self._args, **self._kwargs)
        except (TypeError, ValueError):
            for name in self._args:
                if not self._has_property(subject, name):
                    self._missing = (name,)
                    return False
        finally:
            for name, value in self._kwargs.items():
                if not self._has_property(subject, name, value):
                    self._missing = (name, value)
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
        if self._missing:
            if len(self._missing) == 2:
                return 'have property {!r} with value {!r}'.format(*self._missing)
            return 'have property {!r}'.format(self._missing[0])
