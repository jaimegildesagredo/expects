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

    @property
    def _description(self):
        return 'be empty'
