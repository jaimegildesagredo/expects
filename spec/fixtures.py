# -*- coding: utf-8 -*


class Foo(object):
    bar = 0
    baz = 1


class _Expect(object):
    def __init__(self, actual, *message):
        self.actual = actual
        self.message = list(message)


class DefaultExpect(_Expect):
    pass


class BarExpect(_Expect):
    pass
