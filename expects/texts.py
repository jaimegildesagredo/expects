# -*- coding: utf-8 -*

from .matchers import default_matcher


def plain_enumerate(args, kwargs=None):
    if kwargs is None:
        kwargs = {}

    tokens = []

    for arg in args:
        tokens.append(repr(arg))

    for k, v in _sorted_items(kwargs):
        tokens.append('{0!r} {1!r}'.format(k, default_matcher(v)))

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
