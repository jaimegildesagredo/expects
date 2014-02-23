# -*- coding: utf-8 -*-

import re


class failure(object):
    def __init__(self, actual, message):
        self._message = '{!r} {}'.format(actual, message)

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type is None:
            raise AssertionError('Expected AssertionError to be raised')

        if exc_type != AssertionError:
            raise AssertionError(
                'Expected AssertionError to be raised but {} raised'.format(
                    exc_type))

        exc_message = str(exc_value)

        if (self._message in exc_message or
            re.search(self._message, exc_message, re.DOTALL)):

            return True
        else:
            raise AssertionError(
                "Expected error message '{}' to match '{}'".format(
                    exc_value, self._message))
