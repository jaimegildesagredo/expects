# -*- coding: utf-8 -*


def key(actual, *args):
    name = args[0]

    try:
        expected = args[1]
    except IndexError:
        pass
    else:
        try:
            value = actual[name]
        except KeyError:
            pass
        else:
            return (
                value == expected,
                '{!r} with value {!r} but was {!r}'.format(name, expected, value))

    return name in actual.keys(), repr(name)
