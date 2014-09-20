# -*- coding: utf-8 -*

from collections import OrderedDict

from expects import *
from expects.testing import failure

IRRELEVANT_ARGS = (1, 2)


with describe('start_with'):
    with before.each:
        self.str = 'My foo string'
        self.lst = [1, 2, 3]
        self.dct = {'bar': 0, 'baz': 1}
        self.ordered_dct = OrderedDict([('bar', 0), ('baz', 1)])

    with it('should pass if string starts with string'):
        expect(self.str).to(start_with(self.str[:5]))

    with it('should pass if list starts with arg'):
        expect(self.lst).to(start_with(self.lst[0]))

    with it('should pass if list starts with args'):
        expect(self.lst).to(start_with(*self.lst[:2]))

    with it('should pass if ordered dict starts with keys'):
        expected_args = list(self.ordered_dct)[:2]

        expect(self.ordered_dct).to(start_with(*expected_args))

    with it('should pass if iter starts with args'):
        expect(iter(self.lst)).to(start_with(*self.lst[:2]))

    with it('should fail if string does not start with string'):
        expected = self.str[5:]

        with failure('to start with {!r}'.format(expected)):
            expect(self.str).to(start_with(expected))

    with it('should fail if list does not start with arg'):
        expected = self.lst[1]

        with failure('to start with {!r}'.format(expected)):
            expect(self.lst).to(start_with(expected))

    with it('should fail if list does not start with args'):
        expected_args = self.lst[1:]

        with failure('to start with {!r} and {!r}'.format(*expected_args)):
            expect(self.lst).to(start_with(*expected_args))

    with it('should fail if list starts with first arg but not second'):
        expected_args = self.lst[0], self.lst[0]

        with failure('to start with {!r} and {!r}'.format(*expected_args)):
            expect(self.lst).to(start_with(*expected_args))

    with it('should fail if actual is a dict'):
        with failure('to start with {!r} and {!r} '
                     'but it does not have ordered keys'.format(*IRRELEVANT_ARGS)):

            expect(self.dct).to(start_with(*IRRELEVANT_ARGS))

    with context('#negated'):
        with it('should pass if string does not start with string'):
            expect(self.str).not_to(start_with(self.str[5:]))

        with it('should pass if list does not start with args'):
            expect(self.lst).not_to(start_with(*self.lst[2:]))

        with it('should pass if list starts with first arg but not second'):
            expected_args = self.lst[0], self.lst[0]

            expect(self.lst).not_to(start_with(*expected_args))

        with it('should fail if actual is a dict'):
            with failure('not to start with {!r} and {!r} '
                         'but it does not have ordered keys'.format(*IRRELEVANT_ARGS)):

                expect(self.dct).not_to(start_with(*IRRELEVANT_ARGS))
