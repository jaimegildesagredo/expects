# -*- coding: utf-8 -*

from . import Matcher


class BeNone(Matcher):
    def _match(self, subject):
        return subject is None

    @property
    def _description(self):
        return 'be none'
