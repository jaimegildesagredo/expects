# -*- coding: utf-8 -*-

from contextlib import contextmanager


@contextmanager
def failure(message=None):
    try:
        yield
    except AssertionError as err:
        if message is not None and str(err) != message:
            raise AssertionError("Expected error message '{}' to be '{}'".format(
                err, message))
    else:
        raise AssertionError('Expected AssertionError to be raised')
