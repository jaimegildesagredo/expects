# -*- coding: utf-8 -*

from .expectations import Expectation


def expect(subject):
    return Expectation(subject)
