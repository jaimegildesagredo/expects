# -*- coding: utf-8 -*

from .. import Matcher, default_matcher
from ...texts import plain_enumerate


class _PropertyMatcher(Matcher):
    def _match(self, subject):
        args, kwargs = self._expected

        success_reasons = []
        for name in args:
            has_property, reason = self._has_property(subject, name)
            if not has_property:
                return False, [reason]
            else:
                success_reasons.append(reason)

        for name, value in kwargs.items():
            has_property, reason = self._has_property(subject, name, value)
            if not has_property:
                return False, [reason]
            else:
                success_reasons.append(reason)

        return True, success_reasons

    def _has_property(self, subject, name, *args):
        if args:
            try:
                value = getattr(subject, name)
            except AttributeError:
                return False, 'property {0!r} not found'.format(name)
            else:
                expected_value = default_matcher(args[0])
                result, _ = expected_value._match(value)
                if not result:
                    return  False, 'property {0!r} {1!r} not found'.format(name, expected_value)
                return True, 'property {0!r} {1!r} found'.format(name, expected_value)

        if not hasattr(subject, name):
            return False, 'property {0!r} not found'.format(name)
        return True, 'property {0!r} found'.format(name)

    def __repr__(self):
        return '{0} {1}'.format(type(self).__name__.replace('_', ' '),
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
