# -*- coding: utf-8 -*


class Foo(object):
    bar = 0
    baz = 1


class _Expect(object):
    def __init__(self, actual):
        self.actual = actual


class DefaultExpect(_Expect):
    pass


class BarExpect(_Expect):
    pass
