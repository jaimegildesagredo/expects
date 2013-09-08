# -*- coding: utf-8 -*

from . import errors


class ExpectFactory(object):
    def __init__(self, expectations):
        self._expectations = expectations

    def __call__(self, *args, **kwargs):
        expectation, actual = self.__parse_args(args, kwargs)

        try:
            return self._expectations[expectation](actual)
        except KeyError:
            raise errors.ExtensionError(
                'Extension {!r} not found'.format(expectation))

    def __parse_args(self, args, kwargs):
        total_args = len(args)
        total_kwargs = len(kwargs)

        if total_kwargs > 1 or (total_kwargs >= 1 and total_args >= 1):
            raise TypeError('expect() got an unexpected keyword argument '
                            '{!r}'.format(kwargs.popitem()[0]))

        if total_args > 1:
            raise TypeError('expect() takes 1 positional argument but '
                            '{} were given'.format(total_args))

        if total_args < 1 and total_kwargs < 1:
            raise TypeError('expect() takes 1 required positional argument')

        try:
            actual = args[0]
        except IndexError:
            expectation, actual = kwargs.popitem()
        else:
            expectation = 'default'

        return expectation, actual


def _load_expectations():
    from pkg_resources import iter_entry_points

    return {e.name: e.load() for e in
            iter_entry_points('expects.expectations')}


expect = ExpectFactory(_load_expectations())
