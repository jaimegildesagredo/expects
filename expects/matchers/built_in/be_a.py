# -*- coding: utf-8 -*

from .. import Matcher


class _BeAnInstanceOf(Matcher):
    def __init__(self, expected):
        self._expected = expected

    def _match(self, subject):
        return isinstance(subject, self._expected), []

    def __repr__(self):
        return '{name} {expected}'.format(name=self._name,
                                          expected=self._expected.__name__)


class be_a(_BeAnInstanceOf):
    pass


class be_an(_BeAnInstanceOf):
    pass


class a(_BeAnInstanceOf):
    pass


class an(_BeAnInstanceOf):
    pass
