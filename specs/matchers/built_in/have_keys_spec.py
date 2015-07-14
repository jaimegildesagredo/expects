# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('have_keys'):
    with before.each:
        self.dct = {'bar': 0, 'baz': 1}
        self.str = 'My foo string'

    with it('passes if dict has keys in args'):
        expect(self.dct).to(have_keys('bar', 'baz'))

    with it('passes if dict has keys in kwargs'):
        expect(self.dct).to(have_keys(bar=0, baz=1))

    with it('passes if dict has keys in args and kwargs'):
        expect(self.dct).to(have_keys('bar', baz=1))

    with it('passes if dict has keys in dict'):
        expect(self.dct).to(have_keys({'bar': 0, 'baz': 1}))

    with it('fails if dict does not have key in args'):
        with failure("to have keys 'bar' and 'foo'"):
            expect(self.dct).to(have_keys('bar', 'foo'))

    with it('fails if dict does not have key in kwargs'):
        with failure("to have keys 'bar' equal 0 and 'foo' equal 1"):
            expect(self.dct).to(have_keys(bar=0, foo=1))

    with it('fails if dict has key without value in kwargs'):
        with failure("to have keys 'bar' equal 1 and 'baz' equal 1"):
            expect(self.dct).to(have_keys(bar=1, baz=1))

    with it('fails if dict does not have key in args but in kwargs'):
        with failure("to have keys 'foo', 'fuu' and 'bar' equal 0"):
            expect(self.dct).to(have_keys('foo', 'fuu', bar=0))

    with it('fails if dict has key in args and kwargs without value'):
        with failure("to have keys 'baz' and 'bar' equal 1"):
            expect(self.dct).to(have_keys('baz', bar=1))

    with it('fails if dict has key without value in dict'):
        with failure("to have keys 'bar' equal 1 and 'baz' equal 1"):
            expect(self.dct).to(have_keys({'bar': 1, 'baz': 1}))

    with it('fails if actual is not a dict'):
        # issue-10

        with failure("to have keys 'bar' equal 1 and 'baz' equal 1 but is not a dict"):
            expect(self.str).to(have_keys({'bar': 1, 'baz': 1}))

    with context('#negated'):
        with it('passes if dict does not have keys in args'):
            expect(self.dct).not_to(have_keys('foo', 'foobar'))

        with it('passes if dict does not have keys in kwargs'):
            expect(self.dct).not_to(have_keys(foo=0, foobar=1))

        with it('passes if dict has key without value in kwargs'):
            expect(self.dct).to_not(have_keys(foo=0, bar=1))

        with it('passes if dict does not have keys in dict'):
            expect(self.dct).to_not(have_keys({'foo': 0, 'foobar': 1}))

        with it('passes if dict has one key and not the other in args'):
            expect(self.dct).not_to(have_keys('foo', 'bar'))

        with it('fails if dict has keys in args'):
            with failure("not to have keys 'bar' and 'baz'"):
                expect(self.dct).to_not(have_keys('bar', 'baz'))

        with it('fails if dict has keys in kwargs'):
            with failure("not to have keys 'bar' equal 0 and 'baz' equal 1"):
                expect(self.dct).not_to(have_keys(bar=0, baz=1))

        with it('fails if actual is not a dict'):
            # issue-10

            with failure("not to have keys 'bar' equal 1 and 'baz' equal 1 but is not a dict"):
                expect(self.str).not_to(have_keys({'bar': 1, 'baz': 1}))
