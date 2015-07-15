# -*- coding: utf-8 -*

from .. import Matcher


class _be_none(Matcher):
    def _match(self, subject):
        return subject is None, []

be_none = _be_none()
