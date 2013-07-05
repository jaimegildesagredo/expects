# -*- coding: utf-8 -*


class Foo(object):
    bar = 0
    baz = 1


class Matcher(object):
    expected = True

    def matches(self, obj):
        self.actual = obj
        return obj is self.expected

    def __str__(self):
        return "Expected {} but was {}".format(self.expected, self.actual)
