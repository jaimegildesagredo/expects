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

    with it('fails if list contains fewer elements that the expected one'):
        with failure("to contain exactly 'foo' and 'bar'"):
            expect(['foo']).to(contain_exactly('foo', 'bar'))

    with it('fails if list does not contain expected item'):
        with failure("to contain exactly 'foo'"):
            expect(self.lst).to(contain_exactly('foo'))

    with it('fails if list does not contain expected items'):
        with failure("to contain exactly 'foo' and 'fuu'"):
            expect(self.lst).to(contain_exactly('foo', 'fuu'))

    with it('fails if list does not contain expected items in order'):
        with failure("to contain exactly 'baz' and 'bar'"):
            expect(self.lst).to(contain_exactly('baz', 'bar'))

    with it('fails if list not exactly has expected item'):
        with failure("to contain exactly 'bar'"):
            expect(self.lst).to(contain_exactly('bar'))

    with it('fails if list not exactly has two expected items'):
        self.lst.append('foo')

        with failure("to contain exactly 'bar' and 'baz'"):
            expect(self.lst).to(contain_exactly('bar', 'baz'))

    with it('fails if list not exactly has three expected items'):
        self.lst.extend(['foo', 'fuu'])

        with failure("to contain exactly 'bar', 'baz' and 'foo'"):
            expect(self.lst).to(contain_exactly('bar', 'baz', 'foo'))

    with it('fails if string does not exactly contain string'):
        with failure("to contain exactly 'foo'"):
            expect(self.str).to(contain_exactly('foo'))

    with it('fails if is not an iterable object'):
        with failure("to contain exactly 'bar' but is not a valid sequence type"):
            expect(object()).to(contain_exactly('bar'))

    with it('fails if list does not contain exactly matching items'):
        with failure:
            expect(self.lst).to(contain_exactly(equal('baz'), equal('baz')))
