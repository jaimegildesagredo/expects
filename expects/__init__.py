# -*- coding: utf-8 -*

import inspect

from .matchers import *


def expect(subject):
    return Expectation(subject, _registered_matchers(), inspect.currentframe().f_back)


class Expectation(object):
    def __init__(self, subject, matchers, frame):
        self._subject = subject
        self._matchers = matchers
        self._frame = frame
        self._negated = False

        self._setup_matchers()

    def _setup_matchers(self):
        self._globals_before = dict(self._frame.f_globals)
        self._frame.f_globals.update(self._matchers)

    def to(self, matcher):
        self._teardown_matchers()
        self._assert(matcher)

    @property
    def not_to(self):
        self._negated = True
        return self.to

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


def _registered_matchers():
    return {
        'equal': Equal(),
        'be': Be(),
        'be_above': BeAbove(),
        'be_above_or_equal': BeAboveOrEqual(),
        'be_below': BeBelow(),
        'be_below_or_equal': BeBelowOrEqual(),
        'be_within': BeWithIn(),
        'be_a': BeAnInstanceOf(),
        'be_an': BeAnInstanceOf(),
        'be_empty': BeEmpty(),
        'be_true': BeTrue(),
        'be_false': BeFalse(),
        'be_none': BeNone(),
        'have_length': HaveLength(),
        'have_property': HaveProperty(),
        'have_properties': HaveProperties(),
        'have_key': HaveKey(),
        'have_keys': HaveKeys(),
        'contain': Contain(),
        'contain_only': ContainOnly(),
        'match': Match(),
        'start_with': StartWith(),
        'end_with': EndWith(),
        'raise_error': RaiseError()
    }
