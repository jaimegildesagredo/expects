# -*- coding: utf-8 -*

"""
Introduction
------------

*Expects* can be `extended` by defining `new matchers`.
The :mod:`matchers` module contains the bases for building
custom matchers.

Tutorial
--------

The easiest way to define a new matcher is to extend the
:class:`Matcher` class and override the :func:`Matcher._match`
method.

For example, to define a matcher to check if a `request` object contains
a given header takes <10 lines of code::

    from expects.matchers import Matcher

    class have_header(Matcher):
        def __init__(self, expected):
            self._expected = expected

        def _match(self, request):
            if self._expected in request.headers:
                return True, ['header found']
            return True, ['header not found']

An then you only need to import the new defined matcher and write
your expectation::

    from expects import expect
    from my_custom_matchers import have_header

    expect(my_request).to(have_header('Content-Type'))

Advanced
--------

For more complex matchers you can override the :class:`Matcher`
methods in order to achieve the needed behavior.

"""


class Matcher(object):
    """The :class:`Matcher` class is the base class for all `Expects`
    matchers.

    It defines a set of methods to ease writting new matchers.

    """

    def _match(self, subject):
        """This method will be called when the matcher is used in an
        expectation. It should be overwritten to implement the matcher
        logic. If not raises :class:`NotImplementedError`.

        Receives the expectation `subject` as the unique positional
        argument and should return a :keyword:`tuple` with the
        :keyword:`bool` result of the matcher and a :keyword:`list` of
        reasons for this result.

        If the matcher matches the subject then the boolean result
        should be :keyword:`True`. The reasons should be a list with
        0 or more strings.

        :param subject: The target value of the expectation.
        :rtype: tuple (bool, [str])

        """

        raise NotImplementedError()

    def _match_negated(self, subject):
        """Like :func:`_match` but will be called when used in a
        negated expectation. It can be used to implement a custom
        logic for negated expectations.

        By default returns the result of negating ``self._match(subject)``.

        :param subject: The target value of the expectation.
        :rtype: tuple (bool, [str])

        """

        result, reason = self._match(subject)
        return not result, reason

    def _failure_message(self, subject, reasons):
        """This method will be called from an expectation `only` when
        the expectation is going to fail. It should return a string
        with the failure message.

        By default returns a failure message with the following format::

            expected: {subject} to {description}
                 but: {reasons}

        With the passed `subject` repr, this matcher repr as `description`
        and the passed `reasons` from the matcher result.

        :param subject: The target value of the expectation.
        :param reasons: A list of reasons that caused this matcher to fail.
        :type subject: a string
        :type reasons: list of strings
        :rtype: a string

        """

        message = '\nexpected: {subject!r} to {matcher!r}'.format(
            subject=subject, matcher=self)

        if reasons:
            message += '\n     but: {0}'.format('\n          '.join(reasons))

        return message

    def _failure_message_negated(self, subject, reasons):
        """Like the :func:`_failure_message` method but will be called
        when a negated expectation is going to fail. It should return a
        string with the failure message for the negated expectation.

        By default returns a failure message with the following format::

            expected: {subject} to {description}
                 but: {reasons}

        :param subject: The target value of the expectation.
        :param reasons: A list of reasons that caused this matcher to fail.
        :type subject: a string
        :type reasons: list of strings
        :rtype: a string

        """

        message = '\nexpected: {subject!r} not to {matcher!r}'.format(
            subject=subject, matcher=self)

        if reasons:
            message += '\n     but: {0}'.format('\n          '.join(reasons))

        return message

    def __repr__(self):
        """Returns a string with the description of the matcher.

        By default returns a string with the following format::

            '{name} {expected}'

        Where `name` is based on the matcher class name and `expected`
        is the value passed to the constructor.

        :rtype: a string

        """

        if hasattr(self, '_expected'):
            return '{name} {expected!r}'.format(name=self._name,
                                                expected=self._expected)
        return self._name

    @property
    def _name(self):
        return type(self).__name__.replace('_', ' ').strip()

    def __and__(self, other):
        return _And(self, other)

    def __or__(self, other):
        return _Or(self, other)


def default_matcher(value):
    if not isinstance(value, Matcher):
        return equal_matcher(value)
    return value


class _And(Matcher):
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def _match(self, subject):
        result1, _ = self.op1._match(subject)
        result2, _ = self.op2._match(subject)

        return result1 and result2, []

    def __repr__(self):
        return '{0} and {1}'.format(repr(self.op1).replace(' and ', ', '),
                                    repr(self.op2))


class _Or(Matcher):
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def _match(self, subject):
        result1, _ = self.op1._match(subject)
        result2, _ = self.op2._match(subject)

        return result1 or result2, []

    def __repr__(self):
        return '{0} or {1}'.format(repr(self.op1).replace(' or ', ', '),
                                   repr(self.op2))

from .built_in import equal as equal_matcher
