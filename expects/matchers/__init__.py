# -*- coding: utf-8 -*


class Matcher(object):
    def __call__(self, *args, **kwargs):
        self._initialize(*args, **kwargs)
        return self

    def _failure_message(self, subject):
        return 'Expected {subject!r} to {description}'.format(
            subject=subject, description=self._description)

    def _failure_message_negated(self, subject):
        return 'Expected {subject!r} not to {description}'.format(
            subject=subject, description=self._description)


def plain_enumerate(args):
    result = ''

    total = len(args)
    for i, arg in enumerate(args):
        result += repr(arg)

        if i + 2 == total:
            result += ' and '
        elif i + 1 != total:
            result += ', '
    return result

from .equal import Equal
from .be import Be
from .be_true import BeTrue
from .be_false import BeFalse
from .be_none import BeNone
from .be_a import BeAnInstanceOf
from .be_empty import BeEmpty
from .be_above import BeAbove
from .be_below import BeBelow
from .be_above_or_equal import BeAboveOrEqual
from .be_below_or_equal import BeBelowOrEqual
from .be_within import BeWithIn
from .have_length import HaveLength
from .have_property import HaveProperty
from .have_properties import HaveProperties
from .have_key import HaveKey
from .have_keys import HaveKeys
from .contain import Contain
from .contain_only import ContainOnly
from .start_with import StartWith
from .end_with import EndWith
from .match import Match
from .raise_error import RaiseError
