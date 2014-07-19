# -*- coding: utf-8 -*

from . import Matcher


class BeTrue(Matcher):
    def _match(self, subject):
        return subject is True

    def _description(self, subject):
        return 'be true'
