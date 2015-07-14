# -*- coding: utf-8 -*

import collections

from . import equal as equal_matcher
from .. import Matcher
from ...texts import plain_enumerate


class _DictMatcher(Matcher):
    def _match(self, subject):
        if self._not_a_dict(subject):
            return False, ['is not a dict']

        return self._matches(subject)

    def _not_a_dict(self, value):
        return not isinstance(value, collections.Mapping)

    def _matches(self, subject):
        args, kwargs = self._expected

        reasons = []
        for name in args:
            has_key, reason = self._has_key(subject, name)
            if not has_key:
                return False, [reason]
            else:
                reasons.append(reason)

        for name, value in kwargs.items():
            has_key, reason = self._has_key(subject, name, value)
            if not has_key:
                return False, [reason]
            else:
                reasons.append(reason)

        return True, reasons

    def _has_key(self, subject, name, *args):
        if args:
            try:
                value = subject[name]
            except KeyError:
                return False, 'key {!r} {} not found'.format(name, equal_matcher(args[0])._description(None))
            else:
                result, reason = self._match_value(args[0],value)

                reason_message = 'not found' if not result else 'found'
                return result, 'key {!r} {} {}'.format(name, reason, reason_message)

        if name in subject:
            return True, 'key {!r} found'.format(name)
        return False, 'key {!r} not found'.format(name)

    def _match_negated(self, subject):
        if self._not_a_dict(subject):
            return False, ['is not a dict']

        result, description = self._matches(subject)
        return not result, description

    def _description(self, subject):
        message = '{} {}'.format(type(self).__name__.replace('_', ' '),
                                 plain_enumerate(*self._expected))

        if self._not_a_dict(subject):
            message += ' but is not a dict'

        return message

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

class have_keys(_DictMatcher):
    def __init__(self, *args, **kwargs):
        try:
            self._expected = (), dict(*args, **kwargs)
        except (TypeError, ValueError):
            self._expected = args, kwargs


class have_key(_DictMatcher):
    def __init__(self, name, *args):
        if args:
            self._expected = (), {name: args[0]}
        else:
            self._expected = (name,), {}
