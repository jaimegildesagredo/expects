# -*- coding: utf-8 -*

from expects import *
from expects.testing import failure


with describe('contain_exactly'):
    with before.each:
        self.lst = ['bar', 'baz']
        self.itr = iter(self.lst)
        self.str = 'My foo string'

    with it('should pass if list exactly has expected item'):
        expect(['bar']).to(contain_exactly('bar'))

    with it('should pass if list exactly has expected items'):
        expect(self.lst).to(contain_exactly(*self.lst))

    with it('should passes if iterable contains item'):
        expect(self.itr).to(contain_exactly('bar', 'baz'))

    with it('should pass if string exactly contains string'):
        expect(self.str).to(contain_exactly(self.str))

    with it('should pass if string exactly contains strings'):
        expect(self.str).to(contain_exactly('My foo', ' string'))

    with it('should fail if list does not contain expected item'):
        with failure("to contain exactly 'foo'"):
            expect(self.lst).to(contain_exactly('foo'))

    with it('should fail if list does not contain expected items'):
        with failure("to contain exactly 'foo' and 'fuu'"):
            expect(self.lst).to(contain_exactly('foo', 'fuu'))

    with it('should fail if list not exactly has expected item'):
        with failure("to contain exactly 'bar'"):
            expect(self.lst).to(contain_exactly('bar'))

    with it('should fail if list not exactly has two expected items'):
        self.lst.append('foo')

        with failure("to contain exactly 'bar' and 'baz'"):
            expect(self.lst).to(contain_exactly('bar', 'baz'))

    with it('should fail if list not exactly has three expected items'):
        self.lst.extend(['foo', 'fuu'])

        with failure("to contain exactly 'bar', 'baz' and 'foo'"):
            expect(self.lst).to(contain_exactly('bar', 'baz', 'foo'))

    with it('should fail if string does not exactly contain string'):
        with failure("to contain exactly 'foo'"):
            expect(self.str).to(contain_exactly('foo'))

    with it('should fail if is not an iterable object'):
        with failure("to contain exactly 'bar' but is not a valid sequence type"):
            expect(object()).to(contain_exactly('bar'))
