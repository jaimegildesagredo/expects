# -*- coding: utf-8 -*


class Empty(object):
    def __init__(self, assert_):
        self._assert = assert_

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
