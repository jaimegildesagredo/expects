# -*- coding: utf-8 -*

from .. import Matcher


class _be_false(Matcher):
    def _match(self, subject):
        return subject is False, []

be_false = _be_false()
