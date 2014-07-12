# -*- coding: utf-8 -*

import re
import inspect
import collections

from . import _compat



def expect(subject):
    return Expectation(subject, _registered_matchers(), inspect.currentframe().f_back)


class Expectation(object):
    def __init__(self, subject, matchers, frame):
        self._subject = subject
        self._matchers = matchers
        self._frame = frame
        self._negated = False

        self._setup_matchers()

    def _setup_matchers(self):
        self._globals_before = dict(self._frame.f_globals)
        self._frame.f_globals.update(self._matchers)

    def to(self, matcher):
        self._teardown_matchers()
        self._assert(matcher)

    @property
    def not_to(self):
        self._negated = True
        return self.to

    def _teardown_matchers(self):
        for key in dict(self._frame.f_globals):
            del self._frame.f_globals[key]

        self._frame.f_globals.update(self._globals_before)

    def _assert(self, matcher):
        truth = matcher._match(self._subject)

        if self._negated:
            truth = not truth

        assert truth


def _registered_matchers():
    return {
        'equal': Equal(),
        'be': Be(),
        'be_above': Above(),
        'be_above_or_equal': AboveOrEqual(),
        'be_below': Below(),
        'be_below_or_equal': BelowOrEqual(),
        'be_within': WithIn(),
        'be_a': InstanceOf(),
        'be_an': InstanceOf(),
        'be_empty': Empty(),
        'be_true': IsTrue(),
        'be_false': IsFalse(),
        'be_none': IsNone(),
        'have': Contains(),
        'have_length': Length(),
        'have_property': Property(),
        'have_properties': Properties(),
        'have_key': Key(),
        'have_keys': Keys(),
        'match': Match(),
        'start_with': StartWith(),
        'end_with': EndWith(),
        'raise_error': Raise()
    }


class Matcher(object):
    def __call__(self, *args, **kwargs):
        self._initialize(*args, **kwargs)
        return self


class Equal(Matcher):
    def _initialize(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject == self._expected


class Be(Matcher):
    def _initialize(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject is self._expected


class IsTrue(object):
    def _match(self, subject):
        return subject is True


class IsFalse(object):
    def _match(self, subject):
        return subject is False


class Property(Matcher):
    def _initialize(self, name, *args):
        self._name = name
        self._args = args

    def _match(self, subject):
        if self._args:
            try:
                value = getattr(subject, self._name)
            except AttributeError:
                return False
            else:
                expected_value = self._args[0]

                if hasattr(expected_value, '_match'):
                    return expected_value._match(value)

                return value == expected_value

        return hasattr(subject, self._name)


class Properties(Matcher):
    def _initialize(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    def _match(self, subject):
        try:
            self._kwargs = dict(*self._args, **self._kwargs)
        except (TypeError, ValueError):
            for name in self._args:
                if not self._has_property(subject, name):
                    return False
        finally:
            for name, value in self._kwargs.items():
                if not self._has_property(subject, name, value):
                    return False

        return True

    def _has_property(self, subject, name, *args):
        if args:
            try:
                value = getattr(subject, name)
            except AttributeError:
                return False
            else:
                expected_value = args[0]

                if hasattr(expected_value, '_match'):
                    return expected_value._match(value)

                return value == expected_value

        return hasattr(subject, name)


class Key(Matcher):
    def _initialize(self, name, *args):
        self._name = name
        self._args = args

    def _match(self, subject):
        if isinstance(subject, str):
            return False

        if self._args:
            try:
                value = subject[self._name]
            except KeyError:
                return False
            else:
                expected_value = self._args[0]

                if hasattr(expected_value, '_match'):
                    return expected_value._match(value)

                return value == expected_value

        return self._name in subject


class Keys(Matcher):
    def _initialize(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    def _match(self, subject):
        try:
            self._kwargs = dict(*self._args, **self._kwargs)
        except (TypeError, ValueError):
            for name in self._args:
                if not self._has_key(subject, name):
                    return False
        finally:
            for name, value in self._kwargs.items():
                if not self._has_key(subject, name, value):
                    return False

        return True

    def _has_key(self, subject, name, *args):
        if args:
            try:
                value = subject[name]
            except KeyError:
                return False
            else:
                expected_value = args[0]

                if hasattr(expected_value, '_match'):
                    return expected_value._match(value)

                return value == expected_value

        return name in subject


class Above(Matcher):
    def _initialize(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject > self._expected


class AboveOrEqual(Matcher):
    def _initialize(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject >= self._expected


class Below(Matcher):
    def _initialize(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject < self._expected


class BelowOrEqual(Matcher):
    def _initialize(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject <= self._expected


class InstanceOf(Matcher):
    def _initialize(self, expected):
        self._expected = expected

    def _match(self, subject):
        return isinstance(subject, self._expected)


class Empty(Matcher):
    def _match(self, subject):
        try:
            return len(subject) == 0
        except TypeError:
            try:
                next(subject)
            except StopIteration:
                return True


class StartWith(Matcher):
    def _initialize(self, *args):
        self._args = args

    def _match(self, subject):
        if isinstance(subject, _compat.string_types):
            return subject.startswith(self._args[0])

        elif (isinstance(subject, collections.Mapping) and
              not isinstance(subject, collections.OrderedDict)):

            assert False
        else:
            return list(self._args) == list(subject)[:len(self._args)]


class EndWith(Matcher):
    def _initialize(self, *args):
        self._args = args

    def _match(self, subject):
        if isinstance(subject, _compat.string_types):
            return subject.endswith(self._args[0])

        elif (isinstance(subject, collections.Mapping) and
              not isinstance(subject, collections.OrderedDict)):

            assert False
        else:
            return (list(self._args) ==
                    list(reversed(list(subject)[-len(self._args):])))


class Contains(Matcher):
    def __init__(self):
        super(Contains, self).__init__()
        self._flags = {}

    def _initialize(self, *args):
        self._args = args

    def _match(self, subject):
        if isinstance(subject, collections.Iterator):
            collection = list(subject)
        else:
            collection = subject

        if self._flags.get('only', False):
            for arg in self._args:
                if arg not in collection:
                    return False

            if isinstance(subject, _compat.string_types):
                args_length = len(''.join(self._args))
            else:
                args_length = len(self._args)

            return len(subject) == args_length

        else:
            for arg in self._args:
                if arg not in collection:
                    return False

        return True

    @property
    def only(self):
        self._flags['only'] = True
        return self


class Length(Matcher):
    def _initialize(self, expected):
        self._expected = expected

    def _match(self, subject):
        return self.__length(subject) == self._expected

    def __length(self, collection):
        try:
            return len(collection)
        except TypeError:
            return sum(1 for i in collection)


class Match(Matcher):
    def _initialize(self, expected, *args):
        self._expected = expected
        self._args = args

    def _match(self, subject):
        return True if re.match(self._expected, subject, *self._args) is not None else False


class IsNone(Matcher):
    def _match(self, subject):
        return subject is None


class Raise(Matcher):
    def _initialize(self, expected, *args):
        self._expected = expected
        self._args = args

    def _match(self, subject):
        try:
            subject()
        except self._expected as exc:
            exc_args = exc.args
            exc_message = str(exc)

            if len(self._args) != 0:
                value = self._args[0]

                if isinstance(value, _compat.string_types):
                    return self.__matchs_exception(value, exc_message)
                else:
                    return value == exc_args[0]
            else:
                return True

        except Exception as err:
            return False
        else:
            return False

    def __matchs_exception(self, message, exc_message):
        if message == exc_message:
            return True

        elif (isinstance(message, _compat.string_types) and
              re.search(message, exc_message)):

            return True

        return False


class WithIn(Matcher):
    def _initialize(self, start, stop):
        self._start = start
        self._stop = stop

    def _match(self, subject):
        return subject in range(self._start, self._stop)
