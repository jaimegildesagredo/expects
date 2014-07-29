# -*- coding: utf-8 -*

from collections import OrderedDict

from expects import *
from expects.testing import failure

IRRELEVANT_ARGS = (1, 2)


with describe('end_with'):
    with before.each:
        self.str = 'My foo string'
        self.lst = [1, 2, 3]
        self.dct = {'bar': 0, 'baz': 1}
        self.ordered_dct = OrderedDict([('bar', 0), ('baz', 1)])

    with it('should pass if string ends with string'):
        expect(self.str).to(end_with(self.str[5:]))

    with it('should pass if list ends with arg'):
        expect(self.lst).to(end_with(self.lst[-1]))

    with it('should pass if list ends with args'):
        expect(self.lst).to(end_with(*self.lst[-2:]))

    with it('should pass if ordered dict ends with keys'):
        expected_args = list(self.ordered_dct)[:2]

        expect(self.ordered_dct).to(end_with(*expected_args))

    with it('should fail if string does not end with string'):
        expected = self.str[:5]

        with failure('to end with {!r}'.format(expected)):
            expect(self.str).to(end_with(expected))

    with it('should fail if list ends with first arg but not second'):
        expected_args = self.lst[-1], self.lst[-1]

        with failure('to end with {!r} and {!r}'.format(*expected_args)):
            expect(self.lst).to(end_with(*expected_args))

    with it('should fail if subject is a dict'):
        with failure('to end with {!r} and {!r} '
                     'but it does not have ordered keys'.format(*IRRELEVANT_ARGS)):

            expect(self.dct).to(end_with(*IRRELEVANT_ARGS))

    with context('#negated'):
        with it('should pass if string does not end with string'):
            expect(self.str).not_to(end_with(self.str[:5]))

        with it('should pass if list does not end with args'):
            expect(self.lst).not_to(end_with(*self.lst[:2]))

        with it('should pass if list ends with first arg but not second'):
            expected_args = self.lst[-1], self.lst[-1]

            expect(self.lst).not_to(end_with(*expected_args))

        with it('should fail if subject is a dict'):
            with failure('not to end with {!r} and {!r} '
                         'but it does not have ordered keys'.format(*IRRELEVANT_ARGS)):

                expect(self.dct).not_to(end_with(*IRRELEVANT_ARGS))
