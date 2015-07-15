# -*- coding: utf-8 -*

from .. import Matcher, default_matcher


class have_length(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, subject):
        expected_length = default_matcher(self._expected)
        actual_length = self.__length(subject)
        result, _ = expected_length._match(actual_length)
        return result, ['was {!r}'.format(actual_length)]

    def __length(self, collection):
        try:
            return len(collection)
        except TypeError:
            return sum(1 for i in collection)

    def _failure_message(self, subject, reasons):
        return '\nexpected: {!r} to {}\n     but: {}'.format(
            subject,
            repr(self),
            '\n          '.join(reasons))

    def _failure_message_negated(self, subject, reasons):
         return '\nexpected: {!r} not to {}\n     but: {}'.format(
            subject,
            repr(self),
            '\n          '.join(reasons))


class have_len(have_length):
    pass
