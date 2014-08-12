# -*- coding: utf-8 -*

from .matchers import Matcher
from .matchers.built_in import equal as equal_matcher


def plain_enumerate(args, kwargs=None):
    if kwargs is None:
        kwargs = {}

    total = len(args) + len(kwargs)

    result = ''
    i = 0
    for i, arg in enumerate(args):
        result += repr(arg)

        if i + 2 == total:
            result += ' and '
        elif i + 1 != total:
            result += ', '

    for i, pair in enumerate(_sorted_items(kwargs), i):
        key, value = pair
        if not isinstance(value, Matcher):
            value = equal_matcher(value)

        result += '{!r} {}'.format(key, value._description(None))

        if i + 2 == total:
            result += ' and '
        elif i + 1 != total:
            result += ', '

    return result


def _sorted_items(dct):
    return sorted(dct.items(), key=lambda args: args[0])
