# -*- coding: utf-8 -*

from .expectations import To


class expect(object):
    def __init__(self, actual):
        self.actual = actual
        self.to = To(self)

    def error_message(self, tail):
        return 'Expected {} {}'.format(repr(self.actual), tail)
