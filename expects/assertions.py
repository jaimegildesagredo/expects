# -*- coding: utf-8 -*


class Assertion(object):
    def __init__(self, assert_):
        self._assert = assert_


class Empty(Assertion):
    def __call__(self, value):
        self._assert(self._is_empty(value))

    def _is_empty(self, value):
        try:
            return len(value) == 0
        except TypeError:
            try:
                next(value)
            except StopIteration:
                return True


class Instance(Assertion):
    def __call__(self, value, expected):
        self._assert(isinstance(value, expected),
                     expected.__name__, 'instance')
