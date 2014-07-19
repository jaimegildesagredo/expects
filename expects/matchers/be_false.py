# -*- coding: utf-8 -*

from . import Matcher


class BeFalse(Matcher):
    def _match(self, subject):
        return subject is False

    def _description(self, subject):
        return 'be false'
