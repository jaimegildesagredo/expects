# -*- coding: utf-8 -*

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = lambda *args: None

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
        if self.ordered_dct is None:
            return

        expected_args = list(self.ordered_dct)[:2]

        expect(self.ordered_dct).to(end_with(*expected_args))

    with it('should fail if string does not end with string'):
        str_ = 'My foo string'

        with failure('but: ends with {0!r}'.format(str_[-5:])):
            expect(self.str).to(end_with(str_[:5]))

    with it('should fail if list ends with first arg but not second'):
        with failure('but: ends with {0!r}'.format(self.lst[-2:])):
            expect(self.lst).to(end_with(self.lst[-1], self.lst[-1]))

    with it('should fail if subject is a dict'):
        with failure('but: does not have ordered keys'):
            expect(self.dct).to(end_with(*IRRELEVANT_ARGS))

    with context('when negated'):
        with it('should pass if string does not end with string'):
            expect(self.str).not_to(end_with(self.str[:5]))

        with it('should pass if list does not end with args'):
            expect(self.lst).not_to(end_with(*self.lst[:2]))

        with it('should pass if list ends with first arg but not second'):
            expected_args = self.lst[-1], self.lst[-1]

            expect(self.lst).not_to(end_with(*expected_args))

        with it('should fail if subject is a dict'):
            with failure('but: does not have ordered keys'):
                expect(self.dct).not_to(end_with(*IRRELEVANT_ARGS))
