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

    with it('passes if dict.keys() contains item'):
        # https://github.com/jaimegildesagredo/expects/issues/42

        expect({'bar': 0, 'baz': 1}.keys()).to(contain('bar'))

    with it('passes if dict.keys() contains item'):
        # https://github.com/jaimegildesagredo/expects/issues/42

        expect({'bar': 0, 'baz': 1}.keys()).to(contain('bar'))

    with it('passes if set contains item'):
        # https://github.com/jaimegildesagredo/expects/issues/38

        expect(set(self.lst)).to(contain('bar'))

    with it('fails if list does not contain item'):
        with failure("but: item equal 'foo' not found"):
            expect(self.lst).to(contain('bar', 'foo'))

    with it('fails if list is empty'):
        with failure("but: is empty"):
            expect([]).to(contain('foo'))

    with it('fails if iterable does not contain item'):
        with failure("but: item equal 'foo' not found"):
            expect(self.itr).to(contain('bar', 'foo'))

    with it('fails if is not an iterable object'):
        with failure("but: is not a valid sequence type"):
            expect(object()).to(contain('bar'))

    with it('fails if list does not contain items matching'):
        with failure("but: item be an int not found"):
            expect(self.lst).to(contain(be_an(int), have_len(5)))

    with it('fails if string does not contain string'):
        with failure("but: item 'bar' not found"):
            expect("My foo string").to(contain('bar'))

    with it('fails if string is empty'):
        with failure("but: is empty"):
            expect("").to(contain('foo'))

    with context('when negated'):
        with it('passes if list does not contain item'):
            expect(self.lst).not_to(contain('foo'))

        with it('passes if list does not contain items'):
            expect(self.lst).not_to(contain('foo', 'foobar'))

        with it('passes if list contains one item and not the other'):
            expect(self.lst).not_to(contain('bar', 'foo'))

        with it('fails if list contains item'):
            with failure("but: item equal 'bar' found"):
                expect(self.lst).not_to(contain('bar'))

        with it('fails if list contains items'):
            with failure("but: item equal 'bar' found\n          item equal 'baz' found"):
                expect(self.lst).not_to(contain('bar', 'baz'))

        with it('fails if string contains string'):
            with failure("but: item 'foo' found"):
                expect("My foo string").not_to(contain('foo'))

        with it('fails if is not an iterable object'):
            with failure("but: is not a valid sequence type"):
                expect(object()).not_to(contain('bar'))
