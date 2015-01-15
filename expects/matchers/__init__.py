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
            return self._expected in request.headers

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
        argument and should return :keyword:`True` if the matcher matches
        the subject and :keyword:`False` if it does not.

        :param subject: The target value of the expectation.
        :rtype: a boolean

        """

        raise NotImplementedError()

    def _match_negated(self, subject):
        """Like :func:`_match` but will be called when used in a
        negated expectation. It can be used to implement a custom
        logic for negated expectations.

        By default returns the result of ``not self._match(subject)``.

        :param subject: The target value of the expectation.
        :rtype: a boolean

        """

        return not self._match(subject)

    def _failure_message(self, subject):
        """This method will be called from an expectation `only` when
        the expectation is going to fail. It should return a string
        with the failure message.

        By default returns a failure message with the following format::

            'Expected {subject} to {description}'

        With the passed `subject` and the result of calling the
        :func:`_description` method.

        :param subject: The target value of the expectation.
        :rtype: a string

        """

        return 'Expected {subject!r} to {description}'.format(
            subject=subject, description=self._description(subject))

    def _failure_message_negated(self, subject):
        """Like the :func:`_failure_message` method but will be called
        when a negated expectation is going to fail. It should return a
        string with the failure message for the negated expectation.

        By default returns a failure message with the following format::

            'Expected {subject} not to {description}'

        :param subject: The target value of the expectation.
        :rtype: a string

        """

        return 'Expected {subject!r} not to {description}'.format(
            subject=subject, description=self._description(subject))

    def _description(self, subject):
        """This method receives the `subject` of the expectation and
        returns a string with the description of the matcher to be
        used in failure messages.

        By default returns a string with the following format::

            '{name} {expected}'

        Where `name` is based on the matcher class name and `expected`
        is the value passed to the constructor.

        :param subject: The target value of the expectation.
        :rtype: a string

        """

        if hasattr(self, '_expected'):
            if hasattr(self._expected, '_description'):
                expected = self._expected._description(None)
            else:
                expected = repr(self._expected)

            return '{name} {expected}'.format(name=self._name,
                                                expected=expected)
        return self._name

    @property
    def _name(self):
        return type(self).__name__.replace('_', ' ').strip()

    def _match_value(self, matcher, value):
        """This method receives a :class:`Matcher` instance and a
        `value to be matched` as first and second arguments respectively,
        and returns :keyword:`True` or :keyword:`False` depending on
        whether the `value` matches.

        If the argument passed as `matcher` does not implements the
        :class:`Matcher` interface then the :keyword:`equal` built-in
        matcher is used.

        Examples::

            >>> self._match_value('foo', 'foo')
            True
            >>> self._match_value('foo', 'bar')
            False
            >>> self._match_value(match('\w+'), 'foo')
            True

        :param matcher: A matcher that will be used to match the given value.
        :param value: A value to test if matches.
        :rtype: bool

        """

        if not hasattr(matcher, '_match'):
            matcher = equal_matcher(matcher)

        return matcher._match(value)

    def __and__(self, other):
        return _And(self, other)

    def __or__(self, other):
        return _Or(self, other)

from .built_in import equal as equal_matcher


class _And(Matcher):
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def _match(self, subject):
        return self.op1._match(subject) and self.op2._match(subject)

    def _description(self, subject):
        return '{} and {}'.format(self.op1._description(subject).replace(' and ', ', '),
                                  self.op2._description(subject))


class _Or(Matcher):
    def __init__(self, op1, op2):
        self.op1 = op1
        self.op2 = op2

    def _match(self, subject):
        return self.op1._match(subject) or self.op2._match(subject)

    def _description(self, subject):
        return '{} or {}'.format(self.op1._description(subject).replace(' or ', ', '),
                                 self.op2._description(subject))
