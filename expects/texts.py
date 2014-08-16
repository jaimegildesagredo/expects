# -*- coding: utf-8 -*

from .matchers import Matcher
from .matchers.built_in import equal as equal_matcher


def plain_enumerate(args, kwargs=None):
    if kwargs is None:
        kwargs = {}

    tokens = []

    for arg in args:
        tokens.append(repr(arg))

    for k, v in _sorted_items(kwargs):
        if not isinstance(v, Matcher):
            v = equal_matcher(v)

        tokens.append('{!r} {}'.format(k, v._description(None)))

    total = len(args) + len(kwargs)

    result = ''
    for i, token in enumerate(tokens):
        result += token
        if i == total - 2:
            result += ' and '
        elif i != total - 1:
            result += ', '

    return result



def _sorted_items(dct):
    return sorted(dct.items(), key=lambda args: args[0])
