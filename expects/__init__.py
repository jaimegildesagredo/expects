# -*- coding: utf-8 -*

from .expectations import To


def expect(actual):
    return Expect(actual)


class Expect(object):
    to = To

    def __init__(self, actual):
        self.actual = actual
        self.negated = False

    @property
    def not_to(self):
        self.negated = True
        return self.to

    def error_message(self, tail):
        return 'Expected {} {}'.format(repr(self.actual), tail)
