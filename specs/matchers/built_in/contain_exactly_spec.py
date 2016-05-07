# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('contain_exactly'):
    with before.each:
        self.lst = ['bar', 'baz']
        self.itr = iter(self.lst)
        self.str = 'My foo string'

    with it('passes if list exactly has expected item'):
        expect(['bar']).to(contain_exactly('bar'))

    with it('passes if list exactly has expected items'):
        expect(self.lst).to(contain_exactly(*self.lst))

    with it('passes if list contains exactly matching items'):
        expect(self.lst).to(contain_exactly(equal('bar'), equal('baz')))

    with it('passes if iterable contains item'):
        expect(self.itr).to(contain_exactly('bar', 'baz'))

    with it('passes if string exactly contains string'):
        expect(self.str).to(contain_exactly(self.str))

    with it('passes if string exactly contains strings'):
        expect(self.str).to(contain_exactly('My foo', ' string'))

    with it('passes if dict.keys() exactly contains item'):
        # https://github.com/jaimegildesagredo/expects/issues/42

        expect({'bar': 0}.keys()).to(contain_exactly('bar'))

    with it('passes if set exactly contains items'):
        # https://github.com/jaimegildesagredo/expects/issues/38

        expect(set(['bar'])).to(contain_exactly('bar'))

    with it('fails if list contains fewer elements that the expected one'):
        with failure("but: item equal 'bar' not found at index 1"):
            expect(['foo']).to(contain_exactly('foo', 'bar'))

    with it('fails if list does not contain expected item'):
        with failure("but: item equal 'foo' not found at index 0"):
            expect(self.lst).to(contain_exactly('foo'))

    with it('fails if list does not contain expected items'):
        with failure("but: item equal 'foo' not found at index 0"):
            expect(self.lst).to(contain_exactly('foo', 'fuu'))

    with it('fails if list does not contain expected items in order'):
        with failure("but: item equal 'baz' not found at index 0"):
            expect(self.lst).to(contain_exactly('baz', 'bar'))

    with it('fails if list has the given item and more'):
        with failure("but: have a different length"):
            expect(self.lst).to(contain_exactly('bar'))

    with it('fails if list has the given items and more'):
        self.lst.append('foo')

        with failure("but: have a different length"):
            expect(self.lst).to(contain_exactly('bar', 'baz'))

    with it('fails if string does not exactly contain string'):
        with failure("item equal 'foo' not found at index 0"):
            expect(self.str).to(contain_exactly('foo'))

    with it('fails if string contains first item but not second'):
        with failure("item equal 'bar' not found at index 2"):
            expect(self.str).to(contain_exactly('My', 'bar'))

    with it('fails if string contains item and more'):
        with failure("but: have a different length"):
            expect(self.str).to(contain_exactly('My'))

    with it('fails if is not a valid sequence type'):
        with failure("but: is not a valid sequence type"):
            expect(object()).to(contain_exactly('bar'))

    with it('fails if list does not contain exactly matching items'):
        with failure("but: item be an int not found at index 0"):
            expect(self.lst).to(contain_exactly(be_an(int)))

    with context('when negated'):
        with it('fails when list contains exactly items'):
            with failure("item equal {0!r} found at index 1".format(self.lst[1])):
                expect(self.lst).not_to(contain_exactly(*self.lst))

        with it('fails when string contains exactly string'):
            with failure("item equal {0!r} found at index 0".format(self.str)):
                expect(self.str).not_to(contain_exactly(self.str))
