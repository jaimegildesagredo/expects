# -*- coding: utf-8 -*


def key(actual, name, *args):
    # TODO(jaimegildesagredo): It'd nice to add unit tests

    try:
        expected_value = args[0]
    except IndexError:
        pass
    else:
        try:
            value = actual[name]
        except KeyError:
            pass
        else:
            return (
                value == expected_value,
                '{!r} with value {!r} but was {!r}'.format(
                    name, expected_value, value)
            )

    return name in actual, repr(name)
