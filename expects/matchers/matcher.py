# -*- coding: utf-8 -*


class Matcher(object):
    def _match_negated(self, subject):
        return not self._match(subject)

    def _failure_message(self, subject):
        return 'Expected {subject!r} to {description}'.format(
            subject=subject, description=self._description(subject))

    def _failure_message_negated(self, subject):
        return 'Expected {subject!r} not to {description}'.format(
            subject=subject, description=self._description(subject))


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
