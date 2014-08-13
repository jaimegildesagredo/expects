# -*- coding: utf-8 -*-

"""The :mod:`testing` module provides helpers to ease testing of your
`custom matchers <custom-matchers.html>`_.

"""

import re
import traceback


class failure(object):
    """The :class:`failure` context manager can be used to build
    assertions of your expectations failures. It tests that an
    expectation fails raising an :class:`AssertionError` with the
    proper failure message.

    It receives `a string` that should match the failure message.

    If the expectation does not raise an :class:`AssertionError` or the
    failure message does not match the given string then an
    :class:`AssertionError` is raised.

    Examples::

        >>> with failure("to have property 'foo'"):
        ...     expect(object()).to(have_property('foo'))

        >>> with failure("to have property '__class__'"):
        ...     expect(object()).to(have_property('__class__'))
        Traceback (most recent call last):
          File "<stdin>", line 2, in <module>
          File "expects/testing.py", line 40, in __exit__
            raise AssertionError('Expected AssertionError to be raised')
        AssertionError: Expected AssertionError to be raised


    """

    def __init__(self, message):
        self._message = message

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            raise AssertionError('Expected AssertionError to be raised')

        if exc_type != AssertionError:
            raise AssertionError(
                'Expected AssertionError to be raised but {} raised.'
                '\n\n{}'.format(exc_type.__name__,
                                _format_exception(exc_type, exc_value, exc_tb))
            )

        exc_message = str(exc_value)

        if (self._message in exc_message or
            re.search(self._message, exc_message, re.DOTALL)):

            return True

        raise AssertionError(
            "Expected error message '{}' to match '{}'".format(
                exc_value, self._message))


def _format_exception(exc_type, exc_value, exc_tb):
    return ''.join(traceback.format_exception(exc_type, exc_value, exc_tb))
