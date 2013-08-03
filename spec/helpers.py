# -*- coding: utf-8 -*-

import re


class failure(object):
    def __init__(self, actual, message):
        self.message = 'Expected {} {}'.format(repr(actual), message)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            raise AssertionError('Expected AssertionError to be raised')

        if exc_type == AssertionError:
            exc_str = str(exc_value)

            if self.message == exc_str:
                return True
            elif re.search(self.message, exc_str, re.DOTALL):
                return True
            else:
                raise AssertionError(
                    "Expected error message '{}' to match '{}'".format(
                        exc_value, self.message))
