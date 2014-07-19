# -*- coding: utf-8 -*

from . import Matcher


class BeFalse(Matcher):
    def _match(self, subject):
        return subject is False

    @property
    def _description(self):
        return 'be false'
