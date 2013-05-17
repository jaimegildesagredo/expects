# -*- coding: utf-8 -*-

from contextlib import contextmanager


@contextmanager
def failure(actual, message):
    try:
        yield
    except AssertionError as err:
        message = _failure_message(actual, message)

        if str(err) != message:
            raise AssertionError("Expected error message '{}' to be '{}'".format(err, message))
    else:
        raise AssertionError('Expected AssertionError to be raised')


def _failure_message(actual, message):
    return 'Expected {} {}'.format(repr(actual), message)
