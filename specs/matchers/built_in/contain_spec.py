# -*- coding: utf-8 -*

from expects import *
from expects.aliases import *
from expects.testing import failure


with describe('contain'):
    with before.each:
        self.lst = ['bar', 'baz']
        self.itr = iter(self.lst)
        self.str = 'My foo string'

    with it('passes if list contains item'):
        expect(self.lst).to(contain('bar'))

    with it('passes if list contains items'):
        expect(self.lst).to(contain('bar', 'baz'))

    with it('passes if list contains items in any order'):
        expect(self.lst).to(contain('baz', 'bar'))

    with it('passes if iterable of dicts contains dict'):
        # https://github.com/jaimegildesagredo/expects/issues/8

        expect([{'foo': 1}, 'bar']).to(contain({'foo': 1}))

    with it('passes if iterable contains item'):
        expect(self.itr).to(contain('bar'))

    with it('passes if iterable contains items'):
        expect(self.itr).to(contain('bar', 'baz'))

    with it('passes if string contains string'):
        expect(self.str).to(contain('foo'))

    with it('passes if string contains strings'):
        expect(self.str).to(contain('foo', 'string'))

    with it('passes if list contains a item matching'):
        expect(self.lst).to(contain(a(str)))

    with it('fails if list does not contain item'):
        with failure("to contain 'bar' and 'foo'"):
            expect(self.lst).to(contain('bar', 'foo'))

    with it('fails if iterable does not contain item'):
        with failure(end_with("to contain 'bar' and 'foo'")):
            expect(self.itr).to(contain('bar', 'foo'))

    with it('fails if is not an iterable object'):
        with failure("to contain 'bar' but is not a valid sequence type"):
            expect(object()).to(contain('bar'))

    with it('fails if list does not contain items matching'):
        with failure('contain an int and have len 5'):
            expect(self.lst).to(contain(an(int), have_len(5)))

    with context('#negated'):
        with it('passes if list does not contain item'):
            expect(self.lst).not_to(contain('foo'))

        with it('passes if list does not contain items'):
            expect(self.lst).not_to(contain('foo', 'foobar'))

        with it('passes if list contains one item and not the other'):
            expect(self.lst).not_to(contain('bar', 'foo'))

        with it('fails if list contains item'):
            with failure("not to contain 'bar'"):
                expect(self.lst).not_to(contain('bar'))

        with it('fails if list contains items'):
            with failure("not to contain 'bar' and 'baz'"):
                expect(self.lst).not_to(contain('bar', 'baz'))

        with it('fails if is not an iterable object'):
            with failure("not to contain 'bar' but is not a valid sequence type"):
                expect(object()).not_to(contain('bar'))
