# -*- coding: utf-8 -*

from . import Matcher


class BeTrue(Matcher):
    def _match(self, subject):
        return subject is True

    @property
    def _description(self):
        return 'be true'
