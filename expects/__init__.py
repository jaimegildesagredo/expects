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
        message = ''

        if hasattr(matcher, '_failure_message'):
            message = matcher._failure_message(self._subject)

        if self._negated:
            truth = not truth

            if hasattr(matcher, '_failure_message_negated'):
                message = matcher._failure_message_negated(self._subject)

        assert truth, message


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
        'have_length': Length(),
        'have_property': Property(),
        'have_properties': Properties(),
        'have_key': Key(),
        'have_keys': Keys(),
        'contain': Contains(),
        'contain_only': ContainsOnly(),
        'match': Match(),
        'start_with': StartWith(),
        'end_with': EndWith(),
        'raise_error': RaiseError()
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

    def _failure_message(self, subject):
        return 'Expected {subject!r} to {description}'.format(
            subject=subject, description=self._description)

    def _failure_message_negated(self, subject):
        return 'Expected {subject!r} not to {description}'.format(
            subject=subject, description=self._description)

    @property
    def _description(self):
        return 'equal {expected!r}'.format(expected=self._expected)


class Be(Matcher):
    def _initialize(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject is self._expected

    def _failure_message(self, subject):
        return 'Expected {subject!r} to be {expected!r}'.format(
            subject=subject, expected=self._expected)

    def _failure_message_negated(self, subject):
        return 'Expected {subject!r} not to be {expected!r}'.format(
            subject=subject, expected=self._expected)


class IsTrue(object):
    def _match(self, subject):
        return subject is True

    def _failure_message(self, subject):
        return 'Expected {subject!r} to be true'.format(subject=subject)

    def _failure_message_negated(self, subject):
        return 'Expected {subject!r} not to be true'.format(subject=subject)


class IsFalse(object):
    def _match(self, subject):
        return subject is False

    def _failure_message(self, subject):
        return 'Expected {subject!r} to be false'.format(subject=subject)

    def _failure_message_negated(self, subject):
        return 'Expected {subject!r} not to be false'.format(subject=subject)


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

    def _failure_message(self, subject):
        if not self._args:
            message = 'Expected {subject!r} to have property {expected!r}'.format(
                subject=subject, expected=self._name)
        else:
            expected_value = self._args[0]
            if isinstance(expected_value, Matcher):
                message = 'Expected {subject!r} to have property {expected!r} with value {expected_value}'.format(subject=subject, expected=self._name, expected_value=expected_value._description)
            else:
                message = 'Expected {subject!r} to have property {expected!r} with value {expected_value!r}'.format(subject=subject, expected=self._name, expected_value=expected_value)

        if isinstance(subject, str):
            message += ' but is not a dict'

        return message

    def _failure_message_negated(self, subject):
        if not self._args:
            return 'Expected {subject!r} not to have property {expected!r}'.format(
                subject=subject, expected=self._name)

        return 'Expected {subject!r} not to have property {expected!r} with value {value!r}'.format(
            subject=subject, expected=self._name, value=self._args[0])


class Properties(Matcher):
    def _initialize(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        self._missing = None

    def _match(self, subject):
        try:
            self._kwargs = dict(*self._args, **self._kwargs)
        except (TypeError, ValueError):
            for name in self._args:
                if not self._has_property(subject, name):
                    self._missing = (name,)
                    return False
        finally:
            for name, value in self._kwargs.items():
                if not self._has_property(subject, name, value):
                    self._missing = (name, value)
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

    def _failure_message(self, subject):
        if self._missing:
            if len(self._missing) == 2:
                return 'Expected {!r} to have property {!r} with value {!r}'.format(subject, *self._missing)
            return 'Expected {!r} to have property {!r}'.format(subject, self._missing[0])


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

    def _failure_message(self, subject):
        if not self._args:
            message = 'Expected {subject!r} to have key {expected!r}'.format(
                subject=subject, expected=self._name)
        else:
            expected_value = self._args[0]
            if isinstance(expected_value, Matcher):
                message = 'Expected {subject!r} to have key {expected!r} with value {expected_value}'.format(subject=subject, expected=self._name, expected_value=expected_value._description)
            else:
                message = 'Expected {subject!r} to have key {expected!r} with value {expected_value!r}'.format(subject=subject, expected=self._name, expected_value=expected_value)

        if isinstance(subject, str):
            message += ' but is not a dict'

        return message

    def _failure_message_negated(self, subject):
        if not self._args:
            return 'Expected {subject!r} not to have key {expected!r}'.format(
                subject=subject, expected=self._name)

        return 'Expected {subject!r} not to have key {expected!r} with value {value!r}'.format(
            subject=subject, expected=self._name, value=self._args[0])


class Keys(Matcher):
    def _initialize(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs
        self._missing = None

    def _match(self, subject):
        try:
            self._kwargs = dict(*self._args, **self._kwargs)
        except (TypeError, ValueError):
            for name in self._args:
                if not self._has_key(subject, name):
                    self._missing = (name,)
                    return False
        finally:
            for name, value in self._kwargs.items():
                if not self._has_key(subject, name, value):
                    self._missing = (name, value)
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

    def _failure_message(self, subject):
        if self._missing:
            if len(self._missing) == 2:
                message = 'Expected {!r} to have key {!r} with value {!r}'
            else:
                message = 'Expected {!r} to have key {!r}'

            return message.format(subject, *self._missing)


class Above(Matcher):
    def _initialize(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject > self._expected

    def _failure_message(self, subject):
        return 'Expected {subject!r} to be above {expected!r}'.format(
            subject=subject, expected=self._expected)

    def _failure_message_negated(self, subject):
        return 'Expected {subject!r} not to be above {expected!r}'.format(
            subject=subject, expected=self._expected)


class AboveOrEqual(Matcher):
    def _initialize(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject >= self._expected

    def _failure_message(self, subject):
        return 'Expected {subject!r} to be above or equal {expected!r}'.format(
            subject=subject, expected=self._expected)

    def _failure_message_negated(self, subject):
        return 'Expected {subject!r} not to be above or equal {expected!r}'.format(
            subject=subject, expected=self._expected)


class Below(Matcher):
    def _initialize(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject < self._expected

    def _failure_message(self, subject):
        return 'Expected {subject!r} to be below {expected!r}'.format(
            subject=subject, expected=self._expected)

    def _failure_message_negated(self, subject):
        return 'Expected {subject!r} not to be below {expected!r}'.format(
            subject=subject, expected=self._expected)


class BelowOrEqual(Matcher):
    def _initialize(self, expected):
        self._expected = expected

    def _match(self, subject):
        return subject <= self._expected

    def _failure_message(self, subject):
        return 'Expected {subject!r} to be below or equal {expected!r}'.format(
            subject=subject, expected=self._expected)

    def _failure_message_negated(self, subject):
        return 'Expected {subject!r} not to be below or equal {expected!r}'.format(
            subject=subject, expected=self._expected)


class InstanceOf(Matcher):
    def _initialize(self, expected):
        self._expected = expected

    def _match(self, subject):
        return isinstance(subject, self._expected)

    def _failure_message(self, subject):
        return 'Expected {subject!r} to be an instance of {expected.__name__}'.format(
            subject=subject, expected=self._expected)

    def _failure_message_negated(self, subject):
        return 'Expected {subject!r} not to be an instance of {expected.__name__}'.format(
            subject=subject, expected=self._expected)


class Empty(Matcher):
    def _match(self, subject):
        try:
            return len(subject) == 0
        except TypeError:
            try:
                next(subject)
            except StopIteration:
                return True

    def _failure_message(self, subject):
        return 'Expected {subject!r} to be empty'.format(subject=subject)

    def _failure_message_negated(self, subject):
        return 'Expected {subject!r} not to be empty'.format(subject=subject)


class StartWith(Matcher):
    def _initialize(self, *args):
        self._args = args

    def _match(self, subject):
        if isinstance(subject, _compat.string_types):
            return subject.startswith(self._args[0])

        elif (isinstance(subject, collections.Mapping) and
              not isinstance(subject, collections.OrderedDict)):

            assert False, 'Expected {subject!r} to start with {expected} but it does not have ordered keys'.format(subject=subject, expected=plain_enumerate(self._args))
        else:
            return list(self._args) == list(subject)[:len(self._args)]

    def _failure_message(self, subject):
        if isinstance(subject, _compat.string_types):
            return 'Expected {subject!r} to start with {expected!r}'.format(
                subject=subject, expected=self._args[0])

        return 'Expected {subject!r} to start with {expected}'.format(
            subject=subject, expected=plain_enumerate(self._args))


class EndWith(Matcher):
    def _initialize(self, *args):
        self._args = args

    def _match(self, subject):
        if isinstance(subject, _compat.string_types):
            return subject.endswith(self._args[0])

        elif (isinstance(subject, collections.Mapping) and
              not isinstance(subject, collections.OrderedDict)):

            assert False, 'Expected {subject!r} to end with {expected} but it does not have ordered keys'.format(subject=subject, expected=plain_enumerate(self._args))
        else:
            return (list(self._args) ==
                    list(reversed(list(subject)[-len(self._args):])))

    def _failure_message(self, subject):
        if isinstance(subject, _compat.string_types):
            return 'Expected {subject!r} to end with {expected!r}'.format(
                subject=subject, expected=self._args[0])

        return 'Expected {subject!r} to end with {expected}'.format(
            subject=subject, expected=plain_enumerate(self._args))


class Contains(Matcher):
    def _initialize(self, *args):
        self._args = args

    def _match(self, subject):
        if isinstance(subject, collections.Iterator):
            collection = list(subject)
        else:
            collection = subject

        for arg in self._args:
            if arg not in collection:
                return False

        return True

    def _failure_message(self, subject):
        return 'Expected {subject!r} to contain {expected}'.format(
            subject=subject, expected=plain_enumerate(self._args))


class ContainsOnly(Matcher):
    def _initialize(self, *args):
        self._args = args

    def _match(self, subject):
        if isinstance(subject, collections.Iterator):
            collection = list(subject)
        else:
            collection = subject

        for arg in self._args:
            if arg not in collection:
                return False

        if isinstance(subject, _compat.string_types):
            args_length = len(''.join(self._args))
        else:
            args_length = len(self._args)

        return len(subject) == args_length

    def _failure_message(self, subject):
        return 'Expected {subject!r} to contain only {expected}'.format(
            subject=subject, expected=plain_enumerate(self._args))


def plain_enumerate(args):
    result = ''

    total = len(args)
    for i, arg in enumerate(args):
        result += repr(arg)

        if i + 2 == total:
            result += ' and '
        elif i + 1 != total:
            result += ', '
    return result


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

    def _failure_message(self, subject):
        return 'Expected {subject!r} to have length {expected}'.format(
            subject=subject, expected=self._expected)

    def _failure_message_negated(self, subject):
        return 'Expected {subject!r} not to have length {expected}'.format(
            subject=subject, expected=self._expected)


class Match(Matcher):
    def _initialize(self, expected, *args):
        self._expected = expected
        self._args = args

    def _match(self, subject):
        return True if re.match(self._expected, subject, *self._args) is not None else False

    def _failure_message(self, subject):
        return 'Expected {subject!r} to {description}'.format(
            subject=subject, description=self._description)

    def _failure_message_negated(self, subject):
        return 'Expected {subject!r} not to {description}'.format(
            subject=subject, description=self._description)

    @property
    def _description(self):
        # TODO: Add self._args to failure message
        return 'match {expected!r}'.format(expected=self._expected)


class IsNone(Matcher):
    def _match(self, subject):
        return subject is None

    def _failure_message(self, subject):
        return 'Expected {subject!r} to be none'.format(subject=subject)

    def _failure_message_negated(self, subject):
        return 'Expected {subject!r} not to be none'.format(subject=subject)


class RaiseError(Matcher):
    def _initialize(self, expected, *args):
        self._expected = expected
        self._args = args
        self._got = None
        self._got_value = None

    def _match(self, subject):
        try:
            subject()
        except self._expected as exc:
            self._got = exc

            if len(self._args) != 0:
                self._got_value, expected_value = exc.args[0], self._args[0]

                if hasattr(expected_value, '_match'):
                    return expected_value._match(self._got_value)

                return self._got_value == expected_value
            else:
                return True

        except Exception as err:
            self._got = err
            return False
        else:
            return False

    def _failure_message(self, subject):
        if self._args:
            expected_value = self._args[0]

            if isinstance(expected_value, Matcher):
                message = (
                    'Expected {subject!r} to raise {expected.__name__} '
                    'with {expected_value} but was {got_value!r}'.format(
                        subject=subject, expected=self._expected,
                        expected_value=expected_value._description,
                        got_value=self._got_value)
                )
            else:
                message = (
                    'Expected {subject!r} to raise {expected.__name__} '
                    'with {expected_value!r} but was {got_value!r}'.format(
                        subject=subject, expected=self._expected,
                        expected_value=expected_value, got_value=self._got_value)
                )

            return message

        if self._got is None:
            return 'Expected {subject!r} to raise {expected.__name__} but not raised'.format(
            subject=subject, expected=self._expected)

        return 'Expected {subject!r} to raise {expected.__name__} but {got.__name__} raised'.format(
            subject=subject, expected=self._expected, got=type(self._got))


    def _failure_message_negated(self, subject):
        if self._args:
            expected_value = self._args[0]
            return (
                'Expected {subject!r} not to raise {expected.__name__} '
                'with {expected_value!r} but {got.__name__} raised with {got_value!r}'.format(
                    subject=subject, expected=self._expected,
                    expected_value=expected_value, got_value=self._got_value, got=type(self._got))
            )

        return 'Expected {subject!r} not to raise {expected.__name__} but {got.__name__} raised'.format(
            subject=subject, expected=self._expected, got=type(self._got))


class WithIn(Matcher):
    def _initialize(self, start, stop):
        self._start = start
        self._stop = stop

    def _match(self, subject):
        return subject in range(self._start, self._stop)

    def _failure_message(self, subject):
        return 'Expected {subject!r} to {description}'.format(
            subject=subject, description=self._description)

    def _failure_message_negated(self, subject):
        return 'Expected {subject!r} not to {description}'.format(
            subject=subject, description=self._description)

    @property
    def _description(self):
        return 'be within {start} and {stop}'.format(start=self._start, stop=self._stop)
