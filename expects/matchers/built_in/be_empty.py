# -*- coding: utf-8 -*

from .. import Matcher


class _be_empty(Matcher):
    def _match(self, subject):
        try:
            return len(subject) == 0, []
        except TypeError:
            try:
                next(subject)
            except StopIteration:
                return True, []
            return False, []

be_empty = _be_empty()
