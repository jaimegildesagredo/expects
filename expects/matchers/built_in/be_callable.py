# -*- coding: utf-8 -*-

from .. import Matcher


class _be_callable(Matcher):
    def _match(self, subject):
        return callable(subject), []

be_callable = _be_callable()
