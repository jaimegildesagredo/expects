# -*- coding: utf-8 -*

from .. import Matcher


class be_above_or_equal(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject >= self._expected, ['was {!r}'.format(subject)]

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


class above_or_equal(be_above_or_equal):
    pass
