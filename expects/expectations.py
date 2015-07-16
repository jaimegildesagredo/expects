# -*- coding: utf-8 -*


class Expectation(object):
    def __init__(self, subject):
        self._subject = subject
        self._negated = False

    @property
    def not_to(self):
        self._negated = True
        return self.to

    @property
    def to_not(self):
        return self.not_to

    def to(self, matcher):
        self._assert(matcher)

    def _assert(self, matcher):
        ok, reasons = self._match(matcher)

        if not ok:
            raise AssertionError(self._failure_message(matcher, reasons))

    def _match(self, matcher):
        return getattr(
            matcher,
            '_match_negated' if self._negated else '_match'
        )(self._subject)

    def _failure_message(self, matcher, *args):
        return getattr(
            matcher,
            '_failure_message_negated' if self._negated else '_failure_message'
        )(self._subject, *args)
