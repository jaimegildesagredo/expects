# -*- coding: utf-8 -*

import re

from ._compat import with_metaclass


class Builder(type):
    def __get__(cls, instance, owner):
        if instance is not None:
            return cls(instance)
        return cls


class Expectation(with_metaclass(Builder)):
    def __init__(self, parent):
        self._parent = parent

    @property
    def actual(self):
        return self._parent.actual

    @property
    def negative(self):
        return self._parent.negative

    def _assert(self, result, error_message):
        assert not result if self.negative else result, error_message


class Equal(Expectation):
    def __call__(self, expected):
        self._assert(self.actual == expected, self.error_message(repr(expected)))

    def error_message(self, tail):
        return self._parent.error_message('equal {}'.format(tail))


class Be(Expectation):
    equal = Equal

    def __call__(self, expected):
        self._assert(self.actual is expected, self.error_message(repr(expected)))

    def a(self, expected):
        self.__instance_of(expected, 'a')

    def an(self, expected):
        self.__instance_of(expected, 'an')

    def __instance_of(self, expected, article):
        self._assert(isinstance(self.actual, expected), self.error_message(
            '{} {} instance'.format(article, expected.__name__)))

    def greater_than(self, expected):
        self._assert(self.actual > expected, self.error_message(
            'greater than {}'.format(expected)))

    def greater_or_equal_to(self, expected):
        self._assert(self.actual >= expected, self.error_message(
            'greater or equal to {}'.format(expected)))

    def less_than(self, expected):
        self._assert(self.actual < expected, self.error_message(
            'less than {}'.format(expected)))

    def less_or_equal_to(self, expected):
        self._assert(self.actual <= expected, self.error_message(
            'less or equal to {}'.format(expected)))

    def within(self, start, stop):
        self._assert(self.actual in range(start, stop), self.error_message(
            'within {}, {}'.format(start, stop)))

    @property
    def true(self):
        self(True)

    @property
    def false(self):
        self(False)

    @property
    def none(self):
        self(None)

    @property
    def empty(self):
        self._assert(len(self.actual) == 0, self.error_message('empty'))

    def error_message(self, tail):
        return self._parent.error_message('be {}'.format(tail))


class Have(Expectation):
    def __call__(self, *args):
        for arg in args:
            self._assert(arg in self.actual, self.error_message(repr(arg)))

    def property(self, *args):
        def error_message(tail):
            return self.error_message('property {}'.format(tail))

        name = args[0]

        try:
            expected = args[1]
        except IndexError:
            pass
        else:
            try:
                value = getattr(self.actual, name)
            except AttributeError:
                pass
            else:
                self._assert(value == expected, error_message('{} with value {} but was {}'.format(
                    repr(name), repr(expected), repr(value))))

                return

        self._assert(hasattr(self.actual, name), error_message(repr(name)))

    def key(self, *args):
        name = args[0]

        try:
            expected = args[1]
        except IndexError:
            pass
        else:
            try:
                value = self.actual[name]
            except KeyError:
                pass
            else:
                self._assert(value == expected, self.error_message(
                    'key {} with value {} but was {}'.format(repr(name), repr(expected), repr(value))))

                return

        self._assert(name in self.actual, self.error_message('key {}'.format(repr(name))))

    def properties(self, *args, **kwargs):
        self._dict_based_expectation(self.property, args, kwargs)

    def keys(self, *args, **kwargs):
        self._dict_based_expectation(self.key, args, kwargs)

    def _dict_based_expectation(self, expectation, args, kwargs):
        try:
            kwargs = dict(*args, **kwargs)
        except (TypeError, ValueError):
            for name in args:
                expectation(name)
        finally:
            for name, value in kwargs.items():
                expectation(name, value)

    def length(self, expected):
        value = len(self.actual)

        self._assert(value == expected, self.error_message(
            'length {} but was {}'.format(expected, value)))

    def error_message(self, tail):
        return self._parent.error_message('have {}'.format(tail))


class RaiseError(Expectation):
    def __call__(self, expected, message=None):
        assertion = self._build_assertion(expected, message)

        if assertion is not None:
            self._assert(*assertion)

    def _build_assertion(self, expected, message):
        def error_message(tail):
            return self.error_message('{} {}'.format(
                expected.__name__, tail))

        try:
            self.actual()
        except expected as exc:
            exc_message = str(exc)

            if message is not None:
                return message == exc_message, error_message(
                    'with message {} but message was {}'.format(repr(message), repr(exc_message)))
            else:
                return True, error_message('but {} raised'.format(type(exc).__name__))
        except Exception as err:
            return False, error_message('but {} raised'.format(type(err).__name__))
        else:
            return False, error_message('but {} raised'.format(None))

    def error_message(self, tail):
        return self._parent.error_message('raise {}'.format(tail))


class To(Expectation):
    be = Be
    have = Have
    equal = Equal
    raise_error = RaiseError

    def match(self, expected, *flags):
        self._assert(re.match(expected, self.actual, *flags), self.error_message(
            'match {}'.format(repr(expected))))

    def error_message(self, tail):
        message = 'not to' if self.negative else 'to'

        return self._parent.error_message('{} {}'.format(message, tail))
