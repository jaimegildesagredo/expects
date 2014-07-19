# -*- coding: utf-8 -*

from . import Matcher


class BeNone(Matcher):
    def _match(self, subject):
        return subject is None

    def _description(self, subject):
        return 'be none'
