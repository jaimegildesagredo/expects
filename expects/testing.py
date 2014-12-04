# -*- coding: utf-8 -*-

"""The :mod:`testing` module provides helpers to ease the testing
of your `custom matchers <custom-matchers.html>`_.

"""

import re
import traceback

from ._compat import with_metaclass
from .matchers.built_in import end_with as end_with_matcher


class _ContextManagerMeta(type):
    def __enter__(cls):
        pass

    def __exit__(cls, exc_type, exc_value, exc_tb):
        cls._handle_exception(exc_type, exc_value, exc_tb)
        return True


class failure(with_metaclass(_ContextManagerMeta)):
    """The :class:`failure` context manager can be used to build
    assertions of your expectation failures. It tests that the
    code inside the context manager raises an :class:`AssertionError`
    and matches the given message (whether any has been specified).

    :param message: should match the failure message. If a string is
                    passed, the :class:`end_with` matcher will be used
                    by default.

    :type message: an :class:`expects.matchers.Matcher` or string

    :raises:  :class:`AssertionError` when no *AssertionError* was
              raised, the failure message didn't match or another
              exception raised.

    .. note::

        The :class:`failure` context manager can be used without being
        *called* (for example, if you don't want to specify a *failure message*).

    Examples:

    .. code-block:: python

        >>> with failure:
        ...     expect(object()).to(have_property('foo'))

    .. code-block:: python

        >>> with failure("to have property 'foo'"):
        ...     expect(object()).to(have_property('foo'))

    .. code-block:: python

        >>> with failure(end_with("have property 'foo'")):
        ...     expect(object()).to(have_property('foo'))

    .. code-block:: python

        >>> with failure("to have property '__class__'"):
        ...     expect(object()).to(have_property('__class__'))
        Traceback (most recent call last):
          File "<stdin>", line 2, in <module>
          File "expects/testing.py", line 40, in __exit__
            raise AssertionError('Expected AssertionError to be raised')
        AssertionError: Expected AssertionError to be raised

    """

    def __init__(self, message):
        if not hasattr(message, '_match'):
            message = end_with_matcher(message)

        self._message = message

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._handle_exception(exc_type, exc_value, exc_tb)

        exc_message = str(exc_value)

        if not self._message._match(exc_message):
            raise AssertionError(
                "Expected error message {!r} {}".format(
                    exc_message, self._message._description(exc_value)))

        return True

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
