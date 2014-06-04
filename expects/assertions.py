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


class Property(Assertion):
    # TODO: Rename `value` arg to `actual`
    def __call__(self, value, *args):
        name = args[0]

        try:
            expected = args[1]
        except IndexError:
            pass
        else:
            try:
                value = getattr(value, name)
            except AttributeError:
                pass
            else:
                self._assert(value == expected,
                             '{!r} with value {!r} but was {!r}'.format(
                                 name, expected, value))

                return

        self._assert(hasattr(value, name), repr(name))
