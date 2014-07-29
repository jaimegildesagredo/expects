# -*- coding: utf-8 -*

from ..matcher import Matcher


class _BeNone(Matcher):
    def _match(self, subject):
        return subject is None

    def _description(self, subject):
        return 'be none'

be_none = _BeNone()
