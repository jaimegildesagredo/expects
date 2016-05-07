# -*- coding: utf-8 -*

import traceback

from .. import Matcher, default_matcher


class _raise_error(Matcher):
    def __init__(self, expected, *args):
        self._expected = expected
        self._args = args

    def __call__(self, *args, **kwargs):
        return _raise_error(*args, **kwargs)

    def _match(self, subject):
        try:
            subject()
        except self._expected as exc:
            if len(self._args) != 0:
                actual_value = exc.args[0]
                expected_value = default_matcher(self._args[0])
                result, _ = expected_value._match(actual_value)
                return result, ['{0} raised with {1!r}'.format(type(exc).__name__, actual_value)]

            return True, ['{0} raised'.format(type(exc).__name__)]

        except Exception as err:
            return False, ['{0} raised\n\n{1}'.format(type(err).__name__, traceback.format_exc())]
        else:
            return False, ['no exception raised']


raise_error = _raise_error(Exception)
