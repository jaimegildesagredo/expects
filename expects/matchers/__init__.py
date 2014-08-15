# -*- coding: utf-8 -*

"""
The :mod:`matchers` module contains the bases for building custom matchers.
"""


class Matcher(object):
    """Base class for all Expects matchers"""

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
            return '{name} {expected!r}'.format(name=self.__name,
                                                expected=self._expected)
        return self.__name

    @property
    def __name(self):
        return type(self).__name__.replace('_', ' ').strip()
