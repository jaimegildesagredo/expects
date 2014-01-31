# -*- coding: utf-8 -*

import contextlib


class Expectation(object):
    def __init__(self, actual, *message):
        self._actual = actual
        self._message = list(message)
        self._negated = False
        self._flags = {}

    def __getattribute__(self, name):
        if name.startswith('_') or name.startswith('not__'):
            return object.__getattribute__(self, name)

        if name.startswith('not_') and name != 'not_':
            with self.__negation:
                return self.__getattr_and_append_to_message(name[4:])

        return self.__getattr_and_append_to_message(name)

    @property
    @contextlib.contextmanager
    def __negation(self):
        self._message.append('not')
        self._negated = not self._negated

        try:
            yield
        except AttributeError:
            self._message.pop()
            self._negated = not self._negated

    def __getattr_and_append_to_message(self, name):
        # This should be done before __getattribute__ because properties
        # are evaluated at that time
        self._message.extend(name.split('_'))

        return object.__getattribute__(self, name)

    def _assert(self, result, *message):
        if (not result if self._negated else result) is not True:
            self._message.extend(message)
            raise AssertionError(' '.join(str(i) for i in self._message))


class Proxy(object):
    def __init__(self, obj):
        self.__obj = obj

    def __getattr__(self, name):
        return getattr(self.__obj, name)
