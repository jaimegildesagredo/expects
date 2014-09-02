# -*- coding: utf-8 -*-

"""The :mod:`testing` module provides helpers to ease testing of your
`custom matchers <custom-matchers.html>`_.

"""

import re
import traceback

from ._compat import with_metaclass


class _ContextManagerMeta(type):
    def __enter__(cls):
        pass

    def __exit__(cls, exc_type, exc_value, exc_tb):
        cls._handle_exception(exc_type, exc_value, exc_tb)
        return True


class failure(with_metaclass(_ContextManagerMeta)):
    """The :class:`failure` context manager can be used to build
    assertions of your expectations failures. It tests that the
    code inside the context manager raises an :class:`AssertionError`
    and matches the given message (if any).

    :param message: string matching the failure message
    :type message: a string
    :raises:  :class:`AssertionError` when no *AssertionError* or
              another exception raised

    .. note::

        The :class:`failure` context manager can be used without being
        *called* (for example, if you don't want to specify a *failure message*).

    Examples::

        >>> with failure:
                expect(object()).to(have_property('foo'))

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
        self._handle_exception(exc_type, exc_value, exc_tb)

        exc_message = str(exc_value)

        if (self._message in exc_message or
            re.search(self._message, exc_message, re.DOTALL)):

            return True

        raise AssertionError(
            "Expected error message '{}' to match '{}'".format(
                exc_value, self._message))

    @classmethod
    def _handle_exception(cls, exc_type, exc_value, exc_tb):
        if exc_type is None:
            raise AssertionError('Expected AssertionError to be raised')

        if exc_type != AssertionError:
            raise AssertionError(
                'Expected AssertionError to be raised but {} raised.'
                '\n\n{}'.format(exc_type.__name__,
                                _format_exception(exc_type, exc_value, exc_tb))
            )


def _format_exception(exc_type, exc_value, exc_tb):
    return ''.join(traceback.format_exception(exc_type, exc_value, exc_tb))
