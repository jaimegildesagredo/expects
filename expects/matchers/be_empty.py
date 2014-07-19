# -*- coding: utf-8 -*

from . import Matcher


class BeEmpty(Matcher):
    def _match(self, subject):
        try:
            return len(subject) == 0
        except TypeError:
            try:
                next(subject)
            except StopIteration:
                return True

    def _description(self, subject):
        return 'be empty'
