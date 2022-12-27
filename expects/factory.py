# -*- coding: utf-8 -*

from .expectations import Expectation


def expect(subject, *args, **kwargs):
    return Expectation(subject, *args, **kwargs)
