# -*- coding: utf-8 -*-


class failure(object):
    def __init__(self, actual, message):
        self.message = 'Expected {} {}'.format(repr(actual), message)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            raise AssertionError('Expected AssertionError to be raised')

        if exc_type == AssertionError:
            if str(exc_value) == self.message:
                return True

            raise AssertionError("Expected error message '{}' to be '{}'".format(
                exc_value, self.message))
