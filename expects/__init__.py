# -*- coding: utf-8 -*

import inspect

from . import plugins


def expect(subject):
    return Expectation(subject, plugins.load_matchers(), inspect.currentframe().f_back)


class Expectation(object):
    def __init__(self, subject, matchers, frame):
        self._subject = subject
        self._matchers = matchers
        self._frame = frame
        self._negated = False

        self._setup_matchers()

    def _setup_matchers(self):
        self._globals_before = dict(self._frame.f_globals)

        for name, matcher in self._matchers.items():
            self._frame.f_globals[name] = matcher()

    @property
    def not_to(self):
        self._negated = True
        return self.to

    def to(self, matcher):
        self._teardown_matchers()
        self._assert(matcher)

    def _teardown_matchers(self):
        for key in dict(self._frame.f_globals):
            del self._frame.f_globals[key]

        self._frame.f_globals.update(self._globals_before)

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
