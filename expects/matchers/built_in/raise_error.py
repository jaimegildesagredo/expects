# -*- coding: utf-8 -*

from .. import Matcher


class raise_error(Matcher):
    def __init__(self, expected, *args):
        self._expected = expected
        self._args = args
        self._got = None
        self._got_value = None

    def _match(self, subject):
        try:
            subject()
        except self._expected as exc:
            self._got = exc

            if len(self._args) != 0:
                self._got_value, expected_value = exc.args[0], self._args[0]

                if hasattr(expected_value, '_match'):
                    return expected_value._match(self._got_value)

                return self._got_value == expected_value
            else:
                return True

        except Exception as err:
            self._got = err
            return False
        else:
            return False

    def _failure_message(self, subject):
        if self._args:
            expected_value = self._args[0]

            if isinstance(expected_value, Matcher):
                message = (
                    'Expected {subject!r} to raise {expected.__name__} '
                    'with {expected_value} but was {got_value!r}'.format(
                        subject=subject, expected=self._expected,
                        expected_value=expected_value._description(subject),
                        got_value=self._got_value)
                )
            else:
                message = (
                    'Expected {subject!r} to raise {expected.__name__} '
                    'with {expected_value!r} but was {got_value!r}'.format(
                        subject=subject, expected=self._expected,
                        expected_value=expected_value, got_value=self._got_value)
                )

            return message

        if self._got is None:
            return 'Expected {subject!r} to raise {expected.__name__} but not raised'.format(
            subject=subject, expected=self._expected)

        return 'Expected {subject!r} to raise {expected.__name__} but {got.__name__} raised'.format(
            subject=subject, expected=self._expected, got=type(self._got))


    def _failure_message_negated(self, subject):
        if self._args:
            expected_value = self._args[0]
            return (
                'Expected {subject!r} not to raise {expected.__name__} '
                'with {expected_value!r} but {got.__name__} raised with {got_value!r}'.format(
                    subject=subject, expected=self._expected,
                    expected_value=expected_value, got_value=self._got_value, got=type(self._got))
            )

        return 'Expected {subject!r} not to raise {expected.__name__} but {got.__name__} raised'.format(
            subject=subject, expected=self._expected, got=type(self._got))
