# -*- coding: utf-8 -*


def expect(subject):
    return Expectation(subject)


class Expectation(object):
    def __init__(self, subject):
        self._subject = subject
        self._negated = False

    @property
    def not_to(self):
        self._negated = True
        return self.to

    def to(self, matcher):
        self._assert(matcher)

    def _assert(self, matcher):
        truth = matcher._match(self._subject)
        message = ''

        if hasattr(matcher, '_failure_message'):
            message = matcher._failure_message(self._subject)

        if self._negated:
            truth = not truth

            if hasattr(matcher, '_failure_message_negated'):
                message = matcher._failure_message_negated(self._subject)

        assert truth, message
