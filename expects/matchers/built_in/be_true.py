# -*- coding: utf-8 -*

from .. import Matcher


class _be_true(Matcher):
    def _match(self, subject):
        return subject is True, []

be_true = _be_true()
