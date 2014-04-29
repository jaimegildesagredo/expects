# -*- coding: utf-8 -*

import re
import traceback
import collections

from .expectation import Expectation, Proxy
from . import matchers, _compat


class Expects(Expectation):
    @property
    def only(self):
        self._flags['only'] = True
        return self

    @property
    def to(self):
        return self

    @property
    def with_value(self):
        self._message.append(repr(self._actual))
        return self

    @property
    def be(self):
        return _Be(self)

    @property
    def true(self):
        self._message.pop()
        self.__be(True)

    def __be(self, value):
        return _Be(self)(value)

    @property
    def false(self):
        self._message.pop()
        self.__be(False)

    @property
    def none(self):
        self._message.pop()
        self.__be(None)

    @property
    def empty(self):
        self._assert(self.__is_empty)

    @property
    def __is_empty(self):
        try:
            return len(self._actual) == 0
        except TypeError:
            try:
                next(self._actual)
            except StopIteration:
                return True

    def start_with(self, value):
        self._assert(self._actual.startswith(value))

    def end_with(self, value):
        self._assert(self._actual.endswith(valye))

    def equal(self, expected):
        self._assert(self._actual == expected, repr(expected))

    def a(self, expected):
        return self.__instance_of(expected)

    def an(self, expected):
        return self.__instance_of(expected)

    def __instance_of(self, expected):
        self._assert(isinstance(self._actual, expected),
                     expected.__name__, 'instance')

    def above(self, expected):
        self._assert(self._actual > expected, expected)

    def above_or_equal(self, expected):
        self._assert(self._actual >= expected, expected)

    def below(self, expected):
        self._assert(self._actual < expected, expected)

    def below_or_equal(self, expected):
        self._assert(self._actual <= expected, expected)

    def within(self, start, stop):
        self._assert(self._actual in range(start, stop),
                     '{}, {}'.format(start, stop))

    @property
    def have(self):
        return _Have(self)

    def property(self, *args):
        name = args[0]

        try:
            expected = args[1]
        except IndexError:
            pass
        else:
            try:
                value = getattr(self._actual, name)
            except AttributeError:
                pass
            else:
                self._assert(value == expected,
                             '{!r} with value {!r} but was {!r}'.format(
                                 name, expected, value))

                return

        self._assert(hasattr(self._actual, name), repr(name))

        try:
            message = list(self._message)
            message.append(repr(name))
            return Expects(getattr(self._actual, name), *message)
        except AttributeError:
            pass

    def key(self, name, *args):
        if not isinstance(self._actual, dict):
            self._assert(False, '{!r} but not a dict'.format(name))

            return

        self._assert(*matchers.key(self._actual, name, *args))

        try:
            message = list(self._message)
            message.append(repr(name))
            return Expects(self._actual[name], *message)
        except KeyError:
            pass

    def properties(self, *args, **kwargs):
        self._message.pop()

        self._dict_based_expectation(self.property, args, kwargs)

    def keys(self, *args, **kwargs):
        self._message.pop()

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
        value = self.__length(self._actual)

        self._assert(value == expected,
                     '{} but was {}'.format(expected, value))

    def __length(self, collection):
        try:
            return len(collection)
        except TypeError:
            return sum(1 for i in collection)

    def raise_error(self, exception, *args):
        self._message.pop()  # Removes the trailing 'error'

        assertion = self._build_assertion(exception, args)

        if assertion is not None:
            self._assert(*assertion)

    def _build_assertion(self, exception, args):
        try:
            self._actual()
        except exception as exc:
            exc_args = exc.args
            exc_message = str(exc)

            if len(args) != 0:
                value = args[0]

                if isinstance(value, _compat.string_types):
                    return (self.__matchs_exception(value, exc_message),
                            exception.__name__,
                            'with message {!r} but message was {!r}'.format(
                                value, exc_message))
                else:
                    return (value == exc_args[0],
                            exception.__name__,
                            'with arg {!r} but args were {!r}'.format(
                                value, exc_args))
            else:
                return (True,
                        exception.__name__,
                        'but {} raised\n\n{}'.format(type(exc).__name__,
                                                     traceback.format_exc()))

        except Exception as err:
            return (False,
                    exception.__name__,
                    'but {} raised\n\n{}'.format(type(err).__name__,
                                                 traceback.format_exc()))

        else:
            return False, exception.__name__, 'but not raised'

    def __matchs_exception(self, message, exc_message):
        if message == exc_message:
            return True
        elif isinstance(message, str) and re.search(message, exc_message):
            return True

        return False

    def match(self, expected, *flags):
        self._assert(self.__match(expected, flags), repr(expected))

    def __match(self, expected, flags):
        return True if re.match(expected, self._actual, *flags) is not None else False


class _Have(Proxy):
    def __call__(self, *args):
        if isinstance(self._actual, collections.Iterator):
            collection = list(self._actual)
        else:
            collection = self._actual

        if self._flags.get('only', False):
            for arg in args:
                self._assert(arg in collection,
                             self.__only_have_expected(args))

            if isinstance(self._actual, _compat.string_types):
                args_length = len(''.join(args))
            else:
                args_length = len(args)

            self._assert(len(self._actual) == args_length,
                         self.__only_have_expected(args))

        else:
            for arg in args:
                self._assert(arg in collection, repr(arg))

    def __only_have_expected(self, args):
        result = ''

        total = len(args)
        for i, arg in enumerate(args):
            result += repr(arg)

            if i + 2 == total:
                result += ' and '
            elif i + 1 != total:
                result += ', '
        return result



class _Be(Proxy):
    def __call__(self, expected):
        self._assert(self._actual is expected, repr(expected))
