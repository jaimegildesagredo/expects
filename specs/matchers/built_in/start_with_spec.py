# -*- coding: utf-8 -*

try:
    from collections import OrderedDict
except ImportError:
    OrderedDict = lambda *args: None

from expects import *
from expects.testing import failure

IRRELEVANT_ARGS = (1, 2)


with describe('start_with'):
    with before.each:
        self.str = 'My foo string'
        self.lst = [1, 2, 3]
        self.dct = {'bar': 0, 'baz': 1}
        self.ordered_dct = OrderedDict([('bar', 0), ('baz', 1)])

    with it('passes if string starts with string'):
        expect(self.str).to(start_with(self.str[:5]))

    with it('passes if list starts with arg'):
        expect(self.lst).to(start_with(self.lst[0]))

    with it('passes if list starts with args'):
        expect(self.lst).to(start_with(*self.lst[:2]))

    with it('passes if ordered dict starts with keys'):
        if self.ordered_dct is None:
            return

        expected_args = list(self.ordered_dct)[:2]

        expect(self.ordered_dct).to(start_with(*expected_args))

    with it('passes if iter starts with args'):
        expect(iter(self.lst)).to(start_with(*self.lst[:2]))

    with it('fails if string does not start with string'):
        with failure('but: starts with {0!r}'.format(self.str[:-5])):
            expect(self.str).to(start_with(self.str[-5:]))

    with it('fails if list does not start with arg'):
        with failure('but: starts with {0!r}'.format(self.lst[:1])):
            expect(self.lst).to(start_with(self.lst[1]))

    with it('fails if list does not start with args'):
        with failure('but: starts with {0!r}'.format(self.lst[:2])):
            expect(self.lst).to(start_with(*self.lst[1:]))

    with it('fails if list starts with first arg but not second'):
        with failure('but: starts with {0!r}'.format(self.lst[:2])):
            expect(self.lst).to(start_with(self.lst[0], self.lst[0]))

    with it('fails if actual is a dict'):
        with failure('but: does not have ordered keys'):
            expect(self.dct).to(start_with(*IRRELEVANT_ARGS))

    with context('when negated'):
        with it('passes if string does not start with string'):
            expect(self.str).not_to(start_with(self.str[5:]))

        with it('passes if list does not start with args'):
            expect(self.lst).not_to(start_with(*self.lst[2:]))

        with it('passes if list starts with first arg but not second'):
            expect(self.lst).not_to(start_with(self.lst[0], self.lst[0]))

        with it('fails if actual is a dict'):
            with failure('but: does not have ordered keys'):
                expect(self.dct).not_to(start_with(*IRRELEVANT_ARGS))
