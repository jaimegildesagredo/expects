# -*- coding: utf-8 -*

from .. import Matcher


class not_(Matcher):
    def __init__(self, matcher):
        self._matcher = matcher

    def _match(self, subject):
        return self._matcher._match_negated(subject)

    def __repr__(self):
        return 'not {0!r}'.format(self._matcher)
