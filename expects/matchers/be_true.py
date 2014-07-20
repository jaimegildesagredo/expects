# -*- coding: utf-8 -*

from . import Matcher


class _BeTrue(Matcher):
    def _match(self, subject):
        return subject is True

    def _description(self, subject):
        return 'be true'

be_true = _BeTrue()
